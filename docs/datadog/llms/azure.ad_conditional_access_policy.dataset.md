# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.ad_conditional_access_policy.dataset.md

---
title: Active Directory Conditional Access Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Active Directory Conditional Access
  Policy
---

# Active Directory Conditional Access Policy

This table represents the Active Directory Conditional Access Policy resource from Microsoft Azure.

```
azure.ad_conditional_access_policy
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                            | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key               | core | string     |
| conditions         | core | json       |
| created_date_time  | core | string     | The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly. |
| description        | core | string     |
| grant_controls     | core | json       | Specifies the grant controls that must be fulfilled to pass the policy.                                                                                                              |
| id                 | core | string     | The unique identifier for an entity. Read-only.                                                                                                                                      |
| location           | core | string     |
| modified_date_time | core | string     | The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly. |
| name               | core | string     |
| resource_group     | core | string     |
| session_controls   | core | json       | Specifies the session controls that are enforced after sign-in.                                                                                                                      |
| state              | core | string     |
| subscription_id    | core | string     |
| subscription_name  | core | string     |
| tags               | core | hstore_csv |
| template_id        | core | string     |
