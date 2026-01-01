# Installation Guide

## Source: https://github.com/SqueezeAILab/SqueezeLLM/blob/main/README.md

## Prerequisites

- Python 3.9 or higher
- CUDA 11.3+ (for GPU support)
- Conda (recommended)

## Installation Steps

### 1. Create a Conda Environment

```bash
conda create --name sqllm python=3.9 -y
conda activate sqllm
```

### 2. Clone and Install Dependencies

```bash
git clone https://github.com/SqueezeAILab/SqueezeLLM
cd SqueezeLLM
pip install -e .
cd squeezellm
python setup_cuda.py install
```

This will install:
- torch
- transformers==4.29.0
- accelerate
- sentencepiece
- tokenizers>=0.12.1
- datasets

### 3. Verify Installation

You can verify the installation by importing the squeezellm module:

```python
import squeezellm
print("SqueezeLLM installed successfully!")
```

## Dependencies

The following dependencies are automatically installed:

- **torch**: Deep learning framework for GPU computation
- **transformers==4.29.0**: Hugging Face transformers library (specific version required)
- **accelerate**: Multi-GPU training and inference utilities
- **sentencepiece**: Tokenization library
- **tokenizers>=0.12.1**: Fast tokenizer implementation
- **datasets**: Dataset loading and processing

## GPU Setup

SqueezeLLM requires CUDA for efficient quantization and inference. Ensure your GPU drivers are installed:

```bash
# Check CUDA version
nvidia-smi

# Install CUDA toolkit if needed (if not already installed with torch)
conda install cuda-toolkit -c nvidia
```

## Troubleshooting

### TransformersVersion Error

If you encounter errors related to transformers version:

```
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed...
```

This is expected. The framework requires transformers==4.29.0 for compatibility. If needed, you can downgrade:

```bash
pip install transformers==4.29.0
```

### CUDA Compilation Issues

If you encounter CUDA compilation errors during `python setup_cuda.py install`:

1. Ensure CUDA toolkit is properly installed
2. Verify your GPU supports the CUDA version
3. Check that g++ and nvcc are in your PATH

### Module Import Errors

If you get `ModuleNotFoundError` when importing squeezellm:

```bash
# Reinstall in development mode
cd SqueezeLLM
pip install -e .
cd squeezellm
python setup_cuda.py install
```

---

Generated from: https://github.com/SqueezeAILab/SqueezeLLM
