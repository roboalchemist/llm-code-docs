# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_artifact.dataset.md

---
title: SageMaker Artifact
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Artifact
---

# SageMaker Artifact

SageMaker Artifact in AWS represents metadata and lineage information about machine learning artifacts, such as datasets, models, or code, that are tracked within SageMaker. It helps users manage, organize, and trace the origin and usage of these artifacts across experiments and workflows, supporting reproducibility and governance in ML projects.

```
aws.sagemaker_artifact
```

## Fields

| Title               | ID   | Type       | Data Type                                                                | Description |
| ------------------- | ---- | ---------- | ------------------------------------------------------------------------ | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| artifact_arn        | core | string     | The Amazon Resource Name (ARN) of the artifact.                          |
| artifact_name       | core | string     | The name of the artifact.                                                |
| artifact_type       | core | string     | The type of the artifact.                                                |
| created_by          | core | json       | Information about the user who created or modified a SageMaker resource. |
| creation_time       | core | timestamp  | When the artifact was created.                                           |
| last_modified_by    | core | json       | Information about the user who created or modified a SageMaker resource. |
| last_modified_time  | core | timestamp  | When the artifact was last modified.                                     |
| lineage_group_arn   | core | string     | The Amazon Resource Name (ARN) of the lineage group.                     |
| metadata_properties | core | json       | Metadata properties of the tracking entity, trial, or trial component.   |
| properties          | core | hstore     | A list of the artifact's properties.                                     |
| tags                | core | hstore_csv |
