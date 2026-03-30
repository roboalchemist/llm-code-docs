# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-event-table.md

# DESCRIBE EVENT TABLE

Describes the columns in an [event table](../../developer-guide/logging-tracing/event-table-setting-up.md).

DESCRIBE can be abbreviated to DESC.

See also:
:   [ALTER TABLE (event tables)](alter-table-event-table.md) , [CREATE EVENT TABLE](create-event-table.md) , [SHOW EVENT TABLES](show-event-tables.md)

## Syntax

```sqlsyntax
DESC[RIBE] EVENT TABLE <name>
```

## Parameters

`name`
:   Specifies the identifier for the event table to describe. If the identifier contains spaces or special characters, the entire
    string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Usage notes

* This command does not show the object parameters for a table. Instead, use
  [SHOW PARAMETERS IN TABLE …](show-parameters.md).

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

Describe the columns in the event table named `my_logged_events`:

> ```sqlexample
> DESC EVENT TABLE my_logged_events;
> ```
