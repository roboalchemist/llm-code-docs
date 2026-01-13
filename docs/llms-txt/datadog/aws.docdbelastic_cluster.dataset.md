# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.docdbelastic_cluster.dataset.md

---
title: DocumentDB Elastic Cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DocumentDB Elastic Cluster
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.docdbelastic_cluster.dataset/index.html
---

# DocumentDB Elastic Cluster

DocumentDB Elastic Cluster is a fully managed, scalable cluster for Amazon DocumentDB that automatically adjusts capacity to handle variable workloads. It provides elastic scaling of compute and storage, making it easier to run document-based applications without manual provisioning. This resource is designed for high availability, security, and integration with other AWS services, while reducing operational overhead.

```
aws.docdbelastic_cluster
```

## Fields

| Title                        | ID   | Type          | Data Type                                                                                                                                                                                                                                    | Description |
| ---------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string        |
| account_id                   | core | string        |
| admin_user_name              | core | string        | The name of the elastic cluster administrator.                                                                                                                                                                                               |
| auth_type                    | core | string        | The authentication type for the elastic cluster.                                                                                                                                                                                             |
| backup_retention_period      | core | int64         | The number of days for which automatic snapshots are retained.                                                                                                                                                                               |
| cluster_arn                  | core | string        | The ARN identifier of the elastic cluster.                                                                                                                                                                                                   |
| cluster_endpoint             | core | string        | The URL used to connect to the elastic cluster.                                                                                                                                                                                              |
| cluster_name                 | core | string        | The name of the elastic cluster.                                                                                                                                                                                                             |
| create_time                  | core | string        | The time when the elastic cluster was created in Universal Coordinated Time (UTC).                                                                                                                                                           |
| kms_key_id                   | core | string        | The KMS key identifier to use to encrypt the elastic cluster.                                                                                                                                                                                |
| preferred_backup_window      | core | string        | The daily time range during which automated backups are created if automated backups are enabled, as determined by backupRetentionPeriod.                                                                                                    |
| preferred_maintenance_window | core | string        | The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC). Format: ddd:hh24:mi-ddd:hh24:mi                                                                                                        |
| shard_capacity               | core | int64         | The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.                                                                                                                           |
| shard_count                  | core | int64         | The number of shards assigned to the elastic cluster. Maximum is 32.                                                                                                                                                                         |
| shard_instance_count         | core | int64         | The number of replica instances applying to all shards in the cluster. A shardInstanceCount value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability. |
| shards                       | core | json          | The total number of shards in the cluster.                                                                                                                                                                                                   |
| status                       | core | string        | The status of the elastic cluster.                                                                                                                                                                                                           |
| subnet_ids                   | core | array<string> | The Amazon EC2 subnet IDs for the elastic cluster.                                                                                                                                                                                           |
| tags                         | core | hstore        |
| vpc_security_group_ids       | core | array<string> | A list of EC2 VPC security groups associated with thie elastic cluster.                                                                                                                                                                      |
