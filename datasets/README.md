# Downloaded Datasets

This directory contains locally downloaded benchmark datasets for studying whether skeptical or judgmental prompt tone changes reasoning quality. Data files are intentionally excluded from git by `datasets/.gitignore`.

## Dataset 1: GSM8K

### Overview
- Source: Hugging Face `gsm8k` with config `main`
- Local path: `datasets/gsm8k/`
- Size: train 7,473; test 1,319; about 2.8 MB on disk
- Format: Hugging Face dataset saved with `save_to_disk`
- Task: grade-school math word-problem reasoning
- Why useful here: clean objective reasoning benchmark for testing whether tone changes accuracy rather than style

### Download Instructions

Using Hugging Face:

```python
from datasets import load_dataset
dataset = load_dataset("gsm8k", "main")
dataset.save_to_disk("datasets/gsm8k")
```

### Loading the Dataset

```python
from datasets import load_from_disk
dataset = load_from_disk("datasets/gsm8k")
print(dataset["test"][0])
```

### Sample Data

See `datasets/gsm8k/samples.json`.

### Notes

- Columns: `question`, `answer`
- Good primary benchmark for objective reasoning where sycophancy should be weaker according to prior work

## Dataset 2: CommonsenseQA

### Overview
- Source: Hugging Face `tau/commonsense_qa`
- Local path: `datasets/commonsense_qa/`
- Size: train 9,741; validation 1,221; test 1,140; about 2.2 MB on disk
- Format: Hugging Face dataset saved with `save_to_disk`
- Task: multiple-choice commonsense reasoning
- Why useful here: more ambiguity than GSM8K, so prompt framing may have more room to affect answer selection

### Download Instructions

```python
from datasets import load_dataset
dataset = load_dataset("tau/commonsense_qa")
dataset.save_to_disk("datasets/commonsense_qa")
```

### Loading the Dataset

```python
from datasets import load_from_disk
dataset = load_from_disk("datasets/commonsense_qa")
print(dataset["validation"][0])
```

### Sample Data

See `datasets/commonsense_qa/samples.json`.

### Notes

- Columns: `id`, `question`, `question_concept`, `choices`, `answerKey`
- Good secondary benchmark for testing whether hostile or skeptical framing changes performance on plausibility judgments

## Dataset 3: TruthfulQA Multiple Choice

### Overview
- Source: Hugging Face `truthful_qa` with config `multiple_choice`
- Local path: `datasets/truthful_qa_mc/`
- Size: validation 817; about 323 KB on disk
- Format: Hugging Face dataset saved with `save_to_disk`
- Task: factual robustness and resistance to plausible-but-false answers
- Why useful here: useful for measuring whether judgmental prompts increase truthfulness or instead encourage user-pleasing / overconfident behavior

### Download Instructions

```python
from datasets import load_dataset
dataset = load_dataset("truthful_qa", "multiple_choice")
dataset.save_to_disk("datasets/truthful_qa_mc")
```

### Loading the Dataset

```python
from datasets import load_from_disk
dataset = load_from_disk("datasets/truthful_qa_mc")
print(dataset["validation"][0])
```

### Sample Data

See `datasets/truthful_qa_mc/samples.json`.

### Notes

- Columns: `question`, `mc1_targets`, `mc2_targets`
- Good complement to reasoning benchmarks because “judged” prompts may shift calibration or suggestibility before they shift raw reasoning

## Recommendations

- Primary dataset combination: `gsm8k` + `commonsense_qa` + `truthful_qa_mc`
- Optional expansion: use `MMLU`, `BBH`, and `MATH` through `code/lm-evaluation-harness` or `code/chain-of-thought-hub` instead of downloading ad hoc copies
- Prompt design suggestion: keep item content fixed and vary only tone, certainty, and user-perspective framing
