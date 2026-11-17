# Bildegenerering (tekst-til-bilde og bilderedigering) – åpne vekter på ett RTX PRO 6000 Blackwell (96 GB, sm_120), oktober 2026

## 1. Hvilke åpne modeller leder rangeringene nå?

### Takeaway
Per oktober 2026 leder Qwen-Image-2.1 (Alibaba, 20. sep 2026) blant åpne vekter på Artificial Analysis både for tekst-til-bilde (Elo 1036) og redigering (Elo 1073), fulgt av HunyuanImage 3.0 Instruct (redigering), Qwen-Image-Edit-2511, FLUX.2 [klein] 9B og FLUX.2 [dev]. Lukkede modeller (GPT Image 2, Gemini, Grok, MAI) ligger klart foran alle åpne modeller.

### Cited Findings
- AA-Image-T2I v2.0, filter «open weights»: Qwen-Image-2.1 Elo 1036 (totalrang 18, sep 2026), FLUX.2 [dev] 1000 (rang 42, nov 2025), FLUX.2 [dev] Turbo 997, FLUX.2 [dev] Flash 987, FLUX.2 [klein] Base 9B 902 (rang 99), FLUX.2 [klein] 4B 863, FLUX.1 [schnell] 803. Siden sier «Qwen-Image-2.1 currently leads among open weights models». — [Artificial Analysis T2I, open weights](https://artificialanalysis.ai/image/leaderboard/text-to-image?open-weights=true) (hentet 6. okt 2026)
- Samme uttrekk listet også «Ideogram 4.0» (1011/1004) og «Cosmos3-Super-Text2Image» (987, oppgitt som Alibaba) under åpne vekter — dette er usikkert/mulig feil i uttrekket (Ideogram har ikke kjent åpne vekter; Cosmos er NVIDIA-navn). Ikke bekreftet. — [Artificial Analysis T2I](https://artificialanalysis.ai/image/leaderboard/text-to-image?open-weights=true)
- Speil av AA-data: 20 åpne modeller fra Qwen-Image-2.1 (1036, rang 1) ned til FLUX.1 [dev] (841, rang 20). — [The Open Weights](https://theopenweights.com/leaderboards/text-to-image)
- AA-Image-Editing v2.0, åpne vekter: 1) Qwen-Image-2.1 1073±99 (sep 2026), 2) HunyuanImage 3.0 Instruct 1066±99 (jan 2026), 3) Qwen Image Edit Plus 2511 1021±89 (nov 2025), 4) FLUX.2 [klein] 9B 1013±89 (jan 2026), 5) FLUX.2 [dev] Turbo (fal) 1001±89, 6) FLUX.2 [dev] 1000 (referanse), 7) FLUX.2 [dev] Flash 997±89, 8) Qwen Image Edit Plus 2509 981±79. Merk store konfidensintervall (±79–99) — de øverste plassene er statistisk ikke skilt. — [AA Image Editing, open weights](https://artificialanalysis.ai/image/leaderboard/editing/open-weights)
- LMArena tekst-til-bilde (data 27. des 2025 — eldre): GPT Image 1.5 1264, Gemini 3 Pro Image 1235, Flux 2 Max 1168 … Hunyuan Image 3.0 1152 (rang 7), Flux 2 Dev 1149 (rang 8). — [WaveSpeed om LMArena](https://wavespeed.ai/blog/posts/lm-arena-text-to-image-rankings-2026/)
- Image Arena (TrueSkill, oppdatert 4. okt 2026): topp 3 er GPT Image 2, Grok Imagine Image 2.0, MAI-Image-2.5 — alle lukkede; åpne modeller er ikke på topp. — [llm-stats](https://llm-stats.com/leaderboards/best-ai-for-image-generation)
- Qwen-Image-2512 (des 2025) hevdes å være «the strongest open-source model» i Alibabas AI Arena over 10 000+ runder (egen påstand). — [HF Qwen-Image-2512](https://huggingface.co/Qwen/Qwen-Image-2512)
- Z-Image-Turbo: «competitive Elo» i Alibaba AI Arena blant topp åpne modeller (ingen tall i kortet). — [HF Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)
- Qwen-Image-2.1: ingen uavhengige benchmarktall (GenEval/DPG/GEdit) ved publisering; modellkortet oppgir ingen benchmarktall. — [andrew.ooo](https://andrew.ooo/answers/qwen-image-2-1-vs-flux-2-dev-vs-gpt-image-2-5-vs-nano-banana-pro-september-2026/); [HF Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)

### Inferences
- Kandidatliste for ett 96 GB-kort: (1) Qwen-Image-2.1 (beste kvalitet, men ikke-kommersiell lisens), (2) Qwen-Image-2512 + Qwen-Image-Edit-2511 (Apache 2.0, best kommersielt brukbare), (3) FLUX.2 [dev] (32B, sterk, ikke-kommersiell), (4) FLUX.2 [klein] 9B/4B (rask; 4B Apache), (5) Z-Image-Turbo (6B, Apache, svært rask), (6) HunyuanImage 3.0 Instruct (sterk redigering, men passer ikke i BF16 og lisensen ekskluderer EU).
- SD 3.5, HiDream, Lumina, Sana, OmniGen2, Bagel dukker ikke opp blant de øverste åpne på AA i 2026 og er i praksis forbigått.

### Gaps
- Fant ikke ferske GenEval/DPG-Bench/GEdit-Bench/ImgEdit-tall per modell i 2026 fra primærkilder i denne runden.
- Fant ikke LMArena image-edit-rangering for åpne modeller med 2026-data.
- Ideogram 4.0 og «Cosmos3-Super» i AA open-weights-filteret er ubekreftet.

## 2. Parametere, VRAM (BF16/FP8/NVFP4) og hastighet

### Takeaway
Alle hovedkandidatene unntatt HunyuanImage 3.0 passer på 96 GB i BF16; FLUX.2 [dev] (32B) er grensetilfellet (~90 GB full last i BF16, ~54 GB i FP8). Konkrete sekund-per-bilde-tall på RTX PRO 6000 ble ikke funnet.

### Cited Findings
- Qwen-Image-2.1: 7B single-stream DiT (32 lag) + Qwen3-VL 8B tekstenkoder + 64-kanals RGBA-VAE; native 2048×2048 ved 40 steg; opptil 10 referansebilder; to 9B prompt-rewriter-sjekkpunkter. — [AI Weekly](https://aiweekly.co/alerts/alibaba-ships-qwen-image-21-7b-dit-with-native-2048x2048-and-rgba-drops-apache); [HF](https://huggingface.co/Qwen/Qwen-Image-2.1)
- Qwen-Image-2.1 kjører på «~24GB, RTX 3090 class» (aggregator, ikke primærkilde); diffusers `QwenImage21Pipeline`, CPU-offload støttet. — [andrew.ooo](https://andrew.ooo/answers/qwen-image-2-1-vs-flux-2-dev-vs-gpt-image-2-5-vs-nano-banana-pro-september-2026/); [HF](https://huggingface.co/Qwen/Qwen-Image-2.1)
- Qwen-Image-2512 og Qwen-Image-Edit-2511: 20B parametere, BF16. — [HF 2512](https://huggingface.co/Qwen/Qwen-Image-2512); [HF Edit-2511](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)
- Qwen-Image-Lightning finnes i 4- og 8-stegs varianter (LoRA). — [Runware 4-steg](https://runware.ai/models/qwen-image-lightning-4-steps); [Runware 8-steg v1.1](https://runware.ai/models/qwenimage-lightning-8-steps-v1-1)
- FLUX.2 [dev]: 32B; BF16 90 GB full last / 64 GB lowVRAM; FP8 gir ~40 % lavere VRAM og ~40 % høyere ytelse (NVIDIA + ComfyUI). 28 steg anbefalt som avveining. — [NVIDIA-blogg 25. nov 2025](https://blogs.nvidia.com/blog/rtx-ai-garage-flux-2-comfyui); [HF FLUX.2-dev](https://huggingface.co/black-forest-labs/FLUX.2-dev)
- FLUX.2 [klein] (15. jan 2026): 4B og 9B, destillert til 4 steg, «under 0.5s on modern hardware»; 4B passer i ~13 GB. FP8 opptil 1,6× raskere/40 % mindre VRAM, NVFP4 opptil 2,7× raskere/55 % mindre VRAM (målt RTX 5080/5090, 1024×1024). — [BFL-blogg](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence)
- Z-Image-Turbo: 6B, 8 NFE, sub-sekund på H800, passer i 16 GB. — [HF Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)
- HunyuanImage 3.0 Instruct: 80B totalt / 13B aktive (MoE, 64 eksperter); anbefalt ≥8×80 GB GPU; 50 steg standard, Distil-variant med 8 steg; CUDA 12.8. — [HF HunyuanImage-3.0-Instruct](https://huggingface.co/tencent/HunyuanImage-3.0-Instruct)
- Nunchaku SVDQuant: 3,6× minnereduksjon vs BF16 for 12B FLUX.1-dev; på RTX 5090 3,1× raskere enn BF16 og NF4. — [Nunchaku GitHub](https://github.com/nunchaku-ai/nunchaku)

### Inferences
- HunyuanImage 3.0: 80B i BF16 ≈ 160 GB → passer ikke på 96 GB; FP8 ≈ 80 GB vekter + aktivasjoner er i beste fall på grensen. Utelukk den for ett kort med mindre en offisiell ≤96 GB-kvantisering finnes.
- FLUX.2 [dev] bør kjøres i FP8 på 96 GB for å få plass til tekstenkoder + VAE + headroom (BF16 90 GB full last etterlater nesten ingenting).
- Qwen-Image-2512 / Edit-2511 (20B) ≈ 40 GB i BF16 for DiT — begge kan ligge lastet samtidig på 96 GB i FP8.

### Gaps
- Ingen målte sekund/bilde for RTX PRO 6000, RTX 5090 eller H100 ble funnet for Qwen-Image-2.1, Qwen-Image-2512, FLUX.2 [dev] eller Z-Image ved 1024×1024. Må måles lokalt.
- Ingen offisielle NVFP4-tall for Qwen-Image-2.1 eller FLUX.2 [dev].

## 3. Lisens – kommersiell bruk

### Takeaway
Kun Qwen-Image-2512, Qwen-Image-Edit-2511, Z-Image-Turbo og FLUX.2 [klein] 4B er Apache 2.0. Qwen-Image-2.1 byttet til ikke-kommersiell forskningslisens; FLUX.2 [dev] og [klein] 9B er FLUX Non-Commercial; HunyuanImage 3.0 ekskluderer EU/UK/Sør-Korea.

### Cited Findings
- Qwen-Image-2.1: «Qwen Research License Agreement», byttet fra Apache 2.0; kommersiell bruk krever egen avtale med Alibaba. — [HF](https://huggingface.co/Qwen/Qwen-Image-2.1); [AI Weekly](https://aiweekly.co/alerts/alibaba-ships-qwen-image-21-7b-dit-with-native-2048x2048-and-rgba-drops-apache)
- Qwen-Image-2512: Apache 2.0. — [HF](https://huggingface.co/Qwen/Qwen-Image-2512)
- Qwen-Image-Edit-2511: Apache 2.0. — [HF](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)
- Z-Image-Turbo: Apache 2.0. — [HF](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)
- FLUX.2 [klein] 4B og Base 4B: Apache 2.0; [klein] 9B og Base 9B: FLUX Non-Commercial License. — [BFL](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence)
- FLUX.2 [dev]: FLUX Non-Commercial License; utdata «can be used for personal, scientific, and commercial purposes», men selve modellen kun ikke-kommersielt; kommersielle vilkår kan kjøpes fra BFL. — [HF FLUX.2-dev](https://huggingface.co/black-forest-labs/FLUX.2-dev); [andrew.ooo](https://andrew.ooo/answers/qwen-image-2-1-vs-flux-2-dev-vs-gpt-image-2-5-vs-nano-banana-pro-september-2026/)
- HunyuanImage 3.0 CLA: territorium «Worldwide … excluding the territory of the European Union, United Kingdom and South Korea»; kommersiell lisens kreves over 100 mill. MAU. — [ScanCode LicenseDB](https://scancode-licensedb.aboutcode.org/tencent-hunyuan-image-3.0-cla.html)

### Inferences
- Norge er EØS, ikke EU; teksten nevner bare EU. Om dette dekker Norge er en juridisk tolkning — behandle Hunyuan som risikabel for drift i Norge.
- For kommersiell drift (f.eks. tjenester under eget enkeltpersonforetak) er Qwen-Image-2512 + Edit-2511 det sterkeste trygge valget; Z-Image-Turbo / klein 4B for fart.

### Gaps
- Fullteksten i Qwen Research License (eksakte begrensninger, f.eks. på utdata) ble ikke lest.

## 4. Programvarestøtte og Blackwell (sm_120)

### Takeaway
diffusers og ComfyUI dekker alle kandidatene; SGLang-Diffusion har day-0 for FLUX.2, Qwen-Image-2512/Edit-2511 og Z-Image-Turbo. Nunchaku NVFP4 (RTX 5090/Blackwell) støtter Qwen-Image/Edit og Z-Image-Turbo offisielt, men ikke FLUX.2 [dev] eller Qwen-Image-2.1.

### Cited Findings
- SGLang-Diffusion (16. jan 2026): «Day-0 support for Flux.2, Qwen-Image-Edit-2511, Qwen-Image-2512, Z-Image-Turbo» + GLM-Image; Cache-DiT opptil 169 % raskere; nunchaku/NVFP4-kvantisering kun på veikart; maskinvare nevnt: AMD, 4090, 5090, MUSA. — [LMSYS-blogg](https://lmsys.org/blog/2026-01-16-sglang-diffusion/)
- Nunchaku: støtter FLUX.1-familien, Qwen-Image, Qwen-Image-Edit, Qwen-Image-Edit-2509, Z-Image-Turbo, SANA; «NVFP4 support on NVIDIA RTX 5090»; v1.2.0 (jan 2026) gir 20–30 % Z-Image-boost, LoRA, ComfyUI 0.7. — [Nunchaku GitHub](https://github.com/nunchaku-ai/nunchaku)
- Community-port: FLUX.2 [klein] 9B i Nunchaku-format. — [HF tonera/FLUX.2-klein-9B-Nunchaku](https://huggingface.co/tonera/FLUX.2-klein-9B-Nunchaku)
- BFL leverer egne FP8- og NVFP4-versjoner av FLUX.2 [klein]. — [BFL](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence)
- FLUX.2 [dev]: diffusers og ComfyUI; FP8 via NVIDIA/ComfyUI. — [HF](https://huggingface.co/black-forest-labs/FLUX.2-dev); [NVIDIA](https://blogs.nvidia.com/blog/rtx-ai-garage-flux-2-comfyui)
- Qwen-Image-2.1: diffusers (`QwenImage21Pipeline`), krever transformers ≥5.17; ComfyUI/SGLang ikke nevnt i kortet. — [HF](https://huggingface.co/Qwen/Qwen-Image-2.1); [andrew.ooo](https://andrew.ooo/answers/qwen-image-2-1-vs-flux-2-dev-vs-gpt-image-2-5-vs-nano-banana-pro-september-2026/)
- HunyuanImage 3.0 Instruct: Transformers, vLLM (fra 30. okt 2025), diffusers; FlashInfer krever ~10 min kernel-kompilering første gang; CUDA 12.8. — [HF](https://huggingface.co/tencent/HunyuanImage-3.0-Instruct)

### Inferences
- NVFP4-ytelsestallene er målt på RTX 5090 (også sm_120), så de bør overføres til RTX PRO 6000 (samme arkitektur), men ikke verifisert.

### Gaps
- Fant ingen dokumenterte sm_120-spesifikke feil for disse modellene i denne runden. vLLM-Omni og xDiT-støtte ble ikke verifisert.

## 5. Ikke-engelske prompter (norsk) og tekst i bilder

### Takeaway
Ingen kilde dokumenterer norsk prompt-følging for noen modell. Qwen- og Z-Image-modellene er eksplisitt sterke på kinesisk/engelsk tekstgjengivelse; Qwen-Image-2.1 bruker en multilingual VLM (Qwen3-VL 8B) som tekstenkoder.

### Cited Findings
- Z-Image-Turbo: «accurate rendering complex Chinese and English text». — [HF](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)
- Qwen-Image-2512: forbedret tekstgjengivelse og layout. — [HF](https://huggingface.co/Qwen/Qwen-Image-2512)
- Qwen-Image-Edit-2511: metadata oppgir engelsk og kinesisk. — [HF](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)
- Qwen-Image-2.1: Qwen3-VL 8B som tekstenkoder; forbedret tekstgjengivelse, infografikk. — [AI Weekly](https://aiweekly.co/alerts/alibaba-ships-qwen-image-21-7b-dit-with-native-2048x2048-and-rgba-drops-apache); [andrew.ooo](https://andrew.ooo/answers/qwen-image-2-1-vs-flux-2-dev-vs-gpt-image-2-5-vs-nano-banana-pro-september-2026/)
- FLUX.2 [dev]: «Strong typography and world knowledge». — [andrew.ooo](https://andrew.ooo/answers/qwen-image-2-1-vs-flux-2-dev-vs-gpt-image-2-5-vs-nano-banana-pro-september-2026/)

### Inferences
- Modeller med LLM/VLM-tekstenkoder (Qwen-familien, FLUX.2) forstår sannsynligvis norske prompter bedre enn CLIP/T5-baserte, men æ/ø/å i bildetekst er udokumentert. Anbefaling: test norsk tekstgjengivelse lokalt, eller oversett prompt til engelsk via LLM (Qwen-Image-2.1 har egne prompt-rewriter-modeller).

### Gaps
- Ingen benchmark eller kilde for norsk prompt-følging eller æ/ø/å-gjengivelse.
- FLUX.2 [dev]s tekstenkoder ble ikke bekreftet fra primærkilde i denne runden.
