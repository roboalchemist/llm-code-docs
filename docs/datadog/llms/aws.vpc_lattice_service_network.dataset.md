# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpc_lattice_service_network.dataset.md

---
title: VPC Lattice Service Network
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VPC Lattice Service Network
---

# VPC Lattice Service Network

This table represents the VPC Lattice Service Network resource from Amazon Web Services.

```
aws.vpc_lattice_service_network
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                   | Description |
| ----------------------------- | ---- | ---------- | --------------------------------------------------------------------------- | ----------- |
| _key                          | core | string     |
| account_id                    | core | string     |
| arn                           | core | string     | The Amazon Resource Name (ARN) of the service network.                      |
| auth_type                     | core | string     | The type of IAM policy.                                                     |
| created_at                    | core | timestamp  | The date and time that the service network was created, in ISO-8601 format. |
| id                            | core | string     | The ID of the service network.                                              |
| last_updated_at               | core | timestamp  | The date and time of the last update, in ISO-8601 format.                   |
| name                          | core | string     | The name of the service network.                                            |
| number_of_associated_services | core | int64      | The number of services associated with the service network.                 |
| number_of_associated_vpcs     | core | int64      | The number of VPCs associated with the service network.                     |
| sharing_config                | core | json       | Specifies if the service network is enabled for sharing.                    |
| tags                          | core | hstore_csv |
