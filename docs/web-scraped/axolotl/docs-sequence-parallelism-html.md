# Source: https://docs.axolotl.ai/docs/sequence_parallelism.html

Title: Sequence Parallelism – Axolotl

URL Source: https://docs.axolotl.ai/docs/sequence_parallelism.html

Published Time: Sat, 07 Mar 2026 12:17:16 GMT

Markdown Content:
Sequence Parallelism – Axolotl
===============

[![Image 1](https://docs.axolotl.ai/image/axolotl_logo_digital_white.svg)![Image 2](https://docs.axolotl.ai/image/axolotl_logo_digital_white.svg)](https://docs.axolotl.ai/index.html)

[](https://twitter.com/axolotl_ai)[](https://github.com/axolotl-ai-cloud/axolotl/)[](https://discord.gg/7m9sfhzaf3)

1. [Advanced Features](https://docs.axolotl.ai/docs/fsdp_qlora.html)
2. [Sequence Parallelism](https://docs.axolotl.ai/docs/sequence_parallelism.html)

[](https://docs.axolotl.ai/docs/sequence_parallelism.html)

* [Home](https://docs.axolotl.ai/index.html)
* [Getting Started](https://docs.axolotl.ai/docs/sequence_parallelism.html)[](https://docs.axolotl.ai/docs/sequence_parallelism.html)
  * [Quickstart](https://docs.axolotl.ai/docs/getting-started.html)
  * [Installation](https://docs.axolotl.ai/docs/installation.html)
  * [Inference and Merging](https://docs.axolotl.ai/docs/inference.html)
  * [Model Guides](https://docs.axolotl.ai/docs/sequence_parallelism.html)[](https://docs.axolotl.ai/docs/sequence_parallelism.html)
    * [Kimi Linear](https://docs.axolotl.ai/docs/models/kimi-linear.html)
    * [Plano Orchestrator](https://docs.axolotl.ai/docs/models/plano.html)
    * [MiMo](https://docs.axolotl.ai/docs/models/mimo.html)
    * [InternVL 3.5](https://docs.axolotl.ai/docs/models/internvl3_5.html)
    * [OLMo 3](https://docs.axolotl.ai/docs/models/olmo3.html)
    * [Trinity](https://docs.axolotl.ai/docs/models/trinity.html)
    * [Arcee AFM](https://docs.axolotl.ai/docs/models/arcee.html)
    * [Ministral3](https://docs.axolotl.ai/docs/sequence_parallelism.html)[](https://docs.axolotl.ai/docs/sequence_parallelism.html)
      * [Ministral3](https://docs.axolotl.ai/docs/models/ministral3.html)
      * [Ministral 3 Thinking](https://docs.axolotl.ai/docs/models/ministral3/think.html)
      * [Ministral 3 Vision](https://docs.axolotl.ai/docs/models/ministral3/vision.html)

    * [Magistral](https://docs.axolotl.ai/docs/sequence_parallelism.html)[](https://docs.axolotl.ai/docs/sequence_parallelism.html)
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

* [Dataset Formats](https://docs.axolotl.ai/docs/dataset-formats/index.html)[](https://docs.axolotl.ai/docs/sequence_parallelism.html)
  * [Pre-training](https://docs.axolotl.ai/docs/dataset-formats/pretraining.html)
  * [Instruction Tuning](https://docs.axolotl.ai/docs/dataset-formats/inst_tune.html)
  * [Conversation](https://docs.axolotl.ai/docs/dataset-formats/conversation.html)
  * [Stepwise Supervised Format](https://docs.axolotl.ai/docs/dataset-formats/stepwise_supervised.html)
  * [Template-Free](https://docs.axolotl.ai/docs/dataset-formats/template_free.html)
  * [Custom Pre-Tokenized Dataset](https://docs.axolotl.ai/docs/dataset-formats/tokenized.html)

* [Deployments](https://docs.axolotl.ai/docs/sequence_parallelism.html)[](https://docs.axolotl.ai/docs/sequence_parallelism.html)
  * [Docker](https://docs.axolotl.ai/docs/docker.html)
  * [Multi-GPU](https://docs.axolotl.ai/docs/multi-gpu.html)
  * [Multi Node](https://docs.axolotl.ai/docs/multi-node.html)
  * [Ray Train](https://docs.axolotl.ai/docs/ray-integration.html)
  * [AMD GPUs on HPC Systems](https://docs.axolotl.ai/docs/amd_hpc.html)
  * [Mac M-series](https://docs.axolotl.ai/docs/mac.html)

* [How To Guides](https://docs.axolotl.ai/docs/sequence_parallelism.html)[](https://docs.axolotl.ai/docs/sequence_parallelism.html)
  * [MultiModal / Vision Language Models (BETA)](https://docs.axolotl.ai/docs/multimodal.html)
  * [RLHF (Beta)](https://docs.axolotl.ai/docs/rlhf.html)
  * [Reward Modelling](https://docs.axolotl.ai/docs/reward_modelling.html)
  * [Learning Rate Groups](https://docs.axolotl.ai/docs/lr_groups.html)
  * [LoRA Optimizations](https://docs.axolotl.ai/docs/lora_optims.html)
  * [Dataset Loading](https://docs.axolotl.ai/docs/dataset_loading.html)
  * [Quantization Aware Training (QAT)](https://docs.axolotl.ai/docs/qat.html)
  * [Quantization with torchao](https://docs.axolotl.ai/docs/quantize.html)
  * [Optimizations Guide](https://docs.axolotl.ai/docs/optimizations.html)

* [Core Concepts](https://docs.axolotl.ai/docs/sequence_parallelism.html)[](https://docs.axolotl.ai/docs/sequence_parallelism.html)
  * [Batch size vs Gradient accumulation](https://docs.axolotl.ai/docs/batch_vs_grad.html)
  * [Dataset Preprocessing](https://docs.axolotl.ai/docs/dataset_preprocessing.html)
  * [Streaming Datasets](https://docs.axolotl.ai/docs/streaming.html)
  * [Multipack (Sample Packing)](https://docs.axolotl.ai/docs/multipack.html)
  * [Mixed Precision Training](https://docs.axolotl.ai/docs/mixed_precision.html)
  * [Optimizers](https://docs.axolotl.ai/docs/optimizers.html)
  * [Attention](https://docs.axolotl.ai/docs/attention.html)

* [Advanced Features](https://docs.axolotl.ai/docs/sequence_parallelism.html)[](https://docs.axolotl.ai/docs/sequence_parallelism.html)
  * [FSDP + QLoRA](https://docs.axolotl.ai/docs/fsdp_qlora.html)
  * [Unsloth](https://docs.axolotl.ai/docs/unsloth.html)
  * [PyTorch ao](https://docs.axolotl.ai/docs/torchao.html)
  * [Custom Integrations](https://docs.axolotl.ai/docs/custom_integrations.html)
  * [Sequence Parallelism](https://docs.axolotl.ai/docs/sequence_parallelism.html)
  * [Gradient Checkpointing and Activation Offloading](https://docs.axolotl.ai/docs/gradient_checkpointing.html)
  * [N-D Parallelism (Beta)](https://docs.axolotl.ai/docs/nd_parallelism.html)
  * [MoE Expert Quantization](https://docs.axolotl.ai/docs/expert_quantization.html)

* [Troubleshooting](https://docs.axolotl.ai/docs/sequence_parallelism.html)[](https://docs.axolotl.ai/docs/sequence_parallelism.html)
  * [FAQ](https://docs.axolotl.ai/docs/faq.html)
  * [Debugging](https://docs.axolotl.ai/docs/debugging.html)
  * [NCCL](https://docs.axolotl.ai/docs/nccl.html)

On this page
------------

* [When to Use Sequence Parallelism](https://docs.axolotl.ai/docs/sequence_parallelism.html#when-to-use-sequence-parallelism)
* [Configuration](https://docs.axolotl.ai/docs/sequence_parallelism.html#configuration)
* [Implementation Details](https://docs.axolotl.ai/docs/sequence_parallelism.html#implementation-details)
* [Requirements](https://docs.axolotl.ai/docs/sequence_parallelism.html#requirements)
* [Limitations](https://docs.axolotl.ai/docs/sequence_parallelism.html#limitations)
* [Example](https://docs.axolotl.ai/docs/sequence_parallelism.html#example)
* [Sample Packing with Sequence Parallelism](https://docs.axolotl.ai/docs/sequence_parallelism.html#sample-packing-with-sequence-parallelism)
* [Effect on Batch Size](https://docs.axolotl.ai/docs/sequence_parallelism.html#effect-on-batch-size)

1. [Advanced Features](https://docs.axolotl.ai/docs/fsdp_qlora.html)
2. [Sequence Parallelism](https://docs.axolotl.ai/docs/sequence_parallelism.html)

Sequence Parallelism
====================

 Train with long sequences split across multiple GPUs.

Sequence parallelism is a technique that splits sequences across multiple GPUs, allowing you to train with very long sequences that wouldn’t fit on a single GPU. Each GPU processes a different portion of the sequence, and the results are aggregated through a ring communication pattern.

When to Use Sequence Parallelism
--------------------------------

Use sequence parallelism when:

* You need to train with sequence lengths that don’t fit into a single GPU’s memory
* You have multiple GPUs available
* You’re experiencing OOM (Out Of Memory) errors with long sequences

Configuration
-------------

To enable sequence parallelism, add the following to your configuration file:

```
# Set to a divisor (> 1) of the number of GPUs available
context_parallel_size: 4  # Split sequences across 4 GPUs
# Optional; strides across the key dimension. Larger values use more memory but should make training faster.
heads_k_stride: 1
# Optional; one of "varlen_llama3" or "batch_ring". Defaults to
# "varlen_llama3" when `sample_packing: true`, and "batch_ring" otherwise.
ring_attn_func:
```

The `context_parallel_size` should be a divisor of the total number of GPUs. For example:

* With 8 GPUs, valid values would be 2, 4, or 8
* With 4 GPUs, valid values would be 2 or 4

Implementation Details
----------------------

When sequence parallelism is enabled:

1. Each sequence is divided into equal chunks across the GPUs in a sequence parallel group
2. The data collator handles the chunking of input_ids, attention_mask, labels, and position_ids
3. Position IDs are adjusted to maintain proper relative positions
4. The trainer uses special ring communication patterns for attention operations

Requirements
------------

To use sequence parallelism, you need:

* Multiple GPUs (at least 2)
* The `ring-flash-attn` package. Install with:
  * `pip install axolotl[ring-flash-attn]` (preferred)
  * `pip install ring-flash-attn>=0.1.4`

Limitations
-----------

* Flash attention must be enabled for this to work (`flash_attention: true` in config YAML)
* May have a small performance overhead due to communication between GPUs

Example
-------

```
base_model: meta-llama/Llama-3-8B-Instruct
sequence_len: 8192

...

context_parallel_size: 4  # Split each sequence into 4 parts, one per GPU
# Optional; strides across the key dimension. Larger values use more memory but should make training faster.
heads_k_stride: 1
# Optional; one of "varlen_llama3" or "batch_ring". Defaults to
# "varlen_llama3" when `sample_packing: true`, and "batch_ring" otherwise.
ring_attn_func:

...
```

This will train the Llama 3 8B model with 8K context length, with each sequence split into 2 subsequences of length 4096 across 2 GPUs.

Sample Packing with Sequence Parallelism
----------------------------------------

Sequence parallelism is compatible with Axolotl’s sample packing functionality. When using both features together:

1. Samples are first packed together
2. The packed sequences are then divided across GPUs in the sequence parallel group
3. Position IDs are automatically adjusted to maintain proper relative positions

Effect on Batch Size
--------------------

When using sequence parallelism, your effective global batch size is **divided** by the `context_parallel_size`. This happens because:

* Each group of `context_parallel_size` GPUs works on the same batch (just different parts of each sequence)
* The number of batches processed per step decreases

For example: - With 8 GPUs and no sequence parallelism: 8 different batches processed per step - With 8 GPUs and `context_parallel_size=4`: Only 2 different batches processed per step (each split across 4 GPUs) - If your per-GPU `micro_batch_size` is 2, the global batch size decreases from 16 to 4
