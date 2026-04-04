# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.personalize_data_deletion_job.dataset.md

---
title: Personalize Data Deletion Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Personalize Data Deletion Job
---

# Personalize Data Deletion Job

Personalize Data Deletion Job in AWS is a resource that represents the process of removing datasets or records from Amazon Personalize. It provides details about the status, progress, and outcome of a deletion request, ensuring compliance with data management and privacy requirements. This job helps manage lifecycle operations by securely deleting user or item data that is no longer needed.

```
aws.personalize_data_deletion_job
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                      | Description |
| ---------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| creation_date_time     | core | timestamp  | The creation date and time (in Unix time) of the data deletion job.                                                                            |
| data_deletion_job_arn  | core | string     | The Amazon Resource Name (ARN) of the data deletion job.                                                                                       |
| data_source            | core | json       | Describes the data source that contains the data to upload to a dataset, or the list of records to delete from Amazon Personalize.             |
| dataset_group_arn      | core | string     | The Amazon Resource Name (ARN) of the dataset group the job deletes records from.                                                              |
| failure_reason         | core | string     | If a data deletion job fails, provides the reason why.                                                                                         |
| job_name               | core | string     | The name of the data deletion job.                                                                                                             |
| last_updated_date_time | core | timestamp  | The date and time (in Unix time) the data deletion job was last updated.                                                                       |
| num_deleted            | core | int64      | The number of records deleted by a COMPLETED job.                                                                                              |
| role_arn               | core | string     | The Amazon Resource Name (ARN) of the IAM role that has permissions to read from the Amazon S3 data source.                                    |
| status                 | core | string     | The status of the data deletion job. A data deletion job can have one of the following statuses: PENDING > IN_PROGRESS > COMPLETED -or- FAILED |
| tags                   | core | hstore_csv |
