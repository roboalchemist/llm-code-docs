# Source: https://docs.snowflake.com/en/sql-reference/account-usage/table_dml_history.md

Schemas:
:   [ACCOUNT_USAGE](../account-usage.md)

# TABLE_DML_HISTORY view

This Account Usage view can be used to determine the magnitude and effects of the DML operations performed on a table. Note that
these DML operations include ones initiated by [Snowpipe](../../user-guide/data-load-snowpipe-intro.md) but exclude operations initiated
by background maintenance services
(for example, [Automatic Clustering](../../user-guide/tables-auto-reclustering.md), maintenance for materialized views and
[search optimization](../../user-guide/search-optimization-service.md)).

You can query this view with the [QUERY_HISTORY view](query_history.md) and the
[LOAD_HISTORY view](load_history.md) to identify the DML operations that have a significant impact. This can
help you to identify opportunities for optimization.

In addition, you can query this view with the [AUTOMATIC_CLUSTERING_HISTORY view](automatic_clustering_history.md) and the
[SEARCH_OPTIMIZATION_HISTORY view](search_optimization_history.md) to visualize the relationship between these DML operations and the
credits charged for Automatic Clustering and the search optimization service. (These services can be triggered by DML operations.)

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | Start of the time range (on the hour mark) during which the DML operations were performed. |
| END_TIME | TIMESTAMP_LTZ | End of the time range (on the hour mark) during which the DML operations were performed. |
| TABLE_ID | NUMBER | Internal/system-generated identifier for the table modified by the DML operations. |
| TABLE_NAME | VARCHAR | Name of the table modified by the DML operations. |
| SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema that contains the table modified by the DML operations. |
| SCHEMA_NAME | VARCHAR | Name of the schema that contains the table modified by the DML operations. |
| DATABASE_ID | NUMBER | Internal/system-generated identifier for the database that contains the table modified by the DML operations. |
| DATABASE_NAME | VARCHAR | Name of the database that contains the table modified by the DML operations. |
| ROWS_ADDED | NUMBER | Number of rows added by DML operations performed by users on the table during the START_TIME and END_TIME window. |
| ROWS_REMOVED | NUMBER | Number of rows removed by DML operations performed by users on the table during the START_TIME and END_TIME window. |
| ROWS_UPDATED | NUMBER | Number of rows updated by DML operations performed by users on the table during the START_TIME and END_TIME window. |

## Usage notes

* Latency for the view may be up to 6 hours.
* This view does not include DML operations on [hybrid tables](../../user-guide/tables-hybrid.md).

## Examples

The following example returns the top five tables that had the most rows added, removed, and updated by DML operations within the
last seven days.

```sqlexample
SELECT
    table_id,
    ANY_VALUE(table_name) AS table_name,
    SUM(rows_added) AS total_rows_added,
    SUM(rows_removed) AS total_rows_removed,
    SUM(rows_updated) AS total_rows_updated
  FROM SNOWFLAKE.ACCOUNT_USAGE.TABLE_DML_HISTORY
  WHERE start_time >= DATEADD(day, -7, CURRENT_TIMESTAMP())
  GROUP BY table_id
  ORDER BY total_rows_added + total_rows_removed + total_rows_updated DESC
  LIMIT 5;
```

```output
+----------+----------------------+------------------+--------------------+--------------------+
| TABLE_ID | TABLE_NAME           | TOTAL_ROWS_ADDED | TOTAL_ROWS_REMOVED | TOTAL_ROWS_UPDATED |
|----------+----------------------+------------------+--------------------+--------------------|
|   338948 | SENSOR_DATA_TS       |          5356800 |             259200 |                  0 |
|   338950 | SENSOR_DATA_DEVICE2  |          2678400 |                  0 |                  0 |
|   341006 | SENSOR_DATA_30_ROWS  |               30 |                  0 |                  0 |
|   341004 | SENSOR_DATA_12_HOURS |               12 |                  0 |                  0 |
|   340005 | SENSOR_DATA_12_HOURS |               12 |                  0 |                  0 |
+----------+----------------------+------------------+--------------------+--------------------+
```
