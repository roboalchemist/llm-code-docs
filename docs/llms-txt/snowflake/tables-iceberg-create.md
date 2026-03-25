# Source: https://docs.snowflake.com/en/user-guide/tables-iceberg-create.md

# Create an Apache Iceberg™ table in Snowflake

Create [Apache Iceberg™ tables](tables-iceberg.md) in Snowflake for different [Catalog options](tables-iceberg.md).
You can create an Iceberg table by using the [CREATE ICEBERG TABLE](../sql-reference/sql/create-iceberg-table.md) command.

> **Note:**
>
> * To create an Iceberg table, you must have a running warehouse that is specified as the current warehouse for your session.
>   Errors might occur if no running warehouse is specified when you create an Iceberg table.
>   For more information, see [Working with Warehouses](warehouses-tasks.md).
> * To create an Iceberg table that works with [Snowflake Open Catalog](https://other-docs.snowflake.com/en/opencatalog/overview), see [Use Apache Iceberg™ tables with Snowflake Open Catalog in Snowflake](tables-iceberg-open-catalog.md).

## Snowflake-managed

To create an Iceberg table with Snowflake as the catalog,
you must specify an [external volume](tables-iceberg.md) and a base location (directory on the external volume)
where Snowflake can write table data and metadata.
For instructions on creating an external volume, see [Configure an external volume](tables-iceberg-configure-external-volume.md).

To define table columns, you can use Iceberg data types. For more information, see [Data types for Apache Iceberg™ tables](tables-iceberg-data-types.md).

The following example creates an Iceberg table with Snowflake as the Iceberg catalog, and uses the value of the column named `int_col`
to [partition the table](tables-iceberg-metadata.md):

```sqlexample
CREATE OR REPLACE ICEBERG TABLE my_iceberg_table (
    boolean_col boolean,
    int_col int,
    long_col long,
    float_col float,
    double_col double,
    decimal_col decimal(10,5),
    string_col string,
    fixed_col fixed(10),
    binary_col binary,
    date_col date,
    time_col time,
    timestamp_ntz_col timestamp_ntz(6),
    timestamp_ltz_col timestamp_ltz(6)
  )
  PARTITION BY (int_col)
  CATALOG = 'SNOWFLAKE'
  EXTERNAL_VOLUME = 'my_ext_vol'
  BASE_LOCATION = 'my/relative/path/from/extvol';
```

> **Note:**
>
> Alternatively, use variant syntax.
> For more information, see [CREATE TABLE … AS SELECT](../sql-reference/sql/create-iceberg-table-snowflake.md) and
> [CREATE ICEBERG TABLE … LIKE](../sql-reference/sql/create-iceberg-table-snowflake.md).

After you create a table that uses Snowflake as the catalog, you can take actions such as:

* [Generating snapshots](tables-iceberg-manage.md)
* [Querying the table](tables-iceberg-manage.md)
* [Updating the table](tables-iceberg-manage.md)

For more information, see [Manage Apache Iceberg™ tables](tables-iceberg-manage.md).

## External catalog

To create an Iceberg table that uses an external catalog, or no catalog at all, you must specify an
[external volume](tables-iceberg.md) and a [catalog integration](tables-iceberg.md).
If you use an external Iceberg catalog, you might also need to specify additional parameters. For example, when you use AWS Glue as the catalog,
you must specify a catalog table name.

When you create an Iceberg table that uses an external catalog, Snowflake performs an initial metadata refresh.
You can also manually refresh the table metadata using the [ALTER ICEBERG TABLE … REFRESH](../sql-reference/sql/alter-iceberg-table-refresh.md) command to
synchronize the metadata with the most recent table changes. For more information, see [Refresh the table metadata](tables-iceberg-manage.md).

> **Note:**
>
> The CREATE ICEBERG TABLE command supports different options for different external catalogs. The examples in this section specify only
> some of the available options. To view the full syntax, see the following pages:
>
> > * [CREATE ICEBERG TABLE (AWS Glue as the Iceberg catalog)](../sql-reference/sql/create-iceberg-table-aws-glue.md)
> > * [CREATE ICEBERG TABLE (Iceberg files in object storage)](../sql-reference/sql/create-iceberg-table-iceberg-files.md)
> > * [CREATE ICEBERG TABLE (Delta files in object storage)](../sql-reference/sql/create-iceberg-table-delta.md)
> > * [CREATE ICEBERG TABLE (Iceberg REST catalog)](../sql-reference/sql/create-iceberg-table-rest.md)
>
> You can also configure data governance (for example, masking or row access policies)
> for externally managed tables by using [ALTER ICEBERG TABLE](../sql-reference/sql/alter-iceberg-table.md).

### Iceberg files in object storage

The following example creates an Iceberg table from Iceberg metadata in external cloud storage,
specifying a relative path to the table metadata on the external volume (`METADATA_FILE_PATH`).

```sqlexample
CREATE ICEBERG TABLE myIcebergTable
  EXTERNAL_VOLUME='icebergMetadataVolume'
  CATALOG='icebergCatalogInt'
  METADATA_FILE_PATH='path/to/metadata/v1.metadata.json';
```

### Delta files in object storage

The following example command creates an Iceberg table from Delta table files in object storage with
[automated refresh](tables-iceberg-auto-refresh.md).

The example specifies an external volume associated with the cloud location of the Delta table files,
a [catalog integration configured for Delta](tables-iceberg-configure-catalog-integration-object-storage.md),
and a value for the required `BASE_LOCATION` parameter.

```sqlexample
CREATE ICEBERG TABLE my_delta_iceberg_table
  CATALOG = delta_catalog_integration
  EXTERNAL_VOLUME = delta_external_volume
  BASE_LOCATION = 'relative/path/from/ext/vol/'
  AUTO_REFRESH = TRUE;
```

If the Delta table uses a partitioning scheme, Snowflake automatically interprets the scheme from the Delta log.

### Apache Iceberg™ REST catalog

The following example creates a table that uses a remote
[Iceberg REST catalog](tables-iceberg-configure-catalog-integration-rest.md).

```sqlexample
CREATE OR REPLACE ICEBERG TABLE my_iceberg_table
  EXTERNAL_VOLUME = 'my_external_volume'
  CATALOG = 'my_rest_catalog_integration'
  CATALOG_TABLE_NAME = 'my_remote_table'
  AUTO_REFRESH = TRUE;
```

For more examples by use case, see the following topics:

* [Use a catalog-linked database for Apache Iceberg™ tables](tables-iceberg-catalog-linked-database.md)
* [Write support for externally managed Apache Iceberg™ tables](tables-iceberg-externally-managed-writes.md)
* [Use catalog-vended credentials for Apache Iceberg™ tables](tables-iceberg-configure-catalog-integration-vended-credentials.md)
* [Query a table in Snowflake Open Catalog using Snowflake](tables-iceberg-open-catalog-query.md)
