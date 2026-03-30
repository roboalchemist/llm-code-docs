# Calculating the NDCG@5 metric is as simple as that
evaluate(qrels, run, "ndcg@5")

```

## [Anchor](https://qdrant.tech/articles/hybrid-search/\#available-embedding-options-with-query-api) Available embedding options with Query API

Support for multiple vectors per point is nothing new in Qdrant, but introducing the Query API makes it even
more powerful. The 1.10 release supports the multivectors, allowing you to treat embedding lists
as a single entity. There are many possible ways of utilizing this feature, and the most prominent one is the support
for late interaction models, such as [ColBERT](https://qdrant.tech/documentation/fastembed/fastembed-colbert/). Instead of having a single embedding for each document or query, this
family of models creates a separate one for each token of text. In the search process, the final score is calculated
based on the interaction between the tokens of the query and the document. Contrary to cross-encoders, document
embedding might be precomputed and stored in the database, which makes the search process much faster. If you are
curious about the details, please check out [the article about ColBERT, written by our friends from Jina\\
AI](https://jina.ai/news/what-is-colbert-and-late-interaction-and-why-they-matter-in-search/).

![Late interaction](https://qdrant.tech/articles_data/hybrid-search/late-interaction.png)

Besides multivectors, you can use regular dense and sparse vectors, and experiment with smaller data types to reduce
memory use. Named vectors can help you store different dimensionalities of the embeddings, which is useful if you
use multiple models to represent your data, or want to utilize the Matryoshka embeddings.

![Multiple vectors per point](https://qdrant.tech/articles_data/hybrid-search/multiple-vectors.png)

There is no single way of building a hybrid search. The process of designing it is an exploratory exercise, where you
need to test various setups and measure their effectiveness. Building a proper search experience is a
complex task, and it’s better to keep it data-driven, not just rely on the intuition.

## [Anchor](https://qdrant.tech/articles/hybrid-search/\#fusion-vs-reranking) Fusion vs reranking

We can, distinguish two main approaches to building a hybrid search system: fusion and reranking. The former is about
combining the results from different search methods, based solely on the scores returned by each method. That usually
involves some normalization, as the scores returned by different methods might be in different ranges. After that, there
is a formula that takes the relevancy measures and calculates the final score that we use later on to reorder the
documents. Qdrant has built-in support for the Reciprocal Rank Fusion method, which is the de facto standard in the
field.

![Fusion](https://qdrant.tech/articles_data/hybrid-search/fusion.png)

Reranking, on the other hand, is about taking the results from different search methods and reordering them based on
some additional processing using the content of the documents, not just the scores. This processing may rely on an
additional neural model, such as a cross-encoder which would be inefficient enough to be used on the whole dataset.
These methods are practically applicable only when used on a smaller subset of candidates returned by the faster search
methods. Late interaction models, such as ColBERT, are way more efficient in this case, as they can be used to rerank
the candidates without the need to access all the documents in the collection.

![Reranking](https://qdrant.tech/articles_data/hybrid-search/reranking.png)

### [Anchor](https://qdrant.tech/articles/hybrid-search/\#why-not-a-linear-combination) Why not a linear combination?

It’s often proposed to use full-text and vector search scores to form a linear combination formula to rerank
the results. So it goes like this:

`final_score = 0.7 * vector_score + 0.3 * full_text_score`

However, we didn’t even consider such a setup. Why? Those scores don’t make the problem linearly separable. We used
the BM25 score along with cosine vector similarity to use both of them as points coordinates in 2-dimensional space. The
chart shows how those points are distributed:

![A distribution of both Qdrant and BM25 scores mapped into 2D space.](https://qdrant.tech/articles_data/hybrid-search/linear-combination.png)

_A distribution of both Qdrant and BM25 scores mapped into 2D space. It clearly shows relevant and non-relevant_
_objects are not linearly separable in that space, so using a linear combination of both scores won’t give us_
_a proper hybrid search._

Both relevant and non-relevant items are mixed. **None of the linear formulas would be able to distinguish**
**between them.** Thus, that’s not the way to solve it.

## [Anchor](https://qdrant.tech/articles/hybrid-search/\#building-a-hybrid-search-system-in-qdrant) Building a hybrid search system in Qdrant

Ultimately, **any search mechanism might also be a reranking mechanism**. You can prefetch results with sparse vectors
and then rerank them with the dense ones, or the other way around. Or, if you have Matryoshka embeddings, you can start
with oversampling the candidates with the dense vectors of the lowest dimensionality and then gradually reduce the
number of candidates by reranking them with the higher-dimensional embeddings. Nothing stops you from
combining both fusion and reranking.

Let’s go a step further and build a hybrid search mechanism that combines the results from the
Matryoshka embeddings, dense vectors, and sparse vectors and then reranks them with the late interaction model. In the
meantime, we will introduce additional reranking and fusion steps.

![Complex search pipeline](https://qdrant.tech/articles_data/hybrid-search/complex-search-pipeline.png)

Our search pipeline consists of two branches, each of them responsible for retrieving a subset of documents that
we eventually want to rerank with the late interaction model. Let’s connect to Qdrant first and then build the search
pipeline.

```python
from qdrant_client import QdrantClient, models

client = QdrantClient("http://localhost:6333")

```

All the steps utilizing Matryoshka embeddings might be specified in the Query API as a nested structure:

```python