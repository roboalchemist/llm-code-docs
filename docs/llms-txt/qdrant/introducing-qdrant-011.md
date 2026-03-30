# Introducing Qdrant 0.11

Kacper Łukawski

·

October 26, 2022

![Introducing Qdrant 0.11](https://qdrant.tech/articles_data/qdrant-0-11-release/preview/title.jpg)

We are excited to [announce the release of Qdrant v0.11](https://github.com/qdrant/qdrant/releases/tag/v0.11.0),
which introduces a number of new features and improvements.

## [Anchor](https://qdrant.tech/articles/qdrant-0-11-release/\#replication) Replication

One of the key features in this release is replication support, which allows Qdrant to provide a high availability
setup with distributed deployment out of the box. This, combined with sharding, enables you to horizontally scale
both the size of your collections and the throughput of your cluster. This means that you can use Qdrant to handle
large amounts of data without sacrificing performance or reliability.

## [Anchor](https://qdrant.tech/articles/qdrant-0-11-release/\#administration-api) Administration API

Another new feature is the administration API, which allows you to disable write operations to the service. This is
useful in situations where search availability is more critical than updates, and can help prevent issues like memory
usage watermarks from affecting your searches.

## [Anchor](https://qdrant.tech/articles/qdrant-0-11-release/\#exact-search) Exact search

We have also added the ability to report indexed payload points in the info API, which allows you to verify that
payload values were properly formatted for indexing. In addition, we have introduced a new `exact` search parameter
that allows you to force exact searches of vectors, even if an ANN index is built. This can be useful for validating
the accuracy of your HNSW configuration.

## [Anchor](https://qdrant.tech/articles/qdrant-0-11-release/\#backward-compatibility) Backward compatibility

This release is backward compatible with v0.10.5 storage in single node deployment, but unfortunately, distributed
deployment is not compatible with previous versions due to the large number of changes required for the replica set
implementation. However, clients are tested for backward compatibility with the v0.10.x service.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/qdrant-0-11-release.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/qdrant-0-11-release.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-197-lllmstxt|>
## langchain-integration
- [Articles](https://qdrant.tech/articles/)
- Using LangChain for Question Answering with Qdrant

[Back to Practical Examples](https://qdrant.tech/articles/practicle-examples/)