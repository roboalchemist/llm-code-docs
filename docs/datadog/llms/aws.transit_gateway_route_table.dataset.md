# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.transit_gateway_route_table.dataset.md

---
title: Transit Gateway Route Table
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Transit Gateway Route Table
---

# Transit Gateway Route Table

This table represents the Transit Gateway Route Table resource from Amazon Web Services.

```
aws.transit_gateway_route_table
```

## Fields

| Title                                  | ID   | Type       | Data Type                                                                              | Description |
| -------------------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------- | ----------- |
| _key                                   | core | string     |
| account_id                             | core | string     |
| additional_routes_available            | core | bool       | Indicates whether there are additional routes available.                               |
| creation_time                          | core | timestamp  | The creation time.                                                                     |
| default_association_route_table        | core | bool       | Indicates whether this is the default association route table for the transit gateway. |
| default_propagation_route_table        | core | bool       | Indicates whether this is the default propagation route table for the transit gateway. |
| routes                                 | core | json       | Information about the routes.                                                          |
| state                                  | core | string     | The state of the transit gateway route table.                                          |
| tags                                   | core | hstore_csv |
| transit_gateway_id                     | core | string     | The ID of the transit gateway.                                                         |
| transit_gateway_prefix_list_references | core | json       | Information about the prefix list references.                                          |
| transit_gateway_route_table_arn        | core | string     |
| transit_gateway_route_table_id         | core | string     | The ID of the transit gateway route table.                                             |
