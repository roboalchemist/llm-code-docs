# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_pipeline.dataset.md

---
title: SageMaker Pipeline
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Pipeline
---

# SageMaker Pipeline

SageMaker Pipeline is an AWS resource that enables the creation, automation, and management of machine learning workflows. It allows you to define steps such as data preparation, model training, evaluation, and deployment in a structured sequence. This helps streamline ML operations, improve reproducibility, and simplify collaboration across teams.

```
aws.sagemaker_pipeline
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                | Description |
| ------------------------- | ---- | ---------- | ------------------------------------------------------------------------ | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| created_by                | core | json       | Information about the user who created or modified a SageMaker resource. |
| creation_time             | core | timestamp  | The time when the pipeline was created.                                  |
| last_modified_by          | core | json       | Information about the user who created or modified a SageMaker resource. |
| last_modified_time        | core | timestamp  | The time when the pipeline was last modified.                            |
| last_run_time             | core | timestamp  | The time when the pipeline was last run.                                 |
| parallelism_configuration | core | json       | Lists the parallelism configuration applied to the pipeline.             |
| pipeline_arn              | core | string     | The Amazon Resource Name (ARN) of the pipeline.                          |
| pipeline_definition       | core | string     | The JSON pipeline definition.                                            |
| pipeline_description      | core | string     | The description of the pipeline.                                         |
| pipeline_display_name     | core | string     | The display name of the pipeline.                                        |
| pipeline_name             | core | string     | The name of the pipeline.                                                |
| pipeline_status           | core | string     | The status of the pipeline execution.                                    |
| role_arn                  | core | string     | The Amazon Resource Name (ARN) that the pipeline uses to execute.        |
| tags                      | core | hstore_csv |
