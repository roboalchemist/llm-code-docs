# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpc_lattice_resource_endpoint_association.dataset.md

---
title: VPC Lattice Resource Endpoint Association
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > VPC Lattice Resource Endpoint
  Association
---

# VPC Lattice Resource Endpoint Association

This table represents the VPC Lattice Resource Endpoint Association resource from Amazon Web Services.

```
aws.vpc_lattice_resource_endpoint_association
```

## Fields

| Title                       | ID   | Type       | Data Type                                                                            | Description |
| --------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------ | ----------- |
| _key                        | core | string     |
| account_id                  | core | string     |
| arn                         | core | string     | The Amazon Resource Name (ARN) of the VPC endpoint association.                      |
| created_at                  | core | timestamp  | The date and time that the VPC endpoint association was created, in ISO-8601 format. |
| created_by                  | core | string     | The account that created the association.                                            |
| id                          | core | string     | The ID of the VPC endpoint association.                                              |
| resource_configuration_arn  | core | string     | The Amazon Resource Name (ARN) of the resource configuration.                        |
| resource_configuration_id   | core | string     | The ID of the resource configuration.                                                |
| resource_configuration_name | core | string     | The name of the resource configuration.                                              |
| tags                        | core | hstore_csv |
| vpc_endpoint_id             | core | string     | The ID of the VPC endpoint.                                                          |
| vpc_endpoint_owner          | core | string     | The owner of the VPC endpoint.                                                       |
