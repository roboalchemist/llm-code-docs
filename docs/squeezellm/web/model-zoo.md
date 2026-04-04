# SqueezeLLM Model Zoo

## Source: https://github.com/SqueezeAILab/SqueezeLLM/blob/main/README.md

All pre-quantized models are available from the Squeeze AI Lab on Hugging Face Hub:

https://huggingface.co/squeeze-ai-lab

## Model Naming Convention

- `sq-{base-model}-{size}-w{bits}-s{sparsity}`: Standard naming format
- `sq-llama-7b-w3-s0`: LLaMA-7B, 3-bit, 0% sparsity (dense-only)
- `sq-llama-7b-w4-s45`: LLaMA-7B, 4-bit, 0.45% sparsity

## LLaMA (v1)

Supported sizes: 7B, 13B, 30B, 65B

| Model | 3-bit (Dense) | 3-bit (0.05% S) | 3-bit (0.45% S) | 4-bit (Dense) | 4-bit (0.05% S) | 4-bit (0.45% S) |
|-------|---|---|---|---|---|---|
| **LLaMA-7B** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **LLaMA-13B** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **LLaMA-30B** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **LLaMA-65B** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

**Note**: LLaMA v1 requires base model checkpoint

## LLaMA-2

Supported sizes: 7B, 13B

| Model | 3-bit (Dense) | 4-bit (Dense) |
|-------|---|---|
| **LLaMA-2-7B** | ✓ | ✓ |
| **LLaMA-2-13B** | ✓ | ✓ |

**Note**: Includes Hugging Face compatible configs

## Mistral

Supported models: Mistral-7B (base and instruct)

| Model | 3-bit (Dense) | 4-bit (Dense) |
|-------|---|---|
| **Mistral-7B** | ✓ | ✓ |
| **Mistral-7B-Instruct** | ✓ | ✓ |

**Added**: November 2024

## Vicuna (v1.1)

Supported sizes: 7B, 13B

| Model | 3-bit (Dense) | 3-bit (0.45% S) | 4-bit (Dense) | 4-bit (0.45% S) |
|-------|---|---|---|---|
| **Vicuna-7B** | ✓ | ✓ | ✓ | ✓ |
| **Vicuna-13B** | ✓ | ✓ | ✓ | ✓ |

## Vicuna (v1.3)

Supported sizes: 7B, 13B, 30B (30B coming soon)

| Model | 3-bit (Dense) | 4-bit (Dense) |
|-------|---|---|
| **Vicuna-7B-v1.3** | ✓ | ✓ |
| **Vicuna-13B-v1.3** | ✓ | ✓ |
| **Vicuna-30B-v1.3** | Coming | Coming |

See [FastChat docs](https://github.com/lm-sys/FastChat/blob/main/docs/vicuna_weights_version.md) for v1.1 vs v1.3 differences.

## XGen (8K Sequence Length)

Based on [Salesforce XGen-7B](https://blog.salesforceairesearch.com/xgen/)

Models: XGen-7B-8k-Base, XGen-7B-8k-Inst

| Model | 3-bit (Dense) | 3-bit (0.45% S) | 4-bit (Dense) | 4-bit (0.45% S) |
|-------|---|---|---|---|
| **XGen-7B-8k-Base** | ✓ | ✓ | ✓ | ✓ |
| **XGen-7B-8k-Inst** | ✓ | ✓ | ✓ | ✓ |

**Key Feature**: 8K context length support

## OPT

Supported sizes: 1.3B, 2.7B, 6.7B, 13B, 30B

| Model | 3-bit (Dense) | 3-bit (0.45% S) | 4-bit (Dense) | 4-bit (0.45% S) |
|-------|---|---|---|---|
| **OPT-1.3B** | ✓ | ✓ | ✓ | ✓ |
| **OPT-2.7B** | ✓ | ✓ | ✓ | ✓ |
| **OPT-6.7B** | ✓ | ✓ | ✓ | ✓ |
| **OPT-13B** | ✓ | ✓ | ✓ | ✓ |
| **OPT-30B** | ✓ | ✓ | ✓ | ✓ |

## Download Instructions

### Download from Hugging Face Hub

```python
from huggingface_hub import hf_hub_download

# Example: Download LLaMA-7B 3-bit dense-only model
model_name = "squeeze-ai-lab/sq-llama-7b-w3-s0"
checkpoint = hf_hub_download(repo_id=model_name, filename="sq-llama-7b-w3-s0.pt")
print(f"Downloaded to: {checkpoint}")
```

Or via wget:

```bash
wget https://huggingface.co/squeeze-ai-lab/sq-llama-7b-w3-s0/resolve/main/sq-llama-7b-w3-s0.pt
```

### Manual Download

Browse and download directly from:
https://huggingface.co/squeeze-ai-lab

## Loading and Using Models

See [Quick Start Guide](quickstart.md) for inference examples.

For model benchmarking and evaluation:

```bash
CUDA_VISIBLE_DEVICES=0 python llama.py {model_path} c4 --wbits 3 --load sq-llama-7b-w3-s0.pt --eval
```

## Model Performance

Approximate performance metrics (from paper):

### 3-bit Dense-Only Quantization
- LLaMA-7B: ~2-3% accuracy drop
- Vicuna-7B: ~1-2% accuracy drop
- Memory savings: ~75%

### 4-bit Dense-Only Quantization
- LLaMA-7B: <1% accuracy drop
- Vicuna-7B: <0.5% accuracy drop
- Memory savings: ~62%

### 4-bit Dense-and-Sparse (0.45% + 0.05%)
- LLaMA-7B: <0.5% accuracy drop (often better!)
- Vicuna-7B: Minimal accuracy drop
- Memory savings: ~60% with minimal accuracy loss

## Integration with vLLM

SqueezeLLM models are officially supported in [vLLM](https://github.com/vllm-project/vllm) for efficient serving.

## Citation

If you use SqueezeLLM models, please cite:

```bibtex
@article{kim2023squeezellm,
  title={SqueezeLLM: Dense-and-Sparse Quantization},
  author={Kim, Sehoon and Hooper, Coleman and Gholami, Amir and Dong, Zhen and Li, Xiuyu and Shen, Sheng and Mahoney, Michael and Keutzer, Kurt},
  journal={arXiv},
  year={2023}
}
```

---

Generated from: https://github.com/SqueezeAILab/SqueezeLLM
