# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/model-optimization/quantization/quantization.html.md

Title: Quantization — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/model-optimization/quantization/quantization.html

Published Time: Fri, 18 Jul 2025 19:27:10 GMT

Markdown Content:
Quantization[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/model-optimization/quantization/quantization.html.md#quantization "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

NeMo offers Post-Training Quantization (PTQ) to postprocess a FP16/BF16 model to a lower precision format for efficient deployment. The following sections detail how to use it.

Post-Training Quantization[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/model-optimization/quantization/quantization.html.md#post-training-quantization "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

PTQ enables deploying a model in a low-precision format – FP8, INT4, or INT8 – for efficient serving. Different [quantization methods](https://nvidia.github.io/TensorRT-Model-Optimizer/guides/_choosing_quant_methods.html.md) are available including FP8 quantization, INT8 SmoothQuant, and INT4 AWQ.

Model quantization has three primary benefits: reduced model memory requirements, lower memory bandwidth pressure, and increased inference throughput.

In NeMo, quantization is enabled by the [NVIDIA TensorRT Model Optimizer (ModelOpt)](https://github.com/NVIDIA/TensorRT-Model-Optimizer.md) – a library to quantize and compress deep learning models for optimized inference on GPUs.

The quantization process consists of the following steps:

1.   Load a model checkpoint using an appropriate parallelism strategy.

2.   Calibrate the model to obtain scaling factors for lower-precision GEMMs.

3.   Produce a [TensorRT-LLM checkpoint](https://nvidia.github.io/TensorRT-LLM/architecture/checkpoint.html.md) with model config (json) and quantized weights (safetensors). Additionally, the necessary context to set up the model tokenizer is saved.

Loading models requires using a custom ModelOpt spec defined in the [megatron.core.post_training.modelopt](https://github.com/NVIDIA/Megatron-LM/tree/main/megatron/core/post_training/modelopt.md) module for both Transformer and Mamba-type models. Typically, the calibration step is lightweight and uses a small dataset to obtain appropriate statistics for scaling tensors. The output directory produced is ready to be used to build a serving engine with the NVIDIA TensorRT-LLM library (see [Deploy NeMo Models by Exporting TensorRT-LLM](https://docs.nvidia.com/nemo-framework/user-guide/latest/deployment/llm/nemo_models/optimized/tensorrt_llm.html.md#deploy-nemo-framework-models-tensorrt-llm)). We refer to this checkpoint as the qnemo checkpoint henceforth.

The quantization algorithm can also be conveniently set to `"no_quant"` to perform only the weights export step using the default precision for TensorRT-LLM deployment. This is useful for obtaining baseline performance and accuracy results for comparison.

### Support Matrix[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/model-optimization/quantization/quantization.html.md#support-matrix "Link to this heading")

The table below presents a verified model support matrix for popular LLM architectures. Support for other model families is experimental.

| Model Name | Model Parameters | Decoder Type | FP8 | INT8 SQ | INT4 AWQ |
| --- | --- | --- | --- | --- | --- |
| GPT | 2B, 8B, 43B | gptnext | ✓ | ✓ | ✓ |
| Nemotron-3 | 8B, 22B | gptnext | ✓ | ✓ | ✓ |
| Nemotron-4 | 15B, 340B | gptnext | ✓ | ✓ | ✓ |
| Llama 2 | 7B, 13B, 70B | llama | ✓ | ✓ | ✓ |
| Llama 3 | 8B, 70B | llama | ✓ | ✓ | ✓ |
| Llama 3.1 | 8B, 70B, 405B | llama | ✓ | ✓ | ✓ |
| Llama 3.2 | 1B, 3B | llama | ✓ | ✓ | ✓ |
| Falcon | 7B, 40B | falcon | ✗ | ✗ | ✗ |
| Gemma 1 | 2B, 7B | gemma | ✓ | ✓ | ✓ |
| StarCoder 1 | 15B | gpt2 | ✓ | ✓ | ✓ |
| StarCoder 2 | 3B, 7B, 15B | gptnext | ✓ | ✓ | ✓ |
| Mistral | 7B | llama | ✓ | ✓ | ✓ |
| Mixtral | 8x7B | llama | ✓ | ✗ | ✗ |

When running PTQ, the decoder type for exporting TensorRT-LLM checkpoint is detected automatically based on the model used. If necessary, it can be overriden using `decoder_type` parameter.

### Example[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/model-optimization/quantization/quantization.html.md#example "Link to this heading")

The example below shows how to quantize the Llama 3 70b model into FP8 precision, using tensor parallelism of 8 on a single DGX H100 node. The quantized model is designed for serving using 2 H100 GPUs specified with the `export.inference_tp` parameter.

The quantization workflow can be launched with NeMo CLI or using a PTQ script with `torchrun` or Slurm. This is shown below.

#### Use the NeMo CLI[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/model-optimization/quantization/quantization.html.md#use-the-nemo-cli "Link to this heading")

The command below can be launched inside a NeMo container (only single-node use cases are supported):

CALIB_TP=8
INFER_TP=2

nemo llm ptq \
 nemo_checkpoint=/opt/checkpoints/llama3-70b-base \
 calibration_tp=$CALIB_TP \
 quantization_config.algorithm=fp8 \
 export_config.inference_tp=$INFER_TP \
 export_config.path=/opt/checkpoints/llama3-70b-base-fp8-qnemo \
 run.executor=torchrun \
 run.executor.ntasks_per_node=$CALIB_TP

#### Use the PTQ script with `torchrun` or Slurm[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/model-optimization/quantization/quantization.html.md#use-the-ptq-script-with-torchrun-or-slurm "Link to this heading")

Alternatively, the `torchrun` command and [scripts/llm/ptq.py](https://github.com/NVIDIA/NeMo/blob/main/scripts/llm/ptq.py.md) can be used directly. The script must be launched correctly with the number of processes equal to tensor parallelism:

CALIB_TP=8
CALIB_PP=1
INFER_TP=2

torchrun --nproc_per_node $CALIB_TP /opt/NeMo/scripts/llm/ptq.py \
 --nemo_checkpoint=/opt/checkpoints/llama3-70b-base \
 --calibration_tp=$CALIB_TP \
 --calibration_pp=$CALIB_PP \
 --algorithm=fp8 \
 --inference_tp=$INFER_TP \
 --export_path=/opt/checkpoints/llama3-70b-base-fp8-qnemo

For large models, this script can be launched on Slurm for multi-node use cases by setting the `--calibration_tp` and `--calibration_pp` along with the corresponding Slurm `--ntasks-per-node` and `--nodes` parameters, respectively:

CALIB_TP=8
CALIB_PP=2
INFER_TP=8

srun --nodes $CALIB_PP --ntasks-per-node $CALIB_TP ... \
 python /opt/NeMo/scripts/llm/ptq.py \
 --nemo_checkpoint=/opt/checkpoints/nemotron4-340b-base \
 --calibration_tp=$CALIB_TP \
 --calibration_pp=$CALIB_PP \
 ...

For the Llama 3 70b example, the output directory has the following structure:

llama3-70b-base-fp8-qnemo/
├── config.json
├── nemo_context/
├── rank0.safetensors
└── rank1.safetensors

The next step is to build a TensorRT-LLM engine for the checkpoint produced. This can be conveniently achieved and run using the `TensorRTLLM` class available in the `nemo.export` module. See [Deploy NeMo Models by Exporting TensorRT-LLM](https://docs.nvidia.com/nemo-framework/user-guide/latest/deployment/llm/nemo_models/optimized/tensorrt_llm.html.md#deploy-nemo-framework-models-tensorrt-llm) for details. Alternatively, you can use the TensorRT-LLM trtllm-build command directly.

References[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/model-optimization/quantization/quantization.html.md#references "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Please refer to the following papers for more details on quantization techniques:

*   [Integer Quantization for Deep Learning Inference: Principles and Empirical Evaluation, 2020](https://arxiv.org/abs/2004.09602.md)

*   [FP8 Formats for Deep Learning, 2022](https://arxiv.org/abs/2209.05433.md)

*   [SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models, 2022](https://arxiv.org/abs/2211.10438.md)

*   [AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration, 2023](https://arxiv.org/abs/2306.00978.md)

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/model-optimization/quantization/quantization.html.md#references)
- [quantization methods](https://nvidia.github.io/TensorRT-Model-Optimizer/guides/_choosing_quant_methods.html.md)
- [NVIDIA TensorRT Model Optimizer (ModelOpt)](https://github.com/NVIDIA/TensorRT-Model-Optimizer.md)
- [TensorRT-LLM checkpoint](https://nvidia.github.io/TensorRT-LLM/architecture/checkpoint.html.md)
- [megatron.core.post_training.modelopt](https://github.com/NVIDIA/Megatron-LM/tree/main/megatron/core/post_training/modelopt.md)
- [Deploy NeMo Models by Exporting TensorRT-LLM](https://docs.nvidia.com/nemo-framework/user-guide/latest/deployment/llm/nemo_models/optimized/tensorrt_llm.html.md#deploy-nemo-framework-models-tensorrt-llm)
- [scripts/llm/ptq.py](https://github.com/NVIDIA/NeMo/blob/main/scripts/llm/ptq.py.md)
- [Integer Quantization for Deep Learning Inference: Principles and Empirical Evaluation, 2020](https://arxiv.org/abs/2004.09602.md)
- [FP8 Formats for Deep Learning, 2022](https://arxiv.org/abs/2209.05433.md)
- [SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models, 2022](https://arxiv.org/abs/2211.10438.md)
- [AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration, 2023](https://arxiv.org/abs/2306.00978.md)
