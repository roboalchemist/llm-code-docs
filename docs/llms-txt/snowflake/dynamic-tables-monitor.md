# Source: https://docs.snowflake.com/en/user-guide/dynamic-tables-monitor.md

# Monitor dynamic tables

This topic describes how to view and monitor the dynamic tables in your pipelines. For
guidance on what to look for when diagnosing performance issues, see
[Monitor dynamic table performance](dynamic-tables-performance-monitor.md).

| Section | Description |
| --- | --- |
| List dynamic tables or view information on specific columns | List the dynamic tables in a schema and view information about them. |
| View the graph of tables connected to your dynamic tables | See the graph of tables connected to your dynamic tables. |
| Monitor your dynamic tables using SQL table functions | Monitor your dynamic tables using SQL table functions. |
| Monitor the refresh status for your dynamic tables | View the refresh status for your dynamic tables. |

## List dynamic tables or view information on specific columns

To list the dynamic tables in a schema and view information about those dynamic tables, you can use either the following SQL commands or
[Snowsight](ui-snowsight-gs.md), as long as you use a role that has the MONITOR privilege on the dynamic tables.

For more information, see [Privileges to view a dynamic table’s metadata](dynamic-tables-privileges.md).

SQLSnowsight

To list the dynamic tables in the current database (or in the account, if no database is currently in use), use the
[SHOW DYNAMIC TABLES](../sql-reference/sql/show-dynamic-tables.md) command.

For example, to list the dynamic tables with names that start with `product_` in the database `mydb` and schema `myschema`, execute
the following SQL statement:

```sqlexample
SHOW DYNAMIC TABLES LIKE 'product_%' IN SCHEMA mydb.myschema;
```

```output
+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | created_on               | name       | database_name | schema_name | cluster_by | rows | bytes  | owner    | target_lag | refresh_mode | refresh_mode_reason  | warehouse | comment | text                            | automatic_clustering | scheduling_state | last_suspended_on | is_clone  | is_replica  | is_iceberg | data_timestamp           | owner_role_type |
  |-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  |2025-01-01 16:32:28 +0000 | product_dt | my_db         | my_schema   |            | 2    | 2048   | ORGADMIN | DOWNSTREAM | INCREMENTAL  | null                 | mywh      |         | create or replace dynamic table | OFF                  | ACTIVE           | null              | false     | false       | false      |2025-01-01 16:32:28 +0000 | ROLE            |
                                                                                                                                                                                         |  product dt ...                 |                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                       |
  +-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

To output information about the columns in a dynamic table, use the [DESCRIBE DYNAMIC TABLE](../sql-reference/sql/desc-dynamic-table.md) command.

For example, to list the columns in `my_dynamic_table`, execute the following SQL statement:

```sqlexample
DESC DYNAMIC TABLE my_dynamic_table;
```

```output
+-------------------+--------------------------------------------------------------------------------------------------------------------------+
  | name   | type         | kind   | null? | default | primary key | unique key | check | expression | comment | policy name  | privacy domain |
  |-------------------+------------------------------------------------------------------------------------------------------------------------|
  | AMOUNT | NUMBER(38,0) | COLUMN | Y     | null    | N           | N          | null  | null       | null    | null         | null           |                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                       |
  +-------------------+------------------------------------------------------------------------------------------------------------------------+
