# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53resolver_firewall_rule_group_association.dataset.md

---
title: "Route\_53 Resolver DNS Firewall Rule Group Association"
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: "Docs > DDSQL Reference > Data Directory > Route\_53 Resolver DNS Firewall Rule Group Association"
---

# Route 53 Resolver DNS Firewall Rule Group Association

Route 53 Resolver DNS Firewall Rule Group Association is an AWS resource that links a DNS Firewall rule group to a specific VPC. This association ensures that DNS queries from the VPC are inspected and filtered according to the rules defined in the rule group, helping enforce security policies and block unwanted domains.

```
aws.route53resolver_firewall_rule_group_association
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                                           | Description |
| ---------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| arn                    | core | string     | The Amazon Resource Name (ARN) of the firewall rule group association.                                                                                                                                                              |
| creation_time          | core | string     | The date and time that the association was created, in Unix time format and Coordinated Universal Time (UTC).                                                                                                                       |
| creator_request_id     | core | string     | A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp.                          |
| firewall_rule_group_id | core | string     | The unique identifier of the firewall rule group.                                                                                                                                                                                   |
| id                     | core | string     | The identifier for the association.                                                                                                                                                                                                 |
| managed_owner_name     | core | string     | The owner of the association, used only for associations that are not managed by you. If you use Firewall Manager to manage your DNS Firewalls, then this reports Firewall Manager as the managed owner.                            |
| modification_time      | core | string     | The date and time that the association was last modified, in Unix time format and Coordinated Universal Time (UTC).                                                                                                                 |
| mutation_protection    | core | string     | If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections.                                                                              |
| name                   | core | string     | The name of the association.                                                                                                                                                                                                        |
| priority               | core | int64      | The setting that determines the processing order of the rule group among the rule groups that are associated with a single VPC. DNS Firewall filters VPC traffic starting from rule group with the lowest numeric priority setting. |
| status                 | core | string     | The current status of the association.                                                                                                                                                                                              |
| status_message         | core | string     | Additional information about the status of the response, if available.                                                                                                                                                              |
| tags                   | core | hstore_csv |
| vpc_id                 | core | string     | The unique identifier of the VPC that is associated with the rule group.                                                                                                                                                            |
