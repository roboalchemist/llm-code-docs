# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.deadline_fleet.dataset.md

---
title: Deadline Cloud Fleet
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Deadline Cloud Fleet
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.deadline_fleet.dataset/index.html
---

# Deadline Cloud Fleet

Deadline Cloud Fleet in AWS is a managed resource within AWS Deadline Cloud that represents a group of compute resources used for rendering workloads. A fleet defines the capacity, instance types, and scaling behavior for rendering jobs, allowing studios to efficiently manage and optimize compute usage for visual effects, animation, and other high-performance rendering tasks.

```
aws.deadline_fleet
```

## Fields

| Title               | ID   | Type      | Data Type                                             | Description |
| ------------------- | ---- | --------- | ----------------------------------------------------- | ----------- |
| _key                | core | string    |
| account_id          | core | string    |
| auto_scaling_status | core | string    | The Auto Scaling status of a fleet.                   |
| configuration       | core | json      | The configuration details for the fleet.              |
| created_at          | core | timestamp | The date and time the resource was created.           |
| created_by          | core | string    | The user or system that created this resource.        |
| farm_id             | core | string    | The farm ID.                                          |
| fleet_id            | core | string    | The fleet ID.                                         |
| max_worker_count    | core | int64     | The maximum number of workers specified in the fleet. |
| min_worker_count    | core | int64     | The minimum number of workers in the fleet.           |
| status              | core | string    | The status of the fleet.                              |
| tags                | core | hstore    |
| target_worker_count | core | int64     | The target number of workers in a fleet.              |
| updated_at          | core | timestamp | The date and time the resource was updated.           |
| updated_by          | core | string    | The user or system that updated this resource.        |
| worker_count        | core | int64     | The number of workers in the fleet summary.           |
