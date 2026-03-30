# Source: https://docs.anyscale.com/rag.md

# Retrieval-augmented generation (RAG) on Anyscale

[View Markdown](/rag.md)

# Retrieval-augmented generation (RAG) on Anyscale

This page provides an overview of RAG on Anyscale, including what RAG is, how to get started, how to improve quality and scale for production, and the benefits of using Anyscale for RAG workloads.

## What is RAG?[​](#what-is-rag "Direct link to What is RAG?")

Retrieval-augmented generation combines an LLM with fresh, task-specific context fetched from your data. You retrieve relevant knowledge, compose the prompt with that context, and generate an answer that you can cite and audit.

At a high level, a RAG workflow does the following:

1. Retrieves supporting context from a knowledge source such as a vector index, keyword search, or a database.
2. Augments the prompt by combining the user request with the retrieved context and clear instructions.
3. Generates a response with an LLM and optionally returns citations.

For more details on RAG architecture, data ingestion, and retrieval pipelines, see [RAG basics](/rag/rag_basics.md).

## Get started with RAG[​](#get-started "Direct link to Get started with RAG")

To get started with RAG on Anyscale, see the [distributed RAG pipeline template](https://console.anyscale.com/template-preview/e2e-rag-deepdive?file=%252Ffiles%252Fnotebooks). The template covers building a basic ingestion pipeline, scaling with Ray Data, deploying LLMs with Ray Serve, building query pipelines, using advanced prompt engineering, and running scalable evaluations.

See [RAG quickstart on Anyscale](/rag/quickstart.md).

## Improve RAG quality[​](#improve-quality "Direct link to Improve RAG quality")

To optimize RAG systems, address failures across three stages: pre-retrieval (indexing and chunking), retrieval (search quality), and generation (LLM synthesis). Common challenges include missing or stale content, suboptimal chunking strategies, misinterpreted user intent, low precision or recall, and hallucinations.

To improve quality, use strategies such as semantic chunking, hybrid search, and HyDE. See [RAG quality improvement strategies](/rag/quality-improvement.md).

Measure retrieval quality (Precision\@k, Recall\@k, MRR) and generation quality (faithfulness, relevance, completeness) using frameworks such as RAGAS, TruLens, or DeepEval. See [RAG evaluation](/rag/evaluation.md).

## Scale RAG for production[​](#scale-production "Direct link to Scale RAG for production")

When you're ready to move from a RAG prototype to production, you likely have to address challenges in data processing scale, retrieval latency, inference throughput, and operational reliability.

Key considerations include the following:

* **Distributed data ingestion**: Use heterogeneous compute with CPUs for text processing and GPUs for embeddings.
* **Prefix caching**: Reduce time-to-first-token for long RAG prompts.
* **Cache-aware routing**: Maximize cache hits across replicas with [prefix-aware routing](https://docs.ray.io/en/latest/serve/llm/user-guides/prefix-aware-routing.html).
* **Multi-level caching**: Implement embedding cache, semantic cache, and generation cache.
* **Vector database optimization**: Select the right database and maintain indexes properly.

Production systems also need comprehensive observability with trace logging and automated evaluation in CI/CD pipelines using the RAG Triad metrics (contextual relevance, faithfulness, and answer relevance).

See [Scale RAG for production](/rag/production-scalability.md).

## Benefits of running RAG on Anyscale[​](#benefits "Direct link to Benefits of running RAG on Anyscale")

Anyscale provides a unified, enterprise platform, powered by Ray, to build, scale, and operate RAG systems from prototype to production. See [What is Anyscale?](/get-started/what-is-anyscale.md) and [What is Ray?](/get-started/what-is-ray.md).

### Key capabilities[​](#capabilities "Direct link to Key capabilities")

**Unified end-to-end platform**: Develop ingestion, retrieval, and generation on one platform. Anyscale manages Ray clusters, persistent logs, and observability so you don't have to stitch together ad-hoc infrastructure. See [Compute configuration on Anyscale](/configuration/compute.md).

**Production-grade LLM serving**: Anyscale Services combine Ray Serve (for orchestration, autoscaling, and canaries) with vLLM (for high-throughput, paged-attention inference). Get low-latency, streaming endpoints with OpenAI-compatible APIs that integrate with existing apps and SDKs. See [Serve LLMs with Anyscale services](/llm/serving.md).

**Scalable data ingestion and evaluation**: With Ray Data, parallelize extraction, cleaning, chunking, and embedding across elastic CPU/GPU clusters, turning hours into minutes at large scale. Run distributed batch evaluations (golden sets, retrieval sweeps, and prompt/reranker experiments) as first-class jobs. See [What is Ray Data?](/get-started/what-is-ray.md#ray-data).

**Enterprise security and governance**: Operate in your own cloud (BYOC) with private networking. Use role-based access controls, audit logs, cost tracking, and policy enforcement to keep proprietary data safe and access controlled. See [IAM on Anyscale](/iam.md), [Accessing logs](/monitoring/accessing-logs.md), and [Usage dashboard](/administration/billing/usage-dashboard.md).

**Cost-effective, reliable operations**: Elastic autoscaling adapts to spiky workloads. Batch clusters auto-suspend when idle. Spot instances and right-sizing keep unit economics tight without sacrificing SLOs. See [Worker nodes scaling config](/configuration/compute.md#scaling).

**Observability you can act on**: Managed dashboards surface per-stage latencies (embed, retrieve, rerank, and generate), token usage, and failure modes. These dashboards pinpoint bottlenecks across pipelines. See [Custom dashboards and alerting](/monitoring/custom-dashboards-and-alerting.md). For LLM serving metrics such as time to first token (TTFT), token throughput (TPS), and end-to-end request latency, enable the Ray Serve LLM dashboard. See <!-- -->\_<!-- -->.

### Value summary[​](#value-summary "Direct link to Value summary")

| Need                                            | Value that Anyscale brings                                     |
| ----------------------------------------------- | -------------------------------------------------------------- |
| Fast ingestion of thousands to millions of docs | Distributed Ray Data pipelines on elastic, managed clusters.   |
| Production LLM endpoints                        | Ray Serve and vLLM with streaming and OpenAI-compatible APIs.  |
| Enterprise posture                              | BYOC, private networking, access controls, auditability.       |
| Cost control                                    | Autoscaling, auto-suspend, and efficient use of spot capacity. |
| End-to-end visibility                           | Managed metrics and logs.                                      |

## Additional resources[​](#resources "Direct link to Additional resources")

The following are additional resources for learning about RAG on Anyscale:

* [Building Scalable RAG Pipelines with Ray and Anyscale](https://www.anyscale.com/blog/rag-pipelines-how-to)
* [Why RAG Breaks at Scale | Anyscale Webinar](https://www.youtube.com/watch?v=uTz7Jyunb98)
* [Building RAG-based LLM Applications for Production](https://www.anyscale.com/blog/a-comprehensive-guide-for-building-rag-based-llm-applications-part-1)
* [RAG at Scale: 10x Cheaper Embedding Computations with Anyscale and Pinecone](https://www.anyscale.com/blog/rag-at-scale-10x-cheaper-embedding-computations-with-anyscale-and-pinecone)
* [Building a RAG Batch Inference Pipeline with Anyscale and Union](https://www.anyscale.com/blog/anyscale-union-batch-inference-pipeline)
