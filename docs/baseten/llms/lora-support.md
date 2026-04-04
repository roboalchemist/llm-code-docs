# Source: https://docs.baseten.co/engines/engine-builder-llm/lora-support.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# LoRA support

> Multi-LoRA adapters for Engine-Builder-LLM engine

Engine-Builder-LLM supports multi-LoRA deployments with runtime adapter switching. Share base model weights across fine-tuned variants and switch adapters without redeployment.

## Overview

Deploy multiple LoRA adapters on a single base model and switch between them at inference time. The engine shares base model weights across all adapters for memory efficiency.

## Configuration

### Basic LoRA configuration

```yaml  theme={"system"}
model_name: Qwen2.5-Coder-LoRA
resources:
  accelerator: H100
  cpu: '2'
  memory: 20Gi
  use_gpu: true
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen2.5-Coder-1.5B-Instruct"
      revision: "2e1fd397ee46e1388853d2af2c993145b0f1098a"
    lora_adapters:
      lora1:
        repo: "ai-blond/Qwen-Qwen2.5-Coder-1.5B-Instruct-lora"
        revision: "9cde18d8ed964b0519fb481cca6acd936b2ca811"
        source: "HF"
    max_lora_rank: 16
    plugin_configuration:
      lora_plugin: "float16"
  runtime:
    served_model_name: "Qwen2.5-Coder-base"
```

## Limitations

* **Same rank and same modules**: For optimal performance and stability, the LoRA adapters for one deployment should be uniform. All target modules must be the same.
* **Build time availability**: The engine relies on numpy-style weights. These need to be pre-converted during deployment and distributed to each replica. For Engine-Builder-LLM, these repos must be known ahead of time.
* **Inference performance**: If you're using only one LoRA adapter, merging the adapter into the base weights provides better performance. Additional LoRA adapters add complexity to kernel selection and fundamentally increase flops.

## LoRA adapter configuration

### Adapter repository structure

LoRA adapters must follow the standard HuggingFace repository structure:

```
adapter-repo/
├── adapter_config.json
├── adapter_model.safetensors
└── README.md
```

### Required files

**adapter\_config.json**

```yaml  theme={"system"}
  # same base model for all configs 
  "base_model_name_or_path": "Qwen/Qwen2.5-Coder-1.5B-Instruct", 
  # same target modules among all lora adapters 
  "target_modules": [
    "attn_q",
    "attn_k", 
    "attn_v",
    "attn_dense",
    "mlp_h_to_4h",
    "mlp_4h_to_h",
    "mlp_gate"
  ],
  # same rank among all lora adapters
  "r": 16
```

**model.lora\_weights.npy**

* NumPy array containing LoRA weight matrices
* Shape: `(num_layers, rank, hidden_size, hidden_size)`
* Must match the target modules specified in config

**model.lora\_config.npy**

* NumPy array containing LoRA configuration
* Includes scaling factors and other parameters
* Must match the adapter\_config.json specifications

## Build configuration options

### `lora_adapters`

Dictionary of LoRA adapters to load during build:

```yaml  theme={"system"}
lora_adapters:
  adapter_name:
    repo: "username/model-name"
    revision: "main"
    source: "HF"  # or "GCS", "S3", "AZURE"
```

### `max_lora_rank`

Maximum LoRA rank for all adapters.

```yaml  theme={"system"}
max_lora_rank: 16  # Default: 8
```

**Range**: 1 to 64, must be power of 2
**Recommended**: Set to exactly the rank `r` that you use for all adapters.

### `plugin_configuration`

LoRA plugin configuration:

```yaml  theme={"system"}
plugin_configuration:
  lora_plugin: "float16" 
```

**Options:**

* `float16`: Reduced memory usage, slight accuracy impact.
* `float32`: Higher precision, much slower inference.

## Engine inference configuration

The model parameter in OpenAI-format requests selects which adapter to use. For the above example, valid model names are `Qwen2.5-Coder-base` or `lora1`.

This lets you select different adapters at runtime through the OpenAI client.

## Further reading

* [Engine-Builder-LLM overview](/engines/engine-builder-llm/overview): Main engine documentation.
* [Engine-Builder-LLM configuration](/engines/engine-builder-llm/engine-builder-config): Complete reference config.
* [Custom engine builder](/engines/engine-builder-llm/custom-engine-builder): Custom model.py implementation.
* [Quantization guide](/engines/performance-concepts/quantization-guide): Performance optimization.
