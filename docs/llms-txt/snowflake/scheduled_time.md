# Source: https://docs.snowflake.com/en/sql-reference/functions/scheduled_time.md

Categories:
:   [Date & time functions](../functions-date-time.md) (Alerts)

# SCHEDULED_TIME

Returns the timestamp representing the scheduled time of the current alert. Refer to [Specifying timestamps based on alert schedules](../../user-guide/alerts.md).

## Syntax

```sqlsyntax
SNOWFLAKE.ALERT.SCHEDULED_TIME()
```

## Arguments

None.

## Returns

TIMESTAMP_LTZ value that represents the scheduled time of the current alert.

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

Refer to [Specifying timestamps based on alert schedules](../../user-guide/alerts.md).
