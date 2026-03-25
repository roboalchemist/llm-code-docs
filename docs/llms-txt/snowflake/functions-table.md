# Source: https://docs.snowflake.com/en/sql-reference/functions-table.md

# Table functions

A table function returns a set of rows for each input row. The returned set can contain zero, one, or more rows. Each row can
contain one or more columns.

Table functions are sometimes called “tabular functions”.

## What are table functions?

Table functions are typically used when a function returns multiple rows for each individual input.

Each time that a table function is called, it can return a different number of rows. For example, a function
`record_high_temperatures_for_date()`, which returns a list of record high temperatures for a specified date, might
return 0 rows on April 10, 1 row on June 10, and 40 rows on August 20.

### Simple examples of table functions

The following are appropriate as table functions:

* A function that accepts an account number and a date, and returns all charges billed to that account on that date.
  (More than one charge might have been billed on a particular date.)
* A function that accepts a user ID and returns the database roles assigned to that user.
  (A user might have multiple roles, including “sysadmin” and “useradmin”.)

### Functions in which each output row depends upon multiple input rows

Table functions can be grouped into two categories based on the number of input rows that affect each output row:

* 1-to-N
* M-to-N

The functions described earlier are 1-to-N table functions: each output row depends upon only one input row. For example, a
function `record_high_temperatures_for_date()` might produce multiple output rows (one for each city that hit a record on
that date). Each output row for a specific input date depends only on that date; each output row is independent of the rows for
every other date.

Snowflake also supports M-to-N table functions: each output row can depend upon multiple input rows. For example, if a function
generates a moving average of stock prices, that function uses stock prices from multiple input rows (multiple dates) to generate
each output row.

More generally, in an M-to-N function, a group of M input rows produces a group of N output rows. M can be one or more rows.
N can be zero, one, or more rows.

For example, in a 10-day moving average, M is 10. N is 1 because each group of 10 input rows produces one average price.

### Built-in table functions vs user-defined table functions

Snowflake provides hundreds of built-in functions, many of which are table functions. Built-in table functions are listed in
System-Defined Table Functions.

Users can also write their own functions, called user-defined functions or “UDFs”. Some UDFs are scalar; some are tabular.
User-defined table functions are called “UDTFs”. For information about UDFs (including UDTFs), see
[User-defined functions overview](../developer-guide/udf/udf-overview.md).

Built-in table functions and user-defined table functions generally follow the same rules; for example, they are called the same way
from SQL statements.

## Using a table function

### Using a table function in the FROM clause

A table contains a set of rows. Similarly, a table function returns a set of rows. Both tables and table functions are used in
contexts that expect a set of rows. Specifically, table functions are used in the [FROM](constructs/from.md) clause of a
SQL statement.

To help the SQL compiler recognize a table function as a source of rows, Snowflake requires that the table function call be
wrapped by the `TABLE()` keyword.

For example, the following statement calls a table function named `record_high_temperatures_for_date()`, which takes a DATE
value as an argument:

> ```sqlexample
> SELECT city_name, temperature
>     FROM TABLE(record_high_temperatures_for_date('2021-06-27'::DATE))
>     ORDER BY city_name;
> ```

For more information about the syntax of `TABLE()`, see [Table literals](literals-table.md).

Table functions, like functions in general, can accept zero, one, or multiple input arguments in each invocation. Each argument
must be a scalar expression.

For more details about the syntax of table function calls, see Syntax (in this topic).

### Using a table as input to a table function

The argument to a table function can be a literal or an expression, such as a column of a table.
For example, the SELECT statement below passes values from a table as arguments to a table function:

```sqlexample
CREATE OR REPLACE table dates_of_interest (event_date DATE);
INSERT INTO dates_of_interest (event_date) VALUES
    ('2021-06-21'::DATE),
    ('2022-06-21'::DATE);

CREATE OR REPLACE FUNCTION record_high_temperatures_for_date(d DATE)
    RETURNS TABLE (event_date DATE, city VARCHAR, temperature NUMBER)
    as
    $$
    SELECT d, 'New York', 65.0
    UNION ALL
    SELECT d, 'Los Angeles', 69.0
    $$;
```

