# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.elbv2_listener_rule.dataset.md

---
title: ELB V2 Listener Rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > ELB V2 Listener Rule
---

# ELB V2 Listener Rule

This table represents the ELB V2 Listener Rule resource from Amazon Web Services.

```
aws.elbv2_listener_rule
```

## Fields

| Title      | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                               | Description |
| ---------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key       | core | string     |
| account_id | core | string     |
| actions    | core | json       | The actions. Each rule must include exactly one of the following types of actions: <code>forward</code>, <code>redirect</code>, or <code>fixed-response</code>, and it must be the last action to be performed.                                                                                         |
| conditions | core | json       | The conditions. Each rule can include zero or one of the following conditions: <code>http-request-method</code>, <code>host-header</code>, <code>path-pattern</code>, and <code>source-ip</code>, and zero or more of the following conditions: <code>http-header</code> and <code>query-string</code>. |
| is_default | core | bool       | Indicates whether this is the default rule.                                                                                                                                                                                                                                                             |
| priority   | core | string     | The priority.                                                                                                                                                                                                                                                                                           |
| rule_arn   | core | string     |
| tags       | core | hstore_csv |
