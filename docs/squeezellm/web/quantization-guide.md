# From-Scratch Quantization Guide

## Source: https://github.com/SqueezeAILab/SqueezeLLM/blob/main/quantization/README.md

This guide covers how to quantize custom models using SqueezeLLM from scratch.

## Overview

SqueezeLLM quantization involves 4 main steps:

1. **Compute gradients** (Fisher-based sensitivity scores)
2. **Chunk model weights and gradients** (layer granularity)
3. **Generate outlier configuration** (optional, for Dense-and-Sparse)
4. **K-means clustering** (generate non-uniform quantization LUT)
5. **Packing** (save quantized model)

## Prerequisites

### Base Requirements

In addition to SqueezeLLM installation dependencies:

```bash
pip install scikit-learn==1.3.1
```

### Model Checkpoint

You must have your own LLaMA Hugging Face checkpoint saved locally at `[MODEL_PATH]`.

## Step 1: Compute Gradients (Fisher-based Sensitivity Score)

SqueezeLLM employs the **Fisher Information matrix** as a sensitivity metric to identify which weights are most critical to model performance.

### Using the Separate Framework

Use the dedicated gradient computation framework:

https://github.com/kssteven418/SqueezeLLM-gradients

This framework will:
- Compute gradient squares for your target model
- Output in the same format as the original Hugging Face checkpoint
- Replace weight values with gradient square values

### Running Gradient Computation

Follow the instructions in the SqueezeLLM-gradients repository:

```bash
git clone https://github.com/kssteven418/SqueezeLLM-gradients
cd SqueezeLLM-gradients
# Follow README for gradient computation
```

This produces: `[GRADIENT_PATH]` - gradient checkpoint with Fisher scores

## Step 2: Chunk Model Weights and Gradients

Both model and gradient checkpoints must be chunked at layer granularity to reduce memory overhead during loading.

### Chunk Model Weights

```bash
python chunk_models.py --model [MODEL_PATH] --output [MODEL_CHUNKS_PATH] --model_type llama
```

### Chunk Gradient Checkpoint

```bash
python chunk_models.py --model [GRADIENT_PATH] --output [GRADIENT_CHUNKS_PATH] --model_type llama
```

### Output

This produces:
- `[MODEL_CHUNKS_PATH]`: Chunked model weights at layer granularity
- `[GRADIENT_CHUNKS_PATH]`: Chunked gradients at layer granularity

These chunked formats reduce loading overhead significantly.

## Step 3: Outlier Configuration Generation (Optional)

This step is **optional** and only needed for **Dense-and-Sparse (D+S) quantization**.

### Purpose

Generates a configuration file defining thresholds for identifying outlier values in weights.

### Run Outlier Configuration

```bash
python generate_outlier_config.py --model [MODEL_CHUNKS_PATH] --range [RANGE] --output [OUTLIERS_CONFIG_PATH]
```

### Arguments

- `--model`: Path to chunked model weights from Step 2
- `--range`: Threshold multiplier for T_min and T_max (see paper Section 4.2)
  - Larger values = fewer outliers
  - Recommended starting range: **1.5-2.0**
- `--output`: Output directory (saves as `[OUTLIERS_CONFIG_PATH]/outlier_config_o{percentage}.json`)

### Output

Configuration file: `[OUTLIERS_CONFIG_PATH]/outlier_config_o0.45.json` (example for 0.45% outliers)

You will need to fine-tune `--range` to achieve desired outlier percentage.

## Step 4: K-means Clustering (Non-uniform Quantization LUT)

Performs K-means clustering to generate the non-uniform quantization look-up table (LUT).

### Dense-Only Quantization

```bash
python nuq.py --bit 4 --model_type llama --model [MODEL_CHUNKS_PATH] --gradient [GRADIENT_CHUNKS_PATH] --output [LUT_PATH]
```

### Dense-and-Sparse Quantization

If using D+S quantization with 0.45% outliers and 0.05% sensitive values:

```bash
python nuq.py --bit 4 --model_type llama --model [MODEL_CHUNKS_PATH] --gradient [GRADIENT_CHUNKS_PATH] --output [LUT_PATH] --outlier_config [OUTLIERS_CONFIG_PATH]/outlier_config_o0.45.json --sensitivity 0.05
```

### Arguments

