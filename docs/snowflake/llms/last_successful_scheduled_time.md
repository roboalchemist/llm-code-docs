# Source: https://docs.snowflake.com/en/sql-reference/functions/last_successful_scheduled_time.md

Categories:
:   [Date & time functions](../functions-date-time.md) (Alerts)

# LAST_SUCCESSFUL_SCHEDULED_TIME

Returns the timestamp representing the scheduled time for the most recent successful evaluation of the alert condition, where no
errors occurred when executing the action. (In the [alert history](../../user-guide/alerts.md), these are the alerts with the
STATE CONDITION_FALSE or TRIGGERED.) Refer to [Specifying timestamps based on alert schedules](../../user-guide/alerts.md).

## Syntax

```sqlsyntax
SNOWFLAKE.ALERT.LAST_SUCCESSFUL_SCHEDULED_TIME()
```

## Arguments

None.

## Returns

TIMESTAMP_LTZ value that represents when the most recent successful evaluation of the alert condition was scheduled, or NULL
if there are no recent successful evaluations of the alert condition.

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
