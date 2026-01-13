# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.frauddetector_batch_prediction_job.dataset.md

---
title: Fraud Detector Batch Prediction Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Fraud Detector Batch Prediction Job
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.frauddetector_batch_prediction_job.dataset/index.html
---

# Fraud Detector Batch Prediction Job

This table represents the Fraud Detector Batch Prediction Job resource from Amazon Web Services.

```
aws.frauddetector_batch_prediction_job
```

## Fields

| Title                   | ID   | Type   | Data Type                                                                                   | Description |
| ----------------------- | ---- | ------ | ------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string |
| account_id              | core | string |
| arn                     | core | string | The ARN of batch prediction job.                                                            |
| completion_time         | core | string | Timestamp of when the batch prediction job completed.                                       |
| detector_name           | core | string | The name of the detector.                                                                   |
| detector_version        | core | string | The detector version.                                                                       |
| event_type_name         | core | string | The name of the event type.                                                                 |
| failure_reason          | core | string | The reason a batch prediction job failed.                                                   |
| iam_role_arn            | core | string | The ARN of the IAM role to use for this job request.                                        |
| input_path              | core | string | The Amazon S3 location of your training file.                                               |
| job_id                  | core | string | The job ID for the batch prediction.                                                        |
| last_heartbeat_time     | core | string | Timestamp of most recent heartbeat indicating the batch prediction job was making progress. |
| output_path             | core | string | The Amazon S3 location of your output file.                                                 |
| processed_records_count | core | int64  | The number of records processed by the batch prediction job.                                |
| start_time              | core | string | Timestamp of when the batch prediction job started.                                         |
| status                  | core | string | The batch prediction status.                                                                |
| tags                    | core | hstore |
| total_records_count     | core | int64  | The total number of records in the batch prediction job.                                    |
