# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpc_lattice_service_network_vpc_association.dataset.md

---
title: VPC Lattice Service Network VPC Association
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > VPC Lattice Service Network VPC
  Association
---

# VPC Lattice Service Network VPC Association

This table represents the VPC Lattice Service Network VPC Association resource from Amazon Web Services.

```
aws.vpc_lattice_service_network_vpc_association
```

## Fields

| Title                | ID   | Type       | Data Type                                                                    | Description |
| -------------------- | ---- | ---------- | ---------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| arn                  | core | string     | The Amazon Resource Name (ARN) of the association.                           |
| created_at           | core | timestamp  | The date and time that the association was created, in ISO-8601 format.      |
| created_by           | core | string     | The account that created the association.                                    |
| id                   | core | string     | The ID of the association.                                                   |
| last_updated_at      | core | timestamp  | The date and time that the association was last updated, in ISO-8601 format. |
| service_network_arn  | core | string     | The Amazon Resource Name (ARN) of the service network.                       |
| service_network_id   | core | string     | The ID of the service network.                                               |
| service_network_name | core | string     | The name of the service network.                                             |
| status               | core | string     | The status.                                                                  |
| tags                 | core | hstore_csv |
| vpc_id               | core | string     | The ID of the VPC.                                                           |
