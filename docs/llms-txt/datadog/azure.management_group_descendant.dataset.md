# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.management_group_descendant.dataset.md

---
title: Management Group Descendant
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Management Group Descendant
---

# Management Group Descendant

This table represents the management_group_descendant resource from Microsoft Azure.

```
azure.management_group_descendant
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                                                          | Description |
| ----------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| id                | core | string     | The fully qualified ID for the descendant. For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000 or /subscriptions/0000000-0000-0000-0000-000000000000 |
| location          | core | string     |
| name              | core | string     | The name of the descendant. For example, 00000000-0000-0000-0000-000000000000                                                                                                                      |
| parent            | core | json       |
| resource_group    | core | string     |
| subscription_id   | core | string     |
| subscription_name | core | string     |
| tags              | core | hstore_csv |
| type              | core | string     | The type of the resource. For example, Microsoft.Management/managementGroups or /subscriptions                                                                                                     |
