# [Anchor](https://qdrant.tech/documentation/guides/capacity-planning/\#capacity-planning) Capacity Planning

When setting up your cluster, you’ll need to figure out the right balance of **RAM** and **disk storage**. The best setup depends on a few things:

- How many vectors you have and their dimensions.
- The amount of payload data you’re using and their indexes.
- What data you want to store in memory versus on disk.
- Your cluster’s replication settings.
- Whether you’re using quantization and how you’ve set it up.

## [Anchor](https://qdrant.tech/documentation/guides/capacity-planning/\#calculating-ram-size) Calculating RAM size

You should store frequently accessed data in RAM for faster retrieval. If you want to keep all vectors in memory for optimal performance, you can use this rough formula for estimation:

```text
memory_size = number_of_vectors * vector_dimension * 4 bytes * 1.5

```

At the end, we multiply everything by 1.5. This extra 50% accounts for metadata (such as indexes and point versions) and temporary segments created during optimization.

Let’s say you want to store 1 million vectors with 1024 dimensions:

```text
memory_size = 1,000,000 * 1024 * 4 bytes * 1.5

```

The memory\_size is approximately 6,144,000,000 bytes, or about 5.72 GB.

Depending on the use case, large datasets can benefit from reduced memory requirements via [quantization](https://qdrant.tech/documentation/guides/quantization/).

## [Anchor](https://qdrant.tech/documentation/guides/capacity-planning/\#calculating-payload-size) Calculating payload size

This is always different. The size of the payload depends on the [structure and content of your data](https://qdrant.tech/documentation/concepts/payload/#payload-types). For instance:

- **Text fields** consume space based on length and encoding (e.g. a large chunk of text vs a few words).
- **Floats** have fixed sizes of 8 bytes for `int64` or `float64`.
- **Boolean fields** typically consume 1 byte.

Calculating total payload size is similar to vectors. We have to multiply it by 1.5 for back-end indexing processes.

```text
total_payload_size = number_of_points * payload_size * 1.5

```

Let’s say you want to store 1 million points with JSON payloads of 5KB:

```text
total_payload_size = 1,000,000 * 5KB * 1.5

```

The total\_payload\_size is approximately 5,000,000 bytes, or about 4.77 GB.

## [Anchor](https://qdrant.tech/documentation/guides/capacity-planning/\#choosing-disk-over-ram) Choosing disk over RAM

For optimal performance, you should store only frequently accessed data in RAM. The rest should be offloaded to the disk. For example, extra payload fields that you don’t use for filtering can be stored on disk.

Only [indexed fields](https://qdrant.tech/documentation/concepts/indexing/#payload-index) should be stored in RAM. You can read more about payload storage in the [Storage](https://qdrant.tech/documentation/concepts/storage/#payload-storage) section.

### [Anchor](https://qdrant.tech/documentation/guides/capacity-planning/\#storage-focused-configuration) Storage-focused configuration

If your priority is to handle large volumes of vectors with average search latency, it’s recommended to configure [memory-mapped (mmap) storage](https://qdrant.tech/documentation/concepts/storage/#configuring-memmap-storage). In this setup, vectors are stored on disk in memory-mapped files, while only the most frequently accessed vectors are cached in RAM.

The amount of available RAM greatly impacts search performance. As a general rule, if you store half as many vectors in RAM, search latency will roughly double.

Disk speed is also crucial. [Contact us](https://qdrant.tech/documentation/support/) if you have specific requirements for high-volume searches in our Cloud.

### [Anchor](https://qdrant.tech/documentation/guides/capacity-planning/\#subgroup-oriented-configuration) Subgroup-oriented configuration

If your use case involves splitting vectors into multiple collections or subgroups based on payload values (e.g., serving searches for multiple users, each with their own subset of vectors), memory-mapped storage is recommended.

In this scenario, only the active subset of vectors will be cached in RAM, allowing for fast searches for the most recent and active users. You can estimate the required memory size as:

```text
memory_size = number_of_active_vectors * vector_dimension * 4 bytes * 1.5

```

Please refer to our [multitenancy](https://qdrant.tech/documentation/guides/multiple-partitions/) documentation for more details on partitioning data in a Qdrant.

## [Anchor](https://qdrant.tech/documentation/guides/capacity-planning/\#scaling-disk-space-in-qdrant-cloud) Scaling disk space in Qdrant Cloud

Clusters supporting vector search require substantial disk space compared to other search systems. If you’re running low on disk space, you can use the UI at [cloud.qdrant.io](https://cloud.qdrant.io/) to **Scale Up** your cluster.

When running low on disk space, consider the following benefits of scaling up:

- **Larger Datasets**: Supports larger datasets, which can improve the relevance and quality of search results.
- **Improved Indexing**: Enables the use of advanced indexing strategies like HNSW.
- **Caching**: Enhances speed by having more RAM, allowing more frequently accessed data to be cached.
- **Backups and Redundancy**: Facilitates more frequent backups, which is a key advantage for data safety.

Always remember to add 50% of the vector size. This would account for things like indexes and auxiliary data used during operations such as vector insertion, deletion, and search. Thus, the estimated memory size including metadata is:

```text
total_vector_size = number_of_dimensions * 4 bytes * 1.5

```

**Disclaimer**

The above calculations are estimates at best. If you’re looking for more accurate numbers, you should always test your data set in practice.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/capacity-planning.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/capacity-planning.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-52-lllmstxt|>
## machine-learning
- [Articles](https://qdrant.tech/articles/)
- Machine Learning

#### Machine Learning

Explore Machine Learning principles and practices which make modern semantic similarity search possible. Apply Qdrant and vector search capabilities to your ML projects.

[![Preview](https://qdrant.tech/articles_data/minicoil/preview/preview.jpg)\\
**miniCOIL: on the Road to Usable Sparse Neural Retrieval** \\
Introducing miniCOIL, a lightweight sparse neural retriever capable of generalization.\\
\\
Evgeniya Sukhodolskaya\\
\\
May 13, 2025](https://qdrant.tech/articles/minicoil/)[![Preview](https://qdrant.tech/articles_data/search-feedback-loop/preview/preview.jpg)\\
**Relevance Feedback in Informational Retrieval** \\
Relerance feedback: from ancient history to LLMs. Why relevance feedback techniques are good on paper but not popular in neural search, and what we can do about it.\\
\\
Evgeniya Sukhodolskaya\\
\\
March 27, 2025](https://qdrant.tech/articles/search-feedback-loop/)[![Preview](https://qdrant.tech/articles_data/modern-sparse-neural-retrieval/preview/preview.jpg)\\
**Modern Sparse Neural Retrieval: From Theory to Practice** \\
A comprehensive guide to modern sparse neural retrievers: COIL, TILDEv2, SPLADE, and more. Find out how they work and learn how to use them effectively.\\
\\
Evgeniya Sukhodolskaya\\
\\
October 23, 2024](https://qdrant.tech/articles/modern-sparse-neural-retrieval/)[![Preview](https://qdrant.tech/articles_data/cross-encoder-integration-gsoc/preview/preview.jpg)\\
**Qdrant Summer of Code 2024 - ONNX Cross Encoders in Python** \\
A summary of my work and experience at Qdrant Summer of Code 2024.\\
\\
Huong (Celine) Hoang\\
\\
October 14, 2024](https://qdrant.tech/articles/cross-encoder-integration-gsoc/)[![Preview](https://qdrant.tech/articles_data/late-interaction-models/preview/preview.jpg)\\
**Any\* Embedding Model Can Become a Late Interaction Model... If You Give It a Chance!** \\
We recently discovered that embedding models can become late interaction models & can perform surprisingly well in some scenarios. See what we learned here.\\
\\
Kacper Łukawski\\
\\
August 14, 2024](https://qdrant.tech/articles/late-interaction-models/)[![Preview](https://qdrant.tech/articles_data/bm42/preview/preview.jpg)\\
**BM42: New Baseline for Hybrid Search** \\
Introducing BM42 - a new sparse embedding approach, which combines the benefits of exact keyword search with the intelligence of transformers.\\
\\
Andrey Vasnetsov\\
\\
July 01, 2024](https://qdrant.tech/articles/bm42/)[![Preview](https://qdrant.tech/articles_data/embedding-recycling/preview/preview.jpg)\\
**Layer Recycling and Fine-tuning Efficiency** \\
Learn when and how to use layer recycling to achieve different performance targets.\\
\\
Yusuf Sarıgöz\\
\\
August 23, 2022](https://qdrant.tech/articles/embedding-recycler/)[![Preview](https://qdrant.tech/articles_data/cars-recognition/preview/preview.jpg)\\
**Fine Tuning Similar Cars Search** \\
Learn how to train a similarity model that can retrieve similar car images in novel categories.\\
\\
Yusuf Sarıgöz\\
\\
June 28, 2022](https://qdrant.tech/articles/cars-recognition/)[![Preview](https://qdrant.tech/articles_data/detecting-coffee-anomalies/preview/preview.jpg)\\
**Metric Learning for Anomaly Detection** \\
Practical use of metric learning for anomaly detection. A way to match the results of a classification-based approach with only ~0.6% of the labeled data.\\
\\
Yusuf Sarıgöz\\
\\
May 04, 2022](https://qdrant.tech/articles/detecting-coffee-anomalies/)[![Preview](https://qdrant.tech/articles_data/triplet-loss/preview/preview.jpg)\\
**Triplet Loss - Advanced Intro** \\
What are the advantages of Triplet Loss over Contrastive loss and how to efficiently implement it?\\
\\
Yusuf Sarıgöz\\
\\
March 24, 2022](https://qdrant.tech/articles/triplet-loss/)[![Preview](https://qdrant.tech/articles_data/metric-learning-tips/preview/preview.jpg)\\
**Metric Learning Tips & Tricks** \\
Practical recommendations on how to train a matching model and serve it in production. Even with no labeled data.\\
\\
Andrei Vasnetsov\\
\\
May 15, 2021](https://qdrant.tech/articles/metric-learning-tips/)

×

[Powered by](https://qdrant.tech/)

<|page-53-lllmstxt|>
## support
- [Documentation](https://qdrant.tech/documentation/)
- Support