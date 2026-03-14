# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-index.md

# DROP INDEX

Drops a secondary index.

See also:
:   [CREATE INDEX](create-index.md) , [SHOW INDEXES](show-indexes.md) , [CREATE HYBRID TABLE](create-hybrid-table.md) , [DROP TABLE](drop-table.md) , [DESCRIBE TABLE](desc-table.md) , [SHOW HYBRID TABLES](show-hybrid-tables.md)

## Syntax

```sqlsyntax
DROP INDEX [ IF EXISTS ] <table_name>.<index_name>
```

## Parameters

`table_name`
:   Specifies the identifier for the table.

`index_name`
:   Specifies the identifier for the index.

## Usage notes

* This command can only be used to drop a *secondary* index. To drop an index that is used to enforce a UNIQUE
  or FOREIGN KEY constraint, use the [ALTER TABLE](alter-table.md) command to drop the constraint.
* Indexes cannot be undropped.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

Removes the secondary index `c_idx` on table `t0`:

```sqlexample
DROP INDEX t0.c_idx;
```
