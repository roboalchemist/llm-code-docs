# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53resolver_firewall_config.dataset.md

---
title: "Route\_53 Resolver Firewall Config"
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: "Docs > DDSQL Reference > Data Directory > Route\_53 Resolver Firewall Config"
---

# Route 53 Resolver Firewall Config

Route 53 Resolver Firewall Config is an AWS resource that defines the default behavior of DNS firewall rules for VPCs using Route 53 Resolver. It allows you to specify whether DNS queries that do not match any firewall rule should be allowed or blocked, providing centralized control over DNS traffic security across your environment.

```
aws.route53resolver_firewall_config
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| firewall_fail_open | core | string     | Determines how DNS Firewall operates during failures, for example when all traffic that is sent to DNS Firewall fails to receive a reply. By default, fail open is disabled, which means the failure mode is closed. This approach favors security over availability. DNS Firewall returns a failure error when it is unable to properly evaluate a query. If you enable this option, the failure mode is open. This approach favors availability over security. DNS Firewall allows queries to proceed if it is unable to properly evaluate them. This behavior is only enforced for VPCs that have at least one DNS Firewall rule group association. |
| id                 | core | string     | The ID of the firewall configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| owner_id           | core | string     | The Amazon Web Services account ID of the owner of the VPC that this firewall configuration applies to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| resource_id        | core | string     | The ID of the VPC that this firewall configuration applies to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| tags               | core | hstore_csv |
