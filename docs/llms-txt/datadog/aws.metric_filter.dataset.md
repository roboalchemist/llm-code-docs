# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.metric_filter.dataset.md

---
title: Metric Filter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Metric Filter
---

# Metric Filter

This table represents the Metric Filter resource from Amazon Web Services.

```
aws.metric_filter
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                               | Description |
| ------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| apply_on_transformed_logs | core | bool       | This parameter is valid only for log groups that have an active log transformer. For more information about log transformers, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html">PutTransformer</a>. If this value is <code>true</code>, the metric filter is applied on the transformed version of the log events instead of the original ingested log events. |
| creation_time             | core | int64      | The creation time of the metric filter, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.                                                                                                                                                                                                                                                                                            |
| filter_name               | core | string     | The name of the metric filter.                                                                                                                                                                                                                                                                                                                                                                                          |
| filter_pattern            | core | string     |
| log_group_name            | core | string     | The name of the log group.                                                                                                                                                                                                                                                                                                                                                                                              |
| metric_filter_arn         | core | string     |
| metric_transformations    | core | json       | The metric transformations.                                                                                                                                                                                                                                                                                                                                                                                             |
| tags                      | core | hstore_csv |
