# SmoothQuant API Reference

## Core Modules

### smoothquant.smooth

Main module for applying SmoothQuant to models.

#### `smooth_lm(model, scales, alpha=0.5)`

Apply SmoothQuant smoothing to a model.

**Parameters:**
- `model` (nn.Module): Language model to smooth
- `scales` (dict): Activation scales per layer
- `alpha` (float): Smoothing factor, range [0, 1], default 0.5

**Returns:** None (modifies model in-place)

**Example:**
```python
from smoothquant.smooth import smooth_lm
smooth_lm(model, activation_scales, alpha=0.85)
```

### smoothquant.fake_quant

Provides fake (simulated) quantization functions for testing.

#### `fake_quantize_activation_per_token_asymmetric(activation, scales)`

Simulate asymmetric per-token INT8 activation quantization.

**Parameters:**
- `activation` (torch.Tensor): Activation tensor [seq_len, hidden_dim]
- `scales` (torch.Tensor): Per-token scales [seq_len]

**Returns:** Quantized activation tensor

**Example:**
```python
from smoothquant.fake_quant import fake_quantize_activation_per_token_asymmetric
quant_act = fake_quantize_activation_per_token_asymmetric(activation, scales)
```

#### `fake_quantize_weight_per_channel_symmetric(weight, scales)`

Simulate symmetric per-channel INT8 weight quantization.

**Parameters:**
- `weight` (torch.Tensor): Weight tensor [out_features, in_features]
- `scales` (torch.Tensor): Per-channel scales [out_features]

**Returns:** Quantized weight tensor

### smoothquant.opt

Quantized OPT model implementation.

#### `Int8OPTForCausalLM`

OPT model with INT8 quantization.

**Methods:**
- `from_pretrained(model_id)`: Load pre-quantized model from Hugging Face
- `generate(**kwargs)`: Generate text (standard Transformers API)
- `forward(input_ids, attention_mask, ...)`: Standard forward pass

**Example:**
```python
from smoothquant.opt import Int8OPTForCausalLM
model = Int8OPTForCausalLM.from_pretrained("mit-han-lab/opt-30b-smoothquant")
output = model.generate(input_ids=input_ids)
```

### smoothquant.calibration

Calibration and scale computation.

#### `compute_activation_scales(model, data_loader, num_samples=512)`

Compute activation scales for quantization.

**Parameters:**
- `model` (nn.Module): Model to calibrate
- `data_loader` (DataLoader): Calibration data loader
- `num_samples` (int): Number of calibration samples

**Returns:** dict of activation scales per layer

**Example:**
```python
from smoothquant.calibration import compute_activation_scales
scales = compute_activation_scales(model, calib_loader, num_samples=512)
```

### smoothquant.ppl_eval

Perplexity evaluation for quantized models.

#### `evaluate_ppl(model, dataset, scales, alpha=0.5, smooth=True, quantize=True)`

Evaluate perplexity of quantized model.

**Parameters:**
- `model` (nn.Module): Model to evaluate
- `dataset` (str): Dataset name ('wikitext-2', 'wikitext-103', etc.)
- `scales` (dict): Activation scales
- `alpha` (float): Smoothing factor
- `smooth` (bool): Whether to apply smoothing
- `quantize` (bool): Whether to apply fake quantization

**Returns:** float (perplexity value)

## Command-line Tools

### generate_act_scales.py

Generate activation channel scales for a model.

**Usage:**
```bash
python examples/generate_act_scales.py \
    --model-name <model_id> \
    --output-path <output_file> \
    --num-samples 512 \
    --seq-len 512
```

**Arguments:**
- `--model-name`: Hugging Face model ID or local path
- `--output-path`: Where to save scales (.pt file)
- `--num-samples`: Number of calibration samples (default: 512)
- `--seq-len`: Sequence length (default: 512)
- `--dataset-path`: Path to calibration dataset
- `--per-gpu-batch-size`: Batch size per GPU (default: 8)

### export_int8_model.py

Export a model quantized with SmoothQuant.

**Usage:**
```bash
python examples/export_int8_model.py \
    --model_path <model_id> \
    --output_path <output_dir> \
    --act_scales_path <scales_file> \
    --alpha 0.85
```

**Arguments:**
- `--model_path`: Original model (Hugging Face ID or path)
- `--output_path`: Output directory for quantized model
- `--act_scales_path`: Path to activation scales file
- `--alpha`: Smoothing factor (default: 0.5)

### ppl_eval.py

Evaluate perplexity of quantized models.

**Usage:**
```bash
python smoothquant/ppl_eval.py \
    --model_path <model_id> \
    --act_scales_path <scales_file> \
    --smooth \
    --alpha 0.85 \
    --quantize \
    --dataset_name wikitext \
    --dataset_config wikitext-2
```

**Arguments:**
- `--model_path`: Model to evaluate
- `--act_scales_path`: Path to activation scales
- `--smooth`: Apply smoothing (flag)
- `--alpha`: Smoothing factor
- `--quantize`: Apply fake quantization (flag)
- `--dataset_name`: Dataset for evaluation
- `--dataset_config`: Dataset configuration

## Tensor Specifications

### Activation Scales Format

Activation scales are stored as PyTorch tensors in `.pt` files.

**Structure:**
```python
scales = {
    'layer.0': torch.tensor([...]),  # Shape: [hidden_dim] or [num_heads]
    'layer.1': torch.tensor([...]),
    # ...
}
```

### Quantization Parameters

**INT8 Activation Quantization:**
- Range: [-128, 127]
- Zero-point: computed per-token
- Scale: per-token from data

**INT8 Weight Quantization:**
- Range: [-128, 127]
- Zero-point: 0 (symmetric)
- Scale: per-output-channel

## Performance Characteristics

### Computational Complexity

- Calibration: O(n*d) where n=num_samples, d=hidden_dim
- Smoothing: O(l*d) where l=num_layers
- Quantization: O(model_size)

### Memory Usage

- Original model: 100%
- After INT8 quantization: 50%
- During quantization process: 150% (temporary)

### Latency

- Typical 1.5x speedup on NVIDIA GPUs
- Varies by model size and GPU architecture
- Better results with larger batch sizes

## Error Handling

### Common Exceptions

```python
# Missing activation scales
RuntimeError: "scales not found for layer..."

# Incompatible model type
ValueError: "unsupported model architecture"

# Out of memory during calibration
RuntimeError: "CUDA out of memory"
```

## Version Compatibility

- PyTorch: >= 1.12.0
- Transformers: >= 4.36.0
- CUDA: 11.3+ recommended
- Python: 3.8+
