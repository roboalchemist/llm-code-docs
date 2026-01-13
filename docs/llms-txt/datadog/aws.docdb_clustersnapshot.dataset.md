# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.docdb_clustersnapshot.dataset.md

---
title: DocumentDB Cluster Snapshot
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DocumentDB Cluster Snapshot
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.docdb_clustersnapshot.dataset/index.html
---

# DocumentDB Cluster Snapshot

This table represents the DocumentDB Cluster Snapshot resource from Amazon Web Services.

```
aws.docdb_clustersnapshot
```

## Fields

| Title                                 | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                     | Description |
| ------------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                  | core | string        |
| account_id                            | core | string        |
| availability_zones                    | core | array<string> | Provides the list of Amazon EC2 Availability Zones that instances in the cluster snapshot can be restored in.                                                                                                                                                                                                 |
| cluster_create_time                   | core | timestamp     | Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).                                                                                                                                                                                                                         |
| db_cluster_identifier                 | core | string        | Specifies the cluster identifier of the cluster that this cluster snapshot was created from.                                                                                                                                                                                                                  |
| db_cluster_snapshot_arn               | core | string        | The Amazon Resource Name (ARN) for the cluster snapshot.                                                                                                                                                                                                                                                      |
| db_cluster_snapshot_attributes_result | core | json          |
| db_cluster_snapshot_identifier        | core | string        | Specifies the identifier for the cluster snapshot.                                                                                                                                                                                                                                                            |
| engine                                | core | string        | Specifies the name of the database engine.                                                                                                                                                                                                                                                                    |
| engine_version                        | core | string        | Provides the version of the database engine for this cluster snapshot.                                                                                                                                                                                                                                        |
| kms_key_id                            | core | string        | If <code>StorageEncrypted</code> is <code>true</code>, the KMS key identifier for the encrypted cluster snapshot.                                                                                                                                                                                             |
| master_username                       | core | string        | Provides the master user name for the cluster snapshot.                                                                                                                                                                                                                                                       |
| percent_progress                      | core | int64         | Specifies the percentage of the estimated data that has been transferred.                                                                                                                                                                                                                                     |
| port                                  | core | int64         | Specifies the port that the cluster was listening on at the time of the snapshot.                                                                                                                                                                                                                             |
| snapshot_create_time                  | core | timestamp     | Provides the time when the snapshot was taken, in UTC.                                                                                                                                                                                                                                                        |
| snapshot_type                         | core | string        | Provides the type of the cluster snapshot.                                                                                                                                                                                                                                                                    |
| source_db_cluster_snapshot_arn        | core | string        | If the cluster snapshot was copied from a source cluster snapshot, the ARN for the source cluster snapshot; otherwise, a null value.                                                                                                                                                                          |
| status                                | core | string        | Specifies the status of this cluster snapshot.                                                                                                                                                                                                                                                                |
| storage_encrypted                     | core | bool          | Specifies whether the cluster snapshot is encrypted.                                                                                                                                                                                                                                                          |
| storage_type                          | core | string        | Storage type associated with your cluster snapshot For information on storage types for Amazon DocumentDB clusters, see Cluster storage configurations in the <i>Amazon DocumentDB Developer Guide</i>. Valid values for storage type - <code>standard | iopt1</code> Default value is <code>standard </code> |
| tags                                  | core | hstore        |
| vpc_id                                | core | string        | Provides the virtual private cloud (VPC) ID that is associated with the cluster snapshot.                                                                                                                                                                                                                     |
