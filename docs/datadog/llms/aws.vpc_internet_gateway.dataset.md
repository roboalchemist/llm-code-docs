# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpc_internet_gateway.dataset.md

---
title: VPC Internet Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VPC Internet Gateway
---

# VPC Internet Gateway

This table represents the VPC Internet Gateway resource from Amazon Web Services.

```
aws.vpc_internet_gateway
```

## Fields

| Title                | ID   | Type       | Data Type                                                                 | Description |
| -------------------- | ---- | ---------- | ------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| attachments          | core | json       | Any VPCs attached to the internet gateway.                                |
| internet_gateway_arn | core | string     |
| internet_gateway_id  | core | string     | The ID of the internet gateway.                                           |
| owner_id             | core | string     | The ID of the Amazon Web Services account that owns the internet gateway. |
| tags                 | core | hstore_csv |
