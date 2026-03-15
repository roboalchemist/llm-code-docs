# Source: https://docs.confluent.io/cloud/current/clusters/cluster-types.md

<!-- *********************************************************** -->
<!-- string replacements for cluster limits throughout the topic -->
<!-- *********************************************************** -->
<!-- cluster limits: -->
<!-- eCKU/CKU limits -->
<!-- string replacements for min/max eCKU/CKU values throughout the topic -->

<a id="cloud-cluster-types"></a>

# Kafka Cluster Types in Confluent Cloud

Confluent offers different types of Apache KafkaÂ® clusters in Confluent Cloud. The cluster type you
choose determines the features, capabilities, and price of the cluster. Use the information
in this topic to find the cluster with the features and capabilities that best
meets your needs.

<a id="basic-cluster"></a>

<a id="standard-cluster"></a>

<a id="enterprise-cluster"></a>

<a id="dedicated-cluster"></a>

<a id="freight-cluster"></a>

## Cluster types

Confluent Cloud offers these Kafka cluster types:

- Basic clusters - Used for experimentation, early development and basic use cases.
- Standard clusters - Used for production-ready features and functionality.
- Enterprise clusters - Used for production-ready functionality that requires private networking capabilities.
- Dedicated clusters - Used for critical production workloads with high traffic or private networking requirements.
- Freight clusters - Used for high-throughput, relaxed latency workloads that are less expensive than self-managed open source Kafka.

<a id="freight-limitations"></a>
<details>
<summary style="display: list-item; cursor:pointer; color:#337ab7;">
  Freight cluster considerations
