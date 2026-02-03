# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.log_analytics_storage_insight.dataset.md

---
title: Log Analytics Storage Insight
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Log Analytics Storage Insight
---

# Log Analytics Storage Insight

This table represents the Log Analytics Storage Insight resource from Microsoft Azure.

```
azure.log_analytics_storage_insight
```

## Fields

| Title             | ID   | Type          | Data Type                                                                                                                                                                                 | Description |
| ----------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string        |
| containers        | core | array<string> | The names of the blob containers that the workspace should read                                                                                                                           |
| e_tag             | core | string        | The ETag of the storage insight.                                                                                                                                                          |
| id                | core | string        | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| location          | core | string        |
| name              | core | string        | The name of the resource                                                                                                                                                                  |
| resource_group    | core | string        |
| status            | core | json          | The status of the storage insight                                                                                                                                                         |
| storage_account   | core | json          | The storage account connection details                                                                                                                                                    |
| subscription_id   | core | string        |
| subscription_name | core | string        |
| tables            | core | array<string> | The names of the Azure tables that the workspace should read                                                                                                                              |
| tags              | core | hstore_csv    |
| type              | core | string        | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                 |
