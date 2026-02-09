# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53_recovery_control_assertion_safety_rule.dataset.md

---
title: Route 53 Recovery Control Assertion Safety Rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Route 53 Recovery Control Assertion
  Safety Rule
---

# Route 53 Recovery Control Assertion Safety Rule

This table represents the Route 53 Recovery Control Assertion Safety Rule resource from Amazon Web Services.

```
aws.route53_recovery_control_assertion_safety_rule
```

## Fields

| Title             | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description |
| ----------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string        |
| account_id        | core | string        |
| asserted_controls | core | array<string> | The routing controls that are part of transactions that are evaluated to determine if a request to change a routing control state is allowed. For example, you might include three routing controls, one for each of three Amazon Web Services Regions.                                                                                                                                                                                                     |
| control_panel_arn | core | string        | The Amazon Resource Name (ARN) of the control panel.                                                                                                                                                                                                                                                                                                                                                                                                        |
| name              | core | string        | Name of the assertion rule. You can use any non-white space character in the name.                                                                                                                                                                                                                                                                                                                                                                          |
| owner             | core | string        | The Amazon Web Services account ID of the assertion rule owner.                                                                                                                                                                                                                                                                                                                                                                                             |
| rule_config       | core | json          | The criteria that you set for specific assertion routing controls (AssertedControls) that designate how many routing control states must be ON as the result of a transaction. For example, if you have three assertion routing controls, you might specify ATLEAST 2 for your rule configuration. This means that at least two assertion routing control states must be ON, so that at least two Amazon Web Services Regions have traffic flowing to them. |
| safety_rule_arn   | core | string        | The Amazon Resource Name (ARN) of the assertion rule.                                                                                                                                                                                                                                                                                                                                                                                                       |
| status            | core | string        | The deployment status of an assertion rule. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.                                                                                                                                                                                                                                                                                                                                        |
| tags              | core | hstore_csv    |
| wait_period_ms    | core | int64         | An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value.                                                                                                                                                                                                                       |
