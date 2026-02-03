# Source: https://docs.baseten.co/engines/engine-builder-llm/lookahead-decoding.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Speculative decoding guide

> Faster inference with speculative decoding for coding agents and text generation

Lookahead decoding is a speculative decoding technique that provides 2x-4x faster inference for suitable workloads by predicting future tokens using n-gram patterns. It's particularly effective for coding agents and content with predictable patterns.

## Overview

Lookahead decoding identifies n-gram patterns in the input context and past tokens, speculates on future tokens by generating candidate sequences, verifies predictions against the model's actual output, and accepts verified tokens in a single step.

The technique works with any model compatible with Engine-Builder-LLM. Baseten's B10 Lookahead implementation searches up to 10M past tokens for n-gram matches across language patterns.

## When to use lookahead decoding

Lookahead decoding excels at code generation where programming language syntax creates predictable patterns, and function signatures, variable names, and common idioms all benefit. It also accelerates prompt lookup scenarios where you provide example completions in the prompt, and general low-latency use cases where you can trade slightly decreased throughput for faster individual responses.

### Limitations

* Lookahead is supported on A10G, L4, A100, H100\_40GB, H200, and H100. Other GPUs may not be supported.
* During speculative decoding, sampling is disabled and temperature is set to 0.0.
* Speculative decoding does not affect output quality. The output depends only on model weights and prompt.
* Speculative decoding generates multiple tokens at a time. Structured output (xgrammar, outlines) with state-machine guarantees (enforced json via `response_format`) is not possible with `engine-builder-llm`.
* For few versions, chunked prefill is now allowed with lookahead decoding, we will dynamically disable chunked prefill in this case.

## Configuration

### Basic lookahead configuration

Add a `speculator` section to your build configuration:

```yaml  theme={"system"}
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen2.5-7B-Instruct"
    speculator:
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 3
      lookahead_ngram_size: 8
      lookahead_verification_set_size: 3
      enable_b10_lookahead: true
```

### Configuration parameters

**`speculative_decoding_mode`**: Set to `LOOKAHEAD_DECODING` to enable Baseten's lookahead decoding algorithm.

**`lookahead_ngram_size`**: Size of n-gram patterns for speculation. Range: 1-64, default: 8. Use `4` for simple patterns, `8` for general use (recommended), or `16-32` for complex, highly predictable patterns.

**`lookahead_verification_set_size`**: Size of verification buffer for speculation. Range: 1-8. Use `1` for high-confidence patterns, `3` for general use (recommended), or `5` for complex patterns requiring more verification.

**`lookahead_windows_size`**: Size of the speculation window. Range: 1-8. Set to the same value as `lookahead_verification_set_size`.

**`enable_b10_lookahead`**: Enable Baseten's optimized lookahead algorithm. Default: `true`. Recommenedation to keep it to `true`.

### Performance tuning

**For coding agents:** Use smaller window sizes with moderate n-gram sizes:

```yaml  theme={"system"}
speculator:
  speculative_decoding_mode: LOOKAHEAD_DECODING
  lookahead_windows_size: 1
  lookahead_ngram_size: 8
  lookahead_verification_set_size: 3
  enable_b10_lookahead: true
```

**For general text generation:** Use balanced window and n-gram sizes:

```yaml  theme={"system"}
speculator:
  speculative_decoding_mode: LOOKAHEAD_DECODING
  lookahead_windows_size: 3
  lookahead_ngram_size: 8
  lookahead_verification_set_size: 3
  enable_b10_lookahead: true
```

**For highly predictable content:** Use larger n-gram sizes with conservative verification:

```yaml  theme={"system"}
speculator:
  speculative_decoding_mode: LOOKAHEAD_DECODING
  lookahead_windows_size: 1
  lookahead_ngram_size: 32
  lookahead_verification_set_size: 1
  enable_b10_lookahead: true
```

## Performance impact

### Batch size considerations

Lookahead decoding performs best with smaller batch sizes. Set `max_batch_size` to 32 or 64, depending on your use case.

### Memory overhead

Lookahead decoding does not require additional GPU memory.

## Production best practices

### Recommended configurations

**Standard (general purpose):** Balanced settings for general-purpose text generation:

