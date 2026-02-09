# Source: https://docs.baseten.co/reference/cli/index.md

# Source: https://docs.baseten.co/engines/index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Engine selection guide for embeddings, dense LLMs, and MoE models

Baseten engines optimize model inference for specific architectures using [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM). Select an engine based on your model type (embeddings, dense LLMs, or mixture-of-experts) to achieve the best latency and throughput.

## Engine ecosystem

<CardGroup cols={2}>
  <Card title="BEI (Embeddings & Classification)" href="/engines/bei/overview" icon="brain-circuit" iconType="duotone">
    Embeddings, reranking, and classification models with up to 1400 embeddings/sec throughput.
  </Card>

  <Card title="Engine-Builder-LLM (Dense Models)" href="/engines/engine-builder-llm/overview" icon="microchip" iconType="duotone">
    Dense text generation models with [lookahead decoding](/engines/engine-builder-llm/lookahead-decoding), [structured outputs](/engines/performance-concepts/structured-outputs), and single node inference.
  </Card>

  <Card title="BIS-LLM (MoE & Advanced)" href="/engines/bis-llm/overview" icon="network" iconType="duotone">
    MoE models with [KV-aware routing](/engines/bis-llm/advanced-features#kv-aware-routing), [tool calling](/engines/performance-concepts/function-calling), and speculative decoding.
  </Card>

  <Card title="Specialized Deployments" href="#specialized-deployments" icon="server" iconType="duotone">
    Specialized engines for models like Whisper, Orpheus, or Flux, available as dedicated deployments rather than self-serviceable options.
  </Card>
</CardGroup>

## Engine selection

Select an engine based on your model's architecture and expected workload.

| Model type         | Architecture                  | Recommended engine | Key features                              | **Hardware**             |
| ------------------ | ----------------------------- | ------------------ | ----------------------------------------- | ------------------------ |
| **Dense LLM**      | CausalLM (text generation)    | Engine-Builder-LLM | Lookahead decoding, structured outputs    | H100, B200               |
| **MoE Models**     | Mixture of Experts            | BIS-LLM            | KV-aware routing, advanced quantization   | H100, B200               |
| **Large Models**   | 700B+ parameters              | BIS-LLM            | Distributed inference, `FP4` support      | H100, B200               |
| **Embeddings**     | BERT-based (bidirectional)    | BEI-Bert           | Cold-start optimization, 16-bit precision | T4, L4, A10G, H100, B200 |
| **Embeddings**     | Causal (Llama, Mistral, Qwen) | BEI                | `FP8` quantization, high throughput       | L4, A10G, H100, B200     |
| **Reranking**      | Cross-encoder architectures   | BEI / BEI-Bert     | Low latency, batch processing             | L4, A10G, H100, B200     |
| **Classification** | Sequence classification       | BEI / BEI-Bert     | High throughput, cached weights           | L4, A10G, H100, B200     |

### Feature availability

| Feature                              | BIS-LLM | Engine-Builder-LLM | BEI | BEI-Bert | Notes                                            |
| ------------------------------------ | ------- | ------------------ | --- | -------- | ------------------------------------------------ |
| **Quantization**                     | ✅       | ✅                  | ✅   | ❌        | BEI-Bert: `FP16`/`BF16` only                     |
| **KV quantization**                  | ✅       | ✅                  | ⚠️  | ⚠️       | `FP8_KV`, `FP4_KV` supported                     |
| **Speculative lookahead decoding**   | Gated   | ✅                  | ❌   | ❌        | n-gram based speculation                         |
| **Self-serviceable**                 | Gated/✅ | ✅                  | ✅   | ✅        | All engines self-service                         |
| **KV-routing**                       | Gated   | ❌                  | ❌   | ❌        | BIS-LLM only                                     |
| **Disaggregated serving**            | Gated   | ❌                  | ❌   | ❌        | BIS-LLM enterprise                               |
| **Tool calling & structured output** | ✅       | ✅                  | ❌   | ❌        | Function calling support                         |
| **Classification models**            | ❌       | ❌                  | ✅   | ✅        | Sequence classification                          |
| **Embedding models**                 | ❌       | ❌                  | ✅   | ✅        | Embedding generation                             |
| **Mixture-of-experts**               | ✅       | ⚠️ (Qwen3MoE only) | ❌   | ❌        | Mixture of Experts models like DeepSeek          |
| **MTP and Eagle 3 speculation**      | Gated   | ❌                  | ❌   | ❌        | Model-based speculation                          |
| **HTTP request cancellation**        | ✅       | ❌                  | ✅   | ✅        | Engine-Builder supports it within the first 10ms |
| **MultiModal Inputs**                | Gated   | ❌                  | ⚠️  | ❌        | Selected architectures only                      |

## Architecture recommendations

### BEI vs BEI-Bert (embeddings)

BEI-Bert optimizes BERT-based architectures (sentence-transformers, jinaai, nomic-ai) with fast cold-start performance and 16-bit precision. Choose BEI-Bert for bidirectional models under 4B parameters where cold-start latency matters. Jina-BERT, Nomic, and ModernBERT architectures all run well on this engine.

BEI handles causal embedding architectures (Llama, Mistral, Qwen) with `FP8`/`FP4` quantization support. Choose BEI when you need maximum throughput or want to run larger embedding models like BAAI/bge, Qwen3-Embedding, or Salesforce/SFR-Embedding with quantization.

### Engine-Builder-LLM vs BIS-LLM (text generation)

Engine-Builder-LLM serves dense models (non-MoE) with lookahead decoding and structured outputs. Choose it for Llama 3.3, Qwen-3, Qwen2.5, Mistral, or Gemma-3 when you need speculative decoding for coding agents or JSON schema validation.

BIS-LLM serves large MoE models with KV-aware routing and advanced tool calling. Choose it for DeepSeek-R1, Qwen3MoE, Kimi-K2, Llama-4, or GLM-4.7 when you need enterprise features like disaggregated serving or H100/B200 optimization.

## Performance benchmarks

Benchmark results depend on model size, GPU type, and quantization settings. The figures below represent typical performance on H100 GPUs.

### Embedding performance (BEI/BEI-Bert)

* **Throughput**: Up to 1400 client embeddings per second.
* **Latency**: Sub-millisecond response times.
* **Quantization**: `FP8`/`FP4` provides 2x speedup with less than 1% accuracy loss.

### Text generation performance (Engine-Builder-LLM/BIS-LLM)

* **Speculative decoding**: Faster inference for code and structured content through lookahead decoding.
* **Quantization**: Memory reduction and speed improvements with `FP8`/`FP4`.
* **Distributed inference**: Scalable deployment with tensor parallelism.

## Hardware requirements and optimization

*[Quantization](/engines/performance-concepts/quantization-guide)* reduces memory usage and improves inference speed.

| Quantization  | Minimum GPU | Recommended GPU | Memory reduction | Notes                                       |
| ------------- | ----------- | --------------- | ---------------- | ------------------------------------------- |
| `FP16`/`BF16` | A100        | H100            | None             | Baseline precision                          |
| `FP8`         | L4          | H100            | \~50%            | Good balance of performance and accuracy    |
| `FP8_KV`      | L4          | H100            | \~60%            | KV cache quantization for memory efficiency |
| `FP4`         | B200        | B200            | \~75%            | B200-only quantization                      |
| `FP4_KV`      | B200        | B200            | \~80%            | Maximum memory reduction                    |

<Note id="specialized-deployments">
  Some models require specialized engines that are not self-serviceable:

  * **Whisper**: Audio transcription and speech recognition.
  * **Orpheus**: Audio generation.
</Note>

## Next steps

* [BEI documentation](/engines/bei/overview): Embeddings and classification.
* [Engine-Builder-LLM documentation](/engines/engine-builder-llm/overview): Dense text generation.
* [BIS-LLM documentation](/engines/bis-llm/overview): MoE and advanced features.

**Examples:**

* [BEI deployment guide](/examples/bei): Complete embedding model setup.
* [TensorRT-LLM examples](/examples/tensorrt-llm): Dense LLM deployment.
* [DeepSeek examples](/examples/models/deepseek/deepseek-r1): Large MoE deployment.
