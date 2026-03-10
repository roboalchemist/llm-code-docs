# Source: https://docs.axolotl.ai/docs/mixed_precision.html

Title: Mixed Precision Training – Axolotl

URL Source: https://docs.axolotl.ai/docs/mixed_precision.html

Published Time: Sat, 07 Mar 2026 12:17:16 GMT

Markdown Content:
Mixed Precision Training – Axolotl
===============

[![Image 1](https://docs.axolotl.ai/image/axolotl_logo_digital_white.svg)![Image 2](https://docs.axolotl.ai/image/axolotl_logo_digital_white.svg)](https://docs.axolotl.ai/index.html)

[](https://twitter.com/axolotl_ai)[](https://github.com/axolotl-ai-cloud/axolotl/)[](https://discord.gg/7m9sfhzaf3)

1. [Core Concepts](https://docs.axolotl.ai/docs/batch_vs_grad.html)
2. [Mixed Precision Training](https://docs.axolotl.ai/docs/mixed_precision.html)

[](https://docs.axolotl.ai/docs/mixed_precision.html)

* [Home](https://docs.axolotl.ai/index.html)
* [Getting Started](https://docs.axolotl.ai/docs/mixed_precision.html)[](https://docs.axolotl.ai/docs/mixed_precision.html)
  * [Quickstart](https://docs.axolotl.ai/docs/getting-started.html)
  * [Installation](https://docs.axolotl.ai/docs/installation.html)
  * [Inference and Merging](https://docs.axolotl.ai/docs/inference.html)
  * [Model Guides](https://docs.axolotl.ai/docs/mixed_precision.html)[](https://docs.axolotl.ai/docs/mixed_precision.html)
    * [Kimi Linear](https://docs.axolotl.ai/docs/models/kimi-linear.html)
    * [Plano Orchestrator](https://docs.axolotl.ai/docs/models/plano.html)
    * [MiMo](https://docs.axolotl.ai/docs/models/mimo.html)
    * [InternVL 3.5](https://docs.axolotl.ai/docs/models/internvl3_5.html)
    * [OLMo 3](https://docs.axolotl.ai/docs/models/olmo3.html)
    * [Trinity](https://docs.axolotl.ai/docs/models/trinity.html)
    * [Arcee AFM](https://docs.axolotl.ai/docs/models/arcee.html)
    * [Ministral3](https://docs.axolotl.ai/docs/mixed_precision.html)[](https://docs.axolotl.ai/docs/mixed_precision.html)
      * [Ministral3](https://docs.axolotl.ai/docs/models/ministral3.html)
      * [Ministral 3 Thinking](https://docs.axolotl.ai/docs/models/ministral3/think.html)
      * [Ministral 3 Vision](https://docs.axolotl.ai/docs/models/ministral3/vision.html)

    * [Magistral](https://docs.axolotl.ai/docs/mixed_precision.html)[](https://docs.axolotl.ai/docs/mixed_precision.html)
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

* [Dataset Formats](https://docs.axolotl.ai/docs/dataset-formats/index.html)[](https://docs.axolotl.ai/docs/mixed_precision.html)
  * [Pre-training](https://docs.axolotl.ai/docs/dataset-formats/pretraining.html)
  * [Instruction Tuning](https://docs.axolotl.ai/docs/dataset-formats/inst_tune.html)
  * [Conversation](https://docs.axolotl.ai/docs/dataset-formats/conversation.html)
  * [Stepwise Supervised Format](https://docs.axolotl.ai/docs/dataset-formats/stepwise_supervised.html)
  * [Template-Free](https://docs.axolotl.ai/docs/dataset-formats/template_free.html)
  * [Custom Pre-Tokenized Dataset](https://docs.axolotl.ai/docs/dataset-formats/tokenized.html)

* [Deployments](https://docs.axolotl.ai/docs/mixed_precision.html)[](https://docs.axolotl.ai/docs/mixed_precision.html)
  * [Docker](https://docs.axolotl.ai/docs/docker.html)
  * [Multi-GPU](https://docs.axolotl.ai/docs/multi-gpu.html)
  * [Multi Node](https://docs.axolotl.ai/docs/multi-node.html)
  * [Ray Train](https://docs.axolotl.ai/docs/ray-integration.html)
  * [AMD GPUs on HPC Systems](https://docs.axolotl.ai/docs/amd_hpc.html)
  * [Mac M-series](https://docs.axolotl.ai/docs/mac.html)

* [How To Guides](https://docs.axolotl.ai/docs/mixed_precision.html)[](https://docs.axolotl.ai/docs/mixed_precision.html)
  * [MultiModal / Vision Language Models (BETA)](https://docs.axolotl.ai/docs/multimodal.html)
  * [RLHF (Beta)](https://docs.axolotl.ai/docs/rlhf.html)
  * [Reward Modelling](https://docs.axolotl.ai/docs/reward_modelling.html)
  * [Learning Rate Groups](https://docs.axolotl.ai/docs/lr_groups.html)
  * [LoRA Optimizations](https://docs.axolotl.ai/docs/lora_optims.html)
  * [Dataset Loading](https://docs.axolotl.ai/docs/dataset_loading.html)
  * [Quantization Aware Training (QAT)](https://docs.axolotl.ai/docs/qat.html)
  * [Quantization with torchao](https://docs.axolotl.ai/docs/quantize.html)
  * [Optimizations Guide](https://docs.axolotl.ai/docs/optimizations.html)

* [Core Concepts](https://docs.axolotl.ai/docs/mixed_precision.html)[](https://docs.axolotl.ai/docs/mixed_precision.html)
  * [Batch size vs Gradient accumulation](https://docs.axolotl.ai/docs/batch_vs_grad.html)
  * [Dataset Preprocessing](https://docs.axolotl.ai/docs/dataset_preprocessing.html)
  * [Streaming Datasets](https://docs.axolotl.ai/docs/streaming.html)
  * [Multipack (Sample Packing)](https://docs.axolotl.ai/docs/multipack.html)
  * [Mixed Precision Training](https://docs.axolotl.ai/docs/mixed_precision.html)
  * [Optimizers](https://docs.axolotl.ai/docs/optimizers.html)
  * [Attention](https://docs.axolotl.ai/docs/attention.html)

* [Advanced Features](https://docs.axolotl.ai/docs/mixed_precision.html)[](https://docs.axolotl.ai/docs/mixed_precision.html)
  * [FSDP + QLoRA](https://docs.axolotl.ai/docs/fsdp_qlora.html)
  * [Unsloth](https://docs.axolotl.ai/docs/unsloth.html)
  * [PyTorch ao](https://docs.axolotl.ai/docs/torchao.html)
  * [Custom Integrations](https://docs.axolotl.ai/docs/custom_integrations.html)
  * [Sequence Parallelism](https://docs.axolotl.ai/docs/sequence_parallelism.html)
  * [Gradient Checkpointing and Activation Offloading](https://docs.axolotl.ai/docs/gradient_checkpointing.html)
  * [N-D Parallelism (Beta)](https://docs.axolotl.ai/docs/nd_parallelism.html)
  * [MoE Expert Quantization](https://docs.axolotl.ai/docs/expert_quantization.html)

* [Troubleshooting](https://docs.axolotl.ai/docs/mixed_precision.html)[](https://docs.axolotl.ai/docs/mixed_precision.html)
  * [FAQ](https://docs.axolotl.ai/docs/faq.html)
  * [Debugging](https://docs.axolotl.ai/docs/debugging.html)
  * [NCCL](https://docs.axolotl.ai/docs/nccl.html)

On this page
------------

* [1 FP16 Mixed Precision](https://docs.axolotl.ai/docs/mixed_precision.html#sec-fp16)
  * [1.1 Overview](https://docs.axolotl.ai/docs/mixed_precision.html#sec-fp16-overview)
  * [1.2 Configuration](https://docs.axolotl.ai/docs/mixed_precision.html#sec-fp16-config)
  * [1.3 FP16 Considerations](https://docs.axolotl.ai/docs/mixed_precision.html#sec-fp16-considerations)

* [2 BF16 Mixed Precision](https://docs.axolotl.ai/docs/mixed_precision.html#sec-bf16)
  * [2.1 Overview](https://docs.axolotl.ai/docs/mixed_precision.html#sec-bf16-overview)
  * [2.2 Configuration](https://docs.axolotl.ai/docs/mixed_precision.html#sec-bf16-config)

* [3 FP8 Mixed Precision](https://docs.axolotl.ai/docs/mixed_precision.html#sec-fp8)
  * [3.1 What is FP8?](https://docs.axolotl.ai/docs/mixed_precision.html#sec-fp8-overview)
  * [3.2 Requirements](https://docs.axolotl.ai/docs/mixed_precision.html#sec-fp8-software)
  * [3.3 Configuration](https://docs.axolotl.ai/docs/mixed_precision.html#sec-fp8-config)
  * [3.4 Advanced FP8 Configs](https://docs.axolotl.ai/docs/mixed_precision.html#sec-fp8-advanced)

* [4 Best Practices](https://docs.axolotl.ai/docs/mixed_precision.html#sec-best-practices)
  * [4.1 Choosing Precision Format](https://docs.axolotl.ai/docs/mixed_precision.html#sec-choosing-format)
  * [4.2 Validation and Testing](https://docs.axolotl.ai/docs/mixed_precision.html#sec-validation)
  * [4.3 FP8 Particulars](https://docs.axolotl.ai/docs/mixed_precision.html#sec-fp8-details)

1. [Core Concepts](https://docs.axolotl.ai/docs/batch_vs_grad.html)
2. [Mixed Precision Training](https://docs.axolotl.ai/docs/mixed_precision.html)

Mixed Precision Training
========================

 Code

Mixed precision training uses lower precision data types to reduce memory usage and increase training speed while maintaining model quality. Axolotl supports several mixed precision formats:

* **FP16** - Half precision 16-bit (Pascal generation+)
* **BF16** - Brain Float 16-bit (Ampere generation+)
* **FP8** - 8-bit floating point (Hopper generation+)

1 FP16 Mixed Precision
----------------------

### 1.1 Overview

FP16 is the traditional half-precision format, supported on older GPUs but can be less numerically stable than BF16.

### 1.2 Configuration

`fp16: true`

### 1.3 FP16 Considerations

* May require gradient scaling to prevent underflow
* Less numerically stable than BF16
* Can cause training instability with some model architectures
* Consider using BF16 if your hardware supports it

2 BF16 Mixed Precision
----------------------

### 2.1 Overview

BF16 (Brain Float 16) offers better numerical stability than FP16 and is the recommended mixed precision format for modern GPUs. It provides the same dynamic range as FP32 while using half the memory.

### 2.2 Configuration

```
# Automatic BF16 detection (recommended)
bf16: auto

# Or explicitly enable
bf16: true

# For evaluation with BF16
bf16: full  # Equivalent to bf16_full_eval in the HF trainer
```

3 FP8 Mixed Precision
---------------------

 Note

FP8 support is experimental and requires compatible hardware (H100, H200) and recent PyTorch versions with TorchAO.

### 3.1 What is FP8?

FP8 (8-bit floating point) can provide significant time savings compared to FP16/BF16 while maintaining training stability. Axolotl’s implementation uses PyTorch’s TorchAO library with “tensorwise” scaling strategy.

### 3.2 Requirements

* Hopper+ GPUs (H100/H200)
* PyTorch 2.7+ (+ compatible TorchAO version)
* CUDA 12.4+

### 3.3 Configuration

Add to your YAML config:

```
# Enable FP8 mixed precision
fp8: true

# Optional: Enable FP8 for FSDP all-gather operations
fp8_enable_fsdp_float8_all_gather: true

# Enable torch.compile (almost always necessary for FP8 speedups)
torch_compile: true
```

 Important

**torch.compile is critical for FP8 performance**

FP8 training requires `torch_compile: true` to see meaningful speedups. Without compilation, FP8 may actually be slower and use more memory than FP16/BF16.

### 3.4 Advanced FP8 Configs

For [FSDP](https://docs.axolotl.ai/docs/multi-gpu.html#sec-fsdp) (Fully Sharded Data Parallel) training:

```
fp8: true
fp8_enable_fsdp_float8_all_gather: true

torch_compile: true

# FSDP configuration
fsdp_version: 2
fsdp_config:
  offload_params: false
  cpu_ram_efficient_loading: true
  auto_wrap_policy: TRANSFORMER_BASED_WRAP
  transformer_layer_cls_to_wrap: LlamaDecoderLayer
  state_dict_type: FULL_STATE_DICT
  reshard_after_forward: true
```

4 Best Practices
----------------

### 4.1 Choosing Precision Format

* **Start with automatic detection**: `bf16: auto`
* **For Hopper+ (H100/H200)**: Try FP8 + torch.compile for maximum speed
* **For Ampere (A100/RTX 30/40)**: Use BF16
* **For older Pascal/Turing GPUs**: Use FP16 with caution
* **For very old or unsupported GPUs**: Use FP32

### 4.2 Validation and Testing

Always validate your mixed precision setup:

* **Start with a small dataset** to verify stability
* **Monitor loss curves** for irregularities
* **Compare with FP32 baseline** when possible
* **Test evaluation metrics** match expectations

### 4.3 FP8 Particulars

* Use cases
  * Single GPU training
  * Multi GPU training with FSDP2 or Deepspeed

* Speedups
  * Please refer to the [TorchAO FP8 training benchmarks](https://github.com/pytorch/ao/tree/main/torchao/float8#rowwise-scaling) for expected matmul speedups for different (M, K, N) settings
  * Concrete number for LLaMA 3 8B training can be found [here](https://github.com/pytorch/ao/tree/main/torchao/float8#training-benchmarks)

* Known issues:
  * FP8 + DDP + `torch.compile` (causes [error](https://gist.github.com/djsaunde/0c1664c32e44a64d31b5e01b4aafe5c4))
  * FP8 + FSDP2 + `torch.compile` + FSDP2 activation checkpointing tends to be _slower_ than the BF16 equivalent training
  * Flash Attention 2 does not play nicely with `torch.compile`

See `examples/llama-3/3b-fp8-fsdp2.yaml` for an optimized example config. Enabling FP8 mixed precision + FP8 all-gather training results in ~10% faster iterations per second vs.BF16 for a relatively small (3B param) model

For more information on multi-GPU training, see our [Multi-GPU guide](https://docs.axolotl.ai/docs/multi-gpu.html).

##### Source Code

```
---
title: "Mixed Precision Training"
format:
  html:
    toc: true
    toc-depth: 3
    number-sections: true
    code-tools: true
execute:
  enabled: false
---

Mixed precision training uses lower precision data types to reduce memory usage and increase training speed while maintaining model quality. Axolotl supports several mixed precision formats:

- **FP16** - Half precision 16-bit (Pascal generation+)
- **BF16** - Brain Float 16-bit (Ampere generation+)
- **FP8** - 8-bit floating point (Hopper generation+)

## FP16 Mixed Precision {#sec-fp16}

### Overview {#sec-fp16-overview}

FP16 is the traditional half-precision format, supported on older GPUs but can be less numerically stable than BF16.

### Configuration {#sec-fp16-config}

```{.yaml}
fp16: true
```

### FP16 Considerations {#sec-fp16-considerations}

* May require gradient scaling to prevent underflow
* Less numerically stable than BF16
* Can cause training instability with some model architectures
* Consider using BF16 if your hardware supports it

## BF16 Mixed Precision {#sec-bf16}

### Overview {#sec-bf16-overview}

BF16 (Brain Float 16) offers better numerical stability than FP16 and is the recommended mixed precision format for modern GPUs. It provides the same dynamic range as FP32 while using half the memory.

### Configuration {#sec-bf16-config}

```{.yaml}
# Automatic BF16 detection (recommended)
bf16: auto

# Or explicitly enable
bf16: true

# For evaluation with BF16
bf16: full  # Equivalent to bf16_full_eval in the HF trainer
```

## FP8 Mixed Precision {#sec-fp8}

::: {.callout-note}
FP8 support is experimental and requires compatible hardware (H100, H200) and recent PyTorch versions with TorchAO.
:::

### What is FP8? {#sec-fp8-overview}

FP8 (8-bit floating point) can provide significant time savings compared to FP16/BF16 while maintaining training stability. Axolotl's implementation uses PyTorch's TorchAO library with "tensorwise" scaling strategy.

### Requirements {#sec-fp8-software}

* Hopper+ GPUs (H100/H200)
* PyTorch 2.7+ (+ compatible TorchAO version)
* CUDA 12.4+

### Configuration {#sec-fp8-config}

Add to your YAML config:

```{.yaml}
# Enable FP8 mixed precision
fp8: true

# Optional: Enable FP8 for FSDP all-gather operations
fp8_enable_fsdp_float8_all_gather: true

# Enable torch.compile (almost always necessary for FP8 speedups)
torch_compile: true
```

::: {.callout-important}
**torch.compile is critical for FP8 performance**

FP8 training requires `torch_compile: true` to see meaningful speedups. Without compilation, FP8 may actually be slower and use more memory than FP16/BF16.
:::

### Advanced FP8 Configs {#sec-fp8-advanced}

For [FSDP](multi-gpu.qmd#sec-fsdp) (Fully Sharded Data Parallel) training:

```{.yaml}
fp8: true
fp8_enable_fsdp_float8_all_gather: true

torch_compile: true

# FSDP configuration
fsdp_version: 2
fsdp_config:
  offload_params: false
  cpu_ram_efficient_loading: true
  auto_wrap_policy: TRANSFORMER_BASED_WRAP
  transformer_layer_cls_to_wrap: LlamaDecoderLayer
  state_dict_type: FULL_STATE_DICT
  reshard_after_forward: true
```

## Best Practices {#sec-best-practices}

### Choosing Precision Format {#sec-choosing-format}

* **Start with automatic detection**: `bf16: auto`
* **For Hopper+ (H100/H200)**: Try FP8 + torch.compile for maximum speed
* **For Ampere (A100/RTX 30/40)**: Use BF16
* **For older Pascal/Turing GPUs**: Use FP16 with caution
* **For very old or unsupported GPUs**: Use FP32

### Validation and Testing {#sec-validation}

Always validate your mixed precision setup:

* **Start with a small dataset** to verify stability
* **Monitor loss curves** for irregularities
* **Compare with FP32 baseline** when possible
* **Test evaluation metrics** match expectations

### FP8 Particulars {#sec-fp8-details}

* Use cases
  * Single GPU training
  * Multi GPU training with FSDP2 or Deepspeed
* Speedups
  * Please refer to the [TorchAO FP8 training benchmarks](https://github.com/pytorch/ao/tree/main/torchao/float8#rowwise-scaling) for expected matmul speedups for different (M, K, N) settings
  * Concrete number for LLaMA 3 8B training can be found [here](https://github.com/pytorch/ao/tree/main/torchao/float8#training-benchmarks)
* Known issues:
  * FP8 + DDP + `torch.compile` (causes [error](https://gist.github.com/djsaunde/0c1664c32e44a64d31b5e01b4aafe5c4))
  * FP8 + FSDP2 + `torch.compile` + FSDP2 activation checkpointing tends to be _slower_ than the BF16 equivalent training
  * Flash Attention 2 does not play nicely with `torch.compile`

See `examples/llama-3/3b-fp8-fsdp2.yaml` for an optimized example config. Enabling FP8 mixed precision + FP8 all-gather training results in ~10% faster iterations per second vs. BF16 for a relatively small (3B param) model

For more information on multi-GPU training, see our [Multi-GPU guide](multi-gpu.qmd).

```
