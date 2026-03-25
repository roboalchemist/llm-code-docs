# Source: https://docs.anyscale.com/rag/production-scalability.md

# Scale RAG for production

[View Markdown](/rag/production-scalability.md)

# Scale RAG for production

Moving from a RAG prototype to a production system requires you to address challenges in data processing scale, retrieval latency, inference throughput, and operational reliability. This guide shows how Ray and Anyscale address these challenges with distributed data processing, scalable model serving, and managed infrastructure.

If you're new to RAG, see [Retrieval-augmented generation (RAG) on Anyscale](/rag.md) and [RAG basics](/rag/rag_basics.md) for an introduction to the architecture and basic concepts.

## Scale the data ingestion pipeline[​](#scale-ingestion "Direct link to Scale the data ingestion pipeline")

The first bottleneck in a production RAG system is often the data ingestion pipeline. As your knowledge base grows from dozens to millions of documents, chunking documents and generating embeddings becomes computationally expensive and can't run on a single machine. This requires a distributed systems approach.

### Use a heterogeneous compute pipeline[​](#heterogeneous-compute "Direct link to Use a heterogeneous compute pipeline")

Use a heterogeneous hardware pipeline that assigns different stages of the process to the compute resources best suited for them. Ray Data is a distributed data processing library that orchestrates this workflow across a cluster of CPU and GPU workers, maximizing resource utilization and minimizing cost. For an example using Ray Data for a scalable RAG compute pipeline, see the [Scalable RAG Data Ingestion with Ray Data](https://console.anyscale.com/template-preview/e2e-rag-deepdive?file=%252Ffiles%252Fnotebooks%252F02_Scalable_RAG_Data_Ingestion_with_Ray_Data.ipynb) template notebook.

* **Use CPUs for text processing and chunking**: Loading documents, parsing text, and chunking are CPU-intensive tasks. Ray Data distributes this work across multiple CPU workers to parallelize the load.
* **Use GPUs for embedding generation**: Generating embeddings is a massively parallel task well-suited for GPUs. Ray Data streams the text chunks from the CPU workers to a separate pool of GPU workers.

This streaming execution ensures that expensive GPUs don't sit idle waiting for CPU-bound preprocessing tasks to complete, which reduces the end-to-end time for ingestion. For production workloads, you implement this using stateful actors, which load the embedding model into memory once per worker and reuse it for all subsequent batches, avoiding costly I/O latency from reloading the model repeatedly.

### Decouple compute from storage[​](#decouple-storage "Direct link to Decouple compute from storage")

Decouple the embedding generation pipeline from the vector database. Instead of writing embeddings directly to the database as they're computed, write the final dataset of chunks and embeddings to intermediate object storage (for example, Parquet files on AWS, Google Cloud, or Azure). A separate, simpler job then bulk-inserts this prepared data into the vector database.

This decoupled architecture is more fault-tolerant. If a long-running embedding job fails late in the process due to a transient database error, the direct-to-database pattern can lose hours of compute. In the decoupled pattern, the database ingestion is a separate, idempotent operation that you can retry independently without rerunning the costly embedding pipeline.

## Optimize LLM serving for high throughput and low latency[​](#optimize-serving "Direct link to Optimize LLM serving for high throughput and low latency")

For RAG applications, the primary performance challenge is time to first token (TTFT). RAG prompts are uniquely long, composed of a system prompt, a large, dynamically retrieved context, and the user's question. The "prefill stage," where the LLM processes this long input to generate the first token, is the dominant source of latency. For more information on optimizing LLM serving performance, see [Optimize performance for Ray Serve LLM](/llm/serving/performance-optimization.md).

### Use prefix caching[​](#prefix-caching "Direct link to Use prefix caching")

Prefix caching stores the LLM's internal state after processing a shared initial sequence of tokens (a prefix). When a new request arrives with the same prefix, the model reuses this cached state instead of recomputing it.

This is effective for RAG workloads. When multiple users ask different questions about the same topic, the RAG system often retrieves the same document chunks. In many applications, the system prompt and instructions at the start of the request are also identical (for example, "You are a helpful assistant... Given the following context... Output the answer in JSON..."), which creates an additional shared prefix across requests. With prefix caching, the LLM processes this long shared prefix and context only once. All subsequent requests that retrieve the same prefix and context skip the recomputation and proceed directly to processing the user's specific question, which reduces TTFT. The vLLM inference engine, which integrates with Ray Serve, enables prefix caching automatically. See [Automatic prefix caching](/llm/serving/performance-optimization.md#prefix-caching) for more details.

### Use prefix cache-aware routing[​](#prefix-cache-routing "Direct link to Use prefix cache-aware routing")

In a distributed, multi-replica deployment, prefix caching alone isn't enough. A stateless load balancer might send requests with the same prefix to different replicas, causing a cache miss every time and negating the benefit.

Ray Serve's `PrefixCacheAffinityRouter` is a stateful, cache-aware router that solves this problem. It tracks the cache content on each replica and routes incoming requests to the replica with the longest matching prefix. This ensures maximum cache utilization in a distributed environment. See [Prefix cache-aware router](/llm/serving/performance-optimization.md#cache-aware-router) and the [Ray documentation on PrefixCacheAffinityRouter](https://docs.ray.io/en/latest/serve/llm/prefix-aware-request-router.html) for more details.

### Optimize prompts for caching[​](#optimize-prompts "Direct link to Optimize prompts for caching")

You can maximize the benefit of prefix caching with a simple change to your prompt structure. To create the longest possible stable prefix, design your prompts so that static content comes first and variable content appears at the end. Placing the user's question or variables such as date and time at the end creates the largest possible shared prefix for the system to match and cache.

### Use quantized models[​](#quantized-models "Direct link to Use quantized models")

Quantization reduces the precision of a model's weights, which decreases its memory footprint and speeds up inference. This allows you to serve larger models on the same hardware or use smaller, less expensive GPUs. Ray Serve LLM and vLLM provide optimized support for various quantization techniques. See [Optimize LLM performance with quantization](/llm/serving/performance-optimization.md#quantization) and the [vLLM quantization documentation](https://docs.vllm.ai/en/latest/features/quantization/index.html) for more details.

### Use n-gram speculative decoding[​](#ngram-speculative-decoding "Direct link to Use n-gram speculative decoding")

Speculative decoding accelerates generation by proposing and verifying multiple tokens at once. An n-gram-based approach drafts several likely next tokens using n-gram statistics, then validates them with the target model in a single step. Accepted tokens are emitted immediately. If a proposed token doesn't match what the model would normally generate under your decoding settings, the algorithm discards the remaining draft and continues generating tokens in the usual way.

This reduces time to first token and improves throughput when prompts are long and decoding is near-greedy (low temperature, small top-p or top-k). Start with a small look-ahead (for example, 2-4 tokens), measure the acceptance rate and answer quality on your prompts, then gradually increase the look-ahead as needed.

This technique is particularly effective for RAG workloads because RAG requests reuse a shared prompt template and often retrieve similar context across queries. Early output tokens are predictable, which raises draft acceptance rates and increases throughput. See the [vLLM speculative decoding documentation](https://docs.vllm.ai/en/latest/features/speculative_decoding.html) for configuration details.

## Implement a multi-level caching strategy[​](#multi-level-caching "Direct link to Implement a multi-level caching strategy")

Caching at different levels of the RAG pipeline reduces redundant computation, lowers costs, and improves response times.

* **Embedding cache**: Cache the vector embeddings of frequently seen user queries. This simple key-value cache saves the cost and latency of running the embedding model for common questions.
* **Semantic caching**: Cache the final LLM response for a given query, indexed by the query's embedding. When a new query arrives, check if a semantically similar query exists in the cache (for example, with cosine similarity greater than 0.95) and return the stored result, bypassing the entire RAG pipeline.

warning

High embedding similarity doesn't guarantee that the cached answer is correct for the new query. Queries with specific qualifiers such as dates, years, versions, or user scope (for example, "What are the top 10 AI trends in 2024?" versus "What are the top 10 AI trends in 2025?") can have very similar embeddings but still require fresh retrieval and generation. When in doubt, rerun the RAG pipeline or incorporate those qualifiers into your cache key.

* **Generation cache**: Cache the final LLM-generated response for an identical prompt. This works best for frequently asked questions where the query and retrieved context are identical.

### Manage cache invalidation[​](#cache-invalidation "Direct link to Manage cache invalidation")

Address stale data in your caching strategy. When you update the underlying knowledge base, invalidate the cache.

* **Adaptive time to live (TTL)**: Set expiration times based on how often the content changes. Static documents can have long TTLs (hours or days), while dynamic data needs short TTLs (minutes).
* **Event-driven invalidation**: Use webhooks from your content management system to trigger a purge command that immediately evicts stale entries from the cache when a document is updated.
* **Version-based cache keys**: Embed a data version into the cache key. When you update the knowledge base to a new version, all new queries hash to a new key, automatically missing the old cache and invalidating it.

## Select a vector database for production[​](#vector-database "Direct link to Select a vector database for production")

While a local vector store is useful for prototyping, a production system requires a dedicated, scalable vector database. Consider the following criteria when choosing one:

* **Scalability**: Ensure the database can scale to your projected vector count for the next 12-24 months.
* **Performance**: Evaluate query latency at your desired recall (accuracy).
* **Metadata filtering**: Assess how efficiently it supports filtering on vector metadata, which is critical for multi-tenant or security-trimmed applications.
* **Keyword or hybrid search**: Evaluate whether the database supports keyword search or hybrid search (combining vector similarity with keyword matching), which can improve retrieval quality for queries with specific terms or exact matches.
* **Deployment model**: Choose between a managed SaaS solution for ease of use or a self-hosted open-source database for maximum control and potentially lower cost at scale.

The following table compares common vector databases for production use cases.

| Database | Deployment model     | Ideal use case                                                                                                                                                                                        | Key differentiator                                                      |
| -------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Pinecone | Managed (SaaS)       | Commercial AI SaaS; for teams valuing time-to-market over cluster control.                                                                                                                            | Serverless, "minimal ops," and easy to scale.                           |
| Weaviate | Open-source, Managed | Applications needing a balance of control and strong hybrid (keyword + vector) search.                                                                                                                | Strong native hybrid search and modular design.                         |
| Milvus   | Open-source, Managed | Enterprise-scale or on-premise deployments with dedicated data engineering talent.                                                                                                                    | Proven architecture for billion-scale vector counts.                    |
| Qdrant   | Open-source, Managed | Cost-sensitive or performance-conscious workloads.                                                                                                                                                    | Resource-efficient, written in Rust, with powerful filtering.           |
| Chroma   | Open-source, Managed | Developer-led LLM apps that want a local-first path to production, strong metadata filtering, and native full-text + vector search; single-node for moderate scale or managed cloud for larger needs. | Native FTS + vector + metadata in one engine; simple client/server mode |
| pgvector | PostgreSQL Extension | For teams already using PostgreSQL who need "good enough" vector search without adding a new database.                                                                                                | Integrates vector search into an existing relational database.          |

For an example integrating embedding computing with Pinecone on Anyscale, see [10x Cheaper Embedding Computations with Anyscale and Pinecone](https://www.anyscale.com/blog/rag-at-scale-10x-cheaper-embedding-computations-with-anyscale-and-pinecone).

## Monitor your RAG system[​](#monitor-system "Direct link to Monitor your RAG system")

Monitor your RAG application continuously to maintain quality and reliability in production. For comprehensive guidance on RAG evaluation, including detailed metrics, evaluation frameworks, and best practices, see [RAG evaluation](/rag/evaluation.md).

### Monitor key quality metrics[​](#quality-metrics "Direct link to Monitor key quality metrics")

Track the following metrics to monitor RAG system quality:

* **Contextual relevance**: Measures whether the retrieved context is relevant to the user's query. This metric evaluates your retriever.
* **Faithfulness**: Measures whether the generated answer is grounded in the retrieved context. This metric detects hallucination and evaluates your generator.
* **Answer relevance**: Measures whether the generated answer addresses the user's query. An answer can be faithful to the context but still miss the point of the question.

These metrics form the "RAG Triad" and provide an actionable framework for debugging. By logging these scores, you can quickly diagnose the root cause of a failure:

* Low contextual relevance signals a retrieval failure. The problem is in your data parsing, chunking strategy, or embedding model.
* High contextual relevance but low faithfulness signals a generation failure (hallucination). The retriever found the right information, but the LLM ignored it. The problem is in your prompt engineering or the LLM itself.

For detailed information on these metrics and additional evaluation approaches, see [Generation metrics](/rag/evaluation.md#generation-metrics).

### Automate evaluation in CI/CD[​](#automate-testing "Direct link to Automate evaluation in CI/CD")

Integrate evaluation into your CI/CD pipeline. Test every change, whether to the knowledge base, retrieval model, or LLM prompt, against a "gold standard" set of questions and answers to prevent regressions. Frameworks such as DeepEval integrate directly with testing suites such as pytest, allowing you to fail a build automatically if a quality metric drops below a set threshold.

For more information on evaluation frameworks and automation best practices, see [Evaluation frameworks](/rag/evaluation.md#evaluation-frameworks) and [Best practices](/rag/evaluation.md#best-practices).

### Iterate and improve quality[​](#iterate-quality "Direct link to Iterate and improve quality")

Use your monitoring metrics to drive continuous improvement. When you identify quality issues through evaluation, iterate on your RAG pipeline to address root causes.

Quality problems often manifest at one stage but originate at another. For example, low faithfulness scores might indicate a generation problem, but the root cause could be poor chunking that breaks semantic context. Use the RAG Triad metrics to diagnose where failures occur, then apply targeted improvements.

The following guides provide strategies for addressing common quality issues across each stage of your RAG pipeline:

* **Data ingestion**: Fix missing content, improve chunking strategies, and address semantic mismatches. See [Data ingestion strategies: building a quality foundation](/rag/quality-improvement/data-ingestion-strategies.md).
* **Retrieval**: Improve precision and recall, handle complex queries, and combine vector search with exact-match lookups. See [Retrieval strategies: Finding the right information](/rag/quality-improvement/retrieval-strategies.md).
* **Generation**: Address context overload, reduce hallucination, and improve extraction accuracy. See [Generation strategies: Ensuring accurate synthesis](/rag/quality-improvement/generation-strategies.md).

For a holistic approach to quality improvement, including how to combine strategies and measure their impact, see [RAG quality improvement strategies](/rag/quality-improvement.md).
