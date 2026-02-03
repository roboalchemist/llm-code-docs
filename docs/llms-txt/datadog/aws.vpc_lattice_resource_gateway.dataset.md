# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpc_lattice_resource_gateway.dataset.md

---
title: VPC Lattice Resource Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VPC Lattice Resource Gateway
---

# VPC Lattice Resource Gateway

This table represents the VPC Lattice Resource Gateway resource from Amazon Web Services.

```
aws.vpc_lattice_resource_gateway
```

## Fields

| Title              | ID   | Type          | Data Type                                                                         | Description |
| ------------------ | ---- | ------------- | --------------------------------------------------------------------------------- | ----------- |
| _key               | core | string        |
| account_id         | core | string        |
| arn                | core | string        | The Amazon Resource Name (ARN) of the resource gateway.                           |
| created_at         | core | timestamp     | The date and time that the resource gateway was created, in ISO-8601 format.      |
| id                 | core | string        | The ID of the resource gateway.                                                   |
| ip_address_type    | core | string        | The type of IP address for the resource gateway.                                  |
| last_updated_at    | core | timestamp     | The date and time that the resource gateway was last updated, in ISO-8601 format. |
| name               | core | string        | The name of the resource gateway.                                                 |
| security_group_ids | core | array<string> | The security group IDs associated with the resource gateway.                      |
| status             | core | string        | The status for the resource gateway.                                              |
| subnet_ids         | core | array<string> | The IDs of the VPC subnets for resource gateway.                                  |
| tags               | core | hstore_csv    |
| vpc_id             | core | string        | The ID of the VPC for the resource gateway.                                       |
