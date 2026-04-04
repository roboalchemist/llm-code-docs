# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.netapp_backup_vault.dataset.md

---
title: NetApp Backup Vault
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > NetApp Backup Vault
---

# NetApp Backup Vault

NetApp Backup Vault on Google Cloud is a managed storage service that securely stores backups of Cloud Volumes ONTAP and Cloud Volumes Service data. It provides long-term, cost-effective, and durable backup retention with integrated data protection and recovery capabilities.

```
gcp.netapp_backup_vault
```

## Fields

| Title                    | ID   | Type          | Data Type                                                                                                                                           | Description |
| ------------------------ | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string        |
| ancestors                | core | array<string> |
| backup_region            | core | string        | Optional. Region where the backups are stored. Format: `projects/{project_id}/locations/{location}`                                                 |
| backup_vault_type        | core | string        | Optional. Type of backup vault to be created. Default is IN_REGION.                                                                                 |
| create_time              | core | timestamp     | Output only. Create time of the backup vault.                                                                                                       |
| datadog_display_name     | core | string        |
| description              | core | string        | Description of the backup vault.                                                                                                                    |
| destination_backup_vault | core | string        | Output only. Name of the Backup vault created in backup region. Format: `projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}` |
| labels                   | core | array<string> | Resource labels to represent user provided metadata.                                                                                                |
| name                     | core | string        | Identifier. The resource name of the backup vault. Format: `projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}`.             |
| organization_id          | core | string        |
| parent                   | core | string        |
| project_id               | core | string        |
| project_number           | core | string        |
| region_id                | core | string        |
| resource_name            | core | string        |
| source_backup_vault      | core | string        | Output only. Name of the Backup vault created in source region. Format: `projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}` |
| source_region            | core | string        | Output only. Region in which the backup vault is created. Format: `projects/{project_id}/locations/{location}`                                      |
| state                    | core | string        | Output only. The backup vault state.                                                                                                                |
| tags                     | core | hstore_csv    |
| zone_id                  | core | string        |
