# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sfn_maprun.dataset.md

---
title: Step Functions Maprun
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Step Functions Maprun
---

# Step Functions Maprun

This table represents the Step Functions Maprun resource from Amazon Web Services.

```
aws.sfn_maprun
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                                                                                                                                                                        | Description |
| ---------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| account_id                   | core | string     |
| execution_arn                | core | string     | The Amazon Resource Name (ARN) that identifies the execution in which the Map Run was started.                                                                                                                                   |
| execution_counts             | core | json       | A JSON object that contains information about the total number of child workflow executions for the Map Run, and the count of child workflow executions for each status, such as <code>failed</code> and <code>succeeded</code>. |
| item_counts                  | core | json       | A JSON object that contains information about the total number of items, and the item count for each processing status, such as <code>pending</code> and <code>failed</code>.                                                    |
| map_run_arn                  | core | string     | The Amazon Resource Name (ARN) that identifies a Map Run.                                                                                                                                                                        |
| max_concurrency              | core | int64      | The maximum number of child workflow executions configured to run in parallel for the Map Run at the same time.                                                                                                                  |
| redrive_count                | core | int64      | The number of times you've redriven a Map Run. If you have not yet redriven a Map Run, the <code>redriveCount</code> is 0. This count is only updated if you successfully redrive a Map Run.                                     |
| redrive_date                 | core | timestamp  | The date a Map Run was last redriven. If you have not yet redriven a Map Run, the <code>redriveDate</code> is null.                                                                                                              |
| start_date                   | core | timestamp  | The date when the Map Run was started.                                                                                                                                                                                           |
| status                       | core | string     | The current status of the Map Run.                                                                                                                                                                                               |
| stop_date                    | core | timestamp  | The date when the Map Run was stopped.                                                                                                                                                                                           |
| tags                         | core | hstore_csv |
| tolerated_failure_count      | core | int64      | The maximum number of failed child workflow executions before the Map Run fails.                                                                                                                                                 |
| tolerated_failure_percentage | core | float64    | The maximum percentage of failed child workflow executions before the Map Run fails.                                                                                                                                             |
