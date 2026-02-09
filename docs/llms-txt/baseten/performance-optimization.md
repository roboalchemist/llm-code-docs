# Source: https://docs.baseten.co/development/model/performance-optimization.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Performance optimization

> Optimize model latency, throughput, and cost with Baseten engines

Model performance means optimizing every layer of your model serving infrastructure to balance four goals:

1. **Latency**: How quickly does each user get output from the model?
2. **Throughput**: How many requests can the deployment handle at once?
3. **Cost**: How much does a standardized unit of work cost?
4. **Quality**: Does your model consistently deliver high-quality output after optimization?

## Performance engines

Baseten's performance-optimized engines deliver the best possible inference speed and efficiency:

### **[Engine-Builder-LLM](/engines/engine-builder-llm/overview)** - Dense Models

* **Best for**: Llama, Mistral, Qwen, and other causal language models
* **Features**: TensorRT-LLM optimization, lookahead decoding, quantization
* **Performance**: Lowest latency and highest throughput for dense models

### **[BIS-LLM](/engines/bis-llm/overview)** - MoE Models

* **Best for**: DeepSeek, Mixtral, and other mixture-of-experts models
* **Features**: V2 inference stack, expert routing, structured outputs
* **Performance**: Optimized for large-scale MoE inference

### **[BEI](/engines/bei/overview)** - Embedding Models

* **Best for**: Sentence transformers, rerankers, classification models
* **Features**: OpenAI-compatible, high-performance embeddings
* **Performance**: Fastest embedding inference with optimized batching

## Performance concepts

Detailed performance optimization guides are now organized in the **[Performance Concepts](/engines/performance-concepts/quantization-guide)** section:

* **[Quantization Guide](/engines/performance-concepts/quantization-guide)** - FP8/FP4 trade-offs and hardware requirements
* **[Structured Outputs](/engines/performance-concepts/structured-outputs)** - JSON schema validation and controlled generation
* **[Function Calling](/engines/performance-concepts/function-calling)** - Tool use and function selection
* **[Performance Client](/engines/performance-concepts/performance-client)** - High-throughput client library
* **[Deployment Guide](/engines/performance-concepts/deployment-from-training-and-s3)** - Training checkpoints and cloud storage

## ⚡ Quick performance wins

### **Quantization**

Reduce memory usage and improve speed with post-training quantization:

```yaml  theme={"system"}
trt_llm:
  build:
    quantization_type: fp8  # 50% memory reduction
```

### **Lookahead Decoding**

Accelerate inference for predictable content (code, JSON):

```yaml  theme={"system"}
trt_llm:
  build:
    speculator:
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 5
```

### **Performance Client**

Maximize client-side throughput with Rust-based client:

```bash  theme={"system"}
pip install baseten-performance-client
```

## 🔧 Where to start

1. **Choose your engine**: [Engines overview](/engines)
2. **Configure your model**: Engine-specific configuration guides
3. **Optimize performance**: [Performance concepts](/engines/performance-concepts/quantization-guide)
4. **Deploy and monitor**: Use [performance client](/engines/performance-concepts/performance-client) for maximum throughput

***

**💡 Tip**: Start with the default engine configuration, then apply quantization and other optimizations based on your specific performance requirements.
