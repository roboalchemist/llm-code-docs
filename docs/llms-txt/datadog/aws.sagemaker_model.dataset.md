# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_model.dataset.md

---
title: SageMaker Model
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Model
---

# SageMaker Model

An AWS SageMaker Model is a containerized machine learning model that defines how inference should be run in SageMaker. It specifies the location of model artifacts in Amazon S3, the Docker image containing inference code, and optional environment variables. Once created, the model can be deployed to an endpoint for real-time predictions or used in batch transform jobs for offline inference.

```
aws.sagemaker_model
```

## Fields

| Title                      | ID   | Type       | Data Type                                                                                                                                                     | Description |
| -------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string     |
| account_id                 | core | string     |
| containers                 | core | json       | The containers in the inference pipeline.                                                                                                                     |
| creation_time              | core | timestamp  | A timestamp that shows when the model was created.                                                                                                            |
| deployment_recommendation  | core | json       | A set of recommended deployment configurations for the model.                                                                                                 |
| enable_network_isolation   | core | bool       | If True, no inbound or outbound network calls can be made to or from the model container.                                                                     |
| execution_role_arn         | core | string     | The Amazon Resource Name (ARN) of the IAM role that you specified for the model.                                                                              |
| inference_execution_config | core | json       | Specifies details of how containers in a multi-container endpoint are called.                                                                                 |
| model_arn                  | core | string     | The Amazon Resource Name (ARN) of the model.                                                                                                                  |
| model_name                 | core | string     | Name of the SageMaker model.                                                                                                                                  |
| primary_container          | core | json       | The location of the primary inference code, associated artifacts, and custom environment map that the inference code uses when it is deployed in production.  |
| tags                       | core | hstore_csv |
| vpc_config                 | core | json       | A VpcConfig object that specifies the VPC that this model has access to. For more information, see Protect Endpoints by Using an Amazon Virtual Private Cloud |