```

Dynamic tables are also included in the results of the [TABLES view](../sql-reference/account-usage/tables.md).

To list the dynamic tables in a schema and view information about a specific dynamic table, do the following:

1. Sign in to [Snowsight](ui-snowsight-gs.md).
2. In the navigation menu, select Catalog » Database Explorer.
3. Select a database and schema.
4. Select the Dynamic Tables tab or expand Dynamic Tables in the database object explorer.
5. To view information about a specific dynamic table, select the dynamic table from the list of dynamic tables in the Dynamic Tables
   tab or from the database object explorer.
6. The tabs in this page provide the following details about your selected dynamic table:

   * Table Details: Displays basic information about the dynamic table, including:
   > * The scheduling state of your dynamic table.
   > * The last refresh status of your dynamic table. For failed refreshes, you can see more information about the error if you hover over
   >   the status.
   > * The current and target lag for your dynamic table.
   > * Whether [incremental refreshes or full refreshes](dynamic-tables-refresh.md) are used to update the table.
   > * The definition of the dynamic table.
   > * The tags for the dynamic table.
   > * The privileges granted for working with the dynamic table.

> * Columns: Information about the columns in the dynamic table.
> * Data Preview: A preview of up to 100 rows of the data in the dynamic table.
> * Graph: Displays the [directed acyclic graph (DAG)](dynamic-tables-create.md) that includes this dynamic
>   table.
> * Refresh History: Displays the history of refreshes and the lag metrics.

## View the graph of tables connected to your dynamic tables

Viewing dependencies is particularly useful for troubleshooting dynamic table chains. In Snowsight, you can visualize which dynamic
tables a given dynamic table depends on using the lineage graph. For example, you can identify the following:

* Upstream dependencies where a dynamic table pulls data from.
* Downstream dependencies that might be impacted by changes to a dynamic table.

Dependencies can impact refresh performance. For example, suppose your dynamic table’s upstream table has a large data load added just before
its scheduled refresh. Your dynamic table will wait for it to finish the refresh, causing it to miss its target lag. In the lineage graph,
you’d see the input table marked as “executing,” indicating the delay.

To view the graph of a particular dynamic table, do the following:

1. Sign in to [Snowsight](ui-snowsight-gs.md).
2. In the navigation menu, select Transformation » Dynamic tables.
3. Select your dynamic table. The Graph view is displayed by default. This displays the graph with the node for the dynamic table
   selected. The Details pane on the right displays information about its lag metrics and configuration.
4. To display the details of a different table in the graph, select that table.

To update the graph, select the refresh button in the bar above the graph.

If a refresh failed due to an UPSTREAM_FAILED error code, you can use the graph to visualize which upstream table caused the failure.

To view the full details of a table in the graph, see List dynamic tables or view information on specific columns.

## Monitor your dynamic tables using SQL table functions

Use the following INFORMATION_SCHEMA table functions to monitor your dynamic tables:

* [DYNAMIC_TABLES](../sql-reference/functions/dynamic_tables.md): Returns metadata about your dynamic tables, including aggregate lag metrics and the status
  of the most recent refreshes, within seven days of the current time.
* [DYNAMIC_TABLE_REFRESH_HISTORY](../sql-reference/functions/dynamic_table_refresh_history.md): Returns information about each completed and running refresh of your dynamic
  tables, including refresh status and trigger, and the target lag.

  * [DYNAMIC_TABLE_REFRESH_HISTORY view](../sql-reference/account-usage/dynamic_table_refresh_history.md): This Account Usage view also displays information for dynamic table
    refresh history. It is useful for debugging issues that are for longer than the DYNAMIC_TABLE_REFRESH_HISTORY table function’s data
    retention time (seven days).
* [DYNAMIC_TABLE_GRAPH_HISTORY](../sql-reference/functions/dynamic_table_graph_history.md): Returns information that provides the history of each dynamic table, its
  properties, and its dependencies on other tables and dynamic tables.

  You can use this table function to get a snapshot of the dependency tree of dynamic tables at a given point in time.

  The output also reflects the changes made to the properties of a dynamic table over time. Each row represents a dynamic table
  and a specific set of properties. If you change a property of a dynamic table (for example, the target lag), the function returns the most
  up to date property.

## Monitor the refresh status for your dynamic tables

This section explains how to view the refresh status of all or specific dynamic tables.

* For guidance on what to look for when diagnosing slow refreshes, see
  [Monitor dynamic table performance](dynamic-tables-performance-monitor.md).
* For troubleshooting skipped or failed refreshes, see
  [Troubleshooting skipped or failed dynamic table refreshes](dynamic-tables-troubleshoot-refresh.md).

### Monitor the refreshes for all your dynamic tables

You can use Snowsight or the DYNAMIC_TABLES table function to view the refresh status for all your dynamic tables.

SnowsightSQL

Sign in to [Snowsight](ui-snowsight-gs.md). In the navigation menu, select Transformation » Dynamic tables.

You can view the state and last refresh status for all your dynamic tables on this page. You can also filter by database or schema to
narrow the results.

[DYNAMIC_TABLES](../sql-reference/functions/dynamic_tables.md) provides information about all of the dynamic tables in your account.

The following example retrieves the information about the state and target lag for all dynamic tables in the account and their associated
database and schema.

```sqlexample
SELECT
  name,
  database_name,
  schema_name,
  scheduling_state,
  target_lag_type,
  target_lag_sec,
