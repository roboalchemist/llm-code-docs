# Source: https://docs.snowflake.com/en/sql-reference/sql-dml.md

# Data Manipulation Language (DML) commands

This topic provides links to all the DML commands, grouped by category.

## General DML

Commands for inserting, deleting, updating, and merging data in Snowflake tables:

* [INSERT](sql/insert.md)
* [INSERT (multi-table)](sql/insert-multi-table.md)
* [MERGE](sql/merge.md)
* [UPDATE](sql/update.md)
* [DELETE](sql/delete.md)
* [TRUNCATE TABLE](sql/truncate-table.md)

## Data loading / unloading DML

Commands for bulk copying data into and out of Snowflake tables:

* [COPY INTO <table>](sql/copy-into-table.md) (loading/importing data)
* [COPY INTO <location>](sql/copy-into-location.md) (unloading/exporting data)

See also:
:   [VALIDATE](functions/validate.md) (table function)

## File staging commands (for data loading / unloading)

These commands do not perform any actual DML, but are used to stage and manage files stored in Snowflake locations (named internal stages, table stages,
and user stages), for the purpose of loading and unloading data:

* [PUT](sql/put.md)
* [GET](sql/get.md)
* [LIST](sql/list.md) (can also be used with named external stages)
* [REMOVE](sql/remove.md)
