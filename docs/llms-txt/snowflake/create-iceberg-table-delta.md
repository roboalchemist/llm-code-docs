# Source: https://docs.snowflake.com/en/sql-reference/sql/create-iceberg-table-delta.md

# CREATE ICEBERG TABLE (Delta files in object storage)

Creates or replaces an [Apache Iceberg™ table](../../user-guide/tables-iceberg.md) in the current/specified schema
using Delta table files in object storage (external cloud storage).
This type of Iceberg table requires a [catalog integration](../../user-guide/tables-iceberg.md).

This topic refers to Iceberg tables as simply “tables” except where specifying *Iceberg tables* avoids confusion.

> **Note:**
>
> Before creating a table, you must create the [external volume](create-external-volume.md) where the Iceberg metadata
> and data files are stored.
> For instructions, see [Configure an external volume](../../user-guide/tables-iceberg-configure-external-volume.md).
>
> You also need a catalog integration for the table.
> For more information, see [Configure a catalog integration for files in object storage](../../user-guide/tables-iceberg-configure-catalog-integration-object-storage.md).

See also:
:   [ALTER ICEBERG TABLE](alter-iceberg-table.md) , [DROP ICEBERG TABLE](drop-iceberg-table.md) , [SHOW ICEBERG TABLES](show-iceberg-tables.md) , [DESCRIBE ICEBERG TABLE](desc-iceberg-table.md) , [UNDROP ICEBERG TABLE](undrop-iceberg-table.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] ICEBERG TABLE [ IF NOT EXISTS ] <table_name>
  [ EXTERNAL_VOLUME = '<external_volume_name>' ]
  [ CATALOG = '<catalog_integration_name>' ]
  BASE_LOCATION = '<relative_path_from_external_volume>'
  [ REPLACE_INVALID_CHARACTERS = { TRUE | FALSE } ]
  [ AUTO_REFRESH = { TRUE | FALSE } ]
  [ COMMENT = '<string_literal>' ]
  [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
  [ WITH CONTACT ( <purpose> = <contact_name> [ , <purpose> = <contact_name> ... ] ) ]
```

## Required parameters

`table_name`
:   Specifies the identifier (name) for the table; must be unique for the schema in which the table is created.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`BASE_LOCATION = 'relative_path_from_external_volume'`
:   Specifies a relative path from the table’s `EXTERNAL_VOLUME` location to a directory where Snowflake can access your Delta
    table files.

    The base location must point to a directory and cannot point to a single file.
    It must contain the Delta transaction log subfolder (for example, `my/base/location/_delta_log/`).

## Optional parameters

`EXTERNAL_VOLUME = 'external_volume_name'`
:   Specifies the identifier (name) for the external volume where the Iceberg table stores its metadata files and data in Parquet
    format. Iceberg metadata and manifest files store the table schema, partitions, snapshots, and other metadata.

    If you don’t specify this parameter, the Iceberg table defaults to the external volume for the schema, database, or account.
    The schema takes precedence over the database, and the database takes precedence over the account.

`CATALOG = 'catalog_integration_name'`
:   Specifies the identifier (name) of the catalog integration for this table.

    If not specified, the Iceberg table defaults to the catalog integration for the schema, database, or account.
    The schema takes precedence over the database, and the database takes precedence over the account.

`REPLACE_INVALID_CHARACTERS = { TRUE | FALSE }`
:   Specifies whether to replace invalid UTF-8 characters with the Unicode replacement character (�) in query results.
    You can only set this parameter for tables that use an external Iceberg catalog.

    * `TRUE` replaces invalid UTF-8 characters with the Unicode replacement character.
    * `FALSE` leaves invalid UTF-8 characters unchanged. Snowflake returns a user error message when it encounters invalid UTF-8
      characters in a Parquet data file.

    If not specified, the Iceberg table defaults to the parameter value for the schema, database, or account.
    The schema takes precedence over the database, and the database takes precedence over the account.

    Default: `FALSE`

`AUTO_REFRESH = { TRUE | FALSE }`
:   Specifies whether Snowflake should automatically poll your external cloud storage for updates.

    If no value is specified for the `REFRESH_INTERVAL_SECONDS` parameter on the catalog integration, Snowflake uses a default
    refresh interval of 30 seconds.

    For more information, see [automated refresh](../../user-guide/tables-iceberg-auto-refresh.md).

    Default: FALSE

    > > **Note:**
    > >
    > > Using AUTO_REFRESH with INFER_SCHEMA isn’t supported.

`COMMENT = 'string_literal'`
:   Specifies a comment for the table.

    Default: No value

`TAG ( tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ] )`
:   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

    The tag value is always a string, and the maximum number of characters for the tag value is 256.

    For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

`WITH CONTACT ( purpose = contact [ , purpose = contact ...] )`
:   Associate the new object with one or more [contacts](../../user-guide/contacts-using.md).

    Specify the WITH CONTACT clause after all other clauses except the AS clause (if that clause is supported by this command).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE ICEBERG TABLE | Schema |  |
| CREATE EXTERNAL VOLUME | Account | Required to create a new external volume. |
| USAGE | External Volume | Required to reference an existing external volume. |
| CREATE INTEGRATION | Account | Required to create a new catalog integration. |
| USAGE | Catalog integration | Required to reference an existing catalog integration. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Considerations for running this command:

  * If you created your external volume or catalog integration using a double-quoted identifier,
    you must specify the identifier exactly as created (including the double quotes) in your CREATE ICEBERG TABLE statement.
    Failure to include the quotes might result in an `Object does not exist` error (or
    similar type of error).
* Considerations for Iceberg tables created from Delta table files:

  * You can use [Time Travel](../../user-guide/data-time-travel.md) to query Iceberg tables created from Delta table files.
    The table versions correspond to the individual Delta log commit files.
  * Snowflake supports minReaderVersion 3 and can read all tables written by engines that use the latest version of Delta Lake,
    which is 4.0.0. Delta Lake version 4.0.0 includes support for deletion vectors and liquid clustering.
  * Snowflake streams aren’t supported for Iceberg tables created from Delta table files with partition columns.
    However, insert-only streams for tables created from Delta files *without* partition columns are supported.
  * Iceberg tables created from Delta files that were created before the [2024_04](../../release-notes/bcr-bundles/2025_04_bundle.md) release bundle are not supported in dynamic tables.
  * Snowflake doesn’t support creating Iceberg tables from Delta table definitions in the AWS Glue Data Catalog.
  * Parquet files (data files for Delta tables) that use any of the following features or data types aren’t supported:

    * Field IDs.
    * The INTERVAL data type.
    * The DECIMAL data type with precision higher than 38.
    * LIST or MAP types with one-level or two-level representation.
    * Unsigned integer types (INT(signed = false)).
    * The FLOAT16 data type.
  * You can use the Parquet physical type `int96` for TIMESTAMP, but Snowflake doesn’t support `int96` for TIMESTAMP_NTZ.
  * For more information about Delta data types and Iceberg tables, see [Delta data types](../../user-guide/tables-iceberg-data-types.md).
  * Snowflake processes a maximum of 1000 Delta commit files each time you refresh a table using CREATE/ALTER … REFRESH.
    If your table has over 1000 commit files, you can do additional manual refreshes.
    Each time, the refresh process continues from where the last one stopped.

    > **Note:**
    >
    > Snowflake uses Delta checkpoint files when creating an Iceberg table.
    > The 1,000 commit file limit only applies to commits after the latest checkpoint.
    >
    > When you refresh an existing table, Snowflake processes Delta commit files, but not checkpoint files. If table maintenance removes stale log and data files for the source
    > Delta table, you should refresh Delta-based
    > Iceberg tables in Snowflake more frequently than the retention period of Delta logs and data files.
  * The following Delta Lake features aren’t currently supported: Row Tracking, change data files, change metadata,
    DataChange, CDC, protocol evolution.
* Considerations for creating tables:

  > * A schema cannot contain tables and/or views with the same name. When creating a table:
  >
  >   > * If a view with the same name already exists in the schema, an error is returned and the table is not created.
  >   > * If a table with the same name already exists in the schema, an error is returned and the table is not created, unless the optional
  >   >   `OR REPLACE` keyword is included in the command.
  > * CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.
  >
  >   This means that any queries concurrent with the CREATE OR REPLACE ICEBERG TABLE operation use either the old or new table version.
  > * The `OR REPLACE` and `IF NOT EXISTS` clauses are mutually exclusive. They can’t both be used in the same statement.
  > * Similar to [reserved keywords](../reserved-keywords.md), ANSI-reserved function names
  >   ([CURRENT_DATE](../functions/current_date.md), [CURRENT_TIMESTAMP](../functions/current_timestamp.md), etc.) cannot be used as column names.
  > * Recreating a table (using the optional `OR REPLACE` keyword) drops its history, which makes any stream on the table stale. A stale
  >   stream is unreadable.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

The following example command creates an Iceberg table from Delta table files in object storage with
[automated refresh](../../user-guide/tables-iceberg-auto-refresh.md).

The example specifies an external volume associated with the cloud location of the Delta table files,
a [catalog integration configured for Delta](../../user-guide/tables-iceberg-configure-catalog-integration-object-storage.md),
and a value for the required `BASE_LOCATION` parameter.

```sqlexample
CREATE ICEBERG TABLE my_delta_iceberg_table
  CATALOG = delta_catalog_integration
  EXTERNAL_VOLUME = delta_external_volume
  BASE_LOCATION = 'relative/path/from/ext/vol/'
  AUTO_REFRESH = TRUE;
```

If the Delta table uses a partitioning scheme, Snowflake automatically interprets the scheme from the Delta log.
