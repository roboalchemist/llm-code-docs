# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.log_analytics_workspace.dataset.md

---
title: Log Analytics Workspace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Log Analytics Workspace
---

# Log Analytics Workspace

This table represents the Log Analytics Workspace resource from Microsoft Azure.

```
azure.log_analytics_workspace
```

## Fields

| Title                               | ID   | Type       | Data Type                                                                                                                                                                                 | Description |
| ----------------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                | core | string     |
| created_date                        | core | string     | Workspace creation date.                                                                                                                                                                  |
| customer_id                         | core | string     | This is a read-only property. Represents the ID associated with the workspace.                                                                                                            |
| etag                                | core | string     | The etag of the workspace.                                                                                                                                                                |
| features                            | core | json       | Workspace features.                                                                                                                                                                       |
| force_cmk_for_query                 | core | bool       | Indicates whether customer managed storage is mandatory for query management.                                                                                                             |
| id                                  | core | string     | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| location                            | core | string     | The geo-location where the resource lives                                                                                                                                                 |
| modified_date                       | core | string     | Workspace modification date.                                                                                                                                                              |
| name                                | core | string     | The name of the resource                                                                                                                                                                  |
| private_link_scoped_resources       | core | json       | List of linked private link scope resources.                                                                                                                                              |
| provisioning_state                  | core | string     | The provisioning state of the workspace.                                                                                                                                                  |
| public_network_access_for_ingestion | core | string     | The network access type for accessing Log Analytics ingestion.                                                                                                                            |
| public_network_access_for_query     | core | string     | The network access type for accessing Log Analytics query.                                                                                                                                |
| resource_group                      | core | string     |
| retention_in_days                   | core | int64      | The workspace data retention in days. Allowed values are per pricing plan. See pricing tiers documentation for details.                                                                   |
| sku                                 | core | json       | The SKU of the workspace.                                                                                                                                                                 |
| subscription_id                     | core | string     |
| subscription_name                   | core | string     |
| tags                                | core | hstore_csv |
| type                                | core | string     | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                 |
| workspace_capping                   | core | json       | The daily volume cap for ingestion.                                                                                                                                                       |
