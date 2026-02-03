# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.storagegateway_cache_report.dataset.md

---
title: Storage Gateway Cache Report
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Storage Gateway Cache Report
---

# Storage Gateway Cache Report

Provides details about the cache status of an AWS Storage Gateway. The Cache Report includes information such as the amount of data stored, cache utilization, and performance metrics. It helps monitor how effectively the local cache is being used to optimize data transfers between on-premises environments and AWS cloud storage.

```
aws.storagegateway_cache_report
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                        | Description |
| ------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------ | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| cache_report_arn          | core | string     | The Amazon Resource Name (ARN) of the cache report you want to describe.                         |
| cache_report_status       | core | string     | The status of the specified cache report.                                                        |
| end_time                  | core | timestamp  | The time at which the gateway stopped generating the cache report.                               |
| exclusion_filters         | core | json       | The list of filters and parameters that determine which files are excluded from the report.      |
| file_share_arn            | core | string     | The Amazon Resource Name (ARN) of the file share.                                                |
| inclusion_filters         | core | json       | The list of filters and parameters that determine which files are included in the report.        |
| location_arn              | core | string     | The ARN of the Amazon S3 bucket location where the cache report is saved.                        |
| report_completion_percent | core | int64      | The percentage of the report generation process that has been completed at time of inquiry.      |
| report_name               | core | string     | The file name of the completed cache report object stored in Amazon S3.                          |
| role                      | core | string     | The ARN of the IAM role that an S3 File Gateway assumes when it accesses the underlying storage. |
| start_time                | core | timestamp  | The time at which the gateway started generating the cache report.                               |
| tags                      | core | hstore_csv |
