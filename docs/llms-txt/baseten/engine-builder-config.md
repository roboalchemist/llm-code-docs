# Source: https://docs.baseten.co/engines/engine-builder-llm/engine-builder-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Reference config (Engine-Builder-LLM)

> Complete reference config for dense text generation models

This reference covers all build and runtime options for Engine-Builder-LLM deployments. All settings use the `trt_llm` section in `config.yaml`.

## Configuration structure

```yaml  theme={"system"}
trt_llm:
  inference_stack: v1  # Always v1 for Engine-Builder-LLM
  build:
    base_model: decoder
    checkpoint_repository: {...}
    max_seq_len: 131072
    max_batch_size: 256
    max_num_tokens: 8192
    quantization_type: no_quant | fp8 | fp8_kv | fp4 | fp4_kv | fp4_mlp_only
    quantization_config: {...}
    tensor_parallel_count: 1
    plugin_configuration: {...}
    speculator: {...}  # Optional for lookahead decoding
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.9
    enable_chunked_context: true
    batch_scheduler_policy: guaranteed_no_evict
    served_model_name: "model-name"
    total_token_limit: 500000
```

## Build configuration

The `build` section configures model compilation and optimization settings.

<ParamField body="base_model" type="string" required>
  The base model architecture for your model checkpoint.

  **Options:**

  * `decoder`: For CausalLM models (Llama, Mistral, Qwen, Gemma, Phi)

  ```yaml  theme={"system"}
  build:
    base_model: decoder
  ```
</ParamField>

<ParamField body="checkpoint_repository" type="object" required>
  Specifies where to find the model checkpoint. Repository must be a valid Hugging Face model repository with the standard structure (config.json, tokenizer files, model weights).

  **Source options:**

  * `HF`: Hugging Face Hub (default)
  * `GCS`: Google Cloud Storage
  * `S3`: AWS S3
  * `AZURE`: Azure Blob Storage
  * `REMOTE_URL`: HTTP URL to tar.gz file
  * `BASETEN_TRAINING`: Baseten Training checkpoints

  For detailed configuration options including training checkpoints and cloud storage setup, see [Deploy training and S3 checkpoints](/engines/performance-concepts/deployment-from-training-and-s3).

  ```yaml  theme={"system"}
  checkpoint_repository:
    source: HF
    repo: "meta-llama/Llama-3.3-70B-Instruct"
    revision: main
    runtime_secret_name: hf_access_token
  ```
</ParamField>

<ParamField body="max_seq_len" type="number" default="max_position_embeddings from model config">
  Maximum sequence length (context) for single requests. Range: 1 to 1048576.

  ```yaml  theme={"system"}
  build:
    max_seq_len: 131072  # 128K context
  ```
</ParamField>

<ParamField body="max_batch_size" type="number" default="256">
  Maximum number of input sequences processed concurrently. Range: 1 to 2048.

  Unless lookahead decoding is enabled, this parameter has little effect on performance. Keep it at 256 for most cases.
  Recommended not to be set below 8 to keep performance dynamic for various problems.

  ```yaml  theme={"system"}
  build:
    max_batch_size: 256
  ```
</ParamField>

<ParamField body="max_num_tokens" type="number" default="8192">
  Maximum number of batched input tokens after padding removal in each batch. Range: 256 to 131072, must be multiple of 64.

  If `enable_chunked_prefill: false`, this also limits the `max_seq_len` that can be processed. Recommended: `8192` or `16384`.

  ```yaml  theme={"system"}
  build:
    max_num_tokens: 16384
  ```
</ParamField>

<ParamField body="quantization_type" type="string" default="no_quant">
  Specifies the quantization format for model weights.

  **Options:**

  * `no_quant`: `FP16`/`BF16` precision
  * `fp8`: `FP8` weights + 16-bit KV cache
  * `fp8_kv`: `FP8` weights + `FP8` KV cache
  * `fp4`: `FP4` weights + 16-bit KV cache (B200 only)
  * `fp4_kv`: `FP4` weights + `FP8` KV cache (B200 only)
  * `fp4_mlp_only`: `FP4` MLP only + 16-bit KV (B200 only)

  For detailed quantization guidance, see [Quantization Guide](/engines/performance-concepts/quantization-guide).

  ```yaml  theme={"system"}
  build:
    quantization_type: fp8_kv
  ```
