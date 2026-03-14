# Source: https://docs.snowflake.com/en/sql-reference/functions/dynamic_tables.md

Categories:
:   [Information Schema](../info-schema.md) , [Table functions](../functions-table.md)

# DYNAMIC_TABLES

This table function returns metadata about [dynamic tables](../../user-guide/dynamic-tables-about.md), including aggregate lag metrics and the status of the most recent refreshes, within 7 days
of the current time.

## Syntax

```sqlsyntax
DYNAMIC_TABLES (
  [ NAME => '<string>' ]
  [ , REFRESH_DATA_TIMESTAMP_START => <constant_expr> ]
  [ , RESULT_LIMIT => <integer> ]
  [ , INCLUDE_CONNECTED => { TRUE | FALSE } ]
)
```

## Arguments

All the arguments are optional.
If no arguments are provided, 100 refreshes from all dynamic tables in the account will be returned.

`NAME => 'string'`
:   The name of a dynamic table.

    Names must be single-quoted and are case insensitive.

    You can specify the unqualified name (`dynamic_table_name`),
    the partially qualified name (`schema_name.dynamic_table_name`),
    or the fully qualified name (`database_name.schema_name.dynamic_table_name`).

    For more information on object name resolution, refer to [Object name resolution](../name-resolution.md).

    The function returns the metadata for this table.

`REFRESH_DATA_TIMESTAMP_START => constant_expr`
:   Time (in TIMESTAMP_LTZ format) for computing metrics related to dynamic table target lag. Includes all refreshes with LATEST_DATA_TIMESTAMP greater than or equal to REFRESH_DATA_TIMESTAMP_START.

    Default: All refreshes in refresh history are retained for 7 days.

`RESULT_LIMIT => integer`
:   A number specifying the maximum number of rows returned by the function.

    By default, the function returns 100 rows and the results are sorted by the dynamic table’s last completed refresh state in the following
    order, unless specified otherwise using the RESULT_LIMIT argument.

    1. FAILED
    2. UPSTREAM_FAILED
    3. SKIPPED
    4. SUCCEEDED
    5. CANCELED

    To sort by a different order, you must provide a large enough RESULT_LIMIT value (for example, the maximum value of a signed integer). As
    long as RESULT_LIMIT exceeds the total number of dynamic tables in the account, the results can be sorted using an ORDER BY clause.

    To apply a filter on the results, also specify a large enough RESULT_LIMIT value for the filter to be applied on all dynamic tables.

    **Examples**:

    The following example sorts by a different order of `name` and returns 100 rows:

    ```sqlsyntax
    SELECT * FROM TABLE(INFORMATION_SCHEMA.DYNAMIC_TABLES(result_limit => <max_value>)) ORDER BY name ASC LIMIT 100 ;
    ```

    The following example sorts by a different order of `name` and returns all rows:

    ```sqlsyntax
    SELECT * FROM TABLE(INFORMATION_SCHEMA.DYNAMIC_TABLES(result_limit => <max_value>)) ORDER BY name ASC ;
    ```

    The following example filters for all dynamic tables with 1-minute target lag, uses the default sort, and returns all rows:

    ```sqlsyntax
    SELECT * FROM TABLE(INFORMATION_SCHEMA.DYNAMIC_TABLES(result_limit => <max_value>)) WHERE TARGET_LAG_SEC = 60 ;
    ```

    Range: `1` to `10000`

    Default: `100`.

`INCLUDE_CONNECTED => { TRUE | FALSE }`
:   When set to TRUE, the function returns metadata for all dynamic tables connected to the dynamic table specified by the NAME argument.

    You must specify the NAME argument, you must not specify the RESULT_LIMIT argument.

    Default: `FALSE`

## Output

The function returns the following columns.

To view these columns, you must use a role with the MONITOR privilege. Otherwise, the function only returns a value for `NAME`,
`SCHEMA_NAME`, `DATABASE_NAME`, and `QUALIFIED_NAME`. For more information about dynamic table privileges, see
[Privileges to view a dynamic table’s metadata](../../user-guide/dynamic-tables-privileges.md).

