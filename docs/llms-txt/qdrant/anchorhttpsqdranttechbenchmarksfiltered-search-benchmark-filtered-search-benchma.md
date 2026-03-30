# [Anchor](https://qdrant.tech/benchmarks/\#filtered-search-benchmark) Filtered search benchmark

Applying filters to search results brings a whole new level of complexity.
It is no longer enough to apply one algorithm to plain data. With filtering, it becomes a matter of the _cross-integration_ of the different indices.

To measure how well different search engines perform in this scenario, we have prepared a set of **Filtered ANN Benchmark Datasets** -
[https://github.com/qdrant/ann-filtering-benchmark-datasets](https://github.com/qdrant/ann-filtering-benchmark-datasets)

It is similar to the ones used in the [ann-benchmarks project](https://github.com/erikbern/ann-benchmarks/) but enriched with payload metadata and pre-generated filtering requests. It includes synthetic and real-world datasets with various filters, from keywords to geo-spatial queries.

### [Anchor](https://qdrant.tech/benchmarks/\#why-filtering-is-not-trivial) Why filtering is not trivial?

Not many ANN algorithms are compatible with filtering.
HNSW is one of the few of them, but search engines approach its integration in different ways:

- Some use **post-filtering**, which applies filters after ANN search. It doesn’t scale well as it either loses results or requires many candidates on the first stage.
- Others use **pre-filtering**, which requires a binary mask of the whole dataset to be passed into the ANN algorithm. It is also not scalable, as the mask size grows linearly with the dataset size.

On top of it, there is also a problem with search accuracy.
It appears if too many vectors are filtered out, so the HNSW graph becomes disconnected.

Qdrant uses a different approach, not requiring pre- or post-filtering while addressing the accuracy problem.
Read more about the Qdrant approach in our [Filtrable HNSW](https://qdrant.tech/articles/filtrable-hnsw/) article.

## [Anchor](https://qdrant.tech/benchmarks/\#)

**Updated: Feb 2023**

Dataset:keyword-100range-100int-2048100-kw-small-vocabkeyword-2048geo-radius-100range-2048geo-radius-2048int-100h-and-m-2048arxiv-titles-384

Plot values:

Regular search

Filter search

_Download raw data: [here](https://qdrant.tech/benchmarks/filter-result-2023-02-03.json)_

## [Anchor](https://qdrant.tech/benchmarks/\#filtered-results) Filtered Results

As you can see from the charts, there are three main patterns:

- **Speed boost** \- for some engines/queries, the filtered search is faster than the unfiltered one. It might happen if the filter is restrictive enough, to completely avoid the usage of the vector index.

- **Speed downturn** \- some engines struggle to keep high RPS, it might be related to the requirement of building a filtering mask for the dataset, as described above.

- **Accuracy collapse** \- some engines are loosing accuracy dramatically under some filters. It is related to the fact that the HNSW graph becomes disconnected, and the search becomes unreliable.


Qdrant avoids all these problems and also benefits from the speed boost, as it implements an advanced [query planning strategy](https://qdrant.tech/documentation/search/#query-planning).