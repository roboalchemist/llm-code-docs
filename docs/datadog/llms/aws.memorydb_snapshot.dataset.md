# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.memorydb_snapshot.dataset.md

---
title: MemoryDB Snapshot
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MemoryDB Snapshot
---

# MemoryDB Snapshot

A MemoryDB Snapshot in AWS is a point-in-time backup of a MemoryDB for Redis cluster. It captures the data stored in the cluster, allowing you to restore it later for recovery, cloning, or migration purposes. Snapshots can be created manually or automatically based on retention policies.

```
aws.memorydb_snapshot
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                                                                                                                             | Description |
| --------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| arn                   | core | string     | The ARN (Amazon Resource Name) of the snapshot.                                                                                                                                       |
| cluster_configuration | core | json       | The configuration of the cluster from which the snapshot was taken                                                                                                                    |
| data_tiering          | core | string     | Enables data tiering. Data tiering is only supported for clusters using the r6gd node type. This parameter must be set when using r6gd nodes. For more information, see Data tiering. |
| kms_key_id            | core | string     | The ID of the KMS key used to encrypt the snapshot.                                                                                                                                   |
| name                  | core | string     | The name of the snapshot                                                                                                                                                              |
| status                | core | string     | The status of the snapshot. Valid values: creating | available | restoring | copying | deleting.                                                                                      |
| tags                  | core | hstore_csv |