</ParamField>

<ParamField body="quantization_config" type="object">
  Configuration for post-training quantization calibration.

  **Fields:**

  * `calib_size`: Size of calibration dataset (64-16384, multiple of 64). Defines how many rows of the train split with text column to take.
  * `calib_dataset`: HuggingFace dataset for calibration. Dataset must have 'text' column (str type) for samples, or 'train' split as subsection.
  * `calib_max_seq_length`: Maximum sequence length for calibration.

  ```yaml  theme={"system"}
  build:
    quantization_type: fp8
    quantization_config:
      calib_size: 1536
      calib_dataset: "cnn_dailymail"
      calib_max_seq_length: 1024
  ```
</ParamField>

<ParamField body="tensor_parallel_count" type="number" default="1">
  Number of GPUs to use for tensor parallelism. Range: 1 to 8.

  ```yaml  theme={"system"}
  build:
    tensor_parallel_count: 4  # For 70B+ models
  ```
</ParamField>

<ParamField body="plugin_configuration" type="object">
  TensorRT-LLM plugin configuration for performance optimization.

  **Fields:**

  * `paged_kv_cache`: Enable paged KV cache (recommended: true)
  * `use_paged_context_fmha`: Enable paged context FMHA (recommended: true)
  * `use_fp8_context_fmha`: Enable `FP8` context FMHA (requires `FP8_KV` quantization)

  ```yaml  theme={"system"}
  build:
    plugin_configuration:
      paged_kv_cache: true
      use_paged_context_fmha: true
      use_fp8_context_fmha: true  # For FP8_KV quantization
  ```
</ParamField>

<ParamField body="speculator" type="object">
  Configuration for speculative decoding with lookahead. For detailed configuration, see [Lookahead decoding](/engines/engine-builder-llm/lookahead-decoding).

  **Fields:**

  * `speculative_decoding_mode`: `LOOKAHEAD_DECODING` (recommended)
  * `lookahead_windows_size`: Window size for speculation (1-8)
  * `lookahead_ngram_size`: N-gram size for patterns (1-16)
  * `lookahead_verification_set_size`: Verification buffer size (1-8)
  * `enable_b10_lookahead`: Enable Baseten's lookahead algorithm

  ```yaml  theme={"system"}
  build:
    speculator:
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 3
      lookahead_ngram_size: 8
      lookahead_verification_set_size: 3
      enable_b10_lookahead: true
  ```
</ParamField>

<ParamField body="num_builder_gpus" type="number">
  Number of GPUs to use during the build job. Only set this if you encounter errors during the build job. It has no impact once the model reaches the deploying stage. If not set, equals `tensor_parallel_count`.

  ```yaml  theme={"system"}
  build:
    num_builder_gpus: 2
  ```
</ParamField>

## Runtime configuration

The `runtime` section configures inference engine behavior.

<ParamField body="kv_cache_free_gpu_mem_fraction" type="number" default="0.9">
  Fraction of GPU memory to reserve for KV cache. Range: 0.1 to 1.0.

  ```yaml  theme={"system"}
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.85
  ```
</ParamField>

<ParamField body="enable_chunked_context" type="boolean" default="true">
  Enable chunked prefilling for long sequences.

  ```yaml  theme={"system"}
  runtime:
    enable_chunked_context: true
  ```
</ParamField>

<ParamField body="batch_scheduler_policy" type="string" default="guaranteed_no_evict">
  Policy for scheduling requests in batches.

  **Options:**

  * `max_utilization`: Maximize GPU utilization (may evict requests)
  * `guaranteed_no_evict`: Guarantee request completion (recommended)

  ```yaml  theme={"system"}
  runtime:
    batch_scheduler_policy: guaranteed_no_evict
  ```
</ParamField>

<ParamField body="served_model_name" type="string">
  Model name returned in API responses.

  ```yaml  theme={"system"}
  runtime:
    served_model_name: "Llama-3.3-70B-Instruct"
  ```
