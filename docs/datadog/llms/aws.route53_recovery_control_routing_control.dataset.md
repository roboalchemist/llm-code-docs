# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53_recovery_control_routing_control.dataset.md

---
title: Route 53 Recovery Control Routing Control
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Route 53 Recovery Control Routing
  Control
---

# Route 53 Recovery Control Routing Control

This table represents the Route 53 Recovery Control Routing Control resource from Amazon Web Services.

```
aws.route53_recovery_control_routing_control
```

## Fields

| Title               | ID   | Type       | Data Type                                                                                                            | Description |
| ------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| control_panel_arn   | core | string     | The Amazon Resource Name (ARN) of the control panel that includes the routing control.                               |
| name                | core | string     | The name of the routing control.                                                                                     |
| owner               | core | string     | The Amazon Web Services account ID of the routing control owner.                                                     |
| routing_control_arn | core | string     | The Amazon Resource Name (ARN) of the routing control.                                                               |
| status              | core | string     | The deployment status of a routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION. |
| tags                | core | hstore_csv |
