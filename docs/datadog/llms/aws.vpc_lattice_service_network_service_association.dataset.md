# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpc_lattice_service_network_service_association.dataset.md

---
title: VPC Lattice Service Network Service Association
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > VPC Lattice Service Network Service
  Association
---

# VPC Lattice Service Network Service Association

This table represents the VPC Lattice Service Network Service Association resource from Amazon Web Services.

```
aws.vpc_lattice_service_network_service_association
```

## Fields

| Title                | ID   | Type       | Data Type                                                               | Description |
| -------------------- | ---- | ---------- | ----------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| arn                  | core | string     | The Amazon Resource Name (ARN) of the association.                      |
| created_at           | core | timestamp  | The date and time that the association was created, in ISO-8601 format. |
| created_by           | core | string     | The account that created the association.                               |
| custom_domain_name   | core | string     | The custom domain name of the service.                                  |
| dns_entry            | core | json       | The DNS information.                                                    |
| id                   | core | string     | The ID of the association.                                              |
| service_arn          | core | string     | The Amazon Resource Name (ARN) of the service.                          |
| service_id           | core | string     | The ID of the service.                                                  |
| service_name         | core | string     | The name of the service.                                                |
| service_network_arn  | core | string     | The Amazon Resource Name (ARN) of the service network.                  |
| service_network_id   | core | string     | The ID of the service network.                                          |
| service_network_name | core | string     | The name of the service network.                                        |
| status               | core | string     | The status. If the deletion fails, try to delete again.                 |
| tags                 | core | hstore_csv |
