# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_local_gateway_route_table_vpc_association.dataset.md

---
title: EC2 Local Gateway Route Table VPC Association
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > EC2 Local Gateway Route Table VPC
  Association
---

# EC2 Local Gateway Route Table VPC Association

EC2 Local Gateway Route Table VPC Association is an AWS resource that links a VPC to a local gateway route table. This association enables routing between on-premises networks connected through AWS Outposts and the VPC, ensuring traffic flows correctly between local environments and AWS resources.

```
aws.ec2_local_gateway_route_table_vpc_association
```

## Fields

| Title                                        | ID   | Type       | Data Type                                                                                              | Description |
| -------------------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------ | ----------- |
| _key                                         | core | string     |
| account_id                                   | core | string     |
| local_gateway_id                             | core | string     | The ID of the local gateway.                                                                           |
| local_gateway_route_table_arn                | core | string     | The Amazon Resource Name (ARN) of the local gateway route table for the association.                   |
| local_gateway_route_table_id                 | core | string     | The ID of the local gateway route table.                                                               |
| local_gateway_route_table_vpc_association_id | core | string     | The ID of the association.                                                                             |
| owner_id                                     | core | string     | The ID of the Amazon Web Services account that owns the local gateway route table for the association. |
| state                                        | core | string     | The state of the association.                                                                          |
| tags                                         | core | hstore_csv |
| vpc_id                                       | core | string     | The ID of the VPC.                                                                                     |
