# Source: https://docs.snowflake.com/en/sql-reference/account-usage/column_query_pruning_history.md

Schemas:
:   [ACCOUNT_USAGE](../account-usage.md)

# COLUMN_QUERY_PRUNING_HISTORY view

Use this Account Usage view to gain a better understanding of data access patterns during
query execution, including some column-level details, such as the “access type” and candidate
[search optimization expressions](../../user-guide/search-optimization-service.md) that are potentially beneficial.

You can use this view in combination with the [TABLE_QUERY_PRUNING_HISTORY view](table_query_pruning_history.md). For example,
you can identify access to target tables by using the TABLE_QUERY_PRUNING_HISTORY view, then
identify frequently used columns on those tables by using the COLUMN_QUERY_PRUNING_HISTORY view.

Each row in this view represents the query pruning history for a specific column within a given time interval. The data is
aggregated per column, per table, per interval, and includes metrics such as the number of queries executed, partitions scanned,
partitions pruned, rows scanned, rows pruned, and rows matched.

See also [TABLE_PRUNING_HISTORY view](table_pruning_history.md) and [Query Pruning](../../user-guide/tables-clustering-micropartitions.md).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| INTERVAL_START_TIME | TIMESTAMP_LTZ | Start of the time range (on the hour mark) during which the queries were executed and completed. |
| INTERVAL_END_TIME | TIMESTAMP_LTZ | End of the time range (on the hour mark) during which the queries were executed and completed. |
| TABLE_ID | NUMBER | Internal/system-generated identifier for the table that was queried. |
| TABLE_NAME | VARCHAR | Name of the table that was queried. |
| SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema that contains the table that was queried. |
| SCHEMA_NAME | VARCHAR | Name of the schema that contains the table that was queried. |
| DATABASE_ID | NUMBER | Internal/system-generated identifier for the database that contains the table that was queried. |
| DATABASE_NAME | VARCHAR | Name of the database that contains the table that was queried. |
| WAREHOUSE_ID | NUMBER | Internal/system-generated identifier for the warehouse that was used to run the queries. |
| WAREHOUSE_NAME | VARCHAR | Name of the warehouse that ran the queries. |
| QUERY_HASH | VARCHAR | The [hash value](../../user-guide/query-hash.md) computed based on the canonicalized SQL text. |
| QUERY_PARAMETERIZED_HASH | VARCHAR | The [hash value](../../user-guide/query-hash.md) computed based on the parameterized query. |
| COLUMN_ID | NUMBER | Internal/system-generated identifier for the column accessed from the table that was queried. |
| COLUMN_NAME | VARCHAR | Name of the column accessed from the table that was queried. |
| VARIANT_PATH | VARCHAR | Path to the semi-structured data being accessed (if applicable). NULL if the column accessed does not have a semi-structured data type. |
| ACCESS_TYPE | VARCHAR | Type of access performed on the column (`WHERE` or `JOIN` condition). |
| NUM_QUERIES | NUMBER | Number of queries executed in this time range with this specific QUERY_HASH value, using this warehouse, accessing this column (and variant path if applicable) on this table with this type of access. |
| AGGREGATE_QUERY_ELAPSED_TIME | NUMBER | Total elapsed time (in milliseconds) for queries defined by NUM_QUERIES. This total includes queueing and other time not associated with compilation and execution. |
| AGGREGATE_QUERY_COMPILATION_TIME | NUMBER | Total compilation time (in milliseconds) for queries defined by NUM_QUERIES. |
| AGGREGATE_QUERY_EXECUTION_TIME | NUMBER | Total execution time (in milliseconds) for queries defined by NUM_QUERIES. |
| PARTITIONS_SCANNED | NUMBER | Number of partitions scanned on this table for queries defined by NUM_QUERIES. |
| PARTITIONS_PRUNED | NUMBER | Number of partitions pruned on this table for queries defined by NUM_QUERIES. These partitions were eliminated during query processing and not scanned, improving the efficiency of the query. |
| ROWS_SCANNED | NUMBER | Number of rows scanned on this table for queries defined by NUM_QUERIES. |
| ROWS_PRUNED | NUMBER | Number of rows pruned on this table for queries defined by NUM_QUERIES. These rows were eliminated during query processing and not scanned, improving the efficiency of the query. |
| ROWS_MATCHED | NUMBER | Number of rows that matched the WHERE clause filters while scanning this table for the queries defined by NUM_QUERIES. |
| SEARCH_OPTIMIZATION_SUPPORTED_EXPRESSIONS | ARRAY | List of supported search optimization expressions on this column that could potentially speed up scanning this table for the queries defined by NUM_QUERIES. |

