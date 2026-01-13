# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotsitewise_dataset.dataset.md

---
title: IoT SiteWise Dataset
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT SiteWise Dataset
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iotsitewise_dataset.dataset/index.html
---

# IoT SiteWise Dataset

An IoT SiteWise Dataset in AWS represents the response details when describing a dataset used for industrial IoT data processing. It provides information about dataset configuration, status, and metadata, enabling users to manage and monitor how data is collected, processed, and made available for analysis within IoT SiteWise.

```
aws.iotsitewise_dataset
```

## Fields

| Title                    | ID   | Type      | Data Type                                                                                                                                                                                                   | Description |
| ------------------------ | ---- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string    |
| account_id               | core | string    |
| dataset_arn              | core | string    | The ARN of the dataset. The format is arn:${Partition}:iotsitewise:${Region}:${Account}:dataset/${DatasetId}.                                                                                               |
| dataset_creation_date    | core | timestamp | The dataset creation date, in Unix epoch time.                                                                                                                                                              |
| dataset_description      | core | string    | A description about the dataset, and its functionality.                                                                                                                                                     |
| dataset_id               | core | string    | The ID of the dataset.                                                                                                                                                                                      |
| dataset_last_update_date | core | timestamp | The date the dataset was last updated, in Unix epoch time.                                                                                                                                                  |
| dataset_name             | core | string    | The name of the dataset.                                                                                                                                                                                    |
| dataset_source           | core | json      | The data source for the dataset.                                                                                                                                                                            |
| dataset_status           | core | json      | The status of the dataset. This contains the state and any error messages. State is CREATING after a successfull call to this API, and any associated error message. The state is ACTIVE when ready to use. |
| dataset_version          | core | string    | The version of the dataset.                                                                                                                                                                                 |
| tags                     | core | hstore    |
