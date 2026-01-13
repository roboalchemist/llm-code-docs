# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.dynamodb_export.dataset.md

---
title: DynamoDB Export
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DynamoDB Export
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.dynamodb_export.dataset/index.html
---

# DynamoDB Export

DynamoDB Export in AWS provides details about an ongoing or completed export of table data to Amazon S3. It allows you to track the status, progress, and configuration of the export, including information such as the export destination, start and end times, and any errors encountered. This helps monitor and manage data exports for backup, analytics, or migration purposes.

```gdscript3
aws.dynamodb_export
```

## Fields

| Title                            | ID   | Type      | Data Type                                                                                                                                                                                                              | Description |
| -------------------------------- | ---- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string    |
| account_id                       | core | string    |
| billed_size_bytes                | core | int64     | The billable size of the table export.                                                                                                                                                                                 |
| client_token                     | core | string    | The client token that was provided for the export task. A client token makes calls to ExportTableToPointInTimeInput idempotent, meaning that multiple identical calls have the same effect as one single call.         |
| end_time                         | core | timestamp | The time at which the export task completed.                                                                                                                                                                           |
| export_arn                       | core | string    | The Amazon Resource Name (ARN) of the table export.                                                                                                                                                                    |
| export_format                    | core | string    | The format of the exported data. Valid values for ExportFormat are DYNAMODB_JSON or ION.                                                                                                                               |
| export_manifest                  | core | string    | The name of the manifest file for the export task.                                                                                                                                                                     |
| export_status                    | core | string    | Export can be in one of the following states: IN_PROGRESS, COMPLETED, or FAILED.                                                                                                                                       |
| export_time                      | core | timestamp | Point in time from which table data was exported.                                                                                                                                                                      |
| export_type                      | core | string    | The type of export that was performed. Valid values are FULL_EXPORT or INCREMENTAL_EXPORT.                                                                                                                             |
| failure_code                     | core | string    | Status code for the result of the failed export.                                                                                                                                                                       |
| failure_message                  | core | string    | Export failure reason description.                                                                                                                                                                                     |
| incremental_export_specification | core | json      | Optional object containing the parameters specific to an incremental export.                                                                                                                                           |
| item_count                       | core | int64     | The number of items exported.                                                                                                                                                                                          |
| s3_bucket                        | core | string    | The name of the Amazon S3 bucket containing the export.                                                                                                                                                                |
| s3_bucket_owner                  | core | string    | The ID of the Amazon Web Services account that owns the bucket containing the export.                                                                                                                                  |
| s3_prefix                        | core | string    | The Amazon S3 bucket prefix used as the file name and path of the exported snapshot.                                                                                                                                   |
| s3_sse_algorithm                 | core | string    | Type of encryption used on the bucket where export data is stored. Valid values for S3SseAlgorithm are: AES256 - server-side encryption with Amazon S3 managed keys KMS - server-side encryption with KMS managed keys |
| s3_sse_kms_key_id                | core | string    | The ID of the KMS managed key used to encrypt the S3 bucket where export data is stored (if applicable).                                                                                                               |
| start_time                       | core | timestamp | The time at which the export task began.                                                                                                                                                                               |
| table_arn                        | core | string    | The Amazon Resource Name (ARN) of the table that was exported.                                                                                                                                                         |
| table_id                         | core | string    | Unique ID of the table that was exported.                                                                                                                                                                              |
| tags                             | core | hstore    |
