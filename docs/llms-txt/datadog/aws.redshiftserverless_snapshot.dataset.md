# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.redshiftserverless_snapshot.dataset.md

---
title: Redshift Serverless Snapshot
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Redshift Serverless Snapshot
---

# Redshift Serverless Snapshot

A Redshift Serverless Snapshot in AWS is a point-in-time backup of a Redshift Serverless workgroup. It captures the state of data and configurations, allowing you to restore or recover workloads if needed. Snapshots can be automated or created manually, providing data protection and disaster recovery for analytics environments without managing infrastructure.

```
aws.redshiftserverless_snapshot
```

## Fields

| Title                                        | ID   | Type          | Data Type                                                                                                          | Description |
| -------------------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                                         | core | string        |
| account_id                                   | core | string        |
| accounts_with_provisioned_restore_access     | core | array<string> | All of the Amazon Web Services accounts that have access to restore a snapshot to a provisioned cluster.           |
| accounts_with_restore_access                 | core | array<string> | All of the Amazon Web Services accounts that have access to restore a snapshot to a namespace.                     |
| actual_incremental_backup_size_in_mega_bytes | core | float64       | The size of the incremental backup in megabytes.                                                                   |
| admin_password_secret_arn                    | core | string        | The Amazon Resource Name (ARN) for the namespace's admin user credentials secret.                                  |
| admin_password_secret_kms_key_id             | core | string        | The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. |
| admin_username                               | core | string        | The username of the database within a snapshot.                                                                    |
| backup_progress_in_mega_bytes                | core | float64       | The size in megabytes of the data that has been backed up to a snapshot.                                           |
| current_backup_rate_in_mega_bytes_per_second | core | float64       | The rate at which data is backed up into a snapshot in megabytes per second.                                       |
| elapsed_time_in_seconds                      | core | int64         | The amount of time it took to back up data into a snapshot.                                                        |
| estimated_seconds_to_completion              | core | int64         | The estimated amount of seconds until the snapshot completes backup.                                               |
| kms_key_id                                   | core | string        | The unique identifier of the KMS key used to encrypt the snapshot.                                                 |
| namespace_arn                                | core | string        | The Amazon Resource Name (ARN) of the namespace the snapshot was created from.                                     |
| namespace_name                               | core | string        | The name of the namepsace.                                                                                         |
| owner_account                                | core | string        | The owner Amazon Web Services; account of the snapshot.                                                            |
| snapshot_arn                                 | core | string        | The Amazon Resource Name (ARN) of the snapshot.                                                                    |
| snapshot_create_time                         | core | timestamp     | The timestamp of when the snapshot was created.                                                                    |
| snapshot_name                                | core | string        | The name of the snapshot.                                                                                          |
| snapshot_remaining_days                      | core | int64         | The amount of days until the snapshot is deleted.                                                                  |
| snapshot_retention_period                    | core | int64         | The period of time, in days, of how long the snapshot is retained.                                                 |
| snapshot_retention_start_time                | core | timestamp     | The timestamp of when data within the snapshot started getting retained.                                           |
| status                                       | core | string        | The status of the snapshot.                                                                                        |
| tags                                         | core | hstore_csv    |
| total_backup_size_in_mega_bytes              | core | float64       | The total size, in megabytes, of how big the snapshot is.                                                          |
