# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.financialservices_backtest_result.dataset.md

---
title: Backtest Result
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Backtest Result
---

# Backtest Result

This table represents the Backtest Result resource from Google Cloud Platform.

```
gcp.financialservices_backtest_result
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                    | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| backtest_periods     | core | int64         | The number of consecutive months to conduct backtesting for, ending with the last full month prior to the end_time according to the dataset's timezone.                                                                      |
| create_time          | core | timestamp     | Output only. The timestamp of creation of this resource.                                                                                                                                                                     |
| datadog_display_name | core | string        |
| dataset              | core | string        | Required. The resource name of the Dataset to backtest on Format: `/projects/{project_num}/locations/{location}/instances/{instance}/datasets/{dataset}`                                                                     |
| end_time             | core | timestamp     | Required. End_time specifies the latest time from which labels are used and from which data is used to generate features for backtesting. End_time should be no later than the end of the date_range of the primary dataset. |
| labels               | core | array<string> | Labels                                                                                                                                                                                                                       |
| line_of_business     | core | string        | Output only. The line of business (Retail/Commercial) this backtest is for. Determined by Model, cannot be set by user.                                                                                                      |
| model                | core | string        | Required. The resource name of the Model to use or to backtest. Format: `/projects/{project_num}/locations/{location}/instances/{instance}/models/{model}`                                                                   |
| name                 | core | string        | Output only. The resource name of the BacktestResult. format: `/projects/{project_num}/locations/{location}/instances/{instance}/backtestResults/{backtest_result}`                                                          |
| organization_id      | core | string        |
| parent               | core | string        |
| performance_target   | core | json          | Required. PerformanceTarget gives information on how the test will be evaluated.                                                                                                                                             |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. State of the BacktestResult (creating, active, deleting, etc.)                                                                                                                                                  |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The timestamp of the most recent update of this resource.                                                                                                                                                       |
| zone_id              | core | string        |
