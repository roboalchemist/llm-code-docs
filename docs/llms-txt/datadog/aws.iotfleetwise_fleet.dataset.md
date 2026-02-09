# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotfleetwise_fleet.dataset.md

---
title: IoT FleetWise Fleet
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT FleetWise Fleet
---

# IoT FleetWise Fleet

An IoT FleetWise Fleet in AWS represents a group of vehicles managed together for data collection and analysis. It allows you to organize vehicles, define data collection schemes, and manage how vehicle telemetry is ingested into AWS. This resource helps streamline large-scale vehicle data management, enabling insights, monitoring, and integration with analytics or machine learning services.

```
aws.iotfleetwise_fleet
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                          | Description |
| ---------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| arn                    | core | string     | The Amazon Resource Name (ARN) of the fleet.                                                       |
| creation_time          | core | timestamp  | The time the fleet was created, in seconds since epoch (January 1, 1970 at midnight UTC time).     |
| description            | core | string     | A brief description of the fleet.                                                                  |
| id                     | core | string     | The unique ID of the fleet.                                                                        |
| last_modification_time | core | timestamp  | The time the fleet was last updated in seconds since epoch (January 1, 1970 at midnight UTC time). |
| signal_catalog_arn     | core | string     | The ARN of the signal catalog associated with the fleet.                                           |
| tags                   | core | hstore_csv |
