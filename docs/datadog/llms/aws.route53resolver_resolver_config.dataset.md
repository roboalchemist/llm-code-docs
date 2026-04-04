# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53resolver_resolver_config.dataset.md

---
title: "Route\_53 Resolver Config"
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: "Docs > DDSQL Reference > Data Directory > Route\_53 Resolver Config"
---

# Route 53 Resolver Config

Route 53 Resolver Config is an AWS resource that lets you manage how DNS queries are handled within your VPCs. It allows you to specify whether DNS queries from your VPCs are sent to the Route 53 Resolver for resolution, enabling centralized DNS management and control. This helps ensure consistent DNS behavior across multiple VPCs and accounts.

```
aws.route53resolver_resolver_config
```

## Fields

| Title               | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description |
| ------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| autodefined_reverse | core | string     | The status of whether or not the Resolver will create autodefined rules for reverse DNS lookups. This is enabled by default. The status can be one of following: ENABLING: Autodefined rules for reverse DNS lookups are being enabled but are not complete. ENABLED: Autodefined rules for reverse DNS lookups are enabled. DISABLING: Autodefined rules for reverse DNS lookups are being disabled but are not complete. DISABLED: Autodefined rules for reverse DNS lookups are disabled. |
| id                  | core | string     | ID for the Resolver configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| owner_id            | core | string     | The owner account ID of the Amazon Virtual Private Cloud VPC.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| resource_id         | core | string     | The ID of the Amazon Virtual Private Cloud VPC or a Route 53 Profile that you're configuring Resolver for.                                                                                                                                                                                                                                                                                                                                                                                   |
| tags                | core | hstore_csv |
