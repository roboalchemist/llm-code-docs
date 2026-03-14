# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-warehouse.md

# DESCRIBE WAREHOUSE

Describes a [virtual warehouse](../../user-guide/warehouses-overview.md). For example, shows the date that the warehouse was created.

You can abbreviate DESCRIBE to DESC.

See also:
:   [ALTER WAREHOUSE](alter-warehouse.md) , [CREATE WAREHOUSE](create-warehouse.md), [DROP WAREHOUSE](drop-warehouse.md) , [SHOW WAREHOUSES](show-warehouses.md)

## Syntax

```sqlsyntax
DESC[RIBE] WAREHOUSE <name>
```

## Parameters

`name`
:   Specifies the [identifier](../identifiers.md) of the warehouse to describe.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| MONITOR | Warehouse |  |

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

## Examples

This demonstrates the DESCRIBE WAREHOUSE command:

```sqlexample
CREATE WAREHOUSE temporary_warehouse WAREHOUSE_SIZE=XSMALL;
```

```sqlexample
DESCRIBE WAREHOUSE temporary_warehouse;
```

```output
+-------------------------------+---------------------+-----------+
| created_on                    | name                | kind      |
|-------------------------------+---------------------+-----------|
| 2022-06-23 00:00:00.000 -0700 | TEMPORARY_WAREHOUSE | WAREHOUSE |
+-------------------------------+---------------------+-----------+
```