</ParamField>

<ParamField body="total_token_limit" type="number" default="500000">
  Maximum number of tokens that can be scheduled at once. Range: 1 to 1000000.

  ```yaml  theme={"system"}
  runtime:
    total_token_limit: 1000000
  ```
</ParamField>

## Configuration examples

### Llama 3.3 70B

```yaml  theme={"system"}
model_name: Llama-3.3-70B-Instruct
resources:
  accelerator: H100:4
  cpu: '4'
  memory: 40Gi
  use_gpu: true
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "meta-llama/Llama-3.3-70B-Instruct"
      revision: main
      runtime_secret_name: hf_access_token
    max_seq_len: 131072
    max_batch_size: 256
    max_num_tokens: 8192
    quantization_type: fp8_kv
    tensor_parallel_count: 4
    plugin_configuration:
      paged_kv_cache: true
      use_paged_context_fmha: true
      use_fp8_context_fmha: true
    quantization_config:
      calib_size: 1024
      calib_dataset: "cnn_dailymail"
      calib_max_seq_length: 2048
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.9
    enable_chunked_context: true
    batch_scheduler_policy: guaranteed_no_evict
    served_model_name: "Llama-3.3-70B-Instruct"
```

### Qwen 2.5 32B with lookahead decoding

```yaml  theme={"system"}
model_name: Qwen-2.5-32B-Lookahead
resources:
  accelerator: H100:2
  cpu: '2'
  memory: 20Gi
  use_gpu: true
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen2.5-32B-Instruct"
      revision: main
    max_seq_len: 32768
    max_batch_size: 128
    max_num_tokens: 8192
    quantization_type: fp8_kv
    tensor_parallel_count: 2
    speculator:
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 3
      lookahead_ngram_size: 8
      lookahead_verification_set_size: 3
      enable_b10_lookahead: true
    plugin_configuration:
      paged_kv_cache: true
      use_paged_context_fmha: true
      use_fp8_context_fmha: true
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.85
    enable_chunked_context: true
    batch_scheduler_policy: guaranteed_no_evict
    served_model_name: "Qwen-2.5-32B-Instruct"
```

### Small model on L4

```yaml  theme={"system"}
model_name: Llama-3.2-3B-Instruct
resources:
  accelerator: L4
  cpu: '1'
  memory: 10Gi
  use_gpu: true
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "meta-llama/Llama-3.2-3B-Instruct"
      revision: main
    max_seq_len: 8192
    max_batch_size: 256
    max_num_tokens: 4096
    quantization_type: fp8
    tensor_parallel_count: 1
    plugin_configuration:
      paged_kv_cache: true
      use_paged_context_fmha: true
      use_fp8_context_fmha: false
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.9
    enable_chunked_context: true
    batch_scheduler_policy: guaranteed_no_evict
    served_model_name: "Llama-3.2-3B-Instruct"
```

### B200 with `FP4` quantization

```yaml  theme={"system"}
model_name: Qwen-2.5-32B-FP4
resources:
  accelerator: B200
  cpu: '2'
  memory: 20Gi
  use_gpu: true
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen2.5-32B-Instruct"
      revision: main
    max_seq_len: 32768
    max_batch_size: 256
    max_num_tokens: 8192
    quantization_type: fp4_kv
    tensor_parallel_count: 1
    plugin_configuration:
      paged_kv_cache: true
      use_paged_context_fmha: true
      use_fp8_context_fmha: true
    quantization_config:
      calib_size: 1024
      calib_dataset: "cnn_dailymail"
      calib_max_seq_length: 2048
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.9
    enable_chunked_context: true
    batch_scheduler_policy: guaranteed_no_evict
    served_model_name: "Qwen-2.5-32B-Instruct"
```

## Validation and troubleshooting

### Common errors

**Error:** `FP8 quantization is only supported on L4, H100, H200, B200`

* **Cause:** Using `FP8` quantization on unsupported GPU.
* **Fix:** Use H100 or newer GPU, or use `no_quant`.

**Error:** `FP4 quantization is only supported on B200`

