# Source: https://docs.snowflake.com/en/sql-reference/functions/dbt_project_execution_history.md

Categories:
:   [Information Schema](../info-schema.md) , [Table functions](../functions-table.md)

# DBT_PROJECT_EXECUTION_HISTORY

Returns the execution history of [dbt Projects on Snowflake](../../user-guide/data-engineering/dbt-projects-on-snowflake.md).

Call this function to get metadata and results from past dbt Project executions within seven days of the current time. Optionally, specify the values to filter the results by.

Use this function with the following system functions to access dbt artifacts and logs programmatically:

* [SYSTEM$GET_DBT_LOG](system_get_dbt_log.md)
* [SYSTEM$LOCATE_DBT_ARCHIVE](system_locate_dbt_archive.md)
* [SYSTEM$LOCATE_DBT_ARTIFACTS](system_locate_dbt_artifacts.md)

For more information, see [Access dbt artifacts and logs programmatically](../../user-guide/data-engineering/dbt-projects-on-snowflake-monitoring-observability.md).

See also:
:   [CREATE DBT PROJECT](../sql/create-dbt-project.md), [EXECUTE DBT PROJECT](../sql/execute-dbt-project.md)

## Syntax

```sqlsyntax
DBT_PROJECT_EXECUTION_HISTORY (
  [ OBJECT_NAME => '<name>' ]
  [ , OBJECT_TYPE = { WORKSPACE | DBT PROJECT }]
  [ , START_TIME_RANGE_START => <start_time> ]
  [ , START_TIME_RANGE_END => <end_time>  ]
  [ , RESULT_LIMIT = <integer> ]
  [ , COMMAND = <dbt_command> ]
  [ , USER_NAME = <user_name> ]
  [ , DATABASE = <db_name> ]
  [ , SCHEMA = <schema_name> ]
)
```

## Arguments

`OBJECT_NAME = <name>`
:   Name of the workspace or dbt project that the run belongs to.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`OBJECT_TYPE = { WORKSPACE | DBT PROJECT }`
:   The type of the object, WORKSPACE or DBT PROJECT, the run belongs to.

`START_TIME_RANGE_START | START_TIME_RANGE_END = timestamp`
:   Timestamp to filter a range of dbt project runs.

`RESULT_LIMIT = integer`
:   An integer specifying the maximum number of rows returned by the function, from 1 - 10,000 inclusive.

    Default: 100

`COMMAND = dbt_command`
:   Specifies the [dbt command](https://docs.getdbt.com/reference/dbt-commands) used to execute the dbt project.

`USER_NAME = user_name`
:   Name of the user that initiated the dbt project object run.

`DATABASE = db_name`
:   Return only records for the specified database.

`SCHEMA = schema_name`
:   Return only records for the specified schema.

## Output

The function returns the following columns.

To view these columns, you must use a role with the MONITOR privilege.

| Column Name | Data Type | Description |
| --- | --- | --- |
| QUERY_ID | TEXT | ID of the query. |
| QUERY_START_TIME | TIMESTAMP_LTZ | The time the query started. |
| QUERY_END_TIME | TIMESTAMP_LTZ | The time the query ended. |
| USER_NAME | TEXT | The user that created the dbt Project. |
| OBJECT_NAME | TEXT | Name of the workspace or dbt Project the run belonged to. |
| OBJECT_TYPE | TEXT | Type of object, such as WORKSPACE or DBT PROJECT. |
| DATABASE_NAME | TEXT | Database of the object. |
| SCHEMA_NAME | TEXT | Schema of the object. |
| COMMAND | TEXT | The command that was run for the object. |
| ARGS | TEXT | The arguments that were used in the run for the object. |
| ERROR_CODE | NUMBER | If applicable, the error code for the run. |
| ERROR_MESSAGE | TEXT | If applicable, error message stating why the run failed. |
| WAREHOUSE | TEXT | Warehouse used for the object. |
| STATE | TEXT | State of run, such as HANDLED_ERROR or SUCCESS. |
| DBT_VERSION | TEXT | The specific version used for this run. For example, `1.9.4`. |
| DBT_SNOWFLAKE_VERSION | TEXT | The specific dbt Projects on Snowflake version with patch version used for this run. For example, `1.9.4`. |

## Access control requirements

This table function includes only runs from workspaces and dbt Projects in which you have the following privileges:

* OWNERSHIP, READ, or WRITE on workspaces
* OWNERSHIP, USAGE, or MONITOR on dbt Projects

## Usage notes

* Use the exact dbt Project name (case-sensitive if created with quotes). If no row matches (wrong dbt Project name or no runs yet), you might get an `Inputs may not be null.` error.

## Examples

The following example audits which engine version was used for recent runs:

```sqlexample
SELECT
    query_start_time,
    query_id,
    dbt_version
FROM
  TABLE (
    INFORMATION_SCHEMA.DBT_PROJECT_EXECUTION_HISTORY (
     OBJECT_NAME => 'finance_analytics'
    )
  );
```

For detailed examples of using the DBT_PROJECT_EXECUTION_HISTORY table function with system functions to access dbt artifacts and logs programmatically,
see [Access dbt artifacts and logs programmatically](../../user-guide/data-engineering/dbt-projects-on-snowflake-monitoring-observability.md).
