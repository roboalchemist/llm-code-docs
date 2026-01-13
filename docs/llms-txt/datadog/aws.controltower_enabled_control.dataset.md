# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.controltower_enabled_control.dataset.md

---
title: Control Tower Enabled Control
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Control Tower Enabled Control
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.controltower_enabled_control.dataset/index.html
---

# Control Tower Enabled Control

An AWS Control Tower Enabled Control represents a governance rule that has been activated within a landing zone. It shows which controls are currently enforced on accounts or organizational units, helping ensure compliance with best practices and organizational policies.

```
aws.controltower_enabled_control
```

## Fields

| Title                | ID   | Type   | Data Type                                                 | Description |
| -------------------- | ---- | ------ | --------------------------------------------------------- | ----------- |
| _key                 | core | string |
| account_id           | core | string |
| arn                  | core | string | The ARN of the enabled control.                           |
| control_identifier   | core | string | The controlIdentifier of the enabled control.             |
| drift_status_summary | core | json   | The drift status of the enabled control.                  |
| status_summary       | core | json   | A short description of the status of the enabled control. |
| tags                 | core | hstore |
| target_identifier    | core | string | The ARN of the organizational unit.                       |
