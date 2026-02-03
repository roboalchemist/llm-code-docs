# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.kafka_replicator.dataset.md

---
title: MSK Replicator
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MSK Replicator
---

# MSK Replicator

MSK Replicator is an Amazon Managed Streaming for Apache Kafka (MSK) feature that enables replication of data between Kafka clusters. It helps synchronize topics across regions or environments, supporting disaster recovery, data migration, and multi-region architectures. This service simplifies cross-cluster data movement without requiring custom replication tools.

```
aws.kafka_replicator
```

## Fields

| Title                      | ID   | Type       | Data Type                                                                                                                                            | Description |
| -------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string     |
| account_id                 | core | string     |
| creation_time              | core | timestamp  | The time when the replicator was created.                                                                                                            |
| current_version            | core | string     | The current version number of the replicator.                                                                                                        |
| is_replicator_reference    | core | bool       | Whether this resource is a replicator reference.                                                                                                     |
| kafka_clusters             | core | json       | Kafka Clusters used in setting up sources / targets for replication.                                                                                 |
| replication_info_list      | core | json       | A list of replication configurations, where each configuration targets a given source cluster to target cluster replication flow.                    |
| replicator_arn             | core | string     | The Amazon Resource Name (ARN) of the replicator.                                                                                                    |
| replicator_description     | core | string     | The description of the replicator.                                                                                                                   |
| replicator_name            | core | string     | The name of the replicator.                                                                                                                          |
| replicator_resource_arn    | core | string     | The Amazon Resource Name (ARN) of the replicator resource in the region where the replicator was created.                                            |
| replicator_state           | core | string     | State of the replicator.                                                                                                                             |
| service_execution_role_arn | core | string     | The Amazon Resource Name (ARN) of the IAM role used by the replicator to access resources in the customer's account (e.g source and target clusters) |
| state_info                 | core | json       | Details about the state of the replicator.                                                                                                           |
| tags                       | core | hstore_csv |
