# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.transit_gateway.dataset.md

---
title: Transit Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Transit Gateway
---

# Transit Gateway

This table represents the Transit Gateway resource from Amazon Web Services.

```
aws.transit_gateway
```

## Fields

| Title               | ID   | Type       | Data Type                                                                | Description |
| ------------------- | ---- | ---------- | ------------------------------------------------------------------------ | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| creation_time       | core | timestamp  | The creation time.                                                       |
| description         | core | string     | The description of the transit gateway.                                  |
| options             | core | json       | The transit gateway options.                                             |
| owner_id            | core | string     | The ID of the Amazon Web Services account that owns the transit gateway. |
| state               | core | string     | The state of the transit gateway.                                        |
| tags                | core | hstore_csv |
| transit_gateway_arn | core | string     | The Amazon Resource Name (ARN) of the transit gateway.                   |
| transit_gateway_id  | core | string     | The ID of the transit gateway.                                           |
