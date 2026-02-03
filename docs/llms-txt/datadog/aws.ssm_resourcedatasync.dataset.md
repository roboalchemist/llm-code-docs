# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ssm_resourcedatasync.dataset.md

---
title: Systems Manager Resource Data Sync
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Systems Manager Resource Data Sync
---

# Systems Manager Resource Data Sync

This table represents the Systems Manager Resource Data Sync resource from Amazon Web Services.

```
aws.ssm_resourcedatasync
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                             | Description |
| ------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| last_status               | core | string     | The status reported by the last sync.                                                                                                                                                                                                                                                                                                 |
| last_successful_sync_time | core | timestamp  | The last time the sync operations returned a status of <code>SUCCESSFUL</code> (UTC).                                                                                                                                                                                                                                                 |
| last_sync_status_message  | core | string     | The status message details reported by the last sync.                                                                                                                                                                                                                                                                                 |
| last_sync_time            | core | timestamp  | The last time the configuration attempted to sync (UTC).                                                                                                                                                                                                                                                                              |
| s3_destination            | core | json       | Configuration information for the target S3 bucket.                                                                                                                                                                                                                                                                                   |
| sync_created_time         | core | timestamp  | The date and time the configuration was created (UTC).                                                                                                                                                                                                                                                                                |
| sync_last_modified_time   | core | timestamp  | The date and time the resource data sync was changed.                                                                                                                                                                                                                                                                                 |
| sync_name                 | core | string     | The name of the resource data sync.                                                                                                                                                                                                                                                                                                   |
| sync_source               | core | json       | Information about the source where the data was synchronized.                                                                                                                                                                                                                                                                         |
| sync_type                 | core | string     | The type of resource data sync. If <code>SyncType</code> is <code>SyncToDestination</code>, then the resource data sync synchronizes data to an S3 bucket. If the <code>SyncType</code> is <code>SyncFromSource</code> then the resource data sync synchronizes data from Organizations or from multiple Amazon Web Services Regions. |
| tags                      | core | hstore_csv |
