# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotwireless_gateway.dataset.md

---
title: Iotwireless Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Iotwireless Gateway
---

# Iotwireless Gateway

This table represents the iotwireless_gateway resource from Amazon Web Services.

```
aws.iotwireless_gateway
```

## Fields

| Title       | ID   | Type       | Data Type                                                                                                                    | Description |
| ----------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key        | core | string     |
| account_id  | core | string     |
| arn         | core | string     | The Amazon Resource Name of the resource.                                                                                    |
| description | core | string     | The description of the resource.                                                                                             |
| id          | core | string     | The ID of the wireless gateway.                                                                                              |
| lo_ra_wan   | core | json       | Information about the wireless gateway.                                                                                      |
| name        | core | string     | The name of the resource.                                                                                                    |
| tags        | core | hstore_csv |
| thing_arn   | core | string     | The ARN of the thing associated with the wireless gateway.                                                                   |
| thing_name  | core | string     | The name of the thing associated with the wireless gateway. The value is empty if a thing isn't associated with the gateway. |
