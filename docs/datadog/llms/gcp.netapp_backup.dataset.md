# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.netapp_backup.dataset.md

---
title: NetApp Backup for Google Cloud
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > NetApp Backup for Google Cloud
---

# NetApp Backup for Google Cloud

NetApp Backup for Google Cloud is a managed backup service that provides secure, automated protection for data stored in NetApp Cloud Volumes ONTAP and Cloud Volumes Service. It enables efficient snapshot-based backups, long-term retention, and quick recovery options directly within Google Cloud. The service helps ensure data durability, compliance, and business continuity while minimizing operational overhead.

```
gcp.netapp_backup
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                            | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| backup_region        | core | string        | Output only. Region in which backup is stored. Format: `projects/{project_id}/locations/{location}`                                                                                                                                                  |
| backup_type          | core | string        | Output only. Type of backup, manually created or created by a backup policy.                                                                                                                                                                         |
| chain_storage_bytes  | core | int64         | Output only. Total size of all backups in a chain in bytes = baseline backup size + sum(incremental backup size)                                                                                                                                     |
| create_time          | core | timestamp     | Output only. The time when the backup was created.                                                                                                                                                                                                   |
| datadog_display_name | core | string        |
| description          | core | string        | A description of the backup with 2048 characters or less. Requests with longer descriptions will be rejected.                                                                                                                                        |
| labels               | core | array<string> | Resource labels to represent user provided metadata.                                                                                                                                                                                                 |
| name                 | core | string        | Identifier. The resource name of the backup. Format: `projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}/backups/{backup_id}`.                                                                                                |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| satisfies_pzi        | core | bool          | Output only. Reserved for future use                                                                                                                                                                                                                 |
| satisfies_pzs        | core | bool          | Output only. Reserved for future use                                                                                                                                                                                                                 |
| source_snapshot      | core | string        | If specified, backup will be created from the given snapshot. If not specified, there will be a new snapshot taken to initiate the backup creation. Format: `projects/{project_id}/locations/{location}/volumes/{volume_id}/snapshots/{snapshot_id}` |
| source_volume        | core | string        | Volume full name of this backup belongs to. Format: `projects/{projects_id}/locations/{location}/volumes/{volume_id}`                                                                                                                                |
| state                | core | string        | Output only. The backup state.                                                                                                                                                                                                                       |
| tags                 | core | hstore_csv    |
| volume_region        | core | string        | Output only. Region of the volume from which the backup was created. Format: `projects/{project_id}/locations/{location}`                                                                                                                            |
| volume_usage_bytes   | core | int64         | Output only. Size of the file system when the backup was created. When creating a new volume from the backup, the volume capacity will have to be at least as big.                                                                                   |
| zone_id              | core | string        |
