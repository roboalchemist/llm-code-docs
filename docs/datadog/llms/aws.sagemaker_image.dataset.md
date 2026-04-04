# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_image.dataset.md

---
title: SageMaker Image
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Image
---

# SageMaker Image

An AWS SageMaker Image is a custom container image that provides the runtime environment for machine learning tasks in SageMaker. It defines the software, libraries, and dependencies needed to train or deploy models. These images can be reused across different SageMaker jobs, endpoints, and notebooks, ensuring consistency and flexibility in managing ML workflows.

```
aws.sagemaker_image
```

## Fields

| Title              | ID   | Type       | Data Type                                                                     | Description |
| ------------------ | ---- | ---------- | ----------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| creation_time      | core | timestamp  | When the image was created.                                                   |
| description        | core | string     | The description of the image.                                                 |
| failure_reason     | core | string     | When a create, update, or delete operation fails, the reason for the failure. |
| image_arn          | core | string     | The ARN of the image.                                                         |
| image_name         | core | string     | The name of the image.                                                        |
| image_status       | core | string     | The status of the image.                                                      |
| last_modified_time | core | timestamp  | When the image was last modified.                                             |
| tags               | core | hstore_csv |
