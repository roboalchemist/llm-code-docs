# SqueezeLLM Documentation

## Overview

SqueezeLLM is a post-training quantization framework that uses Dense-and-Sparse Quantization to enable efficient LLM serving.

**Paper:** [SqueezeLLM: Dense-and-Sparse Quantization](https://arxiv.org/abs/2306.07629) (ICML 2024)
**GitHub Repository:** https://github.com/SqueezeAILab/SqueezeLLM
**License:** MIT

## Key Features

- **Dense-and-Sparse Quantization**: Splits weight matrices into:
  - Dense component: heavily quantized without affecting model performance
  - Sparse part: preserves sensitive and outlier parts of weight matrices
- **Non-uniform Quantization**: Uses sensitivity-based compression to maintain accuracy
- **Efficient LLM Serving**: Serve larger models with smaller memory footprints
- **3-bit and 4-bit Precision**: Support for multiple quantization levels
- **Variable Sparsity**: Dense-only (0%), 0.05%, and 0.45% sparsity levels

## Supported Models

### LLaMA (v1)
- LLaMA-7B, 13B, 30B, 65B
- 3-bit and 4-bit quantization
- Multiple sparsity levels (0%, 0.05%, 0.45%)

### LLaMA-2
- LLaMA-2-7B, 13B
- 3-bit and 4-bit quantization

### Mistral
- Mistral-7B (base and instruct variants)
- 3-bit and 4-bit quantization

### Vicuna
- Vicuna-7B, 13B (v1.1, v1.3)
- 3-bit and 4-bit quantization
- Multiple sparsity levels

### XGen
- XGen-7B-8k-Base, XGen-7B-8k-Inst
- 3-bit and 4-bit quantization
- 8K sequence length support

### OPT
- OPT-1.3B, 2.7B, 6.7B, 13B, 30B
- 3-bit and 4-bit quantization
- Multiple sparsity levels

## Performance Highlights

- Vicuna-7B models can be served in 6 GB of memory
- Achieve 2% higher MMLU accuracy than baseline FP16 models
- Maintain same latency as full-precision models
- Support for integration with vLLM framework

## Documentation Index

1. **Installation Guide** - Setup and environment configuration
2. **Usage & Benchmarking** - Running inference and performance evaluation
3. **From-Scratch Quantization** - Quantizing custom models
4. **Model Zoo** - Available pre-quantized models
5. **Integration** - Using SqueezeLLM with vLLM

## Citation

```bibtex
@article{kim2023squeezellm,
  title={SqueezeLLM: Dense-and-Sparse Quantization},
  author={Kim, Sehoon and Hooper, Coleman and Gholami, Amir and Dong, Zhen and Li, Xiuyu and Shen, Sheng and Mahoney, Michael and Keutzer, Kurt},
  journal={arXiv},
  year={2023}
}
```

---

Source: https://github.com/SqueezeAILab/SqueezeLLM
Generated: 2026-01-01T07:38:04.739695