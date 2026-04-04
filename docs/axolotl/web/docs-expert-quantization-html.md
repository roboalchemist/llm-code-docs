# Source: https://docs.axolotl.ai/docs/expert_quantization.html

Title: MoE Expert Quantization – Axolotl

URL Source: https://docs.axolotl.ai/docs/expert_quantization.html

Published Time: Sat, 07 Mar 2026 12:17:16 GMT

Markdown Content:
MoE Expert Quantization – Axolotl
===============

[![Image 1](https://docs.axolotl.ai/image/axolotl_logo_digital_white.svg)![Image 2](https://docs.axolotl.ai/image/axolotl_logo_digital_white.svg)](https://docs.axolotl.ai/index.html)

[](https://twitter.com/axolotl_ai)[](https://github.com/axolotl-ai-cloud/axolotl/)[](https://discord.gg/7m9sfhzaf3)

1. [Advanced Features](https://docs.axolotl.ai/docs/fsdp_qlora.html)
2. [MoE Expert Quantization](https://docs.axolotl.ai/docs/expert_quantization.html)

[](https://docs.axolotl.ai/docs/expert_quantization.html)

* [Home](https://docs.axolotl.ai/index.html)
* [Getting Started](https://docs.axolotl.ai/docs/expert_quantization.html)[](https://docs.axolotl.ai/docs/expert_quantization.html)
  * [Quickstart](https://docs.axolotl.ai/docs/getting-started.html)
  * [Installation](https://docs.axolotl.ai/docs/installation.html)
  * [Inference and Merging](https://docs.axolotl.ai/docs/inference.html)
  * [Model Guides](https://docs.axolotl.ai/docs/expert_quantization.html)[](https://docs.axolotl.ai/docs/expert_quantization.html)
    * [Kimi Linear](https://docs.axolotl.ai/docs/models/kimi-linear.html)
    * [Plano Orchestrator](https://docs.axolotl.ai/docs/models/plano.html)
    * [MiMo](https://docs.axolotl.ai/docs/models/mimo.html)
    * [InternVL 3.5](https://docs.axolotl.ai/docs/models/internvl3_5.html)
    * [OLMo 3](https://docs.axolotl.ai/docs/models/olmo3.html)
    * [Trinity](https://docs.axolotl.ai/docs/models/trinity.html)
    * [Arcee AFM](https://docs.axolotl.ai/docs/models/arcee.html)
    * [Ministral3](https://docs.axolotl.ai/docs/expert_quantization.html)[](https://docs.axolotl.ai/docs/expert_quantization.html)
      * [Ministral3](https://docs.axolotl.ai/docs/models/ministral3.html)
      * [Ministral 3 Thinking](https://docs.axolotl.ai/docs/models/ministral3/think.html)
      * [Ministral 3 Vision](https://docs.axolotl.ai/docs/models/ministral3/vision.html)

    * [Magistral](https://docs.axolotl.ai/docs/expert_quantization.html)[](https://docs.axolotl.ai/docs/expert_quantization.html)
      * [Magistral](https://docs.axolotl.ai/docs/models/magistral.html)
      * [Magistral Thinking](https://docs.axolotl.ai/docs/models/magistral/think.html)
      * [Magistral Vision](https://docs.axolotl.ai/docs/models/magistral/vision.html)

    * [Ministral](https://docs.axolotl.ai/docs/models/ministral.html)
    * [Mistral Small 3.1/3.2](https://docs.axolotl.ai/docs/models/mistral-small.html)
    * [Voxtral](https://docs.axolotl.ai/docs/models/voxtral.html)
    * [Devstral](https://docs.axolotl.ai/docs/models/devstral.html)
    * [Mistral 7B](https://docs.axolotl.ai/docs/models/mistral.html)
    * [Llama 4](https://docs.axolotl.ai/docs/models/llama-4.html)
    * [Llama 2](https://docs.axolotl.ai/docs/models/llama-2.html)
    * [Qwen 3 Next](https://docs.axolotl.ai/docs/models/qwen3-next.html)
    * [Qwen 3](https://docs.axolotl.ai/docs/models/qwen3.html)
    * [Gemma 3n](https://docs.axolotl.ai/docs/models/gemma3n.html)
    * [Apertus](https://docs.axolotl.ai/docs/models/apertus.html)
    * [GPT-OSS](https://docs.axolotl.ai/docs/models/gpt-oss.html)
    * [Seed-OSS](https://docs.axolotl.ai/docs/models/seed-oss.html)
    * [Phi](https://docs.axolotl.ai/docs/models/phi.html)
    * [SmolVLM 2](https://docs.axolotl.ai/docs/models/smolvlm2.html)
    * [Granite 4](https://docs.axolotl.ai/docs/models/granite4.html)
    * [Liquid Foundation Models 2](https://docs.axolotl.ai/docs/models/LiquidAI.html)
    * [Hunyuan](https://docs.axolotl.ai/docs/models/hunyuan.html)
    * [Jamba](https://docs.axolotl.ai/docs/models/jamba.html)
    * [Orpheus](https://docs.axolotl.ai/docs/models/orpheus.html)

  * [Command Line Interface (CLI)](https://docs.axolotl.ai/docs/cli.html)
  * [Telemetry](https://docs.axolotl.ai/docs/telemetry.html)
  * [Config Reference](https://docs.axolotl.ai/docs/config-reference.html)
  * [API Reference](https://docs.axolotl.ai/docs/api)

* [Dataset Formats](https://docs.axolotl.ai/docs/dataset-formats/index.html)[](https://docs.axolotl.ai/docs/expert_quantization.html)
  * [Pre-training](https://docs.axolotl.ai/docs/dataset-formats/pretraining.html)
  * [Instruction Tuning](https://docs.axolotl.ai/docs/dataset-formats/inst_tune.html)
  * [Conversation](https://docs.axolotl.ai/docs/dataset-formats/conversation.html)
  * [Stepwise Supervised Format](https://docs.axolotl.ai/docs/dataset-formats/stepwise_supervised.html)
  * [Template-Free](https://docs.axolotl.ai/docs/dataset-formats/template_free.html)
  * [Custom Pre-Tokenized Dataset](https://docs.axolotl.ai/docs/dataset-formats/tokenized.html)

* [Deployments](https://docs.axolotl.ai/docs/expert_quantization.html)[](https://docs.axolotl.ai/docs/expert_quantization.html)
  * [Docker](https://docs.axolotl.ai/docs/docker.html)
  * [Multi-GPU](https://docs.axolotl.ai/docs/multi-gpu.html)
  * [Multi Node](https://docs.axolotl.ai/docs/multi-node.html)
  * [Ray Train](https://docs.axolotl.ai/docs/ray-integration.html)
  * [AMD GPUs on HPC Systems](https://docs.axolotl.ai/docs/amd_hpc.html)
  * [Mac M-series](https://docs.axolotl.ai/docs/mac.html)

* [How To Guides](https://docs.axolotl.ai/docs/expert_quantization.html)[](https://docs.axolotl.ai/docs/expert_quantization.html)
  * [MultiModal / Vision Language Models (BETA)](https://docs.axolotl.ai/docs/multimodal.html)
  * [RLHF (Beta)](https://docs.axolotl.ai/docs/rlhf.html)
  * [Reward Modelling](https://docs.axolotl.ai/docs/reward_modelling.html)
  * [Learning Rate Groups](https://docs.axolotl.ai/docs/lr_groups.html)
  * [LoRA Optimizations](https://docs.axolotl.ai/docs/lora_optims.html)
  * [Dataset Loading](https://docs.axolotl.ai/docs/dataset_loading.html)
  * [Quantization Aware Training (QAT)](https://docs.axolotl.ai/docs/qat.html)
  * [Quantization with torchao](https://docs.axolotl.ai/docs/quantize.html)
  * [Optimizations Guide](https://docs.axolotl.ai/docs/optimizations.html)

* [Core Concepts](https://docs.axolotl.ai/docs/expert_quantization.html)[](https://docs.axolotl.ai/docs/expert_quantization.html)
  * [Batch size vs Gradient accumulation](https://docs.axolotl.ai/docs/batch_vs_grad.html)
  * [Dataset Preprocessing](https://docs.axolotl.ai/docs/dataset_preprocessing.html)
  * [Streaming Datasets](https://docs.axolotl.ai/docs/streaming.html)
  * [Multipack (Sample Packing)](https://docs.axolotl.ai/docs/multipack.html)
  * [Mixed Precision Training](https://docs.axolotl.ai/docs/mixed_precision.html)
  * [Optimizers](https://docs.axolotl.ai/docs/optimizers.html)
  * [Attention](https://docs.axolotl.ai/docs/attention.html)

* [Advanced Features](https://docs.axolotl.ai/docs/expert_quantization.html)[](https://docs.axolotl.ai/docs/expert_quantization.html)
  * [FSDP + QLoRA](https://docs.axolotl.ai/docs/fsdp_qlora.html)
  * [Unsloth](https://docs.axolotl.ai/docs/unsloth.html)
  * [PyTorch ao](https://docs.axolotl.ai/docs/torchao.html)
  * [Custom Integrations](https://docs.axolotl.ai/docs/custom_integrations.html)
  * [Sequence Parallelism](https://docs.axolotl.ai/docs/sequence_parallelism.html)
  * [Gradient Checkpointing and Activation Offloading](https://docs.axolotl.ai/docs/gradient_checkpointing.html)
  * [N-D Parallelism (Beta)](https://docs.axolotl.ai/docs/nd_parallelism.html)
  * [MoE Expert Quantization](https://docs.axolotl.ai/docs/expert_quantization.html)

* [Troubleshooting](https://docs.axolotl.ai/docs/expert_quantization.html)[](https://docs.axolotl.ai/docs/expert_quantization.html)
  * [FAQ](https://docs.axolotl.ai/docs/faq.html)
  * [Debugging](https://docs.axolotl.ai/docs/debugging.html)
  * [NCCL](https://docs.axolotl.ai/docs/nccl.html)

On this page
------------

* [Usage](https://docs.axolotl.ai/docs/expert_quantization.html#usage)
  * [Expert LoRA targeting](https://docs.axolotl.ai/docs/expert_quantization.html#expert-lora-targeting)

* [Requirements](https://docs.axolotl.ai/docs/expert_quantization.html#requirements)
* [Limitations](https://docs.axolotl.ai/docs/expert_quantization.html#limitations)
* [Implementation details](https://docs.axolotl.ai/docs/expert_quantization.html#implementation-details)

1. [Advanced Features](https://docs.axolotl.ai/docs/fsdp_qlora.html)
2. [MoE Expert Quantization](https://docs.axolotl.ai/docs/expert_quantization.html)

MoE Expert Quantization
=======================

 Reduce VRAM usage when training MoE model adapters by quantizing expert weights on load

Transformers v5 changed MoE expert layers from `nn.Linear` to fused `nn.Parameter` (3D+ tensors). This means `bitsandbytes` can no longer quantize them during model loading, resulting in all expert weights being loaded in full bf16 precision and causing massive VRAM usage.

`quantize_moe_experts` solves this by quantizing expert weights during model loading. It intercepts the weight loading process, quantizes each expert tensor on the fly, and immediately frees the original bf16 tensor from VRAM. This dramatically reduces peak memory. For example, GLM-4.7-Flash QLoRA drops from ~127GiB to ~23GiB reserved memory.

Usage
-----

Enable expert quantization in your Axolotl config:

`quantize_moe_experts: true`

This works with both 4-bit (QLoRA) and 8-bit (LoRA) quantization.

### Expert LoRA targeting

You can optionally apply LoRA adapters directly to expert weights using `lora_target_parameters`:

```
lora_target_parameters:
  - mlp.experts.gate_up_proj
  - mlp.experts.down_proj
  # - mlp.gate.weight  # router
```

 Note

`lora_dropout` must be `0` when using `lora_target_parameters`.

Requirements
------------

* Requires (`adapter: lora` and `load_in_8bit: true`) or (`adapter: qlora` and `load_in_4bit: true`)
* CUDA GPUs only (not tested with ROCm or other backends)
* FSDP2 compatible for distributed training

Limitations
-----------

* `lora_target_linear` is not compatible with `quantize_moe_experts`. See [Expert LoRA targeting](https://docs.axolotl.ai/docs/expert_quantization.html#expert-lora-targeting) instead.
* `cpu_ram_efficient_loading` hangs / takes long time with FSDP2 + QLoRA.
* Total model parameter count may display incorrectly (trainable param count is correct).
* FSDP LoRA (8-bit) may have a large initial VRAM spike at the first 1-2 steps, which then drops. QLoRA does not exhibit this.
* FSDP2 may use more VRAM per GPU than single GPU training due to not all layers being properly sharded across ranks.
* Model loading takes longer due to on-demand quantization, even on consecutive runs.
* DeepSpeed has not been tested.

Implementation details
----------------------

The quantization is applied by patching transformers to intercept weight loading. When a 3D+ CUDA tensor with “expert” in its name is detected:

* **4-bit mode:** Uses bitsandbytes NF4 parametrization (configurable via `bnb_4bit_quant_type`).
* **8-bit mode:** Uses a custom row-wise int8 parametrization with bitsandbytes dequantization.

The original bf16 tensor is freed immediately after quantization. Multiple sub-patches are applied to transformers, PEFT and accelerate FSDP2 to support these parametrized expert modules.

For full implementation details, see [PR #3439](https://github.com/axolotl-ai-cloud/axolotl/pull/3439).