## Usage notes

* Latency for the view may be up to 4 hours.
* Data is retained for 1 year.
* This view does not include pruning information for [hybrid tables](../../user-guide/tables-hybrid.md).
* Users and roles that have been granted the USAGE_VIEWER database role can access this view. For more information, see
  [SNOWFLAKE database roles](../snowflake-db-roles.md).
* The ACCESS_TYPE column contains one of the following values:

  * `WHERE`: The column is used in a filter condition in the [WHERE](../constructs/where.md) clause.
  * `JOIN`: The column is used in a condition for a [JOIN](../constructs/join.md) operation.
* The access behavior shown in this view reflects the actual query plan that was executed, which might be different from the original query text. For example, if a HAVING clause does not reference aggregated results produced by the GROUP BY clause, it might be optimized and rewritten as a WHERE clause, and the ACCESS_TYPE value will be `WHERE`.
* For complex filtering conditions that can’t benefit from a pushdown optimization, rows might not be filtered out during the table scan operation, even if they do not match the filtering condition. Therefore, these rows are counted in the ROWS_MATCHED value.
* Currently, the SEARCH_OPTIMIZATION_SUPPORTED_EXPRESSIONS column only suggests the EQUALITY and SUBSTRING [search methods](../sql/alter-table.md).
* This view retains data for the 1,000 longest-running table scans per query. Only extremely complex queries
  exceed this number of scans so data is rarely omitted.

## Example

For a given day, return column-level pruning history for queries against a specific table:

```sqlexample
SELECT interval_start_time, table_name, column_name, access_type, num_queries,
    rows_scanned, rows_pruned, rows_matched,
    search_optimization_supported_expressions::VARCHAR as search_optim
  FROM SNOWFLAKE.ACCOUNT_USAGE.COLUMN_QUERY_PRUNING_HISTORY
  WHERE interval_start_time like '2025-04-24%' AND table_name='SENSOR_DATA_TS'
  ORDER BY 3, 1;
```

