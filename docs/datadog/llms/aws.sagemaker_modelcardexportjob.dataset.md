# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_modelcardexportjob.dataset.md

---
title: SageMaker Model Card Export Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Model Card Export Job
---

# SageMaker Model Card Export Job

This table represents the SageMaker Model Card Export Job resource from Amazon Web Services.

```gdscript3
aws.sagemaker_modelcardexportjob
```

## Fields

| Title                      | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                               | Description |
| -------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string     |
| account_id                 | core | string     |
| created_at                 | core | timestamp  | The date and time that the model export job was created.                                                                                                                                                                                                                                                                                                                                                                                |
| export_artifacts           | core | json       | The exported model card artifacts.                                                                                                                                                                                                                                                                                                                                                                                                      |
| failure_reason             | core | string     | The failure reason if the model export job fails.                                                                                                                                                                                                                                                                                                                                                                                       |
| last_modified_at           | core | timestamp  | The date and time that the model export job was last modified.                                                                                                                                                                                                                                                                                                                                                                          |
| model_card_export_job_arn  | core | string     | The Amazon Resource Name (ARN) of the model card export job.                                                                                                                                                                                                                                                                                                                                                                            |
| model_card_export_job_name | core | string     | The name of the model card export job to describe.                                                                                                                                                                                                                                                                                                                                                                                      |
| model_card_name            | core | string     | The name or Amazon Resource Name (ARN) of the model card that the model export job exports.                                                                                                                                                                                                                                                                                                                                             |
| model_card_version         | core | int64      | The version of the model card that the model export job exports.                                                                                                                                                                                                                                                                                                                                                                        |
| output_config              | core | json       | The export output details for the model card.                                                                                                                                                                                                                                                                                                                                                                                           |
| status                     | core | string     | The completion status of the model card export job. <ul> <li> <code>InProgress</code>: The model card export job is in progress. </li> <li> <code>Completed</code>: The model card export job is complete. </li> <li> <code>Failed</code>: The model card export job failed. To see the reason for the failure, see the <code>FailureReason</code> field in the response to a <code>DescribeModelCardExportJob</code> call. </li> </ul> |
| tags                       | core | hstore_csv |
