# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_endpoint_config.dataset.md

---
title: SageMaker Endpoint Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Endpoint Configuration
---

# SageMaker Endpoint Configuration

An Amazon SageMaker Endpoint Configuration defines how a SageMaker endpoint will serve machine learning models. It specifies one or more production variants, including the model to use, the instance type, and the number of instances. This configuration allows you to control deployment settings such as traffic distribution, autoscaling, and encryption. It is a prerequisite for creating a SageMaker endpoint, ensuring that models are deployed with the desired compute resources and operational parameters.

```
aws.sagemaker_endpoint_config
```

## Fields

| Title                      | ID   | Type       | Data Type                                                                                                                                                                                                                                                                               | Description |
| -------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string     |
| account_id                 | core | string     |
| async_inference_config     | core | json       | Returns the description of an endpoint configuration created using the CreateEndpointConfig API.                                                                                                                                                                                        |
| creation_time              | core | timestamp  | A timestamp that shows when the endpoint configuration was created.                                                                                                                                                                                                                     |
| data_capture_config        | core | json       | Configuration to control how SageMaker AI captures inference data.                                                                                                                                                                                                                      |
| enable_network_isolation   | core | bool       | Indicates whether all model containers deployed to the endpoint are isolated. If they are, no inbound or outbound network calls can be made to or from the model containers.                                                                                                            |
| endpoint_config_arn        | core | string     | The Amazon Resource Name (ARN) of the endpoint configuration.                                                                                                                                                                                                                           |
| endpoint_config_name       | core | string     | Name of the SageMaker endpoint configuration.                                                                                                                                                                                                                                           |
| execution_role_arn         | core | string     | The Amazon Resource Name (ARN) of the IAM role that you assigned to the endpoint configuration.                                                                                                                                                                                         |
| explainer_config           | core | json       | The configuration parameters for an explainer.                                                                                                                                                                                                                                          |
| kms_key_id                 | core | string     | Amazon Web Services KMS key ID Amazon SageMaker uses to encrypt data when storing it on the ML storage volume attached to the instance.                                                                                                                                                 |
| production_variants        | core | json       | An array of ProductionVariant objects, one for each model that you want to host at this endpoint.                                                                                                                                                                                       |
| shadow_production_variants | core | json       | An array of ProductionVariant objects, one for each model that you want to host at this endpoint in shadow mode with production traffic replicated from the model specified on ProductionVariants.                                                                                      |
| tags                       | core | hstore_csv |
| vpc_config                 | core | json       | Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see Give SageMaker Access to Resources in your Amazon VPC. |
