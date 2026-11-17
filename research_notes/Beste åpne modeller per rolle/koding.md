# Best open-weight coding / agentic-coding LLMs for ONE RTX PRO 6000 Blackwell (96 GB, sm_120), October 2026

Research date: 2026-10-06. Baseline: Qwen3.6-35B-A3B. Almost all benchmark numbers are **vendor-reported** (model cards). Each vendor uses its own harness, so the numbers are not directly comparable across vendors. I found no independent SWE-bench bash-only (mini-SWE-agent) numbers for the 2026 mid-size models, because the swebench.com page did not render the table.

## Q1: Which models exist and what do they score (SWE-bench Verified/Pro/Multilingual, Terminal-Bench, LiveCodeBench, BFCL)?

### Takeaway
The strongest candidates that realistically fit on one 96 GB card are **Qwen3.8-27B** (dense, Aug 2026: SWE-bench Pro 61.7, TB 2.1 73.0, LCB v6 90.3) and **Qwen3.8-Flash-Next** (125B/6B active plus a 51B n-gram table, Aug 2026: SWE-Pro 62.5, SWE-Multilingual 81.0, LCB 91.9). Flash-Next only fits on one card if the n-gram table sits in system RAM, and it does not have an Apache license. After those two come Qwen3.6-27B, the baseline Qwen3.6-35B-A3B, Qwen3.5-122B-A10B and Qwen3-Coder-Next. gpt-oss-120b, Nemotron 3 Super and Devstral Small 2 clearly trail on agentic coding.

### Cited Findings
**Baseline: Qwen3.6-35B-A3B** (35B/3B active, Apache 2.0, April 2026, 262K native ctx, up to ~1M)
- SWE-bench Verified 73.4, SWE-bench Multilingual 67.2, SWE-bench Pro 49.5, Terminal-Bench 2.0 51.5, LiveCodeBench v6 80.4 (vendor) — [HF model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)

