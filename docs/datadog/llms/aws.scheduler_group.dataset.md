# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.scheduler_group.dataset.md

---
title: EventBridge Scheduler Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EventBridge Scheduler Group
---

# EventBridge Scheduler Group

This table represents the EventBridge Scheduler Group resource from Amazon Web Services.

```
aws.scheduler_group
```

## Fields

| Title                  | ID   | Type       | Data Type                                               | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| arn                    | core | string     | The Amazon Resource Name (ARN) of the schedule group.   |
| creation_date          | core | timestamp  | The time at which the schedule group was created.       |
| last_modification_date | core | timestamp  | The time at which the schedule group was last modified. |
| name                   | core | string     | The name of the schedule group.                         |
| state                  | core | string     | Specifies the state of the schedule group.              |
| tags                   | core | hstore_csv |
