# Source: https://docs.baseten.co/development/model/performance/engine-builder-config.md

# Engine builder configuration

> Configure your TensorRT-LLM inference engine

This reference lists every configuration option for the TensorRT-LLM Engine Builder. These options are used in `config.yaml`, such as for this Llama 3.1 8B example:

```yaml config.yaml theme={"system"}
model_name: Llama 3.1 8B Engine
resources:
  accelerator: H100:1
secrets:
  hf_access_token: "set token in baseten workspace"
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      repo: meta-llama/Llama-3.1-8B-Instruct
      source: HF
```

## `trt_llm.build`

TRT-LLM engine build configuration. TensorRT-LLM attempts to build a highly optimized network based on input shapes representative of your workload.

### `base_model`

The base model architecture of your model checkpoint. Supported architectures include:

* `decoder` - for CausalLM such as `Llama/Mistral/Qwen3ForCausalLM`
* `encoder` - for `Bert/Roberta/LLamaForSequenceClassification`, sentence-transformer models, embedding models

### `checkpoint_repository`

Specification of the model checkpoint to be leveraged for engine building. E.g.

```yaml  theme={"system"}
checkpoint_repository:
  source: HF | GCS | REMOTE_URL
  repo: meta-llama/Llama-3.1-8B-Instruct | gs://bucket_name | https://your-checkpoint.com/model.tar.gz
  revision: main  # Optional, only applicable to HF models
```