FROM
  TABLE (
    INFORMATION_SCHEMA.DYNAMIC_TABLES ()
  )
ORDER BY
  name;
```

```output
+--------------------+------------------------------+--------------------------------------------------------------------------------------------------+-----------------+----------------+
| NAME               | DATABASE_NAME | SCHEMA_NAME | SCHEDULING_STATE                                                                                  | TARGET_LAG_TYPE | TARGET_LAG_SEC |
|--------------------+------------------------------+--------------------------------------------------------------------------------------------------|-----------------+----------------+
| MY_DYNAMIC_TABLE_1 | MY_DB_1       | MY_SCHEMA_1 | {                                                                                                 |                 |                |
|                    |               |             |    "reason_code": "UPSTREAM_SUSPENDED_DUE_TO_ERRORS",                                             |                 |                |
|                    |               |             |    "reason_message": "The DT was suspended because an input DT had 5 consecutive refresh errors", |                 |                |
|                    |               |             |    "state": "SUSPENDED",                                                                          |                 |                |
|                    |               |             |    "suspended_on": "2025-04-14 11:49:09.576 Z"                                                    | USER_DEFINED    | 60             |
|                    |               |             |  }                                                                                                |                 |                |
| MY_DYNAMIC_TABLE_2 | MY_DB_2       | MY_SCHEMA_2 | null                                                                                              |                 |                |
+--------------------+------------------------------+--------------------------------------------------------------------------------------------------+-----------------+----------------|
```

The following example retrieves the state and information about each state for refresh for all dynamic tables in the account.

```sqlexample
-- latest_data_timestamp is the refresh timestamp associated with last successful refresh.
SELECT
  name,
  last_completed_refresh_state,
  last_completed_refresh_state_code,
  last_completed_refresh_state_message,
  latest_data_timestamp,
  time_within_target_lag_ratio,
  maximum_lag_sec,
  executing_refresh_query_id
FROM
  TABLE (
    INFORMATION_SCHEMA.DYNAMIC_TABLES ()
  )
ORDER BY
  name;
```

```output
-- Both dynamic tables in the example below have a target lag of one minute.

+--------------------+------------------------------+-----------------------------------+-----------------------------------------------+-----------------------+------------------------------+-----------------+----------------------------+
| NAME               | LAST_COMPLETED_REFRESH_STATE | LAST_COMPLETED_REFRESH_STATE_CODE | LAST_COMPLETED_REFRESH_STATE_MESSAGE          | LATEST_DATA_TIMESTAMP | TIME_WITHIN_TARGET_LAG_RATIO | MAXIMUM_LAG_SEC | EXECUTING_REFRESH_QUERY_ID |
|--------------------+------------------------------+-----------------------------------+-----------------------------------------------|-----------------------+------------------------------+-----------------+----------------------------+
| MY_DYNAMIC_TABLE_1 | UPSTREAM_FAILED              | UPSTREAM_FAILURE                  | Skipped refreshing because an input DT failed | 2025-04-12 09:00:48   | null                         | null            | null                       |
| MY_DYNAMIC_TABLE_2 | SUCCEEDED                    | SUCCESS                           | null                                          | 2025-04-12 09:01:36   | 0.999                        | 125             | null                       |
+--------------------+------------------------------+-----------------------------------+-----------------------------------------------+-----------------------+------------------------------+-----------------+----------------------------+
```

### Monitor all the refreshes for a specific dynamic table

You can use Snowsight or the DYNAMIC_TABLES_REFRESH_HISTORY table function to view the refresh history for a given dynamic table.

SnowsightSQL

1. Sign in to [Snowsight](ui-snowsight-gs.md).
2. In the navigation menu, select Transformation » Dynamic tables.
3. Select your dynamic table and then go to the Refresh History tab.

   This page displays your dynamic table’s refresh history, which includes information about each refresh’s status, duration, and actual
   lag time, and the number of rows changed with each refresh.

   It also displays your dynamic table’s lag metrics, which includes the percentage of the time within the target lag and the longest
   actual lag time during the given interval.

To view the refresh history for a specific dynamic table, use the [DYNAMIC_TABLE_REFRESH_HISTORY](../sql-reference/functions/dynamic_table_refresh_history.md) table
function.

For example, if you want to view the refresh history for all the dynamic tables in the `my_db` database and `my_schema` schema, execute
the following statement:

```sqlexample
SELECT
  name,
  data_timestamp,
  state,
  state_code,
  state_message
    FROM TABLE (INFORMATION_SCHEMA.DYNAMIC_TABLE_REFRESH_HISTORY (NAME_PREFIX => 'MY_DB.MY_SCHEMA')) ORDER BY data_timestamp desc;
