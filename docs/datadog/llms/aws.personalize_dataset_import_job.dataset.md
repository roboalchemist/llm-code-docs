# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.personalize_dataset_import_job.dataset.md

---
title: Personalize Dataset Import Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Personalize Dataset Import Job
---

# Personalize Dataset Import Job

An Amazon Personalize Dataset Import Job is a resource that loads data from Amazon S3 into a Personalize dataset. It transforms and validates the data according to the dataset schema, making it ready for training recommendation models. This job is essential for preparing user interaction, item, or user metadata so that Personalize can generate accurate and personalized recommendations.

```
aws.personalize_dataset_import_job
```

## Fields

| Title                             | ID   | Type       | Data Type                                                                                                                                                         | Description |
| --------------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                              | core | string     |
| account_id                        | core | string     |
| creation_date_time                | core | timestamp  | The creation date and time (in Unix time) of the dataset import job.                                                                                              |
| data_source                       | core | json       | The Amazon S3 bucket that contains the training data to import.                                                                                                   |
| dataset_arn                       | core | string     | The Amazon Resource Name (ARN) of the dataset that receives the imported data.                                                                                    |
| dataset_import_job_arn            | core | string     | The ARN of the dataset import job.                                                                                                                                |
| failure_reason                    | core | string     | If a dataset import job fails, provides the reason why.                                                                                                           |
| import_mode                       | core | string     | The import mode used by the dataset import job to import new records.                                                                                             |
| job_name                          | core | string     | The name of the import job.                                                                                                                                       |
| last_updated_date_time            | core | timestamp  | The date and time (in Unix time) the dataset was last updated.                                                                                                    |
| publish_attribution_metrics_to_s3 | core | bool       | Whether the job publishes metrics to Amazon S3 for a metric attribution.                                                                                          |
| role_arn                          | core | string     | The ARN of the IAM role that has permissions to read from the Amazon S3 data source.                                                                              |
| status                            | core | string     | The status of the dataset import job. A dataset import job can be in one of the following states: CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED |
| tags                              | core | hstore_csv |
