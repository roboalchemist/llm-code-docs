# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rds_cluster_snapshot.dataset.md

---
title: RDS Cluster Snapshot
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > RDS Cluster Snapshot
---

# RDS Cluster Snapshot

This table represents the RDS Cluster Snapshot resource from Amazon Web Services.

```
aws.rds_cluster_snapshot
```

## Fields

| Title                                 | ID   | Type          | Data Type                                                                                                                                                                                                                                | Description |
| ------------------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                  | core | string        |
| account_id                            | core | string        |
| allocated_storage                     | core | int64         | The allocated storage size of the DB cluster snapshot in gibibytes (GiB).                                                                                                                                                                |
| availability_zones                    | core | array<string> | The list of Availability Zones (AZs) where instances in the DB cluster snapshot can be restored.                                                                                                                                         |
| cluster_create_time                   | core | timestamp     | The time when the DB cluster was created, in Universal Coordinated Time (UTC).                                                                                                                                                           |
| db_cluster_identifier                 | core | string        | The DB cluster identifier of the DB cluster that this DB cluster snapshot was created from.                                                                                                                                              |
| db_cluster_resource_id                | core | string        | The resource ID of the DB cluster that this DB cluster snapshot was created from.                                                                                                                                                        |
| db_cluster_snapshot_arn               | core | string        | The Amazon Resource Name (ARN) for the DB cluster snapshot.                                                                                                                                                                              |
| db_cluster_snapshot_attributes_result | core | json          |
| db_cluster_snapshot_identifier        | core | string        | The identifier for the DB cluster snapshot.                                                                                                                                                                                              |
| db_system_id                          | core | string        | Reserved for future use.                                                                                                                                                                                                                 |
| engine                                | core | string        | The name of the database engine for this DB cluster snapshot.                                                                                                                                                                            |
| engine_mode                           | core | string        | The engine mode of the database engine for this DB cluster snapshot.                                                                                                                                                                     |
| engine_version                        | core | string        | The version of the database engine for this DB cluster snapshot.                                                                                                                                                                         |
| iam_database_authentication_enabled   | core | bool          | Indicates whether mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts is enabled.                                                                                                          |
| kms_key_id                            | core | string        | If <code>StorageEncrypted</code> is true, the Amazon Web Services KMS key identifier for the encrypted DB cluster snapshot. The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. |
| license_model                         | core | string        | The license model information for this DB cluster snapshot.                                                                                                                                                                              |
| master_username                       | core | string        | The master username for this DB cluster snapshot.                                                                                                                                                                                        |
| percent_progress                      | core | int64         | The percentage of the estimated data that has been transferred.                                                                                                                                                                          |
| port                                  | core | int64         | The port that the DB cluster was listening on at the time of the snapshot.                                                                                                                                                               |
| snapshot_create_time                  | core | timestamp     | The time when the snapshot was taken, in Universal Coordinated Time (UTC).                                                                                                                                                               |
| snapshot_type                         | core | string        | The type of the DB cluster snapshot.                                                                                                                                                                                                     |
| source_db_cluster_snapshot_arn        | core | string        | If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.                                                                     |
| status                                | core | string        | The status of this DB cluster snapshot. Valid statuses are the following: <ul> <li> <code>available</code> </li> <li> <code>copying</code> </li> <li> <code>creating</code> </li> </ul>                                                  |
| storage_encrypted                     | core | bool          | Indicates whether the DB cluster snapshot is encrypted.                                                                                                                                                                                  |
| storage_throughput                    | core | int64         | The storage throughput for the DB cluster snapshot. The throughput is automatically set based on the IOPS that you provision, and is not configurable. This setting is only for non-Aurora Multi-AZ DB clusters.                         |
| storage_type                          | core | string        | The storage type associated with the DB cluster snapshot. This setting is only for Aurora DB clusters.                                                                                                                                   |
| tags                                  | core | hstore_csv    |
| vpc_id                                | core | string        | The VPC ID associated with the DB cluster snapshot.                                                                                                                                                                                      |
