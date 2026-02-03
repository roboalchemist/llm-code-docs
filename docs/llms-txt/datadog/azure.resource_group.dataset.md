# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.resource_group.dataset.md

---
title: Resource Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Resource Group
---

# Resource Group

This table represents the Resource Group resource from Microsoft Azure.

```
azure.resource_group
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                            | Description |
| ------------------ | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| id                 | core | string     | The ID of the resource group.                                                                                                                        |
| location           | core | string     | The location of the resource group. It cannot be changed after the resource group has been created. It must be one of the supported Azure locations. |
| managed_by         | core | string     | The ID of the resource that manages this resource group.                                                                                             |
| name               | core | string     | The name of the resource group.                                                                                                                      |
| provisioning_state | core | string     | The provisioning state.                                                                                                                              |
| resource_group     | core | string     |
| subscription_id    | core | string     |
| subscription_name  | core | string     |
| tags               | core | hstore_csv |
| type               | core | string     | The type of the resource group.                                                                                                                      |
