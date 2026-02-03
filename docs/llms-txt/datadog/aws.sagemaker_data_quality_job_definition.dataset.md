# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_data_quality_job_definition.dataset.md

---
title: SageMaker Data Quality Job Definition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > SageMaker Data Quality Job
  Definition
---

# SageMaker Data Quality Job Definition

SageMaker Data Quality Job Definition in AWS defines the configuration for monitoring and evaluating the quality of data used in machine learning workflows. It specifies details such as the dataset, monitoring schedule, resources, and output location for reports. This helps detect issues like missing values, data drift, or anomalies, ensuring that models are trained and evaluated on reliable data.

```
aws.sagemaker_data_quality_job_definition
```

## Fields

| Title                          | ID   | Type       | Data Type                                                                                                          | Description |
| ------------------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                           | core | string     |
| account_id                     | core | string     |
| creation_time                  | core | timestamp  | The time that the data quality monitoring job definition was created.                                              |
| data_quality_app_specification | core | json       | Information about the container that runs the data quality monitoring job.                                         |
| data_quality_baseline_config   | core | json       | The constraints and baselines for the data quality monitoring job definition.                                      |
| data_quality_job_input         | core | json       | The list of inputs for the data quality monitoring job. Currently endpoints are supported.                         |
| data_quality_job_output_config | core | json       | The output configuration for monitoring jobs.                                                                      |
| job_definition_arn             | core | string     | The Amazon Resource Name (ARN) of the data quality monitoring job definition.                                      |
| job_definition_name            | core | string     | The name of the data quality monitoring job definition.                                                            |
| job_resources                  | core | json       | Identifies the resources to deploy for a monitoring job.                                                           |
| network_config                 | core | json       | The networking configuration for the data quality monitoring job.                                                  |
| role_arn                       | core | string     | The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform tasks on your behalf. |
| stopping_condition             | core | json       | A time limit for how long the monitoring job is allowed to run before stopping.                                    |
| tags                           | core | hstore_csv |
