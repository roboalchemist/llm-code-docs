# Source: https://docs.baseten.co/engines/bis-llm/bis-llm-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Reference Config (BIS-LLM)

> Complete reference config for V2 inference stack and MoE models

This reference provides complete configuration options for BIS-LLM (Baseten Inference Stack V2) engine. BIS-LLM uses the V2 inference stack with simplified configuration and enhanced features for MoE models and advanced use cases.

## Configuration structure

```yaml  theme={"system"}
trt_llm:
  inference_stack: v2  # Always v2 for BIS-LLM
  build:
    checkpoint_repository: {...}
    quantization_type: no_quant | fp8 | fp4
    quantization_config: {...}
    num_builder_gpus: 1
    skip_build_result: false
  runtime:
    max_seq_len: 32768
    max_batch_size: 256
    max_num_tokens: 8192
    tensor_parallel_size: 1
    enable_chunked_prefill: true
    served_model_name: "model-name"
    patch_kwargs: {...}
```

## Build configuration

### `checkpoint_repository`

Specifies where to find the model checkpoint. Same structure as V1 but with V2-specific optimizations.

**Structure:**

```yaml  theme={"system"}
checkpoint_repository:
  source: HF | GCS | S3 | AZURE | REMOTE_URL | BASETEN_TRAINING
  repo: "model-repository-name"
  revision: main  # Optional, only for HF
  runtime_secret_name: hf_access_token  # Optional, for private repos
```

For detailed configuration options including training checkpoints and cloud storage setup, see [Deploy training and S3 checkpoints](/engines/performance-concepts/deployment-from-training-and-s3).

### `quantization_type`

Quantization options for V2 inference stack (simplified from V1):

**Options:**

* `no_quant`: precision of the repo. This can be fp16 / bf16. Unique to BIS-LLM is that we also do support quantized checkpoints from nvidia-modelopt libraries.
* `fp8`: FP8 weights + 16-bit KV cache
* `fp4`: FP4 weights + 16-bit KV cache (B200 only)
* `fp4_mlp_only`: FP4 MLP layers only + 16-bit KV cache

For detailed quantization guidance including hardware requirements, calibration strategies, and model-specific recommendations, see [Quantization Guide](/engines/performance-concepts/quantization-guide).

### `quantization_config`

Configuration for post-training quantization calibration:

**Structure:**

```yaml  theme={"system"}
quantization_config:
  calib_size: 1024
  calib_dataset: "cnn_dailymail"
  calib_max_seq_length: 2048
```

### `num_builder_gpus`

Number of GPUs to use during the build process.

**Default:** `1` (auto-detected from resources)\
**Range:** 1 to 8

**Example:**

```yaml  theme={"system"}
build:
  num_builder_gpus: 4  # For large models or complex quantization
```

### `skip_build_result`

Skip the engine build step and use a pre-built model, that does not require any quantization.

**Default:** `false`\
**Use case:** When you have a pre-built engine from model cache

**Example:**

```yaml  theme={"system"}
build:
  skip_build_result: true
```

## Engine configuration

### `max_seq_len`

Maximum sequence length (context) for single requests.

**Default:** `32768` (64K)\
**Range:** 1 to 1048576

**Example:**

```yaml  theme={"system"}
runtime:
  max_seq_len: 131072  # 128K context
```

### `max_batch_size`

Maximum number of input sequences processed concurrently.

**Default:** `256`\
**Range:** 1 to 2048

**Example:**

```yaml  theme={"system"}
runtime:
  max_batch_size: 128  # Lower for better latency
```

### `max_num_tokens`

Maximum number of batched input tokens after padding removal.

**Default:** `8192`\
**Range:** 64 to 131072

**Example:**

```yaml  theme={"system"}
runtime:
  max_num_tokens: 16384  # Higher for better throughput
```

### `tensor_parallel_size`

Number of GPUs to use for tensor parallelism.

**Default:** `1` (auto-detected from resources)\
**Range:** 1 to 8

**Example:**

```yaml  theme={"system"}
runtime:
  tensor_parallel_size: 4  # For large models
```

