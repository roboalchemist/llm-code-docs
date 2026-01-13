# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_model_customization_job.dataset.md

---
title: Bedrock Model Customization Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Model Customization Job
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.bedrock_model_customization_job.dataset/index.html
---

# Bedrock Model Customization Job

Bedrock Model Customization Job in AWS allows you to create and manage fine-tuning jobs for foundation models in Amazon Bedrock. It provides details about the customization process, including job status, configuration, input data, and output location. This resource helps track and manage the lifecycle of model customization, enabling you to adapt foundation models to your specific domain or use case.

```
aws.bedrock_model_customization_job
```

## Fields

| Title                    | ID   | Type      | Data Type                                                                                                                                                                                                      | Description |
| ------------------------ | ---- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string    |
| account_id               | core | string    |
| base_model_arn           | core | string    | Amazon Resource Name (ARN) of the base model.                                                                                                                                                                  |
| client_request_token     | core | string    | The token that you specified in the CreateCustomizationJob request.                                                                                                                                            |
| creation_time            | core | timestamp | Time that the resource was created.                                                                                                                                                                            |
| customization_config     | core | json      | The customization configuration for the model customization job.                                                                                                                                               |
| customization_type       | core | string    | The type of model customization.                                                                                                                                                                               |
| end_time                 | core | timestamp | Time that the resource transitioned to terminal state.                                                                                                                                                         |
| failure_message          | core | string    | Information about why the job failed.                                                                                                                                                                          |
| hyper_parameters         | core | hstore    | The hyperparameter values for the job. For details on the format for different models, see Custom model hyperparameters.                                                                                       |
| job_arn                  | core | string    | The Amazon Resource Name (ARN) of the customization job.                                                                                                                                                       |
| job_name                 | core | string    | The name of the customization job.                                                                                                                                                                             |
| last_modified_time       | core | timestamp | Time that the resource was last modified.                                                                                                                                                                      |
| output_data_config       | core | json      | Output data configuration                                                                                                                                                                                      |
| output_model_arn         | core | string    | The Amazon Resource Name (ARN) of the output model.                                                                                                                                                            |
| output_model_kms_key_arn | core | string    | The custom model is encrypted at rest using this key.                                                                                                                                                          |
| output_model_name        | core | string    | The name of the output model.                                                                                                                                                                                  |
| role_arn                 | core | string    | The Amazon Resource Name (ARN) of the IAM role.                                                                                                                                                                |
| status                   | core | string    | The status of the job. A successful job transitions from in-progress to completed when the output model is ready to use. If the job failed, the failure message contains information about why the job failed. |
| status_details           | core | json      | For a Distillation job, the details about the statuses of the sub-tasks of the customization job.                                                                                                              |
| tags                     | core | hstore    |
| training_data_config     | core | json      | Contains information about the training dataset.                                                                                                                                                               |
| training_metrics         | core | json      | Contains training metrics from the job creation.                                                                                                                                                               |
| validation_data_config   | core | json      | Contains information about the validation dataset.                                                                                                                                                             |
| validation_metrics       | core | json      | The loss metric for each validator that you provided in the createjob request.                                                                                                                                 |
| vpc_config               | core | json      | VPC configuration for the custom model job.                                                                                                                                                                    |
