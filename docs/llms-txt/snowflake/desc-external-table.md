# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-external-table.md

# DESCRIBE EXTERNAL TABLE

Describes the VALUE column and virtual columns in an external table.

DESCRIBE can be abbreviated to DESC.

See also:
:   [DROP EXTERNAL TABLE](drop-external-table.md) , [ALTER EXTERNAL TABLE](alter-external-table.md) , [CREATE EXTERNAL TABLE](create-external-table.md) , [SHOW EXTERNAL TABLES](show-external-tables.md)

    [DESCRIBE VIEW](desc-view.md)

## Syntax

```sqlsyntax
DESC[RIBE] [ EXTERNAL ] TABLE <name> [ TYPE =  { COLUMNS | STAGE } ]
```

## Parameters

`name`
:   Specifies the identifier for the external table to describe. If the identifier contains spaces or special characters, the entire string
    must be enclosed in double quotes. Identifiers enclosed in double quotes are also case sensitive.

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

Create an example external table:

> ```sqlexample
> CREATE EXTERNAL TABLE emp ( ... );
> ```

Describe the columns in the table:

> ```sqlexample
> DESC EXTERNAL TABLE emp;
> ```
