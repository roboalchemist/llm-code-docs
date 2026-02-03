# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53resolver_firewall_domain_list.dataset.md

---
title: "Route\_53 Resolver DNS Firewall Domain List"
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: "Docs > DDSQL Reference > Data Directory > Route\_53 Resolver DNS Firewall Domain List"
---

# Route 53 Resolver DNS Firewall Domain List

A Route 53 Resolver DNS Firewall Domain List is a managed collection of domain names that you define to allow or block DNS queries in your VPC. It is used with DNS Firewall rule groups to control access to specific domains, helping protect your network from malicious or unwanted traffic.

```
aws.route53resolver_firewall_domain_list
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                  | Description |
| ------------------ | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The Amazon Resource Name (ARN) of the firewall domain list metadata.                                                                                                                                       |
| creator_request_id | core | string     | A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp. |
| id                 | core | string     | The ID of the domain list.                                                                                                                                                                                 |
| managed_owner_name | core | string     | The owner of the list, used only for lists that are not managed by you. For example, the managed domain list AWSManagedDomainsMalwareDomainList has the managed owner name Route 53 Resolver DNS Firewall. |
| name               | core | string     | The name of the domain list.                                                                                                                                                                               |
| tags               | core | hstore_csv |
