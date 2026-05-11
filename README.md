# Judgment Pressure in LLMs

This project tests whether skeptical or judgmental user tone changes LLM reasoning quality, not just style. On 2026-05-11, it ran 1,600 real OpenAI API calls across `gpt-4.1` and `gpt-4.1-mini` on GSM8K, CommonsenseQA, and TruthfulQA-MC with controlled tone variants and misleading-hint conditions.

Key findings:
- `gpt-4.1` showed a small pooled no-hint gain under mild skeptical questioning: `+5.0` accuracy points vs neutral.
- Harsher judgment did not improve further and often only lengthened rationales.
- Under misleading hints, the mild-skepticism gain disappeared or reversed on `gpt-4.1`.
- Wrong-hint agreement stayed low overall, so the main failure mode was overthinking rather than overt sycophancy.
- Apology markers were `0/1600` across all conditions.

Reproduce:
```bash
source .venv/bin/activate
python src/run_experiments.py --gsm8k-n 40 --commonsenseqa-n 40 --truthfulqa-n 40 --models gpt-4.1 gpt-4.1-mini --concurrency 8
python src/analyze_results.py
```

File structure:
- [REPORT.md](/workspaces/llm-judgment-impact-7e69-codex/REPORT.md): full methodology, results, and interpretation
- [planning.md](/workspaces/llm-judgment-impact-7e69-codex/planning.md): preregistered research plan
- [prompts/judgment_conditions.json](/workspaces/llm-judgment-impact-7e69-codex/prompts/judgment_conditions.json): exact prompt prefixes
- [src/run_experiments.py](/workspaces/llm-judgment-impact-7e69-codex/src/run_experiments.py): API runner
- [src/analyze_results.py](/workspaces/llm-judgment-impact-7e69-codex/src/analyze_results.py): statistical analysis and plotting
- [results/summaries](/workspaces/llm-judgment-impact-7e69-codex/results/summaries): tables and intermediate artifacts
- [figures](/workspaces/llm-judgment-impact-7e69-codex/figures): output plots
