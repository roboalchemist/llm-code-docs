# Source: https://docs.baseten.co/engines/performance-concepts/quantization-guide.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Quantization guide

> FP8 and FP4 trade-offs and hardware requirements for all engines

*Quantization* trades precision for speed and memory efficiency. This guide covers Baseten's supported formats, hardware requirements, and model-specific recommendations.

## Quantization options

Quantization type availability depends on the engine and GPU.

### Engine support

| **Quantization** | [**BIS-LLM**](/engines/bis-llm/overview) | [**Engine-Builder-LLM**](/engines/engine-builder-llm/overview) | [**BEI**](/engines/bei/overview) |
| ---------------- | ---------------------------------------- | -------------------------------------------------------------- | -------------------------------- |
| `FP8`            | ✅                                        | ✅                                                              | ✅                                |
| `FP8_KV`         | ✅                                        | ✅                                                              | ⚠️                               |
| `FP4`            | ✅                                        | ✅                                                              | ⚠️                               |
| `FP4_KV`         | ✅                                        | ✅                                                              | ⚠️                               |
| `FP4_MLP_ONLY`   | ✅                                        | ✅                                                              | ✅                                |

### GPU support

| **GPU type** | `FP8` | `FP8_KV` | `FP4` | `FP4_KV` | `FP4_MLP_ONLY` |
| ------------ | ----- | -------- | ----- | -------- | -------------- |
| **L4**       | ✅     | ✅        | ❌     | ❌        | ❌              |
| **H100**     | ✅     | ✅        | ❌     | ❌        | ❌              |
| **H200**     | ✅     | ✅        | ❌     | ❌        | ❌              |
| **B200**     | ✅     | ✅        | ✅     | ✅        | ✅              |

## Model recommendations

Some model families have specific quantization requirements that affect accuracy.

### Qwen2 models

Qwen2 retains QKV projection bias (attention bias), while Qwen3, Llama3, Llama2, and most other models remove it. This makes Qwen2 sensitive to symmetric KV cache quantization, so `FP8_KV` causes quality degradation. Use regular `FP8` instead and increase calibration size to 1024 or greater for better accuracy.

### Llama models

Llama variants work well with `FP8_KV` and standard calibration sizes (1024-1536). For B200 deployments, use `FP4_MLP_ONLY` for the best balance of speed and quality.

### BEI models (embeddings)

Use `FP8` for embedding models for causal models. Skip quantization for smaller models since the overhead isn't worth the minimal benefit and Bert is not supported. BEI doesn't support `FP8_KV`.

## Calibration

Quantization requires calibration data to determine optimal scaling factors. Larger models generally need more calibration samples.

### Calibration datasets

The default dataset is `cnn_dailymail` (general news text). For specialized models, or fine-tunes specific to a chat template, use domain-specific datasets when available.
For using a custom dataset, reference the huggingface name under `calib_dataset`, and make sure the dataset has a `train` split with a `text`/`messages` column.

When using the `messages` column, we require the tokenizer of your model to have a `apply_chat_template()` function on which we can apply `apply_chat_template(row["messages"]) for row in rows`.
If you want to use a dataset without preprocessing, you can provide a `text` column.

For chat-based calibration with thinking , we open-sourced [`baseten/quant_calibration_dataset_v1`](https://huggingface.co/datasets/baseten/quant_calibration_dataset_v1), to showcase an example.

### Calibration configuration

```yaml  theme={"system"}
quantization_config:
  calib_size: 768                    # Number of samples
  calib_dataset: "cnn_dailymail"      # Dataset name
  calib_max_seq_length: 1024          # Max sequence length
```

Increase `calib_size` for larger models. Use domain-specific datasets when available for better accuracy on specialized tasks.

## Hardware requirements

`FP4` quantization requires B200 GPUs. `FP8` runs on L4 and above.

| **Quantization** | **Minimum GPU** | **Recommended GPU** | **Memory reduction** |
| ---------------- | --------------- | ------------------- | -------------------- |
| `FP16`/`BF16`    | A100            | H100                | None                 |
| `FP8`            | L4              | H100                | \~50%                |
| `FP8_KV`         | L4              | H100                | \~60%                |
| `FP4`            | B200            | B200                | \~75%                |
| `FP4_KV`         | B200            | B200                | \~80%                |

### Configuration examples

**Engine-Builder-LLM:**

```yaml  theme={"system"}
trt_llm:
  build:
    base_model: decoder
    quantization_type: fp8
    quantization_config:
      calib_size: 1024
```

**BIS-LLM:**

```yaml  theme={"system"}
trt_llm:
  inference_stack: v2
  build:
    quantization_type: fp8
    quantization_config:
      calib_size: 1024
  runtime:
    max_seq_len: 32768
```

**BEI:**

```yaml  theme={"system"}
trt_llm:
  build:
    base_model: encoder
    quantization_type: fp8
    max_num_tokens: 16384
```

Set `quantization_type` in the build section and add `quantization_config` to customize calibration. BIS-LLM uses `inference_stack: v2` while Engine-Builder-LLM uses `base_model: decoder`.

## Best practices

### When to use quantization

Use `FP8` for production deployments to achieve cost-effective scaling. For memory-constrained environments, `FP8_KV` or `FP4` variants provide additional memory reduction. Quantization becomes essential for models over 15B parameters where memory and cost savings are significant.

### When to avoid quantization

Skip quantization when maximum accuracy is critical. Use `FP16`/`BF16` instead. Small models under 8B parameters see minimal benefit from quantization. BEI-Bert models don't support quantization at all. During research and development, `FP16` provides faster iteration without calibration overhead.

### Optimization tips

Use calibration datasets that match your domain for best accuracy. Test quantized models with your specific data before production deployment. Monitor the accuracy vs. performance trade-off and consider your hardware constraints when selecting quantization type.

## Further reading

* [Engine-Builder-LLM configuration](/engines/engine-builder-llm/engine-builder-config): Dense model configuration.
* [BIS-LLM configuration](/engines/bis-llm/bis-llm-config): MoE model configuration.
* [BEI configuration](/engines/bei/bei-reference): Embedding model configuration.
