# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotwireless_device.dataset.md

---
title: Iotwireless Device
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Iotwireless Device
---

# Iotwireless Device

This table represents the iotwireless_device resource from Amazon Web Services.

```
aws.iotwireless_device
```

## Fields

| Title            | ID   | Type       | Data Type                                                                                                                  | Description |
| ---------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| arn              | core | string     | The Amazon Resource Name of the resource.                                                                                  |
| description      | core | string     | The description of the resource.                                                                                           |
| destination_name | core | string     | The name of the destination to which the device is assigned.                                                               |
| id               | core | string     | The ID of the wireless device.                                                                                             |
| lo_ra_wan        | core | json       | Information about the wireless device.                                                                                     |
| name             | core | string     | The name of the resource.                                                                                                  |
| positioning      | core | string     | FPort values for the GNSS, stream, and ClockSync functions of the positioning information.                                 |
| sidewalk         | core | json       | Sidewalk device object.                                                                                                    |
| tags             | core | hstore_csv |
| thing_arn        | core | string     | The ARN of the thing associated with the wireless device.                                                                  |
| thing_name       | core | string     | The name of the thing associated with the wireless device. The value is empty if a thing isn't associated with the device. |
| type             | core | string     | The wireless device type.                                                                                                  |
