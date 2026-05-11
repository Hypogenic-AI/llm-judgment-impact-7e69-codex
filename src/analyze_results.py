#!/usr/bin/env python3
"""Analyze judgment-pressure experiment outputs and generate report artifacts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import shapiro, ttest_rel, wilcoxon
from statsmodels.stats.contingency_tables import mcnemar
from statsmodels.stats.multitest import multipletests


ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = ROOT / "results"
SUMMARY_DIR = RESULTS_DIR / "summaries"
FIG_DIR = ROOT / "figures"

CONDITION_ORDER = [
    "neutral",
    "mild_skeptical_question",
    "strong_judgment_question",
    "strong_judgment_statement",
]


def ensure_dirs() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)


def bootstrap_mean_ci(values: np.ndarray, n_boot: int = 5000, seed: int = 42) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    samples = rng.choice(values, size=(n_boot, len(values)), replace=True).mean(axis=1)
    return float(np.percentile(samples, 2.5)), float(np.percentile(samples, 97.5))


def cohens_d_paired(values: np.ndarray) -> float:
    std = np.std(values, ddof=1)
    if std == 0 or np.isnan(std):
        return 0.0
    return float(np.mean(values) / std)


def run_paired_tests(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    valid_df = df[df["is_correct"].notna()].copy()
    for (model, dataset, hint_condition), sub_df in valid_df.groupby(["model", "dataset", "hint_condition"]):
        neutral = sub_df[sub_df["condition"] == "neutral"].set_index("example_id")
        for condition in CONDITION_ORDER[1:]:
            comp = sub_df[sub_df["condition"] == condition].set_index("example_id")
            aligned = neutral.join(
                comp[["is_correct", "followed_hint", "confidence", "rationale_word_count"]],
                lsuffix="_neutral",
                rsuffix=f"_{condition}",
                how="inner",
            )
            if aligned.empty:
                continue

            accuracy_delta = (
                aligned[f"is_correct_{condition}"] - aligned["is_correct_neutral"]
            ).to_numpy()
            rationale_delta = (
                aligned[f"rationale_word_count_{condition}"] - aligned["rationale_word_count_neutral"]
            ).to_numpy()
            confidence_delta = (
                aligned[f"confidence_{condition}"] - aligned["confidence_neutral"]
            ).dropna().to_numpy()
            hint_delta = (
                aligned[f"followed_hint_{condition}"] - aligned["followed_hint_neutral"]
            ).to_numpy()

            table = [
                [
                    int(((aligned["is_correct_neutral"] == 1) & (aligned[f"is_correct_{condition}"] == 1)).sum()),
                    int(((aligned["is_correct_neutral"] == 1) & (aligned[f"is_correct_{condition}"] == 0)).sum()),
                ],
                [
                    int(((aligned["is_correct_neutral"] == 0) & (aligned[f"is_correct_{condition}"] == 1)).sum()),
                    int(((aligned["is_correct_neutral"] == 0) & (aligned[f"is_correct_{condition}"] == 0)).sum()),
                ],
            ]
            if table[0][1] + table[1][0] == 0:
                mc_p = 1.0
            else:
                mc_p = float(mcnemar(table, exact=False, correction=True).pvalue)
            acc_ci_low, acc_ci_high = bootstrap_mean_ci(accuracy_delta)

            rationale_p = np.nan
            rationale_test = "wilcoxon"
            if len(rationale_delta) >= 3 and shapiro(rationale_delta).pvalue > 0.05:
                rationale_test = "paired_t"
                rationale_p = ttest_rel(
                    aligned[f"rationale_word_count_{condition}"],
                    aligned["rationale_word_count_neutral"],
                    nan_policy="omit",
                ).pvalue
            elif len(rationale_delta) >= 1 and np.any(rationale_delta != 0):
                rationale_p = wilcoxon(rationale_delta).pvalue

            confidence_p = np.nan
            confidence_test = "wilcoxon"
            if len(confidence_delta) >= 3 and shapiro(confidence_delta).pvalue > 0.05:
                confidence_test = "paired_t"
                confidence_p = ttest_rel(
                    aligned[f"confidence_{condition}"],
                    aligned["confidence_neutral"],
                    nan_policy="omit",
                ).pvalue
            elif len(confidence_delta) >= 1 and np.any(confidence_delta != 0):
                confidence_p = wilcoxon(confidence_delta).pvalue

            rows.append(
                {
                    "model": model,
                    "dataset": dataset,
                    "hint_condition": hint_condition,
                    "comparison": f"{condition}_vs_neutral",
                    "n": len(aligned),
                    "accuracy_delta_mean": float(np.mean(accuracy_delta)),
                    "accuracy_ci_low": acc_ci_low,
                    "accuracy_ci_high": acc_ci_high,
                    "accuracy_mcnemar_p": mc_p,
                    "accuracy_effect_size_d": cohens_d_paired(accuracy_delta),
                    "hint_follow_delta_mean": float(np.mean(hint_delta)),
                    "confidence_delta_mean": float(np.mean(confidence_delta)) if len(confidence_delta) else np.nan,
                    "confidence_test": confidence_test,
                    "confidence_p": confidence_p,
                    "rationale_word_delta_mean": float(np.mean(rationale_delta)),
                    "rationale_test": rationale_test,
                    "rationale_p": rationale_p,
                }
            )

    stats_df = pd.DataFrame(rows)
    if not stats_df.empty:
        for col in ["accuracy_mcnemar_p", "confidence_p", "rationale_p"]:
            mask = stats_df[col].notna()
            if mask.any():
                stats_df.loc[mask, f"{col}_fdr"] = multipletests(stats_df.loc[mask, col], method="fdr_bh")[1]
    return stats_df


def build_error_cases(df: pd.DataFrame) -> pd.DataFrame:
    valid_df = df[df["is_correct"].notna()].copy()
    neutral = valid_df[valid_df["condition"] == "neutral"][
        ["model", "dataset", "hint_condition", "example_id", "is_correct", "predicted_answer", "raw_response"]
    ].rename(
        columns={
            "is_correct": "neutral_correct",
            "predicted_answer": "neutral_prediction",
            "raw_response": "neutral_response",
        }
    )
    merged = valid_df.merge(
        neutral,
        on=["model", "dataset", "hint_condition", "example_id"],
        how="left",
    )
    cases = merged[
        (merged["condition"] != "neutral")
        & (merged["is_correct"] != merged["neutral_correct"])
    ].copy()
    return cases.sort_values(["model", "dataset", "hint_condition", "condition", "example_id"])


def save_plots(summary: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid")

    obj = summary[summary["hint_condition"] == "no_hint"].copy()
    plt.figure(figsize=(12, 6))
    sns.barplot(
        data=obj,
        x="dataset",
        y="accuracy",
        hue="condition",
        order=sorted(obj["dataset"].unique()),
        hue_order=CONDITION_ORDER,
    )
    plt.ylim(0, 1)
    plt.title("Objective Accuracy by Prompt Condition")
    plt.ylabel("Accuracy")
    plt.xlabel("Dataset")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "accuracy_by_condition.png", dpi=200)
    plt.close()

    hinted = summary[summary["hint_condition"] == "misleading_wrong_hint"].copy()
    if not hinted.empty:
        plt.figure(figsize=(12, 6))
        sns.barplot(
            data=hinted,
            x="dataset",
            y="hint_follow_rate",
            hue="condition",
            order=sorted(hinted["dataset"].unique()),
            hue_order=CONDITION_ORDER,
        )
        plt.ylim(0, 1)
        plt.title("Wrong-Hint Agreement Rate by Prompt Condition")
        plt.ylabel("Wrong-Hint Agreement Rate")
        plt.xlabel("Dataset")
        plt.tight_layout()
        plt.savefig(FIG_DIR / "hint_follow_rate.png", dpi=200)
        plt.close()

        plt.figure(figsize=(12, 6))
        sns.barplot(
            data=hinted,
            x="dataset",
            y="accuracy",
            hue="condition",
            order=sorted(hinted["dataset"].unique()),
            hue_order=CONDITION_ORDER,
        )
        plt.ylim(0, 1)
        plt.title("Accuracy Under Misleading User Hints")
        plt.ylabel("Accuracy")
        plt.xlabel("Dataset")
        plt.tight_layout()
        plt.savefig(FIG_DIR / "accuracy_with_hints.png", dpi=200)
        plt.close()

    plt.figure(figsize=(12, 6))
    sns.barplot(
        data=summary,
        x="dataset",
        y="mean_rationale_words",
        hue="condition",
        order=sorted(summary["dataset"].unique()),
        hue_order=CONDITION_ORDER,
    )
    plt.title("Mean Rationale Length by Prompt Condition")
    plt.ylabel("Mean Rationale Words")
    plt.xlabel("Dataset")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "rationale_length.png", dpi=200)
    plt.close()


def main() -> None:
    ensure_dirs()
    df = pd.read_csv(SUMMARY_DIR / "judgment_eval_raw.csv")
    summary = pd.read_csv(SUMMARY_DIR / "condition_summary.csv")
    stats_df = run_paired_tests(df)
    stats_df.to_csv(SUMMARY_DIR / "paired_stats.csv", index=False)

    cases = build_error_cases(df)
    cases.to_csv(SUMMARY_DIR / "changed_outcomes.csv", index=False)

    save_plots(summary)

    narrative = {
        "models": sorted(df["model"].unique().tolist()),
        "datasets": sorted(df["dataset"].unique().tolist()),
        "n_total_responses": int(len(df)),
        "n_unique_examples": int(df["example_id"].nunique()),
        "mean_accuracy_overall": float(df["is_correct"].mean()),
    }
    (SUMMARY_DIR / "analysis_overview.json").write_text(json.dumps(narrative, indent=2))


if __name__ == "__main__":
    main()
