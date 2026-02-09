# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpc_peering_connection.dataset.md

---
title: VPC Peering Connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VPC Peering Connection
---

# VPC Peering Connection

This table represents the VPC Peering Connection resource from Amazon Web Services.

```
aws.vpc_peering_connection
```

## Fields

| Title                      | ID   | Type       | Data Type                                                                                                                      | Description |
| -------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                       | core | string     |
| accepter_vpc_info          | core | json       | Information about the accepter VPC. CIDR block information is only returned when describing an active VPC peering connection.  |
| account_id                 | core | string     |
| expiration_time            | core | timestamp  | The time that an unaccepted VPC peering connection will expire.                                                                |
| requester_vpc_info         | core | json       | Information about the requester VPC. CIDR block information is only returned when describing an active VPC peering connection. |
| status                     | core | json       | The status of the VPC peering connection.                                                                                      |
| tags                       | core | hstore_csv |
| vpc_peering_connection_arn | core | string     |
| vpc_peering_connection_id  | core | string     | The ID of the VPC peering connection.                                                                                          |
