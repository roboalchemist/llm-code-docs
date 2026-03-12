# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_dbt_log.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$GET_DBT_LOG

Returns logs for the specified run for a dbt Projects on Snowflake.

Use this function with the [DBT_PROJECT_EXECUTION_HISTORY](dbt_project_execution_history.md) function to access dbt artifacts and logs programmatically.

## Syntax

```sqlsyntax
SYSTEM$GET_DBT_LOG ( '<query_id>' )
```

## Arguments

`query_id`
:   Query ID of the run that you want logs for.

## Returns

The function returns the last 1,000 lines of the `dbt.log` file. For full logs, download the archive ZIP file.

For more information and examples, see [Access dbt artifacts and logs programmatically](../../user-guide/data-engineering/dbt-projects-on-snowflake-monitoring-observability.md).

## Access control requirements

This function includes only runs from workspaces and dbt Projects in which you have the following privileges:

* OWNERSHIP, READ, or WRITE on workspaces
* OWNERSHIP, USAGE, or MONITOR on dbt Projects

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* This system function works only on dbt project objects; it isn’t available for workspaces.
* Query IDs generated from CREATE DBT PROJECT or ALTER DBT PROJECT … ADD VERSION aren’t supported for this system function.
* Direct querying of file content (for example, [Query examples](../../user-guide/querying-stage.md)) isn’t supported.
* If `query_id` is NULL or not a dbt execution, you’ll get an error.
* dbt project results are available for up to 14 days.
* Logs might be unavailable if a run times out, is canceled, or fails before files are uploaded. In such cases, runs appear as `UNHANDLED ERROR` in dbt history, and these entries might not include logs.
* You can’t use this function to get logs for runs that are in progress because the logs file is only available after the run in complete.

## Examples

The following example looks up the most recent dbt Project execution for `MY_DBT_PROJECT` using DBT_PROJECT_EXECUTION_HISTORY and then fetches the dbt run logs for that execution using
SYSTEM$GET_DBT_LOG, so you can inspect what happened during the run.

```sqlexample
--Look up the most recent dbt Project execution
SET latest_query_id = (SELECT query_id
  FROM TABLE(INFORMATION_SCHEMA.DBT_PROJECT_EXECUTION_HISTORY())
  WHERE OBJECT_NAME = 'MY_DBT_PROJECT'
  ORDER BY query_end_time DESC LIMIT 1);

--Get the dbt run logs for the most recent dbt Project execution
SELECT SYSTEM$GET_DBT_LOG($latest_query_id);
```

```output
============================== 15:14:53.100781 | 46d19186-61b8-4442-8339-53c771083f16 ==============================
[0m15:14:53.100781 [info ] [Dummy-1   ]: Running with dbt=1.9.4
...
[0m15:14:58.198545 [debug] [Dummy-1   ]: Command `cli run` succeeded at 15:14:58.198121 after 5.19 seconds
```

For more information, see [Access dbt artifacts and logs programmatically](../../user-guide/data-engineering/dbt-projects-on-snowflake-monitoring-observability.md).
