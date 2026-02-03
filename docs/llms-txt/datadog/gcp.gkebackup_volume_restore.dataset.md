# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.gkebackup_volume_restore.dataset.md

---
title: Backup for GKE Volume Restore
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Backup for GKE Volume Restore
---

# Backup for GKE Volume Restore

Backup for GKE Volume Restore in Google Cloud is a feature that allows you to recover persistent volumes associated with Google Kubernetes Engine workloads from backups. It restores data to a previous state, helping recover from data loss, corruption, or accidental deletion. This resource ensures application consistency and supports restoring volumes to the same or different clusters, improving disaster recovery and business continuity.

```
gcp.gkebackup_volume_restore
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                      | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| complete_time        | core | timestamp     | Output only. The timestamp when the associated underlying volume restoration completed.                                                                                                                                                                                                                                        |
| create_time          | core | timestamp     | Output only. The timestamp when this VolumeRestore resource was created.                                                                                                                                                                                                                                                       |
| datadog_display_name | core | string        |
| etag                 | core | string        | Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a volume restore from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform volume restore updates in order to avoid race conditions. |
| labels               | core | array<string> |
| name                 | core | string        | Output only. Full name of the VolumeRestore resource. Format: `projects/*/locations/*/restorePlans/*/restores/*/volumeRestores/*`                                                                                                                                                                                              |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. The current state of this VolumeRestore.                                                                                                                                                                                                                                                                          |
| state_message        | core | string        | Output only. A human readable message explaining why the VolumeRestore is in its current state.                                                                                                                                                                                                                                |
| tags                 | core | hstore_csv    |
| target_pvc           | core | json          | Output only. The reference to the target Kubernetes PVC to be restored.                                                                                                                                                                                                                                                        |
| uid                  | core | string        | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format.                                                                                                                                                                                          |
| update_time          | core | timestamp     | Output only. The timestamp when this VolumeRestore resource was last updated.                                                                                                                                                                                                                                                  |
| volume_backup        | core | string        | Output only. The full name of the VolumeBackup from which the volume will be restored. Format: `projects/*/locations/*/backupPlans/*/backups/*/volumeBackups/*`.                                                                                                                                                               |
| volume_handle        | core | string        | Output only. A storage system-specific opaque handler to the underlying volume created for the target PVC from the volume backup.                                                                                                                                                                                              |
| volume_type          | core | string        | Output only. The type of volume provisioned                                                                                                                                                                                                                                                                                    |
| zone_id              | core | string        |
