# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_custom_model.dataset.md

---
title: Bedrock Custom Model
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Custom Model
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.bedrock_custom_model.dataset/index.html
---

# Bedrock Custom Model

Bedrock Custom Model in AWS allows you to manage and retrieve details about custom foundation models that you have created or fine-tuned using Amazon Bedrock. It provides information such as model name, version, status, and configuration, enabling you to track and use your tailored models for generative AI applications.

```
aws.bedrock_custom_model
```

## Fields

| Title                  | ID   | Type      | Data Type                                                                                                                                                                                                                                                                            | Description |
| ---------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                   | core | string    |
| account_id             | core | string    |
| base_model_arn         | core | string    | Amazon Resource Name (ARN) of the base model.                                                                                                                                                                                                                                        |
| creation_time          | core | timestamp | Creation time of the model.                                                                                                                                                                                                                                                          |
| customization_config   | core | json      | The customization configuration for the custom model.                                                                                                                                                                                                                                |
| customization_type     | core | string    | The type of model customization.                                                                                                                                                                                                                                                     |
| failure_message        | core | string    | A failure message for any issues that occurred when creating the custom model. This is included for only a failed CreateCustomModel operation.                                                                                                                                       |
| hyper_parameters       | core | hstore    | Hyperparameter values associated with this model. For details on the format for different models, see Custom model hyperparameters.                                                                                                                                                  |
| job_arn                | core | string    | Job Amazon Resource Name (ARN) associated with this model. For models that you create with the CreateCustomModel API operation, this is NULL.                                                                                                                                        |
| job_name               | core | string    | Job name associated with this model.                                                                                                                                                                                                                                                 |
| model_arn              | core | string    | Amazon Resource Name (ARN) associated with this model.                                                                                                                                                                                                                               |
| model_kms_key_arn      | core | string    | The custom model is encrypted at rest using this key.                                                                                                                                                                                                                                |
| model_name             | core | string    | Model name associated with this model.                                                                                                                                                                                                                                               |
| model_status           | core | string    | The current status of the custom model. Possible values include: Creating - The model is being created and validated. Active - The model has been successfully created and is ready for use. Failed - The model creation process failed. Check the failureMessage field for details. |
| output_data_config     | core | json      | Output data configuration associated with this custom model.                                                                                                                                                                                                                         |
| tags                   | core | hstore    |
| training_data_config   | core | json      | Contains information about the training dataset.                                                                                                                                                                                                                                     |
| training_metrics       | core | json      | Contains training metrics from the job creation.                                                                                                                                                                                                                                     |
| validation_data_config | core | json      | Contains information about the validation dataset.                                                                                                                                                                                                                                   |
| validation_metrics     | core | json      | The validation metrics from the job creation.                                                                                                                                                                                                                                        |
