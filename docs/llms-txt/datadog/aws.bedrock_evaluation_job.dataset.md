# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_evaluation_job.dataset.md

---
title: Bedrock Evaluation Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Evaluation Job
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.bedrock_evaluation_job.dataset/index.html
---

# Bedrock Evaluation Job

An AWS Bedrock Evaluation Job is a managed resource that allows you to assess and compare the performance of foundation models on specific tasks. It runs evaluations using your chosen datasets and metrics, producing results that help you understand model quality, accuracy, and suitability for your use case.

```
aws.bedrock_evaluation_job
```

## Fields

| Title                      | ID   | Type          | Data Type                                                                                                                          | Description |
| -------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string        |
| account_id                 | core | string        |
| application_type           | core | string        | Specifies whether the evaluation job is for evaluating a model or evaluating a knowledge base (retrieval and response generation). |
| creation_time              | core | timestamp     | The time the evaluation job was created.                                                                                           |
| customer_encryption_key_id | core | string        | The Amazon Resource Name (ARN) of the customer managed encryption key specified when the evaluation job was created.               |
| evaluation_config          | core | json          | Contains the configuration details of either an automated or human-based evaluation job.                                           |
| failure_messages           | core | array<string> | A list of strings that specify why the evaluation job failed to create.                                                            |
| inference_config           | core | json          | Contains the configuration details of the inference model used for the evaluation job.                                             |
| job_arn                    | core | string        | The Amazon Resource Name (ARN) of the evaluation job.                                                                              |
| job_description            | core | string        | The description of the evaluation job.                                                                                             |
| job_name                   | core | string        | The name for the evaluation job.                                                                                                   |
| job_type                   | core | string        | Specifies whether the evaluation job is automated or human-based.                                                                  |
| last_modified_time         | core | timestamp     | The time the evaluation job was last modified.                                                                                     |
| output_data_config         | core | json          | Contains the configuration details of the Amazon S3 bucket for storing the results of the evaluation job.                          |
| role_arn                   | core | string        | The Amazon Resource Name (ARN) of the IAM service role used in the evaluation job.                                                 |
| status                     | core | string        | The current status of the evaluation job.                                                                                          |
| tags                       | core | hstore        |
