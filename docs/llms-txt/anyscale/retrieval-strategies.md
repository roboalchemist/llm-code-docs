# Source: https://docs.anyscale.com/rag/quality-improvement/retrieval-strategies.md

# Retrieval strategies: Finding the right information

[View Markdown](/rag/quality-improvement/retrieval-strategies.md)

# Retrieval strategies: Finding the right information

This page provides strategies to improve retrieval quality in your RAG system. You can learn how to handle user intent misinterpretation, improve precision and recall, and support exact-match and relational lookups.

For an overview of common RAG challenges, see [Common RAG challenges](/rag/quality-improvement.md#common-challenges).

## Misinterpreting user intent[​](#user-intent "Direct link to Misinterpreting user intent")

Users often ask vague, complex, or poorly worded questions. Taking this raw query and directly searching the vector database often leads to poor results.

**Strategies:**

* **Query rewriting and expansion**: Use an LLM to refine the user's query before retrieval. It can correct spelling, expand acronyms, clarify ambiguities, or add synonyms. Use a light-weight LLM to reduce the latency, and optimize with prompt engineering.
* **Multi-query retrieval**: Use an LLM to generate several different versions of the user's query from various perspectives. Run all these queries against your index and merge the results to get a more comprehensive set of documents.
* **Query decomposition**: For complex, multi-hop questions (such as "Compare the pros and cons of RAG and fine-tuning"), use an LLM to break the question into simpler, logical sub-queries. Retrieve answers for each sub-query and then synthesize a final answer.

## Low precision or recall (missed retrieval)[​](#precision-recall "Direct link to Low precision or recall (missed retrieval)")

Vector search excels at finding semantically similar documents but often fails to retrieve documents based on exact keywords (such as names, codes, or specific terms).

**Strategies:**

* **Hybrid search**: Combine semantic retrieval using an embedding datastore with traditional lexical, keyword-based retrieval approaches such as BM25. This captures documents that are both about the topic and contain the exact keywords.

* **Hypothetical Document Embeddings (HyDE)**: This technique addresses the mismatch between short queries and dense document chunks. Instead of embedding the user's query, you first use an LLM to generate a hypothetical answer to the query. Then, you embed this generated document and use its vector to perform the search. Drawbacks include high query-time latency and cost, as it requires an additional LLM call for generating the hypothetical answer. This makes it slow for real-time applications. Its performance also depends on the LLM's quality at that moment, risking "factual drift" if the generated answer is poor or doesn't match the real answer.

* **Reverse HyDE (Hypothetical Question Generation)**: This approach shifts the computational load to index time by generating multiple hypothetical questions for each document chunk and storing those question embeddings. Benefits include extremely fast query performance. With no LLM call at runtime, latency and per-query costs are minimal, making it ideal for high-volume, production-level applications. It also creates a strong question-to-question semantic match. Limitations include a very high upfront indexing cost and "index bloat," as the vector store becomes much larger. This approach is also critically dependent on the quality of the pre-generated questions. If they are poor, a document chunk can become permanently undiscoverable until a costly re-indexing is performed.

* **Reranking**: First-pass retrieval quickly narrows a large corpus to a candidate set (such as the top 50-100 documents), but this initial ranking doesn't always align with true relevance. Reranking uses a specialized model to reassess and reorder candidates, placing the most relevant items at the top. This improves the signal-to-noise ratio and reduces hallucinations. The following are three common reranking approaches:

  <!-- -->

  * **LLM-as-a-reranker**: Use LLMs with a listwise strategy. The input is the list of chunks, and the output is the ranked and filtered chunk IDs in JSON format. Use a smaller LLM or an LLM that's fine-tuned on ranking tasks to minimize latency. It works zero‑shot out of the box and doesn't require training a separate model; optional fine‑tuning can help.
  * **Cross-encoders**: Process the query and document together for deep, token-level comparison. This strategy is most accurate but computationally expensive. Some examples include BGE, Sentence-Transformers. These are typically supervised and trained on relevance labels. You can use an off‑the‑shelf reranker without training, or fine‑tune one on your domain for best results.
  * **Late-interaction models (ColBERT)**: ColBERT (Contextualized Late Interaction over BERT) balances the efficiency of traditional methods such as BM25 with the accuracy of deep learning models such as BERT. Unlike standard transformer-based retrievers that concatenate queries and documents into a single sequence, ColBERT uses late interaction: query and document embeddings are computed independently, and interaction happens during scoring rather than encoding. This allows pre-computation of document embeddings, making retrieval faster without significant accuracy loss. It's usually supervised and requires its own model (you can use a pre‑trained checkpoint). Domain fine‑tuning can further improve its quality.

* **Reciprocal Rank Fusion (RRF)**: When you use multiple retrievers (such as in hybrid search), you need a way to merge their ranked lists. RRF is a highly effective technique that combines results based on their rank rather than their absolute scores, making it robust and tuning-free. It's unsupervised and doesn't require training a separate model.

## Exact-match and relational lookups[​](#exact-match-lookups "Direct link to Exact-match and relational lookups")

Vector search excels at semantic similarity but struggles with precise lookups that require exact matches (such as IDs, dates, codes) or relational operations (such as "all orders from customer X in 2024" or "employees in department Y with salary > Z"). Pure vector embeddings blur these discrete values, making them hard to retrieve reliably.

**Strategies:**

* **Metadata filtering**: Store key structured fields (such as IDs, dates, categories, status codes, numeric ranges) as metadata in your vector store. Most vector databases support metadata filters that let you combine semantic search with exact predicates. For example, "Find documents semantically similar to 'quarterly earnings' WHERE date >= '2024-01-01' AND department = 'Finance'". This hybrid approach gives you both semantic relevance and precise filtering.
* **Hybrid retrieval with keyword search**: Combine vector search with traditional keyword or BM25 search. Keyword search handles exact string matches better than embeddings. Use filters or boosting to prioritize documents containing the exact ID, code, or term the user specified. Merge the results using techniques such as Reciprocal Rank Fusion (RRF).
* **Entity extraction and lookup routing**: Before retrieval, use Named Entity Recognition (NER) or regular expressions to detect entities in the user's query (such as customer IDs, order numbers, dates). Route queries with detected entities to structured lookups (such as database queries or metadata filters) instead of relying solely on semantic search. This ensures precision for fact-based questions.
* **SQL generation for structured queries**: For complex relational questions that involve joins, aggregations, or multi-table filters, translate the natural language query into SQL using an LLM. Execute the SQL query against your database to get precise results. This is especially effective when your knowledge base includes relational databases or data warehouses. See [Integrating RAG with structured data](/rag/structured-data.md) for implementation details.
* **Dual-index strategy**: Maintain two separate indexes: one vector index for unstructured documents and semantic search, and one structured index (such as a SQL database or Elasticsearch) for precise lookups. Use a query classifier or router to decide which index to query based on the question type. For example, "What's our refund policy?" goes to the vector index, while "Show me order #12345" goes to the structured index.
* **Store structured data in retrievable format**: When embedding structured data, preserve its relational structure in a way that's recoverable after retrieval. For example, instead of embedding a flattened table row, embed each table with its full schema and primary/foreign keys as metadata. After retrieval, the LLM can reason about relationships between retrieved chunks.
* **Use graph databases for relational knowledge**: For knowledge bases with rich entity relationships (such as knowledge graphs, organizational hierarchies, or product catalogs), consider using graph databases (such as Neo4j) alongside your vector store. Graph queries can traverse relationships (such as "Find all projects connected to this customer through vendor relationships") that are difficult to express in vector or SQL alone.
