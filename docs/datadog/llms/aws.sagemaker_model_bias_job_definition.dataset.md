# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_model_bias_job_definition.dataset.md

---
title: SageMaker Model Bias Job Definition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Model Bias Job Definition
---

# SageMaker Model Bias Job Definition

An AWS SageMaker Model Bias Job Definition is a resource that specifies the configuration for running bias detection jobs on machine learning models. It defines details such as the dataset used, the model to evaluate, bias metrics, and output locations. This helps monitor and detect potential bias in models to ensure fairness and compliance.

```
aws.sagemaker_model_bias_job_definition
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                                                                                                         | Description |
| ---------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| account_id                   | core | string     |
| creation_time                | core | timestamp  | The time at which the model bias job was created.                                                                                                                 |
| job_definition_arn           | core | string     | The Amazon Resource Name (ARN) of the model bias job.                                                                                                             |
| job_definition_name          | core | string     | The name of the bias job definition. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.                             |
| job_resources                | core | json       | Identifies the resources to deploy for a monitoring job.                                                                                                          |
| model_bias_app_specification | core | json       | Configures the model bias job to run a specified Docker container image.                                                                                          |
| model_bias_baseline_config   | core | json       | The baseline configuration for a model bias job.                                                                                                                  |
| model_bias_job_input         | core | json       | Inputs for the model bias job.                                                                                                                                    |
| model_bias_job_output_config | core | json       | The output configuration for monitoring jobs.                                                                                                                     |
| network_config               | core | json       | Networking options for a model bias job.                                                                                                                          |
| role_arn                     | core | string     | The Amazon Resource Name (ARN) of the IAM role that has read permission to the input data location and write permission to the output data location in Amazon S3. |
| stopping_condition           | core | json       | A time limit for how long the monitoring job is allowed to run before stopping.                                                                                   |
| tags                         | core | hstore_csv |
