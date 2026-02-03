# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_co_ip_pool.dataset.md

---
title: Ec2 Co Ip Pool
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Ec2 Co Ip Pool
---

# Ec2 Co Ip Pool

This table represents the ec2_co_ip_pool resource from Amazon Web Services.

```
aws.ec2_co_ip_pool
```

## Fields

| Title                        | ID   | Type          | Data Type                                | Description |
| ---------------------------- | ---- | ------------- | ---------------------------------------- | ----------- |
| _key                         | core | string        |
| account_id                   | core | string        |
| local_gateway_route_table_id | core | string        | The ID of the local gateway route table. |
| pool_arn                     | core | string        | The ARN of the address pool.             |
| pool_cidrs                   | core | array<string> | The address ranges of the address pool.  |
| pool_id                      | core | string        | The ID of the address pool.              |
| tags                         | core | hstore_csv    |
