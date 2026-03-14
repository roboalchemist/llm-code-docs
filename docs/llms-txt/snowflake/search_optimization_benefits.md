# Source: https://docs.snowflake.com/en/sql-reference/account-usage/search_optimization_benefits.md

Schemas:
:   [ACCOUNT_USAGE](../account-usage.md)

# SEARCH_OPTIMIZATION_BENEFITS view

This Account Usage view can be used to determine the efficacy of pruning due to
[search optimization](../../user-guide/search-optimization-service.md).

This view provides information about pruning, similar to the information provided by the [TABLE_PRUNING_HISTORY view](table_pruning_history.md). Note that
TABLE_PRUNING_HISTORY view provides information about all pruning, as opposed to pruning due to search optimization.

You can use this view to compare the effects on pruning before and after adding search optimization to a table. When you query
this view, compare the number of partitions pruned due to search optimization (`PARTITIONS_PRUNED_ADDITIONAL`) against the
total number of partitions pruned (`PARTITIONS_PRUNED_DEFAULT + PARTITIONS_PRUNED_ADDITIONAL`).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | Start of the time range (on the hour mark) during which the queries were executed. |
| END_TIME | TIMESTAMP_LTZ | End of the time range (on the hour mark) during which the queries were executed. |
| TABLE_ID | NUMBER | Internal/system-generated identifier for the table that was queried. |
| TABLE_NAME | VARCHAR | Name of the table that was queried. |
| SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema that contains the table that was queried. |
| SCHEMA_NAME | VARCHAR | Name of the schema that contains the table that was queried. |
| DATABASE_ID | NUMBER | Internal/system-generated identifier for the database that contains the table that was queried. |
| DATABASE_NAME | VARCHAR | Name of the database that contains the table that was queried. |
| NUM_SCANS | NUMBER | Number of scan operations (from all queries on the table during the START_TIME and END_TIME window) that used [search optimization](../../user-guide/search-optimization-service.md) to improve pruning. Note that a given query might result in multiple scan operations on the same table. |
| PARTITIONS_SCANNED | NUMBER | Number of partitions scanned during the scan operations described in `NUM_SCANS`. |
| PARTITIONS_PRUNED_DEFAULT | NUMBER | Number of partitions that were pruned as a result of the default (natural) ordering of data for the queries described in `NUM_SCANS`. These partitions were eliminated during query processing, improving the efficiency of the query. |
| PARTITIONS_PRUNED_ADDITIONAL | NUMBER | Number of partitions that were pruned as a result of [search optimization](../../user-guide/search-optimization-service.md) for the queries described in `NUM_SCANS`. These partitions were eliminated during query processing, improving the efficiency of the query. |

## Usage Notes

* Latency for the view may be up to 6 hours.
* This view retains data for the 1,000 longest-running table scans per query. Only extremely complex queries
  exceed this number of scans so data is rarely omitted.

## Examples

List the top five tables that have benefited the most from search optimization within the last seven days:

```sqlexample
SELECT
    table_id,
    ANY_VALUE(table_name) AS table_name,
    SUM(num_scans) AS total_num_scans,
    SUM(partitions_pruned_default) AS total_partitions_pruned_default,
    SUM(partitions_pruned_additional) AS total_partitions_pruned_additional,
    SUM(partitions_scanned) AS total_partitions_scanned
  FROM SNOWFLAKE.ACCOUNT_USAGE.SEARCH_OPTIMIZATION_BENEFITS
  WHERE start_time >= DATEADD(day, -7, CURRENT_TIMESTAMP())
  GROUP BY table_id
  ORDER BY
    total_partitions_pruned_additional / GREATEST(total_partitions_pruned_default + total_partitions_pruned_additional, 1) DESC,
    total_partitions_pruned_additional DESC
  LIMIT 5;
```

The example above uses [GREATEST](../functions/greatest.md) to avoid dividing by zero when the number of partitions pruned is
zero.
