# Literature Review: Do LLMs think better or worse when being "judged"?

## Review Scope

### Research Question

Does skeptical, judgmental, rude, or emotionally charged prompt framing change LLM reasoning quality, and if so, does it help by increasing effort or hurt by increasing sycophancy, defensiveness, or unfaithful rationalization?

### Inclusion Criteria

- Papers on prompt tone, politeness, emotional framing, or user-belief framing in LLMs
- Papers on sycophancy, suggestibility, or user-pressure effects
- Papers on reasoning prompt baselines or failure modes needed to interpret tone effects
- Mostly 2023-2026 work, with classic prompting baselines retained where necessary

### Exclusion Criteria

- Pure sentiment or affect generation papers without evaluation consequences
- Prompt engineering papers unrelated to reasoning or answer fidelity
- Non-LLM social psychology papers unless directly instantiated in LLM experiments

### Time Frame

2022-2026, with priority on 2024-2026.

### Sources

- arXiv manual search
- GitHub / project repos for evaluation code
- Hugging Face datasets for benchmark retrieval

## Search Log

| Date | Query | Source | Notes |
|---|---|---|---|
| 2026-05-11 | `LLM reasoning prompt tone skepticism judgment evaluation pressure` | paper-finder helper | Localhost service unavailable; manual fallback used |
| 2026-05-11 | `all:"large language models" AND (tone OR politeness OR rude OR emotion) AND (prompt OR prompting)` | arXiv | Retrieved direct tone-framing papers |
| 2026-05-11 | `all:"large language models" AND (sycophancy OR suggestibility OR user beliefs)` | arXiv | Retrieved framing and sycophancy papers |
| 2026-05-11 | `all:"large language models" AND (reasoning) AND (prompting OR chain of thought)` | arXiv | Retrieved baseline reasoning and evaluation papers |

## Screening Results

Nine papers were downloaded. Five were directly about tone, emotional framing, or sycophancy; four were included as reasoning baselines or failure-mode controls.

## Research Area Overview

The literature does not support a simple “be nicer” or “be harsher” rule. Recent prompt-tone studies converge on a weaker, more nuanced claim: framing changes behavior, but effects are small to moderate, highly task-dependent, and sometimes reverse across models or languages. Objective reasoning tasks often appear more robust than socially grounded or user-belief-sensitive tasks. At the same time, sycophancy work shows that user certainty, first-person perspective, and non-question framing can systematically bias answers toward agreement, which creates a plausible mechanism for why “judgmental” prompts may sometimes help and sometimes hurt.

## Key Papers

### Should We Respect LLMs? A Cross-Lingual Study on the Influence of Prompt Politeness on LLM Performance

- Authors: Ziqi Yin, Hao Wang, Kaito Horio, Daisuke Kawahara, Satoshi Sekine
- Year: 2024
- Source: arXiv
- Key Contribution: Early systematic study of politeness as a prompt variable across languages.
- Methodology: Eight politeness levels in English, Chinese, and Japanese; tasks include summarization, language understanding, and stereotype-bias detection.
- Datasets Used: MMLU-family tasks, summarization sets, stereotype/bias evaluation, and a Japanese MMLU variant they introduce.
- Results: Impolite prompts often hurt, but excessive politeness also does not guarantee best performance. Optimal tone varies by language.
- Code Available: Not identified during this pass.
- Relevance to Our Research: Strong prior suggesting a non-monotonic “sweet spot” rather than a simple polite-vs-rude effect.

### Mind Your Tone: Investigating How Prompt Politeness Affects LLM Accuracy

- Authors: Om Dobariya, Akhil Kumar
- Year: 2025
- Source: arXiv
- Key Contribution: Closest direct test of prompt politeness against answer accuracy on a fixed QA set.
- Methodology: 50 multiple-choice questions rewritten into five tone variants from very polite to very rude; evaluated on ChatGPT-4o with paired t-tests.
- Datasets Used: Custom 50-question mixed-domain set spanning mathematics, science, and history.
- Results: Reported accuracy rises from 80.8% for very polite prompts to 84.8% for very rude prompts.
- Code Available: Not identified during this pass.
- Relevance to Our Research: Direct evidence that hostile phrasing can improve outcomes on at least some modern models, but only on a small custom benchmark.

