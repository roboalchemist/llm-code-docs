# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/query_history.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/query_history.md

# Source: https://docs.snowflake.com/en/sql-reference/functions/query_history.md

Categories:
:   [Information Schema](../info-schema.md) , [Table functions](../functions-table.md)

# QUERY_HISTORY , QUERY_HISTORY_BY_\*

You can use the QUERY_HISTORY family of table functions to query Snowflake query history along various dimensions:

* QUERY_HISTORY returns queries within a specified time range.
* QUERY_HISTORY_BY_SESSION returns queries within a specified session and time range.
* QUERY_HISTORY_BY_USER returns queries submitted by a specified user within a specified time range.
* QUERY_HISTORY_BY_WAREHOUSE returns queries executed by a specified warehouse within a specified time range.

Each function is optimized for querying along the specified dimension. The results can be further filtered using SQL predicates.

See also:

> [QUERY_HISTORY view](../account-usage/query_history.md) (Account Usage)
> [Monitor query activity with Query History](../../user-guide/ui-snowsight-activity.md) (Snowsight dashboard)

## Syntax

```sqlsyntax
QUERY_HISTORY(
      [ END_TIME_RANGE_START => <constant_expr> ]
      [, END_TIME_RANGE_END => <constant_expr> ]
      [, RESULT_LIMIT => <num> ]
      [, INCLUDE_CLIENT_GENERATED_STATEMENT => <boolean_expr> ] )

QUERY_HISTORY_BY_SESSION(
      [ SESSION_ID => <constant_expr> ]
      [, END_TIME_RANGE_START => <constant_expr> ]
      [, END_TIME_RANGE_END => <constant_expr> ]
      [, RESULT_LIMIT => <num> ]
      [, INCLUDE_CLIENT_GENERATED_STATEMENT => <boolean_expr> ] )

QUERY_HISTORY_BY_USER(
      [ USER_NAME => '<string>' ]
      [, END_TIME_RANGE_START => <constant_expr> ]
      [, END_TIME_RANGE_END => <constant_expr> ]
      [, RESULT_LIMIT => <num> ]
      [, INCLUDE_CLIENT_GENERATED_STATEMENT => <boolean_expr> ] )

QUERY_HISTORY_BY_WAREHOUSE(
      [ WAREHOUSE_NAME => '<string>' ]
      [, END_TIME_RANGE_START => <constant_expr> ]
      [, END_TIME_RANGE_END => <constant_expr> ]
      [, RESULT_LIMIT => <num> ]
      [, INCLUDE_CLIENT_GENERATED_STATEMENT => <boolean_expr> ] )
```

## Arguments

All the arguments are optional.

`END_TIME_RANGE_START => constant_expr` , . `END_TIME_RANGE_END => constant_expr`
:   Time range (in TIMESTAMP_LTZ format), within the last 7 days, in which the query completed running:

    * If `END_TIME_RANGE_END` is not specified, the function returns all queries, including those that are still running.
    * If `END_TIME_RANGE_END` is [CURRENT_TIMESTAMP](current_timestamp.md), the function returns only those queries that have completed.

    If the time range does not fall within the last 7 days, an error is returned.

    > **Note:**
    >
    > If no start or end time is specified, the most recent queries are returned, up to the specified limit.

`SESSION_ID => constant_expr`
:   Applies only to QUERY_HISTORY_BY_SESSION

    The numeric identifier for a session or [CURRENT_SESSION](current_session.md). Only queries from the specified session are returned.

    Default: [CURRENT_SESSION](current_session.md)

`USER_NAME => 'string'`
:   Applies only to QUERY_HISTORY_BY_USER

    A string specifying a user login name or [CURRENT_USER](current_user.md). Only queries run by the specified user are returned. Note that the login name must be enclosed in single quotes. Also, if the
    login name contains any spaces, mixed-case characters, or special characters, the name must be double-quoted within the single quotes (e.g. `'"User 1"'` vs `'user1'`).
    You cannot specify `SYSTEM` (`USER_NAME =>'SYSTEM'`), which is a background service rather than a user. However, you can filter on `user_name='SYSTEM'` when you run queries against QUERY_HISTORY table functions.

    Default: [CURRENT_USER](current_user.md)

`WAREHOUSE_NAME => 'string'`
:   Applies only to QUERY_HISTORY_BY_WAREHOUSE

    A string specifying a warehouse name or [CURRENT_WAREHOUSE](current_warehouse.md). Only queries executed by that warehouse are returned. Note that the warehouse name must be enclosed in single quotes. Also, if the
    warehouse name contains any spaces, mixed-case characters, or special characters, the name must be double-quoted within the single quotes (e.g. `'"My Warehouse"'` vs `'mywarehouse'`).

    Default: [CURRENT_WAREHOUSE](current_warehouse.md)

