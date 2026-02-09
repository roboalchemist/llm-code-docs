# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.drs_job.dataset.md

---
title: Elastic Disaster Recovery Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elastic Disaster Recovery Job
---

# Elastic Disaster Recovery Job

An Elastic Disaster Recovery Job in AWS represents a task or operation performed by the Elastic Disaster Recovery (DRS) service. It tracks activities such as launching recovery instances, replicating data, or performing failover and failback processes. Jobs provide status, progress, and outcome details, helping users monitor and manage disaster recovery workflows effectively.

```
aws.drs_job
```

## Fields

| Title                   | ID   | Type       | Data Type                                        | Description |
| ----------------------- | ---- | ---------- | ------------------------------------------------ | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| arn                     | core | string     | The ARN of a Job.                                |
| creation_date_time      | core | string     | The date and time of when the Job was created.   |
| end_date_time           | core | string     | The date and time of when the Job ended.         |
| initiated_by            | core | string     | A string representing who initiated the Job.     |
| job_id                  | core | string     | The ID of the Job.                               |
| participating_resources | core | json       | A list of resources that the Job is acting upon. |
| participating_servers   | core | json       | A list of servers that the Job is acting upon.   |
| status                  | core | string     | The status of the Job.                           |
| tags                    | core | hstore_csv |
| type                    | core | string     | The type of the Job.                             |
