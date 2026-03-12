# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-sequence.md

# DESCRIBE SEQUENCE

Describes a sequence, including the sequence’s interval.

DESCRIBE can be abbreviated to DESC.

See also:
:   [ALTER SEQUENCE](alter-sequence.md) , [CREATE SEQUENCE](create-sequence.md) , [DROP SEQUENCE](drop-sequence.md) , [SHOW SEQUENCES](show-sequences.md)

## Syntax

```sqlsyntax
DESC[RIBE] SEQUENCE <name>
```

## Parameters

`name`
:   Specifies the identifier for the sequence to describe.

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

```sqlexample
DESC SEQUENCE my_sequence;
```
