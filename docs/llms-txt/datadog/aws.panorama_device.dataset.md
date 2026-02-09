# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.panorama_device.dataset.md

---
title: Panorama Appliance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Panorama Appliance
---

# Panorama Appliance

Panorama Appliance in AWS is a physical or virtual device used with AWS Panorama to run computer vision applications at the edge. It allows organizations to deploy and manage machine learning models directly on-premises, processing video streams locally without sending data to the cloud. This reduces latency, improves privacy, and enables real-time insights for use cases like quality control, safety monitoring, and operational efficiency.

```
aws.panorama_device
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                      | Description |
| ------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| alternate_softwares       | core | json       | Beta software releases available for the device.                                                               |
| arn                       | core | string     | The device's ARN.                                                                                              |
| brand                     | core | string     | The device's maker.                                                                                            |
| created_time              | core | timestamp  | When the device was created.                                                                                   |
| current_networking_status | core | json       | The device's networking status.                                                                                |
| current_software          | core | string     | The device's current software version.                                                                         |
| description               | core | string     | The device's description.                                                                                      |
| device_aggregated_status  | core | string     | A device's aggregated status. Including the device's connection status, provisioning status, and lease status. |
| device_connection_status  | core | string     | The device's connection status.                                                                                |
| device_id                 | core | string     | The device's ID.                                                                                               |
| latest_alternate_software | core | string     | The most recent beta software release.                                                                         |
| latest_device_job         | core | json       | A device's latest job. Includes the target image version, and the job status.                                  |
| latest_software           | core | string     | The latest software version available for the device.                                                          |
| lease_expiration_time     | core | timestamp  | The device's lease expiration time.                                                                            |
| name                      | core | string     | The device's name.                                                                                             |
| networking_configuration  | core | json       | The device's networking configuration.                                                                         |
| provisioning_status       | core | string     | The device's provisioning status.                                                                              |
| serial_number             | core | string     | The device's serial number.                                                                                    |
| tags                      | core | hstore_csv |
| type                      | core | string     | The device's type.                                                                                             |
