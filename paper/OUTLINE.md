# Outline: Do LLMs Think Better or Worse When Being "Judged"?

## Title
- When Being "Judged" Helps and Hurts: Mild Skepticism Can Improve LLM Accuracy, but Harsh Prompting Mostly Increases Volatility

## Abstract
- Frame prompt tone as a cheap but under-tested intervention.
- State the gap: prior work studies politeness, emotion, and sycophancy, but not a clean judgment-pressure ladder on objective benchmarks.
- Summarize the design: 1,600 API calls, two OpenAI models, three datasets, four tone conditions, with and without misleading hints.
- Report the key result: mild skepticism improves pooled no-hint accuracy for `gpt-4.1` by +5.0 points over neutral; harsher prompts increase rationale length more reliably than accuracy.
- Close with the practical implication: mild skepticism is a fragile sweet spot, not a general recipe.

## Introduction
- Hook: users constantly change tone when prompting models; the field lacks evidence on whether "judging" helps.
- Importance: product UX, benchmark design, and safety evaluations depend on this being understood.
- Gap: existing work treats politeness, emotion, or sycophancy separately.
- Approach: repeated-measures benchmark with tone-only interventions and misleading-hint stress test.
- Quantitative preview: +5.0 points for `gpt-4.1` under mild skepticism, no corresponding gain under hints, zero apology markers across 1,600 responses.
- Contributions:
  - We define a compact judgment-pressure ladder.
  - We run paired experiments on objective and suggestibility-sensitive tasks.
  - We show output length shifts are more robust than accuracy shifts.
  - We identify overcorrection rather than direct sycophancy as the main failure mode.

## Related Work
- Theme 1: prompt politeness and tone effects.
- Theme 2: emotional framing and adaptive prompt selection.
- Theme 3: sycophancy and framing-induced agreement.
- Theme 4: reasoning traces, self-correction, and explanation faithfulness.
- Positioning: unlike prior work, combine objective accuracy and misleading-hint conformity under matched judgment prompts.

## Methodology
- Task: evaluate tone effects on accuracy, rationale length, confidence, and hint agreement.
- Models, datasets, sample sizes, API settings, prompt conditions.
- Baselines: neutral plus three stronger judgment variants.
- Hint manipulation: content-preserving wrong-answer hint on CSQA and TruthfulQA.
- Metrics and statistical tests: exact match / label accuracy, bootstrap CIs, McNemar, paired tests with FDR.
- Reproducibility and cost details.

## Results
- Table 1: pooled no-hint accuracy, rationale length, confidence by model and condition.
- Table 2: misleading-hint results with wrong-hint agreement.
- Figure references for pooled accuracy, hint accuracy, wrong-hint agreement, rationale length.
- Dataset-level analysis: CSQA gains for `gpt-4.1`, GSM8K losses for `gpt-4.1-mini`.
- Statistical interpretation: rationale differences survive correction more often than accuracy.

## Discussion
- Interpret the "sweet spot" as weak and model-dependent.
- Explain why this is not straightforward sycophancy.
- Discuss representative success and failure cases from the report.
- State limitations: two models, modest sample sizes, benchmark contamination, rationale visibility, phrasing family.
- Broader implications for UX, eval design, and adversarial prompting.

## Conclusion
- Summarize contribution and takeaways.
- Emphasize that harsh judging is not a reliable tool for better reasoning.
- List clear future work directions: more models, larger samples, non-social controls, richer failure annotations.

## Tables and Figures
- `tables/pooled_no_hint.tex`
- `tables/misleading_hint.tex`
- `tables/dataset_patterns.tex`
- `figures/accuracy_by_condition.png`
- `figures/accuracy_with_hints.png`
- `figures/hint_follow_rate.png`
- `figures/rationale_length.png`

## Citation Plan
- Tone/politeness: Yin et al. (2024), Dobariya and Kumar (2025), Zhao et al. (2026)
- Sycophancy/framing: Dubois et al. (2026), Ranaldi and Pucci (2023)
- Reasoning baselines and failure analysis: Wei et al. (2022), Fu et al. (2023), Turpin et al. (2023), Huang et al. (2024)
