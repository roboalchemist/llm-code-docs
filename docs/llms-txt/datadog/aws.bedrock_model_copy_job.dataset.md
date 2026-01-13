# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_model_copy_job.dataset.md

---
title: Bedrock Model Copy Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Model Copy Job
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.bedrock_model_copy_job.dataset/index.html
---

# Bedrock Model Copy Job

Bedrock Model Copy Job in AWS allows you to create and manage jobs that copy foundation models within Amazon Bedrock. It provides details about the status, progress, and configuration of a model copy operation, enabling you to duplicate models for use in different accounts or regions while maintaining control over access and usage.

```
aws.bedrock_model_copy_job
```

## Fields

| Title                    | ID   | Type      | Data Type                                                                         | Description |
| ------------------------ | ---- | --------- | --------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string    |
| account_id               | core | string    |
| creation_time            | core | timestamp | The time at which the model copy job was created.                                 |
| failure_message          | core | string    | An error message for why the model copy job failed.                               |
| job_arn                  | core | string    | The Amazon Resource Name (ARN) of the model copy job.                             |
| source_account_id        | core | string    | The unique identifier of the account that the model being copied originated from. |
| source_model_arn         | core | string    | The Amazon Resource Name (ARN) of the original model being copied.                |
| source_model_name        | core | string    | The name of the original model being copied.                                      |
| status                   | core | string    | The status of the model copy job.                                                 |
| tags                     | core | hstore    |
| target_model_arn         | core | string    | The Amazon Resource Name (ARN) of the copied model.                               |
| target_model_kms_key_arn | core | string    | The Amazon Resource Name (ARN) of the KMS key encrypting the copied model.        |
| target_model_name        | core | string    | The name of the copied model.                                                     |
| target_model_tags        | core | json      | The tags associated with the copied model.                                        |
