# Source: https://docs.snowflake.com/en/sql-reference/functions/dmf_data_metric_schedule_time.md

Categories:
:   [Data metric functions](../functions-data-metric.md)

# DATA_METRIC_SCHEDULED_TIME (system data metric function)

Returns the timestamp for when a DMF is scheduled to run or the current timestamp if the function is called manually.

You can use this DMF to define custom metrics to measure the freshness of your data or to define incremental metrics in
conjunction with DMFs that already exist.

## Syntax

```sqlsyntax
SNOWFLAKE.CORE.DATA_METRIC_SCHEDULED_TIME()
```

## Arguments

None.

## Returns

The function returns a scalar value with a TIMESTAMP_LTZ data type.

## Usage notes

Calling this function manually in a SELECT query returns the same value as the [CURRENT_TIMESTAMP](current_timestamp.md) function.

## Example

Create a custom data metric function to determine the data freshness on a table in the last hour:

> ```sqlexample
> CREATE OR REPLACE DATA METRIC FUNCTION data_freshness_hour(
>   ARG_T TABLE (ARG_C TIMESTAMP_LTZ))
>   RETURNS NUMBER AS
>   'SELECT TIMEDIFF(
>      minute,
>      MAX(ARG_C),
>      SNOWFLAKE.CORE.DATA_METRIC_SCHEDULED_TIME())
>    FROM ARG_T';
> ```

Call the data metric function manually:

> ```sqlexample
> SELECT data_freshness_hour(SELECT last_updated FROM hr.tables.empl_info) < 60;
> ```
>
> The statement returns `True` if there are no updates to the table in the last hour (60 minutes).
>
> The statement returns `False` if there were updates to the table that took place more than one hour ago.