* **Cause:** Using `FP4` quantization on unsupported GPU.
* **Fix:** Use B200 GPU or `FP8` quantization.

**Error:** `Using fp8 context fmha requires fp8 kv, or fp4 with kv cache dtype`

* **Cause:** Mismatch between quantization and context FMHA settings.
* **Fix:** Use `fp8_kv` quantization or disable `use_fp8_context_fmha`.

**Error:** `Tensor parallelism and GPU count must be the same`

* **Cause:** Mismatch between `tensor_parallel_count` and GPU count.
* **Fix:** Ensure `tensor_parallel_count` matches `accelerator` count.

### Performance tuning

**For lowest latency:**

* Reduce `max_batch_size` and `max_num_tokens`.
* Use `batch_scheduler_policy: guaranteed_no_evict`.
* Consider smaller models or quantization.

**For highest throughput:**

* Increase `max_batch_size` and `max_num_tokens`.
* Use `batch_scheduler_policy: max_utilization`.
* Enable quantization on supported hardware.

**For cost optimization:**

* Use L4 GPUs with `FP8` quantization.
* Choose appropriately sized models.
* Tune `max_seq_len` to your actual requirements.

## Model repository structure

All model sources (S3, GCS, HuggingFace, or tar.gz) must follow the standard HuggingFace repository structure. Files must be in the root directory, similar to running:

```bash  theme={"system"}
git clone https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
```

### Required files

**Model configuration (`config.json`):**

* `max_position_embeddings`: Limits maximum context size (content beyond this is truncated).
* `vocab_size`: Vocabulary size for the model.
* `architectures`: Must include `LlamaForCausalLM`, `MistralForCausalLM`, or similar causal LM architectures. Custom code is typically not read.
* `torch_dtype`: Default inference dtype (`float16` or `bfloat16`). Cannot be a pre-quantized model.

**Model weights (`model.safetensors`):**

* Or: `model.safetensors.index.json` + `model-xx-of-yy.safetensors` (sharded).
* Convert to safetensors if you encounter issues with other formats.
* Cannot be a pre-quantized model. Model must be an `fp16`, `bf16`, or `fp32` checkpoint.

**Tokenizer files (`tokenizer_config.json` and `tokenizer.json`):**

* For maximum compatibility, use "FAST" tokenizers compatible with Rust.
* Cannot contain custom Python code.
* For chat completions: must contain `chat_template`, a Jinja2 template.

### Architecture support

| **Model family** | **Supported architectures**            | **Notes**                                           |
| ---------------- | -------------------------------------- | --------------------------------------------------- |
| **Llama**        | `LlamaForCausalLM`                     | Full support for Llama 3. For Llama 4, use BIS-LLM. |
| **Mistral**      | `MistralForCausalLM`                   | Including v0.3 and Small variants.                  |
| **Qwen**         | `Qwen2ForCausalLM`, `Qwen3ForCausalLM` | Including Qwen 2.5 and Qwen 3 series.               |
| **QwenMoE**      | `Qwen3MoEForCausalLM`                  | Specfic support for Qwen3MoE.                       |
| **Gemma**        | `GemmaForCausalLM`                     | Including Gemma 2 and Gemma 3 series, bf16 only.    |

## Best practices

### Model size and GPU selection

| **Model size** | **Recommended GPU** | **Quantization** | **Tensor parallel** |
| -------------- | ------------------- | ---------------- | ------------------- |
| `<8B`          | L4/H100             | `FP8_KV`         | 1                   |
| 8B-70B         | H100                | `FP8_KV`         | 1-2                 |
| 70B+           | H100/B200           | `FP8_KV`/`FP4`   | 4+                  |

### Production recommendations

* Use `quantization_type: fp8_kv` for best performance/accuracy balance.
* Set `max_batch_size` based on your expected traffic patterns.
* Enable `paged_kv_cache` and `use_paged_context_fmha` for optimal performance.

### Development recommendations

* Use `quantization_type: no_quant` for fastest iteration.
* Set smaller `max_seq_len` to reduce build time.
* Use `batch_scheduler_policy: guaranteed_no_evict` for predictable behavior.