### `enable_chunked_prefill`

Enable chunked prefilling for long sequences.

**Default:** `true`

**Example:**

```yaml  theme={"system"}
runtime:
  enable_chunked_prefill: true
```

### `served_model_name`

Model name returned in API responses.

**Default:** `None` (uses model name from config)

**Example:**

```yaml  theme={"system"}
runtime:
   served_model_name: "gpt-oss-120b"
```

### `patch_kwargs`

Advanced configuration patches for V2 inference stack.

**Structure:**

```yaml  theme={"system"}
patch_kwargs:
  custom_setting: "value"
  advanced_config:
    nested_setting: true
```

**Note:** This is a preview feature and may change in future versions.

## Complete configuration examples

### Qwen3-30B-A3B-Instruct-2507 MoE with FP4 on B200

```yaml  theme={"system"}
model_name: Qwen3-30B-A3B-Instruct-2507-FP4
resources:
  accelerator: B200:1
  cpu: '4'
  memory: 40Gi
  use_gpu: true
trt_llm:
  inference_stack: v2
  build:
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen3-Coder-30B-A3B-Instruct"
      revision: main
    quantization_type: fp4
    quantization_config:
      calib_size: 2048
      calib_dataset: "cnn_dailymail"
      calib_max_seq_length: 4096
    num_builder_gpus: 1
  runtime:
    max_seq_len: 65536
    max_batch_size: 256
    max_num_tokens: 8192
    tensor_parallel_size: 1
    enable_chunked_prefill: true
    served_model_name: "Qwen3-30B-A3B-Instruct-2507"
```

### GPT-OSS 120B on B200:1 with no\_quant

**Note**: We have GPT-OSS much more optimized. The below example is functional, but you can sequeeze much more performance using `B200`, e.g. with Baseten's custom Eagle Heads.

```yaml  theme={"system"}
model_name: gpt-oss-120b-b200
resources:
  accelerator: B200:1
  cpu: '4'
  memory: 40Gi
  use_gpu: true
trt_llm:
  inference_stack: v2
  build:
    checkpoint_repository:
      source: HF
      repo: "openai/gpt-oss-120b"
      revision: main
      runtime_secret_name: hf_access_token
    quantization_type: no_quant
    quantization_config:
      calib_size: 1024
      calib_dataset: "cnn_dailymail"
      calib_max_seq_length: 2048
  runtime:
    max_seq_len: 131072
    max_batch_size: 256
    max_num_tokens: 16384
    tensor_parallel_size: 1
    enable_chunked_prefill: true
    served_model_name: "gpt-oss-120b"
```

### DeepSeek V3

**Note**: We have DeepSeek V3 / V3.1 / V3.2 much more optimized. The below example is functional, but you can sequeeze much more performance using `B200:4`, e.g. with MTP Heads and disaggregated serving, or data-parallel attention.

```yaml  theme={"system"}
model_name: nvidia/DeepSeek-V3.1-NVFP4
resources:
  accelerator: B200:4
  cpu: '8'
  memory: 80Gi
  use_gpu: true
trt_llm:
  inference_stack: v2
  build:
    checkpoint_repository:
      source: HF
      repo: "nvidia/DeepSeek-V3.1-NVFP4"
      revision: main
      runtime_secret_name: hf_access_token
    quantization_type: no_quant # nvidia/DeepSeek-V3.1-NVFP4 is already modelopt compatible
    quantization_config:
      calib_size: 1024
      calib_dataset: "cnn_dailymail"
      calib_max_seq_length: 2048
  runtime:
    max_seq_len: 131072
    max_batch_size: 256
    max_num_tokens: 16384
    tensor_parallel_size: 8
    enable_chunked_prefill: true
    served_model_name: "nvidia/DeepSeek-V3.1-NVFP4"
```

## V2 vs V1 configuration differences

### Simplified build configuration

**V1 build configuration:**

```yaml  theme={"system"}
trt_llm:
  build:
    base_model: decoder
    max_seq_len: 131072
    max_batch_size: 256
    max_num_tokens: 8192
    quantization_type: fp8_kv
    tensor_parallel_count: 4
    plugin_configuration: {...}
    speculator: {...}
```

