# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.ad_device_registered_owner.dataset.md

---
title: Active Directory Device Registered Owner
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Active Directory Device Registered
  Owner
---

# Active Directory Device Registered Owner

This table represents the Active Directory Device Registered Owner resource from Microsoft Azure.

```
azure.ad_device_registered_owner
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                    | Description |
| ----------------- | ---- | ---------- | -------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| deleted_date_time | core | string     | Date and time when this object was deleted. Always null when the object hasn't been deleted. |
| id                | core | string     | The unique identifier for an entity. Read-only.                                              |
| location          | core | string     |
| name              | core | string     |
| resource_group    | core | string     |
| subscription_id   | core | string     |
| subscription_name | core | string     |
| tags              | core | hstore_csv |