**Qwen3.8-27B** (dense 27B, Apache 2.0, released 2026-08-14, 262K ctx, up to 1M)
- SWE-bench Pro 61.7, Terminal-Bench 2.1 73.0, LiveCodeBench v6 90.3, DeepSWE 1.1 42.2, NL2Repo 42.3. Comparisons on the same card: Qwen3.6-27B scores 53.5 / 63.4 / 83.9; "Opus4.6 Max" scores 53.4 / 78.2 / 88.8 — [HF model card](https://huggingface.co/Qwen/Qwen3.8-27B)
- SWE-bench Multilingual 73.8 (from the Flash-Next card's comparison column) — [HF Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- Release date and the open model list (only 27B and 2.4T-A95B in the Qwen3.8 repo) — [GitHub QwenLM/Qwen3.8](https://github.com/QwenLM/Qwen3.8)
- Note: TB 2.1 for Qwen3.6-27B is 63.4 on the Qwen3.8 card but 59.3 (TB 2.0) on the Qwen3.6-27B card. The two are different benchmark versions.

**Qwen3.8-Flash-Next** (125B total / 6B active plus 51B n-gram embeddings = 176B; 512 experts; Gated DeltaNet + "Qwen Sparse Attention"; license **qwen-community-1.0**, not Apache; released 2026-08-26)
- SWE-bench Pro 62.5, SWE-bench Multilingual 81.0, LiveCodeBench v6 91.9, DeepSWE 1.1 58.7 — [HF model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- The license restricts large products and model-as-a-service use; weights are ~360 GB in BF16; also CoWorkBench 73.9 and Toolathlon Verified 73.5 — [DataNorth](https://datanorth.ai/news/alibaba-releases-qwen3-8-flash-next)
- No SWE-bench Verified or Terminal-Bench numbers found on the card.

**Qwen3.6-27B** (dense, Apache 2.0, April 2026, 262K ctx)
- SWE-bench Verified 77.2, Pro 53.5, Multilingual 71.3, Terminal-Bench 2.0 59.3, LCB v6 83.9. Harness: "internal agent scaffold (bash + file-edit tools), temp 1.0, top_p 0.95, 200K ctx"; TB 2.0 used Harbor/Terminus-2 with a 3h timeout. Qwen says it "corrected" some SWE-Pro tasks — [HF model card](https://huggingface.co/Qwen/Qwen3.6-27B)

**Qwen3.5-122B-A10B** (122B/10B active, Apache 2.0, Feb 2026, 262K ctx)
- SWE-bench Verified 72.0, Terminal-Bench 2 49.4, LCB v6 78.9, **BFCL-V4 72.2**, TAU2-Bench 79.5. The same card lists GPT-OSS-120B at TB2 18.7 — [HF model card](https://huggingface.co/Qwen/Qwen3.5-122B-A10B)

**Qwen3-Coder-Next** (80B/3B active, Apache 2.0, 2026-02-03, 256K ctx)
- SWE-bench Verified 70.6, SWE-bench Pro 44.3, Terminal-Bench 2.0 36.2 — [HF model card](https://huggingface.co/Qwen/Qwen3-Coder-Next)

**gpt-oss-120b** (117B/5.1B active, Apache 2.0, MXFP4 native, 131K ctx; older model from Aug 2025)
- 62.4% SWE-bench Verified as published by OpenAI, but only ~26% on the official SWE leaderboard. The paper attributes the gap to harness mismatch: undisclosed in-distribution tools such as `apply_patch`, and Harmony→Chat Completions conversion. With conversion, context overflowed far more often (Harmony avoided overflow in 97.2% vs 37.8%) — [arXiv 2604.00362 "In harmony with gpt-oss"](https://www.alphaxiv.org/abs/2604.00362.md)
- SWE-bench Pro 16.2% — [Morph best open-source LLM (updated 2026-10-03)](https://www.morphllm.com/best-open-source-llm)
- Terminal-Bench 2: 18.7 (Qwen's comparison) — [HF Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B)

**Nemotron 3 Super** (120B/12B active, hybrid Mamba-Transformer MoE, NVIDIA Nemotron Open Model License, 2026-03-11, up to 1M ctx)
- Terminal Bench (hard subset) 24.48, LiveCodeBench v6 78.44. SWE-bench Verified (OpenHands) is mentioned but I found no number in the extracted text — [HF NVFP4 card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4)
- Paper figure: Terminal Bench Hard 22.8 vs Qwen3.5-122B 19.0 vs GPT-OSS-120B 24.5; Tau2 25.8 vs 24.0; claims 2.2× (vs gpt-oss-120b) and 7.5× (vs Qwen3.5-122B) throughput on B200 at 8k in / 64k out — [arXiv 2604.12374](https://arxiv.org/pdf/2604.12374)

**Devstral Small 2** (24B dense, Apache 2.0, Dec 2025, "2512", 256K ctx; older)
- SWE-bench Verified 68.0, Multilingual 55.7, Terminal-Bench 2 22.5. **Devstral 2 (123B dense)**: 72.2 / 61.3 / 32.6 — [HF model card](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512)

**Too large for one 96 GB card (for context only)**: Kimi K3 2.8T/104B (TB 2.1 88.3), DeepSeek-V4.1-Flash 552B (TB 90.6, vendor), GLM-5.3 753B (88.2), GLM-5.3-Flash 320B/18B (MIT), MiniMax M3 428B/23B (SWE-Pro 59.0), DeepSeek-V4-Pro 1.6T (SWE-V 80.6) — [Morph](https://www.morphllm.com/best-open-source-llm); Qwen3.8-2.4T-A95B — [GitHub QwenLM/Qwen3.8](https://github.com/QwenLM/Qwen3.8)

### Inferences
- Ranking for one 96 GB card, by vendor numbers and practicality: (1) Qwen3.8-27B, (2) Qwen3.8-Flash-Next (only with ≥100 GB free system RAM and if the license is acceptable), (3) Qwen3.6-27B, (4) Qwen3.6-35B-A3B (baseline, fastest), (5) Qwen3.5-122B-A10B (best BFCL documentation, but weaker than the 27B models on SWE/TB), (6) Qwen3-Coder-Next. gpt-oss-120b, Nemotron 3 Super and Devstral are not competitive on agentic coding by 2026 standards.
- Versus the baseline, Qwen3.8-27B gains about +12 points on SWE-Pro and about +20 on Terminal-Bench (note: TB 2.0 vs 2.1 differ).
- The older models in the original list (Qwen3-Coder-30B-A3B, GLM-4.5/4.6/4.7-Air, Seed-OSS-36B, KAT-Dev, MiniMax-M2) are superseded by the Qwen3.6/3.8 generation. I did not re-verify them in this round.

### Gaps
- No independent, same-harness numbers (swebench.com bash-only, Terminal-Bench leaderboard, Aider Polyglot) for Qwen3.8-27B or Flash-Next. The swebench.com table did not render, and I did not reach the Aider or TB leaderboards.
- SWE-bench Verified is missing for Qwen3.8-27B and Flash-Next (Qwen appears to have switched to SWE-Pro, Multilingual and DeepSWE).
- I found no SWE-bench Verified number for Nemotron 3 Super.
- BFCL is missing for most models; only Qwen3.5-122B-A10B has BFCL-V4 (72.2).
- I did not find Gemma 4 31B coding numbers beyond the Qwen card (SWE-V 52.0, TB2 42.9 in the Qwen3.6-35B card) — [HF](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)

## Q2: Fit on 96 GB (quant + KV/context), sm_120 kernel status in vLLM/SGLang, and tok/s

### Takeaway
All Qwen 27B/35B models fit in BF16 or FP8 with full 262K context, because the hybrid DeltaNet architecture gives a very small KV cache. 120B-class MoEs need NVFP4/MXFP4. On sm_120, the NVFP4 MoE path has historically been unstable (CUTLASS TMA bug; Marlin W4A16 is the safe fallback), so FP8 or BF16 on the smaller Qwen models is the low-risk choice.

### Cited Findings
- Jarvislabs (2026-06-25) on one RTX PRO 6000 with vLLM at full 256K ctx: Qwen3.6-27B ~216 tok/s (summed across concurrent users), 35B-A3B FP8 had the highest throughput, Coder-Next 80B FP8 degraded beyond 32 users. FP8 matched the original 94–97% of the time (KL test); NVFP4 88–90% while freeing 35–41% memory. Recommendation: "Qwen3.6-35B-A3B in FP8" for cost/speed, 27B for quality — [Jarvislabs](https://jarvislabs.ai/blog/coding-model-rtx-pro-6000)
- Qwen3.8-27B decode (community, Sept 2026): single RTX PRO 6000 70–100 tok/s depending on quant; RTX 5090 NVFP4 140–180 tok/s; dual PRO 6000 bf16 105–110 tok/s. One user hit "MTP related errors" and ran unquantized instead — [r/LocalLLaMA snapshot 2026-09-04](https://reddit.sentinel-team.org/posts/1w4k3ai/snapshots/2026-09-04T21%3A20%3A12.3645Z)
- Community quants exist: Qwen3.8-27B FP8, NVFP4, MTP-NVFP4 and INT8-W8A16-MTP — [HF sakamakismile MTP-NVFP4](https://huggingface.co/sakamakismile/Qwen3.8-27B-MTP-NVFP4), [HF Chungulus FP8](https://huggingface.co/Chungulus/Qwen3.8-27B-FP8)
- Qwen3.8-Flash-Next NVFP4 on **one** RTX PRO 6000 (2026-08-28): requires ~100 GB of free system RAM for the 51B n-gram table. vLLM gives 81–88 tok/s without MTP and 120–173 tok/s with MTP; prefill ~12k tok/s; 6 clients 341 tok/s aggregate; max ctx 268K without MTP (404K KV) and 200K with MTP. vLLM does not support KV offload to RAM — [Level1Techs forum](https://forum.level1techs.com/t/qwen-3-8-flash-next-nvfp4-on-a-single-rtx-pro-6000-and-system-memory/254579)
- vLLM v0.29.0 added Qwen3.8-Flash-Next with BF16/FP8/NVFP4 + MTP and made Model Runner V2 the default. v0.30.0 (Sept 22, 2026) added Flash-Next optimizations and "FlashInfer CuTeDSL NVFP4 W4A16 default over Marlin on **SM100/103**". The release notes did not mention SM120 — [vLLM releases](https://github.com/vllm-project/vllm/releases). (The fetch showed the year as 2024, evidently a parsing error; the content describes 2026 models. I found no v0.31 notes.)
- sm_120 NVFP4 MoE (forum report, Qwen3.5-397B NVFP4, TP=4): only Marlin W4A16 (`VLLM_MOE_FORCE_MARLIN=1`) is fast and correct (50.5 tok/s). FlashInfer CUTLASS NVFP4 fails all 80 TMA warp-specialized tactics (garbage or 6–41 tok/s), vLLM native CUTLASS gives ~5 tok/s with corrupt output, the FlashInfer sampler gives an 8.6× regression, and SGLang 0.5.8 gives NaN. Root cause is CUTLASS issue #3096. MTP should be disabled on the Marlin path (−22%). Recommended `--kv-cache-dtype fp8_e4m3` — [discuss.vllm.ai](https://discuss.vllm.ai/t/sm120-rtx-pro-6000-nvfp4-moe-performance-report-qwen3-5-397b/2536) (date not stated; older vLLM version, early 2026)
- vLLM v0.15.0 regression: NVFP4 MoE (e.g., MiniMax-M2.1-NVFP4) refused on SM12.0 because the capability check matched only family 100; v0.14.0 worked — [vLLM #33416](https://github.com/vllm-project/vllm/issues/33416) (old issue, early 2026)
- Nemotron 3 Super NVFP4: requires vLLM ≥0.20.0 and `--kv-cache-dtype fp8`. Supported GPUs listed as B200 / DGX Spark / Hopper / "Blackwell"; RTX PRO 6000 is not explicitly named — [HF NVFP4 card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4). Memory at 4-bit ~64–72 GB — [Unsloth](https://unsloth.ai/docs/models/nemotron-3/nemotron-3-super)
- gpt-oss-120b MXFP4 (native) fits with the full 131K ctx on one card, ~196 tok/s on PRO 6000 (engine not specified) — [RunAIHome 2026-08-20](https://runaihome.com/blog/best-local-llm-96gb-vram-2026/)
- Qwen3.6-35B-A3B: DGX Spark (sm_121) 53–78 tok/s single stream on vLLM 0.19–0.20 — [NVIDIA forum](https://forums.developer.nvidia.com/t/qwen-qwen3-6-35b-a3b-and-fp8-has-landed/366822?page=9). A DFlash speculative-decoding guide for RTX PRO 6000 (vLLM nightly) exists — [Yotta Labs](https://www.yottalabs.ai/post/how-to-run-qwen3-6-35b-a3b-on-a-single-gpu-rtx-pro-6000-guide.md)

### Inferences (my estimates, not verified against config.json)
- Weights: Qwen3.6-35B-A3B BF16 ~70 GB / FP8 ~35 GB; Qwen3.6/3.8-27B BF16 ~54 GB / FP8 ~28 GB; Qwen3-Coder-Next FP8 ~80 GB (tight) / NVFP4 ~45 GB; Qwen3.5-122B-A10B NVFP4 ~65–70 GB; Nemotron 3 Super NVFP4 ~65–72 GB; gpt-oss-120b MXFP4 ~63 GB; Devstral Small 2 FP8 ~24 GB.
- KV cache at FP8 (assuming Qwen3.5/3.6 hybrid with 1 in 4 full-attention layers, 2–4 KV heads × 256 dim): 35B-A3B ≈ 10 KB/token (262K ≈ 2.7 GB); 27B ≈ 32 KB/token (262K ≈ 8.5 GB). In practice the full 262K context fits with plenty of headroom for parallel sessions. Devstral Small 2 (classic GQA, 40 layers × 8 KV × 128) ≈ 80 KB/token, so 256K ≈ 21 GB. gpt-oss-120b (half sliding-window) ≈ 18 KB/token FP8.
- Safest sm_120 choice: BF16 or FP8 on the dense 27B, or FP8 on the 35B-A3B. NVFP4 MoE (120B class, Flash-Next) requires testing the Marlin fallback.
- Dense 27B is memory-bandwidth bound (~1.8 TB/s), roughly 3× slower decode than 35B-A3B. MTP / DFlash spec-decode recovers much of that.

### Gaps
- I could not verify whether vLLM 0.30/0.31 fixed native CUTLASS NVFP4/FP8 grouped-GEMM on SM120. The release notes mention only SM100/103.
- No measured single-stream tok/s for Qwen3.8-27B FP8 with a vLLM version and flags on the PRO 6000 (the community range is 70–100).
- No tok/s for Qwen3.5-122B-A10B or Nemotron 3 Super on a single PRO 6000.

## Q3: Tool-call parsers in vLLM and known problems

### Takeaway
All Qwen candidates (3.5/3.6/3.8, Coder-Next) and Nemotron 3 Super use `--tool-call-parser qwen3_coder` (with `--reasoning-parser qwen3` or `super_v3`). Devstral uses `mistral`. gpt-oss uses Harmony, and Chat Completions conversion hurts agentic results measurably.

### Cited Findings
- Qwen3.6-35B-A3B: `--reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser qwen3_coder`, same in SGLang — [HF](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
- Qwen3.8-27B: same flags (vLLM and SGLang) — [GitHub QwenLM/Qwen3.8](https://github.com/QwenLM/Qwen3.8)
- Qwen3.5-122B-A10B: `qwen3_coder` — [HF](https://huggingface.co/Qwen/Qwen3.5-122B-A10B); Qwen3-Coder-Next: `qwen3_coder`, vLLM ≥0.15.0 — [HF](https://huggingface.co/Qwen/Qwen3-Coder-Next)
- Nemotron 3 Super: `--reasoning-parser super_v3 --tool-call-parser qwen3_coder` — [HF](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4)
- Devstral Small 2: `--tool-call-parser mistral --enable-auto-tool-choice` — [HF](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512)
- Qwen3.8-Flash-Next: the card shows only `vllm serve "Qwen/Qwen3.8-Flash-Next"`, with no parser specified — [HF](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- Known problem with Qwen3.6-35B-A3B: tool calls end up as XML inside `thinking_content` instead of being parsed, which a correct chat template fixes. Loops / "change of plan" in long contexts across FP8/INT4/NVFP4; the suggested mitigation (repetition_penalty 1.1, temp 0.4) stops helping above ~30K ctx — [NVIDIA forum](https://forums.developer.nvidia.com/t/qwen-qwen3-6-35b-a3b-and-fp8-has-landed/366822?page=9)
- Security: the qwen3_coder parser used `eval()`, giving RCE (CVSS 8.8) in vLLM 0.10.0–0.10.1, fixed in 0.10.1.1. Not relevant for 0.30+ — [OSV PYSEC-2026-2014](https://osv.dev/vulnerability/PYSEC-2026-2014)
- gpt-oss: no backend offers a native Harmony API, and conversion to Chat Completions distorts output and context usage — [arXiv 2604.00362](https://www.alphaxiv.org/abs/2604.00362.md)

### Inferences
- Since all the top candidates share `qwen3_coder` + `qwen3`, switching models on the same harness is cheap (same serve flags).
- Tool-calling robustness should be tested in the actual harness (OpenHands / Claude-Code-style). Vendor SWE numbers come from internal scaffolds.

### Gaps
- I found no specific open vLLM issues on qwen3_coder parsing for Qwen3.8 (Sept–Oct 2026).
- Parser and reasoning-parser for Qwen3.8-Flash-Next are not documented on the card.
