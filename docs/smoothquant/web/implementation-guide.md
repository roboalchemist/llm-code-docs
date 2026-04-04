# SmoothQuant Implementation Guide

## Overview

This guide covers the main workflows for using SmoothQuant to quantize Large Language Models to INT8.

## Workflow 1: Using Pre-quantized Models

The simplest approach is to use pre-quantized OPT models already available on Hugging Face.

### Load Model

```python
from smoothquant.opt import Int8OPTForCausalLM

# Load pre-quantized INT8 model
model = Int8OPTForCausalLM.from_pretrained("mit-han-lab/opt-30b-smoothquant")

# Generate text
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("facebook/opt-30b")
inputs = tokenizer("Hello world", return_tensors="pt")
outputs = model.generate(**inputs)
```

### Available Models

- `mit-han-lab/opt-125m-smoothquant`
- `mit-han-lab/opt-1.3b-smoothquant`
- `mit-han-lab/opt-2.7b-smoothquant`
- `mit-han-lab/opt-6.7b-smoothquant`
- `mit-han-lab/opt-13b-smoothquant`
- `mit-han-lab/opt-30b-smoothquant`
- `mit-han-lab/opt-66b-smoothquant`

## Workflow 2: Quantize Your Own Model

To quantize a model not in the pre-quantized collection:

### Step 1: Generate Activation Scales

```bash
python examples/generate_act_scales.py \
    --model-name meta-llama/Llama-2-7b \
    --output-path llama2-7b-scales.pt \
    --num-samples 512 \
    --seq-len 512 \
    --dataset-path data/calibration_data
```

Parameters:
- `--model-name`: Hugging Face model ID or local path
- `--output-path`: Where to save activation scales
- `--num-samples`: Number of calibration samples (512 recommended)
- `--seq-len`: Sequence length (512 typical)
- `--dataset-path`: Path to calibration dataset (uses Pile by default)

### Step 2: Export Quantized Model

```bash
python examples/export_int8_model.py \
    --model_path meta-llama/Llama-2-7b \
    --output_path ./llama2-7b-smoothquant \
    --act_scales_path llama2-7b-scales.pt \
    --alpha 0.85
```

Parameters:
- `--model_path`: Original model (Hugging Face ID or path)
- `--output_path`: Where to save quantized model
- `--act_scales_path`: Path to activation scales from Step 1
- `--alpha`: Smoothing factor (0.8-0.9 recommended)

### Step 3: Use Quantized Model

```python
from smoothquant.opt import Int8OPTForCausalLM
from transformers import AutoTokenizer

model = Int8OPTForCausalLM.from_pretrained("./llama2-7b-smoothquant")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b")

inputs = tokenizer("Explain quantum computing", return_tensors="pt")
outputs = model.generate(**inputs, max_length=256)
print(tokenizer.decode(outputs[0]))
```

## Workflow 3: Evaluate Quantized Models

Evaluate perplexity of quantized models:

```bash
python smoothquant/ppl_eval.py \
    --model_path meta-llama/Llama-2-7b \
    --act_scales_path llama2-7b-scales.pt \
    --smooth \
    --alpha 0.85 \
    --quantize \
    --dataset_name wikitext \
    --dataset_config wikitext-2
```

## Smoothing Algorithm Details

### Mathematical Foundation

SmoothQuant applies per-channel scaling transformation:

```
X_smoothed = X * S
W_smoothed = W * S^(-1)
```

Where:
- `X` = activation tensor
- `W` = weight tensor
- `S` = per-channel scaling matrix

### Alpha Parameter

The alpha parameter controls the smoothing ratio:

```
S_i = max(|X_i|)^(1-α) * 2^α
```

- `α = 0.5`: Balanced smoothing (default starting point)
- `α = 0.8-0.9`: More smoothing toward weights (often better for LLMs)
- `α = 1.0`: All difficulty in weights

### Tuning Alpha

For best results with your model:

1. Start with α = 0.85
2. If accuracy drops > 1%: increase α to 0.9
3. If no improvement: decrease α to 0.8

## Performance Optimization

### For Single GPU

Fake quantization provides accurate PPL estimation without special hardware:

```python
from smoothquant.fake_quant import fake_quantize_activation_per_token_asymmetric
import torch

# Simulate INT8 inference on FP16 model
quantized_output = fake_quantize_activation_per_token_asymmetric(
    activation, 
    scales
)
```

### For Multi-GPU Inference

Use FasterTransformer for production:

```bash
# Compile FasterTransformer with INT8 support
git clone https://github.com/NVIDIA/FasterTransformer.git
cd FasterTransformer
# Build with -DENABLE_INT8=ON flag
```

Then use quantized model with FasterTransformer backend for 1.56x speedup.

### Memory Savings

- FP16 model: 1x (baseline)
- INT8 model: 0.5x (50% reduction)
- With KV cache optimization: Additional 0.5x for attention

## Pre-computed Activation Scales

Pre-computed scales available at: https://huggingface.co/mit-han-lab/smoothquant-scales

This includes scales for:
- OPT (125M - 66B)
- BLOOM
- Llama-1/2/3
- Falcon
- Mistral
- Mixtral

Use with your model:

```python
import torch

# Load pre-computed scales
scales = torch.load("path/to/scales.pt")

# Apply to your model
from smoothquant.smooth import smooth_lm
smooth_lm(model, scales, alpha=0.85)
```

## Troubleshooting

### Issue: Low accuracy after quantization

**Solution**: Try different alpha values
```bash
for alpha in 0.75 0.80 0.85 0.90; do
    python smoothquant/ppl_eval.py \
        --model_path <model> \
        --act_scales_path <scales> \
        --alpha $alpha \
        --smooth \
        --quantize
done
```

### Issue: CUDA out of memory

**Solution**: Reduce batch size during calibration
```bash
python examples/generate_act_scales.py \
    --model-name <model> \
    --num-samples 256 \
    --per-gpu-batch-size 1
```

### Issue: torch-int not available

**Solution**: Install required dependencies
```bash
pip install torch-int
# If build fails, ensure CUDA toolkit matches your PyTorch installation
```

## Integration Examples

### With Hugging Face Transformers

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load and quantize
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b")

# Apply smoothing (see examples/export_int8_model.py for full implementation)
from smoothquant.smooth import smooth_lm
smooth_lm(model, scales, alpha=0.85)
```

### With vLLM

SmoothQuant quantized models compatible with vLLM for efficient serving:

```bash
python -m vllm.entrypoints.openai.api_server \
    --model mit-han-lab/opt-30b-smoothquant \
    --quantization smoothquant
```

### With TensorRT-LLM

For production inference with maximum performance:

```bash
# Build with SmoothQuant support
trtllm-build \
    --checkpoint_dir ./quantized_model \
    --output_dir ./trt_engine \
    --quantization smoothquant
```

## References

- Paper: https://arxiv.org/abs/2211.10438
- GitHub: https://github.com/mit-han-lab/smoothquant
- Hugging Face: https://huggingface.co/mit-han-lab
