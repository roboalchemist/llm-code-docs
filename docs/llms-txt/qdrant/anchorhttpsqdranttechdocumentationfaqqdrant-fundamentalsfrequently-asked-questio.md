# [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#frequently-asked-questions-general-topics) Frequently Asked Questions: General Topics

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [Vectors](https://qdrant.tech/documentation/faq/qdrant-fundamentals/#vectors) | [Search](https://qdrant.tech/documentation/faq/qdrant-fundamentals/#search) | [Collections](https://qdrant.tech/documentation/faq/qdrant-fundamentals/#collections) | [Compatibility](https://qdrant.tech/documentation/faq/qdrant-fundamentals/#compatibility) | [Cloud](https://qdrant.tech/documentation/faq/qdrant-fundamentals/#cloud) |

## [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#vectors) Vectors

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#what-is-the-maximum-vector-dimension-supported-by-qdrant) What is the maximum vector dimension supported by Qdrant?

Qdrant supports up to 65,535 dimensions by default, but this can be configured to support higher dimensions.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#what-is-the-maximum-size-of-vector-metadata-that-can-be-stored) What is the maximum size of vector metadata that can be stored?

There is no inherent limitation on metadata size, but it should be [optimized for performance and resource usage](https://qdrant.tech/documentation/guides/optimize/). Users can set upper limits in the configuration.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#can-the-same-similarity-search-query-yield-different-results-on-different-machines) Can the same similarity search query yield different results on different machines?

Yes, due to differences in hardware configurations and parallel processing, results may vary slightly.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#how-do-i-choose-the-right-vector-embeddings-for-my-use-case) How do I choose the right vector embeddings for my use case?

This depends on the nature of your data and the specific application. Consider factors like dimensionality, domain-specific models, and the performance characteristics of different embeddings.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#how-does-qdrant-handle-different-vector-embeddings-from-various-providers-in-the-same-collection) How does Qdrant handle different vector embeddings from various providers in the same collection?

Qdrant natively [supports multiple vectors per data point](https://qdrant.tech/documentation/concepts/vectors/#multivectors), allowing different embeddings from various providers to coexist within the same collection.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#can-i-migrate-my-embeddings-from-another-vector-store-to-qdrant) Can I migrate my embeddings from another vector store to Qdrant?

Yes, Qdrant supports migration of embeddings from other vector stores, facilitating easy transitions and adoption of Qdrant’s features.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#why-the-amount-of-indexed-vectors-doesnt-match-the-amount-of-vectors-in-the-collection) Why the amount of indexed vectors doesn’t match the amount of vectors in the collection?

Qdrant doesn’t always need to index all vectors in the collection.
It stores data is segments, and if the segment is small enough, it is more efficient to perform a full-scan search on it.

Make sure to check that the collection status is `green` and that the number of unindexed vectors smaller than indexing threshold.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#why-collection-info-shows-inaccurate-number-of-points) Why collection info shows inaccurate number of points?

Collection info API in Qdrant returns an approximate number of points in the collection.
If you need an exact number, you can use the [count](https://qdrant.tech/documentation/concepts/points/#counting-points) API.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#vectors-in-the-collection-dont-match-what-i-uploaded) Vectors in the collection don’t match what I uploaded.

There are two possible reasons for this:

- You used the `Cosine` distance metric in the [collection settings](https://qdrant.tech/concepts/collections/#collections). In this case, Qdrant pre-normalizes your vectors for faster distance computation. If you strictly need the original vectors to be preserved, consider using the `Dot` distance metric instead.
- You used the `uint8` [datatype](https://qdrant.tech/documentation/concepts/vectors/#datatypes) to store vectors. `uint8` requires a special format for input values, which might not be compatible with the typical output of embedding models.

## [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#search) Search

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#how-does-qdrant-handle-real-time-data-updates-and-search) How does Qdrant handle real-time data updates and search?

Qdrant supports live updates for vector data, with newly inserted, updated and deleted vectors available for immediate search. The system uses full-scan search on unindexed segments during background index updates.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#my-search-results-contain-vectors-with-null-values-why) My search results contain vectors with null values. Why?

By default, Qdrant tries to minimize network traffic and doesn’t return vectors in search results.
But you can force Qdrant to do so by setting the `with_vector` parameter of the Search/Scroll to `true`.

If you’re still seeing `"vector": null` in your results, it might be that the vector you’re passing is not in the correct format, or there’s an issue with how you’re calling the upsert method.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#how-can-i-search-without-a-vector) How can I search without a vector?

You are likely looking for the [scroll](https://qdrant.tech/documentation/concepts/points/#scroll-points) method. It allows you to retrieve the records based on filters or even iterate over all the records in the collection.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#does-qdrant-support-a-full-text-search-or-a-hybrid-search) Does Qdrant support a full-text search or a hybrid search?

Qdrant is a vector search engine in the first place, and we only implement full-text support as long as it doesn’t compromise the vector search use case.
That includes both the interface and the performance.

What Qdrant can do:

- Search with full-text filters
- Apply full-text filters to the vector search (i.e., perform vector search among the records with specific words or phrases)
- Do prefix search and semantic [search-as-you-type](https://qdrant.tech/articles/search-as-you-type/)
- Sparse vectors, as used in [SPLADE](https://github.com/naver/splade) or similar models
- [Multi-vectors](https://qdrant.tech/documentation/concepts/vectors/#multivectors), for example ColBERT and other late-interaction models
- Combination of the [multiple searches](https://qdrant.tech/documentation/concepts/hybrid-queries/)

What Qdrant doesn’t plan to support:

- Non-vector-based retrieval or ranking functions
- Built-in ontologies or knowledge graphs
- Query analyzers and other NLP tools

Of course, you can always combine Qdrant with any specialized tool you need, including full-text search engines.
Read more about [our approach](https://qdrant.tech/articles/hybrid-search/) to hybrid search.

## [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#collections) Collections

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#how-many-collections-can-i-create) How many collections can I create?

As many as you want, but be aware that each collection requires additional resources.
It is _highly_ recommended not to create many small collections, as it will lead to significant resource consumption overhead.

We consider creating a collection for each user/dialog/document as an antipattern.

Please read more about collections, isolation, and multiple users in our [Multitenancy](https://qdrant.tech/documentation/tutorials/multiple-partitions/) tutorial.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#how-do-i-upload-a-large-number-of-vectors-into-a-qdrant-collection) How do I upload a large number of vectors into a Qdrant collection?

Read about our recommendations in the [bulk upload](https://qdrant.tech/documentation/tutorials/bulk-upload/) tutorial.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#can-i-only-store-quantized-vectors-and-discard-full-precision-vectors) Can I only store quantized vectors and discard full precision vectors?

No, Qdrant requires full precision vectors for operations like reindexing, rescoring, etc.

## [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#compatibility) Compatibility

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#is-qdrant-compatible-with-cpus-or-gpus-for-vector-computation) Is Qdrant compatible with CPUs or GPUs for vector computation?

Qdrant primarily relies on CPU acceleration for scalability and efficiency. However, we also support GPU-accelerated indexing on all major vendors.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#do-you-guarantee-compatibility-across-versions) Do you guarantee compatibility across versions?

In case your version is older, we only guarantee compatibility between two consecutive minor versions. This also applies to client versions. Ensure your client version is never more than one minor version away from your cluster version.
While we will assist with break/fix troubleshooting of issues and errors specific to our products, Qdrant is not accountable for reviewing, writing (or rewriting), or debugging custom code.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#do-you-support-downgrades) Do you support downgrades?

We do not support downgrading a cluster on any of our products. If you deploy a newer version of Qdrant, your
data is automatically migrated to the newer storage format. This migration is not reversible.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#how-do-i-avoid-issues-when-updating-to-the-latest-version) How do I avoid issues when updating to the latest version?

We only guarantee compatibility if you update between consecutive versions. You would need to upgrade versions one at a time: `1.1 -> 1.2`, then `1.2 -> 1.3`, then `1.3 -> 1.4`.

## [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#cloud) Cloud

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#is-it-possible-to-scale-down-a-qdrant-cloud-cluster) Is it possible to scale down a Qdrant Cloud cluster?

Yes, it is possible to both vertically and horizontally scale down a Qdrant Cloud cluster.
Note, that during the vertical scaling down, the disk size cannot be reduced.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/faq/qdrant-fundamentals.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/faq/qdrant-fundamentals.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-120-lllmstxt|>
## embeddings
- [Documentation](https://qdrant.tech/documentation/)
- Embeddings