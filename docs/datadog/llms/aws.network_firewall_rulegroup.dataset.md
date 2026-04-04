# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.network_firewall_rulegroup.dataset.md

---
title: Network Firewall Rule Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Firewall Rule Group
---

# Network Firewall Rule Group

This table represents the Network Firewall Rule Group resource from Amazon Web Services.

```
aws.network_firewall_rulegroup
```

## Fields

| Title               | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description |
| ------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| rule_group          | core | json       | The object that defines the rules in a rule group. This, along with <a>RuleGroupResponse</a>, define the rule group. You can retrieve all objects for a rule group by calling <a>DescribeRuleGroup</a>. Network Firewall uses a rule group to inspect and control network traffic. You define stateless rule groups to inspect individual packets and you define stateful rule groups to inspect packets in the context of their traffic flow. To use a rule group, you include it by reference in an Network Firewall firewall policy, then you use the policy in a firewall. You can reference a rule group from more than one firewall policy, and you can use a firewall policy in more than one firewall. |
| rule_group_response | core | json       | The high-level properties of a rule group. This, along with the <a>RuleGroup</a>, define the rule group. You can retrieve all objects for a rule group by calling <a>DescribeRuleGroup</a>.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| tags                | core | hstore_csv |
| update_token        | core | string     | A token used for optimistic locking. Network Firewall returns a token to your requests that access the rule group. The token marks the state of the rule group resource at the time of the request. To make changes to the rule group, you provide the token in your request. Network Firewall uses the token to ensure that the rule group hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the rule group again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.                                                  |
