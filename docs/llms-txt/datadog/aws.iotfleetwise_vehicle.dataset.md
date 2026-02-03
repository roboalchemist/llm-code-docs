# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotfleetwise_vehicle.dataset.md

---
title: IoT FleetWise Vehicle
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT FleetWise Vehicle
---

# IoT FleetWise Vehicle

An IoT FleetWise Vehicle in AWS represents a digital model of a physical vehicle that you can manage within the IoT FleetWise service. It stores vehicle attributes, such as make, model, and year, and links to signal catalogs and decoder manifests. This resource allows you to collect, organize, and transfer vehicle data to the cloud for analysis, monitoring, and building connected vehicle applications.

```
aws.iotfleetwise_vehicle
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                            | Description |
| ---------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| arn                    | core | string     | The Amazon Resource Name (ARN) of the vehicle to retrieve information about.                         |
| attributes             | core | hstore     | Static information about a vehicle in a key-value pair. For example: "engineType" : "1.3 L R2"       |
| creation_time          | core | timestamp  | The time the vehicle was created in seconds since epoch (January 1, 1970 at midnight UTC time).      |
| decoder_manifest_arn   | core | string     | The ARN of a decoder manifest associated with the vehicle.                                           |
| last_modification_time | core | timestamp  | The time the vehicle was last updated in seconds since epoch (January 1, 1970 at midnight UTC time). |
| model_manifest_arn     | core | string     | The ARN of a vehicle model (model manifest) associated with the vehicle.                             |
| state_templates        | core | json       | State templates associated with the vehicle.                                                         |
| tags                   | core | hstore_csv |
| vehicle_name           | core | string     | The ID of the vehicle.                                                                               |
