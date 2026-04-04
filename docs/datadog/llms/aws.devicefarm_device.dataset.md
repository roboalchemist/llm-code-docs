# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.devicefarm_device.dataset.md

---
title: Device Farm Device
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Device Farm Device
---

# Device Farm Device

An AWS Device Farm Device represents a real mobile device available in the Device Farm service. It provides details such as the device model, manufacturer, operating system, form factor, and availability. This resource allows you to select and run tests on specific physical devices to ensure your applications work correctly across different hardware and software configurations.

```
aws.devicefarm_device
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                                                                    | Description |
| --------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| arn                   | core | string     | The device's ARN.                                                                                                            |
| availability          | core | string     | Indicates how likely a device is available for a test run. Currently available in the ListDevices and GetDevice API methods. |
| carrier               | core | string     | The device's carrier.                                                                                                        |
| cpu                   | core | json       | Information about the device's CPU.                                                                                          |
| fleet_name            | core | string     | The name of the fleet to which this device belongs.                                                                          |
| fleet_type            | core | string     | The type of fleet to which this device belongs. Possible values are PRIVATE and PUBLIC.                                      |
| form_factor           | core | string     | The device's form factor. Allowed values include: PHONE TABLET                                                               |
| heap_size             | core | int64      | The device's heap size, expressed in bytes.                                                                                  |
| image                 | core | string     | The device's image name.                                                                                                     |
| instances             | core | json       | The instances that belong to this device.                                                                                    |
| manufacturer          | core | string     | The device's manufacturer name.                                                                                              |
| memory                | core | int64      | The device's total memory size, expressed in bytes.                                                                          |
| model                 | core | string     | The device's model name.                                                                                                     |
| model_id              | core | string     | The device's model ID.                                                                                                       |
| name                  | core | string     | The device's display name.                                                                                                   |
| os                    | core | string     | The device's operating system type.                                                                                          |
| platform              | core | string     | The device's platform. Allowed values include: ANDROID IOS                                                                   |
| radio                 | core | string     | The device's radio.                                                                                                          |
| remote_access_enabled | core | bool       | Specifies whether remote access has been enabled for the specified device.                                                   |
| remote_debug_enabled  | core | bool       | This flag is set to true if remote debugging is enabled for the device. Remote debugging is no longer supported.             |
| resolution            | core | json       | The resolution of the device.                                                                                                |
| tags                  | core | hstore_csv |
