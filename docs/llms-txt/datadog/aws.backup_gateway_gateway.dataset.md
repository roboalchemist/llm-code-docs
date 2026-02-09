# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.backup_gateway_gateway.dataset.md

---
title: Backup Gateway Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Backup Gateway Gateway
---

# Backup Gateway Gateway

This table represents the Backup Gateway Gateway resource from Amazon Web Services.

```
aws.backup_gateway_gateway
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                                                                                                                        | Description |
| ----------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string     |
| account_id                    | core | string     |
| gateway_arn                   | core | string     | The Amazon Resource Name (ARN) of the gateway. Use the <code>ListGateways</code> operation to return a list of gateways for your account and Amazon Web Services Region.         |
| gateway_display_name          | core | string     | The display name of the gateway.                                                                                                                                                 |
| gateway_type                  | core | string     | The type of the gateway type.                                                                                                                                                    |
| hypervisor_id                 | core | string     | The hypervisor ID of the gateway.                                                                                                                                                |
| last_seen_time                | core | timestamp  | Details showing the last time Backup gateway communicated with the cloud, in Unix format and UTC time.                                                                           |
| maintenance_start_time        | core | json       | Returns your gateway's weekly maintenance start time including the day and time of the week. Note that values are in terms of the gateway's time zone. Can be weekly or monthly. |
| next_update_availability_time | core | timestamp  | Details showing the next update availability time of the gateway.                                                                                                                |
| tags                          | core | hstore_csv |
| vpc_endpoint                  | core | string     | The DNS name for the virtual private cloud (VPC) endpoint the gateway uses to connect to the cloud for backup gateway.                                                           |
