# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.synapse_workspace_azure_ad_only_authentication.dataset.md

---
title: Synapse Workspace Azure Ad Only Authentication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Synapse Workspace Azure Ad Only
  Authentication
---

# Synapse Workspace Azure Ad Only Authentication

This table represents the synapse_workspace_azure_ad_only_authentication resource from Microsoft Azure.

```
azure.synapse_workspace_azure_ad_only_authentication
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                                                                                                                                 | Description |
| ---------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| azure_ad_only_authentication | core | bool       | Azure Active Directory only Authentication enabled.                                                                                                                                       |
| creation_date                | core | string     | property configuration date                                                                                                                                                               |
| id                           | core | string     | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| location                     | core | string     |
| name                         | core | string     | The name of the resource                                                                                                                                                                  |
| resource_group               | core | string     |
| state                        | core | string     | property configuration state                                                                                                                                                              |
| subscription_id              | core | string     |
| subscription_name            | core | string     |
| tags                         | core | hstore_csv |
| type                         | core | string     | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                 |
