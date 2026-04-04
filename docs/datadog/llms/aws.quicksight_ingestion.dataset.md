# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.quicksight_ingestion.dataset.md

---
title: QuickSight Ingestion
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > QuickSight Ingestion
---

# QuickSight Ingestion

QuickSight Ingestion in AWS refers to the process of loading data into Amazon QuickSight for analysis and visualization. An ingestion represents a specific data load job that imports data from a source into a dataset within QuickSight. It tracks the status, progress, and results of the data load, enabling users to refresh datasets and keep dashboards up to date with the latest information.

```
aws.quicksight_ingestion
```

## Fields

| Title                     | ID   | Type       | Data Type                                               | Description |
| ------------------------- | ---- | ---------- | ------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| arn                       | core | string     | The Amazon Resource Name (ARN) of the resource.         |
| created_time              | core | timestamp  | The time that this ingestion started.                   |
| error_info                | core | json       | Error information for this ingestion.                   |
| ingestion_id              | core | string     | Ingestion ID.                                           |
| ingestion_size_in_bytes   | core | int64      | The size of the data ingested, in bytes.                |
| ingestion_status          | core | string     | Ingestion status.                                       |
| ingestion_time_in_seconds | core | int64      | The time that this ingestion took, measured in seconds. |
| queue_info                | core | json       | Information about a queued dataset SPICE ingestion.     |
| request_source            | core | string     | Event source for this ingestion.                        |
| request_type              | core | string     | Type of this ingestion.                                 |
| row_info                  | core | json       | Information about rows for a data set SPICE ingestion.  |
| tags                      | core | hstore_csv |
