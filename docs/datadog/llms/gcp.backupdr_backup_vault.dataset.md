# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.backupdr_backup_vault.dataset.md

---
title: Backup Vault
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Backup Vault
---

# Backup Vault

A Backup Vault in Google Cloud is a managed container that securely stores backup data for various GCP services. It centralizes backup management, enabling consistent policies, retention settings, and access controls. The vault ensures data durability, encryption, and compliance with organizational or regulatory requirements.

```
gcp.backupdr_backup_vault
```

## Fields

| Title                                      | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                    | Description |
| ------------------------------------------ | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                       | core | string        |
| access_restriction                         | core | string        | Optional. Note: This field is added for future use case and will not be supported in the current release. Access restriction for the backup vault. Default value is WITHIN_ORGANIZATION if not provided during creation.                                                                                                     |
| ancestors                                  | core | array<string> |
| annotations                                | core | hstore        | Optional. User annotations. See https://google.aip.dev/128#annotations Stores small amounts of arbitrary data.                                                                                                                                                                                                               |
| backup_count                               | core | int64         | Output only. The number of backups in this backup vault.                                                                                                                                                                                                                                                                     |
| backup_minimum_enforced_retention_duration | core | string        | Required. The default and minimum enforced retention for each backup within the backup vault. The enforced retention for each backup can be extended. Note: Longer minimum enforced retention period impacts potential storage costs post introductory trial. We recommend starting with a short duration of 3 days or less. |
| create_time                                | core | timestamp     | Output only. The time when the instance was created.                                                                                                                                                                                                                                                                         |
| datadog_display_name                       | core | string        |
| deletable                                  | core | bool          | Output only. Set to true when there are no backups nested under this resource.                                                                                                                                                                                                                                               |
| description                                | core | string        | Optional. The description of the BackupVault instance (2048 characters or less).                                                                                                                                                                                                                                             |
| effective_time                             | core | timestamp     | Optional. Time after which the BackupVault resource is locked.                                                                                                                                                                                                                                                               |
| etag                                       | core | string        | Optional. Server specified ETag for the backup vault resource to prevent simultaneous updates from overwiting each other.                                                                                                                                                                                                    |
| labels                                     | core | array<string> | Optional. Resource labels to represent user provided metadata. No labels currently defined:                                                                                                                                                                                                                                  |
| name                                       | core | string        | Output only. Identifier. Name of the backup vault to create. It must have the format`"projects/{project}/locations/{location}/backupVaults/{backupvault}"`. `{backupvault}` cannot be changed after creation. It must be between 3-63 characters long and must be unique within the project and location.                    |
| organization_id                            | core | string        |
| parent                                     | core | string        |
| project_id                                 | core | string        |
| project_number                             | core | string        |
| region_id                                  | core | string        |
| resource_name                              | core | string        |
| service_account                            | core | string        | Output only. Service account used by the BackupVault Service for this BackupVault. The user should grant this account permissions in their workload project to enable the service to run backups and restores there.                                                                                                         |
| state                                      | core | string        | Output only. The BackupVault resource instance state.                                                                                                                                                                                                                                                                        |
| tags                                       | core | hstore_csv    |
| total_stored_bytes                         | core | int64         | Output only. Total size of the storage used by all backup resources.                                                                                                                                                                                                                                                         |
| uid                                        | core | string        | Output only. Immutable after resource creation until resource deletion.                                                                                                                                                                                                                                                      |
| update_time                                | core | timestamp     | Output only. The time when the instance was updated.                                                                                                                                                                                                                                                                         |
| zone_id                                    | core | string        |
