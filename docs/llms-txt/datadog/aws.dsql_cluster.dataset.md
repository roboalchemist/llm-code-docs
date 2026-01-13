# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.dsql_cluster.dataset.md

---
title: DynamoDB Standard-Infrequent Access Cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > DynamoDB Standard-Infrequent Access
  Cluster
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.dsql_cluster.dataset/index.html
---

# DynamoDB Standard-Infrequent Access Cluster

DynamoDB Standard-Infrequent Access Cluster is a managed database cluster configuration in AWS DynamoDB designed for workloads that require durable storage with lower access frequency. It provides cost savings by offering reduced storage pricing for data that is not accessed often, while still maintaining the performance and scalability of DynamoDB when queries are made. This option is ideal for applications with large datasets where only a subset of data is frequently used, helping balance performance needs with cost efficiency.

```
aws.dsql_cluster
```

## Fields

| Title                       | ID   | Type      | Data Type                                                                                                        | Description |
| --------------------------- | ---- | --------- | ---------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string    |
| account_id                  | core | string    |
| arn                         | core | string    | The ARN of the retrieved cluster.                                                                                |
| creation_time               | core | timestamp | The time of when the cluster was created.                                                                        |
| deletion_protection_enabled | core | bool      | Whether deletion protection is enabled in this cluster.                                                          |
| identifier                  | core | string    | The ID of the retrieved cluster.                                                                                 |
| multi_region_properties     | core | json      | Returns the current multi-Region cluster configuration, including witness region and linked cluster information. |
| status                      | core | string    | The status of the retrieved cluster.                                                                             |
| tags                        | core | hstore    |
