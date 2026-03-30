# Source: https://docs.snowflake.com/en/sql-reference/sql/undrop-iceberg-table.md

# UNDROP ICEBERG TABLE

Restores the most recent version of a dropped [Apache Iceberg™ table](../../user-guide/tables-iceberg.md).

This topic refers to Iceberg tables as simply “tables” except where specifying *Iceberg tables* avoids confusion.

See also:
:   [CREATE ICEBERG TABLE](create-iceberg-table.md) , [ALTER ICEBERG TABLE](alter-iceberg-table.md) , [DROP ICEBERG TABLE](drop-iceberg-table.md) ,
    [SHOW ICEBERG TABLES](show-iceberg-tables.md) , [DESCRIBE ICEBERG TABLE](desc-iceberg-table.md)

## Syntax

```sqlsyntax
UNDROP ICEBERG TABLE <name>
```

## Parameters

`name`
:   Specifies the identifier for the table to restore. If the identifier contains spaces or special characters, the entire string must
    be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Usage notes

* This command isn’t supported for tables in a catalog-linked database.
* Restoring Iceberg tables is only supported in the current schema or current database, even if the table name is fully qualified.
* If an Iceberg table with the same name already exists, an error is returned.
* To undrop an Iceberg table whose external volume has been dropped, undrop the external volume first. You can’t undrop the Iceberg table
  by creating a new external volume with same name as the dropped external volume.
* You can’t restore a table that uses an external catalog if the associated catalog integration has been dropped.

* UNDROP relies on the Snowflake [Time Travel](../../user-guide/data-time-travel.md) feature. An object can be restored only if
  the object was deleted within the [Data retention period](../../user-guide/data-time-travel.md). The default value is 24 hours.

## Examples

Restore the most recent version of a dropped table `my_iceberg_table`:

```sqlexample
UNDROP ICEBERG TABLE my_iceberg_table;
```