`RESULT_LIMIT => num`
:   A number specifying the maximum number of rows returned by the function:

    If the number of matching rows is greater than this limit, the queries with the most recent end time (or those that are still executing) are returned, up to the specified limit.

    Range: `1` to `10000`

    Default: `100`.

    > **Note:**
    >
    > When you select from a QUERY_HISTORY table function, the time range and RESULT_LIMIT arguments
    > are applied *first*, followed by the WHERE clause. To apply a filter on a larger range of
    > queries, increase the RESULT_LIMIT value.

`INCLUDE_CLIENT_GENERATED_STATEMENT => 'boolean_expr'`
:   Specifies whether client-generated statements are included in table function queries (given the value of the `is_client_generated_statement` column).

    Default: `FALSE`.

    The ACCOUNT_USAGE [QUERY_HISTORY view](../account-usage/query_history.md) also contains an `is_client_generated_statement` column, but queries of this view return all statements, whether or not they are client-generated. If necessary, you can filter the query result.

## Usage notes

* Returns queries run by the current user. Also returns queries run by any user when the executing role, or a higher role in a hierarchy, has either of the following privileges:

  * The MONITOR or OPERATE privilege on the user-managed warehouses where the queries were run.
  * The MONITOR or OPERATE privilege on the task. Exception: If the task executes an owner’s right stored procedure or UDF, the role requires at least MONITOR privilege on the warehouse on which the task executed to view the stored procedure query and the UDF query.
  * The MONITOR EXECUTION privilege on the account in which the task resides.
  * Exceptions: Neither [stored procedures](../../developer-guide/stored-procedure/stored-procedures-overview.md) nor [user-defined functions (UDFs)](../../developer-guide/udf/udf-overview.md) can run this query.

  For more information, see [Virtual warehouse privileges](../../user-guide/security-access-control-privileges.md).
* When you call an Information Schema table function, your session must use the INFORMATION_SCHEMA, *or* the function name must be fully-qualified. For more information, see [Snowflake Information Schema](../info-schema.md).
* The values for the columns `external_function_total_invocations`, `external_function_total_sent_rows`,
  `external_function_total_received_rows`, `external_function_total_sent_bytes`, and `external_function_total_received_bytes`
  are affected by many factors, including:

  * The number of external functions in the SQL statement.
  * The number of rows per batch sent to each remote service.
  * The number of retries due to transient errors (e.g. because a response was not received within the expected time).
* Canceled queries are identified by their `error_message` text (`SQL execution canceled`), not by their `execution_status` value.
* When you select from a QUERY_HISTORY table function, the function arguments (time range, RESULT_LIMIT)
  are applied first to retrieve rows, followed by any WHERE and LIMIT clauses in your query.
  For example, if RESULT_LIMIT is set to 100 (the default), the WHERE clause applies only to the most recent
  100 queries. To search a larger range of queries before filtering, increase the RESULT_LIMIT value.

### Query retry columns

A query might need to be retried one or more times in order to successfully complete. There can be multiple causes that result in a query
retry. Some of these causes are *actionable*, that is, a user can make changes to reduce or eliminate query retries for a specific query.
For example, if a query is retried due to an out of memory error, modifying warehouse settings might resolve the issue.

Some query retries are caused by a fault that is not actionable. That is, there is no change a user can make to prevent the
query retry. For example, a network outage might result in a query retry. In this case, there is no change to the query or to the
warehouse that executes it that can prevent the query retry.

The QUERY_RETRY_TIME, QUERY_RETRY_CAUSE, and FAULT_HANDLING_TIME columns can help you optimize queries that are retried and better
understand fluctuations in query performance.

## Output

The function returns the following columns:

| Column Name | Data Type | Description |
| --- | --- | --- |
| `query_id` | VARCHAR | The statement’s unique id. |
| `query_text` | VARCHAR | Text of the SQL statement. |
| `database_name` | VARCHAR | Database that was specified in the context of the query at compilation. |
| `schema_name` | VARCHAR | Schema that was specified in the context of the query at compilation. |
| `query_type` | VARCHAR | DML, query, etc. If the query is currently running, or the query failed, then the query type may be UNKNOWN. |
| `session_id` | NUMBER | Session that executed the statement. |
| `authn_event_id` | NUMBER | ID for the event for the authentication of the user for this query. This ID corresponds to the value in the `event_id` column in the [LOGIN_HISTORY](../account-usage/login_history.md) view. ^ |
| `user_name` | VARCHAR | User who issued the query. |
| `user_type` | VARCHAR | The type of user executing the query. It’s the same as the `type` column in the [USERS view](../account-usage/users.md). If a Snowpark Container Services service executes the query, the user type is SNOWFLAKE_SERVICE (see [Access service user query history](../../developer-guide/snowpark-container-services/spcs-execute-sql.md)). |
| `user_database_name` | VARCHAR | When the value in the `user_type` column is SNOWFLAKE_SERVICE, it specifies the service’s database name; otherwise, it’s NULL. |
| `user_schema_name` | VARCHAR | When the value in the `user_type` column is SNOWFLAKE_SERVICE, it specifies the service’s schema name; otherwise, it’s NULL. |
| `role_name` | VARCHAR | Role that was active in the session at the time of the query. |
| `warehouse_name` | VARCHAR | Warehouse that the query executed on, if any. |
| `warehouse_size` | VARCHAR | Size of the warehouse when this statement executed. |
| `warehouse_type` | VARCHAR | Type of the warehouse when this statement executed. |
| `cluster_number` | NUMBER | The cluster (in a multi-cluster warehouse) that this statement executed on. |
| `query_tag` | VARCHAR | Query tag set for this statement through the QUERY_TAG session parameter. |
| `execution_status` | VARCHAR | Execution status for the query: resuming_warehouse, running, queued, blocked, success, failed_with_error, or failed_with_incident. |
| `error_code` | NUMBER | Error code, if the query returned an error |
| `error_message` | VARCHAR | Error message, if the query returned an error |
| `start_time` | TIMESTAMP_LTZ | Statement start time |
| `end_time` | TIMESTAMP_LTZ | Statement end time. If the query is still running, the `end_time` is the UNIX epoch timestamp (“1970-01-01 00:00:00”), adjusted for the local time zone. E.g. for Pacific Standard Time, this would be “1969-12-31 16:00:00.000 -0800”. |
| `total_elapsed_time` | NUMBER | Elapsed time (in milliseconds) |
| `bytes_scanned` | NUMBER | Number of bytes scanned by this statement. |
| `rows_produced` | NUMBER | Number of rows produced by this statement. |
| `compilation_time` | NUMBER | Compilation time (in milliseconds) |
| `execution_time` | NUMBER | Execution time (in milliseconds) |
| `queued_provisioning_time` | NUMBER | Time (in milliseconds) spent in the warehouse queue, waiting for the warehouse compute resources to provision, due to warehouse creation, resume, or resize. |
| `queued_repair_time` | NUMBER | Time (in milliseconds) spent in the warehouse queue, waiting for compute resources in the warehouse to be repaired. |
| `queued_overload_time` | NUMBER | Time (in milliseconds) spent in the warehouse queue, due to the warehouse being overloaded by the current query workload. |
| `transaction_blocked_time` | NUMBER | Time (in milliseconds) spent blocked by a concurrent DML. |
| `outbound_data_transfer_cloud` | VARCHAR | Target cloud provider for statements that unload data to another region and/or cloud. |
| `outbound_data_transfer_region` | VARCHAR | Target region for statements that unload data to another region and/or cloud. |
| `outbound_data_transfer_bytes` | NUMBER | Number of bytes transferred in statements that unload data to another region and/or cloud. |
| `inbound_data_transfer_cloud` | VARCHAR | Source cloud provider for statements that load data from another region and/or cloud. |
| `inbound_data_transfer_region` | VARCHAR | Source region for statements that load data from another region and/or cloud. |
| `inbound_data_transfer_bytes` | NUMBER | Number of bytes transferred in a replication operation from another account. The source account could be in the same region or a different region than the current account. |
| `list_external_file_time` | NUMBER | Time (in milliseconds) spent listing external files. |
| `credits_used_cloud_services` | NUMBER | Number of credits used for cloud services. |
| `release_version` | VARCHAR | Release version in the format of `major_release.minor_release.patch_release`. |
| `external_function_total_invocations` | NUMBER | The aggregate number of times that this query called remote services. For important details, see the Usage Notes. |
| `external_function_total_sent_rows` | NUMBER | The total number of rows that this query sent in all calls to all remote services. |
| `external_function_total_received_rows` | NUMBER | The total number of rows that this query received from all calls to all remote services. |
| `external_function_total_sent_bytes` | NUMBER | The total number of bytes that this query sent in all calls to all remote services. |
| `external_function_total_received_bytes` | NUMBER | The total number of bytes that this query received from all calls to all remote services. |
| `is_client_generated_statement` | BOOLEAN | Indicates whether the query was client-generated. |
| `query_hash` | VARCHAR | The [hash value](../../user-guide/query-hash.md) computed based on the canonicalized SQL text. |
| `query_hash_version` | NUMBER | The [version of the logic](../../user-guide/query-hash.md) used to compute `QUERY_HASH`. |
| `query_parameterized_hash` | VARCHAR | The [hash value](../../user-guide/query-hash.md) computed based on the parameterized query. |
| `query_parameterized_hash_version` | NUMBER | The [version of the logic](../../user-guide/query-hash.md) used to compute `QUERY_PARAMETERIZED_HASH`. |
| `transaction_id` | NUMBER | [ID of the transaction](../transactions.md) that contains the statement or `0` if the statement is not executed within a transaction. |
| `query_acceleration_bytes_scanned` | NUMBER | Number of bytes scanned by the [query acceleration service](../../user-guide/query-acceleration-service.md). |
| `query_acceleration_partitions_scanned` | NUMBER | Number of partitions scanned by the query acceleration service. |
| `query_acceleration_upper_limit_scale_factor` | NUMBER | Upper limit [scale factor](../../user-guide/query-acceleration-service.md) that a query would have benefited from. |
| `bytes_written_to_result` | NUMBER | Number of bytes written to a result object. For example, `SELECT * FROM ...` would produce a set of results in tabular format representing each field in the selection. . . In general, the results object represents whatever is produced as a result of the query, and `bytes_written_to_result` represents the size of the returned result. |
| `rows_written_to_result` | NUMBER | Number of rows written to a result object. For CREATE TABLE AS SELECT (CTAS) and all DML operations, this result is `1`. |
| `rows_inserted` | NUMBER | Number of rows inserted by the query. |
| `query_retry_time` | NUMBER | Total execution time (in milliseconds) for query retries caused by actionable errors. For more information, see Query retry columns. |
| `query_retry_cause` | VARCHAR | Error that caused the query to retry. If there is no query retry, the field is NULL. For more information, see Query retry columns. |
| `fault_handling_time` | NUMBER | Total execution time (in milliseconds) for query retries caused by errors that are *not* actionable. For more information, see Query retry columns. |
| `bind_values` | ARRAY | Bind values in serialized form. If the query contains no bind values, then this column contains an empty array. If the array is too large or the [ALLOW_BIND_VALUES_ACCESS](../parameters.md) parameter is set to `FALSE`, this column contains NULL. For more information, see [Retrieve bind variable values](../bind-variables.md). |

