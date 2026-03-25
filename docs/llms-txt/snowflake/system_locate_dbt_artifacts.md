# Source: https://docs.snowflake.com/en/sql-reference/functions/system_locate_dbt_artifacts.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$LOCATE_DBT_ARTIFACTS

Returns the location of artifacts from a specified dbt Project run (for example, `manifest.json`).

Use this function with the [DBT_PROJECT_EXECUTION_HISTORY](dbt_project_execution_history.md) function to access dbt artifacts and logs programmatically.

## Syntax

```sqlsyntax
SYSTEM$LOCATE_DBT_ARTIFACTS ( '<query_id>' )
```

## Arguments

`query_id`
:   The query ID of the dbt project run whose files you want to locate.

## Returns

The function returns the file path for dbt Project artifacts from a run (for example, `snow://dbt/DBTEST.PUBLIC.MY_DBT_PROJECT/results/query_id_01bf3f5a-010b-4d87-0000-53493abb7cce/`).

For more information and examples, see [Access dbt artifacts and logs programmatically](../../user-guide/data-engineering/dbt-projects-on-snowflake-monitoring-observability.md).

## Access control requirements

This function includes only runs from workspaces and dbt Projects in which you have the following privileges:

* OWNERSHIP, READ, or WRITE on workspaces
* OWNERSHIP, USAGE, or MONITOR on dbt Projects

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* This system function works only on dbt project objects; it isn’t available for workspaces.
* Query IDs generated from CREATE DBT PROJECT or ALTER DBT PROJECT … ADD VERSION aren’t supported for this system function.
* Direct querying of file content (for example, [Query examples](../../user-guide/querying-stage.md)) isn’t supported.
* If `query_id` is NULL or not a dbt execution, you’ll get an error.
* dbt project results are available for up to 14 days.
* Files might be unavailable if a run times out, is canceled, or fails before they are uploaded. In such cases, runs appear as `UNHANDLED ERROR` in dbt history.
* You can’t use this function to get logs for runs that are in progress because the logs file is only available after the run in complete.

## Examples

To view the stage path where Snowflake stored the dbt Project run’s artifacts (that is, the results folder for that execution), use the SYSTEM$LOCATE_DBT_ARTIFACTS function, as shown in the following
example. You can then use that path with `GET` or `COPY FILES` or the Snowflake CLI to download things like `manifest.json`, compiled SQL, or logs.

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

```sqlexample
--Get the location of the dbt Project archive ZIP file (see all files)
SELECT SYSTEM$LOCATE_DBT_ARTIFACTS($latest_query_id);
```

```output
+-------------------------------------------------------------------------------------------------+
| SYSTEM$LOCATE_DBT_ARTIFACTS($LATEST_QUERY_ID)                                                   |
+-------------------------------------------------------------------------------------------------+
| snow://dbt/TESTDBT.PUBLIC.MY_DBT_PROJECT/results/query_id_01c01096-010c-0ccb-0000-a99506bd199e/ |
+-------------------------------------------------------------------------------------------------+
```

```sqlexample
--List all the files of the retrieved dbt run
ls 'snow://dbt/TESTDBT.PUBLIC.MY_DBT_PROJECT/results/query_id_01bf3f5a-010b-4d87-0000-53493abb7cce/';
```

You can also create a fresh internal stage, locate the Snowflake-managed path for the specified dbt Project run’s artifacts, and copy those artifacts into your stage for retrieval, as shown in the
following example:

```sqlexample
CREATE OR REPLACE STAGE my_dbt_stage ENCRYPTION = (TYPE = 'SNOWFLAKE_SSE');
```

For more information, see [Access dbt artifacts and logs programmatically](../../user-guide/data-engineering/dbt-projects-on-snowflake-monitoring-observability.md).
