# Resources Catalog

## Summary

This document catalogs papers, datasets, and code repositories gathered for the project `Do LLMs think better / longer (or maybe even worse) when being "judged"?`

## Papers

Total papers downloaded: 9

| Title | Authors | Year | File | Key Info |
|---|---|---:|---|---|
| Should We Respect LLMs? | Yin et al. | 2024 | `papers/2402.14531_should_we_respect_llms.pdf` | Cross-lingual politeness study; non-monotonic effects |
| Mind Your Tone | Dobariya, Kumar | 2025 | `papers/2510.04950_mind_your_tone.pdf` | Small direct study; rude prompts slightly outperform polite ones |
| Do Emotions in Prompts Matter? | Zhao et al. | 2026 | `papers/2604.02236_do_emotions_in_prompts_matter.pdf` | Emotional framing usually has small, task-dependent effects |
| Ask don't tell | Dubois et al. | 2026 | `papers/2602.23971_ask_dont_tell.pdf` | Question-vs-statement framing strongly affects sycophancy |
| LLMs' Sycophantic Behaviour | Ranaldi, Pucci | 2023 | `papers/2311.09410_llm_sycophantic_behaviour.pdf` | User hints bias subjective tasks more than math |
| Chain-of-Thought Prompting | Wei et al. | 2022 | `papers/2201.11903_chain_of_thought_prompting.pdf` | Canonical reasoning-prompt baseline |
| Chain-of-Thought Hub | Fu et al. | 2023 | `papers/2305.17306_chain_of_thought_hub.pdf` | Benchmark curation for reasoning-focused evals |
| Unfaithful CoT Explanations | Turpin et al. | 2023 | `papers/2305.04388_unfaithful_cot_explanations.pdf` | Reasoning traces can rationalize biased answers |
| Cannot Self-Correct Reasoning Yet | Huang et al. | 2024 | `papers/2310.01798_cannot_self_correct_reasoning_yet.pdf` | More reflection can degrade reasoning without feedback |

See `papers/README.md` for detailed descriptions.

## Datasets

Total datasets downloaded: 3

| Name | Source | Size | Task | Location | Notes |
|---|---|---|---|---|---|
| GSM8K | Hugging Face `gsm8k/main` | 7,473 train / 1,319 test | Math reasoning | `datasets/gsm8k/` | Strong objective benchmark |
| CommonsenseQA | Hugging Face `tau/commonsense_qa` | 9,741 train / 1,221 val / 1,140 test | Commonsense MCQ | `datasets/commonsense_qa/` | Useful for ambiguity-sensitive reasoning |
| TruthfulQA MC | Hugging Face `truthful_qa/multiple_choice` | 817 validation | Truthfulness / suggestibility | `datasets/truthful_qa_mc/` | Good for conformity-vs-truth tension |

See `datasets/README.md` for loading and download instructions.

## Code Repositories

Total repositories cloned: 4

| Name | URL | Purpose | Location | Notes |
|---|---|---|---|---|
| lm-evaluation-harness | https://github.com/EleutherAI/lm-evaluation-harness | Main evaluation harness | `code/lm-evaluation-harness/` | Broadest reusable benchmark runner |
| simple-evals | https://github.com/openai/simple-evals | Compact reference eval implementation | `code/simple-evals/` | Good small baseline for zero-shot CoT style runs |
| chain-of-thought-hub | https://github.com/FranxYao/chain-of-thought-hub | Reasoning benchmark curation | `code/chain-of-thought-hub/` | Useful for adding MMLU, BBH, MATH |
| sycophancy-intervention | https://github.com/google/sycophancy-intervention | Synthetic sycophancy data generation | `code/sycophancy-intervention/` | Helpful for controlled belief-framing prompts |

See `code/README.md` for key entry points.

## Resource Gathering Notes

### Search Strategy

The initial plan was to use the local `paper-finder` helper. On 2026-05-11 it was unavailable because the expected localhost service was not running, so literature search fell back to manual arXiv querying plus targeted web search for repository discovery. Selection focused on three clusters: prompt tone and politeness, sycophancy / user-pressure effects, and reasoning-baseline papers needed for experiment design.

### Selection Criteria

- Direct match to tone, judgment, or user-pressure framing
- Strong relevance to reasoning accuracy or answer faithfulness
- Public availability of PDFs and code
- Practical utility for follow-on experiments

### Challenges Encountered

- `paper-finder` backend unavailable locally
- Semantic Scholar API returned HTTP 429 for unauthenticated queries
- The fresh `uv add` setup initially failed because the workspace was not a Python package; this was fixed by setting `[tool.uv] package = false` in `pyproject.toml`

### Gaps and Workarounds

- No single established “judgment prompt” benchmark was found; the closest proxies are politeness, emotional framing, and sycophancy framing
- No dedicated codebase for the exact hypothesis was found, so the experiment runner should combine general eval harnesses with custom prompt templates

## Recommendations for Experiment Design

1. Primary datasets: `gsm8k`, `commonsense_qa`, and `truthful_qa_mc`
2. Baseline methods: neutral prompt, zero-shot CoT, rude prompt, skeptical-question prompt, skeptical-statement prompt, and question-reframing anti-sycophancy prompt
3. Evaluation metrics: exact-match accuracy, agreement-with-misleading-hint rate, sycophancy score, and spot-checked explanation faithfulness
4. Code to adapt or reuse: use `code/lm-evaluation-harness/` as the main runner, `code/simple-evals/` as a compact reference, `code/chain-of-thought-hub/` for benchmark extensions, and `code/sycophancy-intervention/` for synthetic belief/persona manipulations

## Execution Notes

- On 2026-05-11, the research execution used the local datasets above with custom API-based evaluation scripts in `src/run_experiments.py` and `src/analyze_results.py`.
- Models tested: `gpt-4.1` and `gpt-4.1-mini` through the OpenAI Chat Completions API.
- Artifacts produced:
  - Raw outputs: `results/model_outputs/judgment_eval_raw.json`
  - Flat CSV export: `results/summaries/judgment_eval_raw.csv`
  - Aggregate tables: `results/summaries/condition_summary.csv`, `results/summaries/paired_stats.csv`
  - Error slices: `results/summaries/changed_outcomes.csv`
  - Figures: `figures/accuracy_by_condition.png`, `figures/accuracy_with_hints.png`, `figures/hint_follow_rate.png`, `figures/rationale_length.png`
