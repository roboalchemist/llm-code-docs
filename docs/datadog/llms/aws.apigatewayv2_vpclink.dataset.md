# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigatewayv2_vpclink.dataset.md

---
title: API Gateway V2 VPC Link
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway V2 VPC Link
---

# API Gateway V2 VPC Link

This table represents the API Gateway V2 VPC Link resource from Amazon Web Services.

```
aws.apigatewayv2_vpclink
```

## Fields

| Title                   | ID   | Type          | Data Type                                                      | Description |
| ----------------------- | ---- | ------------- | -------------------------------------------------------------- | ----------- |
| _key                    | core | string        |
| account_id              | core | string        |
| created_date            | core | timestamp     | The timestamp when the VPC link was created.                   |
| name                    | core | string        | The name of the VPC link.                                      |
| security_group_ids      | core | array<string> | A list of security group IDs for the VPC link.                 |
| subnet_ids              | core | array<string> | A list of subnet IDs to include in the VPC link.               |
| tags                    | core | hstore_csv    |
| vpc_link_id             | core | string        | The ID of the VPC link.                                        |
| vpc_link_status         | core | string        | The status of the VPC link.                                    |
| vpc_link_status_message | core | string        | A message summarizing the cause of the status of the VPC link. |
| vpc_link_version        | core | string        | The version of the VPC link.                                   |