```sqlexample
SELECT
        doi.event_date as "Date",
        record_temperatures.city,
        record_temperatures.temperature
    FROM dates_of_interest AS doi,
         TABLE(record_high_temperatures_for_date(doi.event_date)) AS record_temperatures
      ORDER BY doi.event_date, city;
+------------+-------------+-------------+
| Date       | CITY        | TEMPERATURE |
|------------+-------------+-------------|
| 2021-06-21 | Los Angeles |          69 |
| 2021-06-21 | New York    |          65 |
| 2022-06-21 | Los Angeles |          69 |
| 2022-06-21 | New York    |          65 |
+------------+-------------+-------------+
```

The arguments to a table function can come from other table-like sources, including views and other table functions.

## List of system-defined table functions

Snowflake provides the following system-defined (i.e. built-in) table functions:

| Sub-category | Function | Notes |
| --- | --- | --- |
| Data Loading | [INFER_SCHEMA](functions/infer_schema.md) | For more information, see [Load data into Snowflake](../guides-overview-loading-data.md). |
|  | [VALIDATE](functions/validate.md) |  |
| Data Generation | [GENERATOR](functions/generator.md) |  |
| Data Conversion | [SPLIT_TO_TABLE](functions/split_to_table.md) |  |
|  | [STRTOK_SPLIT_TO_TABLE](functions/strtok_split_to_table.md) |  |
| Differential Privacy | [CUMULATIVE_PRIVACY_LOSSES](functions/cumulative_privacy_losses.md) |  |
| Object Modeling | [GET_OBJECT_REFERENCES](functions/get_object_references.md) |  |
| Parameterized Queries | [TO_QUERY](functions/to_query.md) |  |
| Semi-structured Queries | [FLATTEN](functions/flatten.md) | For more information, see [Querying Semi-structured Data](../user-guide/querying-semistructured.md). |
| Query Results | [RESULT_SCAN](functions/result_scan.md) | Can be used to perform SQL operations on the output from another SQL operation (e.g. SHOW). |
| Query Profile | [GET_QUERY_OPERATOR_STATS](functions/get_query_operator_stats.md) |  |
| Historical & Usage Information |  | Includes:   *[Snowflake Information Schema](info-schema.md)* [Account Usage](account-usage.md) * [LOCAL schema](local.md) |
| User Login | [LOGIN_HISTORY , LOGIN_HISTORY_BY_USER](functions/login_history.md) |  |
| Queries | [QUERY_HISTORY , QUERY_HISTORY_BY_\*](functions/query_history.md) |  |
|  | [QUERY_ACCELERATION_HISTORY](functions/query_acceleration_history.md) | For more information, see [Using the Query Acceleration Service (QAS)](../user-guide/query-acceleration-service.md). |
| Warehouse & Storage Usage | [DATABASE_STORAGE_USAGE_HISTORY](functions/database_storage_usage_history.md) |  |
|  | [WAREHOUSE_LOAD_HISTORY](functions/warehouse_load_history.md) |  |
|  | [WAREHOUSE_METERING_HISTORY](functions/warehouse_metering_history.md) |  |
|  | [STAGE_STORAGE_USAGE_HISTORY](functions/stage_storage_usage_history.md) |  |
| Storage Lifecycle Policies | [STORAGE_LIFECYCLE_POLICY_HISTORY](functions/storage_lifecycle_policy_history.md) | Information Schema table function. For more information, see [Storage lifecycle policies](../user-guide/storage-management/storage-lifecycle-policies.md). |
| Column-level & Row-level Security | [POLICY_REFERENCES](functions/policy_references.md) |  |
| Object Tagging | [TAG_REFERENCES](functions/tag_references.md) | Information Schema table function. |
|  | [TAG_REFERENCES_ALL_COLUMNS](functions/tag_references_all_columns.md) | Information Schema table function. |
|  | [TAG_REFERENCES_WITH_LINEAGE](functions/tag_references_with_lineage.md) | Account Usage table function. |
| Account Replication | [REPLICATION_GROUP_DANGLING_REFERENCES](functions/replication_group_dangling_references.md) | For more information, see [Introduction to replication and failover across multiple accounts](../user-guide/account-replication-intro.md) |
|  | [REPLICATION_GROUP_REFRESH_HISTORY, REPLICATION_GROUP_REFRESH_HISTORY_ALL](functions/replication_group_refresh_history.md) |  |
|  | [REPLICATION_GROUP_REFRESH_PROGRESS, REPLICATION_GROUP_REFRESH_PROGRESS_BY_JOB, REPLICATION_GROUP_REFRESH_PROGRESS_ALL](functions/replication_group_refresh_progress.md) |  |
|  | [REPLICATION_GROUP_USAGE_HISTORY](functions/replication_group_usage_history.md) |  |
| Alerts | [ALERT_HISTORY](functions/alert_history.md) | For more information, see [Setting up alerts based on data in Snowflake](../user-guide/alerts.md). |
|  | [SERVERLESS_ALERT_HISTORY](functions/serverless_alert_history.md) |  |
| Bind variables | [BIND_VALUES](functions/bind_values.md) | For more information, see [Retrieve bind variable values](bind-variables.md). |
| Database Replication | [DATABASE_REFRESH_HISTORY](functions/database_refresh_history.md) | For more information, see [Replicating databases across multiple accounts](../user-guide/db-replication-config.md). |
|  | [DATABASE_REFRESH_PROGRESS , DATABASE_REFRESH_PROGRESS_BY_JOB](functions/database_refresh_progress.md) |  |
|  | [DATABASE_REPLICATION_USAGE_HISTORY](functions/database_replication_usage_history.md) |  |
| Data Loading & Transfer | [COPY_HISTORY](functions/copy_history.md) |  |
|  | [DATA_TRANSFER_HISTORY](functions/data_transfer_history.md) |  |
|  | [PIPE_USAGE_HISTORY](functions/pipe_usage_history.md) |  |
|  | [STAGE_DIRECTORY_FILE_REGISTRATION_HISTORY](functions/stage_directory_file_registration_history.md) |  |
|  | [VALIDATE_PIPE_LOAD](functions/validate_pipe_load.md) |  |
| Data Clustering (within Tables) | [AUTOMATIC_CLUSTERING_HISTORY](functions/automatic_clustering_history.md) | For more information, see [Automatic Clustering](../user-guide/tables-auto-reclustering.md). |
| dbt Projects on Snowflake | [DBT_PROJECT_EXECUTION_HISTORY](functions/dbt_project_execution_history.md) | For more information, see [dbt Projects on Snowflake](../user-guide/data-engineering/dbt-projects-on-snowflake.md). |
| Dynamic Tables | [DYNAMIC_TABLES](functions/dynamic_tables.md) | For more information, see [Create dynamic tables](../user-guide/dynamic-tables-create.md). |
|  | [DYNAMIC_TABLE_GRAPH_HISTORY](functions/dynamic_table_graph_history.md) |  |
|  | [DYNAMIC_TABLE_REFRESH_HISTORY](functions/dynamic_table_refresh_history.md) |  |
| External Functions | [EXTERNAL_FUNCTIONS_HISTORY](functions/external_functions_history.md) | For more information, see [Writing external functions](external-functions.md). |
| External Tables | [AUTO_REFRESH_REGISTRATION_HISTORY](functions/auto_refresh_registration_history.md) | For more information, see [Introduction to external tables](../user-guide/tables-external-intro.md). |
|  | [EXTERNAL_TABLE_FILES](functions/external_table_files.md) |  |
|  | [EXTERNAL_TABLE_FILE_REGISTRATION_HISTORY](functions/external_table_registration_history.md) |  |
| Iceberg Tables | [ICEBERG_TABLE_FILES](functions/iceberg_table_files.md) | Information Schema table function. |
|  | [ICEBERG_TABLE_SNAPSHOT_REFRESH_HISTORY](functions/iceberg_table_snapshot_refresh_history.md) | Information Schema table function. |
| Listings | [AVAILABLE_LISTINGS](functions/available_listings.md) |  |
|  | [AVAILABLE_LISTING_REFRESH_HISTORY](functions/available_listing_refresh_history.md) |  |
|  | [LISTING_REFRESH_HISTORY](functions/listing_refresh_history.md) |  |
| Materialized Views Maintenance | [MATERIALIZED_VIEW_REFRESH_HISTORY](functions/materialized_view_refresh_history.md) | For more information, see [Working with Materialized Views](../user-guide/views-materialized.md). |
| Machine learning | [ONLINE_FEATURE_TABLE_REFRESH_HISTORY](functions/online-feature-table-refresh-history.md) | For more information, see [Feature store commands](commands-feature-store.md). |
| Notifications | [NOTIFICATION_HISTORY](functions/notification_history.md) | For more information, see [Using SYSTEM$SEND_EMAIL to send email notifications](../user-guide/notifications/email-stored-procedures.md). |
| SCIM Maintenance | [REST_EVENT_HISTORY](functions/rest_event_history.md) | For more information, see [Auditing SCIM API requests](../user-guide/scim-intro.md) |
| Search Optimization Maintenance | [SEARCH_OPTIMIZATION_HISTORY](functions/search_optimization_history.md) | For more information, see [Search optimization service](../user-guide/search-optimization-service.md). |
| Streams | [SYSTEM$STREAM_BACKLOG](functions/system_stream_backlog.md) | For more information, see [Introduction to streams](../user-guide/streams-intro.md). |
| Tasks | [COMPLETE_TASK_GRAPHS](functions/complete_task_graphs.md) | For more information, see [Introduction to tasks](../user-guide/tasks-intro.md). |
|  | [CURRENT_TASK_GRAPHS](functions/current_task_graphs.md) |  |
|  | [SERVERLESS_TASK_HISTORY](functions/serverless_task_history.md) |  |
|  | [TASK_DEPENDENTS](functions/task_dependents.md) |  |
|  | [TASK_HISTORY](functions/task_history.md) |  |
| Network rules | [NETWORK_RULE_REFERENCES](functions/network_rule_references.md) | Information Schema table function. For details, see [Network rules](../user-guide/network-rules.md). |
| Data Quality | [DATA_METRIC_FUNCTION_EXPECTATIONS](functions/data_metric_function_expectations.md) |  |
|  | [DATA_METRIC_FUNCTION_REFERENCES](functions/data_metric_function_references.md) |  |
|  | [DATA_QUALITY_MONITORING_EXPECTATION_STATUS](functions/data_quality_monitoring_expectation_status.md) |  |
|  | [DATA_QUALITY_MONITORING_RESULTS](functions/data_quality_monitoring_results.md) |  |
|  | [SYSTEM$DATA_METRIC_SCAN](functions/system_data_metric_scan.md) |  |
|  | [SYSTEM$EVALUATE_DATA_QUALITY_EXPECTATIONS](functions/system_evaluate_data_quality_expectations.md) |  |
| Data Lineage | [GET_LINEAGE (SNOWFLAKE.CORE)](functions/get_lineage-snowflake-core.md) | For more information, see [Data Lineage](../user-guide/ui-snowsight-lineage.md). |
| Cortex Search | [CORTEX_SEARCH_DATA_SCAN](functions/cortex_search_data_scan.md) | For more information, see [Cortex Search](../user-guide/snowflake-cortex/cortex-search/cortex-search-overview.md). |
|  | [CORTEX_SEARCH_REFRESH_HISTORY](functions/cortex_search_refresh_history.md) |  |
| Contacts | [GET_CONTACTS](functions/get_contacts.md) |  |
| Snowpark Container Services | [GET_JOB_HISTORY](functions/get_job_history.md) | For more information, see [Snowpark Container Services: Monitoring Services](../developer-guide/snowpark-container-services/monitoring-services.md). |
|  | [<service_name>!SPCS_GET_EVENTS](functions/spcs_get_events.md) |  |
|  | [<service_name>!SPCS_GET_LOGS](functions/spcs_get_logs.md) |  |
|  | [<service_name>!SPCS_GET_METRICS](functions/spcs_get_metrics.md) |  |
| Snowflake Native Apps | [APPLICATION_CALLBACK_HISTORY](functions/application_callback_history.md) | For more information, see [Callbacks](../developer-guide/native-apps/callbacks.md). |
|  | [APPLICATION_SPECIFICATION_STATUS_HISTORY](functions/application_specification_status_history.md) | For more information, see [Overview of app specifications](../developer-guide/native-apps/requesting-app-specs.md). |
|  | [APPLICATION_CONFIGURATION_VALUE_HISTORY](functions/application_configuration_value_history.md) | For more information, see [Application configuration](../developer-guide/native-apps/app-configuration.md). |

## Syntax

```sqlsyntax
SELECT ...
  FROM [ <input_table> [ [AS] <alias_1> ] ,
         [ LATERAL ]
       ]
       TABLE( <table_function>( [ <arg_1> [, ... ] ] ) ) [ [ AS ] <alias_2> ];
```

For function-specific syntax, see the documentation for the individual system-defined table functions.

## Usage notes

* Table functions can also be applied to a set of rows using the LATERAL construct.
* To enable using table expressions, Snowflake supports ANSI/ISO standard syntax for table expressions in the [FROM](constructs/from.md) clause of queries and subqueries. This syntax is used to
  indicate that an expression returns a collection of rows instead of a single row.
* This ANSI/ISO syntax is valid only in the [FROM](constructs/from.md) clause of the [SELECT](sql/select.md) list. You cannot omit these keywords and parentheses from a
  collection subquery specification in any other context.
