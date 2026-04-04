# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53resolver_resolver_dnssec_config.dataset.md

---
title: "Route\_53 Resolver DNSSEC Configuration"
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: "Docs > DDSQL Reference > Data Directory > Route\_53 Resolver DNSSEC Configuration"
---

# Route 53 Resolver DNSSEC Configuration

Route 53 Resolver DNSSEC Configuration is an AWS resource that lets you manage DNSSEC validation settings for your VPCs. It enables or disables DNSSEC validation on DNS queries handled by Route 53 Resolver, helping ensure the authenticity and integrity of DNS responses.

```
aws.route53resolver_resolver_dnssec_config
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                      | Description |
| ----------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| id                | core | string     | The ID for a configuration for DNSSEC validation.                                                                                                                                                                                                                                                              |
| owner_id          | core | string     | The owner account ID of the virtual private cloud (VPC) for a configuration for DNSSEC validation.                                                                                                                                                                                                             |
| resource_id       | core | string     | The ID of the virtual private cloud (VPC) that you're configuring the DNSSEC validation status for.                                                                                                                                                                                                            |
| tags              | core | hstore_csv |
| validation_status | core | string     | The validation status for a DNSSEC configuration. The status can be one of the following: ENABLING: DNSSEC validation is being enabled but is not complete. ENABLED: DNSSEC validation is enabled. DISABLING: DNSSEC validation is being disabled but is not complete. DISABLED DNSSEC validation is disabled. |
