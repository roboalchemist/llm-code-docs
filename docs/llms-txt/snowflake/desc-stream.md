# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-stream.md

# DESCRIBE STREAM

Describes the properties specified for a stream.

DESCRIBE can be abbreviated to DESC.

See also:
:   [DROP STREAM](drop-stream.md) , [ALTER STREAM](alter-stream.md) , [CREATE STREAM](create-stream.md) , [SHOW STREAMS](show-streams.md)

## Syntax

```sqlsyntax
DESC[RIBE] STREAM <name>
```

## Parameters

`name`
:   Specifies the identifier for the stream to describe. If the identifier contains spaces or special characters, the entire string must be
    enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

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

Create an example stream:

> ```sqlexample
> CREATE STREAM mystream ( ... );
> ```

Describe the columns in the stream:

> ```sqlexample
> DESC STREAM mystream;
> ```
