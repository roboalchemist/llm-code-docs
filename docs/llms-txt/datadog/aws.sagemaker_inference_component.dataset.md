# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_inference_component.dataset.md

---
title: SageMaker Inference Component
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Inference Component
---

# SageMaker Inference Component

SageMaker Inference Component is an AWS resource that provides detailed information about a deployed inference component within Amazon SageMaker. It allows you to describe and monitor the configuration, status, and runtime details of the component, which is used to serve machine learning models in production. This helps manage model endpoints more efficiently by offering visibility into how inference workloads are running.

```
aws.sagemaker_inference_component
```

## Fields

| Title                      | ID   | Type       | Data Type                                                                                       | Description |
| -------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string     |
| account_id                 | core | string     |
| creation_time              | core | timestamp  | The time when the inference component was created.                                              |
| endpoint_arn               | core | string     | The Amazon Resource Name (ARN) of the endpoint that hosts the inference component.              |
| endpoint_name              | core | string     | The name of the endpoint that hosts the inference component.                                    |
| failure_reason             | core | string     | If the inference component status is Failed, the reason for the failure.                        |
| inference_component_arn    | core | string     | The Amazon Resource Name (ARN) of the inference component.                                      |
| inference_component_name   | core | string     | The name of the inference component.                                                            |
| inference_component_status | core | string     | The status of the inference component.                                                          |
| last_deployment_config     | core | json       | The deployment and rollback settings that you assigned to the inference component.              |
| last_modified_time         | core | timestamp  | The time when the inference component was last updated.                                         |
| runtime_config             | core | json       | Details about the runtime settings for the model that is deployed with the inference component. |
| specification              | core | json       | Details about the resources that are deployed with this inference component.                    |
| tags                       | core | hstore_csv |
| variant_name               | core | string     | The name of the production variant that hosts the inference component.                          |