```output
+-------------------------------+----------------+-------------+-------------+-------------+--------------+-------------+--------------+-----------------------------+
| INTERVAL_START_TIME           | TABLE_NAME     | COLUMN_NAME | ACCESS_TYPE | NUM_QUERIES | ROWS_SCANNED | ROWS_PRUNED | ROWS_MATCHED | SEARCH_OPTIM                |
|-------------------------------+----------------+-------------+-------------+-------------+--------------+-------------+--------------+-----------------------------|
| 2025-04-24 14:00:00.000 -0700 | SENSOR_DATA_TS | DEVICE_ID   | WHERE       |           1 |      2678400 |     2678400 |            5 | ["EQUALITY(\"DEVICE_ID\")"] |
| 2025-04-24 14:00:00.000 -0700 | SENSOR_DATA_TS | DEVICE_ID   | WHERE       |           1 |      2678400 |     2678400 |            5 | ["EQUALITY(\"DEVICE_ID\")"] |
| 2025-04-24 15:00:00.000 -0700 | SENSOR_DATA_TS | DEVICE_ID   | WHERE       |           1 |      2678400 |     2678400 |      2678400 | ["EQUALITY(\"DEVICE_ID\")"] |
| 2025-04-24 15:00:00.000 -0700 | SENSOR_DATA_TS | DEVICE_ID   | WHERE       |           1 |      2678400 |     2678400 |      2678400 | ["EQUALITY(\"DEVICE_ID\")"] |
| 2025-04-24 15:00:00.000 -0700 | SENSOR_DATA_TS | DEVICE_ID   | WHERE       |           1 |      2678400 |     2678400 |            5 | ["EQUALITY(\"DEVICE_ID\")"] |
| 2025-04-24 15:00:00.000 -0700 | SENSOR_DATA_TS | DEVICE_ID   | WHERE       |           1 |      2678400 |     2678400 |      2678400 | ["EQUALITY(\"DEVICE_ID\")"] |
| 2025-04-24 17:00:00.000 -0700 | SENSOR_DATA_TS | DEVICE_ID   | WHERE       |           1 |      2678400 |     2678400 |      2678400 | ["EQUALITY(\"DEVICE_ID\")"] |
| 2025-04-24 17:00:00.000 -0700 | SENSOR_DATA_TS | DEVICE_ID   | WHERE       |           1 |      2678400 |     2678400 |      2678400 | ["EQUALITY(\"DEVICE_ID\")"] |
| 2025-04-24 19:00:00.000 -0700 | SENSOR_DATA_TS | DEVICE_ID   | WHERE       |           1 |      2678400 |     2678400 |      2678400 | ["EQUALITY(\"DEVICE_ID\")"] |
| 2025-04-24 19:00:00.000 -0700 | SENSOR_DATA_TS | DEVICE_ID   | WHERE       |           1 |      2678400 |     2678400 |      2678400 | ["EQUALITY(\"DEVICE_ID\")"] |
| 2025-04-24 17:00:00.000 -0700 | SENSOR_DATA_TS | TEMPERATURE | WHERE       |           1 |      5356800 |           0 |      3262387 | NULL                        |
| 2025-04-24 17:00:00.000 -0700 | SENSOR_DATA_TS | TEMPERATURE | WHERE       |           1 |      2678400 |     2678400 |       394106 | NULL                        |
| 2025-04-24 17:00:00.000 -0700 | SENSOR_DATA_TS | TEMPERATURE | WHERE       |           1 |      5356800 |           0 |      1227686 | NULL                        |
| 2025-04-24 17:00:00.000 -0700 | SENSOR_DATA_TS | TEMPERATURE | WHERE       |           1 |      2678400 |     2678400 |       216642 | NULL                        |
| 2025-04-24 17:00:00.000 -0700 | SENSOR_DATA_TS | TEMPERATURE | WHERE       |           1 |      2678400 |     2678400 |       216642 | NULL                        |
| 2025-04-24 17:00:00.000 -0700 | SENSOR_DATA_TS | TEMPERATURE | WHERE       |           1 |      5356800 |           0 |      1227686 | NULL                        |
| 2025-04-24 17:00:00.000 -0700 | SENSOR_DATA_TS | TEMPERATURE | WHERE       |           1 |      5356800 |           0 |       820272 | NULL                        |
| 2025-04-24 17:00:00.000 -0700 | SENSOR_DATA_TS | TEMPERATURE | WHERE       |           1 |      5356800 |           0 |      3262387 | NULL                        |
| 2025-04-24 17:00:00.000 -0700 | SENSOR_DATA_TS | TEMPERATURE | WHERE       |           1 |      5356800 |           0 |      3262387 | NULL                        |
| 2025-04-24 17:00:00.000 -0700 | SENSOR_DATA_TS | TEMPERATURE | WHERE       |           1 |      5356800 |           0 |      1227686 | NULL                        |
| 2025-04-24 17:00:00.000 -0700 | SENSOR_DATA_TS | TEMPERATURE | WHERE       |           1 |      2678400 |     2678400 |       216642 | NULL                        |
+-------------------------------+----------------+-------------+-------------+-------------+--------------+-------------+--------------+-----------------------------+
```

The `sensor_data_ts` table in this query contains 5356800 rows of synthetic time-series data. Exactly half of the rows in the table (2678400) were
pruned for a number of queries that filtered the `device_id` and `temperature` columns in WHERE clause conditions.

The `device_id` column is suggested as a target for a search optimization that uses the EQUALITY search method. Table scans might benefit from the addition of this
search optimization.

> **Tip:**
>
> You can use the [ARRAY_TO_STRING](../functions/array_to_string.md) function to convert the SEARCH_OPTIMIZATION_SUPPORTED_EXPRESSIONS column to a string for easier
> readability. For example:
>
> ```sqlexample
> ARRAY_TO_STRING(search_optimization_supported_expressions, ', ')
> ```
