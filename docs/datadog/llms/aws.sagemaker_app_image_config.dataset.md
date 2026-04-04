# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_app_image_config.dataset.md

---
title: SageMaker App Image Config
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker App Image Config
---

# SageMaker App Image Config

SageMaker App Image Config is an AWS resource that defines configuration settings for custom container images used in SageMaker Studio apps. It allows you to specify details such as kernel specifications, file system settings, and environment variables, ensuring consistent runtime environments for data science and machine learning workflows.

```
aws.sagemaker_app_image_config
```

## Fields

| Title                        | ID   | Type       | Data Type                                  | Description |
| ---------------------------- | ---- | ---------- | ------------------------------------------ | ----------- |
| _key                         | core | string     |
| account_id                   | core | string     |
| app_image_config_arn         | core | string     | The ARN of the AppImageConfig.             |
| app_image_config_name        | core | string     | The name of the AppImageConfig.            |
| code_editor_app_image_config | core | json       | The configuration of the Code Editor app.  |
| creation_time                | core | timestamp  | When the AppImageConfig was created.       |
| jupyter_lab_app_image_config | core | json       | The configuration of the JupyterLab app.   |
| kernel_gateway_image_config  | core | json       | The configuration of a KernelGateway app.  |
| last_modified_time           | core | timestamp  | When the AppImageConfig was last modified. |
| tags                         | core | hstore_csv |
