# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53_recovery_control_control_panel.dataset.md

---
title: Route 53 Recovery Control Control Panel
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Route 53 Recovery Control Control
  Panel
---

# Route 53 Recovery Control Control Panel

This table represents the Route 53 Recovery Control Control Panel resource from Amazon Web Services.

```
aws.route53_recovery_control_control_panel
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                        | Description |
| --------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| cluster_arn           | core | string     | The Amazon Resource Name (ARN) of the cluster that includes the control panel.                                                                                                                                                                                                                                                                   |
| control_panel_arn     | core | string     | The Amazon Resource Name (ARN) of the control panel.                                                                                                                                                                                                                                                                                             |
| default_control_panel | core | bool       | A flag that Amazon Route 53 Application Recovery Controller sets to true to designate the default control panel for a cluster. When you create a cluster, Amazon Route 53 Application Recovery Controller creates a control panel, and sets this flag for that control panel. If you create a control panel yourself, this flag is set to false. |
| name                  | core | string     | The name of the control panel. You can use any non-white space character in the name.                                                                                                                                                                                                                                                            |
| owner                 | core | string     | The Amazon Web Services account ID of the control panel owner.                                                                                                                                                                                                                                                                                   |
| routing_control_count | core | int64      | The number of routing controls in the control panel.                                                                                                                                                                                                                                                                                             |
| status                | core | string     | The deployment status of control panel. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.                                                                                                                                                                                                                                 |
| tags                  | core | hstore_csv |
