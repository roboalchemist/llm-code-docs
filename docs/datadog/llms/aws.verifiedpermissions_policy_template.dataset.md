# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.verifiedpermissions_policy_template.dataset.md

---
title: Verified Permissions Policy Template Item
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Verified Permissions Policy Template
  Item
---

# Verified Permissions Policy Template Item

An AWS Verified Permissions Policy Template Item represents a reusable policy definition that defines access control rules for applications. It allows developers to create standardized authorization policies that can be applied across multiple resources or scenarios, ensuring consistent enforcement of permissions.

```
aws.verifiedpermissions_policy_template
```

## Fields

| Title              | ID   | Type       | Data Type                                                             | Description |
| ------------------ | ---- | ---------- | --------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| created_date       | core | timestamp  | The date and time that the policy template was created.               |
| description        | core | string     | The description attached to the policy template.                      |
| last_updated_date  | core | timestamp  | The date and time that the policy template was most recently updated. |
| policy_store_id    | core | string     | The unique identifier of the policy store that contains the template. |
| policy_template_id | core | string     | The unique identifier of the policy template.                         |
| tags               | core | hstore_csv |
