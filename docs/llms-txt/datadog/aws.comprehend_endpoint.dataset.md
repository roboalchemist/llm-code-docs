# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.comprehend_endpoint.dataset.md

---
title: Comprehend Endpoint Properties
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Comprehend Endpoint Properties
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.comprehend_endpoint.dataset/index.html
---

# Comprehend Endpoint Properties

Comprehend Endpoint Properties in AWS describe the configuration and status details of a custom Comprehend real-time inference endpoint. It includes information such as the endpoint name, model used, current status, creation time, and resource settings. This helps users manage and monitor deployed Comprehend models for tasks like sentiment analysis, entity recognition, or custom classification in real-time applications.

```
aws.comprehend_endpoint
```

## Fields

| Title                        | ID   | Type      | Data Type                                                                                                                                                                                              | Description |
| ---------------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                         | core | string    |
| account_id                   | core | string    |
| creation_time                | core | timestamp | The creation date and time of the endpoint.                                                                                                                                                            |
| current_inference_units      | core | int64     | The number of inference units currently used by the model using this endpoint.                                                                                                                         |
| data_access_role_arn         | core | string    | The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to trained custom models encrypted with a customer managed key (ModelKmsKeyId).                               |
| desired_data_access_role_arn | core | string    | Data access role ARN to use in case the new model is encrypted with a customer KMS key.                                                                                                                |
| desired_inference_units      | core | int64     | The desired number of inference units to be used by the model using this endpoint. Each inference unit represents of a throughput of 100 characters per second.                                        |
| desired_model_arn            | core | string    | ARN of the new model to use for updating an existing endpoint. This ARN is going to be different from the model ARN when the update is in progress                                                     |
| endpoint_arn                 | core | string    | The Amazon Resource Number (ARN) of the endpoint.                                                                                                                                                      |
| flywheel_arn                 | core | string    | The Amazon Resource Number (ARN) of the flywheel                                                                                                                                                       |
| last_modified_time           | core | timestamp | The date and time that the endpoint was last modified.                                                                                                                                                 |
| message                      | core | string    | Specifies a reason for failure in cases of Failed status.                                                                                                                                              |
| model_arn                    | core | string    | The Amazon Resource Number (ARN) of the model to which the endpoint is attached.                                                                                                                       |
| status                       | core | string    | Specifies the status of the endpoint. Because the endpoint updates and creation are asynchronous, so customers will need to wait for the endpoint to be Ready status before making inference requests. |
| tags                         | core | hstore    |
