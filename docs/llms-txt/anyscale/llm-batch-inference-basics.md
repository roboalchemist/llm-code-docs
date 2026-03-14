# Source: https://docs.anyscale.com/llm/batch-inference/llm-batch-inference-basics.md

# Understand LLM batch inference basics

[View Markdown](/llm/batch-inference/llm-batch-inference-basics.md)

# Understand LLM batch inference basics

This page explains what LLM batch inference is, when to use it, and the unique challenges it presents compared to traditional machine learning inference.

*LLM Batch inference* is the process of running an LLM over a fixed set of inputs, such as text files, images, or datasets, rather than serving individual requests interactively.

## Common use cases[​](#use-cases "Direct link to Common use cases")

LLM batch inference shows up in a variety of practical scenarios:

* **Automated summarization**: Long-form text such as reports, articles, or transcripts.
* **Bulk classification and moderation**: User-generated content filtering.
* **Structured data extraction**: Running prompts over millions of unstructured documents such as invoices, emails, or legal contracts to extract structured JSON or XML data.
* **Dataset labeling and augmentation**: Preparing data for downstream training tasks.
* **Offline evaluation**: Prompts, guardrails, or fine-tuned models at scale.
* **Embedding generation**: Generating embeddings for large document or image corpora for retrieval applications with Retrieval-Augmented Generation (RAG) or agents.

## Batch versus online inference[​](#batch-vs-online "Direct link to Batch versus online inference")

When running inference with LLMs, the first design choice is whether the workload is *batch (offline)* or *online (real-time)*. Both have different requirements, trade-offs, and performance goals. Batch inference processes large, fixed datasets efficiently. Online inference delivers fast responses to live user queries. Your use case determines infrastructure, scaling, and evaluation decisions.

* **Batch (offline)**: Process multiple records at once without immediate per-user responses. Throughput and cost efficiency matter more than single-request latency.
* **Online (real-time)**: Provide sub-second to seconds responses for chat or API use cases. Key metrics include Time to First Token (TTFT), Inter-Token Latency (ITL), Time Per Output Token (TPOT), and end-to-end latency. See [Understand LLM latency and throughput metrics](/llm/serving/benchmarking/metrics.md).

## Unique challenges of LLM batch inference[​](#challenges "Direct link to Unique challenges of LLM batch inference")

Batch inference for classic machine learning (for example, a ResNet model) is a relatively solved problem. However, the auto-regressive nature of LLMs introduces unique and significant challenges.

### Heterogeneous workloads[​](#heterogeneous-workloads "Direct link to Heterogeneous workloads")

In classic machine learning, the compute time for each input (for example, an image) is fixed and predictable. In LLMs, the total work for each request is variable and unknown upfront, as it depends on `prompt_tokens` and `generated_tokens`.

A dataset with thousands of long prompts and short outputs (such as summarization) has a completely different compute profile than one with short prompts and long outputs (such as content generation). This variability makes it difficult to pack batches efficiently without either wasting GPU memory or, more commonly, causing Out-of-Memory (OOM) errors.

### Bimodal compute (prefill vs. decode)[​](#bimodal-compute "Direct link to Bimodal compute (prefill vs. decode)")

LLM inference has two distinct operational phases:

* **Prefill**: Processing and computing the kv-cache for each of the input prompt tokens. These matrix-multiplication-heavy calculations can be done in parallel, so this phase is compute-bound. The latency of this stage directly contributes to Time to First Token (TTFT).

* **Decode**: Auto-regressively generating output tokens one at a time. This phase requires fast transfer of data (weights, KVs, activations) between the GPU and memory but less compute—and is therefore memory-bound. The latency of this stage directly determines Time Per Output Token (TPOT).

Keeping GPUs saturated and fully utilized across both phases requires smarter scheduling. Naive batching causes GPUs to idle during the decode phase. Optimized inference engines such as vLLM use techniques such as continuous batching and chunked prefill to enable more optimal utilization and throughput.

### CPU and GPU pipeline imbalance[​](#pipeline-imbalance "Direct link to CPU and GPU pipeline imbalance")

An LLM inference job is rarely just the model call. A production pipeline almost always involves CPU-heavy pre-processing and CPU-heavy post-processing:

