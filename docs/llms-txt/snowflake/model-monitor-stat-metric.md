# Source: https://docs.snowflake.com/en/sql-reference/functions/model-monitor-stat-metric.md

Categories:
:   [Model monitor functions](../functions-model-monitors.md)

# MODEL_MONITOR_STAT_METRIC

Gets count metrics from a [model monitor](../../developer-guide/snowflake-ml/model-registry/model-observability.md). Each model monitor monitors one machine learning model.

See also:
:   [Querying monitoring results](../../developer-guide/snowflake-ml/model-registry/model-observability.md) for more information.

## Syntax

```sqlsyntax
MODEL_MONITOR_STAT_METRIC(<model_monitor_name>, <stat_metric_name>, <column_name>
    [, <granularity> [, <start_time>  [, <end_time> [, <extra_args> ] ] ] ] )
```

## Arguments

**Required:**

`MODEL_MONITOR_NAME`
:   Name of the model monitor used to compute the metric.

    Valid values:

    A string that’s the name of the model monitor. It can be a simple or fully qualified name.

`METRIC_NAME`
:   Name of the metric.

    Valid values:

    > * `'COUNT'`
    > * `'COUNT_NULL'`

`COLUMN_NAME`
:   Name of the column used to compute the count.

    Valid values:

    Any string that exists as a feature column, prediction column, or actual column in the model monitor.

**Optional:**

`GRANULARITY`
:   Granularity of the time range being queried. The default value is `1 DAY`.

    Valid values:

    > * `'<num> DAY'`
    > * `'<num> WEEK'`
    > * `'<num> MONTH'`
    > * `'<num> QUARTER'`
    > * `'<num> YEAR'`
    > * `'ALL'`
    > * `NULL`

`START_TIME`
:   Start of the time range used to compute the metric. The default value is 60 days before the current time, and is calculated each time you call the function.

    Valid values:

    > A timestamp expression or `NULL`.

`END_TIME`
:   End of the time range used to compute the metric. The default value is the current time, and is calculated each time you call the function.

    Valid values:

    > A timestamp expression or `NULL`.

`EXTRA_ARGS`
:   Additional arguments for segment-specific queries. This parameter is optional - if not provided, the query returns metrics for all data (non-segment query).

    Valid values: A string in JSON format specifying segment column and value pairs: `'{"SEGMENTS": [{"column": "<segment_column_name>", "value": "<segment_value>"}]}'`

    > **Note:**
    >
    > Currently, segment queries support only 1 segment column:value pair per query. You cannot query multiple segments simultaneously in a single function call.

    For more information about segments, see [ML Observability: Monitoring model behavior over time](../../developer-guide/snowflake-ml/model-registry/model-observability.md).

## Returns

| **Column** | **Description** |
| --- | --- |
| `EVENT_TIMESTAMP` | Timestamp at the start of the time range. |
| `METRIC_VALUE` | Value of the metric within the specified time range. |
| `METRIC_NAME` | Name of the metric that has been computed. |
| `COLUMN_NAME` | Name of the column for which the stat metric has been computed. |
| `SEGMENT_COLUMN` | Name of the segment column for which the metric is computed (or NULL for non-segment queries). |
| `SEGMENT_VALUE` | Segment value for which the metric is computed (or NULL for non-segment queries). |

## Usage Notes

The model monitor must have the column being used to calculate the metric.

If the values you’ve specified for `column_name` or `model_monitor_name` are case-sensitive or contain special characters or spaces, enclose them in double quotes.
You must enclose the double quotes within single quotes. For example, `'"<example_model_monitor_name>"'`.

If double-quotes are not provided in these two fields, the `column_name` or `model_monitor_name` are assumed to be case-insensitive.

To minimize potential impact from schema changes, update your queries to explicitly select only the necessary columns instead of using a wildcard (\*).

## Examples

The following example gets count metrics for the specified model monitor and time range:

```sqlexample
SELECT * FROM TABLE(MODEL_MONITOR_STAT_METRIC(
'MY_MONITOR', 'COUNT', 'MODEL_PREDICTION', '1 DAY', TO_TIMESTAMP_TZ('2024-01-01')
, TO_TIMESTAMP_TZ('2024-01-02'))
)
```

The following example gets count metric for `MY_MONITOR` over the last 30 days:

```sqlexample
SELECT * FROM TABLE(MODEL_MONITOR_STAT_METRIC(
'MY_MONITOR', 'COUNT', 'MODEL_PREDICTION', '1 DAY', DATEADD('DAY', -30, CURRENT_DATE()), CURRENT_DATE())
)
```
