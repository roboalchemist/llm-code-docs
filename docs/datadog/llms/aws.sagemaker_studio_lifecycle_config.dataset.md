# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_studio_lifecycle_config.dataset.md

---
title: SageMaker Studio Lifecycle Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > SageMaker Studio Lifecycle
  Configuration
---

# SageMaker Studio Lifecycle Configuration

SageMaker Studio Lifecycle Configuration in AWS defines custom scripts that run automatically when a SageMaker Studio app starts or restarts. These scripts allow you to automate environment setup, install packages, configure settings, or integrate with external systems, ensuring consistent and repeatable development environments for data scientists and machine learning engineers.

```
aws.sagemaker_studio_lifecycle_config
```

## Fields

| Title                            | ID   | Type       | Data Type                                                                                                           | Description |
| -------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string     |
| account_id                       | core | string     |
| creation_time                    | core | timestamp  | The creation time of the Amazon SageMaker AI Studio Lifecycle Configuration.                                        |
| last_modified_time               | core | timestamp  | This value is equivalent to CreationTime because Amazon SageMaker AI Studio Lifecycle Configurations are immutable. |
| studio_lifecycle_config_app_type | core | string     | The App type that the Lifecycle Configuration is attached to.                                                       |
| studio_lifecycle_config_arn      | core | string     | The ARN of the Lifecycle Configuration to describe.                                                                 |
| studio_lifecycle_config_content  | core | string     | The content of your Amazon SageMaker AI Studio Lifecycle Configuration script.                                      |
| studio_lifecycle_config_name     | core | string     | The name of the Amazon SageMaker AI Studio Lifecycle Configuration that is described.                               |
| tags                             | core | hstore_csv |
