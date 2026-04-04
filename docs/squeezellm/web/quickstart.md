# Quick Start Guide

## Source: https://github.com/SqueezeAILab/SqueezeLLM/blob/main/README.md

## Download Pre-Quantized Models

SqueezeLLM provides pre-quantized models on Hugging Face Hub. Models are available for:

- **Bitwidth**: 3-bit and 4-bit
- **Sparsity**: 0% (dense-only), 0.05%, and 0.45%
- **Model families**: LLaMA, LLaMA-2, Mistral, Vicuna, XGen, OPT

All models are available at: https://huggingface.co/squeeze-ai-lab

Example model naming scheme:
- `sq-llama-7b-w3-s0`: LLaMA-7B, 3-bit, dense-only
- `sq-llama-7b-w4-s45`: LLaMA-7B, 4-bit, 0.45% sparsity

## Running Inference

### Basic Inference Example

```bash
# Download quantized model
# Example: sq-llama-7b-w3-s0.pt

# Set up environment
export CUDA_VISIBLE_DEVICES=0
export MODEL_PATH=/path/to/base/model  # Required for LLaMA v1 and Vicuna v1.1
export CKPT_PATH=/path/to/sq-llama-7b-w3-s0.pt

# Run inference
python llama.py $MODEL_PATH c4 --wbits 3 --load $CKPT_PATH --benchmark 128
```

### Benchmarking

#### LLaMA Benchmarking

```bash
CUDA_VISIBLE_DEVICES=0 python llama.py {model_path} c4 --wbits 3 --load sq-llama-7b-w3-s0.pt --benchmark 128 --check --torch_profile
```

For models with sparsity:

```bash
CUDA_VISIBLE_DEVICES=0 python llama.py {model_path} c4 --wbits 3 --load sq-llama-7b-w3-s5.pt --include_sparse --benchmark 128 --check --torch_profile
```

#### XGen Benchmarking

```bash
CUDA_VISIBLE_DEVICES=0 python llama.py models/xgen-7b-8k-base c4 --wbits 3 --load sq-xgen-7b-8k-base-w3-s0.pt --benchmark 128 --check --torch_profile
```

### Perplexity Evaluation

Evaluate model perplexity on C4 dataset:

```bash
# Dense-only models
CUDA_VISIBLE_DEVICES=0 python llama.py {model_path} c4 --wbits 3 --load sq-llama-7b-w3-s0.pt --eval

# Sparse models
CUDA_VISIBLE_DEVICES=0 python llama.py {model_path} c4 --wbits 3 --load sq-llama-7b-w3-s5.pt --include_sparse --eval
```

## Command-Line Options

### Common Arguments

- `--wbits`: Quantization bitwidth (3 or 4)
- `--load`: Path to quantized checkpoint
- `--benchmark`: Run benchmarking with specified sequence length
- `--eval`: Evaluate perplexity
- `--check`: Verify quantized model outputs
- `--torch_profile`: Enable PyTorch profiling for runtime analysis
- `--include_sparse`: Include sparse components (for D+S quantized models)

## GPU Requirements

### Minimum Requirements
- 8GB VRAM for 7B models
- 16GB VRAM for 13B models

### Recommended Setup
- A5000 or A6000 GPU
- CUDA 11.3+
- CUDNN 8.2+

## Integration with vLLM

SqueezeLLM is supported in the official vLLM framework for efficient serving:

https://github.com/vllm-project/vllm

See vLLM documentation for integration details.

## Next Steps

- For custom model quantization, see [From-Scratch Quantization Guide](quantization-guide.md)
- For detailed model configurations, see [Model Zoo](model-zoo.md)
- For implementation details, see [Research Paper](https://arxiv.org/abs/2306.07629)

---

Generated from: https://github.com/SqueezeAILab/SqueezeLLM
