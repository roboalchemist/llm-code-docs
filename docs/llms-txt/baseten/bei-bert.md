# Source: https://docs.baseten.co/engines/bei/bei-bert.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# BEI-Bert

> BERT-optimized embeddings with cold-start performance

BEI-Bert is a specialized variant of Baseten Embeddings Inference optimized for BERT-based model architectures. It provides superior cold-start performance and 16-bit precision for models that benefit from bidirectional attention patterns.

## When to use BEI-Bert

### Ideal use cases

**Model architectures:**

* **Sentence-transformers**: `sentence-transformers/all-MiniLM-L6-v2`
* **Jina models**: `jinaai/jina-embeddings-v2-base-en`, `jinaai/jina-embeddings-v2-base-code`
* **Nomic models**: `nomic-ai/nomic-embed-text-v1.5`, `nomic-ai/nomic-embed-code-v1.5`
* **BERT variants**: `FacebookAI/roberta-base`, `cardiffnlp/twitter-roberta-base`
* **Gemma3Bidirectional**: `google/embeddinggemma-300m`
* **ModernBERT**: `answerdotai/ModernBERT-base`
* **Qwen2Bidirectional**: `Alibaba-NLP/gte-Qwen2-7B-instruct`
* **QWen3Bidirectional** `voyageai/voyage-4-nano`
* **LLama3Bidrectional** `nvidia/llama-embed-nemotron-8b`

**Deployment scenarios:**

* **Cold-start sensitive applications**: Where first-request latency is critical
* **Small to medium models**: (under 4B parameters) where quantization isn't needed
* **High-accuracy requirements**: Where 16-bit precision is preferred
* **Bidirectional attention**: Models with bidirectional attention run best on this engine.

### BEI-Bert vs BEI comparison

| Feature      | BEI-Bert                             | BEI                               |
| ------------ | ------------------------------------ | --------------------------------- |
| Architecture | BERT-based (bidirectional)           | Causal (unidirectional)           |
| Precision    | FP16 (16-bit)                        | BF16/FP16/FP8/FP4 (quantized)     |
| Cold-start   | Optimized for fast initialization    | Standard startup                  |
| Quantization | Not supported                        | FP8/FP4 supported                 |
| Memory usage | Lower for small models               | Higher or equal                   |
| Throughput   | 600-900 embeddings/sec               | 800-1400 embeddings/sec           |
| Best for     | Small BERT models, accuracy-critical | Large models, throughput-critical |

## Recommended models (MTEB ranking)

### Top-tier embeddings

**High performance (rank 2-8):**

* `Alibaba-NLP/gte-Qwen2-7B-instruct` (7.61B): Bidirectional.
* `intfloat/multilingual-e5-large-instruct` (560M): Multilingual.
* `google/embeddinggemma-300m` (308M): Google's compact model.

**Mid-range performance (rank 15-35):**

* `Alibaba-NLP/gte-Qwen2-1.5B-instruct` (1.78B): Cost-effective.
* `Salesforce/SFR-Embedding-2_R` (7.11B): Salesforce model.
* `Snowflake/snowflake-arctic-embed-l-v2.0` (568M): Snowflake large.
* `Snowflake/snowflake-arctic-embed-m-v2.0` (305M): Snowflake medium.

**Efficient models (rank 52-103):**

* `WhereIsAI/UAE-Large-V1` (335M): UAE large model.
* `nomic-ai/nomic-embed-text-v1` (137M): Nomic original.
* `nomic-ai/nomic-embed-text-v1.5` (137M): Nomic improved.
* `sentence-transformers/all-mpnet-base-v2` (109M): MPNet base.

**Specialized models:**

* `nomic-ai/nomic-embed-text-v2-moe` (475M-A305M): Mixture of experts.
* `Alibaba-NLP/gte-large-en-v1.5` (434M): Alibaba large English.
* `answerdotai/ModernBERT-large` (396M): Modern BERT large.
* `jinaai/jina-embeddings-v2-base-en` (137M): Jina English.
* `jinaai/jina-embeddings-v2-base-code` (137M): Jina code.

### Re-ranking models

**Top re-rankers:**

* `BAAI/bge-reranker-large`: XLM-RoBERTa based.
* `BAAI/bge-reranker-base`: XLM-RoBERTa base.
* `Alibaba-NLP/gte-multilingual-reranker-base`: GTE multilingual.
* `Alibaba-NLP/gte-reranker-modernbert-base`: ModernBERT reranker.

### Classification models

**Sentiment analysis:**

* `SamLowe/roberta-base-go_emotions`: RoBERTa for emotions.

## Supported model families

### Popular Hugging Face models

Find supported models on Hugging Face:

