# Source: https://code.kx.com/kdbai/latest/reference/reranking.html

Title: About reranking in KDB.AI - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/reference/reranking.html

Markdown Content:
_This page explains the concepts of reranking, bi-encoders, cross-encoders and reranker models._

If you're already familiar with this topic, you can skip ahead to the [How-to guide](https://code.kx.com/kdbai/latest/use/rerank.html).

Reranking is the process of reordering an initial set of search results to enhance their relevance and accuracy. Vector databases use this technique to refine the results retrieved based on vector similarity.

Why is reranking important?

Benefits of reranking include:

*   **Enhanced Relevance:** Rerankers leverage advanced natural language processing to deeply understand the intent behind queries. This ensures that the results are not just relevant but precisely what the user needs, significantly improving the overall relevance of search outcomes. 
*   **Handling Complex Queries:** Rerankers are particularly useful for complex or ambiguous queries. They excel in capturing the specific nuances and context that might be missed during the initial - retrieval stage, providing more accurate and contextually appropriate results. 
*   **Optimization for Specific Metrics:** Different applications may require optimization for specific metrics beyond simple relevance. Rerankers can adjust the rankings according to these business-specific metrics, ensuring that the search results align with the unique goals and requirements of the application. 
*   **Improved Search Results:** Reranking improves precision and recall, leveraging deep semantic understanding to capture subtle nuances. Reranking refines initial search results to provide users with the most accurate and relevant information, thereby greatly enhancing the search experience and satisfaction.

Key Concepts
------------

Before delving into the technical details of reranking with KDB.AI, let's explore a few key topics:

*   [Two-stage retrieval process](https://code.kx.com/kdbai/latest/reference/reranking.html#two-stage-retrieval-process)
*   [Bi-encoders vs. cross-encoders](https://code.kx.com/kdbai/latest/reference/reranking.html#bi-encoders-vs-cross-encoders)
*   [Reranker models](https://code.kx.com/kdbai/latest/reference/reranking.html#reranker-models)

### Two-stage retrieval process

The two-stage retrieval process involves an **initial retrieval phase** that employs a quick and scalable method, like bi-encoder models, to gather a broad set of candidate documents. This is followed by a **reranking phase**, where a more sophisticated model, often a cross-encoder, reorders these candidates based on their relevance to the query. This approach balances efficiency and accuracy, ensuring that the most relevant documents are prioritized.

### Bi-encoders vs. cross-encoders

Bi-encoders and Cross-encoders are two distinct approaches used in information retrieval and natural language processing to compute similarity scores between queries and documents.

#### Bi-encoders

Bi-encoders independently process the query and the document to generate embeddings, which are then compared using metrics like cosine similarity. This approach is highly efficient, enabling the rapid retrieval of relevant documents. However, because bi-encoders generate embeddings without considering the specific query context, there can be some information loss, potentially limiting accuracy.

Use Cases:

*   Initial retrieval stage in search engines
*   Semantic search
*   Clustering

#### Cross-encoders

Cross-encoders, on the other hand, take both the query and the candidate documents as input simultaneously to compute a similarity score. This approach reduces information loss by deeply analyzing the relationship between the query and the documents, leading to improved performance and relevance in search results. Cross-encoders are typically used to reorder the top-k results from the initial retrieval stage, enhancing overall retrieval performance.

Use Cases:

*   Re-ranking in search engines
*   Fine-tuning for specific tasks requiring high accuracy

#### Combined workflow

In many retrieval systems, bi-encoders are used in the initial stage to quickly narrow down the pool of candidate documents. These candidates are then re-ranked using cross-encoders to provide more accurate and context-aware results. This combination leverages the efficiency of bi-encoders and the precision of cross-encoders.

### Reranker models

A reranker model uses a cross-encoder to rerank documents based on a similarity score derived from both the query and the documents. This process leverages advanced natural language processing to deeply understand the intent behind queries, ensuring that the results are not just relevant but precisely what the user needs. Rerankers are helpful when handling complex or ambiguous queries where the initial retrieval might miss specific nuances.

KDB.AI supports the following reranking models:

#### Cohere

Cohere’s reranking models are designed to enhance the relevance of search results by reordering them based on semantic relevance to a query. These models are particularly useful in retrieval-augmented generation (RAG) systems. They work by taking an initial set of search results, which could be from a keyword-based or semantic search system, and re-rank them to better match your query. Cohere offers models like `rerank-english-v3.0` and `rerank-multilingual-v3.0` that support multiple languages and can handle long texts up to 4096 tokens.

#### Jina AI

Jina AI’s reranking models focus on improving search relevancy and retrieval accuracy for both structured and unstructured data. The `Jina Reranker v2` is a transformer-based model that takes a query and a document as an input pair and outputs a relevance score. This model covers multilingual retrieval, function-calling, and code search, making it versatile for various applications.

#### Voyage AI

Voyage AI’s reranking models are cross-encoders that process query-document pairs to predict relevance more accurately. The `rerank-2` and `rerank-2-lite` models are optimized for quality and latency, respectively. These rerankers support multilingual queries and large context lengths, making them suitable for complex search tasks. Voyage AI’s reranking models refine the initial search results from embedding-based retrieval systems, providing more precise and contextually relevant results.

### Next steps

*   Learn how to [use rerankers](https://code.kx.com/kdbai/latest/use/rerank.html) in KDB.AI. 
*   Read our Jina AI-related blog article, [The end of high dimensions](https://kx.com/blog/end-high-dimensions-ai-search/), to discover how Matryoshka learning is revolutionizing AI search.
