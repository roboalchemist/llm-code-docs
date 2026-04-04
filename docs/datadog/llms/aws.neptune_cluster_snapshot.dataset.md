# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.neptune_cluster_snapshot.dataset.md

---
title: Neptune Cluster Snapshot
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Neptune Cluster Snapshot
---

# Neptune Cluster Snapshot

This table represents the Neptune Cluster Snapshot resource from Amazon Web Services.

```
aws.neptune_cluster_snapshot
```

## Fields

| Title                               | ID   | Type          | Data Type                                                                                                                                                            | Description |
| ----------------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                | core | string        |
| account_id                          | core | string        |
| allocated_storage                   | core | int64         | Specifies the allocated storage size in gibibytes (GiB).                                                                                                             |
| availability_zones                  | core | array<string> | Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.                                                            |
| cluster_create_time                 | core | timestamp     | Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).                                                                             |
| cluster_snapshot_arn                | core | string        |
| db_cluster_identifier               | core | string        | Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was created from.                                                                |
| db_cluster_snapshot_arn             | core | string        | The Amazon Resource Name (ARN) for the DB cluster snapshot.                                                                                                          |
| db_cluster_snapshot_attributes      | core | json          | The list of attributes and values for the manual DB cluster snapshot.                                                                                                |
| db_cluster_snapshot_identifier      | core | string        | The identifier of the manual DB cluster snapshot that the attributes apply to.                                                                                       |
| engine                              | core | string        | Specifies the name of the database engine.                                                                                                                           |
| engine_version                      | core | string        | Provides the version of the database engine for this DB cluster snapshot.                                                                                            |
| iam_database_authentication_enabled | core | bool          | True if mapping of Amazon Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.                                        |
| kms_key_id                          | core | string        | If <code>StorageEncrypted</code> is true, the Amazon KMS key identifier for the encrypted DB cluster snapshot.                                                       |
| license_model                       | core | string        | Provides the license model information for this DB cluster snapshot.                                                                                                 |
| master_username                     | core | string        | Not supported by Neptune.                                                                                                                                            |
| percent_progress                    | core | int64         | Specifies the percentage of the estimated data that has been transferred.                                                                                            |
| port                                | core | int64         | Specifies the port that the DB cluster was listening on at the time of the snapshot.                                                                                 |
| snapshot_create_time                | core | timestamp     | Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).                                                                                  |
| snapshot_type                       | core | string        | Provides the type of the DB cluster snapshot.                                                                                                                        |
| source_db_cluster_snapshot_arn      | core | string        | If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value. |
| status                              | core | string        | Specifies the status of this DB cluster snapshot.                                                                                                                    |
| storage_encrypted                   | core | bool          | Specifies whether the DB cluster snapshot is encrypted.                                                                                                              |
| storage_type                        | core | string        | The storage type associated with the DB cluster snapshot.                                                                                                            |
| tags                                | core | hstore_csv    |
| vpc_id                              | core | string        | Provides the VPC ID associated with the DB cluster snapshot.                                                                                                         |
