# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/oci/oci.network_security_rule.dataset.md

---
title: Network Security Rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Security Rule
---

# Network Security Rule

This table represents the Network Security Rule resource from Oracle Cloud Infrastructure.

```
oci.network_security_rule
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                  | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key               | core | string     |
| cloud_account_id   | core | string     | The identifier of the related cloud account. The concept of an account might have different names in different cloud providers. AWS is calling it account, GCP calls it project and Azure uses the term subscription.                                                                      |
| cloud_account_name | core | string     | The name of the account this resource belongs to.                                                                                                                                                                                                                                          |
| cloud_provider     | core | string     | The name of the cloud provider.                                                                                                                                                                                                                                                            |
| cloud_tags         | core | hstore     |
| compartment_id     | core | string     | Compartment containing the resource. Used for Access control, logical grouping, and authorization boundaries.                                                                                                                                                                              |
| created_at         | core | timestamp  | Time when the resource has been created.                                                                                                                                                                                                                                                   |
| description        | core | string     | The value to assign to the description property of this SecurityRule.                                                                                                                                                                                                                      |
| destination        | core | string     | The value to assign to the destination property of this SecurityRule.                                                                                                                                                                                                                      |
| destination_type   | core | string     | The value to assign to the destination_type property of this SecurityRule. Allowed values for this property are: "CIDR_BLOCK", "SERVICE_CIDR_BLOCK", "NETWORK_SECURITY_GROUP", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'. |
| direction          | core | string     | The value to assign to the direction property of this SecurityRule. Allowed values for this property are: "EGRESS", "INGRESS", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.                                                 |
| freeform_tags      | core | hstore     | The value to assign to the freeform_tags property of this Instance.                                                                                                                                                                                                                        |
| icmp_options       | core | json       | The value to assign to the icmp_options property of this SecurityRule.                                                                                                                                                                                                                     |
| id                 | core | string     | The value to assign to the id property of this SecurityRule.                                                                                                                                                                                                                               |
| is_stateless       | core | bool       | The value to assign to the is_stateless property of this SecurityRule.                                                                                                                                                                                                                     |
| is_valid           | core | bool       | The value to assign to the is_valid property of this SecurityRule.                                                                                                                                                                                                                         |
| name               | core | string     | The name of this resource.                                                                                                                                                                                                                                                                 |
| protocol           | core | string     | The value to assign to the protocol property of this SecurityRule.                                                                                                                                                                                                                         |
| region_id          | core | string     | The region this resource resides within.                                                                                                                                                                                                                                                   |
| resource_type      | core | string     | The name of the resource type.                                                                                                                                                                                                                                                             |
| source_type        | core | string     | The value to assign to the source_type property of this SecurityRule. Allowed values for this property are: "CIDR_BLOCK", "SERVICE_CIDR_BLOCK", "NETWORK_SECURITY_GROUP", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.      |
| tags               | core | hstore_csv |
| tcp_options        | core | json       | The value to assign to the tcp_options property of this SecurityRule.                                                                                                                                                                                                                      |
| time_created       | core | timestamp  | The value to assign to the time_created property of this SecurityRule.                                                                                                                                                                                                                     |
| udp_options        | core | json       | The value to assign to the udp_options property of this SecurityRule.                                                                                                                                                                                                                      |
| updated_at         | core | timestamp  | Time when the resource has been updated the last time.                                                                                                                                                                                                                                     |
| zone_id            | core | string     | The zone this resource resides within.                                                                                                                                                                                                                                                     |