```

```output
+--------------------+---------------------+-----------+------------------------------+----------------------------------------------------------------+
| NAME               | DATA_TIMESTAMP      | STATE     | STATE_CODE                   | STATE_MESSAGE                                                  |
|--------------------+---------------------+-----------+------------------------------+----------------------------------------------------------------|
| MY_DYNAMIC_TABLE_1 | 2025-04-12 09:01:36 | SKIPPED   | SKIP_DUE_TO_UPSTREAM_FAILURE | Skipped refreshing because an input DT failed.                 |
| MY_DYNAMIC_TABLE_1 | 2025-04-12 09:00:48 | SUCCEEDED |                              |                                                                |
| MY_DYNAMIC_TABLE_1 | 2025-04-12 09:00:00 | FAILED    | 100038                       | Numeric value 'Good' is not recognized.                        |
| MY_DYNAMIC_TABLE_2 | 2025-04-12 09:01:36 | SUCCEEDED |                              |                                                                |
| MY_DYNAMIC_TABLE_2 | 2025-04-12 09:00:48 | FAILED    | 091930                       | SQL compilation error: Change tracking is not enabled or has   |
|                    |                     |           |                              | been missing for the time range requested on table 'MY_TABLE'. |
| MY_DYNAMIC_TABLE_2 | 2025-04-12 09:00:00 | CANCELLED | 002724                       | Dynamic Table refresh job cancelled.                           |
+--------------------+---------------------+-----------+------------------------------+----------------------------------------------------------------+
```

To filter for refreshes that had errors, pass in the argument `ERROR_ONLY => TRUE`. For example:

```sqlexample
SELECT
  name,
  data_timestamp,
  state,
  state_code,
  state_message
    FROM TABLE (INFORMATION_SCHEMA.DYNAMIC_TABLE_REFRESH_HISTORY (NAME_PREFIX => 'MY_DB.MY_SCHEMA', ERROR_ONLY => TRUE));
```

```output
+--------------------+---------------------+-----------+------------------------------+----------------------------------------------------------------+
| NAME               | DATA_TIMESTAMP      | STATE     | STATE_CODE                   | STATE_MESSAGE                                                  |
|--------------------+---------------------+-----------+------------------------------+----------------------------------------------------------------|
| MY_DYNAMIC_TABLE_1 | 2025-04-12 09:00:00 | FAILED    | 100038                       | Numeric value 'Good' is not recognized.                        |
| MY_DYNAMIC_TABLE_2 | 2025-04-12 09:00:48 | FAILED    | 091930                       | SQL compilation error: Change tracking is not enabled or has   |
|                    |                     |           |                              | been missing for the time range requested on table 'MY_TABLE'. |
| MY_DYNAMIC_TABLE_2 | 2025-04-12 09:00:00 | CANCELLED | 002724                       | Dynamic Table refresh job cancelled.                           |
+--------------------+---------------------+-----------+------------------------------+----------------------------------------------------------------+
```