- `--bit`: Quantization bitwidth (3 or 4)
- `--model`: Path to chunked model weights
- `--gradient`: Path to chunked gradients
- `--output`: Output directory for LUT
- `--range`: (Optional) Quantize specific layer range, e.g., `0,10` for layers 0-9
- `--outlier_config`: (D+S only) Path to outlier config from Step 3
- `--sensitivity`: (D+S only) Percentage of sensitive values to extract (e.g., 0.05%)

### Performance Note

This step is **highly CPU-intensive**. Recommended to run on:
- Multi-core CPU systems
- Strong CPU performance
- Sufficient RAM for model loading

### Output

LUT entries saved in: `[LUT_PATH]/lut`

## Step 5: Packing

Saves the quantized model in packed format using the LUT from Step 4.

### Dense-Only Packing

```bash
python pack.py --model [MODEL_PATH] --wbits 4 --folder [LUT_PATH] --save [PACKED_CKPT_PATH]
```

### Dense-and-Sparse Packing

For D+S quantization (with sparse components):

```bash
python pack.py --model [MODEL_PATH] --wbits 4 --folder [LUT_PATH] --save [PACKED_CKPT_PATH] --include_sparse --balance
```

### Arguments

- `--model`: Original model checkpoint path
- `--wbits`: Quantization bitwidth (should match Step 4)
- `--folder`: Path to LUT directory from Step 4
- `--save`: Output path for packed checkpoint
- `--include_sparse`: (D+S only) Include sparse components
- `--balance`: (D+S only) Balance sparse weight distribution

### Output

Packed checkpoint: `[PACKED_CKPT_PATH]` - Ready for immediate use in inference!

## Complete Example Workflow

### Dense-Only Quantization (3-bit)

```bash
# 1. Prepare gradient checkpoint using SqueezeLLM-gradients
# (produces [GRADIENT_PATH])

# 2. Chunk models
python chunk_models.py --model /path/to/llama-7b --output ./llama7b_chunks --model_type llama
python chunk_models.py --model /path/to/gradients --output ./llama7b_grad_chunks --model_type llama

# 3. K-means clustering
python nuq.py --bit 3 --model_type llama     --model ./llama7b_chunks     --gradient ./llama7b_grad_chunks     --output ./llama7b_lut

# 4. Pack model
python pack.py --model /path/to/llama-7b     --wbits 3     --folder ./llama7b_lut     --save ./sq-llama-7b-w3-s0.pt
```

### Dense-and-Sparse Quantization (4-bit, 0.45% outliers, 0.05% sensitive)

```bash
# 1-2. Same as above...

# 3. Generate outlier config
python generate_outlier_config.py     --model ./llama7b_chunks     --range 1.8     --output ./llama7b_outliers

# 4. K-means clustering with outliers
python nuq.py --bit 4 --model_type llama     --model ./llama7b_chunks     --gradient ./llama7b_grad_chunks     --output ./llama7b_lut_ds     --outlier_config ./llama7b_outliers/outlier_config_o0.45.json     --sensitivity 0.05

# 5. Pack with sparse components
python pack.py --model /path/to/llama-7b     --wbits 4     --folder ./llama7b_lut_ds     --save ./sq-llama-7b-w4-s45.pt     --include_sparse     --balance
```

## Supported Model Types

- `llama`: LLaMA (all versions)
- `llama2`: LLaMA-2
- `mistral`: Mistral
- `vicuna`: Vicuna
- `xgen`: XGen
- `opt`: OPT

## Key Concepts

### Fisher Information Matrix

Measures the sensitivity of model outputs to changes in weights. Weights with high Fisher scores are more critical to model performance.

### Non-Uniform Quantization

Instead of uniform quantization (fixed step sizes), SqueezeLLM uses K-means to find optimal per-layer quantization levels based on Fisher sensitivity.

### Dense-and-Sparse Quantization

Splits weights into:
- **Dense**: Aggressively quantized (3-4 bits)
- **Sparse**: Full precision, containing outliers and sensitive values (~0.45% + 0.05%)

This achieves high compression while maintaining accuracy.

## Performance Expectations

- **3-bit Dense-only**: ~1-2% accuracy drop on benchmarks
- **4-bit Dense-only**: <1% accuracy drop
- **4-bit D+S (0.45% + 0.05%)**: ~0% accuracy drop vs. FP16

See the [research paper](https://arxiv.org/abs/2306.07629) for detailed results.

---

Generated from: https://github.com/SqueezeAILab/SqueezeLLM/blob/main/quantization/README.md
