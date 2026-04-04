# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.api_management_workspace.dataset.md

---
title: Api Management Workspace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Api Management Workspace
---

# Api Management Workspace

This table represents the api_management_workspace resource from Microsoft Azure.

```
azure.api_management_workspace
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                                                 | Description |
| ----------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| description       | core | string     | Description of the workspace.                                                                                                                                                             |
| id                | core | string     | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| location          | core | string     |
| name              | core | string     | The name of the resource                                                                                                                                                                  |
| resource_group    | core | string     |
| subscription_id   | core | string     |
| subscription_name | core | string     |
| tags              | core | hstore_csv |
| type              | core | string     | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                 |