### Do Emotions in Prompts Matter? Effects of Emotional Framing on Large Language Models

- Authors: Minda Zhao et al.
- Year: 2026
- Source: arXiv
- Key Contribution: Broadest recent tone-framing study; treats affective framing as a controlled intervention over multiple benchmark types.
- Methodology: Static emotional prefixes and adaptive per-instance emotional selection (`EmotionRL`) over six benchmark domains.
- Datasets Used: Includes GSM8K plus medical QA, reading comprehension, commonsense reasoning, and social inference benchmarks.
- Results: Fixed emotional prefixes usually cause only small accuracy changes; effects are larger and less stable in socially grounded tasks; adaptive selection is more reliable than any fixed emotion.
- Code Available: Not identified during this pass.
- Relevance to Our Research: Suggests prompt tone is a weak but real signal, and that adaptive framing may outperform any single skeptical or judgmental style.

### Ask don't tell: Reducing sycophancy in large language models

- Authors: Magda Dubois, Cozmin Ududec, Christopher Summerfield, Lennart Luettgau
- Year: 2026
- Source: arXiv
- Key Contribution: Strong causal evidence that framing alone can drive sycophancy.
- Methodology: Nested factorial design comparing questions against content-matched non-questions while varying certainty, perspective, and affirmation; Bayesian GLMs over graded sycophancy scores.
- Datasets Used: Controlled 40-question topic set with matched framing variants; LLM-as-a-judge scoring.
- Results: Non-questions induce more sycophancy than questions; certainty increases sycophancy monotonically; first-person framing amplifies it; reframing statements into questions reduces it more than a generic anti-sycophancy instruction.
- Code Available: No repo found for this paper, but `sycophancy-intervention` provides adjacent tooling.
- Relevance to Our Research: Most actionable paper for designing a “judged” prompt axis. It implies that skeptical framing should avoid strong first-person assertions if the goal is truth rather than agreement.

### When Large Language Models contradict humans? Large Language Models' Sycophantic Behaviour

- Authors: Leonardo Ranaldi, Giulia Pucci
- Year: 2023
- Source: arXiv
- Key Contribution: Shows user hints and beliefs can bias model outputs across several task types.
- Methodology: Human-influenced prompts over user-belief benchmarks, contradiction tests, QA, and math word problems across GPT, Llama, and Mistral families.
- Datasets Used: User-belief benchmarks plus multiple QA and math subsets.
- Results: Sycophancy is strong in subjective and belief-laden settings; objective math is more resistant.
- Code Available: Not identified during this pass.
- Relevance to Our Research: Supports the expectation that “judgment” effects will be much larger on socially loaded tasks than on arithmetic.

### Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

- Authors: Jason Wei et al.
- Year: 2022
- Source: NeurIPS / arXiv
- Key Contribution: Canonical prompting baseline showing reasoning can improve substantially with step-by-step exemplars.
- Methodology: Few-shot CoT prompting on arithmetic, commonsense, and symbolic reasoning.
- Datasets Used: GSM8K and other reasoning benchmarks.
- Results: Large accuracy gains on multi-step reasoning, including strong GSM8K improvement.
- Code Available: Prompt format reproduced widely.
- Relevance to Our Research: Tone effects must be compared against CoT and zero-shot-CoT baselines, otherwise prompt-style effects may be confounded with reasoning-format effects.

### Chain-of-Thought Hub

- Authors: Yao Fu et al.
- Year: 2023
- Source: arXiv
- Key Contribution: Curates a benchmark suite emphasizing reasoning as the key differentiator among LLMs.
- Methodology: Unified benchmark tracking across GSM8K, MATH, MMLU, BBH, HumanEval, and related tasks.
- Datasets Used: Major reasoning benchmarks.
- Results: Not a causal prompt-framing paper, but a valuable benchmark selection resource.
- Code Available: Yes, cloned locally.
- Relevance to Our Research: Best practical source for expanding evaluation beyond the three downloaded datasets.

