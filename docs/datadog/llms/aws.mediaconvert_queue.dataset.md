# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediaconvert_queue.dataset.md

---
title: AWS Elemental MediaConvert Queue
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS Elemental MediaConvert Queue
---

# AWS Elemental MediaConvert Queue

An AWS Elemental MediaConvert Queue manages the order and concurrency of video transcoding jobs. It allows you to control how many jobs run simultaneously and prioritize workloads by assigning them to different queues. Queues help optimize resource usage, manage throughput, and ensure that high-priority video processing tasks are completed efficiently.

```
aws.mediaconvert_queue
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                   | Description |
| ---------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| arn                    | core | string     | An identifier for this resource that is unique within all of AWS.                                                                                                                                                                                                                                                           |
| concurrent_jobs        | core | int64      | The maximum number of jobs your queue can process concurrently.                                                                                                                                                                                                                                                             |
| created_at             | core | timestamp  | The timestamp in epoch seconds for when you created the queue.                                                                                                                                                                                                                                                              |
| description            | core | string     | An optional description that you create for each queue.                                                                                                                                                                                                                                                                     |
| last_updated           | core | timestamp  | The timestamp in epoch seconds for when you most recently updated the queue.                                                                                                                                                                                                                                                |
| name                   | core | string     | A name that you create for each queue. Each name must be unique within your account.                                                                                                                                                                                                                                        |
| pricing_plan           | core | string     | Specifies whether the pricing plan for the queue is on-demand or reserved. For on-demand, you pay per minute, billed in increments of .01 minute. For reserved, you pay for the transcoding capacity of the entire queue, regardless of how much or how little you use it. Reserved pricing requires a 12-month commitment. |
| progressing_jobs_count | core | int64      | The estimated number of jobs with a PROGRESSING status.                                                                                                                                                                                                                                                                     |
| reservation_plan       | core | json       | Details about the pricing plan for your reserved queue. Required for reserved queues and not applicable to on-demand queues.                                                                                                                                                                                                |
| service_overrides      | core | json       | A list of any service overrides applied by MediaConvert to the settings that you have configured. If you see any overrides, we recommend that you contact AWS Support.                                                                                                                                                      |
| status                 | core | string     | Queues can be ACTIVE or PAUSED. If you pause a queue, the service won't begin processing jobs in that queue. Jobs that are running when you pause the queue continue to run until they finish or result in an error.                                                                                                        |
| submitted_jobs_count   | core | int64      | The estimated number of jobs with a SUBMITTED status.                                                                                                                                                                                                                                                                       |
| tags                   | core | hstore_csv |
| type                   | core | string     | Specifies whether this on-demand queue is system or custom. System queues are built in. You can't modify or delete system queues. You can create and modify custom queues.                                                                                                                                                  |
