# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.quicksight_refresh_schedule.dataset.md

---
title: QuickSight Refresh Schedule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > QuickSight Refresh Schedule
---

# QuickSight Refresh Schedule

QuickSight Refresh Schedule in AWS defines how and when datasets in Amazon QuickSight are automatically refreshed. It allows you to set up recurring schedules to update data from source systems, ensuring dashboards and analyses always reflect the latest information. This helps maintain data accuracy without requiring manual refreshes.

```
aws.quicksight_refresh_schedule
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                              | Description |
| --------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| arn                   | core | string     | The Amazon Resource Name (ARN) for the refresh schedule.                                                                                                                                                                                                                                                                                               |
| refresh_type          | core | string     | The type of refresh that a datset undergoes. Valid values are as follows: FULL_REFRESH: A complete refresh of a dataset. INCREMENTAL_REFRESH: A partial refresh of some rows of a dataset, based on the time window specified. For more information on full and incremental refreshes, see Refreshing SPICE data in the Amazon Quick Suite User Guide. |
| schedule_frequency    | core | json       | The frequency for the refresh schedule.                                                                                                                                                                                                                                                                                                                |
| schedule_id           | core | string     | An identifier for the refresh schedule.                                                                                                                                                                                                                                                                                                                |
| start_after_date_time | core | timestamp  | Time after which the refresh schedule can be started, expressed in YYYY-MM-DDTHH:MM:SS format.                                                                                                                                                                                                                                                         |
| tags                  | core | hstore_csv |
