# Source: https://docs.snowflake.com/en/sql-reference/functions/system_locate_dbt_archive.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$LOCATE_DBT_ARCHIVE

Returns the URL from which you can retrieve zipped dbt run artifacts for a specified dbt project.

Use this function with the [DBT_PROJECT_EXECUTION_HISTORY](dbt_project_execution_history.md) function to access dbt artifacts and logs programmatically.

## Syntax

```sqlsyntax
SYSTEM$LOCATE_DBT_ARCHIVE ( '<query_id>' )
```

## Arguments

`query_id`
:   The query ID of the dbt project run whose files you want to locate.

## Returns

This function returns the URL from which you can retrieve the zipped contents of the results of a specified dbt Project.

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
* Files might be unavailable if a run times out, is canceled, or fails before they are uploaded. In such cases, runs appear as `UNHANDLED ERROR` in dbt history.
* You can’t use this function to get logs for runs that are in progress because the logs file is only available after the run in complete.

## Examples

The following example returns the `snow://` URL of the zipped artifacts (for example, `dbt_artifacts.zip`) for the specified execution.

You can use this URL with GET to download the ZIP file (or COPY FILES to move it to your own stage). For the folder path instead of the ZIP, use
[SYSTEM$LOCATE_DBT_ARTIFACTS](system_locate_dbt_artifacts.md).

```sqlexample
SELECT SYSTEM$LOCATE_DBT_ARCHIVE($latest_query_id);
```

For more information, see [Access dbt artifacts and logs programmatically](../../user-guide/data-engineering/dbt-projects-on-snowflake-monitoring-observability.md).
