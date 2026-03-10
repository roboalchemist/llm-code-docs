# [Anchor](https://qdrant.tech/benchmarks/filtered-search-intro/\#filtered-search-benchmark) Filtered search benchmark

Applying filters to search results brings a whole new level of complexity.
It is no longer enough to apply one algorithm to plain data. With filtering, it becomes a matter of the _cross-integration_ of the different indices.

To measure how well different search engines perform in this scenario, we have prepared a set of **Filtered ANN Benchmark Datasets** -
[https://github.com/qdrant/ann-filtering-benchmark-datasets](https://github.com/qdrant/ann-filtering-benchmark-datasets)

It is similar to the ones used in the [ann-benchmarks project](https://github.com/erikbern/ann-benchmarks/) but enriched with payload metadata and pre-generated filtering requests. It includes synthetic and real-world datasets with various filters, from keywords to geo-spatial queries.

### [Anchor](https://qdrant.tech/benchmarks/filtered-search-intro/\#why-filtering-is-not-trivial) Why filtering is not trivial?

Not many ANN algorithms are compatible with filtering.
HNSW is one of the few of them, but search engines approach its integration in different ways:

- Some use **post-filtering**, which applies filters after ANN search. It doesn’t scale well as it either loses results or requires many candidates on the first stage.
- Others use **pre-filtering**, which requires a binary mask of the whole dataset to be passed into the ANN algorithm. It is also not scalable, as the mask size grows linearly with the dataset size.

On top of it, there is also a problem with search accuracy.
It appears if too many vectors are filtered out, so the HNSW graph becomes disconnected.

Qdrant uses a different approach, not requiring pre- or post-filtering while addressing the accuracy problem.
Read more about the Qdrant approach in our [Filtrable HNSW](https://qdrant.tech/articles/filtrable-hnsw/) article.

Share this article

[x](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Ffiltered-search-intro%2F&text=Filtered%20search%20benchmark "x")[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Ffiltered-search-intro%2F "LinkedIn")

Up!

<|page-55-lllmstxt|>
## qdrant-internals
- [Articles](https://qdrant.tech/articles/)
- Qdrant Internals

#### Qdrant Internals

Take a look under the hood of Qdrant’s high-performance vector search engine. Explore the architecture, components, and design principles the Qdrant Vector Search Engine is built on.

[![Preview](https://qdrant.tech/articles_data/dedicated-vector-search/preview/preview.jpg)\\
**Built for Vector Search** \\
Why add-on vector search looks good — until you actually use it.\\
\\
Evgeniya Sukhodolskaya & Andrey Vasnetsov\\
\\
February 17, 2025](https://qdrant.tech/articles/dedicated-vector-search/)[![Preview](https://qdrant.tech/articles_data/gridstore-key-value-storage/preview/preview.jpg)\\
**Introducing Gridstore: Qdrant's Custom Key-Value Store** \\
Why and how we built our own key-value store. A short technical report on our procedure and results.\\
\\
Luis Cossio, Arnaud Gourlay & David Myriel\\
\\
February 05, 2025](https://qdrant.tech/articles/gridstore-key-value-storage/)[![Preview](https://qdrant.tech/articles_data/immutable-data-structures/preview/preview.jpg)\\
**Qdrant Internals: Immutable Data Structures** \\
Learn how immutable data structures improve vector search performance in Qdrant.\\
\\
Andrey Vasnetsov\\
\\
August 20, 2024](https://qdrant.tech/articles/immutable-data-structures/)[![Preview](https://qdrant.tech/articles_data/dedicated-service/preview/preview.jpg)\\
**Vector Search as a dedicated service** \\
Why vector search requires a dedicated service.\\
\\
Andrey Vasnetsov\\
\\
November 30, 2023](https://qdrant.tech/articles/dedicated-service/)[![Preview](https://qdrant.tech/articles_data/geo-polygon-filter-gsoc/preview/preview.jpg)\\
**Google Summer of Code 2023 - Polygon Geo Filter for Qdrant Vector Database** \\
A Summary of my work and experience at Qdrant's Gsoc '23.\\
\\
Zein Wen\\
\\
October 12, 2023](https://qdrant.tech/articles/geo-polygon-filter-gsoc/)[![Preview](https://qdrant.tech/articles_data/binary-quantization/preview/preview.jpg)\\
**Binary Quantization - Vector Search, 40x Faster** \\
Binary Quantization is a newly introduced mechanism of reducing the memory footprint and increasing performance\\
\\
Nirant Kasliwal\\
\\
September 18, 2023](https://qdrant.tech/articles/binary-quantization/)[![Preview](https://qdrant.tech/articles_data/io_uring/preview/preview.jpg)\\
**Qdrant under the hood: io\_uring** \\
Slow disk decelerating your Qdrant deployment? Get on top of IO overhead with this one trick!\\
\\
Andre Bogus\\
\\
June 21, 2023](https://qdrant.tech/articles/io_uring/)[![Preview](https://qdrant.tech/articles_data/product-quantization/preview/preview.jpg)\\
**Product Quantization in Vector Search \| Qdrant** \\
Discover product quantization in vector search technology. Learn how it optimizes storage and accelerates search processes for high-dimensional data.\\
\\
Kacper Łukawski\\
\\
May 30, 2023](https://qdrant.tech/articles/product-quantization/)[![Preview](https://qdrant.tech/articles_data/scalar-quantization/preview/preview.jpg)\\
**Scalar Quantization: Background, Practices & More \| Qdrant** \\
Discover the efficiency of scalar quantization for optimized data storage and enhanced performance. Learn about its data compression benefits and efficiency improvements.\\
\\
Kacper Łukawski\\
\\
March 27, 2023](https://qdrant.tech/articles/scalar-quantization/)[![Preview](https://qdrant.tech/articles_data/memory-consumption/preview/preview.jpg)\\
**Minimal RAM you need to serve a million vectors** \\
How to properly measure RAM usage and optimize Qdrant for memory consumption.\\
\\
Andrei Vasnetsov\\
\\
December 07, 2022](https://qdrant.tech/articles/memory-consumption/)[![Preview](https://qdrant.tech/articles_data/filtrable-hnsw/preview/preview.jpg)\\
**Filtrable HNSW** \\
How to make ANN search with custom filtering? Search in selected subsets without loosing the results.\\
\\
Andrei Vasnetsov\\
\\
November 24, 2019](https://qdrant.tech/articles/filtrable-hnsw/)

×

[Powered by](https://qdrant.tech/)

<|page-56-lllmstxt|>
## send-data
- [Documentation](https://qdrant.tech/documentation/)
- Send Data to Qdrant

## [Anchor](https://qdrant.tech/documentation/send-data/\#how-to-send-your-data-to-a-qdrant-cluster) How to Send Your Data to a Qdrant Cluster

| Example | Description | Stack |
| --- | --- | --- |
| [Pinecone to Qdrant Data Transfer](https://githubtocolab.com/qdrant/examples/blob/master/data-migration/from-pinecone-to-qdrant.ipynb) | Migrate your vector data from Pinecone to Qdrant. | Qdrant, Vector-io |
| [Stream Data to Qdrant with Kafka](https://qdrant.tech/documentation/send-data/data-streaming-kafka-qdrant/) | Use Confluent to Stream Data to Qdrant via Managed Kafka. | Qdrant, Kafka |
| [Qdrant on Databricks](https://qdrant.tech/documentation/send-data/databricks/) | Learn how to use Qdrant on Databricks using the Spark connector | Qdrant, Databricks, Apache Spark |
| [Qdrant with Airflow and Astronomer](https://qdrant.tech/documentation/send-data/qdrant-airflow-astronomer/) | Build a semantic querying system using Airflow and Astronomer | Qdrant, Airflow, Astronomer |

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/send-data/_index.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/send-data/_index.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-57-lllmstxt|>
## neural-search
- [Documentation](https://qdrant.tech/documentation/)
- [Beginner tutorials](https://qdrant.tech/documentation/beginner-tutorials/)
- Build a Neural Search Service