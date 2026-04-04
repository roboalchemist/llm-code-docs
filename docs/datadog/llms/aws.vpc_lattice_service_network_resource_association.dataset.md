# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpc_lattice_service_network_resource_association.dataset.md

---
title: VPC Lattice Service Network Resource Association
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > VPC Lattice Service Network Resource
  Association
---

# VPC Lattice Service Network Resource Association

This table represents the VPC Lattice Service Network Resource Association resource from Amazon Web Services.

```
aws.vpc_lattice_service_network_resource_association
```

## Fields

| Title                       | ID   | Type       | Data Type                                                                                         | Description |
| --------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string     |
| account_id                  | core | string     |
| arn                         | core | string     | The Amazon Resource Name (ARN) of the association.                                                |
| created_at                  | core | timestamp  | The date and time that the association was created, in ISO-8601 format.                           |
| created_by                  | core | string     | The account that created the association.                                                         |
| dns_entry                   | core | json       | The DNS entry for the service.                                                                    |
| failure_code                | core | string     | The failure code.                                                                                 |
| id                          | core | string     | The ID of the association between the service network and resource configuration.                 |
| is_managed_association      | core | bool       | Specifies whether the association is managed by Amazon.                                           |
| private_dns_entry           | core | json       | The private DNS entry for the service.                                                            |
| resource_configuration_arn  | core | string     | The Amazon Resource Name (ARN) of the association.                                                |
| resource_configuration_id   | core | string     | The ID of the resource configuration associated with the service network.                         |
| resource_configuration_name | core | string     | The name of the resource configuration associated with the service network.                       |
| service_network_arn         | core | string     | The Amazon Resource Name (ARN) of the service network associated with the resource configuration. |
| service_network_id          | core | string     | The ID of the service network associated with the resource configuration.                         |
| service_network_name        | core | string     | The name of the service network associated with the resource configuration.                       |
| status                      | core | string     | The status of the service network associated with the resource configuration.                     |
| tags                        | core | hstore_csv |
