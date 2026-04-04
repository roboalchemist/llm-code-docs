# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.firestore_backup.dataset.md

---
title: Firestore Backup and Restore
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Firestore Backup and Restore
---

# Firestore Backup and Restore

Firestore Backup and Restore is a managed Google Cloud service that automates the creation, storage, and recovery of Firestore database backups. It allows users to schedule regular backups, manage retention policies, and restore data to a specific point in time. This helps protect against data loss, corruption, or accidental deletions while ensuring compliance and business continuity.

```
gcp.firestore_backup
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                   | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| database             | core | string        | Output only. Name of the Firestore database that the backup is from. Format is `projects/{project}/databases/{database}`.                                                   |
| database_uid         | core | string        | Output only. The system-generated UUID4 for the Firestore database that the backup is from.                                                                                 |
| datadog_display_name | core | string        |
| expire_time          | core | timestamp     | Output only. The timestamp at which this backup expires.                                                                                                                    |
| labels               | core | array<string> |
| name                 | core | string        | Output only. The unique resource name of the Backup. Format is `projects/{project}/locations/{location}/backups/{backup}`.                                                  |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| snapshot_time        | core | timestamp     | Output only. The backup contains an externally consistent copy of the database at this time.                                                                                |
| state                | core | string        | Output only. The current state of the backup.                                                                                                                               |
| stats                | core | json          | Output only. Statistics about the backup. This data only becomes available after the backup is fully materialized to secondary storage. This field will be empty till then. |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
