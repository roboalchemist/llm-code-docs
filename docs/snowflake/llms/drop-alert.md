# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-alert.md

# DROP ALERT

Drops an existing [alert](../../user-guide/alerts.md).

See also:
:   [CREATE ALERT](create-alert.md) , [ALTER ALERT](alter-alert.md), [DESCRIBE ALERT](desc-alert.md) , [SHOW ALERTS](show-alerts.md) , [EXECUTE ALERT](execute-alert.md)

## Syntax

```sqlsyntax
DROP ALERT [ IF EXISTS ] <name>
```

## Required parameters

`name`
:   Identifier for the alert to drop. If the identifier contains spaces or special characters, the entire string must be enclosed
    in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Alert | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* When an alert is dropped, any current evaluation of the condition of the alert (i.e. a run with an EXECUTING state in the
  [ALERT_HISTORY](../functions/alert_history.md) output) is completed.
* An alert can be dropped by the alert owner (i.e. the role that has the OWNERSHIP privilege on the alert) or a higher role
  without first suspending the alert.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

See [Dropping an alert](../../user-guide/alerts.md).
