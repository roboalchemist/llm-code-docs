# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.memorydb_cluster.dataset.md

---
title: MemoryDB Cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MemoryDB Cluster
---

# MemoryDB Cluster

MemoryDB Cluster is a fully managed, Redis-compatible, in-memory database service in AWS designed for ultra-fast performance and high availability. It stores data in memory for microsecond read and write latency, making it ideal for real-time applications such as caching, session stores, leaderboards, and analytics. The cluster supports automatic failover, multi-AZ replication, and encryption for durability and security.

```
aws.memorydb_cluster
```

## Fields

| Title                             | ID   | Type       | Data Type                                                                                                                                                                                                                     | Description |
| --------------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                              | core | string     |
| account_id                        | core | string     |
| acl_name                          | core | string     | The name of the Access Control List associated with this cluster.                                                                                                                                                             |
| arn                               | core | string     | The Amazon Resource Name (ARN) of the cluster.                                                                                                                                                                                |
| auto_minor_version_upgrade        | core | bool       | When set to true, the cluster will automatically receive minor engine version upgrades after launch.                                                                                                                          |
| availability_mode                 | core | string     | Indicates if the cluster has a Multi-AZ configuration (multiaz) or not (singleaz).                                                                                                                                            |
| cluster_endpoint                  | core | json       | The cluster's configuration endpoint                                                                                                                                                                                          |
| clusters                          | core | json       | The clusters in this multi-Region cluster.                                                                                                                                                                                    |
| data_tiering                      | core | string     | Enables data tiering. Data tiering is only supported for clusters using the r6gd node type. This parameter must be set when using r6gd nodes. For more information, see Data tiering.                                         |
| description                       | core | string     | A description of the cluster                                                                                                                                                                                                  |
| engine                            | core | string     | The name of the engine used by the cluster.                                                                                                                                                                                   |
| engine_patch_version              | core | string     | The Redis OSS engine patch version used by the cluster                                                                                                                                                                        |
| engine_version                    | core | string     | The Redis OSS engine version used by the cluster                                                                                                                                                                              |
| kms_key_id                        | core | string     | The ID of the KMS key used to encrypt the cluster                                                                                                                                                                             |
| maintenance_window                | core | string     | Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. |
| multi_region_cluster_name         | core | string     | The name of the multi-Region cluster that this cluster belongs to.                                                                                                                                                            |
| multi_region_parameter_group_name | core | string     | The name of the multi-Region parameter group associated with the cluster.                                                                                                                                                     |
| name                              | core | string     | The user-supplied name of the cluster. This identifier is a unique key that identifies a cluster.                                                                                                                             |
| node_type                         | core | string     | The cluster's node type                                                                                                                                                                                                       |
| number_of_shards                  | core | int64      | The number of shards in the cluster                                                                                                                                                                                           |
| parameter_group_name              | core | string     | The name of the parameter group used by the cluster                                                                                                                                                                           |
| parameter_group_status            | core | string     | The status of the parameter group used by the cluster, for example 'active' or 'applying'.                                                                                                                                    |
| pending_updates                   | core | json       | A group of settings that are currently being applied.                                                                                                                                                                         |
| security_groups                   | core | json       | A list of security groups used by the cluster                                                                                                                                                                                 |
| shards                            | core | json       | A list of shards that are members of the cluster.                                                                                                                                                                             |
| snapshot_retention_limit          | core | int64      | The number of days for which MemoryDB retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.     |
| snapshot_window                   | core | string     | The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your shard. Example: 05:00-09:00 If you do not specify this parameter, MemoryDB automatically chooses an appropriate time range.        |
| sns_topic_arn                     | core | string     | The Amazon Resource Name (ARN) of the SNS notification topic                                                                                                                                                                  |
| sns_topic_status                  | core | string     | The SNS topic must be in Active status to receive notifications                                                                                                                                                               |
| status                            | core | string     | The status of the cluster. For example, Available, Updating, Creating.                                                                                                                                                        |
| subnet_group_name                 | core | string     | The name of the subnet group used by the cluster                                                                                                                                                                              |
| tags                              | core | hstore_csv |
| tls_enabled                       | core | bool       | A flag to indicate if In-transit encryption is enabled                                                                                                                                                                        |
