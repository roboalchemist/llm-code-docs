# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_model_package_group.dataset.md

---
title: SageMaker Model Package Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Model Package Group
---

# SageMaker Model Package Group

An Amazon SageMaker Model Package Group is a container for organizing and managing multiple versions of machine learning model packages. It allows you to track, compare, and govern different iterations of a model throughout its lifecycle. This helps streamline model versioning, approval workflows, and deployment processes within SageMaker.

```
aws.sagemaker_model_package_group
```

## Fields

| Title                           | ID   | Type       | Data Type                                                                | Description |
| ------------------------------- | ---- | ---------- | ------------------------------------------------------------------------ | ----------- |
| _key                            | core | string     |
| account_id                      | core | string     |
| created_by                      | core | json       | Information about the user who created or modified a SageMaker resource. |
| creation_time                   | core | timestamp  | The time that the model group was created.                               |
| model_package_group_arn         | core | string     | The Amazon Resource Name (ARN) of the model group.                       |
| model_package_group_description | core | string     | A description of the model group.                                        |
| model_package_group_name        | core | string     | The name of the model group.                                             |
| model_package_group_status      | core | string     | The status of the model group.                                           |
| tags                            | core | hstore_csv |
