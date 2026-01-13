# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotfleetwise_model_manifest.dataset.md

---
title: IoT FleetWise Model Manifest
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT FleetWise Model Manifest
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iotfleetwise_model_manifest.dataset/index.html
---

# IoT FleetWise Model Manifest

An IoT FleetWise Model Manifest in AWS defines the structure and relationships of vehicle signals and data models. It acts as a blueprint that describes how vehicle data is organized, enabling consistent data collection, transformation, and transmission from vehicles to the cloud. This resource helps standardize signal definitions across fleets, making it easier to manage, analyze, and integrate vehicle telemetry at scale.

```
aws.iotfleetwise_model_manifest
```

## Fields

| Title                  | ID   | Type      | Data Type                                                                                                                                           | Description |
| ---------------------- | ---- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string    |
| account_id             | core | string    |
| arn                    | core | string    | The Amazon Resource Name (ARN) of the vehicle model.                                                                                                |
| creation_time          | core | timestamp | The time the vehicle model was created, in seconds since epoch (January 1, 1970 at midnight UTC time).                                              |
| description            | core | string    | A brief description of the vehicle model.                                                                                                           |
| last_modification_time | core | timestamp | The time the vehicle model was last updated, in seconds since epoch (January 1, 1970 at midnight UTC time).                                         |
| name                   | core | string    | The name of the vehicle model.                                                                                                                      |
| signal_catalog_arn     | core | string    | The ARN of the signal catalog associated with the vehicle model.                                                                                    |
| status                 | core | string    | The state of the vehicle model. If the status is ACTIVE, the vehicle model can't be edited. If the status is DRAFT, you can edit the vehicle model. |
| tags                   | core | hstore    |
