# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-materialized-view.md

# DESCRIBE MATERIALIZED VIEW

Describes the columns in a materialized view.

DESCRIBE can be abbreviated to DESC.

See also:
:   [CREATE MATERIALIZED VIEW](create-materialized-view.md) , [DROP MATERIALIZED VIEW](drop-materialized-view.md) , [ALTER MATERIALIZED VIEW](alter-materialized-view.md) , [SHOW MATERIALIZED VIEWS](show-materialized-views.md)

## Syntax

```sqlsyntax
DESC[RIBE] MATERIALIZED VIEW <name>
```

## Parameters

`name`
:   Specifies the identifier for the materialized view to describe. If the identifier contains spaces or special characters, the
    entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Usage notes

* The command output does not include the view definition. To see the materialized view’s definition, use [SHOW MATERIALIZED VIEWS](show-materialized-views.md)
  or [GET_DDL](../functions/get_ddl.md).
* DESC MATERIALIZED VIEW and [DESCRIBE TABLE](desc-table.md) are interchangeable. Either command retrieves the details for the table
  or view that matches the criteria in the statement.

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

Example setup:

> ```sqlexample
> CREATE MATERIALIZED VIEW emp_view
>     AS
>     SELECT id "Employee Number", lname "Last Name", location "Home Base" FROM emp;
> ```

Describe the materialized view:

> ```sqlexample
> DESC MATERIALIZED VIEW emp_view;
> ```

```output
+-----------------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------+
| name            | type         | kind   | null? | default | primary key | unique key | check | expression | comment |
|-----------------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------|
| Employee Number | NUMBER(38,0) | COLUMN | Y     | NULL    | N           | N          | NULL  | NULL       | NULL    |
| Last Name       | VARCHAR(50)  | COLUMN | Y     | NULL    | N           | N          | NULL  | NULL       | NULL    |
| Home Base       | VARCHAR(100) | COLUMN | Y     | NULL    | N           | N          | NULL  | NULL       | NULL    |
+-----------------+--------------+--------+-------+---------+-------------+------------+-------+------------+---------+
```
