# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.transit_gateway_vpc_attachment.dataset.md

---
title: Transit Gateway VPC Attachment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Transit Gateway VPC Attachment
---

# Transit Gateway VPC Attachment

This table represents the Transit Gateway VPC Attachment resource from Amazon Web Services.

```
aws.transit_gateway_vpc_attachment
```

## Fields

| Title                              | ID   | Type          | Data Type                                                                                         | Description |
| ---------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------- | ----------- |
| _key                               | core | string        |
| account_id                         | core | string        |
| creation_time                      | core | timestamp     | The creation time.                                                                                |
| options                            | core | json          | The VPC attachment options.                                                                       |
| state                              | core | string        | The state of the VPC attachment. Note that the <code>initiating</code> state has been deprecated. |
| subnet_ids                         | core | array<string> | The IDs of the subnets.                                                                           |
| tags                               | core | hstore_csv    |
| transit_gateway_attachment_id      | core | string        | The ID of the attachment.                                                                         |
| transit_gateway_id                 | core | string        | The ID of the transit gateway.                                                                    |
| transit_gateway_vpc_attachment_arn | core | string        |
| vpc_id                             | core | string        | The ID of the VPC.                                                                                |
| vpc_owner_id                       | core | string        | The ID of the Amazon Web Services account that owns the VPC.                                      |
