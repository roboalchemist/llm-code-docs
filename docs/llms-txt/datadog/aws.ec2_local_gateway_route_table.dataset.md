# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_local_gateway_route_table.dataset.md

---
title: EC2 Local Gateway Route Table
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Local Gateway Route Table
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ec2_local_gateway_route_table.dataset/index.html
---

# EC2 Local Gateway Route Table

An EC2 Local Gateway Route Table in AWS defines how traffic is routed between on-premises networks connected through a local gateway and resources in a VPC. It enables hybrid connectivity by controlling the flow of traffic between your data center and AWS resources, ensuring efficient and secure routing for workloads that span both environments.

```
aws.ec2_local_gateway_route_table
```

## Fields

| Title                         | ID   | Type   | Data Type                                                                          | Description |
| ----------------------------- | ---- | ------ | ---------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string |
| account_id                    | core | string |
| local_gateway_id              | core | string | The ID of the local gateway.                                                       |
| local_gateway_route_table_arn | core | string | The Amazon Resource Name (ARN) of the local gateway route table.                   |
| local_gateway_route_table_id  | core | string | The ID of the local gateway route table.                                           |
| mode                          | core | string | The mode of the local gateway route table.                                         |
| outpost_arn                   | core | string | The Amazon Resource Name (ARN) of the Outpost.                                     |
| owner_id                      | core | string | The ID of the Amazon Web Services account that owns the local gateway route table. |
| state                         | core | string | The state of the local gateway route table.                                        |
| state_reason                  | core | json   | Information about the state change.                                                |
| tags                          | core | hstore |
