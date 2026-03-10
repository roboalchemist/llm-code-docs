# Source: https://docs.axolotl.ai/docs/qat.html

Title: Quantization Aware Training (QAT) – Axolotl

URL Source: https://docs.axolotl.ai/docs/qat.html

Markdown Content:
Quantization Aware Training (QAT) – Axolotl
===============

[![Image 1](https://docs.axolotl.ai/image/axolotl_logo_digital_white.svg)![Image 2](https://docs.axolotl.ai/image/axolotl_logo_digital_white.svg)](https://docs.axolotl.ai/index.html)

[](https://twitter.com/axolotl_ai)[](https://github.com/axolotl-ai-cloud/axolotl/)[](https://discord.gg/7m9sfhzaf3)

1. [How To Guides](https://docs.axolotl.ai/docs/multimodal.html)
2. [Quantization Aware Training (QAT)](https://docs.axolotl.ai/docs/qat.html)

[](https://docs.axolotl.ai/docs/qat.html)

* [Home](https://docs.axolotl.ai/index.html)
* [Getting Started](https://docs.axolotl.ai/docs/qat.html)[](https://docs.axolotl.ai/docs/qat.html)
  * [Quickstart](https://docs.axolotl.ai/docs/getting-started.html)
  * [Installation](https://docs.axolotl.ai/docs/installation.html)
  * [Inference and Merging](https://docs.axolotl.ai/docs/inference.html)
  * [Model Guides](https://docs.axolotl.ai/docs/qat.html)[](https://docs.axolotl.ai/docs/qat.html)
    * [Kimi Linear](https://docs.axolotl.ai/docs/models/kimi-linear.html)
    * [Plano Orchestrator](https://docs.axolotl.ai/docs/models/plano.html)
    * [MiMo](https://docs.axolotl.ai/docs/models/mimo.html)
    * [InternVL 3.5](https://docs.axolotl.ai/docs/models/internvl3_5.html)
    * [OLMo 3](https://docs.axolotl.ai/docs/models/olmo3.html)
    * [Trinity](https://docs.axolotl.ai/docs/models/trinity.html)
    * [Arcee AFM](https://docs.axolotl.ai/docs/models/arcee.html)
    * [Ministral3](https://docs.axolotl.ai/docs/qat.html)[](https://docs.axolotl.ai/docs/qat.html)
      * [Ministral3](https://docs.axolotl.ai/docs/models/ministral3.html)
      * [Ministral 3 Thinking](https://docs.axolotl.ai/docs/models/ministral3/think.html)
      * [Ministral 3 Vision](https://docs.axolotl.ai/docs/models/ministral3/vision.html)

    * [Magistral](https://docs.axolotl.ai/docs/qat.html)[](https://docs.axolotl.ai/docs/qat.html)
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

* [Dataset Formats](https://docs.axolotl.ai/docs/dataset-formats/index.html)[](https://docs.axolotl.ai/docs/qat.html)
  * [Pre-training](https://docs.axolotl.ai/docs/dataset-formats/pretraining.html)
  * [Instruction Tuning](https://docs.axolotl.ai/docs/dataset-formats/inst_tune.html)
  * [Conversation](https://docs.axolotl.ai/docs/dataset-formats/conversation.html)
  * [Stepwise Supervised Format](https://docs.axolotl.ai/docs/dataset-formats/stepwise_supervised.html)
  * [Template-Free](https://docs.axolotl.ai/docs/dataset-formats/template_free.html)
  * [Custom Pre-Tokenized Dataset](https://docs.axolotl.ai/docs/dataset-formats/tokenized.html)

* [Deployments](https://docs.axolotl.ai/docs/qat.html)[](https://docs.axolotl.ai/docs/qat.html)
  * [Docker](https://docs.axolotl.ai/docs/docker.html)
  * [Multi-GPU](https://docs.axolotl.ai/docs/multi-gpu.html)
  * [Multi Node](https://docs.axolotl.ai/docs/multi-node.html)
  * [Ray Train](https://docs.axolotl.ai/docs/ray-integration.html)
  * [AMD GPUs on HPC Systems](https://docs.axolotl.ai/docs/amd_hpc.html)
  * [Mac M-series](https://docs.axolotl.ai/docs/mac.html)

* [How To Guides](https://docs.axolotl.ai/docs/qat.html)[](https://docs.axolotl.ai/docs/qat.html)
  * [MultiModal / Vision Language Models (BETA)](https://docs.axolotl.ai/docs/multimodal.html)
  * [RLHF (Beta)](https://docs.axolotl.ai/docs/rlhf.html)
  * [Reward Modelling](https://docs.axolotl.ai/docs/reward_modelling.html)
  * [Learning Rate Groups](https://docs.axolotl.ai/docs/lr_groups.html)
  * [LoRA Optimizations](https://docs.axolotl.ai/docs/lora_optims.html)
  * [Dataset Loading](https://docs.axolotl.ai/docs/dataset_loading.html)
  * [Quantization Aware Training (QAT)](https://docs.axolotl.ai/docs/qat.html)
  * [Quantization with torchao](https://docs.axolotl.ai/docs/quantize.html)
  * [Optimizations Guide](https://docs.axolotl.ai/docs/optimizations.html)

* [Core Concepts](https://docs.axolotl.ai/docs/qat.html)[](https://docs.axolotl.ai/docs/qat.html)
  * [Batch size vs Gradient accumulation](https://docs.axolotl.ai/docs/batch_vs_grad.html)
  * [Dataset Preprocessing](https://docs.axolotl.ai/docs/dataset_preprocessing.html)
  * [Streaming Datasets](https://docs.axolotl.ai/docs/streaming.html)
  * [Multipack (Sample Packing)](https://docs.axolotl.ai/docs/multipack.html)
  * [Mixed Precision Training](https://docs.axolotl.ai/docs/mixed_precision.html)
  * [Optimizers](https://docs.axolotl.ai/docs/optimizers.html)
  * [Attention](https://docs.axolotl.ai/docs/attention.html)

* [Advanced Features](https://docs.axolotl.ai/docs/qat.html)[](https://docs.axolotl.ai/docs/qat.html)
  * [FSDP + QLoRA](https://docs.axolotl.ai/docs/fsdp_qlora.html)
  * [Unsloth](https://docs.axolotl.ai/docs/unsloth.html)
  * [PyTorch ao](https://docs.axolotl.ai/docs/torchao.html)
  * [Custom Integrations](https://docs.axolotl.ai/docs/custom_integrations.html)
  * [Sequence Parallelism](https://docs.axolotl.ai/docs/sequence_parallelism.html)
  * [Gradient Checkpointing and Activation Offloading](https://docs.axolotl.ai/docs/gradient_checkpointing.html)
  * [N-D Parallelism (Beta)](https://docs.axolotl.ai/docs/nd_parallelism.html)
  * [MoE Expert Quantization](https://docs.axolotl.ai/docs/expert_quantization.html)

* [Troubleshooting](https://docs.axolotl.ai/docs/qat.html)[](https://docs.axolotl.ai/docs/qat.html)
  * [FAQ](https://docs.axolotl.ai/docs/faq.html)
  * [Debugging](https://docs.axolotl.ai/docs/debugging.html)
  * [NCCL](https://docs.axolotl.ai/docs/nccl.html)

On this page
------------

* [Overview](https://docs.axolotl.ai/docs/qat.html#overview)
* [Configuring QAT in Axolotl](https://docs.axolotl.ai/docs/qat.html#configuring-qat-in-axolotl)

1. [How To Guides](https://docs.axolotl.ai/docs/multimodal.html)
2. [Quantization Aware Training (QAT)](https://docs.axolotl.ai/docs/qat.html)

Quantization Aware Training (QAT)
=================================

Overview
--------

[Quantization Aware Training](https://pytorch.org/blog/introduction-to-quantization-on-pytorch/#quantization-aware-training) (QAT) is a technique for improving the accuracy of models which are quantized by applying “fake” quantizations to the model’s weights (and optionally, activations) during training. This fake quantization allows for the model to adjust for noise introduced by the quantization, so when the model is eventually quantized, the accuracy loss is minimized. We use the quantization techniques implemented in [torchao](https://github.com/pytorch/ao) to provide support for QAT and post-training quantization (PTQ) in axolotl.

We recommend reviewing the excellent QAT tutorial in the [torchtune library](https://pytorch.org/torchtune/main/tutorials/qat_finetune.html#quantizing-the-qat-model), and the QAT documentation in the [torchao library](https://github.com/pytorch/ao/tree/main/torchao/quantization/qat), for more details.

Configuring QAT in Axolotl
--------------------------

To enable QAT in axolotl, add the following to your configuration file:

```
qat:
  activation_dtype: # Optional[str] = "int8". Fake quantization layout to use for activation quantization. Valid options are "int4", "int8", "float8"
  weight_dtype: # Optional[str] = "int8". Fake quantization layout to use for weight quantization. Valid options are "int4", "fp8", and "nvfp4".
  group_size: # Optional[int] = 32. The number of elements in each group for per-group fake quantization
  fake_quant_after_n_steps: # Optional[int] = None. The number of steps to apply fake quantization after
```

We support the following quantization schemas:

* `Int4WeightOnly` (requires the `fbgemm-gpu` extra when installing Axolotl)
* `Int8DynamicActivationInt4Weight`
* `Float8DynamicActivationFloat8Weight`
* `Float8DynamicActivationInt4Weight`
* `NVFP4`

Once you have finished training, you must quantize your model by using the same quantization configuration which you used to train the model with. You can use the [`quantize`](https://docs.axolotl.ai/docs/quantize.html) command to do this.
