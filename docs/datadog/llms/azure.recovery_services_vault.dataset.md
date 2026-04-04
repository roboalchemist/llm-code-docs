# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.recovery_services_vault.dataset.md

---
title: Recovery Services Vault
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Recovery Services Vault
---

# Recovery Services Vault

This table represents the Recovery Services Vault resource from Microsoft Azure.

```
azure.recovery_services_vault
```

## Fields

| Title                                    | ID   | Type       | Data Type                                                                                      | Description |
| ---------------------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------- | ----------- |
| _key                                     | core | string     |
| encryption                               | core | json       | Customer Managed Key details of the resource.                                                  |
| etag                                     | core | string     | Optional ETag.                                                                                 |
| id                                       | core | string     | Resource Id represents the complete path to the resource.                                      |
| identity                                 | core | json       |
| location                                 | core | string     | Resource location.                                                                             |
| move_details                             | core | json       | The details of the latest move operation performed on the Azure Resource                       |
| move_state                               | core | string     | The State of the Resource after the move operation                                             |
| name                                     | core | string     | Resource name associated with the resource.                                                    |
| private_endpoint_connections             | core | json       | List of private endpoint connection.                                                           |
| private_endpoint_state_for_backup        | core | string     | Private endpoint state for backup.                                                             |
| private_endpoint_state_for_site_recovery | core | string     | Private endpoint state for site recovery.                                                      |
| provisioning_state                       | core | string     | Provisioning State.                                                                            |
| resource_group                           | core | string     |
| sku                                      | core | json       |
| subscription_id                          | core | string     |
| subscription_name                        | core | string     |
| system_data                              | core | json       |
| tags                                     | core | hstore_csv |
| type                                     | core | string     | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
| upgrade_details                          | core | json       |