* [Embedding Models](https://huggingface.co/models?pipeline_tag=feature-extraction\&other=text-embeddings-inference\&sort=trending)
* [Classification Models](https://huggingface.co/models?pipeline_tag=text-classification\&other=text-embeddings-inference\&sort=trending)

### Sentence-transformers

The most common BERT-based embedding models, optimized for semantic similarity.

**Popular models:**

* `sentence-transformers/all-MiniLM-L6-v2` (384D, 22M params)
* `sentence-transformers/all-mpnet-base-v2` (768D, 110M params)
* `sentence-transformers/multi-qa-mpnet-base-dot-v1` (768D, 110M params)

**Configuration:**

```yaml  theme={"system"}
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "sentence-transformers/all-MiniLM-L6-v2"
    quantization_type: no_quant
  runtime:
    webserver_default_route: /v1/embeddings
```

### Voyage and Nemotron Bidrectional LLMs

Large-decoder architectures with bidirectional attention like Qwen3 (`voyageai/voyage-4-nano`) or Llama3 (`nvidia/llama-embed-nemotron-8b`) can be deployed with BEi-bert.

**Configuration:**

```yaml  theme={"system"}
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "voyageai/voyage-4-nano"
      # rewrite of the config files for compatability (no custom code support)
      revision: "refs/pr/5"
    quantization_type: no_quant
  runtime:
    webserver_default_route: /v1/embeddings
```

### Jina AI embeddings

Jina's BERT-based models optimized for various domains including code.

**Popular models:**

* `jinaai/jina-embeddings-v2-base-en` (512D, 137M params)
* `jinaai/jina-embeddings-v2-base-code` (512D, 137M params)
* `jinaai/jina-embeddings-v2-base-es` (512D, 137M params)

**Configuration:**

```yaml  theme={"system"}
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "jinaai/jina-embeddings-v2-base-en"
    quantization_type: no_quant
  runtime:
    webserver_default_route: /v1/embeddings
```

### Nomic AI embeddings

Nomic's models with specialized training for text and code.

**Popular models:**

* `nomic-ai/nomic-embed-text-v1.5` (768D, 137M params)
* `nomic-ai/nomic-embed-code-v1.5` (768D, 137M params)

**Configuration:**

```yaml  theme={"system"}
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "nomic-ai/nomic-embed-text-v1.5"
    quantization_type: no_quant
  runtime:
    webserver_default_route: /v1/embeddings
```

### Alibaba GTE and Qwen models

Advanced multilingual models with instruction-tuning and long-context support.

**Popular models:**

* `Alibaba-NLP/gte-Qwen2-7B-instruct`: Top-ranked multilingual.
* `Alibaba-NLP/gte-Qwen2-1.5B-instruct`: Cost-effective alternative.
* `intfloat/multilingual-e5-large-instruct`: E5 multilingual variant.

**Configuration:**

```yaml  theme={"system"}
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "Alibaba-NLP/gte-Qwen2-7B-instruct"
    quantization_type: no_quant
  runtime:
    webserver_default_route: /v1/embeddings
```

## Configuration examples

### Cost-effective GTE-Qwen deployment

```yaml  theme={"system"}
model_name: BEI-Bert-GTE-Qwen-1.5B
resources:
  accelerator: L4
  cpu: '1'
  memory: 15Gi
  use_gpu: true
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "Alibaba-NLP/gte-Qwen2-1.5B-instruct"
      revision: main
    max_num_tokens: 8192
    quantization_type: no_quant
  runtime:
    webserver_default_route: /v1/embeddings
    kv_cache_free_gpu_mem_fraction: 0.85
    batch_scheduler_policy: guaranteed_no_evict
```

### Basic sentence-transformer deployment

```yaml  theme={"system"}
model_name: BEI-Bert-MiniLM
resources:
  accelerator: L4
  cpu: '1'
  memory: 10Gi
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
  runtime:
    webserver_default_route: /v1/embeddings
    kv_cache_free_gpu_mem_fraction: 0.9
    batch_scheduler_policy: guaranteed_no_evict
```

### Jina code embeddings deployment

```yaml  theme={"system"}
model_name: BEI-Bert-Jina-Code
resources:
  accelerator: H100
  cpu: '1'
  memory: 10Gi
  use_gpu: true
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "jinaai/jina-embeddings-v2-base-code"
      revision: main
    max_num_tokens: 8192
    quantization_type: no_quant
  runtime:
    webserver_default_route: /v1/embeddings
    kv_cache_free_gpu_mem_fraction: 0.9
    batch_scheduler_policy: guaranteed_no_evict
```

### Nomic text embeddings with custom routing

```yaml  theme={"system"}
model_name: BEI-Bert-Nomic-Text
resources:
  accelerator: L4
  cpu: '1'
  memory: 10Gi
  use_gpu: true
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "nomic-ai/nomic-embed-text-v1.5"
      revision: main
    max_num_tokens: 16384
    quantization_type: no_quant
  runtime:
    webserver_default_route: /v1/embeddings
    kv_cache_free_gpu_mem_fraction: 0.85
    batch_scheduler_policy: guaranteed_no_evict
```

## Integration examples

### OpenAI client with Qwen3 instructions

```python  theme={"system"}
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync/v1"
)

response = client.embeddings.create(
    input="This is a test sentence for embedding.",
    model="not-required"
)

# Batch embedding with multiple documents
documents = [
    "Product documentation for software library",
    "User question about API usage",
    "Code snippet example"
]

response = client.embeddings.create(
    input=documents,
    model="not-required"
)

print(f"Embedding dimension: {len(response.data[0].embedding)}")
print(f"Processed {len(response.data)} embeddings")
```

### Baseten Performance Client

For maximum throughput with BEI-Bert:

```python  theme={"system"}
from baseten_performance_client import PerformanceClient

client = PerformanceClient(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync"
)

# High-throughput batch processing
texts = [f"Sentence {i}" for i in range(1000)]
response = client.embed(
    input=texts,
    model="not-required",
    batch_size=8,
    max_concurrent_requests=16,
    timeout_s=300
)

print(f"Processed {len(response.numpy())} embeddings")
print(f"Embedding shape: {response.numpy().shape}")
```

### Direct API usage

```python  theme={"system"}
import requests
import os
import json

headers = {
    "Authorization": f"Api-Key {os.environ['BASETEN_API_KEY']}",
    "Content-Type": "application/json"
}

data = {
    "input": ["Text to embed", "Another text"],
    "encoding_format": "float"
}

response = requests.post(
    "https://model-xxxxxx.api.baseten.co/environments/production/sync/v1/embeddings",
    headers=headers,
    json=data
)

result = response.json()
print(f"Embeddings: {len(result['data'])} embeddings generated")
```

## Best practices

### Model selection guide

Choose based on your primary constraint:

**Cost-effective (balanced performance/cost):**

* `Alibaba-NLP/gte-Qwen2-7B-instruct`: Instruction-tuned, ranked #1 for multilingual.
* `Alibaba-NLP/gte-Qwen2-1.5B-instruct`: 1/5 the size, still top-tier.
* `Snowflake/snowflake-arctic-embed-m-v2.0`: Multilingual-optimized, MRL support.

**Lightweight & fast (under 500M):**

* `google/embeddinggemma-300m`: 300M params, 100+ languages.
* `Snowflake/snowflake-arctic-embed-m-v2.0`: 305M, compression-friendly.
* `nomic-ai/nomic-embed-text-v1.5`: 137M, minimal latency.
* `sentence-transformers/all-MiniLM-L6-v2`: 22M, legacy standard.

**Specialized:**

* **Code:** `jinaai/jina-embeddings-v2-base-code`
* **Long sequences:** `Alibaba-NLP/gte-large-en-v1.5`
* **Re-ranking:** `BAAI/bge-reranker-large`, `Alibaba-NLP/gte-reranker-modernbert-base`

### Hardware optimization

**Cost-effective deployments:**

* L4 GPUs for models `<200M` parameters
* H100 GPUs for models 200-500M parameters
* Enable autoscaling for variable traffic

**Performance optimization:**

* Use `max_num_tokens: 8192` for most use cases
* Use `max_num_tokens: 16384` for long documents
* Tune `batch_scheduler_policy` based on traffic patterns

### Deployment strategies

**For development:**

* Start with smaller models (MiniLM)
* Use L4 GPUs for cost efficiency
* Enable detailed logging

**For production:**

* Use larger models (MPNet) for better quality
* Use H100 GPUs for better performance
* Implement monitoring and alerting

**For edge deployments:**

* Use smallest suitable models
* Optimize for cold-start performance
* Consider model size constraints

## Troubleshooting

### Common issues

**Slow cold-start times:**

* Ensure model is properly cached
* Consider using smaller models
* Check GPU memory availability

**Lower than expected throughput:**

* Verify `max_num_tokens` is appropriate
* Check `batch_scheduler_policy` settings
* Monitor GPU utilization

**Memory issues:**

* Reduce `max_num_tokens` if needed
* Use smaller models for available memory
* Monitor memory usage during deployment

### Performance tuning

**For lower latency:**

* Reduce `max_num_tokens`
* Use `batch_scheduler_policy: guaranteed_no_evict`
* Consider smaller models

**For higher throughput:**

* Increase `max_num_tokens` appropriately
* Use `batch_scheduler_policy: max_utilization`
* Optimize batch sizes in client code

**For cost optimization:**

* Use L4 GPUs when possible
* Choose appropriately sized models
* Implement efficient autoscaling

## Migration from other systems

### From sentence-transformers library

**Python code:**

```python  theme={"system"}
# Before (sentence-transformers)
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(sentences)

# After (BEI-Bert)
from openai import OpenAI
client = OpenAI(api_key=BASETEN_API_KEY, base_url=BASE_URL)
embeddings = client.embeddings.create(input=sentences, model="not-required")
```

### From other embedding services

BEI-Bert provides OpenAI-compatible endpoints:

1. **Update base URL**: Point to Baseten deployment
2. **Update API key**: Use Baseten API key
3. **Test compatibility**: Verify embedding dimensions and quality
4. **Optimize**: Tune batch sizes and concurrency for performance

## Further reading

* [BEI overview](/engines/bei/overview) - General BEI documentation
* [BEI reference config](/engines/bei/bei-reference) - Complete configuration options
* [Embedding examples](/examples/bei) - Concrete deployment examples
* [Performance client documentation](/engines/performance-concepts/performance-client) - Client Usage with Embeddings
* [Performance optimization](/development/model/performance-optimization) - General performance guidance
