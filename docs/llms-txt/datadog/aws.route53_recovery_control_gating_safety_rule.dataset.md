# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53_recovery_control_gating_safety_rule.dataset.md

---
title: Route 53 Recovery Control Gating Safety Rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Route 53 Recovery Control Gating
  Safety Rule
---

# Route 53 Recovery Control Gating Safety Rule

This table represents the Route 53 Recovery Control Gating Safety Rule resource from Amazon Web Services.

```
aws.route53_recovery_control_gating_safety_rule
```

## Fields

| Title             | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                          | Description |
| ----------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key              | core | string        |
| account_id        | core | string        |
| control_panel_arn | core | string        | The Amazon Resource Name (ARN) of the control panel.                                                                                                                                                                                                                                                                                                                                                               |
| gating_controls   | core | array<string> | An array of gating routing control Amazon Resource Names (ARNs). For a simple "on/off" switch, specify the ARN for one routing control. The gating routing controls are evaluated by the rule configuration that you specify to determine if the target routing control states can be changed.                                                                                                                     |
| name              | core | string        | The name for the gating rule. You can use any non-white space character in the name.                                                                                                                                                                                                                                                                                                                               |
| owner             | core | string        | The Amazon Web Services account ID of the gating rule owner.                                                                                                                                                                                                                                                                                                                                                       |
| rule_config       | core | json          | The criteria that you set for gating routing controls that designate how many of the routing control states must be ON to allow you to update target routing control states.                                                                                                                                                                                                                                       |
| safety_rule_arn   | core | string        | The Amazon Resource Name (ARN) of the gating rule.                                                                                                                                                                                                                                                                                                                                                                 |
| status            | core | string        | The deployment status of a gating rule. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.                                                                                                                                                                                                                                                                                                   |
| tags              | core | hstore_csv    |
| target_controls   | core | array<string> | An array of target routing control Amazon Resource Names (ARNs) for which the states can only be updated if the rule configuration that you specify evaluates to true for the gating routing control. As a simple example, if you have a single gating control, it acts as an overall "on/off" switch for a set of target routing controls. You can use this to manually override automated failover, for example. |
| wait_period_ms    | core | int64         | An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value.                                                                                                                                                                              |
