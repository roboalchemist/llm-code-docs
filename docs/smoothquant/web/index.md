# SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models

**Source:** https://github.com/mit-han-lab/smoothquant

## Overview

SmoothQuant is a training-free, accuracy-preserving post-training quantization (PTQ) solution for Large Language Models that enables INT8 activation and weight quantization (W8A8). Developed by MIT and NVIDIA researchers, it allows efficient inference on LLMs up to 175B parameters.

### Key Features

- **Training-Free**: No fine-tuning required
- **Accuracy-Preserving**: Negligible loss in model accuracy
- **W8A8 Quantization**: Both weights and activations quantized to INT8
- **Hardware Efficient**: 1.56x speedup and 2x memory reduction
- **General Purpose**: Works with OPT, BLOOM, GLM, LLaMA, Falcon, Mistral, Mixtral models

### Technical Innovation

SmoothQuant migrates quantization difficulty from activations to weights through mathematically equivalent transformations, smoothing out activation outliers to make both weights and activations easy to quantize.

### Integration Points

- NVIDIA TensorRT-LLM (INT8 W8A8 support)
- Amazon SageMaker (LLM inference optimization)
- Intel Neural-Compressor (quantization toolkit)
- Microsoft ONNX Runtime (inference examples)
- AMD Instinct MI300X (INT8 GEMM via Composable Kernel)

## Performance Results

### Supported Models with W8A8 Quantization

| Model | Method | PPL | Alpha |
|-------|--------|-----|-------|
| Llama-2-7B | FP16 | 5.474 | - |
| | SQ W8A8 | 5.515 | 0.85 |
| Llama-2-13B | FP16 | 4.950 | - |
| | SQ W8A8 | 4.929 | 0.85 |
| Llama-2-70B | FP16 | 3.320 | - |
| | SQ W8A8 | 3.359 | 0.9 |
| Llama-3-8B | FP16 | 6.138 | - |
| | SQ W8A8 | 6.258 | 0.85 |
| Mistral-7B | FP16 | 5.253 | - |
| | SQ W8A8 | 5.277 | 0.8 |
| Mixtral-8x7B | FP16 | 3.842 | - |
| | SQ W8A8 | 3.893 | 0.8 |
| Falcon-7B | FP16 | 6.590 | - |
| | SQ W8A8 | 6.629 | 0.6 |
| Falcon-40B | FP16 | 5.228 | - |
| | SQ W8A8 | 5.255 | 0.7 |

## Installation

```bash
conda create -n smoothquant python=3.8
conda activate smoothquant
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
pip install transformers==4.36.0 accelerate datasets zstandard
python setup.py install
```

## Quick Start

### Load Pre-quantized INT8 Model

```python
from smoothquant.opt import Int8OPTForCausalLM
model = Int8OPTForCausalLM.from_pretrained("mit-han-lab/opt-30b-smoothquant")
```

Available pre-quantized models: `opt-125m`, `opt-1.3b`, `opt-2.7b`, `opt-6.7b`, `opt-13b`, `opt-30b`, `opt-66b`

### Generate Activation Scales

```bash
python examples/generate_act_scales.py \
    --model-name <model_name_or_path> \
    --output-path <output_act_scales_file_path> \
    --num-samples <num_samples> \
    --seq-len <sequence_length> \
    --dataset-path <path_to_calibration_dataset>
```

### Smooth and Quantize Models

```bash
python examples/export_int8_model.py \
    --model_path <model_path> \
    --output_path <output_path> \
    --act_scales_path <act_scales_file>
```

### Evaluate Perplexity

```bash
python smoothquant/ppl_eval.py \
    --model_path <model_name_or_path> \
    --act_scales_path <act_scales_file_path> \
    --smooth \
    --alpha <alpha_value> \
    --quantize
```

## Core Components

### Main Modules

- **`smoothquant/smooth.py`**: Core smoothing algorithm implementation
- **`smoothquant/fake_quant.py`**: FP16 fake quantization simulation
- **`smoothquant/opt.py`**: Quantized OPT model class with INT8 linear layers
- **`smoothquant/calibration.py`**: Calibration and scale computation
- **`smoothquant/ppl_eval.py`**: Perplexity evaluation for quantized models

### Examples

- **`examples/smoothquant_opt_demo.ipynb`**: OPT-13B W8A8 fake quantization demo
- **`examples/smoothquant_opt_real_int8_demo.ipynb`**: OPT-30B real INT8 inference on A100
- **`examples/smoothquant_llama_demo.ipynb`**: LLaMA model quantization demo
- **`examples/generate_act_scales.py`**: Script to compute activation channel scales
- **`examples/export_int8_model.py`**: Export quantized INT8 models
- **`examples/ppl_eval.sh`**: Batch evaluation script for multiple models

## Hardware Requirements

### For Real INT8 Inference
- Requires NVIDIA GPU with INT8 support (requires torch-int library)
- CUTLASS INT8 GEMM kernels wrapped as PyTorch modules

### For Large Models (Multi-GPU)
- Recommended: Use FasterTransformer backend for distributed inference
- OPT-175B: 4 GPUs with INT8 vs 8 GPUs with FP16

## Activation Channel Scales

Pre-computed activation scales available for:
- OPT (all sizes)
- BLOOM
- Llama (1/2/3)
- Falcon
- Mistral
- Mixtral

Scales computed with 512 random sentences from Pile validation set.

## Research Paper

**SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models**
- **Authors**: Guangxuan Xiao, Ji Lin, Mickaël Seznec, Hao Wu, Julien Demouth, Song Han
- **Conference**: ICML 2023
- **Paper**: https://arxiv.org/abs/2211.10438
- **Slides**: See assets/SmoothQuant.pdf in repository

## Citation

```bibtex
@InProceedings{xiao2023smoothquant,
    title = {{S}mooth{Q}uant: Accurate and Efficient Post-Training Quantization for Large Language Models},
    author = {Xiao, Guangxuan and Lin, Ji and Seznec, Mickael and Wu, Hao and Demouth, Julien and Han, Song},
    booktitle = {Proceedings of the 40th International Conference on Machine Learning},
    year = {2023}
}
```

## References

- **GitHub Repository**: https://github.com/mit-han-lab/smoothquant
- **Hugging Face Models**: https://huggingface.co/mit-han-lab/
- **Paper**: https://arxiv.org/abs/2211.10438
- **torch-int**: https://github.com/Guangxuan-Xiao/torch-int
- **CUTLASS**: https://github.com/NVIDIA/cutlass
- **FasterTransformer**: https://github.com/NVIDIA/FasterTransformer