To configure access to private model checkpoints, [register secrets in your Baseten workspace](/observability/secrets#best-practices-for-secrets), namely the `hf_access_token` or `trt_llm_gcs_service_account` secrets with a valid service account json for HuggingFace or GCS, respectively.

#### `checkpoint_repository.source`

Source where the checkpoint is stored. This should contain assets as if using git clone with lfs for a Hugging Face repository.
This includes the tokenizer files, remote code and safetensor files and any json file related to configuration.
For GCS/REMOTE\_URL, we require the files to be organized in the same folder structured to a huggingface transformers repository.
Supported sources include:

* `HF` (HuggingFace)
* `GCS` (Google Cloud Storage)
* `REMOTE_URL` A tarball containing your checkpoint. **Important**: the archive must unpack with all required files (e.g., `config.json`) at the root level. For example, `config.json` should be directly in the tarball, not nested under a subdirectory like `model_name/config.json`.

#### `checkpoint_repository.repo`

Checkpoint repository name, bucket, or url.

#### `checkpoint_repository.revision`

(default: `"main"`)

The specific model version to use. It can be a branch name, a tag name, or a commit id. This field is only applicable to HF (HuggingFace) models.

### `max_batch_size`

(default: `256`)

Maximum number of input sequences to pass through the engine concurrently. Batch size and throughput share a direct relation, whereas batch size and single request latency share an indirect relation.
Tune this value according to your SLAs and latency budget.

### `max_seq_len`

(default: max\_position\_embeddings from the model repo)

Defines the maximum sequence length (context) of single request​.

### `max_num_tokens`

(default: `8192`)

Defines the maximum number of batched input tokens after padding is removed in each batch. Tuning this value more efficiently allocates memory to KV cache and executes more requests together.

### `max_prompt_embedding_table_size`

(default: `0`)

Maximum prompt embedding table size for [prompt tuning](https://developer.nvidia.com/blog/an-introduction-to-large-language-models-prompt-engineering-and-p-tuning/).

### `num_builder_gpus`

(default: `auto`)

Number of GPUs to be used at build time, defaults to configured `resource.accelerator` count – useful for FP8 quantization in particular, when more GPU memory is required at build time relative to memory usage at inference.

### `plugin_configuration`

Config for inserting plugin nodes into network graph definition for execution of user-defined kernels.

#### `plugin_configuration.paged_kv_cache`

(default: `True`)

Decompose KV cache into page blocks. Read more about what this does [here](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/advanced/gpt-attention.md#paged-kv-cache).

#### `plugin_configuration.use_paged_context_fmha`

(default: `True`)

Utilize paged context for fused multihead attention. This configuration is necessary to enable KV cache reuse. Read more about this configuration [here](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/advanced/kv-cache-reuse.md#how-to-enable-kv-cache-reuse).

#### `plugin_configuration.use_fp8_context_fmha`

(default: `False`)

Utilize FP8 quantization for context fused multihead attention to accelerate attention. To use this configuration, also set `plugin_configuration.use_paged_context_fmha`. Recommended: true
Read more about when to enable this [here](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/advanced/gpt-attention.md#fp8-context-fmha).

### `quantization_type`

(default: `no_quant`)

Quantization format with which to build the engine. Supported formats include:

* `no_quant` (meaning bf16 or fp16 depending on `torch_dtype` in the huggingface repo)
* `fp8` (sm 89+)
* `fp8_kv` (sm 89+)
* `fp4` (sm 100+)
* `fp4_kv` (sm 100+)

Additionally, refer to the hardware and quantization technique [support matrix](https://nvidia.github.io/TensorRT-LLM/reference/support-matrix.html).

### `strongly_typed`

(default: `False`)

Whether to build the engine using strong typing, enabling TensorRT's optimizer to statically infer intermediate tensor types which can speed up build time for some formats.
Automatically typed is always enabled for fp4 and fp8 engines.
Weak typing enables the optimizer to elect tensor types, which may result in a faster runtime. For more information refer to TensorRT documentation [here](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html#strong-vs-weak-typing).

### `tensor_parallel_count`

(default: `1`)

Tensor parallelism count. For more information refer to NVIDIA documentation [here](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/features/parallelisms.html#tensor-parallelism).

### `speculator`

(default: `None`)

Config for inserting optional speculative decoding options.

#### Speculation with lookahead decoding

Speculation with lookahead decoding can be used by any model and does not require training.
The implemenation is based on the work at [lmsys.](https://lmsys.org/blog/2023-11-21-lookahead-decoding/)
We currently disallow performing structured generation and tool-calling with this optimization.

```yaml  theme={"system"}
model_name: Llama-3.1-8B-Instruct (lookahead decoding)
resources:
  accelerator: H100
  use_gpu: true
trt_llm:
  build:
    base_model: llama
    checkpoint_repository:
      repo: meta-llama/Llama-3.1-8B-Instruct
      source: HF
    max_batch_size: 32
    quantization_type: fp8_kv
    speculator:
      speculative_decoding_mode: LOOKAHEAD_DECODING
      windows_size: 7
      ngram_size: 5
      verification_set_size: 7
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.62
```

#### `speculator.lookahead_ngram_size`, `speculator.lookahead_windows_size`, `speculator.lookahead_verification_set_size`

Usage of ngram size, window size, verification\_set\_size in the lookahead algorithm.

* `windows_size` is the Jacobi window size, meaning number of n-grams in lookahead branch that explores future draft tokens.
* `ngram_size` is the n-gram size, meaning the maximum number of draft tokens accepted per iteration.
* `verification_set_size` is the maximum number of n-grams considered for verification, meaning the number of draft token beam hypotheses.

A good default value could be \[5,5,5]. Often, lookahead\_verification\_set\_size is set to lookahead\_windows\_size.
`lookahead_ngram_size` is often increased when the generated tokens are simlar to contents of the prompt, and decreased if dissimilar.

### `lora_adapters`

(default: `None`)

A mapping from LoRA names to checkpoint repositories.
For example.

```yaml  theme={"system"}
checkpoint_repository:
  repo: meta-llama/Llama-2-13b-hf
  source: HF
lora_adapters:
  lora1:
    repo: hfl/chinese-llama-2-lora-13b
    source: HF
```

See [`checkpoint_repository`](/development/model/performance/engine-builder-config#checkpoint-repository) for details on how to configure checkpoint repositories.

Lora naming:
In addition to specifying the LoRAs here, you need to specify the [`served_model_name`](/development/model/performance/engine-builder-config#served-model-name) that is used to refer to the base model.
The `served_model_name` is required for deploying LoRAs.
The LoRA name (in the example above, this is "lora1") is used to query the model using the specified LoRA.

Lora sizes:
For optimal experience wrt efficency and stability we recommend inference with homogenious adapters (all the adapters have the same ranks and target the same modules).

## `trt_llm.runtime`

TRT-LLM engine runtime configuration.

### `kv_cache_free_gpu_mem_fraction`

(default: `0.9`)

Used to control the fraction of free gpu memory allocated for the KV cache. For more information, refer to the documentation [here](https://nvidia.github.io/TensorRT-LLM/performance/performance-tuning-guide/useful-runtime-flags.html#max-tokens-in-paged-kv-cache-and-kv-cache-free-gpu-memory-fraction).
If you are using DRAFT\_TOKENS\_EXTERNAL, we recommend to lower this, depending on the draft model size.

### `enable_chunked_context`

(default: `True`)

Enables chunked context, increasing the chance of batch processing between context and generation phase – which may be useful to increase throughput.
Note that one must set `plugin_configuration.use_paged_context_fmha: True` in order to leverage this feature.

### `batch_scheduler_policy`

(default: `guaranteed_no_evict`)

Supported scheduler policies are as follows:

* `guaranteed_no_evict`
* `max_utilization`

`guaranteed_no_evict` ensures that an in progress request is never evicted by reserving KV cache space for the maximum possible tokens that can be returned for a request.
`max_utilization` packs as many requests as possible during scheduling, which may increase throughput at the expense of additional latency.
For more information refer to the NVIDIA documentation [here](https://nvidia.github.io/TensorRT-LLM/performance/performance-tuning-guide/useful-runtime-flags.html#capacity-scheduler-policy).

### `request_default_max_tokens`

(default: `None`)

Default server configuration for the maximum number of tokens to generate for a single sequence, if one is not provided in the request body.
Sensible settings depend on your use case, a general value to set can be around 1000 tokens.

### `served_model_name`

(default: `None`)

The name used to refer to the base model when using LoRAs.
At least one LoRA must be specified under [`lora_adapters`](/development/model/performance/engine-builder-config#lora-adapters) to use LoRAs.
