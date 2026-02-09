# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_context.dataset.md

---
title: SageMaker Context
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Context
---

# SageMaker Context

SageMaker Context in AWS represents metadata that helps track and organize machine learning workflows. It captures information about activities, datasets, models, or other entities involved in an ML project, enabling better lineage tracking and experiment management. This resource is useful for understanding relationships between different components in SageMaker and for maintaining reproducibility in ML pipelines.

```
aws.sagemaker_context
```

## Fields

| Title              | ID   | Type       | Data Type                                                                | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------ | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| context_arn        | core | string     | The Amazon Resource Name (ARN) of the context.                           |
| context_name       | core | string     | The name of the context.                                                 |
| context_type       | core | string     | The type of the context.                                                 |
| created_by         | core | json       | Information about the user who created or modified a SageMaker resource. |
| creation_time      | core | timestamp  | When the context was created.                                            |
| description        | core | string     | The description of the context.                                          |
| last_modified_by   | core | json       | Information about the user who created or modified a SageMaker resource. |
| last_modified_time | core | timestamp  | When the context was last modified.                                      |
| lineage_group_arn  | core | string     | The Amazon Resource Name (ARN) of the lineage group.                     |
| properties         | core | hstore     | A list of the context's properties.                                      |
| tags               | core | hstore_csv |
