# Hybrid Search Revamped - Building with Qdrant's Query API

Kacper Łukawski

·

July 25, 2024

![Hybrid Search Revamped - Building with Qdrant's Query API](https://qdrant.tech/articles_data/hybrid-search/preview/title.jpg)

It’s been over a year since we published the original article on how to build a hybrid
search system with Qdrant. The idea was straightforward: combine the results from different search methods to improve
retrieval quality. Back in 2023, you still needed to use an additional service to bring lexical search
capabilities and combine all the intermediate results. Things have changed since then. Once we introduced support for
sparse vectors, [the additional search service became obsolete](https://qdrant.tech/articles/sparse-vectors/), but you were still
required to combine the results from different methods on your end.

**Qdrant 1.10 introduces a new Query API that lets you build a search system by combining different search methods**
**to improve retrieval quality**. Everything is now done on the server side, and you can focus on building the best search
experience for your users. In this article, we will show you how to utilize the new [Query\\
API](https://qdrant.tech/documentation/concepts/search/#query-api) to build a hybrid search system.

## [Anchor](https://qdrant.tech/articles/hybrid-search/\#introducing-the-new-query-api) Introducing the new Query API

At Qdrant, we believe that vector search capabilities go well beyond a simple search for nearest neighbors.
That’s why we provided separate methods for different search use cases, such as `search`, `recommend`, or `discover`.
With the latest release, we are happy to introduce the new Query API, which combines all of these methods into a single
endpoint and also supports creating nested multistage queries that can be used to build complex search pipelines.

If you are an existing Qdrant user, you probably have a running search mechanism that you want to improve, whether sparse
or dense. Doing any changes should be preceded by a proper evaluation of its effectiveness.

## [Anchor](https://qdrant.tech/articles/hybrid-search/\#how-effective-is-your-search-system) How effective is your search system?

None of the experiments makes sense if you don’t measure the quality. How else would you compare which method works
better for your use case? The most common way of doing that is by using the standard metrics, such as `precision@k`,
`MRR`, or `NDCG`. There are existing libraries, such as [ranx](https://amenra.github.io/ranx/), that can help you with
that. We need to have the ground truth dataset to calculate any of these, but curating it is a separate task.

```python
from ranx import Qrels, Run, evaluate