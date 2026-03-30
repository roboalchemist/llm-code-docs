# Source: https://docs.snowflake.com/en/sql-reference/account-usage/table_pruning_history.md

Schemas:
:   [ACCOUNT_USAGE](../account-usage.md)

# TABLE_PRUNING_HISTORY view

This Account Usage view can be used to determine the efficiency of pruning for all tables,
and to understand how a table’s default (natural) ordering of data affects pruning.

You can compare the number of partitions pruned (`PARTITIONS_PRUNED`) to the
total number of partitions scanned and pruned (`PARTITIONS_SCANNED + PARTITIONS_PRUNED`).

Each row in this view represents the pruning history for a specific table within a given time interval.
The data is aggregated by time interval and includes information about the number of scans, partitions
scanned, partitions pruned, rows scanned, and rows pruned.

You can also use this view to compare the effects on pruning before and after enabling
[Automatic Clustering](../../user-guide/tables-auto-reclustering.md) and
[search optimization](../../user-guide/search-optimization-service.md) for a table.

See also [TABLE_QUERY_PRUNING_HISTORY view](table_query_pruning_history.md) and
[COLUMN_QUERY_PRUNING_HISTORY view](column_query_pruning_history.md).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | Start of the time range (on the hour mark) during which the queries were executed and completed. |
| END_TIME | TIMESTAMP_LTZ | End of the time range (on the hour mark) during which the queries were executed and completed. |
| TABLE_ID | NUMBER | Internal/system-generated identifier for the table that was queried. |
| TABLE_NAME | VARCHAR | Name of the table that was queried. |
| SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema that contains the table that was queried. |
| SCHEMA_NAME | VARCHAR | Name of the schema that contains the table that was queried. |
| DATABASE_ID | NUMBER | Internal/system-generated identifier for the database that contains the table that was queried. |
| DATABASE_NAME | VARCHAR | Name of the database that contains the table that was queried. |
| NUM_SCANS | NUMBER | Number of scan operations from all queries (including SELECT statements and DML statements) on the table during the START_TIME and END_TIME window. Note that a given query might result in multiple scan operations on the same table. |
| PARTITIONS_SCANNED | NUMBER | Number of partitions scanned during the scan operations described in `NUM_SCANS`. |
| PARTITIONS_PRUNED | NUMBER | Number of partitions pruned for the queries described in `NUM_SCANS`. These partitions were eliminated during query processing, improving the efficiency of the query. |
| ROWS_SCANNED | NUMBER | Number of rows scanned during the scan operations described in `NUM_SCANS`. |
| ROWS_PRUNED | NUMBER | Number of rows pruned for the queries described in `NUM_SCANS`. These rows were eliminated during query processing, improving the efficiency of the query. |

## Usage notes

* Latency for the view may be up to 6 hours.
* This view does not include pruning information for [hybrid tables](../../user-guide/tables-hybrid.md).
* This view retains data for the 1,000 longest-running table scans per query. Only extremely complex queries
  exceed this number of scans so data is rarely omitted.

## Examples

List the top five tables that had the worst pruning efficiency within the last seven days:

```sqlexample
SELECT
    table_id,
    ANY_VALUE(table_name) AS table_name,
    SUM(num_scans) AS total_num_scans,
    SUM(partitions_scanned) AS total_partitions_scanned,
    SUM(partitions_pruned) AS total_partitions_pruned,
    SUM(rows_scanned) AS total_rows_scanned,
    SUM(rows_pruned) AS total_rows_pruned
  FROM SNOWFLAKE.ACCOUNT_USAGE.TABLE_PRUNING_HISTORY
  WHERE start_time >= DATEADD(day, -7, CURRENT_TIMESTAMP())
  GROUP BY table_id
  ORDER BY
    total_partitions_pruned / GREATEST(total_partitions_scanned + total_partitions_pruned, 1),
    total_partitions_scanned DESC
  LIMIT 5;
```

```output
+----------+----------------+-----------------+--------------------------+-------------------------+--------------------+-------------------+
| TABLE_ID | TABLE_NAME     | TOTAL_NUM_SCANS | TOTAL_PARTITIONS_SCANNED | TOTAL_PARTITIONS_PRUNED | TOTAL_ROWS_SCANNED | TOTAL_ROWS_PRUNED |
|----------+----------------+-----------------+--------------------------+-------------------------+--------------------+-------------------|
|   308226 | SENSOR_DATA_TS |              11 |                       21 |                       1 |           52500000 |           2500000 |
|   185364 | MATCH          |              16 |                       14 |                       2 |             240968 |             34424 |
|   209932 | ORDER_HEADER   |               2 |                      300 |                      56 |          421051748 |          75350790 |
|   209922 | K7_T1          |             261 |                      261 |                      52 |              30421 |              3272 |
|   338948 | SENSOR_DATA_TS |               9 |                       15 |                       3 |           38880000 |           8035200 |
+----------+----------------+-----------------+--------------------------+-------------------------+--------------------+-------------------+
```

The example above uses [GREATEST](../functions/greatest.md) to avoid dividing by zero when the sum of the number
of partitions scanned and the number of partitions pruned is zero.
