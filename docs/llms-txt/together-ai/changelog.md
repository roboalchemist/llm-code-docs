# Source: https://docs.together.ai/docs/changelog.md

# Changelog

## December, 2025

<Update label="Dec 17" description="/deprecations">
  **Model Redirects Now Active**

  The following models are now being automatically redirected to their upgraded versions. See our [Model Lifecycle Policy](/docs/deprecations#model-lifecycle-policy) for details.

  | Original Model | Redirects To       |
  | :------------- | :----------------- |
  | `Kimi-K2`      | `Kimi-K2-0905`     |
  | `DeepSeek-V3`  | `DeepSeek-V3-0324` |
  | `DeepSeek-R1`  | `DeepSeek-R1-0528` |

  These are same-lineage upgrades with compatible behavior. If you need the original version, deploy it as a [Dedicated Endpoint](/docs/dedicated-endpoints).
</Update>

<Update label="Dec 12" description="Python v2 SDK, /jobs, /hardware">
  **Python SDK v2.0 Release Candidate**

  Together AI is releasing the **Python SDK v2.0 Release Candidate** — a new, OpenAPI‑generated, strongly‑typed client that replaces the legacy v1.0 package and brings the SDK into lock‑step with the latest platform features.

  * **`pip install together==2.0.0a9`**
  * **RC Period:** The v2.0 RC window starts today and will run for **approximately 1 month**. During this time we’ll iterate quickly based on developer feedback and may make a few small, well‑documented breaking changes before GA.
  * **Type‑Safe, Modern Client:** Stronger typing across parameters and responses, keyword‑only arguments, explicit `NOT_GIVEN` handling for optional fields, and rich `together.types.*` definitions for chat messages, eval parameters, and more.
  * **Redesigned Error Model:** Replaces `TogetherException` with a new `TogetherError` hierarchy, including `APIStatusError` and specific HTTP status code errors such as `BadRequestError (400)`, `AuthenticationError (401)`, `RateLimitError (429)`, and `InternalServerError (5xx)`, plus transport (`APIConnectionError`, `APITimeoutError`) and validation (`APIResponseValidationError`) errors.
  * **New Jobs API:** Adds first‑class support for the **Jobs API** (`client.jobs.*`) so you can create, list, and inspect asynchronous jobs directly from the SDK without custom HTTP wrappers.
  * **New Hardware API:** Adds the **Hardware API** (`client.hardware.*`) to discover available hardware, filter by model compatibility, and compute effective hourly pricing from `cents_per_minute`.
  * **Raw Response & Streaming Helpers:** New `.with_raw_response` and `.with_streaming_response` helpers make it easier to debug, inspect headers and status codes, and stream completions via context managers with automatic cleanup.
  * **Code Interpreter Sessions:** Adds session management for the **Code Interpreter** (`client.code_interpreter.sessions.*`), enabling multi‑step, stateful code‑execution workflows that were not possible in the legacy SDK.
  * **High Compatibility for Core APIs:** Most core usage patterns, including `chat.completions`, `completions`, `embeddings`, `images.generate`, audio transcription/translation/speech, `rerank`, `fine_tuning.create/list/retrieve/cancel`, and `models.list` — are designed to be **drop‑in compatible** between v1 and v2.
  * **Targeted Breaking Changes:** Some APIs (Files, Batches, Endpoints, Evals, Code Interpreter, select fine‑tuning helpers) have updated method names, parameters, or response shapes; these are fully documented in the **Python SDK Migration Guide** and **Breaking Changes** notes.
  * **Migration Resources:** A dedicated **Python SDK Migration Guide** is available with API‑by‑API before/after examples, a feature parity matrix, and troubleshooting tips to help teams smoothly transition from v1 to v2 during the RC period.
</Update>

<Update label="Dec 8" description="/serverless-models">
  **Serverless Model Bring Ups**

  The following models have been added:

  * `mistralai/Ministral-3-14B-Instruct-2512`
</Update>

## November, 2025

<Update label="Nov 10" description="/serverless-models, /function-calling">
  **Serverless Model Bring Ups**

  The following models have been added:

  * `zai-org/GLM-4.6`
  * `moonshotai/Kimi-K2-Thinking`
</Update>

<Update label="Nov 3" description="/audio/speech, /audio/transcriptions">
  **Enhanced Audio Capabilities: Real-time Text-to-Speech and Speech-to-Text**

  Together AI expands audio capabilities with real-time streaming for both TTS and STT, new models, and speaker diarization.

  * **Real-time Text-to-Speech**: WebSocket API for lowest-latency interactive applications
  * **New TTS Models**: Orpheus 3B (`canopylabs/orpheus-3b-0.1-ft`) and Kokoro 82M (`hexgrad/Kokoro-82M`) supporting REST, streaming, and WebSocket endpoints
  * **Real-time Speech-to-Text**: WebSocket streaming transcription with Whisper for live audio applications
  * **Voxtral Model**: New Mistral AI speech recognition model (`mistralai/Voxtral-Mini-3B-2507`) for audio transcriptions
  * **Speaker Diarization**: Identify and label different speakers in audio transcriptions with a free `diarize` flag
  * TTS WebSocket endpoint: `/v1/audio/speech/websocket`
  * STT WebSocket endpoint: `/v1/realtime`
  * Check out the [Text-to-Speech guide](/docs/text-to-speech) and [Speech-to-Text guide](/docs/speech-to-text)
</Update>

## October, 2025

<Update label="Oct 31" description="/images">
  **Model Deprecations**

  The following image models have been deprecated and are no longer available:

  * `black-forest-labs/FLUX.1-pro` (Calls to FLUX.1-pro will now redirect to FLUX.1.1-pro)
  * `black-forest-labs/FLUX.1-Canny-pro`
</Update>

<Update label="Oct 21" description="/videos, /images">
  **Video Generation API & 40+ New Image and Video Models**

  Together AI expands into multimedia generation with comprehensive video and image capabilities. [Read more](https://www.together.ai/blog/40-new-image-and-video-models)

  * **New Video Generation API**: Create high-quality videos with models like OpenAI Sora 2, Google Veo 3.0, and Minimax Hailuo
  * **40+ Image & Video Models**: Including Google Imagen 4.0 Ultra, Gemini Flash Image 2.5 (Nano Banana), ByteDance SeeDream, and specialized editing tools
  * **Unified Platform**: Combine text, image, and video generation through the same APIs, authentication, and billing
  * **Production-Ready**: Serverless endpoints with transparent per-model pricing and enterprise-grade infrastructure
  * Video endpoints: `/videos/create` and `/videos/retrieve`
  * Image endpoint: `/images/generations`
</Update>

## September, 2025

<Update label="Sep 15" description="/batch_api">
  **Improved Batch Inference API: Enhanced UI, Expanded Model Support, and Rate Limit Increase**

  What’s New

  * Streamlined UI: Create and track batch jobs in an intuitive interface — no complex API calls required.
  * Universal Model Access: The Batch Inference API now supports all serverless models and private deployments, so you can run batch workloads on exactly the models you need.
  * Massive Scale Jump: Rate limits are up from 10M to 30B enqueued tokens per model per user, a 3000× increase. Need more? We’ll work with you to customize.
  * Lower Cost: For most serverless models, the Batch Inference API runs at 50% the cost of our real-time API, making it the most economical way to process high-throughput workloads.
</Update>

<Update label="Sep 13" description="/chat/completions">
  **Qwen3-Next-80B Models Release**

  New Qwen3-Next-80B models now available for both thinking and instruction tasks.

  * Model ID: `Qwen/Qwen3-Next-80B-A3B-Thinking`
  * Model ID: `Qwen/Qwen3-Next-80B-A3B-Instruct`
</Update>

<Update label="Sep 10" description="/fine-tunes">
  **Fine-Tuning Platform Upgrades**

  Enhanced fine-tuning capabilities with expanded model support and increased context lengths. [Read more](https://www.together.ai/blog/fine-tuning-updates-sept-2025)

  **Enable fine-tuning for new large models:**

  * `openai/gpt-oss-120b`
  * `deepseek-ai/DeepSeek-V3.1`
  * `deepseek-ai/DeepSeek-V3.1-Base`
  * `deepseek-ai/DeepSeek-R1-0528`
  * `deepseek-ai/DeepSeek-R1`
  * `deepseek-ai/DeepSeek-V3-0324`
  * `deepseek-ai/DeepSeek-V3`
  * `deepseek-ai/DeepSeek-V3-Base`
  * `Qwen/Qwen3-Coder-480B-A35B-Instruct`
  * `Qwen/Qwen3-235B-A22B` (context length 32,768 for SFT and 16,384 for DPO)
  * `Qwen/Qwen3-235B-A22B-Instruct-2507` (context length 32,768 for SFT and 16,384 for DPO)
  * `meta-llama/Llama-4-Maverick-17B-128E`
  * `meta-llama/Llama-4-Maverick-17B-128E-Instruct`
  * `meta-llama/Llama-4-Scout-17B-16E`
  * `meta-llama/Llama-4-Scout-17B-16E-Instruct`

  ***

  **Increased maximum supported context length (per model and variant):**

  **DeepSeek Models**

  * DeepSeek-R1-Distill-Llama-70B: SFT: 8192 → 24,576, DPO: 8192 → 8192
  * DeepSeek-R1-Distill-Qwen-14B: SFT: 8192 → 65,536, DPO: 8192 → 12,288
  * DeepSeek-R1-Distill-Qwen-1.5B: SFT: 8192 → 131,072, DPO: 8192 → 16,384

  **Google Gemma Models**

  * gemma-3-1b-it: SFT: 16,384 → 32,768, DPO: 16,384 → 12,288
  * gemma-3-1b-pt: SFT: 16,384 → 32,768, DPO: 16,384 → 12,288
  * gemma-3-4b-it: SFT: 16,384 → 131,072, DPO: 16,384 → 12,288
  * gemma-3-4b-pt: SFT: 16,384 → 131,072, DPO: 16,384 → 12,288
  * gemma-3-12b-pt: SFT: 16,384 → 65,536, DPO: 16,384 → 8,192
  * gemma-3-27b-it: SFT: 12,288 → 49,152, DPO: 12,288 → 8,192
  * gemma-3-27b-pt: SFT: 12,288 → 49,152, DPO: 12,288 → 8,192

  **Qwen Models**

  * Qwen3-0.6B / Qwen3-0.6B-Base: SFT: 8192 → 32,768, DPO: 8192 → 24,576
  * Qwen3-1.7B / Qwen3-1.7B-Base: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen3-4B / Qwen3-4B-Base: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen3-8B / Qwen3-8B-Base: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen3-14B / Qwen3-14B-Base: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen3-32B: SFT: 8192 → 24,576, DPO: 8192 → 4096
  * Qwen2.5-72B-Instruct: SFT: 8192 → 24,576, DPO: 8192 → 8192
  * Qwen2.5-32B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 12,288
  * Qwen2.5-32B: SFT: 8192 → 49,152, DPO: 8192 → 12,288
  * Qwen2.5-14B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2.5-14B: SFT: 8192 → 65,536, DPO: 8192 → 16,384
  * Qwen2.5-7B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2.5-7B: SFT: 8192 → 131,072, DPO: 8192 → 16,384
  * Qwen2.5-3B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2.5-3B: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2.5-1.5B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2.5-1.5B: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2-72B-Instruct / Qwen2-72B: SFT: 8192 → 32,768, DPO: 8192 → 8192
  * Qwen2-7B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2-7B: SFT: 8192 → 131,072, DPO: 8192 → 16,384
  * Qwen2-1.5B-Instruct: SFT: 8192 → 32,768, DPO: 8192 → 16,384
  * Qwen2-1.5B: SFT: 8192 → 131,072, DPO: 8192 → 16,384

  **Meta Llama Models**

  * Llama-3.3-70B-Instruct-Reference: SFT: 8,192 → 24,576, DPO: 8,192 → 8,192
  * Llama-3.2-3B-Instruct: SFT: 8,192 → 131,072, DPO: 8,192 → 24,576
  * Llama-3.2-1B-Instruct: SFT: 8,192 → 131,072, DPO: 8,192 → 24,576
  * Meta-Llama-3.1-8B-Instruct-Reference: SFT: 8,192 → 131,072, DPO: 8,192 → 16,384
  * Meta-Llama-3.1-8B-Reference: SFT: 8,192 → 131,072, DPO: 8,192 → 16,384
  * Meta-Llama-3.1-70B-Instruct-Reference: SFT: 8,192 → 24,576, DPO: 8,192 → 8,192
  * Meta-Llama-3.1-70B-Reference: SFT: 8,192 → 24,576, DPO: 8,192 → 8,192

  **Mistral Models**

  * mistralai/Mistral-7B-v0.1: SFT: 8,192 → 32,768, DPO: 8,192 → 32,768
  * teknium/OpenHermes-2p5-Mistral-7B: SFT: 8,192 → 32,768, DPO: 8,192 → 32,768

  ***

  **Enhanced Hugging Face integrations:**

  * Fine-tune any \< 100B parameter CausalLM from Hugging Face Hub
  * Support for DPO variants such as LN-DPO, DPO+NLL, and SimPO
  * Support fine-tuning with maximum batch size
  * Public `fine-tunes/models/limits` and `fine-tunes/models/supported` endpoints
  * Automatic filtering of sequences with no trainable tokens (e.g., if a sequence prompt is longer than the model's context length, the completion is pushed outside the window)
</Update>

<Update label="Sep 9" description="/gpu_cluster">
  **Together Instant Clusters General Availability**

  Self-service NVIDIA GPU clusters with API-first provisioning. [Read more](https://www.together.ai/blog/together-instant-clusters-ga)

  * New API endpoints for cluster management:
    * `/v1/gpu_cluster` - Create and manage GPU clusters
    * `/v1/shared_volume` - High-performance shared storage
    * `/v1/regions` - Available data center locations
  * Support for NVIDIA Blackwell (HGX B200) and Hopper (H100, H200) GPUs
  * Scale from single-node (8 GPUs) to hundreds of interconnected GPUs
  * Pre-configured with Kubernetes, Slurm, and networking components
</Update>

<Update label="Sep 8" description="/evaluation">
  **Serverless LoRA and Dedicated Endpoints support for Evaluations**

  You can now run evaluations:

  * Using [Serverless LoRA](docs/lora-inference#serverless-lora-inference) models, including supported LoRA fine-tuned models
  * Using [Dedicated Endpoints](docs/dedicated-endpoints-1), including fine-tuned models deployed via dedicated endpoints
</Update>

<Update label="Sep 5" description="/chat/completions">
  **Kimi-K2-Instruct-0905 Model Release**

  Upgraded version of Moonshot's 1 trillion parameter MoE model with enhanced performance. [Read more](https://www.together.ai/models/kimi-k2-0905)

  * Model ID: `moonshot-ai/Kimi-K2-Instruct-0905`
</Update>

## August, 2025

<Update label="Aug 27" description="/chat/completions">
  **DeepSeek-V3.1 Model Release**

  Upgraded version of DeepSeek-R1-0528 and DeepSeek-V3-0324. [Read more](https://www.together.ai/blog/deepseek-v3-1-hybrid-thinking-model-now-available-on-together-ai)

  * **Dual Modes**: Fast mode for quick responses, thinking mode for complex reasoning
  * **671B total parameters** with 37B active parameters
  * Model ID: `deepseek-ai/DeepSeek-V3.1`

  ***

  **Model Deprecations**

  The following models have been deprecated and are no longer available:

  * `meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo`
  * `black-forest-labs/FLUX.1-canny`
  * `meta-llama/Llama-3-8b-chat-hf`
  * `black-forest-labs/FLUX.1-redux`
  * `black-forest-labs/FLUX.1-depth`
  * `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B`
  * `NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO`
  * `meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo`
  * `meta-llama-llama-3-3-70b-instruct-lora`
  * `Qwen/Qwen2.5-14B`
  * `meta-llama/Llama-Vision-Free`
  * `Qwen/Qwen2-72B-Instruct`
  * `google/gemma-2-27b-it`
  * `meta-llama/Meta-Llama-3-8B-Instruct`
  * `perplexity-ai/r1-1776`
  * `nvidia/Llama-3.1-Nemotron-70B-Instruct-HF`
  * `Qwen/Qwen2-VL-72B-Instruct`
</Update>

<Update label="Aug 19" description="/fine-tunes">
  **GPT-OSS Models Fine-Tuning Support**

  Fine-tune OpenAI's open-source models to create domain-specific variants. [Read more](https://www.together.ai/blog/fine-tune-gpt-oss-models-into-domain-experts-together-ai)

  * Supported models: `gpt-oss-20B` and `gpt-oss-120B`
  * Supports 16K context SFT, 8k context DPO
</Update>

<Update label="Aug 5" description="/chat/completions">
  **OpenAI GPT-OSS Models Now Available**

  OpenAI's first open-weight models now accessible through Together AI. [Read more](https://www.together.ai/blog/announcing-the-availability-of-openais-open-models-on-together-ai)

  * Model IDs: `openai/gpt-oss-20b`, `openai/gpt-oss-120b`
</Update>

## July, 2025

<Update label="Jul 29" description="/chat/completions">
  **VirtueGuard Model Release**

  Enterprise-grade gaurd model for safety monitoring with **8ms response time**. [Read more](https://www.together.ai/blog/virtueguard)

  * Real-time content filtering and bias detection
  * Prompt injection protection
  * Model ID: `VirtueAI/VirtueGuard-Text-Lite`
</Update>

<Update label="Jul 28" description="/evaluation">
  **Together Evaluations Framework**

  Benchmarking platform using **LLM-as-a-judge methodology** for model performance assessment. [Read more](https://www.together.ai/blog/introducing-together-evaluations)

  * Create custom LLM-as-a-Judge evaluation suites for your domain
  * Support `compare`, `classify` and `score` functionality
  * Enables comparing models, prompts and LLM configs, scoring and classifying LLM outputs
</Update>

<Update label="Jul 25" description="/chat/completions">
  **Qwen3-Coder-480B Model Release**

  Agentic coding model with top SWE-Bench Verified performance. [Read more](https://www.together.ai/blog/qwen-3-coder)

  * **480B total parameters** with 35B active (MoE architecture)
  * **256K context length** for entire codebase handling
  * **Leading SWE-Bench scores** on software engineering benchmarks
  * Model ID: `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`
</Update>

<Update label="Jul 17" description="/chat/completions">
  **NVIDIA HGX B200 Hardware Support**

  **Record-breaking serverless inference speed** for DeepSeek-R1-0528 using NVIDIA's Blackwell architecture. [Read more](https://www.together.ai/blog/fastest-inference-for-deepseek-r1-0528-with-nvidia-hgx-b200)

  * Dramatically improved throughput and lower latency
  * Same API endpoints and pricing
  * Model ID: `deepseek-ai/DeepSeek-R1`
</Update>

<Update label="Jul 14" description="/chat/completions">
  **Kimi-K2-Instruct Model Launch**

  Moonshot AI's **1 trillion parameter MoE model** with frontier-level performance. [Read more](https://www.together.ai/blog/kimi-k2-leading-open-source-model-now-available-on-together-ai)

  * Excels at tool use, and multi-step tasks and strong multilingual support
  * Great agentic and function calling capabilities
  * Model ID: `moonshotai/Kimi-K2-Instruct`
</Update>

<Update label="Jul 10" description="/audio/transcriptions">
  **Whisper Speech-to-Text APIs**

  High-performance audio transcription that's **15× faster than OpenAI** with support for **files over 1 GB**. [Read more](https://www.together.ai/blog/speech-to-text-whisper-apis)

  * Multiple audio formats with timestamp generation
  * Speaker diarization and language detection
  * Use `/audio/transcriptions` and `/audio/translations` endpoint
  * Model ID: `openai/whisper-large-v3`
</Update>

<Update label="Jul 8" description="Compliance">
  **SOC 2 Type II Compliance Certification**

  Achieved enterprise-grade security compliance through independent audit of security controls. [Read more](https://www.together.ai/blog/soc-2-compliance)

  * Simplified vendor approval and procurement
  * Reduced due diligence requirements
  * Support for regulated industries
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt