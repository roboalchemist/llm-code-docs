# Source: https://docs.baseten.co/engines/bei/bei-reference.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration reference

> Complete reference config for BEI and BEI-Bert engines

This reference covers all configuration options for BEI and BEI-Bert deployments. All settings use the `trt_llm` section in `config.yaml`.

## Configuration structure

```yaml  theme={"system"}
trt_llm:
  inference_stack: v1  # Always v1 for BEI
  build:
    base_model: encoder | encoder_bert
    checkpoint_repository: {...}
    max_num_tokens: 16384
    quantization_type: no_quant | fp8 | fp4 | fp4_kv
    quantization_config: {...}
    plugin_configuration: {...}
  runtime:
    webserver_default_route: /v1/embeddings | /rerank | /predict
    kv_cache_free_gpu_mem_fraction: 0.9
    enable_chunked_context: true
    batch_scheduler_policy: guaranteed_no_evict
```

## Build configuration

The `build` section configures model compilation and optimization settings.

<ParamField body="base_model" type="string" required>
  The base model architecture determines which BEI variant to use.

  **Options:**

  * `encoder`: BEI - for causal embedding models (Llama, Mistral, Qwen, Gemma)
  * `encoder_bert`: BEI-Bert - for BERT-based models (BERT, RoBERTa, Jina, Nomic)

  ```yaml  theme={"system"}
  build:
    base_model: encoder
  ```
</ParamField>

<ParamField body="checkpoint_repository" type="object" required>
  Specifies where to find the model checkpoint. Repository must follow the standard HuggingFace structure.

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
    repo: "BAAI/bge-large-en-v1.5"
    revision: main
    runtime_secret_name: hf_access_token  # Optional, for private repos
  ```
</ParamField>

<ParamField body="max_num_tokens" type="number" default="16384 (BEI) / 8192 (BEI-Bert)">
  Maximum number of tokens that can be processed in a single batch. BEI and BEI-Bert run without chunked-prefill for performance reasons. This limits the effective context length to the `max_position_embeddings` value.

  **Range:** 64 to 131072, must be multiple of 64. Use higher values (up to 131072) for long context models. Most models use 16384 as default.

  ```yaml  theme={"system"}
  build:
    max_num_tokens: 16384
  ```
</ParamField>

<ParamField body="max_seq_len" type="number">
  Not supported for BEI engines. Leave this value unset. BEI automatically sets it and truncates if context length is exceeded.
</ParamField>

<ParamField body="quantization_type" type="string" default="no_quant">
  Specifies the quantization format for model weights. `FP8` quantization maintains accuracy within 1% of `FP16` for embedding models.

  **Options for BEI:**

  * `no_quant`: `FP16`/`BF16` precision
  * `fp8`: `FP8` weights + 16-bit KV cache
  * `fp4`: `FP4` weights + 16-bit KV cache (B200 only)
  * `fp4_mlp_only`: `FP4` MLP weights only (B200 only)

  **Options for BEI-Bert:**

  * `no_quant`: `FP16` precision (only option)

  For detailed quantization guidance, see [Quantization guide](/engines/performance-concepts/quantization-guide).

  ```yaml  theme={"system"}
  build:
    quantization_type: fp8
  ```
</ParamField>

<ParamField body="quantization_config" type="object">
  Configuration for post-training quantization calibration.

  **Fields:**

  * `calib_size`: Size of calibration dataset (64-16384, multiple of 64)
  * `calib_dataset`: HuggingFace dataset for calibration
  * `calib_max_seq_length`: Maximum sequence length for calibration

  ```yaml  theme={"system"}
  quantization_config:
    calib_size: 512
    calib_dataset: "cnn_dailymail"
    calib_max_seq_length: 1024
  ```
</ParamField>

<ParamField body="plugin_configuration" type="object">
  BEI automatically configures optimal TensorRT-LLM plugin settings. Manual configuration is not required or supported.

  **Automatic optimizations:**

  * XQA kernels for maximum throughput
  * Dynamic batching for optimal utilization
  * Memory-efficient attention mechanisms
  * Hardware-specific optimizations

  **Note:** Plugin configuration is only available for Engine-Builder-LLM engine.
</ParamField>

## Runtime configuration

The `runtime` section configures serving behavior.

<ParamField body="webserver_default_route" type="string" default="/v1/embeddings">
  The default API endpoint for the deployment.

  **Options:**

  * `/v1/embeddings`: OpenAI-compatible embeddings endpoint
  * `/rerank`: Reranking endpoint
  * `/predict`: Classification/prediction endpoint

  BEI automatically detects embedding models and sets `/v1/embeddings`. Classification models default to `/predict`.

  ```yaml  theme={"system"}
  runtime:
    webserver_default_route: /v1/embeddings
  ```
</ParamField>

<ParamField body="kv_cache_free_gpu_mem_fraction" type="number">
  Not applicable to BEI engines. Only used for generative models.
</ParamField>

<ParamField body="enable_chunked_context" type="boolean">
  Not applicable to BEI engines. Only used for generative models.
</ParamField>

<ParamField body="batch_scheduler_policy" type="string">
  Not applicable to BEI engines. Only used for generative models.
</ParamField>

## HuggingFace Model Repository Structure

All model sources (S3, GCS, HuggingFace, or tar.gz) must follow the standard HuggingFace repository structure. Files must be in the root directory, similar to running:

```bash  theme={"system"}
git clone https://huggingface.co/michaelfeil/bge-small-en-v1.5
```

### Model configuration

**config.json**

* `max_position_embeddings`: Limits maximum context size (content beyond this is truncated)
* `id2label`: Required dictionary mapping IDs to labels for classification models.
  * **Note**: Needs to have len of the shape of the last dense layer. Each dense output needs a `name` for the json response.
* `architecture`: Must be `ModelForSequenceClassification` or similar (cannot be `ForCausalLM`)
  * **Note**: Remote code execution is not supported; architecture is inferred automatically
* `torch_dtype`: Default inference dtype (BEI-Bert: always `fp16`, BEI: `float16`, `bfloat16`)
  * **Note**: We don't support `pre-quantized` loading, meaning your weights need to be `float16`, `bfloat16` or `float32` for all engines.
* `quant_config`: Not allowed, as no `pre-quantized` weights.

#### Model weights

**model.safetensors** (preferred)

* Or: `model.safetensors.index.json` + `model-xx-of-yy.safetensors` (sharded)
* **Note**: Convert to safetensors if you encounter issues with other formats

#### Tokenizer files

**tokenizer\_config.json** and **tokenizer.json**

* Must be "FAST" tokenizers compatible with Rust
* Typically cannot contain custom Python code, will be unread.

#### Embedding model files (sentence-transformers)

**1\_Pooling/config.json**

* Required for embedding models to define pooling strategy

**modules.json**

* Required for embedding models
* Shows available pooling layers and configurations

### Pooling layer support

| **Engine**   | **Classification Layers**  | **Pooling Types**                             | **Notes**                |
| ------------ | -------------------------- | --------------------------------------------- | ------------------------ |
| **BEI**      | 1 layer maximum            | Last token, first token                       | Limited pooling options  |
| **BEI-Bert** | Multiple layers or 1 layer | Last token, first token, mean, SPLADE pooling | Advanced pooling support |

## Complete configuration examples

### BEI with `FP8` quantization (embedding model)

```yaml  theme={"system"}
model_name: BEI-BGE-Large-FP8
resources:
  accelerator: H100
  use_gpu: true
trt_llm:
  build:
    base_model: encoder
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen3-Embedding-8B"
      revision: main
    max_num_tokens: 16384
    quantization_type: fp8
    quantization_config:
      calib_size: 1536
      calib_dataset: "cnn_dailymail"
      calib_max_seq_length: 2048
    plugin_configuration:
      paged_kv_cache: true
      use_paged_context_fmha: true
      use_fp8_context_fmha: false
  runtime:
    webserver_default_route: /v1/embeddings
    kv_cache_free_gpu_mem_fraction: 0.9
    batch_scheduler_policy: guaranteed_no_evict
