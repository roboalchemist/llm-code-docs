# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.athena_capacityreservation.dataset.md

---
title: Athena Capacity Reservation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Athena Capacity Reservation
---

# Athena Capacity Reservation

This table represents the Athena Capacity Reservation resource from Amazon Web Services.

```
aws.athena_capacityreservation
```

## Fields

| Title                           | ID   | Type       | Data Type                                                               | Description |
| ------------------------------- | ---- | ---------- | ----------------------------------------------------------------------- | ----------- |
| _key                            | core | string     |
| account_id                      | core | string     |
| allocated_dpus                  | core | int64      | The number of data processing units currently allocated.                |
| creation_time                   | core | timestamp  | The time in UTC epoch millis when the capacity reservation was created. |
| last_allocation                 | core | json       |
| last_successful_allocation_time | core | timestamp  | The time of the most recent capacity allocation that succeeded.         |
| name                            | core | string     | The name of the capacity reservation.                                   |
| status                          | core | string     | The status of the capacity reservation.                                 |
| tags                            | core | hstore_csv |
| target_dpus                     | core | int64      | The number of data processing units requested.                          |
