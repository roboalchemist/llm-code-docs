# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-dynamic-table.md

# DESCRIBE DYNAMIC TABLE

Describes the columns in a [dynamic table](../../user-guide/dynamic-tables-about.md).

DESCRIBE can be abbreviated to DESC.

See also:
:   [CREATE DYNAMIC TABLE](create-dynamic-table.md), [ALTER DYNAMIC TABLE](alter-dynamic-table.md), [DROP DYNAMIC TABLE](drop-dynamic-table.md), [SHOW DYNAMIC TABLES](show-dynamic-tables.md)

## Syntax

```sqlsyntax
DESC[RIBE] DYNAMIC TABLE <name>
```

## Parameters

`name`
:   Specifies the identifier for the dynamic table to describe. If the identifier contains spaces or special characters, the entire
    string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| SELECT | The dynamic table that you want to describe. | Some metadata is hidden if you don’t have the MONITOR privilege. For more information, see [Privileges to view a dynamic table’s metadata](../../user-guide/dynamic-tables-privileges.md). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* To DESCRIBE a dynamic table, you must be using a role that has MONITOR privilege on the table.

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

Describe the columns in `my_dynamic_table`:

> ```sqlexample
> DESC DYNAMIC TABLE my_dynamic_table;
> ```