```

### BEI-Bert for small BERT model

```yaml  theme={"system"}
model_name: BEI-Bert-MiniLM-L6
resources:
  accelerator: L4
  use_gpu: true
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "sentence-transformers/all-MiniLM-L6-v2"
      revision: main
    max_num_tokens: 8192
    quantization_type: no_quant
    plugin_configuration:  # Limited options for encoder models
      paged_kv_cache: false  # Disabled for encoder_bert
      use_paged_context_fmha: false
      use_fp8_context_fmha: false
  runtime:
    webserver_default_route: /v1/embeddings
    kv_cache_free_gpu_mem_fraction: 0.9
    batch_scheduler_policy: guaranteed_no_evict
```

### BEI for reranking model

```yaml  theme={"system"}
model_name: BEI-BGE-Reranker
resources:
  accelerator: H100
  use_gpu: true
trt_llm:
  build:
    base_model: encoder
    checkpoint_repository:
      source: HF
      repo: "BAAI/bge-reranker-large"
      revision: main
    max_num_tokens: 16384
    quantization_type: fp8
    quantization_config:
      calib_size: 1024
      calib_dataset: "cnn_dailymail"
      calib_max_seq_length: 2048
  runtime:
    webserver_default_route: /rerank
    kv_cache_free_gpu_mem_fraction: 0.9
    batch_scheduler_policy: guaranteed_no_evict
```

### BEI-Bert for classification model

```yaml  theme={"system"}
model_name: BEI-Bert-Language-Detection
resources:
  accelerator: L4
  use_gpu: true
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "papluca/xlm-roberta-base-language-detection"
      revision: main
    max_num_tokens: 8192
    quantization_type: no_quant
  runtime:
    webserver_default_route: /predict
    kv_cache_free_gpu_mem_fraction: 0.9
    batch_scheduler_policy: guaranteed_no_evict
```

## Validation and troubleshooting

### Common configuration errors

**Error:** `encoder does not have a kv-cache, therefore a kv specfic datatype is not valid`

* **Cause:** Using KV quantization (fp8\_kv, fp4\_kv) with encoder models
* **Fix:** Use `fp8` or `no_quant` instead

**Error:** `FP8 quantization is only supported on L4, H100, H200, B200`

* **Cause:** Using `FP8` quantization on unsupported GPU.
* **Fix:** Use H100 or newer GPU, or use `no_quant`.

**Error:** `FP4 quantization is only supported on B200`

* **Cause:** Using `FP4` quantization on unsupported GPU.
* **Fix:** Use B200 GPU or `FP8` quantization.

### Performance tuning

**For maximum throughput:**

* Use `max_num_tokens: 16384` for BEI.
* Enable `FP8` quantization on supported hardware.
* Use `batch_scheduler_policy: max_utilization` for high load.

**For lowest latency:**

* Use smaller `max_num_tokens` for your use case
* Use `batch_scheduler_policy: guaranteed_no_evict`
* Consider BEI-Bert for small models with cold-start optimization

**For cost optimization:**

* Use L4 GPUs with `FP8` quantization.
* Use BEI-Bert for small models.
* Tune `max_num_tokens` to your actual requirements.

## Migration from older configurations

If you're migrating from older BEI configurations:

1. **Update base\_model**: Change from specific model types to `encoder` or `encoder_bert`
2. **Add checkpoint\_repository**: Use the new structured repository configuration
3. **Review quantization**: Ensure quantization type matches hardware capabilities
4. **Update engine**: Add engine configuration for better performance

**Old configuration:**

```yaml  theme={"system"}
trt_llm:
  build:
    model_type: "bge"
    checkpoint_repo: "BAAI/bge-large-en-v1.5"
```

**New configuration:**

```yaml  theme={"system"}
trt_llm:
  build:
    base_model: encoder
    checkpoint_repository:
      source: HF
      repo: "BAAI/bge-large-en-v1.5"
    max_num_tokens: 16384
    quantization_type: fp8
  runtime:
    webserver_default_route: /v1/embeddings
```
