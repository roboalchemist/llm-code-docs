# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.deadline_worker.dataset.md

---
title: Deadline Cloud Worker
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Deadline Cloud Worker
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.deadline_worker.dataset/index.html
---

# Deadline Cloud Worker

Deadline Cloud Worker in AWS represents a compute resource within AWS Deadline Cloud, used to process rendering or compute tasks in a managed render farm. Workers are the execution units that pick up jobs from queues and perform the rendering workloads, scaling automatically based on demand.

```
aws.deadline_worker
```

## Fields

| Title           | ID   | Type      | Data Type                                      | Description |
| --------------- | ---- | --------- | ---------------------------------------------- | ----------- |
| _key            | core | string    |
| account_id      | core | string    |
| created_at      | core | timestamp | The date and time the resource was created.    |
| created_by      | core | string    | The user or system that created this resource. |
| farm_id         | core | string    | The farm ID.                                   |
| fleet_id        | core | string    | The fleet ID.                                  |
| host_properties | core | json      | The host properties of the worker.             |
| log             | core | json      | The log configuration for the worker.          |
| status          | core | string    | The status of the worker.                      |
| tags            | core | hstore    |
| updated_at      | core | timestamp | The date and time the resource was updated.    |
| updated_by      | core | string    | The user or system that updated this resource. |
| worker_id       | core | string    | The worker ID.                                 |
