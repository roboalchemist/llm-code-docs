# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.management_lock.dataset.md

---
title: Management Lock
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Management Lock
---

# Management Lock

This table represents the management_lock resource from Microsoft Azure.

```
azure.management_lock
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                                                                                                                                           | Description |
| ----------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| id                | core | string     | The resource ID of the lock.                                                                                                                                                                                                                                                        |
| level             | core | string     | The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete means authorized users are able to read and modify the resources, but not delete. ReadOnly means authorized users can only read from a resource, but they can't modify or delete it. |
| location          | core | string     |
| name              | core | string     | The name of the lock.                                                                                                                                                                                                                                                               |
| notes             | core | string     | Notes about the lock. Maximum of 512 characters.                                                                                                                                                                                                                                    |
| owners            | core | json       | The owners of the lock.                                                                                                                                                                                                                                                             |
| resource_group    | core | string     |
| subscription_id   | core | string     |
| subscription_name | core | string     |
| tags              | core | hstore_csv |
| type              | core | string     | The resource type of the lock - Microsoft.Authorization/locks.                                                                                                                                                                                                                      |
