# Source: https://docs.snowflake.com/en/sql-reference/sql/truncate-table.md

# TRUNCATE TABLE

Removes all rows from a table but leaves the table intact (including all privileges and constraints on the table). Also deletes the load
metadata for the table, which allows the same files to be loaded into the table again after the command completes.

Note that this is different from [DROP TABLE](drop-table.md), which removes the table from the system but retains a version of the table
(along with its load history) so that they can be recovered.

See also:
:   [CREATE TABLE](create-table.md)

## Syntax

```sqlsyntax
TRUNCATE [ TABLE ] [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the table to truncate. If the identifier contains spaces or special characters, the entire string must be
    enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive (e.g. `"My Object"`).

    If the table identifier is not fully-qualified (in the form of `db_name.schema_name.table_name` or
    `schema_name.table_name`), the command looks for the table in the current schema for the session.

## Usage notes

* Both [DELETE](delete.md) and TRUNCATE TABLE maintain deleted data for recovery purposes (i.e. using Time Travel) for the data retention period.
  However, when a table is truncated, the load metadata cannot be recovered.
* The `TABLE` keyword is optional if the table name is fully qualified or a database and schema are currently in use for the session.

## Examples

> ```sqlexample
> -- create a basic table
> CREATE OR REPLACE TABLE temp (i number);
>
> -- populate it with some rows
> INSERT INTO temp SELECT seq8() FROM table(generator(rowcount=>20)) v;
>
> -- verify that the rows exist
> SELECT COUNT (*) FROM temp;
>
> ----------+
>  count(*) |
> ----------+
>  20       |
> ----------+
>
> -- truncate the table
> TRUNCATE TABLE IF EXISTS temp;
>
> -- verify that the table is now empty
> SELECT COUNT (*) FROM temp;
>
> ----------+
>  count(*) |
> ----------+
>  0        |
> ----------+
> ```
