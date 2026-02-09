# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.transit_gateway_peering_attachment.dataset.md

---
title: Transit Gateway Peering Attachment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Transit Gateway Peering Attachment
---

# Transit Gateway Peering Attachment

This table represents the Transit Gateway Peering Attachment resource from Amazon Web Services.

```
aws.transit_gateway_peering_attachment
```

## Fields

| Title                                  | ID   | Type       | Data Type                                                                                                             | Description |
| -------------------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                   | core | string     |
| accepter_tgw_info                      | core | json       | Information about the accepter transit gateway.                                                                       |
| accepter_transit_gateway_attachment_id | core | string     | The ID of the accepter transit gateway attachment.                                                                    |
| account_id                             | core | string     |
| creation_time                          | core | timestamp  | The time the transit gateway peering attachment was created.                                                          |
| options                                | core | json       | Details about the transit gateway peering attachment.                                                                 |
| requester_tgw_info                     | core | json       | Information about the requester transit gateway.                                                                      |
| state                                  | core | string     | The state of the transit gateway peering attachment. Note that the <code>initiating</code> state has been deprecated. |
| status                                 | core | json       | The status of the transit gateway peering attachment.                                                                 |
| tags                                   | core | hstore_csv |
| transit_gateway_attachment_id          | core | string     | The ID of the transit gateway peering attachment.                                                                     |
| transit_gateway_peering_attachment_arn | core | string     |
