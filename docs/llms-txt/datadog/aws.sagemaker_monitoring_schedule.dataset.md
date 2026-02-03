# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_monitoring_schedule.dataset.md

---
title: SageMaker Monitoring Schedule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Monitoring Schedule
---

# SageMaker Monitoring Schedule

SageMaker Monitoring Schedule is an AWS resource that defines and manages recurring monitoring jobs for machine learning models. It allows you to automatically run data quality, model quality, bias, or feature attribution checks on a set schedule. This helps ensure models remain accurate, fair, and reliable over time by continuously evaluating their performance against defined baselines.

```
aws.sagemaker_monitoring_schedule
```

## Fields

| Title                             | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                               | Description |
| --------------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                              | core | string     |
| account_id                        | core | string     |
| creation_time                     | core | timestamp  | The time at which the monitoring job was created.                                                                                                                                                                                                                                                                                                                       |
| endpoint_name                     | core | string     | The name of the endpoint for the monitoring job.                                                                                                                                                                                                                                                                                                                        |
| failure_reason                    | core | string     | A string, up to one KB in size, that contains the reason a monitoring job failed, if it failed.                                                                                                                                                                                                                                                                         |
| last_modified_time                | core | timestamp  | The time at which the monitoring job was last modified.                                                                                                                                                                                                                                                                                                                 |
| last_monitoring_execution_summary | core | json       | Describes metadata on the last execution to run, if there was one.                                                                                                                                                                                                                                                                                                      |
| monitoring_schedule_arn           | core | string     | The Amazon Resource Name (ARN) of the monitoring schedule.                                                                                                                                                                                                                                                                                                              |
| monitoring_schedule_config        | core | json       | The configuration object that specifies the monitoring schedule and defines the monitoring job.                                                                                                                                                                                                                                                                         |
| monitoring_schedule_name          | core | string     | Name of the monitoring schedule.                                                                                                                                                                                                                                                                                                                                        |
| monitoring_schedule_status        | core | string     | The status of an monitoring job.                                                                                                                                                                                                                                                                                                                                        |
| monitoring_type                   | core | string     | The type of the monitoring job that this schedule runs. This is one of the following values. DATA_QUALITY - The schedule is for a data quality monitoring job. MODEL_QUALITY - The schedule is for a model quality monitoring job. MODEL_BIAS - The schedule is for a bias monitoring job. MODEL_EXPLAINABILITY - The schedule is for an explainability monitoring job. |
| tags                              | core | hstore_csv |
