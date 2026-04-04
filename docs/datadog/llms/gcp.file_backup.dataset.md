# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.file_backup.dataset.md

---
title: Backup for Google Cloud FileStore
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Backup for Google Cloud FileStore
---

# Backup for Google Cloud FileStore

Backup for Google Cloud Filestore allows you to create and manage backups of your Filestore instances. These backups capture the file system data at a point in time, enabling you to protect against data loss, restore to a previous state, or replicate data across regions. This resource helps ensure business continuity and simplifies disaster recovery for applications relying on Filestore.

```
gcp.file_backup
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                               | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| capacity_gb          | core | int64         | Output only. Capacity of the source file share when the backup was created.                                                                                                             |
| create_time          | core | timestamp     | Output only. The time when the backup was created.                                                                                                                                      |
| datadog_display_name | core | string        |
| description          | core | string        | A description of the backup with 2048 characters or less. Requests with longer descriptions will be rejected.                                                                           |
| download_bytes       | core | int64         | Output only. Amount of bytes that will be downloaded if the backup is restored. This may be different than storage bytes, since sequential backups of the same disk will share storage. |
| file_system_protocol | core | string        | Output only. The file system protocol of the source Filestore instance that this backup is created from.                                                                                |
| labels               | core | array<string> | Resource labels to represent user provided metadata.                                                                                                                                    |
| name                 | core | string        | Output only. The resource name of the backup, in the format `projects/{project_number}/locations/{location_id}/backups/{backup_id}`.                                                    |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| satisfies_pzi        | core | bool          | Output only. Reserved for future use.                                                                                                                                                   |
| satisfies_pzs        | core | bool          | Output only. Reserved for future use.                                                                                                                                                   |
| source_file_share    | core | string        | Name of the file share in the source Filestore instance that the backup is created from.                                                                                                |
| source_instance      | core | string        | The resource name of the source Filestore instance, in the format `projects/{project_number}/locations/{location_id}/instances/{instance_id}`, used to create this backup.              |
| source_instance_tier | core | string        | Output only. The service tier of the source Filestore instance that this backup is created from.                                                                                        |
| state                | core | string        | Output only. The backup state.                                                                                                                                                          |
| storage_bytes        | core | int64         | Output only. The size of the storage used by the backup. As backups share storage, this number is expected to change with backup creation/deletion.                                     |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
