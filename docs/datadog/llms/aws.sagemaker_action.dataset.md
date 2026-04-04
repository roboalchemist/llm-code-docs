# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_action.dataset.md

---
title: SageMaker Action
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Action
---

# SageMaker Action

SageMaker Action in AWS represents a record of a specific step or event within a SageMaker workflow, such as model training, data processing, or deployment. It provides metadata and details about the action, including its type, status, properties, and associations with other SageMaker entities. This helps track and manage machine learning workflows, ensuring better visibility and reproducibility of ML processes.

```
aws.sagemaker_action
```

## Fields

| Title               | ID   | Type       | Data Type                                                                | Description |
| ------------------- | ---- | ---------- | ------------------------------------------------------------------------ | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| action_arn          | core | string     | The Amazon Resource Name (ARN) of the action.                            |
| action_name         | core | string     | The name of the action.                                                  |
| action_type         | core | string     | The type of the action.                                                  |
| created_by          | core | json       | Information about the user who created or modified a SageMaker resource. |
| creation_time       | core | timestamp  | When the action was created.                                             |
| description         | core | string     | The description of the action.                                           |
| last_modified_by    | core | json       | Information about the user who created or modified a SageMaker resource. |
| last_modified_time  | core | timestamp  | When the action was last modified.                                       |
| lineage_group_arn   | core | string     | The Amazon Resource Name (ARN) of the lineage group.                     |
| metadata_properties | core | json       | Metadata properties of the tracking entity, trial, or trial component.   |
| properties          | core | hstore     | A list of the action's properties.                                       |
| status              | core | string     | The status of the action.                                                |
| tags                | core | hstore_csv |
