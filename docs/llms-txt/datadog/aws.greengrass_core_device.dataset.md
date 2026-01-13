# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.greengrass_core_device.dataset.md

---
title: Greengrass Core Device
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Greengrass Core Device
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.greengrass_core_device.dataset/index.html
---

# Greengrass Core Device

This table represents the greengrass_core_device resource from Amazon Web Services.

```
aws.greengrass_core_device
```

## Fields

| Title                        | ID   | Type      | Data Type                                                                                                                                                                                                                                                                                                                                                                                                   | Description |
| ---------------------------- | ---- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string    |
| account_id                   | core | string    |
| architecture                 | core | string    | The computer architecture of the core device.                                                                                                                                                                                                                                                                                                                                                               |
| core_device_thing_name       | core | string    | The name of the core device. This is also the name of the IoT thing.                                                                                                                                                                                                                                                                                                                                        |
| core_version                 | core | string    | The version of the IoT Greengrass Core software that the core device runs. This version is equivalent to the version of the Greengrass nucleus component that runs on the core device. For more information, see the <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html">Greengrass nucleus component</a> in the <i>IoT Greengrass V2 Developer Guide</i>. |
| last_status_update_timestamp | core | timestamp | The time at which the core device's status last updated, expressed in ISO 8601 format.                                                                                                                                                                                                                                                                                                                      |
| platform                     | core | string    | The operating system platform that the core device runs.                                                                                                                                                                                                                                                                                                                                                    |
| runtime                      | core | string    | The runtime for the core device. The runtime can be: <ul> <li> <code>aws_nucleus_classic</code> </li> <li> <code>aws_nucleus_lite</code> </li> </ul>                                                                                                                                                                                                                                                        |
| status                       | core | string    | The status of the core device. The core device status can be: <ul> <li> <code>HEALTHY</code> â The IoT Greengrass Core software and all components run on the core device without issue. </li> <li> <code>UNHEALTHY</code> â The IoT Greengrass Core software or a component is in a failed state on the core device. </li> </ul>                                                                           |
| tags                         | core | hstore    |
