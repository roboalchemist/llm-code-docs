# [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#changelog) Changelog

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#171-2025-06-03) 1.7.1 (2025-06-03)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.16.6 |
| operator version | 2.6.0 |
| qdrant-cluster-manager version | v0.3.6 |

- Performance and stability improvements

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#170-2025-05-14) 1.7.0 (2025-05-14)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.16.3 |
| operator version | 2.4.2 |
| qdrant-cluster-manager version | v0.3.5 |

- Add optional automatic shard balancing
- Set strict mode by default for new clusters to only allow queries with payload filters on fields that are indexed

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#164-2025-04-17) 1.6.4 (2025-04-17)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.15.5 |
| operator version | 2.3.4 |
| qdrant-cluster-manager version | v0.3.4 |

- Fix bug in operator Helm chart that caused role binding generation to fail when using `watch.namespaces`

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#163-2025-03-28) 1.6.3 (2025-03-28)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.15.0 |
| operator version | 2.3.3 |
| qdrant-cluster-manager version | v0.3.4 |

- Performance and stability improvements for collection re-sharding

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#162-2025-03-21) 1.6.2 (2025-03-21)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.15.0 |
| operator version | 2.3.2 |
| qdrant-cluster-manager version | v0.3.3 |

- Allow disabling NetworkPolicy management in Qdrant Cluster operator

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#161-2025-03-14) 1.6.1 (2025-03-14)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.14.2 |
| operator version | 2.3.2 |
| qdrant-cluster-manager version | v0.3.3 |

- Add support for GPU instances
- Experimental support for automatic shard balancing

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#151-2025-03-04) 1.5.1 (2025-03-04)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.12.0 |
| operator version | 2.1.26 |
| qdrant-cluster-manager version | v0.3.2 |

- Fix scaling down clusters that have TLS with self-signed certificates configured
- Various performance improvements and stability fixes

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#150-2025-02-21) 1.5.0 (2025-02-21)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.12.0 |
| operator version | 2.1.26 |
| qdrant-cluster-manager version | v0.3.0 |

- Added support for P2P TLS configuration
- Faster node removal on scale down
- Various performance improvements and stability fixes

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#140-2025-01-23) 1.4.0 (2025-01-23)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.8.0 |
| operator version | 2.1.26 |
| qdrant-cluster-manager version | v0.3.0 |

- Support deleting peers on horizontal scale down, even if they are already offline
- Support removing partially deleted peers

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#130-2025-01-17) 1.3.0 (2025-01-17)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.8.0 |
| operator version | 2.1.21 |
| qdrant-cluster-manager version | v0.2.10 |

- Support for re-sharding with Qdrant >= 1.13.0

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#120-2025-01-16) 1.2.0 (2025-01-16)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.8.0 |
| operator version | 2.1.20 |
| qdrant-cluster-manager version | v0.2.9 |

- Performance and stability improvements

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#110-2024-12-03) 1.1.0 (2024-12-03)

\| qdrant-kubernetes-api version \| v1.6.4 \|
\| operator version \| 2.1.10 \|
\| qdrant-cluster-manager version \| v0.2.6 \|

- Activate cluster-manager for automatic shard replication

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#100-2024-11-11) 1.0.0 (2024-11-11)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.2.7 |
| operator version | 0.1.3 |
| qdrant-cluster-manager version | v0.2.4 |

- Initial release

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/private-cloud/changelog.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/private-cloud/changelog.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-115-lllmstxt|>
## data-ingestion-beginners
- [Documentation](https://qdrant.tech/documentation/)
- Data Ingestion for Beginners

![data-ingestion-beginners-7](https://qdrant.tech/documentation/examples/data-ingestion-beginners/data-ingestion-7.png)