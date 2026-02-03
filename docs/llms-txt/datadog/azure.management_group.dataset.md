# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.management_group.dataset.md

---
title: Management Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Management Group
---

# Management Group

This table represents the management_group resource from Microsoft Azure.

```
azure.management_group
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                          | Description |
| ----------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| id                | core | string     | The fully qualified ID for the management group. For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000 |
| location          | core | string     |
| name              | core | string     | The name of the management group. For example, 00000000-0000-0000-0000-000000000000                                                                |
| resource_group    | core | string     |
| subscription_id   | core | string     |
| subscription_name | core | string     |
| tags              | core | hstore_csv |
| tenant_id         | core | string     | The AAD Tenant ID associated with the management group. For example, 00000000-0000-0000-0000-000000000000                                          |
| type              | core | string     | The type of the resource. For example, Microsoft.Management/managementGroups                                                                       |