</summary>
- Freight clusters are currently available in select AWS regions. For more information, see [Cloud Providers and Regions for Confluent Cloud](regions.md#providers-regions).
- You must optimize the clients you use to connect to Freight clusters. For more information, see [Freight Clients for Confluent Cloud](../client-apps/optimizing/freight.md#freight-latency-clients).
- Freight clusters do not support the following:
  - Idempotent producer
  - Transactions
  - Audit logs
- Freight clusters do not support the following metrics and functions:
  - `DELETE_RECORDS`
  - `REPLICA_STATUS`

<!-- * us-east-2 --></details>

<a id="cluster-scale-overview"></a>

### Cluster provisioning and scaling

Confluent uses billing units to provision and scale clusters.

Elastic scaling
: Basic, Standard, Enterprise, and Freight clusters are elastic, shrinking and expanding
  automatically based on load. You donât resize these clusters (unlike Dedicated clusters). When you need more capacity, your
  cluster expands up to the fixed ceiling. If youâre not using capacity above the minimum, youâre not paying for it. If youâre at zero
  capacity, you donât pay for anything. For more information, see [Elastic Confluent Unit for Kafka](../billing/overview.md#e-cku-definition) and [eCKU/CKU comparison](#e-cku-details).

<a id="freight-scale-limitations"></a>
<details>
<summary style="display: list-item; cursor:pointer; color:#337ab7;">
  Freight clusters scaling considerations
</summary>

Freight clusters are elastic, scaling automatically based on load, so you only pay for the eCKUs
you use. However, Freight clusters may not scale as quickly as other eCKU clusters. In general,
Freight clusters can support an additional 4 eCKU of capacity (240 MBps of ingress / 720 MBps of egress)
every 10 minutes. If you workload grows faster than this, you may experience higher latency or failed requests.
As your workload decreases, you pay for your actual eCKU usage.

In scenarios where you expect a large, rapid increase in traffic, consider contacting your account team to get
Confluent to work with you to meet your request.

</details>

</br>

<a id="fast-scaling-enterprise"></a>

Fast scaling for Enterprise clusters
: All Enterprise clusters support fast scaling up to 10 eCKUs, which is similar to how elastic scaling has worked in the past. Beyond
  10 eCKUs, Enterprise clusters support *on-demand* scaling, which may be limited to a growth rate of approximately 20 minutes per
  eCKU.
  <br/>
  Considerations:
  : - To provision Enterprise clusters with a maximum of 32 eCKU on AWS, your cluster networking must use Private Network Interface (PNI).
    - Enterprise clusters that use PrivateLink networking on AWS are limited to a maximum of 10 eCKU.
    <br/>
    - If you have workloads that require fast scaling beyond 10 eCKU or workloads larger than 32 eCKU, reach out to Confluent to request
      to have your cluster enabled.

Manual scaling
: Dedicated clusters are provisioned and billed in terms of Confluent Unit for Kafka (CKU). CKUs are a unit of horizontal
  scalability in Confluent Cloud that provide a preallocated amount of resources. How much you can ingest
  and stream per CKU depends on a variety of factors including client application design and
  partitioning strategy. For more information, see [Monitor Dedicated Clusters in Confluent Cloud](../monitoring/cluster-load-metric.md#monitor-dedicated-clusters) and [Dedicated Cluster Performance and Expansion in Confluent Cloud](../monitoring/monitor-performance.md#cloud-cluster-monitor-performance).

## Features

All clusters have the following features:

- [Kafka ACLs](../security/access-control/acls/overview.md#acl-manage)
- [Fully-managed replica placement](resilience.md#confluent-cloud-resilience)
- [User interface to manage consumer lag](../monitoring/monitor-lag.md#cloud-monitoring-lag)
- [Topic management](../topics/overview.md#cloud-topics-manage)
- [Fully-Managed Connectors](../connectors/overview.md#kafka-connect-cloud)
- [View and consume Connect logs](../connectors/logging-cloud-connectors.md#ccloud-connector-logging)
- [Stream Governance](../stream-governance/index.md#cloud-dg)
- [Stream Catalog](../stream-governance/stream-catalog.md#cloud-stream-catalog)
- [Stream Lineage](../stream-governance/stream-lineage.md#cloud-stream-lineage)
- [Encryption-at-rest](https://confluent.safebase.us/?itemUid=ef061e5b-a2f4-469e-92bc-ab973e3d7842&source=title)
- [TLS for data in transit](../security/encrypt/tls.md#manage-data-in-transit-with-tls)
- [Role-based Access Control (RBAC)](../security/access-control/rbac/overview.md#cloud-rbac) (Basic clusters do not support RBAC roles for resources within the Kafka cluster)

### Feature comparison table

The tables below offer comparisons of the features supported by only some Kafka cluster types.

| Feature                                                                                                             | [Basic](#basic-cluster)   | [Standard](#standard-cluster)   | [Enterprise](#enterprise-cluster)   | [Freight](#freight-cluster)   | [Dedicated](#dedicated-cluster)   |
|---------------------------------------------------------------------------------------------------------------------|---------------------------|---------------------------------|-------------------------------------|-------------------------------|-----------------------------------|
| [Exactly Once Semantics](/platform/current/streams/concepts.html#streams-concepts-processing-guarantees)            | â                         | â                               | â                                   |                               | â                                 |
| [Key based compacted storage](/kafka/kafka/log_compaction.html)                                                     | â                         | â                               | â                                   | â                             | â                                 |
| [Custom Connectors](../connectors/bring-your-connector/overview.md#cc-bring-your-connector)                         | â                         | â                               |                                     |                               | â                                 |
| [Flink](../flink/overview.md#ccloud-flink)                                                                          | â                         | â                               | â                                   |                               | â                                 |
| [ksqlDB](../ksqldb/overview.md#cloud-ksqldb-create-stream-processing-apps)                                          | â                         | â                               |                                     |                               | â                                 |
| [Schema validation](../sr/broker-side-schema-validation.md#cloud-schema-validation)                                 |                           |                                 |                                     |                               | â                                 |
| [Public networking](../networking/overview.md#cloud-networking-support-public)                                      | â                         | â                               |                                     |                               | â                                 |
| [Private networking](../networking/overview.md#cloud-networking-support-public)                                     |                           |                                 | â                                   | â                             | â                                 |
| [OAuth](../security/authenticate/workload-identities/identity-providers/oauth/overview.md#oauth-overview)           |                           | â                               | â                                   | â                             | â                                 |
| [Mutual TLS (mTLS)](../security/authenticate/workload-identities/identity-providers/mtls/overview.md#mtls-overview) |                           |                                 | â                                   | â                             | â                                 |
| [Audit logs](../monitoring/audit-logging/cloud-audit-log-concepts.md#cloud-audit-logs)                              |                           | â                               | â                                   |                               | â                                 |
| [Self-managed encryption keys](../security/encrypt/byok/overview.md#byok-encrypted-clusters)                        |                           |                                 | â                                   |                               | â                                 |
| [Automatic Elastic scaling](../billing/overview.md#e-cku-definition)                                                | â                         | â                               | â                                   | â                             |                                   |
| [Stream Sharing](../stream-sharing/index.md#cloud-data-sharing)                                                     | â                         | â                               |                                     |                               | â <sub>(\*)</sub>                 |
| [Client Quotas](client-quotas.md#client-quotas)                                                                     |                           |                                 | â                                   | â                             | â                                 |
| [Access Transparency](../monitoring/audit-logging/access-transparency-overview.md#access-transparency-overview)     |                           |                                 |                                     |                               | â                                 |

\* Stream sharing doesnât support all private networking options.

#### Cluster linking capabilities

The table below offers a comparison of cluster linking capabilities by cluster type.

| Cluster type                  | Basic   | Standard   | Enterprise          | Dedicated           | Freight   |
|-------------------------------|---------|------------|---------------------|---------------------|-----------|
| Supports source clusters      | Yes     | Yes        | Yes <sub>(\*)</sub> | Yes <sub>(\*)</sub> | No        |
| Supports destination clusters | No      | No         | Yes <sub>(\*)</sub> | Yes <sub>(\*)</sub> | No        |

\* Capability dependent on the networking type and the other cluster involved. To learn more, see [Supported cluster types](../multi-cloud/cluster-linking/index.md#cloud-cluster-linking-supported-types) in the Cluster Linking documentation.

#### Uptime service level agreement options

The table below offers a comparison of uptime service level agreements (SLA) options by cluster type. For more information, see [Confluent Cloud Service Level Agreement](https://confluent.io/confluent-cloud-uptime-sla/).

Considerations:
: - To obtain a higher uptime SLA, you can upgrade from Basic to a Standard cluster at any time using the Cloud Console.
  - Standard and Enterprise clusters require 2 eCKU minimums for the 99.99% SLA.
  - Dedicated clusters require Multi-Zone deployments for the 99.99% SLA.

| Cluster type   | 99.5%   | 99.9%   | 99.95%              | 99.99%                            |
|----------------|---------|---------|---------------------|-----------------------------------|
| Basic          | Yes     | No      | No                  | No                                |
| Standard       | No      | Yes     | No                  | Yes <sub>(Requires 2 eCKU)</sub>  |
| Enterprise     | No      | Yes     | No                  | Yes <sub>(Requires 2 eCKU )</sub> |
| Dedicated      | No      | No      | Yes <sub>(SZ)</sub> | Yes <sub>(MZ)</sub>               |
| Freight        | No      | No      | No                  | Yes                               |

<a id="e-cku-basic-details"></a>

<a id="e-cku-standard-details"></a>

<a id="e-cku-details"></a>

<a id="enterprise-cku-guidance"></a>

<a id="ecku-comparison-table"></a>

<a id="e-cku-freight-details"></a>

<a id="freight-ecku-guidance"></a>

## eCKU/CKU comparison

Use the table below to compare limits for a single billing unit for each cluster type. For more information, see [Elastic Confluent Unit for Kafka](../billing/overview.md#e-cku-definition), [Minimum/maximum eCKU requirements](#min-max-ecku) and [Cluster provisioning and scaling](#cluster-scale-overview).

| Dimension                                                                       | [Basic eCKU](#cluster-scale-overview)   | [Standard eCKU](#cluster-scale-overview)   | [Enterprise eCKU](#cluster-scale-overview)   |   [Dedicated CKU](#cluster-scale-overview) | [Freight eCKU](#cluster-scale-overview)   |
|---------------------------------------------------------------------------------|-----------------------------------------|--------------------------------------------|----------------------------------------------|--------------------------------------------|-------------------------------------------|
| [Ingress](../_glossary.md#term-ingress) (MBps)                                  | 5                                       | 25                                         | 60                                           |                                         60 | 60                                        |
| [Egress](../_glossary.md#term-egress) (MBps)                                    | 15                                      | 75                                         | 180                                          |                                        180 | 180                                       |
| [Partitions (pre-replication)](../_glossary.md#term-partitions-pre-replication) | 30                                      | 250                                        | 3,000                                        |                                      4,500 | 3,000                                     |
| Number of partitions that you can compact (pre-replication)                     | 30                                      | 250                                        | 360                                          |                                      4,500 | None                                      |
| [Total client connections](../_glossary.md#term-total-client-connections)       | 20                                      | 1000                                       | 18,000                                       |                                     18,000 | 18,000                                    |
| [Connection attempts](../_glossary.md#term-connection-attempts) (per second)    | 5                                       | 50                                         | 500                                          |                                        500 | 500                                       |
| [Requests](../_glossary.md#term-requests) (per second)                          | 100                                     | 1,500                                      | 7,500                                        |                                     15,000 | 15,000                                    |
| Kafka REST Produce v3 - Max throughput (MBps):                                  | N/a                                     | N/a                                        | N/a                                          |                                         50 | N/a                                       |
| Kafka REST Produce v3 - Max connection requests (per second):                   | N/a                                     | N/a                                        | N/a                                          |                                        300 | N/a                                       |
| Kafka REST Produce v3 - Max streamed requests (per second):                     | N/a                                     | N/a                                        | N/a                                          |                                       3000 | N/a                                       |
| Kafka REST Admin v3 - Max connection requests (per second):                     | N/a                                     | N/a                                        | N/a                                          |                                        300 | N/a                                       |

<a id="min-max-ecku"></a>

### Minimum/maximum eCKU requirements

The table below lists minimum and maximum requirements for elastic cluster types. Dedicated clusters have CKU
limits that depend on billing and other factors. For more information, see [CKU purchase limits](#cku-limits-per-cluster).

Considerations:
: - To provision Enterprise clusters with a maximum of 32 eCKU on AWS, your cluster networking must use Private Network Interface (PNI).
  - Enterprise clusters that use PrivateLink networking on AWS are limited to a maximum of 10 eCKU.
  <br/>
  - Enterprise clusters support fast scaling up to 10 eCKUs and on-demand scaling beyond 10 eCKU. On-demand scaling
    may be limited to a growth rate of approximately 20 minutes per eCKU. For more information, see [Fast scaling for Enterprise clusters](#fast-scaling-enterprise).

| Cluster type SKU   | Minimum eCKU                  |   Maximum eCKU |
|--------------------|-------------------------------|----------------|
| Basic              | 1                             |             50 |
| Standard           | 1 (99.9% SLA), 2 (99.99% SLA) |             10 |
| Enterprise         | 1 (99.9% SLA), 2 (99.99% SLA) |             32 |
| Freight            | 2                             |            152 |

To help you control costs with elastic cluster types, you can set a lower maximum eCKU capacity on your elastic
cluster. When you lower the maximum eCKU, you lower the capacity of your cluster. Use this feature with caution.
The maximum eCKU limits the clusterâs capacity, which can lead to throttling or workload impact when the reduced
capacity limit is reached.

When you lower maximum eCKU to reduce the capacity of your cluster, you must also manage your workload, especially
for limits not currently strictly enforced. Confluent will contact you if your clusters with managed maximum eCKU
repeatedly exceed the user-defined reduced capacity for requests, total client connections, and connection
attempts. For more information about managing limits, see [Cluster limit comparison](#cluster-limits-compare). For information
about how to lower maximum eCKU, see [Update Kafka clusters](create-cluster.md#cloud-cluster-update-api).

<a id="cku-limits-per-cluster"></a>

### CKU purchase limits

Dedicated clusters can be purchased in any whole number of CKUs up to the limit.

- For organizations with credit card billing, the upper limit is 4 CKUs per Dedicated cluster.
  Clusters up to 152 <sub>\*</sub> CKUs are available by request.
- For organizations with integrated cloud provider billing or payment using an invoice,
  the upper limit is 24 CKUs per Dedicated cluster. Clusters up to 152 <sub>\*</sub> CKUs are available by request.

For clusters that can scale to 152 <sub>\*</sub> CKU, contact [Confluent Support](https://support.confluent.io) to discuss
the onboarding process and product considerations.

Single-zone clusters can have 1 or more CKUs, whereas multi-zone clusters, which are spread across three availability zones,
require a minimum of 2 CKUs. Zone availability cannot be changed after the cluster is created.

\* AWS and Google Cloud support Kafka clusters to 152 CKUs. Azure supports Kafka clusters to 100 CKUs.

<a id="cku-details"></a>

### Fixed limits and recommended guidelines

CKUs determine the capacity of your cluster. For a Confluent Cloud cluster, the expected performance for any
given workload is dependent on a variety of dimensions, such as message size and number of partitions.

There are two categories of CKU dimensions:

- Dimensions with a [fixed limit](#fixed-limit) that cannot be exceeded.
- Dimensions with a more flexible [guideline](#guideline) that may be exceeded depending on the overall cluster load.

The recommended guideline for a dimension is calculated for a workload optimized across the dimensions, enabling
high levels of CKU utilization as measured by the [cluster load metric](../monitoring/cluster-load-metric.md#cloud-cluster-load-metric).
You may exceed the recommended guideline for a dimension, and achieve higher performance for that dimension, usually
only if your usage of other dimensions is less than the recommended guideline or fixed limit.

Also note that usage patterns across all dimensions affect the workload and you may not
achieve the suggested guideline for a particular dimension.
For example, if you reach the partition limit, you will not likely reach the maximum CKU
throughput guideline.

You should monitor the [cluster load metric](../monitoring/cluster-load-metric.md#cloud-cluster-load-metric) for your cluster
to see how your usage pattern correlates with cluster utilization.

When a clusterâs load metric is high, the cluster may delay new connections and/or throttle clients
in an attempt to ensure the cluster remains available. This throttling would register as non-zero values
for the producer client [produce-throttle-time-max and produce-throttle-time-avg metrics](../client-apps/jmx-monitoring.md#producer-throttling)  and
[consumer client fetch-throttle-time-max and fetch-throttle-time-avg metrics](/platform/current/kafka/monitoring.html#fetch-metrics-kafka).

<a id="fixed-limit"></a>

#### Dimensions with fixed limits

The following dimensions have fixed limits that you cannot exceed:

- Storage (pre-replication)
- Partitions (pre-replication)
- Connection attempts
- Kafka REST Produce v3
- Kafka REST Admin v3

<a id="guideline"></a>

#### Dimensions with recommended guidelines

These dimensions provide guidelines for capacity planning. The ability to fully utilize these dimensions
depend on the workload and utilization of other dimensions. See more about measuring load
in [cluster load metric](../monitoring/cluster-load-metric.md#cloud-cluster-load-metric) and for the maximum bandwidth for
each cloud provider (AWS, Google Cloud, Azure), are available in
[Benchmark Your Dedicated Apache Kafka Cluster on Confluent Cloud](https://assets.confluent.io/m/2d7c883a8aa6a71d/original/20200501-WP-Benchmark_Your_Dedicated_Apache_Kafka_Cluster_on_Confluent_Cloud.pdf).

The following dimensions come with recommended guidelines:

- Ingress
- Egress
- Total client connections
- Requests

<a id="cluster-limits-compare"></a>

## Cluster limit comparison

Use the table below to compare cluster limits across cluster types.

Considerations:
: - To provision Enterprise clusters with a maximum of 32 eCKU on AWS, your cluster networking must use Private Network Interface (PNI).
  - Enterprise clusters that use PrivateLink networking on AWS are limited to a maximum of 10 eCKU.
  <br/>
  - Basic, Standard, Enterprise, and Freight cluster limits are based on maximum eCKU for the cluster type. For more information, see [Elastic Confluent Unit for Kafka](../billing/overview.md#e-cku-definition).
  - Dedicated Kafka cluster limits are based on 152 CKU. For more information, see [CKU purchase limits](#cku-limits-per-cluster) and [Confluent Unit for Kafka](../billing/overview.md#cku-definition).
  - For connector tasks per cluster, Basic clusters are limited to one task per connector. You can deploy 250 connectors to a Basic cluster but each
    connector can only have one task. If you need more than one task, upgrade your cluster.
  - Enterprise clusters support fast scaling up to 10 eCKUs and on-demand scaling beyond 10 eCKU. On-demand scaling
    may be limited to a growth rate of approximately 20 minutes per eCKU. For more information, see [Fast scaling for Enterprise clusters](#fast-scaling-enterprise).
  - The maximum limits for requests, total client connections, and connection attempts are currently not strictly enforced for
    Basic, Standard, Enterprise, and Freight clusters, whether you are using a cluster with the default capacity, or a maximum capacity you configured.
  - You can lower maximum eCKU to reduce the capacity of your cluster but you must also manage your workload, especially for limits not
    currently strictly enforced. Confluent will contact you if your clusters with managed maximum eCKU repeatedly exceed the user-defined reduced
    capacity for requests, total client connections, and connection attempts. You should be prepared to discuss mitigation strategies, such as
    reduction of workload to stay within the limits of your reduced capacity, or an increase to the maximum eCKU configuration to accommodate the workload.
  - Throughout 2026, Confluent will begin enforcing stricter limits for requests, total client connections, and
    connection attempts for Basic, Standard, Enterprise, and Freight clusters using the following schedule:
    - Starting March 1, 2026, Confluent will begin enforcing stricter limits for requests for Enterprise and Freight clusters.
    - Starting June 30, 2026, Confluent will begin enforcing stricter limits for total client connections and
      connection attempts for Enterprise and Freight clusters.
    - Starting June 30, 2026, Confluent will begin enforcing stricter limits for requests, total client connections, and
      connection attempts for Basic and Standard clusters.

| Dimension                                                                 | [Basic](#basic-cluster)   | [Standard](#standard-cluster)   | [Enterprise](#enterprise-cluster)   | [Dedicated](#dedicated-cluster)   | [Freight](#freight-cluster)   |
|---------------------------------------------------------------------------|---------------------------|---------------------------------|-------------------------------------|-----------------------------------|-------------------------------|
| [Maximum eCKU/CKU](#min-max-ecku)                                         | 50                        | 10                              | 32                                  | 152                               | 152                           |
| Fast scaling                                                              | n/a                       | n/a                             | 10                                  | n/a                               | n/a                           |
| Ingress (MBps)                                                            | 250                       | 250                             | 1,920                               | 9,120                             | 9,120                         |
| Egress (MBps)                                                             | 750                       | 750                             | 5,760                               | 27,360                            | 27,360                        |
| Partitions (pre-replication)                                              | 1500                      | 2500                            | 96,000                              | 100,000                           | 50,000                        |
| Number of partitions you can compact                                      | 1500                      | 2500                            | 11,520                              | 100,000                           | None                          |
| Total client connections                                                  | 1000                      | 10,000                          | 576,000                             | 2,736,000                         | 2,736,000                     |
| Connection attempts (per second)                                          | 80                        | 500                             | 16,000                              | 76,000                            | 76,000                        |
| Requests (per second)                                                     | 15,000                    | 15,000                          | 240,000                             | 2,280,000                         | 2,280,000                     |
| Message size (MB)                                                         | 8                         | 8                               | 20                                  | 20                                | 20                            |
| Client version (minimum)                                                  | 0.11.0                    | 0.11.0                          | 0.11.0                              | 0.11.0                            | 0.11.0                        |
| Request size (MB)                                                         | 100                       | 100                             | 100                                 | 100                               | 100                           |
| Fetch bytes (MB)                                                          | 55                        | 55                              | 55                                  | 55                                | 55                            |
| API keys                                                                  | 50                        | 100                             | 500                                 | 2,000                             | 500                           |
| Partition creation and deletion (per five minute period)                  | 250                       | 500                             | 500                                 | 5,000                             | 500                           |
| Connector tasks per Kafka cluster                                         | 250                       | 250                             | 250                                 | 250                               | N/A                           |
| ACLs                                                                      | 1,000                     | 1,000                           | 4,000                               | 10,000                            | 10,000                        |
| Kafka REST Produce v3 - Max throughput (MBps):                            | 10                        | 10                              | 10                                  | 7,600                             | 10                            |
| Kafka REST Produce v3 - Max connection requests (per second):             | 25                        | 25                              | 25                                  | 45,600                            | 25                            |
| Kafka REST Produce v3 - Max streamed requests (per second):               | 1000                      | 1000                            | 1000                                | 456,000                           | 1000                          |
| Kafka REST Produce v3 - Max message size for Kafka REST Produce API (MB): | 8                         | 8                               | 8                                   | 20                                | 8                             |
| Kafka REST Admin v3 - Max connection requests (per second):               | 25                        | 25                              | 25                                  | 45,600                            | 25                            |

The capabilities provided in this topic are for planning purposes, and are not a guarantee of performance, which varies depending on each unique configuration.

<!-- note that the REST API limits are also noted in the docs-cloud/kafka-rest/kafka-rest-cc.rst topic, so changes should
be duplicated there. -->

### Migrate from open source Kafka

If you are currently self-managing Kafka, use the following information to help choose which cluster type best suits your use-cases. For
information about migrating from open source Kafka to Confluent Cloud, see
the [Migrating from Kafka services to Confluent](https://assets.confluent.io/m/2745775bbd1fa224/original/20240425-EB-Migrating_From_Kafka_To_Confluent.pdf) PDF.

- Ingress: Use [producer outgoing-byte-rate metrics](/platform/current/kafka/monitoring.html#producer-global-request-metrics)
  and [broker kafka.server:type=BrokerTopicMetrics,name=BytesInPerSec metrics](/platform/current/kafka/monitoring.html#kafka-monitoring-metrics-broker)
  to understand your throughput.
- Egress: the [consumer incoming-byte-rate metrics](/platform/current/kafka/monitoring.html#consumer-global-request-metrics)
  and [broker kafka.server:type=BrokerTopicMetrics,name=BytesOutPerSec](/platform/current/kafka/monitoring.html#kafka-monitoring-metrics-broker)
  to understand your throughput.
- Storage (pre-replication): Use the amount of disk space your cluster is using to understand your storage needs.
- Partitions (pre-replication): Use the `kafka.controller:type=KafkaController,name=GlobalPartitionCount` metric to
  understand your partition usage. Find details in the [Broker section](/platform/current/kafka/monitoring.html#kafka-monitoring-metrics-broker).
- Total client connections: Use the [broker kafka.server:type=socket-server-metrics,listener={listener_name},networkProcessor={#},name=connection-count metrics](/platform/current/kafka/monitoring.html#kstypesocketservermetrics)
  to understand how many connections you are using. This value may not have a 1:1 ratio to connections in Confluent Cloud, depending on the
  number of brokers, partitions, and applications in your self-managed cluster.
- Connection attempts: Use the rate of change for the
  [kafka.server:type=socket-server-metrics,listener={listener_name},networkProcessor={#},name=connection-count](/platform/current/kafka/monitoring.html#zk-metrics) metric and
  the Consumer `connection-creation-rate` metric to understand how many new connections you are creating. For details,
  see [Broker Metrics](/platform/current/kafka/monitoring.html#kstypesocketservermetrics)  and [Global Connection Metrics](/platform/current/kafka/monitoring.html#consumer-metric-global-connection-metrics).
- Requests: Use the [broker kafka.network:type=RequestMetrics,name=RequestsPerSec,request={Produce FetchConsumer FetchFollower} metrics](/platform/current/kafka/monitoring.html#kafka-monitoring-metrics-broker)
  and [client request-rate metrics](/platform/current/kafka/monitoring.html#kafka-monitoring-metrics-producer) to understand your request volume.

## Partition guidelines

The partition guidelines that follow are based on benchmarking and intended as practical recommendations for planning purposes.
Performance per partition varies depending on your individual configuration, and these benchmarks do not guarantee performance.

Except for Basic clusters, all clusters offer:

- Unlimited storage per partition
- Unlimited storage per partition for compacted topics

Basic clusters offer:

- 5 TB per partition
- 5 TB per partition for compacted topics

Use the table below to compare partition guidelines across cluster types.

| Dimension             | Basic    | Standard   | Enterprise   | Dedicated                                | Freight   |
|-----------------------|----------|------------|--------------|------------------------------------------|-----------|
| Ingress per partition | ~5 MBps  | ~5 MBps    | ~6 MBps      | ~12 MBps (aggregate producer throughput) | ~6 MBps   |
| Egress per partition  | ~15 MBps | ~15 MBps   | ~18 MBps     | ~36 MBps (aggregate producer throughput) | ~18 MBps  |

## Related content

- For per-topic settings and limits, see [Manage Kafka Cluster Configuration Settings in Confluent Cloud](broker-config.md#cloud-broker-config)
- For quotas that apply to organizations, environments, clusters, and accounts, see [Service Quotas for Confluent Cloud](../quotas/service-quotas.md#ccloud-resource-limits)
- For performance monitoring your clusters, see [Metrics API](../monitoring/metrics-api.md#metrics-api)
- For costs by dimension, see [Billing dimensions in Confluent Cloud](../billing/overview.md#billing-dimensions)
- For cost estimates, see [Confluent Cost Estimator](https://www.confluent.io/pricing/cost-estimator/)
- For information about migrating from open source Kafka to Confluent Cloud, see the
  [Migrating from Kafka services to Confluent](https://assets.confluent.io/m/2745775bbd1fa224/original/20240425-EB-Migrating_From_Kafka_To_Confluent.pdf) PDF
- For information about the security capabilities of Confluent Cloud, see [Confluent Trust Center](https://confluent.safebase.us/?product=default)
