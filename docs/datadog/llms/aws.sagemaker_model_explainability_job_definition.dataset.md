# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_model_explainability_job_definition.dataset.md

---
title: SageMaker Model Explainability Job Definition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > SageMaker Model Explainability Job
  Definition
---

# SageMaker Model Explainability Job Definition

An AWS SageMaker Model Explainability Job Definition is a resource that specifies the configuration for running explainability jobs on machine learning models. It defines how to generate insights into model predictions, such as feature importance or bias detection, using preconfigured tools. This job definition includes details like the model to analyze, input datasets, output locations, and compute resources. It allows you to consistently run explainability analyses on models to improve transparency, compliance, and trust in machine learning outcomes.

```
aws.sagemaker_model_explainability_job_definition
```

## Fields

| Title                                  | ID   | Type       | Data Type                                                                                                                                                         | Description |
| -------------------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                   | core | string     |
| account_id                             | core | string     |
| creation_time                          | core | timestamp  | The time at which the model explainability job was created.                                                                                                       |
| job_definition_arn                     | core | string     | The Amazon Resource Name (ARN) of the model explainability job.                                                                                                   |
| job_definition_name                    | core | string     | The name of the explainability job definition. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.                   |
| job_resources                          | core | json       | Identifies the resources to deploy for a monitoring job.                                                                                                          |
| model_explainability_app_specification | core | json       | Configures the model explainability job to run a specified Docker container image.                                                                                |
| model_explainability_baseline_config   | core | json       | The baseline configuration for a model explainability job.                                                                                                        |
| model_explainability_job_input         | core | json       | Inputs for the model explainability job.                                                                                                                          |
| model_explainability_job_output_config | core | json       | The output configuration for monitoring jobs.                                                                                                                     |
| network_config                         | core | json       | Networking options for a model explainability job.                                                                                                                |
| role_arn                               | core | string     | The Amazon Resource Name (ARN) of the IAM role that has read permission to the input data location and write permission to the output data location in Amazon S3. |
| stopping_condition                     | core | json       | A time limit for how long the monitoring job is allowed to run before stopping.                                                                                   |
| tags                                   | core | hstore_csv |
