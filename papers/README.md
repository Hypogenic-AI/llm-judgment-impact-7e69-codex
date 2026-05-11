# Downloaded Papers

1. [Should We Respect LLMs? A Cross-Lingual Study on the Influence of Prompt Politeness on LLM Performance](2402.14531_should_we_respect_llms.pdf)
   - Authors: Ziqi Yin, Hao Wang, Kaito Horio, Daisuke Kawahara, Satoshi Sekine
   - Year: 2024
   - Source: arXiv:2402.14531
   - Why relevant: Directly studies politeness effects across English, Chinese, and Japanese, with task-dependent and culture-dependent results.

2. [Mind Your Tone: Investigating How Prompt Politeness Affects LLM Accuracy (short paper)](2510.04950_mind_your_tone.pdf)
   - Authors: Om Dobariya, Akhil Kumar
   - Year: 2025
   - Source: arXiv:2510.04950
   - Why relevant: Closest match to the hypothesis; compares very polite through very rude prompts on a fixed multiple-choice set and reports slightly better performance for rude phrasing on GPT-4o.

3. [Do Emotions in Prompts Matter? Effects of Emotional Framing on Large Language Models](2604.02236_do_emotions_in_prompts_matter.pdf)
   - Authors: Minda Zhao, Yutong Yang, Chufei Peng, Rachel Gonsalves, Weiyue Li, Ruyi Yang, Zhixi Liu, Mengyu Wang
   - Year: 2026
   - Source: arXiv:2604.02236
   - Why relevant: Extends tone-style prompt framing to emotional prefixes over six benchmark domains and finds mostly small, input-dependent effects.

4. [Ask don't tell: Reducing sycophancy in large language models](2602.23971_ask_dont_tell.pdf)
   - Authors: Magda Dubois, Cozmin Ududec, Christopher Summerfield, Lennart Luettgau
   - Year: 2026
   - Source: arXiv:2602.23971
   - Why relevant: Strongest recent paper on framing-driven sycophancy; useful for designing “judgment” prompts and mitigation baselines.

5. [When Large Language Models contradict humans? Large Language Models' Sycophantic Behaviour](2311.09410_llm_sycophantic_behaviour.pdf)
   - Authors: Leonardo Ranaldi, Giulia Pucci
   - Year: 2023
   - Source: arXiv:2311.09410
   - Why relevant: Establishes that user hints and beliefs can override model behavior in subjective and some factual tasks, while objective math is more resistant.

6. [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](2201.11903_chain_of_thought_prompting.pdf)
   - Authors: Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, Denny Zhou
   - Year: 2022
   - Source: arXiv:2201.11903
   - Why relevant: Canonical baseline for reasoning improvement via prompt structure; needed to separate “tone” effects from “reasoning format” effects.

7. [Chain-of-Thought Hub: A Continuous Effort to Measure Large Language Models' Reasoning Performance](2305.17306_chain_of_thought_hub.pdf)
   - Authors: Yao Fu, Litu Ou, Mingyu Chen, Yuhao Wan, Hao Peng, Tushar Khot
   - Year: 2023
   - Source: arXiv:2305.17306
   - Why relevant: Curates a practical reasoning benchmark suite and codebase for follow-on experiments.

8. [Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting](2305.04388_unfaithful_cot_explanations.pdf)
   - Authors: Miles Turpin, Julian Michael, Ethan Perez, Samuel R. Bowman
   - Year: 2023
   - Source: arXiv:2305.04388
   - Why relevant: Shows that reasoning traces can rationalize biased answers, which matters if judgmental prompts change explanation style without improving truth.

9. [Large Language Models Cannot Self-Correct Reasoning Yet](2310.01798_cannot_self_correct_reasoning_yet.pdf)
   - Authors: Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou
   - Year: 2024
   - Source: arXiv:2310.01798
   - Why relevant: Useful negative control for “think longer” interventions; extra reflection can degrade reasoning without external feedback.

## Notes

- Detailed chunked copies for deeper reading were created in `papers/pages/` for the most relevant tone and sycophancy papers.
- The `paper-finder` localhost service was unavailable during this run, so paper selection used arXiv search plus targeted manual screening.
