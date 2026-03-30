# Source: https://docs.snowflake.com/en/sql-reference/sql/undrop-external-volume.md

# UNDROP EXTERNAL VOLUME

Restores the most recent version of a dropped [external volume](../../user-guide/tables-iceberg.md).

See also:
:   [CREATE EXTERNAL VOLUME](create-external-volume.md) , [ALTER EXTERNAL VOLUME](alter-external-volume.md), [DESCRIBE EXTERNAL VOLUME](desc-external-volume.md) , [SHOW EXTERNAL VOLUMES](show-external-volumes.md) ,
    [DROP EXTERNAL VOLUME](drop-external-volume.md)

## Syntax

```sqlsyntax
UNDROP EXTERNAL VOLUME <name>
```

## Parameters

`name`
:   Specifies the identifier for the external volume to restore.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Usage notes

* If an external volume with the same name already exists, the UNDROP command returns an error.

* UNDROP relies on the Snowflake [Time Travel](../../user-guide/data-time-travel.md) feature. An object can be restored only if
  the object was deleted within the [Data retention period](../../user-guide/data-time-travel.md). The default value is 24 hours.

## Examples

Restore the most recent version of a dropped external volume named `my_external_volume`:

```sqlexample
UNDROP EXTERNAL VOLUME my_external_volume;
```
