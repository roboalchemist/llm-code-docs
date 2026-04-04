# Source: https://docs.datadoghq.com/cloudprem/configure/cluster_sizing.md

---
title: Cluster Sizing
description: Learn about cluster sizing for CloudPrem
breadcrumbs: Docs > CloudPrem > Configure CloudPrem > Cluster Sizing
source_url: https://docs.datadoghq.com/configure/cluster_sizing/index.html
---

# Cluster Sizing

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### CloudPrem is in Preview

Join the CloudPrem Preview to access new self-hosted log management features.

[Request Access](https://www.datadoghq.com/product-preview/cloudprem/)
{% /callout %}

## Overview{% #overview %}

Proper cluster sizing ensures optimal performance, cost efficiency, and reliability for your CloudPrem deployment. Your sizing requirements depend on several factors including log ingestion volume, query patterns, and the complexity of your log data.

This guide provides baseline recommendations for dimensioning your CloudPrem cluster componentsâindexers, searchers, supporting services, and the PostgreSQL database.
Use your expected daily log volume and peak ingestion rates as starting points, then monitor your cluster's performance and adjust sizing as needed.
## Indexers{% #indexers %}

Indexers receive logs from Datadog Agents, then process, index, and store them as index files (called *splits*) in object storage. Proper sizing is critical for maintaining ingestion throughput and ensuring your cluster can handle your log volume.

| Specification        | Recommendation         | Notes                                                                                                                                          |
| -------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Performance**      | 5 MB/s per vCPU        | Baseline throughput to determine initial sizing. Actual performance depends on log characteristics (size, number of attributes, nesting level) |
| **Memory**           | 4 GB RAM per vCPU      |
| **Minimum Pod Size** | 2 vCPUs, 8 GB RAM      | Recommended minimum for indexer pods                                                                                                           |
| **Storage Capacity** | At least 200 GB        | Required for temporary data while creating and merging index files                                                                             |
| **Storage Type**     | Local SSDs (preferred) | Local HDDs or network-attached block storage (Amazon EBS, Azure Managed Disks) can also be used                                                |
| **Disk I/O**         | ~20 MB/s per vCPU      | Equivalent to 320 IOPS per vCPU for Amazon EBS (assuming 64 KB IOPS)                                                                           |

{% collapsible-section %}
#### Example: Sizing for 1 TB of logs per day

To index 1 TB of logs per day (~11.6 MB/s), follow these steps:

1. **Calculate vCPUs:** `11.6 MB/s Ã· 5 MB/s per vCPU â 2.3 vCPUs`
1. **Calculate RAM:** `2.3 vCPUs Ã 4 GB RAM â 9 GB RAM`
1. **Add headroom:** Start with one indexer pod configured with **3 vCPUs, 12 GB RAM, and a 200 GB disk**. Adjust these values based on observed performance and redundancy needs.

{% /collapsible-section %}

## Searchers{% #searchers %}

Searchers handle search queries from the Datadog UI, reading metadata from the Metastore and fetching data from object storage.

A general starting point is to provision roughly double the total number of vCPUs allocated to Indexers.

- **Performance:** Search performance depends heavily on the workload (query complexity, concurrency, amount of data scanned). For instance, term queries (`status:error AND message:exception`) are usually computationally less expensive than aggregations.
- **Memory:** 4 GB of RAM per searcher vCPU. Provision more RAM if you expect many concurrent aggregation requests.

## Other services{% #other-services %}

Allocate the following resources for these lightweight components:

| Service           | vCPUs | RAM  | Replicas |
| ----------------- | ----- | ---- | -------- |
| **Control Plane** | 2     | 4 GB | 1        |
| **Metastore**     | 2     | 4 GB | 2        |
| **Janitor**       | 2     | 4 GB | 1        |

## PostgreSQL database{% #postgresql-database %}

- **Instance Size:** For most use cases, a PostgreSQL instance with 1 vCPU and 4 GB of RAM is sufficient
- **AWS RDS Recommendation:** If using AWS RDS, the `t4g.medium` instance type is a suitable starting point
- **High Availability:** Enable Multi-AZ deployment with one standby replica for high availability

## Further reading{% #further-reading %}

- [Configure CloudPrem Ingress](https://docs.datadoghq.com/cloudprem/configure/ingress/)
- [Configure CloudPrem Log Processing](https://docs.datadoghq.com/cloudprem/configure/processing/)
- [Learn more about CloudPrem Architecture](https://docs.datadoghq.com/cloudprem/architecture/)
