# [Anchor](https://qdrant.tech/documentation/guides/monitoring/\#monitoring--telemetry) Monitoring & Telemetry

Qdrant exposes its metrics in [Prometheus](https://prometheus.io/docs/instrumenting/exposition_formats/#text-based-format)/ [OpenMetrics](https://github.com/OpenObservability/OpenMetrics) format, so you can integrate them easily
with the compatible tools and monitor Qdrant with your own monitoring system. You can
use the `/metrics` endpoint and configure it as a scrape target.

Metrics endpoint: [http://localhost:6333/metrics](http://localhost:6333/metrics)

The integration with Qdrant is easy to
[configure](https://prometheus.io/docs/prometheus/latest/getting_started/#configure-prometheus-to-monitor-the-sample-targets)
with Prometheus and Grafana.

## [Anchor](https://qdrant.tech/documentation/guides/monitoring/\#monitoring-multi-node-clusters) Monitoring multi-node clusters

When scraping metrics from multi-node Qdrant clusters, it is important to scrape from
each node individually instead of using a load-balanced URL. Otherwise, your metrics will appear inconsistent after each scrape.

## [Anchor](https://qdrant.tech/documentation/guides/monitoring/\#monitoring-in-qdrant-cloud) Monitoring in Qdrant Cloud

Qdrant Cloud offers additional metrics and telemetry that are not available in the open-source version. For more information, see [Qdrant Cloud Monitoring](https://qdrant.tech/documentation/cloud/cluster-monitoring/).

## [Anchor](https://qdrant.tech/documentation/guides/monitoring/\#exposed-metrics) Exposed metrics

There are two endpoints avaliable:

- `/metrics` is the direct endpoint of the underlying Qdrant database node.

- `/sys_metrics` is a Qdrant cloud-only endpoint that provides additional operational and infrastructure metrics about your cluster, like CPU, memory and disk utilisation, collection metrics and load balancer telemetry. For more information, see [Qdrant Cloud Monitoring](https://qdrant.tech/documentation/cloud/cluster-monitoring/).


### [Anchor](https://qdrant.tech/documentation/guides/monitoring/\#node-metrics-metrics) Node metrics `/metrics`

Each Qdrant server will expose the following metrics.

| Name | Type | Meaning |
| --- | --- | --- |
| app\_info | gauge | Information about Qdrant server |
| app\_status\_recovery\_mode | gauge | If Qdrant is currently started in recovery mode |
| collections\_total | gauge | Number of collections |
| collections\_vector\_total | gauge | Total number of vectors in all collections |
| collections\_full\_total | gauge | Number of full collections |
| collections\_aggregated\_total | gauge | Number of aggregated collections |
| rest\_responses\_total | counter | Total number of responses through REST API |
| rest\_responses\_fail\_total | counter | Total number of failed responses through REST API |
| rest\_responses\_avg\_duration\_seconds | gauge | Average response duration in REST API |
| rest\_responses\_min\_duration\_seconds | gauge | Minimum response duration in REST API |
| rest\_responses\_max\_duration\_seconds | gauge | Maximum response duration in REST API |
| grpc\_responses\_total | counter | Total number of responses through gRPC API |
| grpc\_responses\_fail\_total | counter | Total number of failed responses through REST API |
| grpc\_responses\_avg\_duration\_seconds | gauge | Average response duration in gRPC API |
| grpc\_responses\_min\_duration\_seconds | gauge | Minimum response duration in gRPC API |
| grpc\_responses\_max\_duration\_seconds | gauge | Maximum response duration in gRPC API |
| cluster\_enabled | gauge | Whether the cluster support is enabled. 1 - YES |
| memory\_active\_bytes | gauge | Total number of bytes in active pages allocated by the application. [Reference](https://jemalloc.net/jemalloc.3.html#stats.active) |
| memory\_allocated\_bytes | gauge | Total number of bytes allocated by the application. [Reference](https://jemalloc.net/jemalloc.3.html#stats.allocated) |
| memory\_metadata\_bytes | gauge | Total number of bytes dedicated to allocator metadata. [Reference](https://jemalloc.net/jemalloc.3.html#stats.metadata) |
| memory\_resident\_bytes | gauge | Maximum number of bytes in physically resident data pages mapped. [Reference](https://jemalloc.net/jemalloc.3.html#stats.resident) |
| memory\_retained\_bytes | gauge | Total number of bytes in virtual memory mappings. [Reference](https://jemalloc.net/jemalloc.3.html#stats.retained) |
| collection\_hardware\_metric\_cpu | gauge | CPU measurements of a collection |

**Cluster-related metrics**

There are also some metrics which are exposed in distributed mode only.

| Name | Type | Meaning |
| --- | --- | --- |
| cluster\_peers\_total | gauge | Total number of cluster peers |
| cluster\_term | counter | Current cluster term |
| cluster\_commit | counter | Index of last committed (finalized) operation cluster peer is aware of |
| cluster\_pending\_operations\_total | gauge | Total number of pending operations for cluster peer |
| cluster\_voter | gauge | Whether the cluster peer is a voter or learner. 1 - VOTER |

## [Anchor](https://qdrant.tech/documentation/guides/monitoring/\#telemetry-endpoint) Telemetry endpoint

Qdrant also provides a `/telemetry` endpoint, which provides information about the current state of the database, including the number of vectors, shards, and other useful information. You can find a full documentation of this endpoint in the [API reference](https://api.qdrant.tech/api-reference/service/telemetry).

## [Anchor](https://qdrant.tech/documentation/guides/monitoring/\#kubernetes-health-endpoints) Kubernetes health endpoints

_Available as of v1.5.0_

Qdrant exposes three endpoints, namely
[`/healthz`](http://localhost:6333/healthz),
[`/livez`](http://localhost:6333/livez) and
[`/readyz`](http://localhost:6333/readyz), to indicate the current status of the
Qdrant server.

These currently provide the most basic status response, returning HTTP 200 if
Qdrant is started and ready to be used.

Regardless of whether an [API key](https://qdrant.tech/documentation/guides/security/#authentication) is configured,
the endpoints are always accessible.

You can read more about Kubernetes health endpoints
[here](https://kubernetes.io/docs/reference/using-api/health-checks/).

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/monitoring.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/monitoring.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-136-lllmstxt|>
## cloud-pricing-payments
- [Documentation](https://qdrant.tech/documentation/)
- Billing & Payments