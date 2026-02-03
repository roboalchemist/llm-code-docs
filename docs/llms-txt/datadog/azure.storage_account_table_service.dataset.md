# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.storage_account_table_service.dataset.md

---
title: Storage Account Table Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Storage Account Table Service
---

# Storage Account Table Service

This table represents the Storage Account Table Service resource from Microsoft Azure.

```
azure.storage_account_table_service
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                                                                                                           | Description |
| ----------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| cors              | core | json       | Specifies CORS rules for the Table service. You can include up to five CorsRule elements in the request. If no CorsRule elements are included in the request body, all CORS rules will be deleted, and CORS will be disabled for the Table service. |
| id                | core | string     | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}                                                           |
| location          | core | string     |
| name              | core | string     | The name of the resource                                                                                                                                                                                                                            |
| resource_group    | core | string     |
| subscription_id   | core | string     |
| subscription_name | core | string     |
| tags              | core | hstore_csv |
| type              | core | string     | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                                                                           |
