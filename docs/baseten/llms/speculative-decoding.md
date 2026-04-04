# Source: https://docs.baseten.co/examples/speculative-decoding.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Speculative Decoding Examples

> Lookahead decoding configurations for faster inference

Speculative decoding with [lookahead decoding](/engines/engine-builder-llm/lookahead-decoding) accelerates inference for predictable workloads using n-gram patterns.

## Quick start

```yaml  theme={"system"}
trt_llm:
  build:
    speculator:
      enable_b10_lookahead: true
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 8
      lookahead_ngram_size: 1
      lookahead_verification_set_size: 1
```

## Engine compatibility

| Feature                | [Engine-Builder-LLM](/engines/engine-builder-llm/overview) | [BIS-LLM](/engines/bis-llm/overview) |
| ---------------------- | ---------------------------------------------------------- | ------------------------------------ |
| **Lookahead decoding** | ✅ Supported                                                | ✅ Gated Feature                      |
| **Structured outputs** | ❌ Incompatible                                             | ✅ Supported                          |
| **Tool calling**       | ❌ Incompatible                                             | ✅ Supported                          |
| **Eagle speculation**  | ❌ Not supported                                            | ✅ Gated Feature                      |

## Configuration examples

### Code generation (Qwen2.5-Coder)

```yaml  theme={"system"}
model_name: Qwen2.5-Coder-7B-Lookahead
resources:
  accelerator: H100
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen2.5-Coder-7B-Instruct"
    quantization_type: fp8_kv
    speculator:
      enable_b10_lookahead: true
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 3
      lookahead_ngram_size: 8
      lookahead_verification_set_size: 3
```

### Large model (Llama-3.3-70B)

```yaml  theme={"system"}
model_name: Llama-3.3-70B-Lookahead
resources:
  accelerator: H100:2
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "meta-llama/Llama-3.3-70B-Instruct"
    quantization_type: fp8_kv
    tensor_parallel_count: 2
    speculator:
      enable_b10_lookahead: true
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 3
      lookahead_ngram_size: 5
      lookahead_verification_set_size: 3
```

## Parameter tuning

See [lookahead decoding documentation](/engines/engine-builder-llm/lookahead-decoding) for detailed parameter explanations.

**Quick guidelines:**

* **lookahead\_windows\_size**: 1-7 (set to 1 for predictable content, 3 or 5 for others.)
* **lookahead\_ngram\_size**: 4-32 (large for code, smaller for creative tasks)
* **lookahead\_verification\_set\_size**: Usually equal to lookahead\_windows\_size

## Use cases

| Use case                | lookahead\_windows\_size | lookahead\_ngram\_size | Why                            |
| ----------------------- | ------------------------ | ---------------------- | ------------------------------ |
| **Code generation**     | 7                        | 3                      | Code patterns, smaller n-grams |
| **free form JSON/YAML** | 5                        | 5                      | Balanced for structured data   |
| **Template completion** | 7-10                     | 5-7                    | Highly predictable content     |

## Limitations

❌ **Not compatible with:**

* [Structured outputs](/engines/performance-concepts/structured-outputs) - Use BIS-LLM instead
* [Function calling](/engines/performance-concepts/function-calling) - Use BIS-LLM instead
* BIS-LLM engine - V2 stack doesn't support lookahead that is self-serviceable.

## Further reading

* [Lookahead decoding guide](/engines/engine-builder-llm/lookahead-decoding) - Complete reference config
* [Engine-Builder-LLM overview](/engines/engine-builder-llm/overview) - Dense model engine
* [BIS-LLM overview](/engines/bis-llm/overview) - MoE engine with structured outputs
* [Quantization guide](/engines/performance-concepts/quantization-guide) - Performance optimization