* **Ingest and pre-process (CPU)**: Fetch data from a source (for example, S3, GCS, Azure Blob Storage, or a database) and apply prompt templating, truncation, or validation.
* **LLM inference (GPU)**: Model execution (prefill + decode phases).
* **Post-process and egress (CPU)**: Parse model outputs (for example, JSON), validate and enforce guardrails, write results back to storage.

If these steps are run sequentially on a GPU instance, the expensive accelerator sits idle for most of the job while the CPU handles I/O and data manipulation, leading to poor cost-efficiency.

### Dual scaling dimensions[​](#scaling-dimensions "Direct link to Dual scaling dimensions")

A production system must scale along two different axes:

* **Data parallelism**: How do you process a 10 TB dataset? You need to shard the data and distribute it across many model replicas.
* **Model parallelism**: How do you run a 70B+ model that doesn't fit on a single GPU? You need to use techniques such as tensor parallelism or pipeline parallelism to shard the model itself across multiple GPUs.

A robust batch inference system must handle both simultaneously—for example, distributing a 10 TB dataset across 50 replicas, where each replica is a 70B model running on four GPUs.

## Key requirements for a production system[​](#requirements "Direct link to Key requirements for a production system")

Given these challenges, a robust LLM batch inference system isn't just a script—it's an orchestration framework. When designing a pipeline, consider the following requirements:

* **Data-aware scheduling**: The system may stream datasets that are far larger than a single machine's memory, pulling data "just-in-time" from remote storage (for example, Amazon S3, Google Cloud Storage, or Azure Blob Storage) rather than requiring it all to be loaded upfront.
* **Hybrid resource orchestration**: The solution must be able to parallelize the CPU-bound preprocessing and post-processing steps and run them concurrently with the GPU-bound inference step. This ensures all resources (CPU, GPU, and network) are kept busy.
* **Efficient GPU scheduling**: The system must integrate with a modern inference engine such as vLLM that can handle heterogeneous workloads using techniques such as continuous batching and PagedAttention to maximize GPU utilization.
* **Scalability and fault tolerance**: The system must elastically scale to hundreds of nodes to meet demand and, critically, support graceful retries for failed batches. For a job that runs for 12 hours, a single failure shouldn't force the entire job to restart from scratch.

## How Ray Data LLM addresses these challenges[​](#ray-data-solution "Direct link to How Ray Data LLM addresses these challenges")

Ray Data provides a purpose-built framework for production LLM batch inference that directly addresses the challenges described above:

* **Dataset sharding**: Ray Data streams large datasets from remote storage such as Amazon S3, Google Cloud Storage, or Azure Blob Storage without loading everything into memory. The framework automatically shards datasets across multiple machines, enabling you to process terabyte-scale datasets that exceed any single node's capacity. This approach eliminates memory bottlenecks and enables horizontal scaling for massive inference jobs.
* **Automatic CPU and GPU orchestration**: Ray Data automatically parallelizes CPU preprocessing and post-processing across multiple nodes while concurrently running GPU inference. This keeps all resources busy and eliminates idle GPU time.
* **Native vLLM integration**: Ray Data integrates with vLLM out of the box through `ray.data.llm`, providing continuous batching, PagedAttention, and intelligent request scheduling to maximize GPU utilization.
* **Built-in fault tolerance**: Ray Data automatically handles failures and retries at the batch level. If a single batch fails in a 12-hour job, only that batch is retried rather than restarting the entire job from scratch.
* **Elastic scaling**: Ray Data scales from a single GPU to hundreds of nodes with minimal code changes. It handles both data parallelism (sharding datasets across replicas) and model parallelism (distributing large models across multiple GPUs) automatically.

## Next steps[​](#next-steps "Direct link to Next steps")

Batch inference is a critical pattern for operationalizing LLMs at scale. While it promises the highest throughput and lowest cost-per-token, its unique challenges—variable workloads, bimodal compute, and complex data pipelines—require a modern distributed computing framework.

A system that can elastically orchestrate hybrid CPU and GPU tasks, stream massive datasets, and intelligently schedule inference is no longer optional. It is essential for a production-ready, cost-efficient LLM application.

The next sections show how Ray Data simplifies these pipelines for LLM batch inference workloads (`ray.data.llm`) and explore the advantages of running batch inference on Anyscale, including throughput optimizations, cost savings, and production-ready features.
