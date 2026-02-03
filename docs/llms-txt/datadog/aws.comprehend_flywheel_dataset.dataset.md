# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.comprehend_flywheel_dataset.dataset.md

---
title: Comprehend Flywheel Dataset
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Comprehend Flywheel Dataset
---

# Comprehend Flywheel Dataset

This table represents the Comprehend Flywheel Dataset resource from Amazon Web Services.

```
aws.comprehend_flywheel_dataset
```

## Fields

| Title               | ID   | Type       | Data Type                                                                                                                                                                      | Description |
| ------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| creation_time       | core | timestamp  | Creation time of the dataset.                                                                                                                                                  |
| dataset_arn         | core | string     | The ARN of the dataset.                                                                                                                                                        |
| dataset_name        | core | string     | The name of the dataset.                                                                                                                                                       |
| dataset_s3_uri      | core | string     | The S3 URI where the dataset is stored.                                                                                                                                        |
| dataset_type        | core | string     | The dataset type (training data or test data).                                                                                                                                 |
| description         | core | string     | Description of the dataset.                                                                                                                                                    |
| end_time            | core | timestamp  | Time when the data from the dataset becomes available in the data lake.                                                                                                        |
| message             | core | string     | A description of the status of the dataset.                                                                                                                                    |
| number_of_documents | core | int64      | The number of documents in the dataset.                                                                                                                                        |
| status              | core | string     | The dataset status. While the system creates the dataset, the status is <code>CREATING</code>. When the dataset is ready to use, the status changes to <code>COMPLETED</code>. |
| tags                | core | hstore_csv |
