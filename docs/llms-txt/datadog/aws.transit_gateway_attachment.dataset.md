# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.transit_gateway_attachment.dataset.md

---
title: Transit Gateway Attachment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Transit Gateway Attachment
---

# Transit Gateway Attachment

This table represents the Transit Gateway Attachment resource from Amazon Web Services.

```
aws.transit_gateway_attachment
```

## Fields

| Title                          | ID   | Type       | Data Type                                                                                    | Description |
| ------------------------------ | ---- | ---------- | -------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string     |
| account_id                     | core | string     |
| association                    | core | json       | The association.                                                                             |
| creation_time                  | core | timestamp  | The creation time.                                                                           |
| resource_id                    | core | string     | The ID of the resource.                                                                      |
| resource_owner_id              | core | string     | The ID of the Amazon Web Services account that owns the resource.                            |
| resource_type                  | core | string     | The resource type. Note that the <code>tgw-peering</code> resource type has been deprecated. |
| state                          | core | string     | The attachment state. Note that the <code>initiating</code> state has been deprecated.       |
| tags                           | core | hstore_csv |
| transit_gateway_attachment_arn | core | string     |
| transit_gateway_attachment_id  | core | string     | The ID of the attachment.                                                                    |
| transit_gateway_id             | core | string     | The ID of the transit gateway.                                                               |
| transit_gateway_owner_id       | core | string     | The ID of the Amazon Web Services account that owns the transit gateway.                     |
