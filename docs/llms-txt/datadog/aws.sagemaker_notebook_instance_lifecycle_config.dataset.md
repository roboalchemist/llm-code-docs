# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_notebook_instance_lifecycle_config.dataset.md

---
title: SageMaker Notebook Instance Lifecycle Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > SageMaker Notebook Instance
  Lifecycle Configuration
---

# SageMaker Notebook Instance Lifecycle Configuration

An Amazon SageMaker Notebook Instance Lifecycle Configuration lets you define shell scripts that run when a notebook instance is created or started. These scripts can automate setup tasks such as installing packages, configuring environments, or connecting to data sources, ensuring that every notebook instance is consistently prepared for use.

```
aws.sagemaker_notebook_instance_lifecycle_config
```

## Fields

| Title                                   | ID   | Type       | Data Type                                                                                                             | Description |
| --------------------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                    | core | string     |
| account_id                              | core | string     |
| creation_time                           | core | timestamp  | A timestamp that tells when the lifecycle configuration was created.                                                  |
| last_modified_time                      | core | timestamp  | A timestamp that tells when the lifecycle configuration was last modified.                                            |
| notebook_instance_lifecycle_config_arn  | core | string     | The Amazon Resource Name (ARN) of the lifecycle configuration.                                                        |
| notebook_instance_lifecycle_config_name | core | string     | The name of the lifecycle configuration.                                                                              |
| on_create                               | core | json       | The shell script that runs only once, when you create a notebook instance.                                            |
| on_start                                | core | json       | The shell script that runs every time you start a notebook instance, including when you create the notebook instance. |
| tags                                    | core | hstore_csv |
