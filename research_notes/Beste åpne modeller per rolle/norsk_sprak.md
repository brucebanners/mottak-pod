# Beste åpne modeller for norsk (bokmål/nynorsk) på ett RTX PRO 6000 Blackwell (96 GB)

Researched 2026-10-06. Primary data: the EuroEval Norwegian leaderboard (raw data pulled from euroeval.com's frontend bundle on 2026-10-06; EuroEval versions 15.x–18.1 per model), plus Hugging Face model cards and papers. Data source for all EuroEval numbers below: [EuroEval Norwegian leaderboard](https://euroeval.com/leaderboards/Monolingual/norwegian/).

How to read EuroEval numbers: "Rank score" is the mean rank across Norwegian tasks (lower is better; 1.0 = best on everything). Dataset columns are the primary metric (first number) per task: `scala_nb`/`scala_nn` = linguistic acceptability (grammar judgement) in Bokmål/Nynorsk; `idioms_no` = Norwegian idioms (knowledge); `nrk_quiz_qa` = NRK quiz knowledge; `no_sammendrag` = summarization; `norquad` = reading comprehension; `nor_common_sense_qa` = common-sense reasoning; `norne_nn` = Nynorsk NER. "(val)" in the model name means evaluated on validation splits only. 📝 = instruct, 🤔 = reasoning, 🧠 = base.

## 1. Which Norwegian/Scandinavian benchmarks exist and what do the latest results show?

### Takeaway
EuroEval (formerly ScandEval) is the only continuously updated Norwegian leaderboard and covers both Bokmål and Nynorsk; NorEval (UiO LTG, ACL 2025 Findings) is the most thorough academic benchmark but its published results (2025) only cover older ≤12B models. On EuroEval as of Oct 2026 the best open model overall is GLM-5.3-Flash (321B, too large for 96 GB); the best open model that fits on one 96 GB card is Gemma 4 31B-it, followed by Qwen3.6-27B, Gemma 4 26B-A4B and Qwen3.8-27B.

### Cited Findings
- EuroEval Norwegian leaderboard tasks: sentiment (NoReC), NER Bokmål+Nynorsk (NorNE), linguistic acceptability Bokmål+Nynorsk (ScaLA), reading comprehension (NorQuAD), summarization (no_sammendrag), knowledge (NRK-quiz-QA, idioms_no), common-sense reasoning (nor_common_sense_qa) — [EuroEval](https://euroeval.com/leaderboards/Monolingual/norwegian/)
- Overall top of the generative Norwegian leaderboard is closed models: gpt-6-astra (rank score 1.16), Gemini 3.7 Flash / Gemini 3 Pro preview (1.22). Best open model: zai-org/GLM-5.3-Flash (rank 2, score 1.24, 321B params, released 2026-08-26). Next open: google/gemma-4-31B-it (rank 4, 1.35) — on par with gpt-5.6-terra (1.35) and gemini-3-flash-preview no-thinking (1.34) — [EuroEval](https://euroeval.com/leaderboards/Monolingual/norwegian/)
- NorEval: 24 human-created datasets (5 new), covers both Bokmål and Nynorsk with human baselines, 100+ human-written prompts, integrated in LM Evaluation Harness; 19 open models evaluated; published June 2025 (ACL 2025 Findings) — [arXiv 2504.07749](https://arxiv.org/abs/2504.07749v2)
- NorEval results (2025, older models): NorMistral-11B best overall (Borda count), then AI-Sweden Llama-3-8B; best instruction-tuned was Mistral-Nemo-12B-IT. Humans beat models by 10 pts on Belebele, 14.4 on NorQuAD, 17.8 on NorCommonsenseQA — [NorEval (ar5iv)](https://ar5iv.labs.arxiv.org/html/2504.07749)
- NorEval finding: models generally do better in Bokmål than Nynorsk; instruction tuning narrows the gap on some tasks but worsens it on language-specific tasks (NRK-Quiz-QA, NorIdiom) — [NorEval (ar5iv)](https://ar5iv.labs.arxiv.org/html/2504.07749)
- NB AI-lab evaluates Borealis on NorEval, MMLU-English and their own "nb-gpt-bench" — [HF: NbAiLab/borealis-27b](https://huggingface.co/NbAiLab/borealis-27b)

### Inferences
- EuroEval is few-shot task scoring; it measures grammar judgement (ScaLA), knowledge and comprehension well, but free-text fluency/idiomatic writing only indirectly (summarization + idioms). No public benchmark found that scores long-form Norwegian writing quality with native-speaker ratings across current (2026) models.
- `idioms_no` and `nrk_quiz_qa` are the best proxies for "native-like" Norwegian knowledge; `scala_nn` is the best proxy for Nynorsk grammar. These separate models more sharply than the overall rank score.

### Gaps
- NLEBench, Mímir and NorBench: no 2025–2026 results found in this search; NorEval has no public live leaderboard with 2026 models found.
- EuroEval page does not expose a single "last updated" date; newest model entries are dated 2026-08-26 (GLM-5.3-Flash release date), so data is at least that recent.

## 2. Which general models score highest in Norwegian, and which fit on 96 GB?

### Takeaway
Among models that fit on one 96 GB card, Gemma 4 31B-it is clearly the strongest in Norwegian on EuroEval (best Nynorsk grammar of all open models, incl. GLM-5.3), with Qwen3.6-27B as second. gpt-oss-120b fits but is notably weaker in Nynorsk and idioms. Older 70B Llamas are now beaten by ~30B models.

### Cited Findings (EuroEval Norwegian generative leaderboard, accessed 2026-10-06 — [source](https://euroeval.com/leaderboards/Monolingual/norwegian/))

| Model | Rank | Rank score | Released | Params | scala_nb | scala_nn | idioms_no | nrk_quiz | sammendrag | norquad | commonsense |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GLM-5.3-Flash (reasoning) | 2 | 1.24 | 2026-08-26 | 321B | 72.6 | 69.6 | 70.2 | 78.5 | 32.3 | 76.5 | 83.2 |
| Gemma-4-31B-it | 4 | 1.35 | 2026-04-02 | 31.3B | 68.3 | **70.1** | 58.5 | 65.1 | 32.0 | 73.5 | 89.1 |
| Gemma-4-26B-A4B-it (MoE) | 7 | 1.49 | 2026-04-02 | 25.8B | 63.1 | 59.7 | 48.1 | 58.8 | 31.2 | 71.6 | 86.4 |
| Qwen3.6-27B-FP8 (reasoning) | 7 | 1.46 | 2026-04-22 | 27.8B | 63.1 | 59.2 | 56.5 | 60.7 | 30.4 | 73.1 | 87.0 |
| Qwen3.8-27B (reasoning) | 8 | 1.52 | 2026-08-13 | 27.8B | 61.4 | 56.6 | 53.8 | 53.3 | 30.1 | 73.0 | 83.2 |
| Qwen3.5-35B-A3B-FP8 (reasoning) | 8 | 1.54 | 2026-02-25 | 34.5B | 62.2 | 53.4 | 55.1 | 60.1 | 30.8 | 67.4 | 86.0 |
| Gemma-4-12B-it | 9 | 1.58 | 2026-06-03 | 12.0B | 62.6 | 60.3 | 32.3 | 44.0 | 31.2 | 74.3 | 85.0 |
| cogito-v2-preview-llama-70B | 9 | 1.61 | 2025-07-27 | 70.6B | 63.8 | 50.4 | 26.9 | 54.3 | 32.3 | 74.6 | 82.5 |
| Gemma-3-27b-it | 10 | 1.62 | 2025-03-12 | 27.4B | 69.3 | 58.1 | 42.3 | 53.1 | 31.9 | 67.8 | 79.3 |
| Mistral-Small-3.2-24B-Instruct | 10 | 1.68 | 2025-06-20 | 24.0B | 60.1 | 46.2 | 27.6 | 50.7 | 31.9 | 76.1 | 79.5 |
| Llama-3.1-70B (base) | 11 | 1.72 | 2024-07-15 | 70.6B | 58.8 | 47.4 | 28.4 | 55.9 | 27.5 | 78.5 | 77.4 |
| gpt-oss-120b (reasoning) | 12 | 1.79 | 2025-08-04 | 120B | 53.8 | 36.0 | 39.3 | 64.3 | 26.1 | 65.5 | 82.6 |
| Apertus-v1.5-70B | 13 | 1.89 | 2026-07-24 | 72.0B | 56.2 | 46.6 | 20.0 | 41.4 | 31.0 | 67.9 | 77.6 |
| GLM-4.7-Flash | 13 | 1.88 | 2026-01-19 | 31.2B | 45.9 | 32.2 | 33.2 | 50.2 | 29.2 | 67.9 | 73.9 |
| EuroLLM-22B-Instruct-2512 | 16 | 2.05 | 2025-12-05 | 22.6B | 56.5 | 33.5 | 17.6 | 39.3 | 31.0 | 54.5 | 75.7 |
| Nemotron-3-Nano-30B-A3B | 16 | 2.07 | 2025-12-04 | 31.6B | 47.5 | 17.4 | 27.9 | 47.8 | 25.7 | 62.1 | 66.6 |
| Olmo-3.1-32B-Think | 19 | 2.22 | 2025-12-10 | 32.2B | 17.4 | 7.4 | 25.8 | 43.9 | 24.8 | 66.9 | 65.2 |
| EXAONE-4.0-32B | 21 | 2.43 | 2025-07-15 | 32.0B | 26.1 | 12.2 | 3.0 | 27.1 | 29.2 | 65.0 | 35.5 |

- Other entries: Mistral-Small-3.1-24B-Instruct rank 10 (1.67); Ministral-3-14B-Instruct-2512 rank 14 (1.94); gpt-oss-20b (medium) rank 15 (2.02); Qwen3.5-9B rank 15 (1.96); gemma-4-E4B-it rank 15 (2.00) — [EuroEval](https://euroeval.com/leaderboards/Monolingual/norwegian/)
- GLM-5.3-Flash also has a measured hallucination rate of 0.62 on EuroEval (only model of these with that metric filled) — [EuroEval](https://euroeval.com/leaderboards/Monolingual/norwegian/)
- Not found on the Norwegian leaderboard: Llama-3.3-70B, Qwen3.5-122B-A10B, Mistral Large, DeepSeek open weights (only DeepSeek API entries) — [EuroEval](https://euroeval.com/leaderboards/Monolingual/norwegian/)

### Inferences
- VRAM fit (estimated from parameter count: BF16 ≈ 2 bytes/param, FP8 ≈ 1, 4-bit ≈ 0.5–0.6, plus KV cache):
  - Gemma-4-31B-it: ~63 GB BF16 → fits in BF16 with room for KV cache; FP8 (~32 GB) leaves lots of context room.
  - Qwen3.6-27B / Qwen3.8-27B: ~56 GB BF16 → fits; leaderboard itself tested the FP8 variant of 3.6.
  - Qwen3.5-35B-A3B: ~70 GB BF16 → fits, tight on context; FP8 (~35 GB) comfortable. Gemma-4-26B-A4B: ~52 GB BF16 → fits.
  - gpt-oss-120b: ships in MXFP4 (~60–65 GB) → fits.
  - 70B class (cogito-llama-70B, Llama-3.1-70B, Apertus-70B): ~141 GB BF16 → does NOT fit; FP8 (~71 GB) fits with limited KV cache; 4-bit (~40 GB) fits comfortably. No reason to choose them — they score worse than 27–31B models.
  - GLM-5.3-Flash 321B: ~160–190 GB even at 4-bit → does NOT fit on one 96 GB card.
- Ranking for a single 96 GB card, by EuroEval Norwegian: 1) Gemma-4-31B-it, 2) Qwen3.6-27B, 3) Gemma-4-26B-A4B-it (MoE, faster), 4) Qwen3.8-27B, 5) Qwen3.5-35B-A3B, then Gemma-3-27b-it / Mistral-Small-3.x / Borealis-27b.
- Gemma 4 31B leads every fitting model on Nynorsk grammar (scala_nn 70.1 — even above GLM-5.3-Flash 69.6) and on Norwegian idioms/NRK-quiz knowledge among fitting models. Qwen3.6-27B is close overall but ~11 points lower on Nynorsk grammar.
- Newer is not always better: Qwen3.8-27B (Aug 2026) ranks slightly below Qwen3.6-27B (Apr 2026) on Norwegian.

### Gaps
- No native-speaker generation-quality ranking for 2026 models found; EuroEval rank does not directly measure stylistic naturalness.
- Gemma-4-31B-it was evaluated with 8k context in EuroEval; no long-context Norwegian results.

## 3. Norway-specific models: size, base, license, and comparison to general models

### Takeaway
The strongest Norway-specific models are NB AI-lab's Borealis (Gemma 3 fine-tunes, May 2026) and the brand-new Borealis 2 preview (Gemma-4-31B-it with Norwegian continued pre-training, 2026-09-28, not yet benchmarked). Borealis-27b roughly matches its Gemma-3-27b base and is clearly behind Gemma 4 / Qwen 3.6 on EuroEval. Older NorMistral/NorwAI models are far behind modern multilingual models.

### Cited Findings
- **Borealis (NB AI-lab)**: 270M/1B/4B/12B/27B, all Gemma 3-based, instruction-tuned for Norwegian Bokmål, Nynorsk and English; released 2026-05-26; full "borealis" variants use an NB licence (adapted Apache 2.0 with use restrictions) and include ~10,000 SFT tasks derived from copyrighted newspapers; "borealis-open" variants use the Gemma licence with no newspaper data (dataset NbAiLab/aurora-sft-open). Runs with Transformers, vLLM, llama.cpp, Ollama (GGUF) — [ai.nb.no/borealis](https://ai.nb.no/borealis/)
- NB states Borealis is strongest on Norwegian knowledge, grammar, sentiment and safety metrics; "NorMistral remains very strong on some Sámi and translation tasks, and Gemma remains strong on several general metrics" — [ai.nb.no/borealis](https://ai.nb.no/borealis/)
- Borealis-27b is fine-tuned from google/gemma-3-27b-it with SFT (NbAiLab/aurora-sft); model card reports only "slight performance increase in some key metrics" over base on NorEval, MMLU-English, nb-gpt-bench; not a reasoning model — [HF: NbAiLab/borealis-27b](https://huggingface.co/NbAiLab/borealis-27b)
- EuroEval: borealis-27b rank 11 (1.68), scala_nb 61.4, scala_nn 53.2, idioms 42.7, nrk_quiz 58.3, commonsense 89.7 (best of all open models on that task); base gemma-3-27b-it rank 10 (1.62) with scala_nn 58.1, idioms 42.3, nrk_quiz 53.1. borealis-12b rank 13 (1.87) — [EuroEval](https://euroeval.com/leaderboards/Monolingual/norwegian/)
- NB press release 2026-08-10: new Borealis models trained on copyrighted Norwegian newspaper text in both pre-training and fine-tuning, to be published on Hugging Face in week 34 2026; no metrics given — [NTB/Nasjonalbiblioteket](https://kommunikasjon.ntb.no/pressemelding/19017131/nye-sprakmodeller-fra-nasjonalbiblioteket-skal-styrke-ki-tilpasset-norske-forhold); Sigma2 (2026-08-12): trained on Olivia and LUMI supercomputers — [Sigma2](https://www.sigma2.no/node/441)
- **Borealis 2 31B preview** (2026-09-28): built on Gemma-4-31B-it; continued pre-training on Aurora 2604 data (47.6B words; Bokmål 24.3B, Nynorsk 11.1B; knowledge cutoff 2025-01-01; 18 languages incl. Danish, Swedish, Sámi), then 3-epoch SFT on aurora-sft-2606; adapted Apache 2.0 with restrictions; no benchmarks published; "preview experiment… not completely safety-aligned". Also e4b and e2b previews released same day — [HF: NbAiLab/borealis2-31b-preview](https://huggingface.co/NbAiLab/borealis2-31b-preview); [HF API NbAiLab listing](https://huggingface.co/NbAiLab)
- **NorMistral (UiO LTG / norallm)**: normistral-11b-warm (Mistral-Nemo base, 2024-09), normistral-11b-thinking (2025-10/12; SFT on English reasoning traces from Kimi-K2-Thinking, then RLAIF on Bokmål and Nynorsk prompts with Mistral-Large-2411 as reward model; Apache 2.0), normistral-11b-long (2025-12), normistral-11b-translate (2026-02) — [HF: ltg/normistral-11b-thinking](https://huggingface.co/ltg/normistral-11b-thinking); [arXiv 2512.08777](https://arxiv.org/abs/2512.08777)
- arXiv 2512.08777 (LTG): on-policy preference training preserves Norwegian fluency better than SFT on machine-translated data or multilingual fine-tuning, judged by native Bokmål speakers — [arXiv 2512.08777](https://arxiv.org/abs/2512.08777)
- EuroEval scores for NorMistral: normistral-11b-warm scala_nb 17.8 / scala_nn 17.8 / idioms 5.2; normistral-11b-thinking scala_nb 10.7 / scala_nn 16.6; normistral-11b-long scala_nb 26.3 / idioms 7.2; normistral-7b-scratch rank 36 (3.52); normistral-11b-translate rank 43 with ~0 scores — [EuroEval](https://euroeval.com/leaderboards/Monolingual/norwegian/)
- **NorwAI (NTNU)**: models based on GPT, Mistral, Llama2, Mixtral and Magistral, pre-trained/continually pre-trained on 25B–88.45B tokens with Norwegian-extended tokenizer; tech report Jan 2026 gives no comparisons vs general models — [arXiv 2601.03034](https://arxiv.org/abs/2601.03034). NorwAI-Magistral-24B-reasoning (2025-09): gated, use restricted to organizations resident in Nordic countries — [HF: NorwAI-Magistral-24B-reasoning](https://huggingface.co/NorwAI/NorwAI-Magistral-24B-reasoning)
- EuroEval: NorwAI-Mixtral-8x7B (base, 47B) rank 23 (2.56), scala_nn 30.5, idioms 26.1; NorwAI-Mixtral-8x7B-instruct scala_nb 53.0 / scala_nn 44.3; NorwAI-Magistral-24B-reasoning rank 47 with 0.00 on all tasks — [EuroEval](https://euroeval.com/leaderboards/Monolingual/norwegian/)
- HPLT/NorOLMo-13B (2026-01-21): rank 25 (2.69), scala_nb 26.8 — [EuroEval](https://euroeval.com/leaderboards/Monolingual/norwegian/)
- bineric/lynx-instruct-30b (Norwegian company fine-tune, 2026-01): rank 20–21 (2.34–2.40), scala_nn 16.1 — [EuroEval](https://euroeval.com/leaderboards/Monolingual/norwegian/)
- Older NorwAI (2024): first-gen models "tend to default to Bokmål when lacking relevant Nynorsk responses" — [NTNU NorLLM, 2024-04-26](https://www.ntnu.no/norllm/fire-modeller-bygget-fire-nye-p%C3%A5-beddingen)

### Inferences
- The all-zero scores for NorwAI-Magistral-24B-reasoning and normistral-11b-translate almost certainly reflect output-format/evaluation failures (a reasoning or translation-only model not following the few-shot format), not true Norwegian ability; they should not be read as "worst at Norwegian".
- NorMistral-11B models are base/specialised (translation, Sámi, long context) and are not competitive as general Norwegian assistants vs Gemma 4 / Qwen 3.6 in 2026; their value is Sámi/translation niches (per NB's own statement).
- Borealis 2 31B (Gemma 4 31B + 35B words of Bokmål/Nynorsk CPT) is the most promising Norway-specific candidate and fits on 96 GB (~63 GB BF16), but is an unbenchmarked preview; it should be tested head-to-head with plain Gemma-4-31B-it before adoption, since Borealis 1 gave only marginal gains over its base.
- Licence matters: Borealis full models and Borealis 2 carry use restrictions (no training-data reconstruction / press access); borealis-open uses Gemma licence; NorwAI-Magistral is Nordic-only gated; NorMistral is Apache 2.0.

### Gaps
- Viking (Silo AI/AMD) and Poro: not present on the EuroEval Norwegian leaderboard and no 2025–2026 Norwegian results found.
- NB-Llama (NbAiLab Llama-3.x fine-tunes): no current EuroEval entry found in this search.
- No published numbers yet for the August 2026 newspaper-pretrained Borealis release or for Borealis 2 previews.

## 4. Known weaknesses (Danish/Swedish bleed, anglicisms, Nynorsk)

### Takeaway
Nynorsk is the consistent weak spot: most models lose 5–25 points going from Bokmål to Nynorsk grammar on EuroEval, with gpt-oss, Nemotron, Olmo, EXAONE and EuroLLM worst; Gemma 4 31B is the exception (no Nynorsk drop). Concrete published measurements of Danish/Swedish bleed or anglicisms in 2026 models were not found.

### Cited Findings
- Bokmål vs Nynorsk grammar (ScaLA MCC, scala_nb → scala_nn): Gemma-4-31B-it 68.3 → 70.1; Qwen3.6-27B 63.1 → 59.2; Gemma-3-27b-it 69.3 → 58.1; Mistral-Small-3.2 60.1 → 46.2; gpt-oss-120b 53.8 → 36.0; EuroLLM-22B 56.5 → 33.5; Nemotron-3-Nano-30B 47.5 → 17.4; Olmo-3.1-32B-Think 17.4 → 7.4 — [EuroEval](https://euroeval.com/leaderboards/Monolingual/norwegian/)
- Norwegian idioms knowledge is a large separator: GLM-5.3-Flash 70.2, Gemma-4-31B 58.5, Qwen3.6-27B 56.5, Borealis-27b 42.7, gpt-oss-120b 39.3, Mistral-Small-3.2 27.6, Llama-3.1-70B 28.4, Apertus-70B 20.0, EuroLLM-22B 17.6, EXAONE-4.0-32B 3.0 — [EuroEval](https://euroeval.com/leaderboards/Monolingual/norwegian/)
- NorEval (2025): models do better on Bokmål than Nynorsk in most categories; instruction tuning can worsen language-specific tasks — [NorEval](https://ar5iv.labs.arxiv.org/html/2504.07749)
- LTG motivation for normistral-11b-thinking/2512.08777: lower-resource languages lack native-speaker instruction data, and SFT on machine-translated data harms fluency vs on-policy training — [arXiv 2512.08777](https://arxiv.org/abs/2512.08777)
- NB says Gemma remains strong on general metrics while Borealis improves Norwegian knowledge/grammar — [ai.nb.no/borealis](https://ai.nb.no/borealis/)

### Inferences
- Reasoning/"think" models and models trained mainly on English/Chinese (Olmo, EXAONE, Nemotron, gpt-oss) show the largest Nynorsk drops → for Nynorsk output, prefer Gemma-4-31B-it.
- The machine-translated-SFT fluency problem described by LTG implies anglicism-like/translated phrasing is a known risk for fine-tunes built on translated data; NB's Borealis SFT uses native Norwegian sources (incl. newspapers), which targets this.

### Gaps
- No quantitative 2025–2026 study found measuring Danish/Swedish word leakage or anglicism rates per model in Norwegian generation. EuroEval's Scandinavian/Danish/Swedish leaderboards exist but cross-language bleed is not a scored metric.
- No Norwegian tech-press (Digi.no/Kode24) comparison of local models for Norwegian found in this search.
