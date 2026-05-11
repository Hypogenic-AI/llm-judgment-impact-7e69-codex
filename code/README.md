# Cloned Repositories

## Repo 1: lm-evaluation-harness
- URL: https://github.com/EleutherAI/lm-evaluation-harness
- Commit: `6632cb78`
- Purpose: broad benchmark harness for academic LLM evaluation
- Location: `code/lm-evaluation-harness/`
- Key entry points: `lm_eval/tasks/`, `docs/interface.md`, `docs/config_files.md`
- Notes: supports 60+ benchmarks, API and local-model backends, and recent options for stripping reasoning traces with `think_end_token`

## Repo 2: simple-evals
- URL: https://github.com/openai/simple-evals
- Commit: `652c89d`
- Purpose: lightweight reference evals with zero-shot CoT-style prompting
- Location: `code/simple-evals/`
- Key entry points: `simple-evals/simple_evals.py`, `README.md`
- Notes: deprecated for new additions as of July 2025, but still useful as a small reference implementation for MMLU, MATH, GPQA, MGSM, DROP, and SimpleQA-style runs

## Repo 3: chain-of-thought-hub
- URL: https://github.com/FranxYao/chain-of-thought-hub
- Commit: `461e2d5`
- Purpose: curated reasoning-benchmark collection emphasizing CoT evaluation
- Location: `code/chain-of-thought-hub/`
- Key entry points: `gsm8k/`, `MMLU/`, `BBH/`, `readme.md`
- Notes: useful for benchmark selection and prompt templates when comparing reasoning-sensitive tasks

## Repo 4: sycophancy-intervention
- URL: https://github.com/google/sycophancy-intervention
- Commit: `fb75986`
- Purpose: synthetic-data and evaluation pipeline for sycophancy reduction
- Location: `code/sycophancy-intervention/`
- Key entry points: `code/dataset_pipeline.py`, `code/generate_data.py`, `code/pull_from_huggingface.py`
- Notes: especially useful for generating controlled persona-plus-belief prompts and synthetic eval data

## Practical Reuse

- Use `lm-evaluation-harness` as the main runner for reproducible benchmark evaluation.
- Use `simple-evals` as a compact baseline for zero-shot CoT prompt formatting.
- Use `chain-of-thought-hub` to expand from the three downloaded datasets to MMLU, BBH, and MATH.
- Use `sycophancy-intervention` to build controlled “user belief” or “user certainty” manipulations aligned with the hypothesis.
