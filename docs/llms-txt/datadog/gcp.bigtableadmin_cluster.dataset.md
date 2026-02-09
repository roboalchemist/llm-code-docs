# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.bigtableadmin_cluster.dataset.md

---
title: Cloud Bigtable Cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Bigtable Cluster
---

# Cloud Bigtable Cluster

Cloud Bigtable Cluster in GCP is a scalable, high-performance NoSQL database cluster used for large analytical and operational workloads. It stores data in a distributed manner across nodes, providing low-latency access and automatic replication for reliability. Clusters can be resized by adding or removing nodes to adjust performance and throughput without downtime.

```
gcp.bigtableadmin_cluster
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                               | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| cluster_config       | core | json          | Configuration for this cluster.                                                                                                                                                                                                                                         |
| datadog_display_name | core | string        |
| default_storage_type | core | string        | Immutable. The type of storage used by this cluster to serve its parent instance's tables, unless explicitly overridden.                                                                                                                                                |
| encryption_config    | core | json          | Immutable. The encryption configuration for CMEK-protected clusters.                                                                                                                                                                                                    |
| labels               | core | array<string> |
| location             | core | string        | Immutable. The location where this cluster's nodes and storage reside. For best performance, clients should be located as close as possible to this cluster. Currently only zones are supported, so values should be of the form `projects/{project}/locations/{zone}`. |
| name                 | core | string        | The unique name of the cluster. Values are of the form `projects/{project}/instances/{instance}/clusters/a-z*`.                                                                                                                                                         |
| node_scaling_factor  | core | string        | Immutable. The node scaling factor of this cluster.                                                                                                                                                                                                                     |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| serve_nodes          | core | int64         | The number of nodes in the cluster. If no value is set, Cloud Bigtable automatically allocates nodes based on your data footprint and optimized for 50% storage utilization.                                                                                            |
| state                | core | string        | Output only. The current state of the cluster.                                                                                                                                                                                                                          |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
