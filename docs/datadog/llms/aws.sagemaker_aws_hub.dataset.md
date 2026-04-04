# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_aws_hub.dataset.md

---
title: SageMaker Hub
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Hub
---

# SageMaker Hub

SageMaker Hub in AWS is a centralized repository for managing and sharing machine learning resources such as models, notebooks, and solutions. It allows teams to discover, organize, and reuse ML assets across projects, improving collaboration and accelerating development.

```
aws.sagemaker_aws_hub
```

## Fields

| Title               | ID   | Type          | Data Type                                           | Description |
| ------------------- | ---- | ------------- | --------------------------------------------------- | ----------- |
| _key                | core | string        |
| account_id          | core | string        |
| creation_time       | core | timestamp     | The date and time that the hub was created.         |
| failure_reason      | core | string        | The failure reason if importing hub content failed. |
| hub_arn             | core | string        | The Amazon Resource Name (ARN) of the hub.          |
| hub_description     | core | string        | A description of the hub.                           |
| hub_display_name    | core | string        | The display name of the hub.                        |
| hub_name            | core | string        | The name of the hub.                                |
| hub_search_keywords | core | array<string> | The searchable keywords for the hub.                |
| hub_status          | core | string        | The status of the hub.                              |
| last_modified_time  | core | timestamp     | The date and time that the hub was last modified.   |
| s3_storage_config   | core | json          | The Amazon S3 storage configuration for the hub.    |
| tags                | core | hstore_csv    |
