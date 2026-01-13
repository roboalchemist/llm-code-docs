# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.frauddetector_batch_import_job.dataset.md

---
title: Fraud Detector Batch Import Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Fraud Detector Batch Import Job
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.frauddetector_batch_import_job.dataset/index.html
---

# Fraud Detector Batch Import Job

This table represents the Fraud Detector Batch Import Job resource from Amazon Web Services.

```
aws.frauddetector_batch_import_job
```

## Fields

| Title                   | ID   | Type   | Data Type                                                  | Description |
| ----------------------- | ---- | ------ | ---------------------------------------------------------- | ----------- |
| _key                    | core | string |
| account_id              | core | string |
| arn                     | core | string | The ARN of the batch import job.                           |
| completion_time         | core | string | Timestamp of when batch import job completed.              |
| event_type_name         | core | string | The name of the event type.                                |
| failed_records_count    | core | int64  | The number of records that failed to import.               |
| failure_reason          | core | string | The reason batch import job failed.                        |
| iam_role_arn            | core | string | The ARN of the IAM role to use for this job request.       |
| input_path              | core | string | The Amazon S3 location of your data file for batch import. |
| job_id                  | core | string | The ID of the batch import job.                            |
| output_path             | core | string | The Amazon S3 location of your output file.                |
| processed_records_count | core | int64  | The number of records processed by batch import job.       |
| start_time              | core | string | Timestamp of when the batch import job started.            |
| status                  | core | string | The status of the batch import job.                        |
| tags                    | core | hstore |
| total_records_count     | core | int64  | The total number of records in the batch import job.       |
