# Source: https://docs.anyscale.com/llm/batch-inference/throughput-optimization/quantization.md

# Quantization for LLM batch inference

[View Markdown](/llm/batch-inference/throughput-optimization/quantization.md)

# Quantization for LLM batch inference

Quantization reduces the numerical precision of model weights, converting them from higher precision formats to lower precision formats. This technique significantly reduces GPU memory requirements, allowing you to process more requests and improve overall throughput.

For additional optimization strategies beyond quantization, see [Optimize throughput for Ray Data LLM batch inference](/llm/batch-inference/throughput-optimization/tuning-strategies.md).

## Benefits for batch inference[​](#benefits "Direct link to Benefits for batch inference")

Quantization provides several advantages for batch workloads:

* **Reduced memory usage**: Enables larger models to run on fewer or smaller GPUs. FP8 quantization typically halves memory requirements compared to BF16.
* **Increased throughput**: Allows processing more concurrent sequences by freeing up GPU memory for KV cache.
* **Increased scalability**: Enables you to scale up the number of inference workers running on the same cluster.
* **Lower costs**: Enables use of smaller, cheaper GPUs for the same workload.

## Configure quantization[​](#configure "Direct link to Configure quantization")

vLLM supports several quantization methods through Ray Data LLM:

| Method   | Precision            | Memory reduction  | Use case                                  |
| -------- | -------------------- | ----------------- | ----------------------------------------- |
| **FP8**  | 8-bit floating point | \~50% vs BF16     | Best balance of quality and efficiency    |
| **INT8** | 8-bit integer        | \~50% vs BF16     | Good for memory-constrained scenarios     |
| **INT4** | 4-bit integer        | \~75% vs BF16     | Maximum memory savings, quality trade-off |
| **GPTQ** | Variable (2-8 bit)   | Up to 75% vs BF16 | Pre-quantized models from Hugging Face    |
| **AWQ**  | 4-bit                | \~75% vs BF16     | Optimized for generation quality          |

For the complete list of quantization methods and configuration options, see the [vLLM quantization documentation](https://docs.vllm.ai/en/stable/features/quantization/index.html).

Ray Data LLM forwards vLLM engine parameters through the `engine_kwargs` argument in `vLLMEngineProcessorConfig`. You can configure quantization methods, data types, and other vLLM-specific parameters this way.

The following example shows how to perform inflight quantization to load a Llama model with 4-bit quantization:

```
# Install BitsAndBytes
# pip install bitsandbytes>=0.46.1
from ray.data.llm import vLLMEngineProcessorConfig
import torch

config = vLLMEngineProcessorConfig(
    model_source="huggyllama/llama-7b",
    ...,
    engine_kwargs={
        "quantization": "bitsandbytes",
        "trust_remote_code": True,
        "dtype": torch.bfloat16,
        ...
    },
)
```

## GPU compatibility[​](#gpu-compatibility "Direct link to GPU compatibility")

Not all GPUs support all quantization methods. Verify your GPU supports the quantization method you plan to use:

| Quantization method | GPU requirements                                               | Recommended GPUs         |
| ------------------- | -------------------------------------------------------------- | ------------------------ |
| FP8                 | Ada Lovelace or Hopper architecture with FP8 Tensor Cores      | H100, H200, L4, L40S     |
| INT8                | Turing architecture and later generations (Ampere recommended) | A100, A10G, L4, H100, T4 |
| INT4/GPTQ/AWQ       | Most GPUs with CUDA compute capability 7.0+                    | A10G, L4, A100, H100     |

warning

Always verify GPU compatibility before deploying quantized models. Incompatible configurations can cause runtime errors or performance degradation. See the [vLLM compatibility matrix](https://docs.vllm.ai/en/stable/features/quantization/index.html#supported-hardware).

## Evaluate quality trade-offs[​](#quality "Direct link to Evaluate quality trade-offs")

Quantization reduces precision, which can impact model quality. Before deploying to production, test your batch inference on a sample dataset and compare outputs with the unquantized model. Evaluate task-specific quality metrics such as accuracy, BLEU, or perplexity, and pay attention to performance on rare or complex inputs where quantization effects may be more pronounced.

Most modern quantization methods such as FP8 maintain 99%+ of original model quality, but always validate for your specific use case.
