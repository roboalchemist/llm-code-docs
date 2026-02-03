# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.bigtableadmin_backup.dataset.md

---
title: Cloud Bigtable Backup
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Bigtable Backup
---

# Cloud Bigtable Backup

Cloud Bigtable Backup in Google Cloud is a feature that lets you create consistent, point-in-time backups of your Bigtable tables. These backups are stored independently from the source data, ensuring protection against accidental deletions or corruption. You can restore a backup to a new table within the same instance or another instance in the same project and region. This helps with disaster recovery, data retention, and compliance needs without impacting the performance of the live database.

```
gcp.bigtableadmin_backup
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                            | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| backup_type          | core | string        | Indicates the backup type of the backup.                                                                                                                                                                                                                                                                                                                                                                             |
| datadog_display_name | core | string        |
| encryption_info      | core | json          | Output only. The encryption information for the backup.                                                                                                                                                                                                                                                                                                                                                              |
| end_time             | core | timestamp     | Output only. `end_time` is the time that the backup was finished. The row data in the backup will be no newer than this timestamp.                                                                                                                                                                                                                                                                                   |
| expire_time          | core | timestamp     | Required. The expiration time of the backup. When creating a backup or updating its `expire_time`, the value must be greater than the backup creation time by: - At least 6 hours - At most 90 days Once the `expire_time` has passed, Cloud Bigtable will delete the backup.                                                                                                                                        |
| hot_to_standard_time | core | timestamp     | The time at which the hot backup will be converted to a standard backup. Once the `hot_to_standard_time` has passed, Cloud Bigtable will convert the hot backup to a standard backup. This value must be greater than the backup creation time by: - At least 24 hours This field only applies for hot backups. When creating or updating a standard backup, attempting to set this field will fail the request.     |
| labels               | core | array<string> |
| name                 | core | string        | A globally unique identifier for the backup which cannot be changed. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/ backups/_a-zA-Z0-9*` The final segment of the name must be between 1 and 50 characters in length. The backup is stored in the cluster identified by the prefix of the backup name of the form `projects/{project}/instances/{instance}/clusters/{cluster}`. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| size_bytes           | core | int64         | Output only. Size of the backup in bytes.                                                                                                                                                                                                                                                                                                                                                                            |
| source_backup        | core | string        | Output only. Name of the backup from which this backup was copied. If a backup is not created by copying a backup, this field will be empty. Values are of the form: projects//instances//clusters//backups/                                                                                                                                                                                                         |
| source_table         | core | string        | Required. Immutable. Name of the table from which this backup was created. This needs to be in the same instance as the backup. Values are of the form `projects/{project}/instances/{instance}/tables/{source_table}`.                                                                                                                                                                                              |
| start_time           | core | timestamp     | Output only. `start_time` is the time that the backup was started (i.e. approximately the time the CreateBackup request is received). The row data in this backup will be no older than this timestamp.                                                                                                                                                                                                              |
| state                | core | string        | Output only. The current state of the backup.                                                                                                                                                                                                                                                                                                                                                                        |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
