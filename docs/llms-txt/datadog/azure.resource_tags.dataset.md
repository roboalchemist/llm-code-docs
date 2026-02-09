# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.resource_tags.dataset.md

---
title: Resource Tags
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Resource Tags
---

# Resource Tags

This table represents the Resource Tags resource from Microsoft Azure.

```
azure.resource_tags
```

## Fields

| Title             | ID   | Type       | Data Type                 | Description |
| ----------------- | ---- | ---------- | ------------------------- | ----------- |
| _key              | core | string     |
| id                | core | string     | Resource ID               |
| kind              | core | string     | The kind of the resource. |
| location          | core | string     | Resource location         |
| name              | core | string     | Resource name             |
| resource_group    | core | string     |
| subscription_id   | core | string     |
| subscription_name | core | string     |
| tags              | core | hstore_csv |
| type              | core | string     | Resource type             |
