# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.autoscaling_scheduled_action.dataset.md

---
title: Auto Scaling Scheduled Action
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Auto Scaling Scheduled Action
---

# Auto Scaling Scheduled Action

This table represents the Auto Scaling Scheduled Action resource from Amazon Web Services.

```
aws.autoscaling_scheduled_action
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                                                                                                                                                                   | Description |
| ----------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| auto_scaling_group_name | core | string     | The name of the Auto Scaling group.                                                                                                                                                                                                         |
| desired_capacity        | core | int64      | The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.                                                                                            |
| end_time                | core | timestamp  | The date and time in UTC for the recurring schedule to end. For example, <code>"2019-06-01T00:00:00Z"</code>.                                                                                                                               |
| max_size                | core | int64      | The maximum size of the Auto Scaling group.                                                                                                                                                                                                 |
| min_size                | core | int64      | The minimum size of the Auto Scaling group.                                                                                                                                                                                                 |
| recurrence              | core | string     | The recurring schedule for the action, in Unix cron syntax format. When <code>StartTime</code> and <code>EndTime</code> are specified with <code>Recurrence</code>, they form the boundaries of when the recurring action starts and stops. |
| scheduled_action_arn    | core | string     | The Amazon Resource Name (ARN) of the scheduled action.                                                                                                                                                                                     |
| scheduled_action_name   | core | string     | The name of the scheduled action.                                                                                                                                                                                                           |
| start_time              | core | timestamp  | The date and time in UTC for this action to start. For example, <code>"2019-06-01T00:00:00Z"</code>.                                                                                                                                        |
| tags                    | core | hstore_csv |
| time                    | core | timestamp  | This property is no longer used.                                                                                                                                                                                                            |
| time_zone               | core | string     | The time zone for the cron expression.                                                                                                                                                                                                      |
