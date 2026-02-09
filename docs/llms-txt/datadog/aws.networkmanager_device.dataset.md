# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.networkmanager_device.dataset.md

---
title: Network Manager Device
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Manager Device
---

# Network Manager Device

Represents a physical or virtual device in AWS Network Manager, such as a router, switch, or customer premises equipment, that is part of a global network. It helps model and manage on-premises and cloud network infrastructure by tracking device details, locations, and connections.

```
aws.networkmanager_device
```

## Fields

| Title             | ID   | Type       | Data Type                                       | Description |
| ----------------- | ---- | ---------- | ----------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| aws_location      | core | json       | The Amazon Web Services location of the device. |
| created_at        | core | timestamp  | The date and time that the site was created.    |
| description       | core | string     | The description of the device.                  |
| device_arn        | core | string     | The Amazon Resource Name (ARN) of the device.   |
| device_id         | core | string     | The ID of the device.                           |
| global_network_id | core | string     | The ID of the global network.                   |
| location          | core | json       | The site location.                              |
| model             | core | string     | The device model.                               |
| serial_number     | core | string     | The device serial number.                       |
| site_id           | core | string     | The site ID.                                    |
| state             | core | string     | The device state.                               |
| tags              | core | hstore_csv |
| type              | core | string     | The device type.                                |
| vendor            | core | string     | The device vendor.                              |
