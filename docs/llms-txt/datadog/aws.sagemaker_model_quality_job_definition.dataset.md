# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_model_quality_job_definition.dataset.md

---
title: SageMaker Model Quality Job Definition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > SageMaker Model Quality Job
  Definition
---

# SageMaker Model Quality Job Definition

SageMaker Model Quality Job Definition in AWS defines the configuration for monitoring the quality of machine learning models. It specifies details such as the model to evaluate, the dataset used for evaluation, the metrics to compute, and the resources required to run the job. This helps ensure models maintain accuracy and reliability over time by continuously assessing their performance against defined baselines.

```
aws.sagemaker_model_quality_job_definition
```

## Fields

| Title                           | ID   | Type       | Data Type                                                                                                                                | Description |
| ------------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string     |
| account_id                      | core | string     |
| creation_time                   | core | timestamp  | The time at which the model quality job was created.                                                                                     |
| job_definition_arn              | core | string     | The Amazon Resource Name (ARN) of the model quality job.                                                                                 |
| job_definition_name             | core | string     | The name of the quality job definition. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account. |
| job_resources                   | core | json       | Identifies the resources to deploy for a monitoring job.                                                                                 |
| model_quality_app_specification | core | json       | Configures the model quality job to run a specified Docker container image.                                                              |
| model_quality_baseline_config   | core | json       | The baseline configuration for a model quality job.                                                                                      |
| model_quality_job_input         | core | json       | Inputs for the model quality job.                                                                                                        |
| model_quality_job_output_config | core | json       | The output configuration for monitoring jobs.                                                                                            |
| network_config                  | core | json       | Networking options for a model quality job.                                                                                              |
| role_arn                        | core | string     | The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform tasks on your behalf.                       |
| stopping_condition              | core | json       | A time limit for how long the monitoring job is allowed to run before stopping.                                                          |
| tags                            | core | hstore_csv |
