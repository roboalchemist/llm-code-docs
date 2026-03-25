# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-task.md

# DESCRIBE TASK

Shows information about a task.

DESCRIBE can be abbreviated to DESC.

See also:
:   [DROP TASK](drop-task.md) , [ALTER TASK](alter-task.md) , [CREATE TASK](create-task.md) , [SHOW TASKS](show-tasks.md)

## Syntax

```sqlsyntax
DESC[RIBE] TASK <name>
```

## Parameters

`name`
:   Specifies the identifier for the task to describe. If the identifier contains spaces or special characters, the entire string must be
    enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Output

The command provides the same output as [SHOW_TASKS](show-tasks.md).

## Usage notes

* Only returns rows for a task owner—that is, the role with the OWNERSHIP privilege on a task—or a role with either the MONITOR
  or OPERATE privilege on a task.

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

Create an example task:

> ```sqlexample
> CREATE TASK mytask ( ... );
> ```

Show information about the task:

> ```sqlexample
> DESC TASK mytask;
> ```

For output examples, see [SHOW_TASKS](show-tasks.md).
