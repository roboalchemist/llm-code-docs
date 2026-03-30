# Source: https://docs.axolotl.ai/docs/lora_optims.html

Title: LoRA Optimizations – Axolotl

URL Source: https://docs.axolotl.ai/docs/lora_optims.html

Published Time: Sat, 07 Mar 2026 12:17:16 GMT

Markdown Content:
LoRA Optimizations – Axolotl
===============

[![Image 1](https://docs.axolotl.ai/image/axolotl_logo_digital_white.svg)![Image 2](https://docs.axolotl.ai/image/axolotl_logo_digital_white.svg)](https://docs.axolotl.ai/index.html)

[](https://twitter.com/axolotl_ai)[](https://github.com/axolotl-ai-cloud/axolotl/)[](https://discord.gg/7m9sfhzaf3)

1. [How To Guides](https://docs.axolotl.ai/docs/multimodal.html)
2. [LoRA Optimizations](https://docs.axolotl.ai/docs/lora_optims.html)

[](https://docs.axolotl.ai/docs/lora_optims.html)

* [Home](https://docs.axolotl.ai/index.html)
* [Getting Started](https://docs.axolotl.ai/docs/lora_optims.html)[](https://docs.axolotl.ai/docs/lora_optims.html)
  * [Quickstart](https://docs.axolotl.ai/docs/getting-started.html)
  * [Installation](https://docs.axolotl.ai/docs/installation.html)
  * [Inference and Merging](https://docs.axolotl.ai/docs/inference.html)
  * [Model Guides](https://docs.axolotl.ai/docs/lora_optims.html)[](https://docs.axolotl.ai/docs/lora_optims.html)
    * [Kimi Linear](https://docs.axolotl.ai/docs/models/kimi-linear.html)
    * [Plano Orchestrator](https://docs.axolotl.ai/docs/models/plano.html)
    * [MiMo](https://docs.axolotl.ai/docs/models/mimo.html)
    * [InternVL 3.5](https://docs.axolotl.ai/docs/models/internvl3_5.html)
    * [OLMo 3](https://docs.axolotl.ai/docs/models/olmo3.html)
    * [Trinity](https://docs.axolotl.ai/docs/models/trinity.html)
    * [Arcee AFM](https://docs.axolotl.ai/docs/models/arcee.html)
    * [Ministral3](https://docs.axolotl.ai/docs/lora_optims.html)[](https://docs.axolotl.ai/docs/lora_optims.html)
      * [Ministral3](https://docs.axolotl.ai/docs/models/ministral3.html)
      * [Ministral 3 Thinking](https://docs.axolotl.ai/docs/models/ministral3/think.html)
      * [Ministral 3 Vision](https://docs.axolotl.ai/docs/models/ministral3/vision.html)

    * [Magistral](https://docs.axolotl.ai/docs/lora_optims.html)[](https://docs.axolotl.ai/docs/lora_optims.html)
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

* [Dataset Formats](https://docs.axolotl.ai/docs/dataset-formats/index.html)[](https://docs.axolotl.ai/docs/lora_optims.html)
  * [Pre-training](https://docs.axolotl.ai/docs/dataset-formats/pretraining.html)
  * [Instruction Tuning](https://docs.axolotl.ai/docs/dataset-formats/inst_tune.html)
  * [Conversation](https://docs.axolotl.ai/docs/dataset-formats/conversation.html)
  * [Stepwise Supervised Format](https://docs.axolotl.ai/docs/dataset-formats/stepwise_supervised.html)
  * [Template-Free](https://docs.axolotl.ai/docs/dataset-formats/template_free.html)
  * [Custom Pre-Tokenized Dataset](https://docs.axolotl.ai/docs/dataset-formats/tokenized.html)

* [Deployments](https://docs.axolotl.ai/docs/lora_optims.html)[](https://docs.axolotl.ai/docs/lora_optims.html)
  * [Docker](https://docs.axolotl.ai/docs/docker.html)
  * [Multi-GPU](https://docs.axolotl.ai/docs/multi-gpu.html)
  * [Multi Node](https://docs.axolotl.ai/docs/multi-node.html)
  * [Ray Train](https://docs.axolotl.ai/docs/ray-integration.html)
  * [AMD GPUs on HPC Systems](https://docs.axolotl.ai/docs/amd_hpc.html)
  * [Mac M-series](https://docs.axolotl.ai/docs/mac.html)

* [How To Guides](https://docs.axolotl.ai/docs/lora_optims.html)[](https://docs.axolotl.ai/docs/lora_optims.html)
  * [MultiModal / Vision Language Models (BETA)](https://docs.axolotl.ai/docs/multimodal.html)
  * [RLHF (Beta)](https://docs.axolotl.ai/docs/rlhf.html)
  * [Reward Modelling](https://docs.axolotl.ai/docs/reward_modelling.html)
  * [Learning Rate Groups](https://docs.axolotl.ai/docs/lr_groups.html)
  * [LoRA Optimizations](https://docs.axolotl.ai/docs/lora_optims.html)
  * [Dataset Loading](https://docs.axolotl.ai/docs/dataset_loading.html)
  * [Quantization Aware Training (QAT)](https://docs.axolotl.ai/docs/qat.html)
  * [Quantization with torchao](https://docs.axolotl.ai/docs/quantize.html)
  * [Optimizations Guide](https://docs.axolotl.ai/docs/optimizations.html)

* [Core Concepts](https://docs.axolotl.ai/docs/lora_optims.html)[](https://docs.axolotl.ai/docs/lora_optims.html)
  * [Batch size vs Gradient accumulation](https://docs.axolotl.ai/docs/batch_vs_grad.html)
  * [Dataset Preprocessing](https://docs.axolotl.ai/docs/dataset_preprocessing.html)
  * [Streaming Datasets](https://docs.axolotl.ai/docs/streaming.html)
  * [Multipack (Sample Packing)](https://docs.axolotl.ai/docs/multipack.html)
  * [Mixed Precision Training](https://docs.axolotl.ai/docs/mixed_precision.html)
  * [Optimizers](https://docs.axolotl.ai/docs/optimizers.html)
  * [Attention](https://docs.axolotl.ai/docs/attention.html)

* [Advanced Features](https://docs.axolotl.ai/docs/lora_optims.html)[](https://docs.axolotl.ai/docs/lora_optims.html)
  * [FSDP + QLoRA](https://docs.axolotl.ai/docs/fsdp_qlora.html)
  * [Unsloth](https://docs.axolotl.ai/docs/unsloth.html)
  * [PyTorch ao](https://docs.axolotl.ai/docs/torchao.html)
  * [Custom Integrations](https://docs.axolotl.ai/docs/custom_integrations.html)
  * [Sequence Parallelism](https://docs.axolotl.ai/docs/sequence_parallelism.html)
  * [Gradient Checkpointing and Activation Offloading](https://docs.axolotl.ai/docs/gradient_checkpointing.html)
  * [N-D Parallelism (Beta)](https://docs.axolotl.ai/docs/nd_parallelism.html)
  * [MoE Expert Quantization](https://docs.axolotl.ai/docs/expert_quantization.html)

* [Troubleshooting](https://docs.axolotl.ai/docs/lora_optims.html)[](https://docs.axolotl.ai/docs/lora_optims.html)
  * [FAQ](https://docs.axolotl.ai/docs/faq.html)
  * [Debugging](https://docs.axolotl.ai/docs/debugging.html)
  * [NCCL](https://docs.axolotl.ai/docs/nccl.html)

On this page
------------

* [Usage](https://docs.axolotl.ai/docs/lora_optims.html#usage)
* [Requirements](https://docs.axolotl.ai/docs/lora_optims.html#requirements)
* [Implementation details](https://docs.axolotl.ai/docs/lora_optims.html#implementation-details)
  * [Custom autograd functions](https://docs.axolotl.ai/docs/lora_optims.html#custom-autograd-functions)
  * [Triton kernels](https://docs.axolotl.ai/docs/lora_optims.html#triton-kernels)
  * [Integration](https://docs.axolotl.ai/docs/lora_optims.html#integration)

* [Future Work](https://docs.axolotl.ai/docs/lora_optims.html#future-work)

1. [How To Guides](https://docs.axolotl.ai/docs/multimodal.html)
2. [LoRA Optimizations](https://docs.axolotl.ai/docs/lora_optims.html)

LoRA Optimizations
==================

 Custom autograd functions and Triton kernels in Axolotl for optimized LoRA fine-tuning

Inspired by [Unsloth](https://github.com/unslothai/unsloth), we’ve implemented two optimizations for LoRA and QLoRA fine-tuning, supporting both single GPU and multi-GPU (including the DDP, DeepSpeed, and FSDP2 settings) training. These include (1) SwiGLU and GEGLU activation function Triton kernels, and (2) LoRA MLP and attention custom autograd functions. Our goal was to leverage operator fusion and tensor re-use in order to improve speed and reduce memory usage during the forward and backward passes of these calculations.

We currently support several common model architectures, including (but not limited to):

* `llama`
* `mistral`
* `qwen2`
* `gemma`
* `gemma2`
* `gemma3`

The set of models we support is currently limited by our attention patching strategy, which assumes (and replaces) specific code blocks for query / key / value and output projections:

```
ORIGINAL_QKV_CODE = """
    query_states = self.q_proj(hidden_states).view(hidden_shape).transpose(1, 2)
    key_states = self.k_proj(hidden_states).view(hidden_shape).transpose(1, 2)
    value_states = self.v_proj(hidden_states).view(hidden_shape).transpose(1, 2)
""".lstrip(
    "\n"
)

ORIGINAL_O_CODE = """
    attn_output = self.o_proj(attn_output)
""".lstrip(
    "\n"
)
```

Is replaced with:

```
PATCHED_QKV_CODE = """
    query_states, key_states, value_states = self.apply_qkv(hidden_states)
    query_states = query_states.view(hidden_shape).transpose(1, 2)
    key_states = key_states.view(hidden_shape).transpose(1, 2)
    value_states = value_states.view(hidden_shape).transpose(1, 2)
""".lstrip(
    "\n"
)

PATCHED_O_CODE = """
    attn_output = self.apply_o(attn_output)
""".lstrip(
    "\n"
)
```

Where `apply_qkv` and `apply_o` are defined in the `axolotl.kernels.lora` module.

We welcome testing of other model architectures and / or PRs to expand our patching logic to be compatible with more of them.

 Tip

Check out our [LoRA optimizations blog](https://axolotlai.substack.com/p/accelerating-lora-fine-tuning-with).

Usage
-----

These optimizations can be enabled in your Axolotl config YAML file. The `lora_mlp_kernel` option enables the optimized MLP path, while `lora_qkv_kernel` and `lora_o_kernel` enable the fused query-key-value projection and optimized output projection, respectively.

```
lora_mlp_kernel: true
lora_qkv_kernel: true
lora_o_kernel: true
```

 Note

Currently, LoRA kernels are not supported for RLHF training, only SFT.

 Warning

LoRA kernels do not support remote modeling code.

Requirements
------------

* One or more NVIDIA or AMD GPUs (in order to use the Triton kernels)
  * Note: Set `TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1` to enable [memory-efficient attention on AMD GPUs](https://github.com/ROCm/aotriton/issues/16#issuecomment-2346675491)

* Targeted LoRA adapters cannot use Dropout
  * This may limit model expressivity / cause overfitting

* Targeted LoRA adapters cannot have bias terms
  * This may limit model expressivity

Models with pre-existing LoRA adapters that use Dropout or have bias terms may need to be re-finetuned without these features in order to be useful.

Implementation details
----------------------

### Custom autograd functions

The LoRA MLP autograd function optimizes the entire MLP computation path. It fuses the LoRA and base weight computations together and provides a single, efficient backward pass for the entire MLP block.

For attention components, similar optimizations are provided through a function that handles the query, key, and value projections, and a function that handles the output projection. They are designed to work with the existing `transformers` attention implementation via some monkey-patching logic.

### Triton kernels

Two activation functions (SwiGLU and GeGLU) are implemented with Triton kernels for improved speed and memory performance. These kernels handle both the forward and backward passes.

### Integration

The custom autograd functions and Triton kernels are designed to work together. The autograd function manages the high-level computation flow and gradient tracking, while calling the Triton kernels for the activation function computation. During the backward pass, the kernel computes both the activation output and the required gradients, which the autograd function then uses to compute the final gradients for the entire computation path.

Future Work
-----------

* Support for additional model architectures
* Support for dropout and bias
* Additional operator fusions