**V2 build configuration:**

```yaml  theme={"system"}
trt_llm:
  inference_stack: v2
  build:
    checkpoint_repository: {...}
    quantization_type: fp8
    num_builder_gpus: 4
  runtime:
    max_seq_len: 131072
    max_batch_size: 256
    max_num_tokens: 8192
    tensor_parallel_size: 4
```

### Key differences

1. **`inference_stack`**: Explicitly set to `v2`
2. **Simplified build options**: Many V1 options moved to engine
3. **No `base_model`**: Automatically detected from checkpoint
4. **No `plugin_configuration`**: Handled automatically
5. **No `speculator`**: Lookahead decoding requires FDE involement.
6. **Tensor parallel**: Moved to engine as `tensor_parallel_size`

## Validation and troubleshooting

### Common V2 configuration errors

**Error:** `Field trt_llm.build.base_model is not allowed to be set when using v2 inference stack`

* **Cause:** Setting `base_model` in V2 configuration
* **Fix:** Remove `base_model` field, V2 detects automatically

**Error:** `Field trt_llm.build.quantization_type is not allowed to be set when using v2 inference stack`

* **Cause:** Using unsupported quantization type
* **Fix:** Use supported quantization: `no_quant`, `fp8`, `fp4`, `fp4_mlp_only`, `fp4_kv`, `fp8_kv`

**Error:** `Field trt_llm.build.speculator is not allowed to be set when using v2 inference stack`

* **Cause:** Trying to use lookahead decoding in V2
* **Fix:** Use V1 stack for lookahead decoding, or V2 without speculation or reach out to us to use V2 with speculation.

## Migration from V1

### V1 to V2 migration

**V1 configuration:**

```yaml  theme={"system"}
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen3-4B"
    max_seq_len: 32768
    max_batch_size: 256
    max_num_tokens: 8192
    quantization_type: fp8_kv
    tensor_parallel_count: 1
    plugin_configuration:
      paged_kv_cache: true
      use_paged_context_fmha: true
      use_fp8_context_fmha: true
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.9
    enable_chunked_context: true
```

**V2 configuration:**

```yaml  theme={"system"}
trt_llm:
  inference_stack: v2
  build:
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen3-4B"
    quantization_type: fp8_kv
  runtime:
    max_seq_len: 32768
    max_batch_size: 256
    max_num_tokens: 8192
    tensor_parallel_size: 1
    enable_chunked_prefill: true
```

### Migration steps

1. **Add `inference_stack: v2`**
2. **Remove `base_model`** (auto-detected)
3. \*\*Move `max_seq_len`, `max_batch_size`, `max_num_tokens` to engine
4. **Change `tensor_parallel_count` to `tensor_parallel_size`**
5. **Remove `plugin_configuration`** (handled automatically)
6. **Update quantization type** (V2 has simplified options)
7. **Remove `speculator`** (not supported in V2)

## Hardware selection

**GPU recommendations for V2:**

* **B200**: Best for FP4 quantization and next-gen performance
* **H100**: Best for FP8 quantization and production workloads
* **Multi-GPU**: Required for large MoE models (>30B parameters)

**Configuration guidelines:**

| **Model Size** | **Recommended GPU** | **Quantization** | **Tensor Parallel** |
| -------------- | ------------------- | ---------------- | ------------------- |
| `<30B` MoE     | H100:2-4            | FP8              | 2-4                 |
| 30-100B MoE    | H100:4-8            | FP8              | 4-8                 |
| 100B+ MoE      | B200:4-8            | FP4              | 4-8                 |
| Dense >30B     | H100:2-4            | FP8              | 2-4                 |

## Further reading

* [BIS-LLM overview](/engines/bis-llm/overview) - Main engine documentation
* [Advanced features documentation](/engines/bis-llm/advanced-features) - Enterprise features and capabilities
* [Structured outputs for BIS-LLM](/engines/performance-concepts/structured-outputs) - Advanced JSON schema validation
* [Examples section](/examples/overview) - Concrete deployment examples
