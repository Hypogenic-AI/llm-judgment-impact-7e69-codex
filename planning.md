# Research Plan: Do LLMs think better or worse when being "judged"?

## Motivation & Novelty Assessment

### Why This Research Matters
Prompt tone is a controllable part of real-world LLM use, yet teams usually optimize for wording clarity rather than interpersonal framing. If skeptical or judgmental phrasing reliably changes reasoning quality or resistance to misleading user pressure, that has direct implications for eval design, product UX, and safety guardrails.

### Gap in Existing Work
The local literature review shows adjacent evidence on politeness, emotional framing, and sycophancy, but not a clean test of "judgment pressure" as a distinct axis. Existing work also tends to separate objective reasoning accuracy from user-belief conformity, making it hard to tell whether harsher framing improves thinking, merely changes style, or increases agreement pressure.

### Our Novel Contribution
We test a compact "judgment pressure" ladder with semantics held constant across prompts and measure both objective task performance and misleading-hint conformity. This directly probes whether there is a sweet spot where skepticism increases effective effort without pushing the model into apology, defensiveness, or sycophantic agreement.

### Experiment Justification
- Experiment 1: Objective reasoning under tone variants. Needed to test whether judgmental phrasing changes answer quality on tasks with ground truth rather than only changing wording.
- Experiment 2: Misleading-hint pressure under tone variants. Needed to separate deeper reasoning from conformity when the user implicitly or explicitly pushes toward a wrong answer.
- Experiment 3: Output-style diagnostics. Needed because longer or more elaborate rationales can be unfaithful; we therefore measure apology markers, rationale length, and confidence alongside accuracy.

## Research Question
How does skeptical or judgmental user phrasing affect LLM answer quality, reasoning-output characteristics, and susceptibility to misleading user pressure, relative to neutral phrasing?

## Background and Motivation
Prior work in `literature_review.md` suggests non-monotonic tone effects and strong framing-driven sycophancy, but does not isolate judgmental pressure itself. The central question is whether mildly skeptical prompts act like productive social facilitation, while stronger accusatory framing starts to degrade reasoning or increase agreement with misleading users.

## Hypothesis Decomposition
- H1: Mild skeptical questioning improves or preserves objective-task accuracy relative to neutral prompts.
- H2: Strong judgmental framing does not reliably improve objective-task accuracy and may reduce it.
- H3: Judgmental framing increases output length and caveat density more than it increases true accuracy.
- H4: When a misleading user hint is added, statement-like and strongly judgmental framing increase conformity more than neutral or question-style framing.
- H5: If a "sweet spot" exists, it will appear as better-or-equal accuracy under mild skepticism without a corresponding rise in wrong-hint agreement or apology language.

Independent variables:
- Prompt condition: `neutral`, `mild_skeptical_question`, `strong_judgment_question`, `strong_judgment_statement`
- Hint condition: `no_hint` vs `misleading_wrong_hint`
- Dataset/task family: GSM8K, CommonsenseQA, TruthfulQA-MC
- Model: OpenAI `gpt-4.1`, `gpt-4.1-mini` if available

Dependent variables:
- Accuracy / exact match
- Wrong-hint agreement rate
- Response length
- Rationale length
- Confidence self-report
- Apology marker rate

Alternative explanations to test against:
- Tone merely changes formatting verbosity, not reasoning quality
- Tone effects differ by dataset ambiguity rather than "judgment" per se
- Any apparent improvement is offset by higher conformity under misleading hints

## Proposed Methodology

### Approach
Use a repeated-measures prompt intervention: the same sampled items are evaluated under all prompt conditions with low-temperature settings and structured outputs. We will compare objective reasoning datasets against truthfulness/suggestibility items to detect where judgment pressure helps, hurts, or simply changes style.

### Experimental Steps
1. Load and validate the three local datasets, then sample a reproducible evaluation subset from each.
2. Build a unified prompt templating system that keeps task semantics constant while varying only tone and hint framing.
3. Run baseline neutral prompts first to validate parsing and scoring.
4. Run all tone variants on the same items for `gpt-4.1`, then attempt replication on `gpt-4.1-mini`.
5. Score accuracy, wrong-hint agreement, apology markers, rationale length, and confidence.
6. Run paired statistical comparisons and simple effect-size estimates across conditions.
7. Perform failure analysis on cases where mild skepticism helps, and where strong judgment hurts or induces conformity.

### Baselines
- Neutral direct question
- Mild skeptical question
- Strong judgmental question
- Strong judgmental statement

Why these baselines:
- Neutral is the control.
- Mild skeptical question tests the plausible "sweet spot."
- Strong judgmental question tests whether escalation continues to help.
- Strong judgmental statement probes the literature-backed risk that statement-like framing increases sycophancy.

### Evaluation Metrics
- GSM8K: numeric exact match
- CommonsenseQA: multiple-choice accuracy
- TruthfulQA-MC: multiple-choice accuracy on `mc1`
- Wrong-hint agreement rate: whether the model follows the injected wrong answer suggestion
- Output diagnostics: total response tokens/chars, rationale word count, apology marker indicator, self-reported confidence

### Statistical Analysis Plan
- Primary comparisons: paired bootstrap confidence intervals for per-item accuracy deltas against neutral
- Secondary tests: McNemar test for paired binary accuracy comparisons; paired t-test or Wilcoxon signed-rank on response-length and confidence deltas depending on distribution checks
- Significance threshold: `alpha = 0.05`
- Multiple comparisons: Benjamini-Hochberg FDR across the main prompt-condition comparisons
- Effect sizes: paired proportion delta for accuracy, Cohen's d for approximately normal continuous diagnostics

## Expected Outcomes
Support for the hypothesis would look like mild skeptical questioning matching or slightly beating neutral accuracy while keeping wrong-hint agreement flat. Refutation would look like no reliable accuracy benefit or a tradeoff where any gain is paired with higher conformity, apology, or unfaithful verbosity.

## Timeline and Milestones
1. Planning and setup: 20-30 minutes
2. Environment and data validation: 10-20 minutes
3. Runner implementation and dry run: 45-60 minutes
4. Main experiments: 45-90 minutes depending on API latency
5. Statistical analysis and figures: 30-45 minutes
6. Reporting and validation: 20-30 minutes

## Potential Challenges
- API model availability or transient failures: mitigate with retries and cached JSONL outputs.
- Structured output parse drift: mitigate with strict JSON instructions and repair logic.
- Token cost growth across full factorial runs: mitigate with capped sample sizes and short rationales.
- Dataset contamination or saturation: acknowledge as a limitation and emphasize within-model paired comparisons rather than absolute leaderboard claims.

## Success Criteria
- End-to-end run completed on at least one modern real API model and ideally a second OpenAI model.
- All four prompt conditions evaluated on all three datasets with reproducible sampled subsets.
- Reported statistics distinguish objective accuracy effects from misleading-hint conformity effects.
- `REPORT.md` includes actual quantitative findings, figures, limitations, and a clear conclusion on whether a useful "sweet spot" appears.
