# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md

Title: Changelog — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html

Published Time: Thu, 31 Jul 2025 18:51:00 GMT

Markdown Content:
Changelog[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#changelog "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

This section identifies the major changes in each version of the NVIDIA NeMo™ Framework released to date.

25.07 NeMo Framework Container[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-container "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------

### Existing Repository: [NVIDIA/NeMo](https://github.com/NVIDIA/NeMo.md)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#existing-repository-https-github-com-nvidia-nemo "Link to this heading")

#### Training Performance (Speed)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#training-performance-speed "Link to this heading")

*   nvFSDP + Activation offloading tuning for GB200

*   nvFSDP with hybrid model sharding with partial replication

*   nvFSDP with persistent buffers

*   NVL sharp + IB sharp for DP/FSDP communications on H100 and B200

*   MXFP8 with TP communication overlap

*   MXFP8 with reduced memory allocation

*   FP8 sub-channel recipe (128x128 for weight and 1x128 for activation)

*   cuDNN fused attention for MLA (both Hopper and Blackwell)

*   Advanced custom asymmetric pipelining (for MTP, loss function, and embedding)

*   BF16 optimizer for model memory saving

*   CUDA graph fix for fine-tuning benchmarks

*   CUDA graph support for Llama 4

#### Collections[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#collections "Link to this heading")

*   LLM

    *   Improved DeepSeek V3

        *   MoE Permute Fusion supported ([PR](https://github.com/NVIDIA/NeMo/pull/13188.md))

        *   Module-specific recompute supported ([PR](https://github.com/NVIDIA/NeMo/pull/13188.md))

        *   Subchannel FP8 recipe ([PR](https://github.com/NVIDIA/NeMo/pull/12940.md))

        *   Blackwell support ([PR](https://github.com/NVIDIA/NeMo/pull/13620.md))

        *   MoE router score promoted to FP32 to facilitate convergence ([PR](https://github.com/NVIDIA/NeMo/pull/13188.md))

    *   Qwen 3 ([PR](https://github.com/NVIDIA/NeMo/pull/13554.md)[Docs](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/qwen3.html.md))

    *   Gemma3 ([PR](https://github.com/NVIDIA/NeMo/pull/13536.md)[Docs](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/gemma3.html.md))

    *   New embedding models supported ([PR](https://github.com/NVIDIA/NeMo/pull/13890.md) and [Docs](https://docs.nvidia.com/nemo-framework/user-guide/latest/embeddingmodels/gpt/llama_embedding.html.md))

        *   nv-embedqa-e5-v5

        *   llama-3.2-nv-embedqa-300m-v2

        *   llama-3.2-nv-embedqa-1b-v2

    *   New reranker models supported ([PR](https://github.com/NVIDIA/NeMo/pull/13876.md)[Docs](https://docs.nvidia.com/nemo-framework/user-guide/latest/reranker/llama_reranker.html.md))

        *   llama-3.2-nv-rerankqa-500m-v2

        *   llama-3.2-nv-rerankqa-1b-v2

    *   Multimodal

        *   Audio Vision Language model (AVLM) supported ([PR](https://github.com/NVIDIA/NeMo/pull/12477.md)[Docs](https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/avlm.html.md))

#### Speech[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#speech "Link to this heading")

*   Batched beam search for transducers (RNN-T and TDT)

*   RNNT/TDT buffered/streaming inference + batched decoding support in cache-aware

*   Added support for CTC batched beam search with GPU-LM

*   Key fixes

    *   Punctuation marks in timestamps

    *   Fix timestamps when CUDA graphs enabled

    *   Fix masking of <pad> tokens in AED inference

    *   TDT streaming inference fix

### New Repository[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#new-repository "Link to this heading")

#### [Export & Deploy](https://github.com/NVIDIA-NeMo/Export-Deploy.md)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id14 "Link to this heading")

*   [NeMo Export-Deploy Release](https://github.com/NVIDIA-NeMo/Export-Deploy/releases.md)

*   Pip installers for export and deploy

*   RayServe support for multi-instance deployment

*   TensorRT-LLM PyTorch backend

*   MCore inference optimizations

⚠️ Note: The current [NVIDIA/NeMo](https://github.com/NVIDIA/NeMo.md) is being re-organized to enable better user experience. New repos are under [NVIDIA-NeMo](https://github.com/NVIDIA-NeMo.md) github org, where users can also find an overview of how different repos fit into NeMo Framework. At time of the relase, the below Alpha repos in [NVIDIA-NeMo](https://github.com/NVIDIA-NeMo.md) are under active development. New features, improvements, and documentation updates are released regularly. We are working toward a stable release, so expect the interface to solidify over time. Your feedback and contributions are welcome, and we encourage you to follow along as new updates roll out.

#### Megatron-Bridge (Alpha)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#megatron-bridge-alpha "Link to this heading")

*   Llama and Qwen

*   Pretrain/SFT

*   PEFT

*   Recipe structure with examples for plain Python and NeMo Run usage

#### Automodel (Alpha)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#automodel-alpha "Link to this heading")

*   Custom FSDP Support

    *   Docs (WIP) [PR](https://github.com/NVIDIA-NeMo/Automodel/pull/28.md); [PR](https://github.com/NVIDIA-NeMo/Automodel/pull/63.md)

*   Packed sequence support

    *   [Docs](https://docs.nvidia.com/nemo/automodel/latest/guides/llm/dataset.html.md#enable-packed-sequences-in-nemo-automodel); [PR](https://github.com/NVIDIA-NeMo/Automodel/pull/49.md)

*   Triton kernels for LoRA

    *   Docs (WIP); [PR](https://github.com/NVIDIA-NeMo/Automodel/pull/81.md)

#### Eval (Alpha)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#eval-alpha "Link to this heading")

*   Enable log probs benchmarks with nvidia-lm-eval

*   Support for new harnesses:

    *   BFCL

    *   BigCode

    *   Simple-evals

    *   Safety-harness

    *   Garak

*   Single node multi-instance/DP evaluation with Ray

#### nvFSDP (Alpha)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nvfsdp-alpha "Link to this heading")

*   Support sharding strategies for Optimizer State, Gradient and Model Weights (similar to ZeRO 1/2/3)

*   Checkpoint support

*   Integration with Automodel

*   FP8 Mixed Precision with Transformer Engine

*   Hopper related optimizations (User-Buffer-Registration NCCL communication​​)

*   FSDP2 similar API usage

25.07 NeMo Curator Container[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-curator-container "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------

*   [NeMo Curator GitHub Release](https://github.com/NVIDIA-NeMo/Curator/releases.md)

Updates to Non-Container Repositories[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#updates-to-non-container-repositories "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

These repos are not included in the NeMo Framework Containers. For details, please refer to [NVIDIA-NeMo](https://github.com/NVIDIA-NeMo.md).

### RL[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#rl "Link to this heading")

*   [NeMo RL GitHub Release](https://github.com/NVIDIA-NeMo/RL/releases.md)

*   NeMo RL’s container build process is publicly available [here](https://docs.nvidia.com/nemo/rl/latest/docker.html.md)

NeMo Framework 25.04.02[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-25-04-02 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

The new container is available as `nvcr.io/nvidia/nemo:25.04.02`. For convenience, the `nvcr.io/nvidia/nemo:25.04` tag has also been updated to point to this latest patch version.

This release addresses known security issues. For the latest NVIDIA Vulnerability Disclosure Information, visit [NVIDIA Security](https://www.nvidia.com/en-us/security.md/); for acknowledgement, please reach out to the NVIDIA PSIRT team at [PSIRT@nvidia.com](mailto:PSIRT%40nvidia.com.md).

NeMo Framework 25.04.01[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-25-04-01 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

The new container is available as `nvcr.io/nvidia/nemo:25.04.01`. For convenience, the `nvcr.io/nvidia/nemo:25.04` tag has also been updated to point to this latest patch version.

### Collections[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id20 "Link to this heading")

*   LLM

    *   Llama 4: Fixed an accuracy issue caused by MoE probability normalization. Improved pre-train and fine-tune performance.

### Export & Deploy[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id21 "Link to this heading")

*   Updated vLLMExporter to use vLLM V1 to address a security vulnerability.

### AutoModel[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#automodel "Link to this heading")

*   Improved chat-template handling.

### Fault Tolerance[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#fault-tolerance "Link to this heading")

*   Local checkpointing: Fixed support for auto-inserted metric names when resuming from local checkpoints.

NeMo Framework 25.04.00[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-25-04-00 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

### Curator[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#curator "Link to this heading")

*   Llama Based PII Redaction

*   Trafilatura Text Extractor

*   Chinese & Japanese Stopwords for Text Extractors

*   Writing gzip compressed jsonl datasets

*   Training dataset curation for retriever customization using hard-negative mining

*   Implemented a memory efficient pairwise similarity in Semantic Deduplication

### Export & Deploy[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id22 "Link to this heading")

*   NeMo 2.0 export path for NIM

*   ONNX and TensorRT Export for NIM Embedding Container

*   In-framework deployment for HF Models

*   TRT-LLM deployment for HF Models in NeMo Framework

### Evaluation[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#evaluation "Link to this heading")

*   Integrate [nvidia-lm-eval](https://pypi.org/project/nvidia-lm-eval.md/) to NeMo FW for evaluations with OpenAI API compatible in-framework deployment

### AutoModel[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id23 "Link to this heading")

*   VLM AutoModelForImageForTextToText

*   FP8 for AutoModel

*   Support CP with FSDP2

*   Support TP with FSDP2

*   Performance Optimization

    *   Add support for cut cross entropy & Liger kernels

    *   Gradient Checkpointing

### Fault Tolerance[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id24 "Link to this heading")

*   Integrate NVRx v0.3 [Local checkpointing](https://nvidia.github.io/nvidia-resiliency-ext/checkpointing/local/index.html.md)

### Collections[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id25 "Link to this heading")

*   LLM

    *   Llama4 (See [Known Issue](https://docs.nvidia.com/nemo-framework/user-guide/latest/knownissues.html.md#llama4-known-issue))

    *   Llama Nemotron Ultra

    *   Llama Nemotron Super

    *   Llama Nemotron Nano

    *   Nemotron-h/5

    *   DeepSeek V3 Pretraining

    *   Evo2

    *   Qwen 2.5

    *   LoRA for Qwen3-32B and Qwen3-30B-A3B

*   MultiModal

    *   FLUX

    *   Gemma 3

    *   Qwen2-VL

*   ASR

    *   NeMo Run support for ASR training

    *   N-Gram LM on GPU for AED

    *   N-Gram LM on GPU + Transducer greedy decoding (RNN-T, TDT)

    *   Timestamps support for AED timestamp supported models

    *   Migrate SpeechLM to NeMo 2.0

    *   Canary-1.1

    *   Replace ClassificationModels class with LabelModels

### Performance[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#performance "Link to this heading")

*   Functional MXFP8 support for (G)B200

*   Current scaling recipe with TP communication overlap and FP8 param gathers

*   Custom FSDP support that fully utilizes GB200 NVL72

### Deprecations[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#deprecations "Link to this heading")

*   Nemo Aligner is deprecated from 25.04 onwards. Users can use 25.02 or prior if they would like to use Nemo Aligner. A new library, [Nemo RL](https://github.com/NVIDIA/NeMo-RL.md), has been released to replace it.

*   Nemo 1.x path is deprecated from 25.04 onwards. Users can use 25.02 or prior if they would like to use Nemo 1.0 path. However, we strongly encourage you to migrate to Nemo 2.x path to take advantage of our latest features and functionalities. See [migration guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/index.html.md) for more info.

### Long-term support (LTS)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#long-term-support-lts "Link to this heading")

*   25.04 is our first LTS release. The release cadence for LTS containers will be roughly 1-2 times a year and the LTS container will be end-of-lifed when the next LTS container is published. LTS releases will accept critical bug fixes and security patches until end-of-lifed.

NeMo Framework 25.02.01[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-25-02-01 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

### Training[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#training "Link to this heading")

*   Fix MoE based models training instability.

*   Fix bug in Llama exporter for Llama 3.2 1B and 3B.

*   Fix bug in LoRA linear_fc1adapter when different TP is used during saving and loading the adapter checkpoint.

*   Upgrade Nsight Systems to 2025.1.1 to fix an issue in the previous container that kernel overlapping fails to work when profiling is used.

NeMo Framework 25.02[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-25-02 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

### Training[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id26 "Link to this heading")

*   Blackwell and Grace Blackwell support

*   Pipeline parallel support for distillation

*   Improved NeMo Framework installation

### Aligner[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#aligner "Link to this heading")

*   DPO with EP

*   Support MCore Distributed Optimizer

*   Aligner on Blackwell

### Curator[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id27 "Link to this heading")

*   Python 3.12 Support

*   Curator on Blackwell

*   Nemotron-CC Dataset Recipe

*   Performant S3 for Fuzzy Deduplication

### Export & Deploy[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id28 "Link to this heading")

*   vLLM export for NeMo 2.0

### Evaluations[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#evaluations "Link to this heading")

*   Integrate lm-eval-harness

### Collections[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id29 "Link to this heading")

*   LLM

    *   DAPT Example and best practices in nemo 2.0

    *   [NeMo 2.0] Enable Tool Learning and add a tutorial

    *   Support GPT Embedding Model (Llama 3.2 1B/3B)

    *   Qwen2.5, Phi4 (via AutoModel)

    *   SFT for Llama 3.3 model (via AutoModel)

    *   Support BERT Embedding Model with NeMo 2.0

    *   DeepSeek SFT & PEFT Support

*   MultiModal

    *   Clip

    *   SP for NeVA

    *   CP for NeVA

    *   Intern-VIT

### Automodel[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id30 "Link to this heading")

*   Preview release.

*   PEFT and SFT support for LLMs available via Hugging Face’s AutoModelForCausalLM.

*   Support for Hugging Face-native checkpoints (full model and adapter only).

*   Support for distributed training via DDP and FSDP2.

### ASR/TTS[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#asr-tts "Link to this heading")

*   Lhotse: TPS-free 2D bucket estimation and filtering

*   Update model outputs to make all asr outputs to be in consistent format

*   Sortformer Release Model

NeMo Framework 24.12[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-24-12 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

### Training[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id31 "Link to this heading")

*   Fault Tolerance

    *   Straggler Detection

    *   Auto Relaunch

### LLM & MM[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#llm-mm "Link to this heading")

*   MM models

    *   Llava-next

    *   Llama 3.2

*   Sequence Model Parallel for NeVa

*   Enable Energon

*   SigLIP (NeMo 1.0 only)

*   LLM 2.0 migration

    *   Starcoder2

    *   Gemma 2

    *   T5

    *   Baichuan

    *   BERT

    *   Mamba

    *   ChatGLM

*   DoRA support

### Aligner[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id32 "Link to this heading")

*   NeMo 2.0 Model Support

*   Sequence Packing for DPO

*   Reinforce/RLOO Support

*   SFT Knowledge Distillation

*   Context Parallelism for SFT

### Export[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#export "Link to this heading")

*   Nemo 2.0 base model export path for NIM

*   PTQ in Nemo 2.0

### Curator[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id33 "Link to this heading")

*   Synthetic Data Generation for Text Retrieval

    *   LLM-based Filters

        *   Easiness

        *   Answerability

    *   Q&A Retrieval Generation Pipeline

*   Parallel Dataset Curation for Machine Translation

    *   Load/Write Bitext Files

    *   Heuristic filtering (Histogram, Length Ratio)

    *   Classifier filtering (Comet, Cometoid)

### ASR[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#asr "Link to this heading")

*   Timestamps with TDT decoder

*   Timestamps option with .transcribe()

NeMo Framework 24.09[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-24-09 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

### LLM & MM[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id34 "Link to this heading")

*   Training

    *   Long context recipe

    *   PyTorch Native FSDP 1

    *   Distributed Checkpoint

        *   Torch native format

        *   Async

        *   Parallel r/w

    *   NeMo Run OSS

*   Models

    *   Llama 3

    *   Mixtral

    *   Nemotron

    *   E2E BF16 Training of Llama3 with RedPajama2 data (~2.4T tokens)

        *   NeMo2.0 llama3 8b trained on 2.4T RP2 tokens

        *   NeMo2.0 llama3 70b trained on <1T RP2 tokens

*   NeMo 1.0

    *   SDXL (text-2-image)

    *   Model Opt

        *   Depth Pruning [[docs](https://github.com/NVIDIA/NeMo/blob/main/docs/source/nlp/nemo_megatron/model_distillation/drop_layers.rst.md)]

        *   Logit based Knowledge Distillation [[docs](https://github.com/NVIDIA/NeMo/blob/main/docs/source/nlp/distillation.rst.md)]

### Aligner[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id35 "Link to this heading")

*   Rejection Sampling (SFT)

*   Packed sequence training in aligner for SFT

### Export[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id36 "Link to this heading")

*   TensorRT-LLM v0.12 integration

*   LoRA support for vLLM

*   FP8 checkpoint

### Curator[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id37 "Link to this heading")

*   Image Semantic Deduplication

*   NSFW Classifier

*   Aesthetic Classifier

*   CLIP Embedding Creation

*   AEGIS Classifier

*   Quality Classifier

### ASR[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id38 "Link to this heading")

*   Parakeet large (ASR with PnC model)

*   Added [Uzbek](https://huggingface.co/nvidia/stt_uz_fastconformer_hybrid_large_pc.md) offline and [Gregorian](https://huggingface.co/nvidia/stt_ka_fastconformer_hybrid_transducer_ctc_large_streaming_80ms_pc.md) streaming models

*   Optimization feature for efficient bucketing to improve bs consumption on GPUs

NeMo Framework 24.07[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-24-07 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

### Training[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id39 "Link to this heading")

*   Features and Model architectures

    *   PEFT: QLoRA support, LoRA/QLora for Mixture-of-Experts (MoE) dense layer

    *   State Space Models & Hybrid Architecture support (Mamba2 and NV-Mamba2-hybrid)

    *   Support Nemotron, Minitron, Gemma2, Qwen, RAG

*   Multimodal

    *   NeVA: Add SOTA LLM backbone support (Mixtral/LLaMA3) and suite of model parallelism support (PP/EP)

    *   Support Language Instructed Temporal-Localization Assistant (LITA) on top of video NeVA

*   Custom Tokenizer training in NeMo

*   Update the Auto-Configurator for EP, CP and FSDP

### ASR[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id40 "Link to this heading")

*   SpeechLM and SALM

*   Adapters for Canary Customization

*   Pytorch allocator in PyTorch 2.2 improves training speed up to 30% for all ASR models

*   Cuda Graphs for Transducer Inference

*   Replaced webdataset with Lhotse - gives up to 2x speedup

*   Transcription Improvements - Speedup and QoL Changes

*   ASR Prompt Formatter for multimodal Canary

### Aligner[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id41 "Link to this heading")

*   Speed up Aligner RLHF by 7x with TRT-LLM

*   Reward Preference Optimization (RPO)

*   Identity Preference Optimization (IPO)

*   SteerLM2

*   Llama 3 performance and convergence example

*   Constitutional AI algorithm (RLAIF)

### Curator[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id42 "Link to this heading")

*   Semantic Deduplication

*   Resiliparse for Text Extraction

*   Improve Distributed Data Classification - Domain classifier is 1.55x faster through intelligent batching

*   Synthetic data generation for fine-tuning

### Export & Deploy[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id43 "Link to this heading")

*   In framework PyTriton deployment with backends:

    *   PyTorch

    *   vLLM

    *   TRT-LLM update to 0.10

*   TRT-LLM C++ runtime

NeMo Framework 24.05[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-24-05 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

NeMo Framework now supports Large Language Models (LLM), Multimodal (MM), Automatic Speech Recognition (ASR), and Text-to-Speech (TTS) in a single consolidated container.

### LLM and MM[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#llm-and-mm "Link to this heading")

*   Megatron Core RETRO

    *   Pre-training

    *   Zero-shot Evaluation

*   Pretraining, conversion, evaluation, SFT, and PEFT for:

    *   Mixtral 8X22B

    *   Llama 3

    *   SpaceGemma

*   Embedding Models Fine Tuning

    *   Mistral

    *   BERT

*   BERT models

    *   Distributed checkpoint

*   Video capabilities with NeVa

### Performance[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id44 "Link to this heading")

*   Distributed Checkpointing

    *   Torch native backend

    *   Parallel read/write

    *   Async write

*   Multimodal LLM (LLAVA/NeVA)

    *   Pipeline Parallelism support

    *   Sequence packing support

### Export[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id45 "Link to this heading")

*   Integration of Export & Deploy Modules into NeMo Framework container

    *   Upgrade to TRT-LLM 0.9

### Curator[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id46 "Link to this heading")

*   SFT/PEFT (LoRA, and p-tuning) Data Curation Pipeline and Example

*   Dataset Blending Tool

*   Domain Classifier

### Aligner[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#id47 "Link to this heading")

*   LoRA techniques with:

    *   PPO Actor

    *   PDO

    *   SFT/SteerLM

*   Stable Diffusion models

### Speech (ASR & TTS)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#speech-asr-tts "Link to this heading")

*   AED Multi Task Models (Canary) - Multi-Task Multi-Lingual Speech Recognition / Speech Translation model

*   Multimodal Domain - Speech LLM supporting SALM Model

*   Parakeet-tdt_ctc-1.1b Model - RTFx of > 1500 (can transcribe 1500 seconds of audio in 1 second)

*   Audio Codec 16kHz Small - NeMo Neural Audio Codec for discretizing speech for use in LLMs

    *   mel_codec_22khz_medium

    *   mel_codec_44khz_medium

### Perf Improvements[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#perf-improvements "Link to this heading")

*   Transcribe() upgrade - Enables one line transcribe with files, tensors, data loaders

*   Frame looping algorithm for RNNT faster decoding - Improves Real Time Factor (RTF) by 2-3x

*   Cuda Graphs + Label-Looping algorithm for RNN-T and TDT Decoding - Transducer Greedy decoding at over 1500x RTFx, on par with CTC Non-Autoregressive models

*   Semi Sorted Batching support - External User contribution that speeds up training by 15-30%.

### Customization[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#customization "Link to this heading")

*   Context biasing for CTC word stamping - Improve accuracy for custom vocabulary and pronunciation

### Longform Inference[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#longform-inference "Link to this heading")

*   Longform inference support for AED models

*   Transcription of multi-channel audio for AED models

### Misc[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#misc "Link to this heading")

*   Upgraded webdataset - Speech and LLM / Multimodal unified container

NeMo Framework 24.03.01[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-24-03-01 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

Issues Fixed

*   GPT Memory Leak at Loss Function

*   Eval script issue for Mixtral PEFT

*   Llama 7B Out-of-memory issue when using 1TB system memory

*   Enable Pipeline Parallelism support for LoRA merge

*   Multi-node Llama training on Kubernetes while saving checkpoint

NeMo Framework 24.03[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-24-03 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   [Fully Sharded Data Parallel (FSDP)](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gpt/fsdp.html.md) support for GPT

*   Post-Training Quantization (PTQ) with AMMO library (0.7.4) for Llama

*   Support Expert Parallelism on all MoE models e.g. Mixtral

*   Pipeline parallel for p-tuning

*   Updated PEFT metrics for all popular community models. ([Support matrix Temp Internal Link](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/nlp/nemo_megatron/peft/landing_page.html.md))

*   Upgraded PyTorch Lightning to 2.2

*   Upgraded base container to PyTorch 24.02

*   Consolidation of the StarCoder2 and Gemma specific containers, with the previous Framework GA container

*   Customizable distributed data classification tool in Curator

*   GPU-accelerated quality classification model code in Curator

*   GPU-accelerated domain classification model code in Curator

NeMo Framework 24.01.01[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-24-01-01 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

*   Added Mixture of Experts parameter passing for MCore

*   PP/TP support for Mixture of Experts

*   SFT / PEFT support for Gemma model

*   Training / SFT / PEFT / Evaluation support for - Baichuan model - CodeLlama model

*   Fixed SFT/PEFT support nemo-launcher configs for Mistral and Mixtral - Edited configs with correct values

*   Documentation refactor and landing page added

*   NeMo Framework developer docs added

NeMo Framework 24.01[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-24-01 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   New end-to-end support (pretraining, conversion, evaluation, SFT, PEFT) for community models, featuring:

    *   Support for community model Falcon

    *   Support for community model Mixtral (expert parallelism coming in future release)

    *   Support for community model Mistral

    *   Support for community model Code Llama

*   General availability release of NeMo Multimodal, featuring:

    *   Support for vision-language foundation models: CLIP

    *   Support for text-2-image foundation models: Stable Diffusion and Imagen

    *   Support for text-2-image customization: SD-LoRA, SD-ControlNet, SD-instruct pix2pix

    *   Support for multimodal LLM: NeVA and LLAVA

    *   Support for text-2-NeRF: DreamFusion++

    *   Support for NSFW

*   New performance features and key optimization:

    *   Support PyTorch Fully Sharded Data Parallel training (FSDP) with tensor-parallelism

    *   Support CPU offloading and prefetch of activations and weights

    *   Support Context Parallelism for performant long-sequence-length LLM training

    *   Support framework-level FP8 precision that reduces memory usage and training step time

    *   Transformer layer granularity re-computation with FP8 LLM training

    *   Support pipelined tensor-parallel communication overlap with GEMM for all LLMs

    *   Support LLM fine-tuning with packed sequences

    *   Support fused RoPE and Swiglu for LLAMA2 like models

    *   Device memory bug fix; removed FP8 cast/transpose duplicates in FP8 training

*   New features for NeMo Aligner:

    *   Support for MultiEpoch

    *   Added PPO: custom end strings + memory optimizations

    *   Added SFT: LoRa and custom validation metrics

*   New features for NeMo Curator:

    *   Multi-node multi-GPU fuzzy document-level deduplication supported within the launcher.

    *   Added new Personal Identifiable Information (PII) Removal module

    *   Task decontamination for SFT and PEFT (e.g., LoRA, p-tuning, adapters, etc.) datasets supported within the launcher

    *   Code data filtering heuristics from StarCoder

NeMo Framework 23.11[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-23-11 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   Open source release of [NeMo-Aligner](https://github.com/NVIDIA/NeMo-Aligner.md). NeMo-Aligner is a one stop shop for efficient model alignment algorithms, featuring:

    *   Support for the full Reinforcement Learning from Human Feedback(RLHF) pipeline including SFT, Reward Model Training and Reinforcement Learning

    *   Support for the SteerLM technique

    *   Support for Direct Preference Optimization

    *   Support for all Megatron Core GPT models such as LLAMA2 70B

    *   Improved user experience

NeMo Framework 23.10[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-23-10 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   General announcement of the NeMo Framework Inference container, featuring:

    *   Deployment support for distributed checkpoints ([Megatron Core](https://github.com/NVIDIA/Megatron-LM/tree/main/megatron/core.md)) for NeMotron 8B and Llama 2 (BF16 only)

    *   Deployment support for fine-tuned (SFT, RLHF, SteerLM) NeMotron 8B (BF16 only)

    *   Deployment support for P-tuned Llama 2 on a single GPU (BF16 only)

    *   Support for serving GPT and Llama 2 models using PyTriton on Triton Inference Server

    *   Support for serving GPT and Llama 2 models using TensorRT-LLM C++ backend on Triton Inference Server

    *   Support in-flight batching for TensorRT-LLM C++ backend on Triton Inference Server

NeMo Framework 23.08.03[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-23-08-03 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

*   Enabled PEFT to work with Llama-2 models

*   Addressed an issue that occurred when resuming Supervised Fine-Tuning with constant learning rate scheduler

*   Fixed model parallelism bug in SFT and PEFT

*   Included P-tuning state dictionary handling for distributed checkpoints

*   Fixed bug that occurred when using the save_best_model flag

*   Fixed bug where progress bar would show the wrong number of steps

NeMo Framework 23.08.02[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-23-08-02 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

*   Fixed container paths in Hydra configurations

NeMo Framework 23.08.01[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-23-08-01 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

*   Fixed checkpoint search for distributed checkpoints

NeMo Framework 23.08[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-23-08 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   Added the Distributed Checkpoint Format to NeMo and Megatron Core for GPT

*   New GPT transformer from Megatron Core which enables training of improved LLM configs

*   When training 175B GPT with FP8, use tensor parallelism TP=8 and micro batch size MBS = 2 to ensure the model-parallel partitioning fits GPU memory

*   New GPT transformer from Megatron Core which enables Group and Multi Query Attention for models like LLAMA2

*   Support Llama 1 and Llama 2 pre-training with Megatron Core

*   Customize LLMs for Llama 1 and Llama 2 models with techniques like SFT, PEFT (p-tuning, adapters, IA3)

*   Added examples and documentation for Kubernetes training

*   NeMo Data Curator: added downstream task decontamination support

NeMo Framework 23.07[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-23-07 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   Added Low-Rank Adaptation (LoRA) Support for T5 and mT5

*   Added Batch Size Ramp-up Support for GPT

NeMo Framework 23.05[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-23-05 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   Low-Rank Adaptation (LoRA) Support for GPT

*   LDDL (Language Datasets and Data Loaders) for BERT on 100B model resulting in a 30% performance speedup

*   Unify dataset and model classes for all PEFT (p-tuning, adapters, IA3) with SFT model class as parent for GPT

*   Converter from Interleaved PP to non-Interleaved PP

*   Dialog dataset guidance for SFT to help create better chat models

*   Support Dynamic Sequence Length Batches with GPT SFT

*   Data parallelism enabled for RLHF servers, providing a 2x end-to-end speedup in most jobs

NeMo Framework 23.04.1 ——————–@@

*   Addressed issue in RLHF which prevented some jobs from running in Slurm clusters

*   Corrections related to the renaming of NeMo Megatron to NeMo Framework

*   Modified run.name in the *_improved configuration files to match the correct parameter count

NeMo Framework 23.04[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-23-04 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   Supports NeMo Data Curator, a scalable Python library for curating the large-scale datasets required for training large language foundation models

*   Enables continued training for P-tuning

*   Switches to Megatron Core for Model Parallelism

*   Extends the Data Validation Tool to provide P-tuning GPU runtime estimates

*   Supports tensor and pipeline parallelism conversion for GPT and T5 models

*   Supports supervised fine-tuning for GPT

*   Adds Reinforcement Learning from Human Feedback (RLHF) for GPT models

*   Adds four GPT model sizes based on new and improved model configurations:

    *   400M_improved

    *   1B_improved

    *   7B_improved

    *   40B_improved

Following is a list of GPT model configuration changes:

| Configuration | Previous | New |
| --- | --- | --- |
| Activation | GeLU | Fast-SwiGLU |
| Position Embedding | Learned Absolute | RoPE |
| Dropout | 0.1 | 0 |
| Embeddings and Output Layer | Tied | Untied |
| Bias terms | Yes | No |
| Normalization | LayerNorm | LayerNorm1p |

NeMo Framework 23.03[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-23-03 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   Adds a per microbatch data loader for GPT and BERT models

*   Supports `SquaredReLU` and `SwiGLU` activation functions for GPT and T5 models

*   Supports Rotary Position Embedding (RoPE) for GPT and RETRO

*   Supports early stopping when P‑tuning or prompt tuning GPT, T5, and mT5 models

*   Implements refactored adapter learning to mimic the parameter-efficient transfer learning of the NLP approach

*   Adds flash attention for GPT models in Transformer Engine

NeMo Framework 23.01[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-23-01 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   Supports BERT models with tensor parallelism (training only)

*   Supports BERT models with pipeline parallelism (training only)

*   Supports sequence parallelism and selective activation checkpointing for BERT (training only)

*   Supports interleaved pipeline scheduling for BERT models

*   Adds Distributed Adam Optimizer for BERT models

*   Supports AutoConfigurator for BERT models

*   Adds 110M, 4B, 20B, and 100B BERT training configurations

*   Supports mixture-of-experts for T5 models (no expert parallelism, training only)

*   Improves performance for GPT P‑tuning (20%−25% speed-up)

*   Adds ALiBi position embeddings for T5 and mT5 (training only)

*   Logs total model size (across modal parallel ranks) for GPT, T5, mT5, and BERT models

NeMo Framework 22.11[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-22-11 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   Adds interleaved pipeline scheduling for GPT models (training only)

*   Supports FP8 using Transformer Engine (training only)

*   Adds Distributed Adam Optimizer for T5 and mT5 models

*   Supports P‑tuning and prompt tuning for GPT models with sequence parallelism

*   Improves training configurations throughput by 7.9% (5B GPT), 9.6% (3B T5), 4.3% (11B T5), 52.4% (23B T5), and 26.6% (41B T5)

NeMo Framework 22.09[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-22-09 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   Supports NeMo Framework training and inference containers on OCI; for details on orchestration scripts, reach out to [oci_nm@nvidia.com](mailto:oci_nm%40nvidia.com.md)

*   Supports P‑tuning and prompt tuning for T5 and mT5 models with pipeline parallelism (training only)

*   Supports adapter learning for GPT and T5 with tensor parallelism and pipeline parallelism (training only)

*   Supports IA3 learning for GPT and T5 with tensor parallelism and pipeline parallelism (training only)

*   Adds AutoConfigurator to find the highest-throughput configurations for training on Base Command Platform

*   Adds AutoConfigurator for parallel inference hyperparameter search for GPT on Base Command Manager

NeMo Framework 22.08.01[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-22-08-01 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

*   Supports Amazon Web Services as a cloud service provider (performance validated up to 20 `p4d.24xlarge` instances)

*   Adds switched orchestration for cloud service providers from Azure CycleCloud to NVIDIA Nephele for Microsoft Azure

NeMo Framework 22.08[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-22-08 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   Adds distributed Adam Optimizer for GPT models

*   Adds asymmetric encoder-decoder configuration for T5 and mT5 models

*   Supports untying embeddings from the classifier layer for T5 and mT5 models

*   Supports relative position embeddings for T5 and mT5 models (pipeline parallelism ≥3)

*   Supports P‑tuning and prompt tuning for T5 and mT5 models with tensor parallelism (training only)

*   Refactors code to yield improved consistency and readability of configurations and logs

*   Supports SQuAD fine-tuning and evaluation for T5 models with pipeline parallelism ≤2

*   Supports XQuAD fine tuning-and evaluation for mT5 models with pipeline parallelism ≤2

NeMo Framework 22.06-hotfix.01 —————————-@@

*   Fixes AutoConfigurator for T5 and mT5 models

*   Fixes Evaluation harness in GPT models

*   Fixes Prompt learning in GPT models

*   Fixes “out of memory” condition when pretraining GPT models with sequence parallelism

NeMo Framework 22.06[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-22-06 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   Supports sequence parallelism and selective activation checkpointing for GPT

*   Supports relative position embeddings for T5

NVIDIA used the mC4 dataset (24 Languages) for pretraining the mT5 models, and verified the results on KNLI, KorQuAD, KLUE-STS, and XNLI tasks.

*   Updates AutoConfigurator with sequence parallelism and selective activation checkpointing for GPT models

*   Adds AutoConfigurator support for DGX A100 40GB configurations for GPT, T5, and mT5 models

*   Supports P‑tuning and prompt tuning for GPT with pipeline parallelism (training only)

*   Supports operation fusions for higher training throughput (2%-7% speed-up)

*   Changes default GPT configurations to include sequence parallelism and selective activation checkpointing: 20B (speed-up: 14%), 40B (speed-up: 9%), and 175B (speed-up: 15%)

NeMo Framework 22.05.01[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-22-05-01 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

*   Adds cloud service provider support for Microsoft Azure (performance validated up to 36 `Standard_ND96amsr_A100_v4` instances)

*   Adds cluster validation tools (DGMI, NCCL)

*   Improves performance of 20B GPT training configuration by 2.7%

NeMo Framework 22.05[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-22-05 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   Supports asynchronous gradient all-reduce for GPT, T5, mT5 models with pipeline parallel size equal to 1

*   Supports P‑tuning and prompt tuning for GPT with tensor parallelism (training only)

*   Adds AutoConfigurator to find the highest-throughput configurations for training and inference on Base Command Manager

*   Supports custom tokenizers (training only)

*   Supports GPT models with pipeline parallelism on Base Command Manager (inference)

*   Supports new hyperparameters for text generation: `top-p`, `top-k`, and `temperature`

NeMo Framework 22.04[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-22-04 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   Supports T5 models with pipeline parallelism (training only)

*   Switches from GeLU to GeGLU as activation function for T5

*   Supports mT5 with tensor parallelism and pipeline parallelism (training only)

*   Adds 11B, 23B, and 41B T5 model training configurations

*   Adds 170M, 390M, and 3B mT5 model training configurations

*   Adds automatic and configurable Non-Uniform Memory Access (NUMA) mapping

NeMo Framework 22.03[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-22-03 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   Adds tensor parallelism support for T5 models (optimized for <20B parameters, training only)

*   Adds 220M and 3B T5 model training configurations

*   Supports GLUE fine-tuning and evaluation for T5 models

NeMo Framework 22.02[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-22-02 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   Supports GPT models with pipeline parallelism (training only)

*   Adds 40B and 175B GPT model training configurations

NeMo Framework 22.01[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-22-01 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

*   Supports GPT with tensor parallelism on Base Command Platform

*   Supports O2-style AMP (accelerated training of larger models)

*   Includes a chatbot sample application using your trained GPT model

*   Supports training metric monitoring and visualization with Weights & Biases

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/changelog.html.md#nemo-framework-22-01)
- [NVIDIA/NeMo](https://github.com/NVIDIA/NeMo.md)
- [PR](https://github.com/NVIDIA-NeMo/Automodel/pull/81.md)
- [Docs](https://docs.nvidia.com/nemo/automodel/latest/guides/llm/dataset.html.md#enable-packed-sequences-in-nemo-automodel)
- [Export & Deploy](https://github.com/NVIDIA-NeMo/Export-Deploy.md)
- [NeMo Export-Deploy Release](https://github.com/NVIDIA-NeMo/Export-Deploy/releases.md)
- [NVIDIA-NeMo](https://github.com/NVIDIA-NeMo.md)
- [NeMo Curator GitHub Release](https://github.com/NVIDIA-NeMo/Curator/releases.md)
- [NeMo RL GitHub Release](https://github.com/NVIDIA-NeMo/RL/releases.md)
- [here](https://docs.nvidia.com/nemo/rl/latest/docker.html.md)
- [NVIDIA Security](https://www.nvidia.com/en-us/security.md/)
- [PSIRT@nvidia.com](mailto:PSIRT%40nvidia.com.md)
- [nvidia-lm-eval](https://pypi.org/project/nvidia-lm-eval.md/)
- [Local checkpointing](https://nvidia.github.io/nvidia-resiliency-ext/checkpointing/local/index.html.md)
- [Known Issue](https://docs.nvidia.com/nemo-framework/user-guide/latest/knownissues.html.md#llama4-known-issue)
- [Nemo RL](https://github.com/NVIDIA/NeMo-RL.md)
- [migration guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/index.html.md)
- [docs](https://github.com/NVIDIA/NeMo/blob/main/docs/source/nlp/distillation.rst.md)
- [Uzbek](https://huggingface.co/nvidia/stt_uz_fastconformer_hybrid_large_pc.md)
- [Gregorian](https://huggingface.co/nvidia/stt_ka_fastconformer_hybrid_transducer_ctc_large_streaming_80ms_pc.md)
- [Fully Sharded Data Parallel (FSDP)](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/gpt/fsdp.html.md)
- [Support matrix Temp Internal Link](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/nlp/nemo_megatron/peft/landing_page.html.md)
- [NeMo-Aligner](https://github.com/NVIDIA/NeMo-Aligner.md)
- [Megatron Core](https://github.com/NVIDIA/Megatron-LM/tree/main/megatron/core.md)
- [oci_nm@nvidia.com](mailto:oci_nm%40nvidia.com.md)
