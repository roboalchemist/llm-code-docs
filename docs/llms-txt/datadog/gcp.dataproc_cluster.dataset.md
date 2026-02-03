# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataproc_cluster.dataset.md

---
title: Dataproc Cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataproc Cluster
---

# Dataproc Cluster

A Dataproc Cluster in Google Cloud is a managed cluster of virtual machines optimized for running Apache Spark, Apache Hadoop, and other big data frameworks. It simplifies the setup, management, and scaling of distributed data processing environments, allowing users to focus on analytics and machine learning tasks instead of infrastructure.

```
gcp.dataproc_cluster
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                             | Description |
| ---------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| ancestors              | core | array<string> |
| cluster_name           | core | string        | Required. The cluster name, which must be unique within a project. The name must start with a lowercase letter, and can contain up to 51 lowercase letters, numbers, and hyphens. It cannot end with a hyphen. The name of a deleted cluster can be reused.                                                                                                                                                                           |
| cluster_uuid           | core | string        | Output only. A cluster UUID (Unique Universal Identifier). Dataproc generates this value when it creates the cluster.                                                                                                                                                                                                                                                                                                                 |
| config                 | core | json          | Optional. The cluster config for a cluster of Compute Engine Instances. Note that Dataproc may set default values, and values may change when clusters are updated.Exactly one of ClusterConfig or VirtualClusterConfig must be specified.                                                                                                                                                                                            |
| datadog_display_name   | core | string        |
| gcp_status             | core | json          | Output only. Cluster status.                                                                                                                                                                                                                                                                                                                                                                                                          |
| labels                 | core | array<string> | Optional. The labels to associate with this cluster. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a cluster.                                                      |
| metrics                | core | json          | Output only. Contains cluster daemon metrics such as HDFS and YARN stats.Beta Feature: This report is available for testing purposes only. It may be changed before final release.                                                                                                                                                                                                                                                    |
| organization_id        | core | string        |
| parent                 | core | string        |
| project_id             | core | string        | Required. The Google Cloud Platform project ID that the cluster belongs to.                                                                                                                                                                                                                                                                                                                                                           |
| project_number         | core | string        |
| resource_name          | core | string        |
| status_history         | core | json          | Output only. The previous cluster status.                                                                                                                                                                                                                                                                                                                                                                                             |
| tags                   | core | hstore_csv    |
| virtual_cluster_config | core | json          | Optional. The virtual cluster config is used when creating a Dataproc cluster that does not directly control the underlying compute resources, for example, when creating a Dataproc-on-GKE cluster (https://cloud.google.com/dataproc/docs/guides/dpgke/dataproc-gke-overview). Dataproc may set default values, and values may change when clusters are updated. Exactly one of config or virtual_cluster_config must be specified. |
