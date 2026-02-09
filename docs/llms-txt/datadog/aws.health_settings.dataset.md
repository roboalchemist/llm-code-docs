# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.health_settings.dataset.md

---
title: Health Settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Health Settings
---

# Health Settings

This table represents the Health Settings resource from Amazon Web Services.

```
aws.health_settings
```

## Fields

| Title                                         | ID   | Type       | Data Type                                                                                                                                                                      | Description |
| --------------------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                                          | core | string     |
| account_id                                    | core | string     |
| health_service_access_status_for_organization | core | string     | Information about the status of enabling or disabling the Health organizational view feature in your organization. Valid values are <code>ENABLED | DISABLED | PENDING</code>. |
| tags                                          | core | hstore_csv |
