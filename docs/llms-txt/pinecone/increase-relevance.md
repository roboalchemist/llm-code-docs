# Source: https://docs.pinecone.io/guides/optimize/increase-relevance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Increase search relevance

> Learn techniques to improve search result quality.

This page describes helpful techniques for improving search accuracy and relevance.

## Rerank results

[Reranking](/guides/search/rerank-results) is used as part of a two-stage vector retrieval process to improve the quality of results. You first query an index for a given number of relevant results, and then you send the query and results to a reranking model. The reranking model scores the results based on their semantic relevance to the query and returns a new, more accurate ranking. This approach is one of the simplest methods for improving quality in retrieval augmented generation (RAG) pipelines.

Pinecone provides [hosted reranking models](/guides/search/rerank-results#reranking-models) so it's easy to manage two-stage vector retrieval on a single platform. You can use a hosted model to rerank results as an integrated part of a query, or you can use a hosted model to rerank results as a standalone operation.

## Filter by metadata

Every [record](/guides/get-started/concepts#record) in an index must contain an ID and a dense or sparse vector, depending on the [type of index](/guides/index-data/indexing-overview#indexes). In addition, you can include metadata key-value pairs to store related information or context. When you search the index, you can then include a metadata filter to limit the search to records matching a filter expression.

For example, if an index contains records about books, you could use a metadata field to associate each record with a genre, like `"genre": "fiction"` or `"genre": "poetry"`. When you query the index, you could then use a metadata filter to limit your search to records related to a specific genre.

For more details, see [Filter by metadata](/guides/search/filter-by-metadata).

## Use hybrid search

[Semantic search](/guides/search/semantic-search) and [lexical search](/guides/search/lexical-search) are powerful information retrieval techniques, but each has notable limitations. For example, semantic search can miss results based on exact keyword matches, especially in scenarios involving domain-specific terminology, while lexical search can miss results based on relationships, such as synonyms and paraphrases.

To work around these limitations, you can perform hybrid search, which combines semantic and lexical search. There are two ways to do this:

* [Use a single hybrid index](/guides/search/hybrid-search#use-a-single-hybrid-index). This is the **recommended** approach for most use cases because you make requests to a single index, the linkage between dense and sparse vectors is implicit, and you can perform hybrid queries with a single request.
* [Use separate dense and sparse indexes](/guides/search/hybrid-search#use-separate-dense-and-sparse-indexes). This approach provides more flexibility but requires managing two indexes, maintaining linkages between vectors, and querying each index separately before merging results.

For more details, including guidance on choosing the right approach, see [Hybrid search](/guides/search/hybrid-search).

## Explore chunking strategies

You can chunk your content in different ways to get better results. Consider factors like the length of the content, the complexity of queries, and how results will be used in your application.

For more details, see [Chunking strategies](https://www.pinecone.io/learn/chunking-strategies/).