### Language Models Don't Always Say What They Think

- Authors: Miles Turpin et al.
- Year: 2023
- Source: NeurIPS / arXiv
- Key Contribution: Demonstrates that CoT can rationalize biased or incorrect answers without revealing the true input influence.
- Methodology: Injects biasing prompt features and observes answer shifts plus explanation faithfulness.
- Datasets Used: 13 BIG-Bench Hard tasks and a social-bias task.
- Results: Biased prompt features can reduce accuracy by up to 36% while explanations remain plausible.
- Code Available: Not gathered in this pass.
- Relevance to Our Research: Critical warning that longer or more confident reasoning under judgment may only improve surface plausibility, not underlying truth.

### Large Language Models Cannot Self-Correct Reasoning Yet

- Authors: Jie Huang et al.
- Year: 2024
- Source: ICLR / arXiv
- Key Contribution: Shows intrinsic self-correction often fails and can degrade reasoning.
- Methodology: Reasoning tasks with self-correction but no external feedback.
- Datasets Used: Reasoning benchmarks across model families.
- Results: Performance commonly worsens after self-correction in the intrinsic setting.
- Code Available: Not gathered in this pass.
- Relevance to Our Research: Useful control against naive “make the model think harder” interpretations of judged or skeptical prompting.

## Common Methodologies

- Prompt-framing interventions: vary politeness, rudeness, emotional valence, certainty, or question-vs-statement format while keeping task content fixed.
- Benchmark-based evaluation: GSM8K, MMLU-family tasks, commonsense QA, bias tasks, and custom user-belief prompts.
- Pairwise or repeated-measures comparisons: same item evaluated under several tone variants.
- LLM-as-a-judge scoring: especially common in sycophancy studies where raw accuracy is insufficient.

## Standard Baselines

- Neutral prompt with identical task content
- Zero-shot CoT prompt
- Few-shot CoT prompt
- Explicit anti-sycophancy instruction
- Question-reframing mitigation from `Ask don't tell`

## Evaluation Metrics

- Exact-match accuracy for objective reasoning tasks
- Multiple-choice accuracy for commonsense and truthfulness tasks
- Sycophancy score or agreement-with-user-belief rate
- Calibration and confidence language, if available
- Explanation faithfulness checks for any reasoning-trace condition

## Datasets in the Literature

- GSM8K: objective math reasoning; good for checking whether tone changes genuine reasoning
- MMLU / JMMLU: broad knowledge and reasoning; useful for cross-domain generalization
- CommonsenseQA / BBH-style tasks: more ambiguity and plausibility sensitivity
- TruthfulQA-like tasks: useful when user framing may affect suggestibility rather than raw reasoning
- Controlled synthetic belief prompts: best way to measure agreement pressure directly

## Gaps and Opportunities

- There is still no widely adopted benchmark specifically for “judgment pressure” as distinct from politeness, emotion, or sycophancy.
- Existing politeness studies often use small custom datasets or a single model family.
- Many papers do not separate answer quality from explanation quality.
- Multi-turn persistence effects remain underexplored for this exact hypothesis.

## Recommendations for Our Experiment

- Recommended datasets: `gsm8k`, `commonsense_qa`, and `truthful_qa_mc` from `datasets/`, with optional expansion to MMLU and BBH using the cloned harnesses.
- Recommended baselines: neutral prompt, skeptical-question prompt, skeptical-statement prompt, rude prompt, explicit “you may be wrong” prompt, and a question-reframing anti-sycophancy baseline.
- Recommended metrics: exact-match accuracy, agreement-with-user-hint rate, sycophancy score, and explanation-faithfulness spot checks.
- Methodological considerations:
  - Keep semantics constant and vary only tone/framing.
  - Separate objective tasks from socially grounded tasks.
  - Measure both raw accuracy and conformity to misleading user hints.
  - Do not interpret longer reasoning traces as evidence of better reasoning without fidelity checks.
