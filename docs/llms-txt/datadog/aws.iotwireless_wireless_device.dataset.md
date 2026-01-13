# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotwireless_wireless_device.dataset.md

---
title: IoT Wireless Wireless Device
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT Wireless Wireless Device
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iotwireless_wireless_device.dataset/index.html
---

# IoT Wireless Wireless Device

An AWS IoT Wireless Device represents a registered endpoint in the AWS IoT Wireless service, which enables you to connect and manage wireless devices using Low Power Wide Area Network (LPWAN) technologies such as LoRaWAN and Sidewalk. It provides details about the device's configuration, identity, and connectivity status, allowing you to monitor and control communication between the device and AWS IoT Core.

```
aws.iotwireless_wireless_device
```

## Fields

| Title            | ID   | Type   | Data Type                                                                                                                  | Description |
| ---------------- | ---- | ------ | -------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key             | core | string |
| account_id       | core | string |
| arn              | core | string | The Amazon Resource Name of the resource.                                                                                  |
| description      | core | string | The description of the resource.                                                                                           |
| destination_name | core | string | The name of the destination to which the device is assigned.                                                               |
| id               | core | string | The ID of the wireless device.                                                                                             |
| lo_ra_wan        | core | json   | Information about the wireless device.                                                                                     |
| name             | core | string | The name of the resource.                                                                                                  |
| positioning      | core | string | FPort values for the GNSS, stream, and ClockSync functions of the positioning information.                                 |
| sidewalk         | core | json   | Sidewalk device object.                                                                                                    |
| tags             | core | hstore |
| thing_arn        | core | string | The ARN of the thing associated with the wireless device.                                                                  |
| thing_name       | core | string | The name of the thing associated with the wireless device. The value is empty if a thing isn't associated with the device. |
| type             | core | string | The wireless device type.                                                                                                  |