The potential values for the `query_type` column include:

* CREATE_USER
* CREATE_ROLE
* CREATE_NETWORK_POLICY
* ALTER_ROLE
* ALTER_NETWORK_POLICY
* ALTER_ACCOUNT
* DROP_SEQUENCE
* DROP_USER
* DROP_ROLE
* DROP_NETWORK_POLICY
* RENAME_NETWORK_POLICY
* REVOKE

## Examples

Retrieve up to the last 100 queries run in the current session:

```sqlexample
SELECT *
  FROM TABLE(INFORMATION_SCHEMA.QUERY_HISTORY_BY_SESSION())
  ORDER BY start_time;
```

Retrieve up to the last 100 queries run by the current user (or run by any user on any warehouse on which the current user has the MONITOR privilege):

```sqlexample
SELECT *
  FROM TABLE(INFORMATION_SCHEMA.QUERY_HISTORY())
  ORDER BY start_time;
```

Retrieve up to the last 100 queries run in the past hour by the current user (or run by any user on any warehouse on which the current user has the MONITOR privilege):

```sqlexample
SELECT *
  FROM TABLE(INFORMATION_SCHEMA.QUERY_HISTORY(DATEADD('hours',-1,CURRENT_TIMESTAMP()),CURRENT_TIMESTAMP()))
  ORDER BY start_time;
```

Retrieve all queries run by the current user (or run by any user on any warehouse on which the current user has the MONITOR privilege) within a specified 30-minute block of time in the past 7 days:

```sqlexample
SELECT *
  FROM TABLE(INFORMATION_SCHEMA.QUERY_HISTORY(
    END_TIME_RANGE_START=>TO_TIMESTAMP_LTZ('2017-12-4 12:00:00.000 -0700'),
    END_TIME_RANGE_END=>TO_TIMESTAMP_LTZ('2017-12-4 12:30:00.000 -0700')));
```

Retrieve the number of client-generated statements that were run against a warehouse named `my_xsmall_wh`:

```sqlexample
SELECT COUNT(*)
  FROM TABLE(INFORMATION_SCHEMA.QUERY_HISTORY_BY_WAREHOUSE(
    WAREHOUSE_NAME => 'my_xsmall_wh',
    INCLUDE_CLIENT_GENERATED_STATEMENT => TRUE));
```
