# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-alert.md

# DESCRIBE ALERT

Describes the properties of an [alert](../../user-guide/alerts.md).

See also:
:   [CREATE ALERT](create-alert.md) , [ALTER ALERT](alter-alert.md), [DROP ALERT](drop-alert.md) , [SHOW ALERTS](show-alerts.md) , [EXECUTE ALERT](execute-alert.md)

## Syntax

```sqlsyntax
DESC[RIBE] ALERT <name>
```

## Required parameters

`name`
:   Identifier for the alert to describe. If the identifier contains spaces or special characters, the entire string must be
    enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this SQL command must have at least one of the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| MONITOR, OPERATE, or OWNERSHIP | Alert | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Only returns rows for an alert owner (i.e. the role with the OWNERSHIP privilege on an alert) or a role with the OPERATE
  privilege on an alert.

* To post-process the output of this command, you can use the [pipe operator](../operators-flow.md)
  (`->>`) or the [RESULT_SCAN](../functions/result_scan.md) function. Both constructs treat the output as a
  result set that you can query.

  For example, you can use the pipe operator or RESULT_SCAN function to select specific columns from the SHOW
  command output or filter the rows.

  When you refer to the output columns, use [double-quoted identifiers](../identifiers-syntax.md) for
  the column names. For example, to select the output column `type`, specify `SELECT "type"`.

  You must use double-quoted identifiers because the output column names for SHOW commands are in lowercase.
  The double quotes ensure that the column names in the SELECT list or WHERE clause match the column names
  in the SHOW command output that was scanned.

## Examples

See [Viewing details about an alert](../../user-guide/alerts.md).
