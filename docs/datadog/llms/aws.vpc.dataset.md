# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpc.dataset.md

---
title: Virtual Private Cloud
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Virtual Private Cloud
---

# Virtual Private Cloud

This table represents the Virtual Private Cloud resource from Amazon Web Services.

```
aws.vpc
```

## Fields

| Title                           | ID   | Type       | Data Type                                                         | Description |
| ------------------------------- | ---- | ---------- | ----------------------------------------------------------------- | ----------- |
| _key                            | core | string     |
| account_id                      | core | string     |
| arn                             | core | string     |
| block_public_access_states      | core | json       | The state of VPC Block Public Access (BPA).                       |
| cidr_block                      | core | string     | The primary IPv4 CIDR block for the VPC.                          |
| cidr_block_association_set      | core | json       | Information about the IPv4 CIDR blocks associated with the VPC.   |
| dhcp_options_id                 | core | string     | The ID of the set of DHCP options you've associated with the VPC. |
| instance_tenancy                | core | string     | The allowed tenancy of instances launched into the VPC.           |
| ipv6_cidr_block_association_set | core | json       | Information about the IPv6 CIDR blocks associated with the VPC.   |
| is_default                      | core | bool       | Indicates whether the VPC is the default VPC.                     |
| owner_id                        | core | string     | The ID of the Amazon Web Services account that owns the VPC.      |
| state                           | core | string     | The current state of the VPC.                                     |
| tags                            | core | hstore_csv |
| vpc_id                          | core | string     | The ID of the VPC.                                                |
