# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.ad_named_location.dataset.md

---
title: Active Directory Named Location
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Active Directory Named Location
---

# Active Directory Named Location

This table represents the Active Directory Named Location resource from Microsoft Azure.

```
azure.ad_named_location
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                               | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| created_date_time  | core | string     | The Timestamp type represents creation date and time of the location using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.      |
| id                 | core | string     | The unique identifier for an entity. Read-only.                                                                                                                                                         |
| location           | core | string     |
| modified_date_time | core | string     | The Timestamp type represents last modified date and time of the location using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. |
| name               | core | string     |
| resource_group     | core | string     |
| subscription_id    | core | string     |
| subscription_name  | core | string     |
| tags               | core | hstore_csv |
