# Source: https://docs.snowflake.com/en/user-guide/data-quality-system-dmfs.md

# System data metric functions

This topic is a reference for the system data metric functions (DMFs) that Snowflake provides to all accounts. DMFs are the building block
of [data quality checks](data-quality-intro.md).

## About system DMFs

Snowflake provides system DMFs in the CORE schema of the shared [SNOWFLAKE database](../sql-reference/snowflake-db.md). System DMFs are
maintained by Snowflake; you cannot change the name or functionality of any system DMF.

Each system DMF enables you to measure a different data quality attribute. You can assign more than one system DMF to a table or view to
allow for a more comprehensive data quality measurement to address your governance and compliance needs.

## System DMFs

Currently, Snowflake supports these system DMFs to measure common metrics without having to define them:

| Category | System DMF | Description |
| --- | --- | --- |
| Accuracy | [BLANK_COUNT](../sql-reference/functions/dmf_blank_count.md) | Determine how many blank values are in a column. |
|  | [BLANK_PERCENT](../sql-reference/functions/dmf_blank_percent.md) | Determine what percentage of a column’s values are blank. |
|  | [NULL_COUNT](../sql-reference/functions/dmf_null_count.md) | Determine how many NULL values are in a column. |
|  | [NULL_PERCENT](../sql-reference/functions/dmf_null_percent.md) | Determine what percentage of a column’s values are NULL. |
| Freshness | [FRESHNESS](../sql-reference/functions/dmf_freshness.md) | Determine the freshness of a table’s data based on a timestamp column or the most recent [DML operation](../sql-reference/sql-dml.md). |
|  | [DATA_METRIC_SCHEDULE_TIME](../sql-reference/functions/dmf_data_metric_schedule_time.md) | Define custom freshness metrics. |
| Statistics | [AVG](../sql-reference/functions/dmf_avg.md) | Determine the average value of a column. |
|  | [MAX](../sql-reference/functions/dmf_max.md) | Determine the maximum value of a column. |
|  | [MIN](../sql-reference/functions/dmf_min.md) | Determine the minimum value of a column. |
|  | [STDDEV](../sql-reference/functions/dmf_stddev.md) | Determine the standard deviation value for a column. |
| Uniqueness | [ACCEPTED_VALUES](../sql-reference/functions/dmf_accepted_values.md) | Determine whether values in a column match a Boolean expression. |
|  | [DUPLICATE_COUNT](../sql-reference/functions/dmf_duplicate_count.md) | Determine the number of duplicate values in a column, including NULL values. |
|  | [UNIQUE_COUNT](../sql-reference/functions/dmf_unique_count.md) | Determine the number of unique, non-NULL values in a column. |
| Volume | [ROW_COUNT](../sql-reference/functions/dmf_row_count.md) | Determine how many records are in the table or view. |