| Column Name | Data Type | Description |
| --- | --- | --- |
| NAME | TEXT | Name of the dynamic table. |
| SCHEMA_NAME | TEXT | Name of the schema that contains the dynamic table. |
| DATABASE_NAME | TEXT | Name of the database that contains the dynamic table. |
| QUALIFIED_NAME | TEXT | Fully qualified name of the dynamic table. |
| TARGET_LAG_SEC | NUMBER | Target lag time in seconds of the dynamic table. This is the value that was specified in the TARGET_LAG parameter of the dynamic table. |
| TARGET_LAG_TYPE | TEXT | The type of target lag. Can be one of the following:   *USER_DEFINED: Determined by the TARGET_LAG parameter specified for the dynamic table.* DOWNSTREAM: Includes a dynamic table with a DOWNSTREAM target lag. |
| SCHEDULING_STATE | OBJECT | OBJECT consisting of:   *STATE (TEXT): Scheduling state (RUNNING or SUSPENDED).* REASON_CODE (TEXT): Specifies the code for the reason why the dynamic table is not running. *REASON_MESSAGE (TEXT): Text description of the reason the dynamic table is not running. Only applies if the dynamic table is not in the RUNNING state.* SUSPENDED_ON (TIMESTAMP_LTZ): Timestamp when the dynamic table was suspended. Only applies if the dynamic table is in the SUSPENDED state. * RESUMED_ON (TIMESTAMP_LTZ): Timestamp when the dynamic table was last resumed. Only applies if dynamic table is in the RUNNING state. |
| MEAN_LAG_SEC | NUMBER | The mean lag time (in seconds) of refreshes for this dynamic table. |
| MAXIMUM_LAG_SEC | NUMBER | The maximum lag time in seconds of refreshes for this dynamic table. |
| TIME_ABOVE_TARGET_LAG_SEC | NUMBER | The time in seconds in the retention period or since the last configuration change, when the actual lag was more than the defined target lag. |
| TIME_WITHIN_TARGET_LAG_RATIO | NUMBER | The ratio of time in the retention period or since the last configuration change, when actual lag is within the target lag. |
| LATEST_DATA_TIMESTAMP | TIMESTAMP_LTZ | Data timestamp of the last successful refresh. |
| LAST_COMPLETED_REFRESH_STATE | TEXT | Status of the last terminated refresh for the dynamic table. Can be one of the following:   *SUCCEEDED: Refresh completed successfully.* FAILED: Refresh failed during execution. *UPSTREAM_FAILED: Refresh not performed due to an upstream failed refresh.* CANCELLED: Refresh was canceled before execution. |
| LAST_COMPLETED_REFRESH_STATE_CODE | TEXT | Code representing the current state of the refresh.  If the LAST_COMPLETED_REFRESH_STATE is FAILED, this column shows the error code associated with the failure. |
| LAST_COMPLETED_REFRESH_STATE_MESSAGE | TEXT | Description of the current state of the refresh.  If the LAST_COMPLETED_REFRESH_STATE is FAILED, this column shows the error message associated with the failure. |
| EXECUTING_REFRESH_QUERY_ID | TEXT | If present, this represents the query ID of the refresh job. If null, there is no refresh job in progress. |

## Usage notes

* When calling an Information Schema table function, the session must have an INFORMATION_SCHEMA schema in use or the function name must be fully-qualified. For more details, see
  [Snowflake Information Schema](../info-schema.md).

## Examples

Retrieve the names, lag information, and data timestamp of the last successful refresh for all dynamic tables connected with the specified dynamic table.

```sqlexample
SELECT
  name,
  target_lag_sec,
  mean_lag_sec,
  latest_data_timestamp
FROM
  TABLE (
    INFORMATION_SCHEMA.DYNAMIC_TABLES (
      NAME => 'mydb.myschema.mydt',
      INCLUDE_CONNECTED => TRUE
    )
  )
ORDER BY
  target_lag_sec
```
