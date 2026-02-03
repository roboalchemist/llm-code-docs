# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.waf_rule_group.dataset.md

---
title: WAF Rule Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > WAF Rule Group
---

# WAF Rule Group

An AWS WAF Rule Group is a reusable collection of predefined rules that help control and filter web requests based on conditions such as IP addresses, HTTP headers, or query strings. It allows you to group multiple rules together and apply them consistently across different web applications or resources. Rule groups simplify management by enabling centralized updates and can be shared across accounts through AWS Firewall Manager.

```
aws.waf_rule_group
```

## Fields

| Title          | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                       | Description |
| -------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key           | core | string     |
| account_id     | core | string     |
| metric_name    | core | string     | A friendly name or description for the metrics for this RuleGroup. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can't change the name of the metric after you create the RuleGroup.           |
| name           | core | string     | The friendly name or description for the RuleGroup. You can't change the name of a RuleGroup after you create it.                                                                                                                                                                                                                                                               |
| rule_group_arn | core | string     |
| rule_group_id  | core | string     | A unique identifier for a RuleGroup. You use RuleGroupId to get more information about a RuleGroup (see GetRuleGroup), update a RuleGroup (see UpdateRuleGroup), insert a RuleGroup into a WebACL or delete a one from a WebACL (see UpdateWebACL), or delete a RuleGroup from AWS WAF (see DeleteRuleGroup). RuleGroupId is returned by CreateRuleGroup and by ListRuleGroups. |
| tags           | core | hstore_csv |
