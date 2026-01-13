# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.comprehend_dataset.dataset.md

---
title: Comprehend Dataset Properties
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Comprehend Dataset Properties
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.comprehend_dataset.dataset/index.html
---

# Comprehend Dataset Properties

Comprehend Dataset Properties in AWS represent the metadata and configuration details of a dataset used with Amazon Comprehend. It includes information such as dataset name, type, status, creation time, and associated input or output data locations. This resource helps track and manage datasets used for training or evaluating custom natural language processing models within Comprehend.

```
aws.comprehend_dataset
```

## Fields

| Title               | ID   | Type      | Data Type                                                                                                                                            | Description |
| ------------------- | ---- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string    |
| account_id          | core | string    |
| creation_time       | core | timestamp | Creation time of the dataset.                                                                                                                        |
| dataset_arn         | core | string    | The ARN of the dataset.                                                                                                                              |
| dataset_name        | core | string    | The name of the dataset.                                                                                                                             |
| dataset_s3_uri      | core | string    | The S3 URI where the dataset is stored.                                                                                                              |
| dataset_type        | core | string    | The dataset type (training data or test data).                                                                                                       |
| description         | core | string    | Description of the dataset.                                                                                                                          |
| end_time            | core | timestamp | Time when the data from the dataset becomes available in the data lake.                                                                              |
| message             | core | string    | A description of the status of the dataset.                                                                                                          |
| number_of_documents | core | int64     | The number of documents in the dataset.                                                                                                              |
| status              | core | string    | The dataset status. While the system creates the dataset, the status is CREATING. When the dataset is ready to use, the status changes to COMPLETED. |
| tags                | core | hstore    |
