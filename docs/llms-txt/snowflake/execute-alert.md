# Source: https://docs.snowflake.com/en/sql-reference/sql/execute-alert.md

# EXECUTE ALERT

Manually executes an [alert](../../user-guide/alerts.md) independent of the schedule for the alert.

> **Note:**
>
> You cannot use EXECUTE ALERT to execute an [alert on new data](../../user-guide/alerts.md).

See also:
:   [CREATE ALERT](create-alert.md) , [ALTER ALERT](alter-alert.md) , [DROP ALERT](drop-alert.md) , [SHOW ALERTS](show-alerts.md) , [DESCRIBE ALERT](desc-alert.md)

## Syntax

```sqlsyntax
EXECUTE ALERT <name>
```

## Parameters

`name`
:   Identifier for the alert to execute.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| EXECUTE ALERT | Account |  |
| OWNERSHIP or OPERATE | Alert |  |
| USAGE | Warehouse | Required on the warehouse used for the alert. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Alerts always run with the privileges of the owner of the alert, even if a different role with the OPERATE privilege uses
  EXECUTE ALERT to execute the alert.
* If the alert is currently suspended, the EXECUTE ALERT command executes the alert but does not resume the alert. The alert
  remains suspended.
* If the alert is currently running (meaning that the state of the alert in the [ALERT_HISTORY](../functions/alert_history.md)
  table function output or the [ALERT_HISTORY view](../account-usage/alert_history.md) is `EXECUTING`), the
  EXECUTE ALERT command schedules another run of the alert to start immediately after the current run is completed.
* If the alert is currently scheduled (meaning that the state of the alert in the ALERT_HISTORY table function output or the
  ALERT_HISTORY view is `SCHEDULED`), the scheduled run is replaced with the requested run and the current timestamp is set
  to the scheduled time.

  However, if the scheduled time has passed but the alert has not yet transitioned to the `EXECUTING` state, the scheduled run
  occurs as usual. (The scheduled run is not replaced with the run requested by the EXECUTE ALERT command.)

## Examples

The following statement manually triggers an alert named `myalert`:

```sqlexample
EXECUTE ALERT myalert;
```
