# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.gkebackup_volume_backup.dataset.md

---
title: VolumeBackup
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VolumeBackup
---

# VolumeBackup

A VolumeBackup in Google Cloud is a point-in-time copy of a persistent disk or volume used for data protection and recovery. It allows users to back up data from persistent disks, store it securely, and restore it when needed. This helps ensure business continuity and data durability in case of accidental deletion, corruption, or system failure.

```
gcp.gkebackup_volume_backup
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                              | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| complete_time        | core | timestamp     | Output only. The timestamp when the associated underlying volume backup operation completed.                                                                                                                                                                                                                                                           |
| create_time          | core | timestamp     | Output only. The timestamp when this VolumeBackup resource was created.                                                                                                                                                                                                                                                                                |
| datadog_display_name | core | string        |
| disk_size_bytes      | core | int64         | Output only. The minimum size of the disk to which this VolumeBackup can be restored.                                                                                                                                                                                                                                                                  |
| etag                 | core | string        | Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a volume backup from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform volume backup updates in order to avoid race conditions.                           |
| format               | core | string        | Output only. The format used for the volume backup.                                                                                                                                                                                                                                                                                                    |
| labels               | core | array<string> |
| name                 | core | string        | Output only. The full name of the VolumeBackup resource. Format: `projects/*/locations/*/backupPlans/*/backups/*/volumeBackups/*`.                                                                                                                                                                                                                     |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| satisfies_pzi        | core | bool          | Output only. [Output Only] Reserved for future use.                                                                                                                                                                                                                                                                                                    |
| satisfies_pzs        | core | bool          | Output only. [Output Only] Reserved for future use.                                                                                                                                                                                                                                                                                                    |
| source_pvc           | core | json          | Output only. A reference to the source Kubernetes PVC from which this VolumeBackup was created.                                                                                                                                                                                                                                                        |
| state                | core | string        | Output only. The current state of this VolumeBackup.                                                                                                                                                                                                                                                                                                   |
| state_message        | core | string        | Output only. A human readable message explaining why the VolumeBackup is in its current state. This field is only meant for human consumption and should not be used programmatically as this field is not guaranteed to be consistent.                                                                                                                |
| storage_bytes        | core | int64         | Output only. The aggregate size of the underlying artifacts associated with this VolumeBackup in the backup storage. This may change over time when multiple backups of the same volume share the same backup storage location. In particular, this is likely to increase in size when the immediately preceding backup of the same volume is deleted. |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format.                                                                                                                                                                                                                  |
| update_time          | core | timestamp     | Output only. The timestamp when this VolumeBackup resource was last updated.                                                                                                                                                                                                                                                                           |
| volume_backup_handle | core | string        | Output only. A storage system-specific opaque handle to the underlying volume backup.                                                                                                                                                                                                                                                                  |
| zone_id              | core | string        |
