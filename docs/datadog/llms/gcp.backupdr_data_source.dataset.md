# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.backupdr_data_source.dataset.md

---
title: Backup and DR Data Source
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Backup and DR Data Source
---

# Backup and DR Data Source

Backup and DR Data Source in Google Cloud provides access to backup and disaster recovery configurations and metadata. It allows users to retrieve information about backup plans, policies, and recovery points for managed resources. This helps ensure data protection, compliance, and quick restoration in case of data loss or system failure.

```
gcp.backupdr_data_source
```

## Fields

| Title                                      | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                               | Description |
| ------------------------------------------ | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                       | core | string        |
| ancestors                                  | core | array<string> |
| backup_blocked_by_vault_access_restriction | core | bool          | Output only. This field is set to true if the backup is blocked by vault access restriction.                                                                                                                                                                                                                            |
| backup_config_info                         | core | json          | Output only. Details of how the resource is configured for backup.                                                                                                                                                                                                                                                      |
| backup_count                               | core | int64         | Number of backups in the data source.                                                                                                                                                                                                                                                                                   |
| config_state                               | core | string        | Output only. The backup configuration state.                                                                                                                                                                                                                                                                            |
| create_time                                | core | timestamp     | Output only. The time when the instance was created.                                                                                                                                                                                                                                                                    |
| data_source_backup_appliance_application   | core | json          | The backed up resource is a backup appliance application.                                                                                                                                                                                                                                                               |
| data_source_gcp_resource                   | core | json          | The backed up resource is a Google Cloud resource. The word 'DataSource' was included in the names to indicate that this is the representation of the Google Cloud resource used within the DataSource object.                                                                                                          |
| datadog_display_name                       | core | string        |
| etag                                       | core | string        | Server specified ETag for the ManagementServer resource to prevent simultaneous updates from overwiting each other.                                                                                                                                                                                                     |
| labels                                     | core | array<string> | Optional. Resource labels to represent user provided metadata. No labels currently defined:                                                                                                                                                                                                                             |
| name                                       | core | string        | Output only. Identifier. Name of the datasource to create. It must have the format`"projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}"`. `{datasource}` cannot be changed after creation. It must be between 3-63 characters long and must be unique within the backup vault. |
| organization_id                            | core | string        |
| parent                                     | core | string        |
| project_id                                 | core | string        |
| project_number                             | core | string        |
| region_id                                  | core | string        |
| resource_name                              | core | string        |
| state                                      | core | string        | Output only. The DataSource resource instance state.                                                                                                                                                                                                                                                                    |
| tags                                       | core | hstore_csv    |
| total_stored_bytes                         | core | int64         | The number of bytes (metadata and data) stored in this datasource.                                                                                                                                                                                                                                                      |
| update_time                                | core | timestamp     | Output only. The time when the instance was updated.                                                                                                                                                                                                                                                                    |
| zone_id                                    | core | string        |
