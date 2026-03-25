# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-iceberg-table.md

# DROP ICEBERG TABLE

Removes an [Apache Iceberg™ table](../../user-guide/tables-iceberg.md) from the current/specified schema, but retains a version of the
Iceberg table so that it can be recovered using [UNDROP ICEBERG TABLE](undrop-iceberg-table.md). For more information, see Usage Notes (in this topic).

Note that this topic refers to Iceberg tables as simply “tables” except where specifying *Iceberg tables* avoids confusion.

See also:
:   [CREATE ICEBERG TABLE](create-iceberg-table.md) , [SHOW ICEBERG TABLES](show-iceberg-tables.md) , [UNDROP ICEBERG TABLE](undrop-iceberg-table.md)

## Syntax

```sqlsyntax
DROP [ ICEBERG ] TABLE [ IF EXISTS ] <name> [ CASCADE | RESTRICT ]
```

## Parameters

`name`
:   Specifies the identifier for the table to drop. If the identifier contains spaces, special characters, or mixed-case characters, the
    entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive
    (for example, `"My Object"`).

    If the table identifier is not fully qualified (in the form of `db_name.schema_name.table_name` or
    `schema_name.table_name`), the command looks for the table in the current schema for the session.

`CASCADE | RESTRICT`
:   Specifies whether the table can be dropped if foreign keys exist that reference the table:

    * `CASCADE` drops the table even if the table has primary/unique keys that are referenced by foreign keys in other tables.
    * `RESTRICT` returns a warning about existing foreign key references and does not drop the table.

    Default: `CASCADE`

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Iceberg table | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |
| USAGE | External volume |  |
| USAGE | Integration (catalog) | Required if the Iceberg table uses an external catalog. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* For [externally managed Iceberg tables with writes enabled](../../user-guide/tables-iceberg-externally-managed-writes.md),
  Snowflake also instructs your external Iceberg REST catalog to drop the table.
  Snowflake makes a call to your remote Iceberg catalog, instructing it to drop the table and delete the table’s underlying data and metadata.

  Snowflake only drops the table after confirming that the table has successfully been dropped from the remote catalog.

  > **Note:**
  >
  > If you use the AWS Glue Data Catalog as your external catalog, dropping an externally managed table through Snowflake does not delete
  > the underlying table files. This behavior is specific to the AWS Glue Data Catalog implementation.
* Dropping a table does not permanently remove it from the system. Snowflake retains a version of the dropped table in
  [Time Travel](../../user-guide/data-time-travel.md) for the number of days specified by the `DATA_RETENTION_TIME_IN_DAYS` parameter for
  the table. For more information, see [Metadata and snapshots for Iceberg tables](../../user-guide/tables-iceberg.md).
* Within the Time Travel retention period, you can restore a dropped table by using the [UNDROP ICEBERG TABLE](undrop-iceberg-table.md) command.
* After a dropped table has been purged, it cannot be recovered; it must be recreated.
* After dropping a table, creating a table with the same name creates a new version of the table. You can restore
  the dropped version of the previous table with the following steps:

  1. Rename the current version of the table to a different name.
  2. Use the [UNDROP ICEBERG TABLE](undrop-iceberg-table.md) command to restore the previous version.
* Before you drop a table, verify that no views reference the table. Dropping a table that is referenced by a view
  invalidates the view (querying the view returns an “object does not exist” error).

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

Drop a table:

> ```sqlexample
> DROP ICEBERG TABLE t2;
>
> +--------------------------+
> | status                   |
> |--------------------------|
> | T2 successfully dropped. |
> +--------------------------+
> ```

Drop the table again, but don’t raise an error if the table doesn’t exist:

> ```sqlexample
> DROP ICEBERG TABLE IF EXISTS t2;
>
> +------------------------------------------------------------+
> | status                                                     |
> |------------------------------------------------------------|
> | Drop statement executed successfully (T2 already dropped). |
> +------------------------------------------------------------+
> ```
