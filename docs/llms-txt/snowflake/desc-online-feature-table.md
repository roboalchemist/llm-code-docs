# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-online-feature-table.md

# DESCRIBE ONLINE FEATURE TABLE

Describes the columns in an [online feature table](create-online-feature-table.md).

DESCRIBE can be abbreviated to DESC.

See also:
:   [CREATE ONLINE FEATURE TABLE](create-online-feature-table.md) , [ALTER ONLINE FEATURE TABLE](alter-online-feature-table.md), [DROP ONLINE FEATURE TABLE](drop-online-feature-table.md) , [SHOW ONLINE FEATURE TABLES](show-online-feature-tables.md)

## Syntax

```sqlsyntax
{ DESC | DESCRIBE } ONLINE FEATURE TABLE <name>
```

## Parameters

`name`
:   Specifies the identifier for the online feature table to describe.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

| Privilege | Object | Notes |
| --- | --- | --- |
| MONITOR | Online feature table | Role that has the MONITOR privilege on the online feature table. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

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
