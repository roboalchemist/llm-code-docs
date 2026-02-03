# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.timestream_scheduled_query.dataset.md

---
title: Timestream Scheduled Query
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Timestream Scheduled Query
---

# Timestream Scheduled Query

This table represents the Timestream Scheduled Query resource from Amazon Web Services.

```
aws.timestream_scheduled_query
```

## Fields

| Title                      | ID   | Type       | Data Type                                                              | Description |
| -------------------------- | ---- | ---------- | ---------------------------------------------------------------------- | ----------- |
| _key                       | core | string     |
| account_id                 | core | string     |
| arn                        | core | string     | The Amazon Resource Name.                                              |
| creation_time              | core | timestamp  | The creation time of the scheduled query.                              |
| error_report_configuration | core | json       | Configuration for scheduled query error reporting.                     |
| last_run_status            | core | string     | Status of the last scheduled query run.                                |
| name                       | core | string     | The name of the scheduled query.                                       |
| next_invocation_time       | core | timestamp  | The next time the scheduled query is to be run.                        |
| previous_invocation_time   | core | timestamp  | The last time the scheduled query was run.                             |
| state                      | core | string     | State of scheduled query.                                              |
| tags                       | core | hstore_csv |
| target_destination         | core | json       | Target data source where final scheduled query result will be written. |
