# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.deadline_queue.dataset.md

---
title: Deadline Cloud Queue
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Deadline Cloud Queue
---

# Deadline Cloud Queue

Deadline Cloud Queue in AWS is a managed resource within AWS Deadline Cloud that represents a queue for rendering or compute tasks. It organizes and manages the distribution of jobs to worker fleets, ensuring tasks are processed efficiently. Queues help control priorities, manage workloads, and optimize resource usage for rendering pipelines.

```
aws.deadline_queue
```

## Fields

| Title                               | ID   | Type          | Data Type                                                                                                                                                                                           | Description |
| ----------------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                | core | string        |
| account_id                          | core | string        |
| allowed_storage_profile_ids         | core | array<string> | The storage profile IDs for the queue.                                                                                                                                                              |
| blocked_reason                      | core | string        | The reason the queue was blocked.                                                                                                                                                                   |
| created_at                          | core | timestamp     | The date and time the resource was created.                                                                                                                                                         |
| created_by                          | core | string        | The user or system that created this resource.                                                                                                                                                      |
| default_budget_action               | core | string        | The default action taken on a queue if a budget wasn't configured.                                                                                                                                  |
| description                         | core | string        | The description of the queue. This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field. |
| farm_id                             | core | string        | The farm ID for the queue.                                                                                                                                                                          |
| job_attachment_settings             | core | json          | The job attachment settings for the queue.                                                                                                                                                          |
| job_run_as_user                     | core | json          | The jobs in the queue ran as this specified POSIX user.                                                                                                                                             |
| queue_id                            | core | string        | The queue ID.                                                                                                                                                                                       |
| required_file_system_location_names | core | array<string> | A list of the required file system location names in the queue.                                                                                                                                     |
| role_arn                            | core | string        | The IAM role ARN.                                                                                                                                                                                   |
| status                              | core | string        | The status of the queue. ACTIVEâThe queue is active. SCHEDULINGâThe queue is scheduling. SCHEDULING_BLOCKEDâThe queue scheduling is blocked. See the provided reason.                               |
| tags                                | core | hstore_csv    |
| updated_at                          | core | timestamp     | The date and time the resource was updated.                                                                                                                                                         |
| updated_by                          | core | string        | The user or system that updated this resource.                                                                                                                                                      |
