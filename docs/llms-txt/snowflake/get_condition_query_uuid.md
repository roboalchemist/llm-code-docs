# Source: https://docs.snowflake.com/en/sql-reference/functions/get_condition_query_uuid.md

Categories:
:   [Context functions](../functions-context.md) (Alerts)

# GET_CONDITION_QUERY_UUID

Returns the query ID for the SQL statement executed for the condition of an [alert](../../user-guide/alerts.md). In the action for
an alert, you can call this function to
[check the results of the statement for the condition](../../user-guide/alerts.md).

## Syntax

```sqlsyntax
SNOWFLAKE.ALERT.GET_CONDITION_QUERY_UUID()
```

## Arguments

None.

## Returns

The query ID for the SQL statement for the condition of the alert.

## Usage notes

* This function is defined in the ALERT schema of the SNOWFLAKE database.

  To call this function, you must use a role that is granted the
  [SNOWFLAKE database role](../snowflake-db-roles.md) ALERT_VIEWER. For example, to call the function as a user
  with the role alert_role, execute:

  ```sqlexample
  GRANT DATABASE ROLE snowflake.alert_viewer TO ROLE alert_role;
  ```

* This function can only be called from within an [alert](../../user-guide/alerts.md).

## Examples

Refer to [Checking the results of the SQL statement for the condition in the alert action](../../user-guide/alerts.md).
