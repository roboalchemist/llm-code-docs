# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotsitewise_timeseries.dataset.md

---
title: Iotsitewise Timeseries
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Iotsitewise Timeseries
---

# Iotsitewise Timeseries

This table represents the iotsitewise_timeseries resource from Amazon Web Services.

```
aws.iotsitewise_timeseries
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                           | Description |
| ---------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| account_id                   | core | string     |
| alias                        | core | string     | The alias that identifies the time series.                                                                                                                                                                                                                                                                                                                                          |
| asset_id                     | core | string     | The ID of the asset in which the asset property was created.                                                                                                                                                                                                                                                                                                                        |
| data_type                    | core | string     | The data type of the time series. If you specify <code>STRUCT</code>, you must also specify <code>dataTypeSpec</code> to identify the type of the structure for this time series.                                                                                                                                                                                                   |
| data_type_spec               | core | string     | The data type of the structure for this time series. This parameter is required for time series that have the <code>STRUCT</code> data type. The options for this parameter depend on the type of the composite model in which you created the asset property that is associated with your time series. Use <code>AWS/ALARM_STATE</code> for alarm state in alarm composite models. |
| property_id                  | core | string     | The ID of the asset property, in UUID format.                                                                                                                                                                                                                                                                                                                                       |
| tags                         | core | hstore_csv |
| time_series_arn              | core | string     | The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the time series, which has the following format. <code>arn:${Partition}:iotsitewise:${Region}:${Account}:time-series/${TimeSeriesId}</code>                                                                                                                                     |
| time_series_creation_date    | core | timestamp  | The date that the time series was created, in Unix epoch time.                                                                                                                                                                                                                                                                                                                      |
| time_series_id               | core | string     | The ID of the time series.                                                                                                                                                                                                                                                                                                                                                          |
| time_series_last_update_date | core | timestamp  | The date that the time series was last updated, in Unix epoch time.                                                                                                                                                                                                                                                                                                                 |
