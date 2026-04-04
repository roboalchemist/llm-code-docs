# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.securityhub_automation_rule.dataset.md

---
title: Security Hub Automation Rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Security Hub Automation Rule
---

# Security Hub Automation Rule

This table represents the Security Hub Automation Rule resource from Amazon Web Services.

```
aws.securityhub_automation_rule
```

## Fields

| Title       | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                             | Description |
| ----------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key        | core | string     |
| account_id  | core | string     |
| actions     | core | json       | One or more actions to update finding fields if a finding matches the defined criteria of the rule.                                                                                                                                                                                                                                                                                                                   |
| created_at  | core | timestamp  | A timestamp that indicates when the rule was created. For more information about the validation and formatting of timestamp fields in Security Hub, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.                                                                                                                                                    |
| created_by  | core | string     | The principal that created a rule.                                                                                                                                                                                                                                                                                                                                                                                    |
| criteria    | core | json       | A set of <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html">Amazon Web Services Security Finding Format</a> finding field attributes and corresponding expected values that Security Hub uses to filter findings. If a rule is enabled and a finding matches the conditions specified in this parameter, Security Hub applies the rule action to the finding.        |
| description | core | string     | A description of the rule.                                                                                                                                                                                                                                                                                                                                                                                            |
| is_terminal | core | bool       | Specifies whether a rule is the last to be applied with respect to a finding that matches the rule criteria. This is useful when a finding matches the criteria for multiple rules, and each rule has different actions. If a rule is terminal, Security Hub applies the rule action to a finding that matches the rule criteria and doesn't evaluate other rules for the finding. By default, a rule isn't terminal. |
| rule_arn    | core | string     | The Amazon Resource Name (ARN) of a rule.                                                                                                                                                                                                                                                                                                                                                                             |
| rule_name   | core | string     | The name of the rule.                                                                                                                                                                                                                                                                                                                                                                                                 |
| rule_order  | core | int64      | An integer ranging from 1 to 1000 that represents the order in which the rule action is applied to findings. Security Hub applies rules with lower values for this parameter first.                                                                                                                                                                                                                                   |
| rule_status | core | string     | Whether the rule is active after it is created. If this parameter is equal to <code>ENABLED</code>, Security Hub starts applying the rule to findings and finding updates after the rule is created.                                                                                                                                                                                                                  |
| tags        | core | hstore_csv |
| updated_at  | core | timestamp  | A timestamp that indicates when the rule was most recently updated. For more information about the validation and formatting of timestamp fields in Security Hub, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.                                                                                                                                      |
