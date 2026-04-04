# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpn_gateway.dataset.md

---
title: VPN Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VPN Gateway
---

# VPN Gateway

This table represents the VPN Gateway resource from Amazon Web Services.

```
aws.vpn_gateway
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                    | Description |
| ----------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| amazon_side_asn   | core | int64      | The private Autonomous System Number (ASN) for the Amazon side of a BGP session.                                             |
| availability_zone | core | string     | The Availability Zone where the virtual private gateway was created, if applicable. This field may be empty or not returned. |
| state             | core | string     | The current state of the virtual private gateway.                                                                            |
| tags              | core | hstore_csv |
| type              | core | string     | The type of VPN connection the virtual private gateway supports.                                                             |
| vpc_attachments   | core | json       | Any VPCs attached to the virtual private gateway.                                                                            |
| vpn_gateway_arn   | core | string     |
| vpn_gateway_id    | core | string     | The ID of the virtual private gateway.                                                                                       |
