# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iam_access_key_metadata.dataset.md

---
title: IAM Access Key Metadata
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IAM Access Key Metadata
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iam_access_key_metadata.dataset/index.html
---

# IAM Access Key Metadata

This table represents the IAM Access Key Metadata resource from Amazon Web Services.

```
aws.iam_access_key_metadata
```

## Fields

| Title                   | ID   | Type      | Data Type                                                                                                                           | Description |
| ----------------------- | ---- | --------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string    |
| access_key_id           | core | string    | The ID for this access key.                                                                                                         |
| access_key_metadata_arn | core | string    |
| account_id              | core | string    |
| create_date             | core | timestamp | The date when the access key was created.                                                                                           |
| status                  | core | string    | The status of the access key. <code>Active</code> means that the key is valid for API calls; <code>Inactive</code> means it is not. |
| tags                    | core | hstore    |
| user_name               | core | string    | The name of the IAM user that the key is associated with.                                                                           |
