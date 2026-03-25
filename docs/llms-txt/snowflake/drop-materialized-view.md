# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-materialized-view.md

# DROP MATERIALIZED VIEW

Removes the specified materialized view from the current/specified schema.

See also:
:   [ALTER MATERIALIZED VIEW](alter-materialized-view.md) , [CREATE MATERIALIZED VIEW](create-materialized-view.md) , [SHOW MATERIALIZED VIEWS](show-materialized-views.md) , [DESCRIBE MATERIALIZED VIEW](desc-materialized-view.md)

## Syntax

```sqlsyntax
DROP MATERIALIZED VIEW [ IF EXISTS ] <view_name>
```

## Usage notes

* Dropping a materialized view does not update references to that view. For example, if you create a view named “V1” on top of a
  materialized view, and then you drop the materialized view, the definition of view “V1” will become out of date.
* Dropped materialized views can’t be recovered; they must be recreated.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

> ```sqlexample
> DROP MATERIALIZED VIEW mv1;
>
> ---------------------------+
>            status          |
> ---------------------------+
>  MV1 successfully dropped. |
> ---------------------------+
> ```
