# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-view.md

# DROP VIEW

Removes the specified view from the current/specified schema.

See also:
:   [CREATE VIEW](create-view.md) , [ALTER VIEW](alter-view.md) , [SHOW VIEWS](show-views.md) , [DESCRIBE VIEW](desc-view.md)

## Syntax

```sqlsyntax
DROP VIEW [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the view to drop. If the identifier contains spaces, special characters, or mixed-case characters, the
    entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

    If the view identifier is not fully-qualified (in the form of `db_name.schema_name.table_name` or
    `schema_name.table_name`), the command looks for the view in the current schema for the session.

## Usage notes

* Dropped views can’t be recovered; they must be recreated.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

> ```sqlexample
> DROP VIEW myview;
> ```
>
> ```output
> ------------------------------+
>            status             |
> ------------------------------+
>  MYVIEW successfully dropped. |
> ------------------------------+
> ```
