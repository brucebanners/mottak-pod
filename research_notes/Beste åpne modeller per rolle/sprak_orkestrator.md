# Språk/samtale/orkestrator-modell på ett RTX PRO 6000 Blackwell (96 GB, sm_120) — status oktober 2026

Baseline å slå: Qwen3.6-35B-A3B (MoE, BF16). Kode er ikke et krav; fokus er chat, resonnering, instruksjonsfølging og verktøykall.

## 1. Hvilke åpne modeller leder på chat/resonnering/verktøybruk (okt 2026)?

### Takeaway
Toppen av åpne modeller (Kimi K3, GLM-5.3, MiMo-V2.6-Pro, DeepSeek V4.x, Qwen3.8-2.4T) er alle 300B–2.8T og passer IKKE på ett 96 GB-kort. Blant modeller som passer er Qwen3.8-27B (aug 2026, Apache-2.0) den klart sterkeste i Artificial Analysis-målinger og et stort sprang over Qwen3.6-generasjonen; Gemma 4 31B er det sterkeste ikke-kinesiske alternativet.

### Cited Findings
- Artificial Analysis (AA) open-weights-side (Intelligence Index v4.3.2, ingen dato på siden, hentet 2026-10-06): MiMo-V2.6-Pro 46 (1.0T/42B aktiv), GLM-5.3 (Max) 45 (753B/40B), Kimi K3 (Max) 44 (2.8T/104B), GLM-5.3 Flash 42 (320B/18B), DeepSeek V4.1 Flash (Max) 39, Qwen3.8 27B 34 — [AA open-source models](https://artificialanalysis.ai/models/open-source)
- AA modellside Qwen3.8 27B (Xhigh): 34 på Intelligence Index v4.3.2, "#1 / 142 among open weights models of similar size", 260k kontekst, Apache 2.0, utgitt 14. aug 2026, 47.1 tok/s via API — [AA Qwen3.8 27B](https://artificialanalysis.ai/models/qwen3-8-27b)
- Eldre indeksversjon (publisert 31. aug 2026): Qwen3.8-27B AA Intelligence Index 52 (xhigh), 44 (medium), 35 (non-reasoning), Agentic Index 51; vs Qwen3.6-27B 38 → "14-point jump at identical parameter count" — [Qubrid](https://www.qubrid.com/blog/qwen38-27b-benchmarks-official-and-independent-results). MERK: 52 vs 34 skyldes ulike indeksversjoner (AA har re-skalert til v4.3.2); tallene kan ikke sammenlignes direkte.
- Qwen offisielle tall Qwen3.8-27B: GPQA Diamond 89.2, HLE 30.8, IFBench 79.5, Terminal-Bench 2.1 73.0, SWE-bench Pro 61.7, LiveCodeBench v6 90.3, OSWorld-Verified 84.3 (vs 63.9 for Qwen3.6-27B) — [Qubrid](https://www.qubrid.com/blog/qwen38-27b-benchmarks-official-and-independent-results)
- Qwen3.8-serien: åpne vekter kun for Qwen3.8-27B (2026-08-14) og Qwen3.8-2.4T-A95B (2026-08-12) i det offisielle repoet — [GitHub QwenLM/Qwen3.8](https://github.com/QwenLM/Qwen3.8)
- Tredjepartsoversikt hevder også en "Qwen3.8-Flash-Next" (~125B, 6B aktiv, Qwen Community License 1.0, GPQA 91.7) med åpne vekter, og at det ikke finnes Qwen3.8 i 35B/122B-størrelse — [Codersera](https://codersera.com/blog/qwen-3-8-model-lineup-2026/). Ikke bekreftet i det offisielle GitHub-repoet; behandles som usikkert.
- Gemma 4 (lansert 7. april 2026; 12B lagt til 3. juni 2026), instruct m/ thinking: 31B dense — Arena Elo 1452, MMLU-Pro 85.2, GPQA 84.3, τ2-bench 76.9, BBEH 74.4; 26B-A4B MoE — Arena Elo 1441, MMLU-Pro 82.6, GPQA 82.3, τ2-bench 68.2 — [Gemma4all (sekundærkilde, juli 2026)](https://gemma4all.com/blog/gemma-4-benchmarks-performance)
- Gemma 4 er Apache 2.0 — [lilting.ch](https://lilting.ch/en/articles/google-gemma-4-open-model-family)
- AA (30. april 2026): "Gemma 4 31B and NVIDIA Nemotron 3 Super" er de høyest scorende ikke-kinesiske åpne modellene — [AA recent open weights launches](https://artificialanalysis.ai/articles/recent-open-weights-model-launches)
- Baseline Qwen3.6-35B-A3B (16. april 2026, 35B/3B aktiv, Apache 2.0): GPQA Diamond 84.85, HLE 21.4, SWE-bench Verified 73.4 — [DataLearner](https://www.datalearner.com/en/benchmark-compare/qwen3-6-35b-a3b/glm-4-7-flash)
- GLM-4.7-Flash (jan 2026, 31B/3B, MIT): GPQA 75.2, HLE 14.4 — svakere enn baseline — [DataLearner](https://www.datalearner.com/en/benchmark-compare/qwen3-6-35b-a3b/glm-4-7-flash)
- Nemotron 3 Super: 120B/12B aktiv, hybrid Mamba-Transformer LatentMoE, opptil 1M kontekst; BF16/FP8/NVFP4-sjekkpunkter på HF — [vLLM blog, 11. mars 2026](https://vllm.ai/blog/nemotron-3-super); GPQA 79.2, AIME 90.2 — [Thunder Compute (okt 2026)](https://www.thundercompute.com/blog/best-open-source-llms)
- Mistral Small 4: 119B/6.5B aktiv MoE, Apache 2.0, ~111 GB FP8, ~75 GB 4-bit (mars 2026) — [Thunder Compute](https://www.thundercompute.com/blog/best-open-source-llms)
- Qwen3.5-122B-A10B (feb 2026, 122B/10B aktiv, Apache 2.0) — [Codersera](https://codersera.com/blog/qwen-3-8-model-lineup-2026/); en bruker rapporterer at 122B-A10B slo Qwen3.8-27B "in the real world" selv om 27B vant hans benchmark — [Medium (anekdotisk)](https://medium.com/@nexusstudio27/qwen3-8-27b-model-won-my-benchmark-then-the-qwen-3-5-122b-model-crushed-it-in-the-real-world-73ba81407f91)
- LMArena tekst (okt 2026-snapshot, sekundærkilde): beste åpne er Kimi K3 (#12, 1500), GLM-5.3 (#19), GLM-5.2 (#34, 1483), DeepSeek V4 Pro (#38, 1461), DeepSeek V4 Flash (#48, 1441) — alle for store for ett kort — [Swfte](https://www.swfte.com/fr/ai/lmarena-ai)
- For store for 96 GB: GLM-5.2 744B/40B (MIT) — AA 51 på v4.1 (juni 2026), GPQA 89, HLE 40, Tau3 banking 27 — [AA, 16. juni 2026](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index); DeepSeek V4-Flash 284B/13B "2x H100 minimum"; Kimi K3 2.8T — [Thunder Compute](https://www.thundercompute.com/blog/best-open-source-llms)

### Inferences
- Kortliste (passer på 96 GB), rangert for orkestrator-rollen:
  1. **Qwen3.8-27B** (dense, Apache 2.0) — best dokumentert intelligens/agentisk score i klassen, IFBench 79.5, samme parser-økosystem som baseline.
  2. **Gemma 4 31B** (dense, Apache 2.0) — høyest Arena Elo (1452) og τ2 76.9 i klassen; sterk chat-kvalitet.
  3. **Qwen3.5-122B-A10B** (MoE, Apache 2.0) i NVFP4/INT4 — mer kunnskap (større total), rask (10B aktiv); eldre generasjon.
  4. **Nemotron 3 Super 120B-A12B** NVFP4 (NVIDIA Open) — bygget for multi-agent/verktøy, 1M kontekst, hybrid Mamba gir lite KV-cache.
  5. **Gemma 4 26B-A4B** (MoE) — svært rask, men τ2 68.2 vs 76.9 for 31B.
  6. **Mistral Small 4 119B-A6.5B** (Apache 2.0) i 4-bit — kun 6.5B aktiv; mangler gode uavhengige tall.
  7. (Usikker) Qwen3.8-Flash-Next hvis vekter faktisk er åpne og ~125B total — sjekk HF før vurdering; lisens restriktiv for MaaS.
- Qwen3.8-27B vs baseline: GPQA 89.2 vs 84.85, HLE 30.8 vs 21.4 — tydelig bedre på resonnering. Prisen er at dense 27B gir lavere tok/s enn 3B-aktiv MoE.

### Gaps
- Fant ingen BFCL v3/v4-tall for noen av kandidatene i okt 2026 (BFCL-leaderboard ble ikke nådd).
- Ingen τ2-bench/IFBench for Qwen3.6-35B-A3B, Nemotron 3 Super eller Mistral Small 4 funnet i kildene som ble hentet.
- gpt-oss-120b (MXFP4, ~63 GB): ingen ferske 2026-benchmarks hentet; trolig forbigått av Qwen3.8-27B, men ikke verifisert.
- LMArena-plassering for Qwen3.8-27B ble ikke funnet.

## 2. Kandidatdetaljer: parametere, arkitektur, kontekst, lisens, kvantisering og KV-plass

### Takeaway
Dense 27–31B-modeller passer i BF16 (54–62 GB) med 30–40 GB til KV, eller i FP8 med ~60 GB til KV. 120B-klassen MoE krever 4-bit (NVFP4/AWQ/MXFP4, ~60–75 GB) og gir 20–35 GB KV.

### Cited Findings
- Qwen3.8-27B: dense, 262K native → 1M med YaRN, Apache 2.0 — [Codersera](https://codersera.com/blog/qwen-3-8-model-lineup-2026/); AA oppgir 260k — [AA](https://artificialanalysis.ai/models/qwen3-8-27b). NVFP4-variant finnes hos tredjepart — [Friendli Qwen3.8-27B-NVFP4](https://friendli.ai/models/gittensor-model-hub/Qwen3.8-27B-NVFP4)
- Gemma 4: 31B dense; 26B-A4B ~3.8B aktiv — [Gemma4all](https://gemma4all.com/blog/gemma-4-benchmarks-performance)
- Qwen3.6-35B-A3B: 35B/3B, 200K kontekst (DataLearner); NVFP4-variant fra RedHatAI — [DataLearner](https://www.datalearner.com/en/benchmark-compare/qwen3-6-35b-a3b/glm-4-7-flash), [Friendli/RedHatAI](https://friendli.ai/models/RedHatAI/Qwen3.6-35B-A3B-NVFP4)
- Nemotron 3 Super: 120B/12B, hybrid Mamba-Transformer, 1M kontekst, BF16/FP8/NVFP4 offisielt — [vLLM blog](https://vllm.ai/blog/nemotron-3-super)
- Mistral Small 4: ~75 GB 4-bit — [Thunder Compute](https://www.thundercompute.com/blog/best-open-source-llms)
- Qwen3-32B NVFP4 vs BF16 på RTX PRO 6000: GPQA 0.3939 vs 0.3939, FP8 0.3889 — "no statistically meaningful regression" (mai 2026) — [JarvisLabs](https://jarvislabs.ai/blog/nvfp4-rtxpro-6000)

### Inferences (egne estimater, ikke målt)
- Vektstørrelse ≈ params × byte/param: 27B BF16 ≈ 54 GB, FP8 ≈ 28 GB, NVFP4 ≈ 16 GB; 31B BF16 ≈ 62 GB, FP8 ≈ 32 GB; 120–122B NVFP4/INT4 ≈ 62–70 GB.
- Med `gpu-memory-utilization 0.92` (~88 GB brukbart): Qwen3.8-27B FP8 → ~55 GB KV; BF16 → ~30 GB KV. Dersom Qwen3.8 beholder Qwen3.5/3.6-hybriden (Gated DeltaNet + noen få full-attention-lag) er KV per token svært lav og full 262K kontekst er realistisk selv i BF16 — arkitekturen for 3.8 er ikke verifisert i kildene.
- Gemma 4 31B (antatt full/sliding-attention-blanding som Gemma 3) har tyngre KV; i BF16 trolig ~128K enkeltsesjon, FP8 anbefales.
- Nemotron 3 Super NVFP4: ~20–25 GB KV igjen, men Mamba-lag gjør at lang kontekst (flere hundre k) likevel får plass.
- 122B-A10B / Mistral Small 4 i 4-bit: 15–25 GB KV, nok for 64–128K for én til få samtidige brukere.

### Gaps
- Nøyaktige config-verdier (antall KV-heads, lag, hybrid-andel) for Qwen3.8-27B og Gemma 4 ble ikke hentet — KV-estimater bør regnes ut fra config.json.
- Lisens for Nemotron 3 Super oppgis kun som "NVIDIA Open" — vilkår ikke lest.

## 3. vLLM/SGLang-støtte og FP8/NVFP4 på sm_120

### Takeaway
NVFP4 for MoE på sm_120 har vært ustabilt i 2026: native CUTLASS/FlashInfer grouped-GEMM feilet (søppel-output/NaN), mens Marlin W4A16-fallback fungerer. NVFP4/FP8 for dense modeller er rapportert å fungere på RTX PRO 6000. Det tryggeste valget for et 96 GB-kort er derfor en dense modell i FP8/BF16.

### Cited Findings
- 11. april 2026, SM120 (4× RTX PRO 6000), nvidia/Qwen3.5-397B-A17B-NVFP4: Marlin W4A16 virker (50.5 tok/s, TP=4); FlashInfer CUTLASS NVFP4 — alle 80 TMA WS grouped-GEMM-taktikker feiler, søppel/degradert; vLLM native CUTLASS ~5 tok/s søppel; SGLang 0.5.8 gir NaN. Rotårsak CUTLASS issue #3096; patcher FlashInfer PR #2725, vLLM PR #36453 "enable compilation but don't resolve underlying kernel failures"; MTP gir 22 % straff på Marlin — [vLLM forum](https://discuss.vllm.ai/t/sm120-rtx-pro-6000-nvfp4-moe-performance-report-qwen3-5-397b/2536)
- vLLM PR #41834 (stabil preview-tag 2026-08-09): DeepSeek V4 Flash på SM120/SM121 med MXFP4 og NVFP4, krever FlashInfer ≥0.6.15.post1 med SM120 sparse-MLA-kjerner, PyTorch 2.13.0 — viser at sm_120-støtte i aug 2026 fortsatt kom via egne PR-er — [GitHub vLLM #41834](https://github.com/vllm-project/vllm/pull/41834)
- Dense Qwen3-32B på RTX PRO 6000 i vLLM (mai 2026): BF16 869 tok/s, FP8 1 340 tok/s, NVFP4 1 824 tok/s aggregert ved concurrency 64 — dvs. FP8 og NVFP4 dense fungerer på kortet — [JarvisLabs](https://jarvislabs.ai/blog/nvfp4-rtxpro-6000)
- Qwen3.8 deploy-flagg: `--reasoning-parser qwen3 --tool-call-parser qwen3_coder` for både vLLM og SGLang — [GitHub QwenLM/Qwen3.8](https://github.com/QwenLM/Qwen3.8)
- Nemotron 3 Super: `--tool-call-parser qwen3_coder --reasoning-parser nemotron_v3 --enable-auto-tool-choice`, vLLM 0.17.1+ — [vLLM blog](https://vllm.ai/blog/nemotron-3-super)

### Inferences
- For Qwen3.8-27B/Gemma 4 31B: FP8 (block/per-channel) er lavrisiko på sm_120; NVFP4 dense også ok ifølge JarvisLabs.
- For 120B-MoE-kandidater i NVFP4: test med Marlin-backend eksplisitt og verifiser output-kvalitet (ikke bare at serveren starter); vurder AWQ/GPTQ INT4 (Marlin) som alternativ.

### Gaps
- Fant ikke changelog for vLLM ~0.31 som bekrefter at CUTLASS NVFP4 MoE på sm_120 er fikset; status etter april 2026 er ubekreftet.
- Ingen kilde om Gemma 4 FP8 spesifikt på sm_120.

## 4. Målt tok/s på RTX PRO 6000 / RTX 5090

### Takeaway
Få direkte målinger for kandidatene; nærmeste referanser er gpt-oss-120b (~193 tok/s enkeltstrøm i llama.cpp) og Qwen3-32B dense (869–1 824 tok/s aggregert ved c=64 i vLLM).

### Cited Findings
- RTX PRO 6000, llama.cpp: gpt-oss 120B Q8_0 tg128 193.3 tok/s; ~134 tok/s ved 12k kontekst; ~48 tok/s ved maks kontekst; Llama 3.3 70B Q4 enkeltstrøm i vLLM 30–45 tok/s; 70B AWQ batched 8 425 tok/s aggregert (RTX 5090: 4 570) — [dev.to/runaihome, oppdatert 2026-10-04](https://dev.to/jovan_chan_9500711396d4e6/rtx-pro-6000-blackwell-for-local-ai-in-2026-96gb-gddr7-the-120b-moe-threshold-and-whether-a-k2)
- Qwen3-32B dense, vLLM, c=64: BF16 869 / FP8 1 340 / NVFP4 1 824 tok/s — [JarvisLabs, mai 2026](https://jarvislabs.ai/blog/nvfp4-rtxpro-6000)

### Inferences
- Båndbredde-estimat (~1.8 TB/s): Qwen3.8-27B FP8 enkeltstrøm ≈ 45–60 tok/s, BF16 ≈ 25–30 tok/s; 120B-MoE med 10–12B aktiv i 4-bit ≈ 100–150 tok/s; baseline 3B-aktiv ≈ 150–200+ tok/s. En orkestrator som byttes fra 35B-A3B til 27B dense blir altså merkbart tregere per token.

### Gaps
- Ingen målte tok/s for Qwen3.8-27B, Gemma 4 31B, Nemotron 3 Super eller Qwen3.5-122B på én RTX PRO 6000 funnet.
