# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.waf_rule.dataset.md

---
title: WAF Rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > WAF Rule
---

# WAF Rule

An AWS WAF Rule defines a set of conditions used to inspect and control web requests based on criteria such as IP addresses, HTTP headers, or query strings. Rules are building blocks that can be combined into WebACLs to allow, block, or count requests. They help protect applications from common web exploits and unwanted traffic.

```
aws.waf_rule
```

## Fields

| Title       | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                       | Description |
| ----------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key        | core | string     |
| account_id  | core | string     |
| metric_name | core | string     | A friendly name or description for the metrics for this Rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can't change MetricName after you create the Rule. |
| name        | core | string     | The friendly name or description for the Rule. You can't change the name of a Rule after you create it.                                                                                                                                                                                                                                         |
| predicates  | core | json       | The Predicates object contains one Predicate element for each ByteMatchSet, IPSet, or SqlInjectionMatchSet object that you want to include in a Rule.                                                                                                                                                                                           |
| rule_arn    | core | string     |
| rule_id     | core | string     | A unique identifier for a Rule. You use RuleId to get more information about a Rule (see GetRule), update a Rule (see UpdateRule), insert a Rule into a WebACL or delete a one from a WebACL (see UpdateWebACL), or delete a Rule from AWS WAF (see DeleteRule). RuleId is returned by CreateRule and by ListRules.                             |
| tags        | core | hstore_csv |
