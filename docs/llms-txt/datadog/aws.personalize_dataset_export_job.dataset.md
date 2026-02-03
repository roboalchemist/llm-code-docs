# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.personalize_dataset_export_job.dataset.md

---
title: Personalize Dataset Export Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Personalize Dataset Export Job
---

# Personalize Dataset Export Job

An AWS Personalize Dataset Export Job is a resource that allows you to export data from a dataset in Amazon Personalize to an Amazon S3 bucket. This is useful for analyzing the data outside of Personalize, sharing it with other systems, or archiving it. The export job runs asynchronously and provides details such as status, creation time, and destination location.

```gdscript3
aws.personalize_dataset_export_job
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                            | Description |
| ---------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| creation_date_time     | core | timestamp  | The creation date and time (in Unix time) of the dataset export job.                                                                                                                                                                                                                                 |
| dataset_arn            | core | string     | The Amazon Resource Name (ARN) of the dataset to export.                                                                                                                                                                                                                                             |
| dataset_export_job_arn | core | string     | The Amazon Resource Name (ARN) of the dataset export job.                                                                                                                                                                                                                                            |
| failure_reason         | core | string     | If a dataset export job fails, provides the reason why.                                                                                                                                                                                                                                              |
| ingestion_mode         | core | string     | The data to export, based on how you imported the data. You can choose to export BULK data that you imported using a dataset import job, PUT data that you imported incrementally (using the console, PutEvents, PutUsers and PutItems operations), or ALL for both types. The default value is PUT. |
| job_name               | core | string     | The name of the export job.                                                                                                                                                                                                                                                                          |
| job_output             | core | json       | The path to the Amazon S3 bucket where the job's output is stored. For example: s3://bucket-name/folder-name/                                                                                                                                                                                        |
| last_updated_date_time | core | timestamp  | The date and time (in Unix time) the status of the dataset export job was last updated.                                                                                                                                                                                                              |
| role_arn               | core | string     | The Amazon Resource Name (ARN) of the IAM service role that has permissions to add data to your output Amazon S3 bucket.                                                                                                                                                                             |
| status                 | core | string     | The status of the dataset export job. A dataset export job can be in one of the following states: CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED                                                                                                                                    |
| tags                   | core | hstore_csv |