```yaml  theme={"system"}
speculator:
  speculative_decoding_mode: LOOKAHEAD_DECODING
  lookahead_windows_size: 3
  lookahead_ngram_size: 8
  lookahead_verification_set_size: 3
  enable_b10_lookahead: true
```

**Dynamic content (less predictable):**

Setting `enable_b10_lookahead: true` and `lookahead_windows_size: 1 + lookahead_verification_set_size: 1` will enable dynamic length speculation.
The speculated length will depend on the quality of the lookup match. By default we will speculate "a n-gram of k tokens for a k token suffix match".

```yaml  theme={"system"}
speculator:
  speculative_decoding_mode: LOOKAHEAD_DECODING
  lookahead_windows_size: 1
  lookahead_ngram_size: 32
  lookahead_verification_set_size: 1
  enable_b10_lookahead: true
```

**Code generation (highly predictable):** Code has predictable syntax patterns, so you can use larger windows:

```yaml  theme={"system"}
speculator:
  speculative_decoding_mode: LOOKAHEAD_DECODING
  lookahead_windows_size: 7
  lookahead_ngram_size: 5
  lookahead_verification_set_size: 7
  enable_b10_lookahead: true
```

### Build configuration

Set `max_batch_size` to control batch size limits:

```yaml  theme={"system"}
trt_llm:
  build:
    max_batch_size: 64  # Recommended for lookahead decoding
    speculator:
      speculative_decoding_mode: LOOKAHEAD_DECODING
      # ... other speculator config
```

### Engine optimization

* Use smaller batch sizes for maximum benefit (1-8 requests)
* Monitor memory overhead and adjust KV cache allocation
* Test with your specific workload for optimal parameters

## Examples

### Code generation example

Deploy a coding model with lookahead decoding on an H100:

```yaml  theme={"system"}
model_name: Qwen-Coder-7B-Lookahead
resources:
  accelerator: H100
  cpu: '1'
  memory: 10Gi
  use_gpu: true
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen2.5-7B-Instruct"
    quantization_type: fp8
    max_batch_size: 64
    speculator:
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 1
      lookahead_ngram_size: 8
      lookahead_verification_set_size: 1
      enable_b10_lookahead: true
  runtime:
    served_model_name: "Qwen-Coder-7B"
```

## Integration examples - Python code generation

Generate code using the chat completions API:

```python  theme={"system"}
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync/v1"
)

# Generate Python function refactor with lookahead decoding
code = "python\ndef hello_world(name):\n    print(42)"

response = client.chat.completions.create(
    model="not-required",
    messages=[
        {
            "role": "system", 
            "content": "You are a Python programming assistant. Write clean, efficient code."
        },
        {
            "role": "user", # By providing the code anywhere in the prompt, the generation is much faster.
            "content": f"Please refactor the follwing function to have docstrings. {code}"
        }
    ],
    temperature=0.0,
    max_tokens=200
)

print(response.choices[0].message.content)
```

## Best practices

### Configuration optimization

For coding assistants, use `lookahead_windows_size: 1` with `lookahead_ngram_size: 8` and keep batch sizes under 16 for best performance. For structured content like yamls or xml, use `lookahead_windows_size: 1` with `lookahead_ngram_size: 8`, note that `"response_format"` enforcement is not available with Engine-Builder-LLM Lookeahead decoding. For general use, start with default settings (window=3, ngram=8) and adjust based on your content patterns.

### Performance monitoring

Track tokens/second with and without lookahead to measure speed improvement, verification accuracy to see how often speculations succeed, and memory usage to catch overhead. If speed improvement diminishes, reduce batch size. Adjust window size based on content predictability and ngram size based on verification accuracy.

### Troubleshooting

**Common issues:**

**Low speed improvement:**

* Check if content is suitable for lookahead decoding
* Reduce batch size for better performance
* Adjust window and ngram sizes

**Blackwell support**

* Lookahead is not fully supported in `Engine-Builder-LLM`, check [BIS-LLM overview](/engines/bis-llm/overview) for Blackwell support.

## Further reading

* [Engine-Builder-LLM overview](/engines/engine-builder-llm/overview): Main engine documentation.
* [Engine-Builder-LLM configuration](/engines/engine-builder-llm/engine-builder-config): Complete reference config.
* [Structured outputs documentation](/engines/performance-concepts/structured-outputs): JSON schema validation.
* [Examples section](/examples/speculative-decoding): Deployment examples.
