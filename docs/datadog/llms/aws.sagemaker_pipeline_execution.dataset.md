# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_pipeline_execution.dataset.md

---
title: SageMaker Pipeline Execution
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Pipeline Execution
---

# SageMaker Pipeline Execution

SageMaker Pipeline Execution in AWS represents the details of a specific run of a SageMaker pipeline. It provides information about the execution status, start and end times, steps involved, and metadata such as failure reasons or execution display names. This resource helps track, monitor, and manage machine learning workflow executions, making it easier to debug issues, audit processes, and ensure reproducibility of ML pipelines.

```
aws.sagemaker_pipeline_execution
```

## Fields

| Title                           | ID   | Type       | Data Type                                                                | Description |
| ------------------------------- | ---- | ---------- | ------------------------------------------------------------------------ | ----------- |
| _key                            | core | string     |
| account_id                      | core | string     |
| created_by                      | core | json       | Information about the user who created or modified a SageMaker resource. |
| creation_time                   | core | timestamp  | The time when the pipeline execution was created.                        |
| failure_reason                  | core | string     | If the execution failed, a message describing why.                       |
| last_modified_by                | core | json       | Information about the user who created or modified a SageMaker resource. |
| last_modified_time              | core | timestamp  | The time when the pipeline execution was modified last.                  |
| parallelism_configuration       | core | json       | The parallelism configuration applied to the pipeline.                   |
| pipeline_arn                    | core | string     | The Amazon Resource Name (ARN) of the pipeline.                          |
| pipeline_execution_arn          | core | string     | The Amazon Resource Name (ARN) of the pipeline execution.                |
| pipeline_execution_description  | core | string     | The description of the pipeline execution.                               |
| pipeline_execution_display_name | core | string     | The display name of the pipeline execution.                              |
| pipeline_execution_status       | core | string     | The status of the pipeline execution.                                    |
| pipeline_experiment_config      | core | json       | Specifies the names of the experiment and trial created by a pipeline.   |
| selective_execution_config      | core | json       | The selective execution configuration applied to the pipeline run.       |
| tags                            | core | hstore_csv |
