# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.personalize_dataset.dataset.md

---
title: Personalize Dataset
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Personalize Dataset
---

# Personalize Dataset

An AWS Personalize Dataset is a container that stores data used to train and deploy personalized recommendation models. It is created within a dataset group and is associated with a specific schema that defines the structure of the data, such as user interactions, item metadata, or user metadata. This dataset is essential for building recommendation solutions, as it provides the foundation for training models that generate personalized experiences.

```
aws.personalize_dataset
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                                                        | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| creation_date_time     | core | timestamp  | The creation date and time (in Unix time) of the dataset.                                                                                                                                                                                        |
| dataset_arn            | core | string     | The Amazon Resource Name (ARN) of the dataset that you want metadata for.                                                                                                                                                                        |
| dataset_group_arn      | core | string     | The Amazon Resource Name (ARN) of the dataset group.                                                                                                                                                                                             |
| dataset_type           | core | string     | One of the following values: Interactions Items Users Actions Action_Interactions                                                                                                                                                                |
| last_updated_date_time | core | timestamp  | A time stamp that shows when the dataset was updated.                                                                                                                                                                                            |
| latest_dataset_update  | core | json       | Describes the latest update to the dataset.                                                                                                                                                                                                      |
| name                   | core | string     | The name of the dataset.                                                                                                                                                                                                                         |
| schema_arn             | core | string     | The ARN of the associated schema.                                                                                                                                                                                                                |
| status                 | core | string     | The status of the dataset. A dataset can be in one of the following states: CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED DELETE PENDING > DELETE IN_PROGRESS                                                                  |
| tags                   | core | hstore_csv |
| tracking_id            | core | string     | The ID of the event tracker for an Action interactions dataset. You specify the tracker's ID in the PutActionInteractions API operation. Amazon Personalize uses it to direct new data to the Action interactions dataset in your dataset group. |
