# Source: https://docs.snowflake.com/en/sql-reference/functions/model-monitor-drift-metric.md

Categories:
:   [Model monitor functions](../functions-model-monitors.md)

# MODEL_MONITOR_DRIFT_METRIC

Gets drift metrics from a [model monitor](../../developer-guide/snowflake-ml/model-registry/model-observability.md). Each model monitor monitors one machine learning model.

See also:
:   [Querying monitoring results](../../developer-guide/snowflake-ml/model-registry/model-observability.md) for more information.

## Syntax

```sqlsyntax
MODEL_MONITOR_DRIFT_METRIC(
  <model_monitor_name>, <drift_metric_name>, <column_name>
  [ , <granularity> [ , <start_time>  [ , <end_time> [ , <extra_args> ] ] ] ]
)
```

## Arguments

**Required:**

`model_monitor_name`
:   Name of the model monitor used to compute the metric.

    Valid values: A string that’s the name of the model monitor. It can be a simple or fully qualified name.

`drift_metric_name`
:   Name of the metric.

    Valid values:

    * `'JENSEN_SHANNON'`
    * `'DIFFERENCE_OF_MEANS'`
    * `'WASSERSTEIN'`
    * `'POPULATION_STABILITY_INDEX'`

`column_name`
:   Name of the column used to compute drift.

    Valid values: Any string that exists as a feature column, prediction column, or actual column in the model monitor.

**Optional:**

`granularity`
:   Granularity of the time range being queried. Default value is `1 DAY`.

    Valid values:

    * `'<num> DAY'`
    * `'<num> WEEK'`
    * `'<num> MONTH'`
    * `'<num> QUARTER'`
    * `'<num> YEAR'`
    * `'ALL'`
    * `NULL`

`start_time`
:   Start of the time range used to compute the metric. The default value is 60 days before the current time, and is calculated each time you call the function.

    Valid values: A timestamp expression or `NULL`.

`end_time`
:   End of the time range used to compute the metric. The default value is the current time, and is calculated each time you call the function.

    Valid values: A timestamp expression or `NULL`.

`extra_args`
:   Additional arguments for segment-specific queries. This parameter is optional - if not provided, the query returns metrics for all data (non-segment query).

    Valid values: A string in JSON format specifying segment column and value pairs: `'{"SEGMENTS": [{"column": "<segment_column_name>", "value": "<segment_value>"}]}'`

    > **Note:**
    >
    > Currently, segment queries support only 1 segment column:value pair per query. You cannot query multiple segments simultaneously in a single function call.

    For more information about segments, see [ML Observability: Monitoring model behavior over time](../../developer-guide/snowflake-ml/model-registry/model-observability.md).

## Returns

| Column | Description | Example values |
| --- | --- | --- |
| `EVENT_TIMESTAMP` | Timestamp at the start of the time range. | `2024-01-01 00:00:00.000` |
| `METRIC_VALUE` | Value of the metric within the specified time range. | `5` |
| `COL_COUNT_USED` | Number of records used to compute the metric. | `100` |
| `COL_COUNT_UNUSED` | Number of records excluded from the metric computation. | `10` |
| `BASELINE_COL_COUNT_USED` | Number of records used to compute the metric. | `10` |
| `BASELINE_COL_COUNT_UNUSED` | Number of records excluded from the metric computation. | `0` |
| `METRIC_NAME` | Name of the drift metric that has been computed. | `DIFFERENCE_OF_MEANS` |
| `COLUMN_NAME` | Name of the column for which the drift metric has been computed. | `FEATURE_NAME` |
| `SEGMENT_COLUMN` | Name of the segment column for which the metric is computed (or NULL for non-segment queries). | `CUSTOMER_TIER` |
| `SEGMENT_VALUE` | Segment value for which the metric is computed (or NULL for non-segment queries). | `PREMIUM` |

## Usage Notes

The model monitor must have a baseline set for the drift metric to be computed.

You might run into errors if you:

* Don’t set a baseline for the model monitor.
* Requested a numerical drift metric for a non-numeric feature.
* Use a drift metric that doesn’t exist in the model monitor.

If values you’ve specified for `column_name` or `model_monitor_name` are case-sensitive, or contain special characters or spaces, enclose them in double quotes.
You must enclose the double quotes within single quotes, such as `'"<model_monitor_name>"'`.

If double-quotes are not provided in these two fields, the `column_name` or `model_monitor_name` will be assumed to be case-insensitive.

To minimize potential impact from schema changes, update your queries to explicitly select only the necessary columns instead of using a wildcard (\*).

## Examples

The following example gets the differences of means drift metric for `MY_MONITOR` over a one-day period:

```sqlexample
SELECT * FROM TABLE(MODEL_MONITOR_DRIFT_METRIC(
'MY_MONITOR', 'DIFFERENCE_OF_MEANS', 'MODEL_PREDICTION', '1 DAY', TO_TIMESTAMP_TZ('2024-01-01'), TO_TIMESTAMP_TZ('2024-01-02'))
)
```

The following example gets the Jensen-Shannon drift metric for `MY_MONITOR` over the last 30 days:

```sqlexample
SELECT * FROM TABLE(MODEL_MONITOR_DRIFT_METRIC(
'MY_MONITOR', 'JENSEN_SHANNON', 'MODEL_PREDICTION', '1 DAY', DATEADD('DAY', -30, CURRENT_DATE()), CURRENT_DATE())
)
```
