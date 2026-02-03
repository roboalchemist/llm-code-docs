# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.frauddetector_external_model.dataset.md

---
title: Fraud Detector External Model
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Fraud Detector External Model
---

# Fraud Detector External Model

Fraud Detector External Model in AWS allows you to integrate machine learning models hosted outside of Amazon Fraud Detector into your fraud detection workflows. By registering an external model, you can use it alongside native Fraud Detector models and rules to evaluate events for potential fraudulent activity. This enables flexibility to leverage custom or third-party models while still benefiting from Fraud Detector's orchestration and decision-making capabilities.

```
aws.frauddetector_external_model
```

## Fields

| Title                          | ID   | Type       | Data Type                                                        | Description |
| ------------------------------ | ---- | ---------- | ---------------------------------------------------------------- | ----------- |
| _key                           | core | string     |
| account_id                     | core | string     |
| arn                            | core | string     | The model ARN.                                                   |
| created_time                   | core | string     | Timestamp of when the model was last created.                    |
| input_configuration            | core | json       | The input configuration.                                         |
| invoke_model_endpoint_role_arn | core | string     | The role used to invoke the model.                               |
| last_updated_time              | core | string     | Timestamp of when the model was last updated.                    |
| model_endpoint                 | core | string     | The Amazon SageMaker model endpoints.                            |
| model_endpoint_status          | core | string     | The Amazon Fraud Detector status for the external model endpoint |
| model_source                   | core | string     | The source of the model.                                         |
| output_configuration           | core | json       | The output configuration.                                        |
| tags                           | core | hstore_csv |
