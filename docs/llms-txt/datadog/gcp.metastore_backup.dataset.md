# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.metastore_backup.dataset.md

---
title: Dataproc Metastore Backup
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataproc Metastore Backup
---

# Dataproc Metastore Backup

Dataproc Metastore Backup is a Google Cloud resource that creates a backup of a Dataproc Metastore service, preserving metadata such as table definitions, schemas, and configurations. It enables recovery of the metastore to a previous state in case of data loss or corruption, supporting data protection and disaster recovery strategies.

```
gcp.metastore_backup
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                          | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The time when the backup was started.                                                                                                                                 |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. The description of the backup.                                                                                                                                           |
| end_time             | core | timestamp     | Output only. The time when the backup finished creating.                                                                                                                           |
| labels               | core | array<string> |
| name                 | core | string        | Immutable. Identifier. The relative resource name of the backup, in the following form:projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id} |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| restoring_services   | core | array<string> | Output only. Services that are restoring from the backup.                                                                                                                          |
| service_revision     | core | json          | Output only. The revision of the service at the time of backup.                                                                                                                    |
| state                | core | string        | Output only. The current state of the backup.                                                                                                                                      |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
