# Source: https://docs.anyscale.com/rag/quality-improvement.md

# RAG quality improvement strategies

[View Markdown](/rag/quality-improvement.md)

# RAG quality improvement strategies

This guide helps you identify and fix common failure modes in RAG systems across data ingestion, retrieval, and generation stages. Each section outlines specific challenges and practical strategies to address them.

For strategies to integrate RAG with structured data sources such as databases, CSVs, and spreadsheets, see [Integrating RAG with structured data](/rag/structured-data.md).

## Common RAG challenges[​](#common-challenges "Direct link to Common RAG challenges")

Optimizing a RAG system means tackling failures across the entire pipeline. The following are the most common challenges:

* **Data ingestion:**

  * **[Missing or stale content](/rag/quality-improvement/data-ingestion-strategies.md#missing-content)**: The knowledge base lacks the correct, up-to-date information to answer the query.
  * **[Poor OCR or challenging layouts](/rag/quality-improvement/data-ingestion-strategies.md#ocr-layouts)**: Text extraction from documents such as PDFs fails due to poor OCR quality or complex layouts such as tables and multi-column text, leading to garbled or incomplete content.
  * **[Suboptimal chunking](/rag/quality-improvement/data-ingestion-strategies.md#chunking)**: Documents are split in ways that break semantic context, making chunks hard to find or understand.
  * **[Semantic mismatch](/rag/quality-improvement/data-ingestion-strategies.md#semantic-mismatch)**: The embedding model doesn't understand your domain's specific vocabulary, such as internal acronyms or technical terms.
  * **[Schema drift and poor serialization](/rag/quality-improvement/data-ingestion-strategies.md#schema-drift)**: Structured sources change or are converted to text without preserving keys and headers, or with misaligned columns and rows, leading to gaps and downstream errors.

* **Retrieval:**

  * **[Misinterpreted user intent](/rag/quality-improvement/retrieval-strategies.md#user-intent)**: The system fails to understand vague, complex, or multi-part user queries.
  * **[Low precision or recall](/rag/quality-improvement/retrieval-strategies.md#precision-recall)**: The search misses relevant documents (low recall) or returns too many irrelevant ones (low precision).
  * **[Exact-match and relational lookups](/rag/quality-improvement/retrieval-strategies.md#exact-match-lookups)**: Vector-only retrieval misses IDs, dates, and numeric ranges, and can't express joins or multi-table filters.

* **Generation:**

  * **[Lost in the middle and context overload](/rag/quality-improvement/generation-strategies.md#lost-in-middle)**: The LLM ignores relevant information buried in the middle of a long context due to a U-shaped attention pattern, or too much retrieved noise distracts the LLM from the correct answer.
  * **[Missing the big picture](/rag/quality-improvement/generation-strategies.md#missing-big-picture)**: Retrieved chunks from semantic matching can be partial and miss important context, such as document headers or section metadata that provides crucial background information.
  * **[Hallucination and contradiction](/rag/quality-improvement/generation-strategies.md#hallucination)**: The LLM invents facts not in the context or fails to reconcile conflicting information from its sources.
  * **[Numerical reasoning and aggregation errors](/rag/quality-improvement/generation-strategies.md#numerical-errors)**: The LLM can't reliably compute sums, averages, or rankings from retrieved rows without external tools.
  * **[Format or extraction failure](/rag/quality-improvement/generation-strategies.md#wrong-format)**: The LLM finds the answer in the context but fails to extract it or presents it in the wrong format.

***

## A holistic, iterative approach[​](#iterative "Direct link to A holistic, iterative approach")

Optimizing a RAG system isn't a one-time fix. It's an iterative process of identifying and fixing bottlenecks. A failure at one stage (such as bad chunking) often manifests as a symptom at another stage (such as hallucination).

Start with a simple, robust baseline. Then, use a rigorous evaluation framework (measuring retrieval metrics such as Precision\@K and Recall\@K, and generation metrics such as Faithfulness) to test and measure the impact of each new optimization. Every advanced technique introduces a trade-off between performance, latency, and cost. Find the right balance for your specific application.

Ultimately, a robust, enterprise-grade system is often be a hybrid of these approaches, combining different retrieval and generation strategies for both unstructured and structured data. In this model, the LLM's role shifts from being an all-knowing oracle to an intelligent orchestrator that routes a user's query to the best tool, whether that's a vector search, a keyword filter, or a code-generating agent.

For detailed strategies to address these challenges, see the following guides:

* [Data ingestion strategies: building a quality foundation](/rag/quality-improvement/data-ingestion-strategies.md)
* [Retrieval strategies: Finding the right information](/rag/quality-improvement/retrieval-strategies.md)
* [Generation strategies: Ensuring accurate synthesis](/rag/quality-improvement/generation-strategies.md)
