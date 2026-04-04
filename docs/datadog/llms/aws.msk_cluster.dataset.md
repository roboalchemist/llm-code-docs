# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.msk_cluster.dataset.md

---
title: MSK Cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MSK Cluster
---

# MSK Cluster

This table represents the MSK Cluster resource from Amazon Web Services.

```
aws.msk_cluster
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                                                                   | Description |
| -------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| active_operation_arn | core | string     | The Amazon Resource Name (ARN) that uniquely identifies a cluster operation.                                                                |
| cluster_arn          | core | string     | The Amazon Resource Name (ARN) that uniquely identifies the cluster.                                                                        |
| cluster_name         | core | string     | The name of the cluster.                                                                                                                    |
| cluster_type         | core | string     | Cluster Type.                                                                                                                               |
| creation_time        | core | timestamp  | The time when the cluster was created.                                                                                                      |
| current_version      | core | string     | The current version of the MSK cluster.                                                                                                     |
| provisioned          | core | json       | Information about the provisioned cluster.                                                                                                  |
| serverless           | core | json       | Information about the serverless cluster.                                                                                                   |
| state                | core | string     | The state of the cluster. The possible states are ACTIVE, CREATING, DELETING, FAILED, HEALING, MAINTENANCE, REBOOTING_BROKER, and UPDATING. |
| state_info           | core | json       | State Info for the Amazon MSK cluster.                                                                                                      |
| tags                 | core | hstore_csv |
