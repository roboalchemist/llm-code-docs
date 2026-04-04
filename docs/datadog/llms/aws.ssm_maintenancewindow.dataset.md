# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ssm_maintenancewindow.dataset.md

---
title: Systems Manager Maintenance Window
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Systems Manager Maintenance Window
---

# Systems Manager Maintenance Window

This table represents the Systems Manager Maintenance Window resource from Amazon Web Services.

```
aws.ssm_maintenancewindow
```

## Fields

| Title                      | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                          | Description |
| -------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                       | core | string     |
| account_id                 | core | string     |
| allow_unassociated_targets | core | bool       | Whether targets must be registered with the maintenance window before tasks can be defined for those targets.                                                                                                                                                                                                      |
| created_date               | core | timestamp  | The date the maintenance window was created.                                                                                                                                                                                                                                                                       |
| cutoff                     | core | int64      | The number of hours before the end of the maintenance window that Amazon Web Services Systems Manager stops scheduling new tasks for execution.                                                                                                                                                                    |
| description                | core | string     | The description of the maintenance window.                                                                                                                                                                                                                                                                         |
| duration                   | core | int64      | The duration of the maintenance window in hours.                                                                                                                                                                                                                                                                   |
| enabled                    | core | bool       | Indicates whether the maintenance window is enabled.                                                                                                                                                                                                                                                               |
| end_date                   | core | string     | The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become inactive. The maintenance window won't run after this specified time.                                                                                                                                       |
| modified_date              | core | timestamp  | The date the maintenance window was last modified.                                                                                                                                                                                                                                                                 |
| name                       | core | string     | The name of the maintenance window.                                                                                                                                                                                                                                                                                |
| next_execution_time        | core | string     | The next time the maintenance window will actually run, taking into account any specified times for the maintenance window to become active or inactive.                                                                                                                                                           |
| schedule                   | core | string     | The schedule of the maintenance window in the form of a cron or rate expression.                                                                                                                                                                                                                                   |
| schedule_offset            | core | int64      | The number of days to wait to run a maintenance window after the scheduled cron expression date and time.                                                                                                                                                                                                          |
| schedule_timezone          | core | string     | The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los_Angeles", "UTC", or "Asia/Seoul". For more information, see the <a href="https://www.iana.org/time-zones">Time Zone Database</a> on the IANA website. |
| start_date                 | core | string     | The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become active. The maintenance window won't run before this specified time.                                                                                                                                        |
| tags                       | core | hstore_csv |
| window_id                  | core | string     | The ID of the created maintenance window.                                                                                                                                                                                                                                                                          |
