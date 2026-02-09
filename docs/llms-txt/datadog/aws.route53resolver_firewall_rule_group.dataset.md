# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53resolver_firewall_rule_group.dataset.md

---
title: Route 53 Resolver DNS Firewall Rule Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Route 53 Resolver DNS Firewall Rule
  Group
---

# Route 53 Resolver DNS Firewall Rule Group

Route 53 Resolver DNS Firewall Rule Group is an AWS resource that lets you organize and manage collections of DNS firewall rules. These rule groups define how DNS queries are inspected and controlled, allowing you to block, allow, or monitor specific domain names. You can associate rule groups with VPCs to enforce consistent DNS filtering policies across your environment.

```
aws.route53resolver_firewall_rule_group
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                             | Description |
| ------------------ | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The ARN (Amazon Resource Name) of the rule group.                                                                                                                                                                     |
| creator_request_id | core | string     | A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp.            |
| firewall_rules     | core | json       | A list of the rules that you have defined. This might be a partial list of the firewall rules that you've defined. For information, see MaxResults.                                                                   |
| id                 | core | string     | The ID of the rule group.                                                                                                                                                                                             |
| name               | core | string     | The name of the rule group.                                                                                                                                                                                           |
| owner_id           | core | string     | The Amazon Web Services account ID for the account that created the rule group. When a rule group is shared with your account, this is the account that has shared the rule group with you.                           |
| share_status       | core | string     | Whether the rule group is shared with other Amazon Web Services accounts, or was shared with the current account by another Amazon Web Services account. Sharing is configured through Resource Access Manager (RAM). |
| tags               | core | hstore_csv |
