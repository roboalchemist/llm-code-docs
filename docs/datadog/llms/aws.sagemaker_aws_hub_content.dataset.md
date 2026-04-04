# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_aws_hub_content.dataset.md

---
title: SageMaker Hub Content
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Hub Content
---

# SageMaker Hub Content

SageMaker Hub Content in AWS represents information about machine learning resources shared through SageMaker Hub. It provides details about reusable ML assets such as models, notebooks, and solutions that can be discovered, described, and consumed by users. This resource helps teams collaborate and accelerate development by making curated ML content easily accessible within SageMaker.

```
aws.sagemaker_aws_hub_content
```

## Fields

| Title                             | ID   | Type          | Data Type                                                                                                                         | Description |
| --------------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                              | core | string        |
| account_id                        | core | string        |
| creation_time                     | core | timestamp     | The date and time that hub content was created.                                                                                   |
| document_schema_version           | core | string        | The document schema version for the hub content.                                                                                  |
| failure_reason                    | core | string        | The failure reason if importing hub content failed.                                                                               |
| hub_arn                           | core | string        | The Amazon Resource Name (ARN) of the hub that contains the content.                                                              |
| hub_content_arn                   | core | string        | The Amazon Resource Name (ARN) of the hub content.                                                                                |
| hub_content_dependencies          | core | json          | The location of any dependencies that the hub content has, such as scripts, model artifacts, datasets, or notebooks.              |
| hub_content_description           | core | string        | A description of the hub content.                                                                                                 |
| hub_content_display_name          | core | string        | The display name of the hub content.                                                                                              |
| hub_content_document              | core | string        | The hub content document that describes information about the hub content such as type, associated containers, scripts, and more. |
| hub_content_markdown              | core | string        | A string that provides a description of the hub content. This string can include links, tables, and standard markdown formating.  |
| hub_content_name                  | core | string        | The name of the hub content.                                                                                                      |
| hub_content_search_keywords       | core | array<string> | The searchable keywords for the hub content.                                                                                      |
| hub_content_status                | core | string        | The status of the hub content.                                                                                                    |
| hub_content_type                  | core | string        | The type of hub content.                                                                                                          |
| hub_content_version               | core | string        | The version of the hub content.                                                                                                   |
| hub_name                          | core | string        | The name of the hub that contains the content.                                                                                    |
| last_modified_time                | core | timestamp     | The last modified time of the hub content.                                                                                        |
| reference_min_version             | core | string        | The minimum version of the hub content.                                                                                           |
| sage_maker_public_hub_content_arn | core | string        | The ARN of the public hub content.                                                                                                |
| support_status                    | core | string        | The support status of the hub content.                                                                                            |
| tags                              | core | hstore_csv    |
