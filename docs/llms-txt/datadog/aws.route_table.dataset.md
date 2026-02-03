# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route_table.dataset.md

---
title: Route Table
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Route Table
---

# Route Table

This table represents the Route Table resource from Amazon Web Services.

```
aws.route_table
```

## Fields

| Title            | ID   | Type       | Data Type                                                              | Description |
| ---------------- | ---- | ---------- | ---------------------------------------------------------------------- | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| associations     | core | json       | The associations between the route table and your subnets or gateways. |
| owner_id         | core | string     | The ID of the Amazon Web Services account that owns the route table.   |
| propagating_vgws | core | json       | Any virtual private gateway (VGW) propagating routes.                  |
| route_table_arn  | core | string     |
| route_table_id   | core | string     | The ID of the route table.                                             |
| routes           | core | json       | The routes in the route table.                                         |
| tags             | core | hstore_csv |
| vpc_id           | core | string     | The ID of the VPC.                                                     |
