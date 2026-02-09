# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.ad_security_defaults_policy.dataset.md

---
title: Active Directory Security Defaults Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Active Directory Security Defaults
  Policy
---

# Active Directory Security Defaults Policy

This table represents the Active Directory Security Defaults Policy resource from Microsoft Azure.

```
azure.ad_security_defaults_policy
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                    | Description |
| ----------------- | ---- | ---------- | -------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| deleted_date_time | core | string     | Date and time when this object was deleted. Always null when the object hasn't been deleted. |
| description       | core | string     | Description for this policy. Required.                                                       |
| id                | core | string     | The unique identifier for an entity. Read-only.                                              |
| is_enabled        | core | bool       | If set to true, Microsoft Entra security defaults are enabled for the tenant.                |
| location          | core | string     |
| name              | core | string     |
| resource_group    | core | string     |
| subscription_id   | core | string     |
| subscription_name | core | string     |
| tags              | core | hstore_csv |
