# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotfleetwise_signal_catalog.dataset.md

---
title: IoT FleetWise Signal Catalog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT FleetWise Signal Catalog
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iotfleetwise_signal_catalog.dataset/index.html
---

# IoT FleetWise Signal Catalog

AWS IoT FleetWise Signal Catalog is a centralized repository that defines and organizes vehicle signals, such as sensor data, attributes, and custom metrics. It allows you to standardize how vehicle data is described and accessed across different vehicle models and fleets. By using the signal catalog, you can ensure consistency in data collection, simplify integration with applications, and streamline the process of managing and analyzing vehicle telemetry at scale.

```gdscript3
aws.iotfleetwise_signal_catalog
```

## Fields

| Title                  | ID   | Type      | Data Type                                                                                              | Description |
| ---------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------ | ----------- |
| _key                   | core | string    |
| account_id             | core | string    |
| arn                    | core | string    | The Amazon Resource Name (ARN) of the signal catalog.                                                  |
| creation_time          | core | timestamp | The time the signal catalog was created in seconds since epoch (January 1, 1970 at midnight UTC time). |
| description            | core | string    | A brief description of the signal catalog.                                                             |
| last_modification_time | core | timestamp | The last time the signal catalog was modified.                                                         |
| name                   | core | string    | The name of the signal catalog.                                                                        |
| node_counts            | core | json      | The total number of network nodes specified in a signal catalog.                                       |
| tags                   | core | hstore    |
