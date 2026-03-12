# Source: https://docs.snowflake.com/en/user-guide/tables-iceberg-manage.md

# Manage Apache Iceberg™ tables

Manage [Apache Iceberg™ tables](tables-iceberg.md) in Snowflake:

* Query a table
* Use DML commands
* Generate snapshots of DML changes
* Use row-level deletes
* Set a target file size
* Table optimization for Snowflake-managed Iceberg tables
* Maintain tables that use an external catalog
* Refresh the table metadata
* Retrieve storage metrics
* Set data compaction
* Use default values with Iceberg tables
* Use row lineage with Iceberg tables

You can also convert an Iceberg table that uses an external catalog into a table that uses Snowflake as the Iceberg catalog.
To learn more, see [Convert an Apache Iceberg™ table to use Snowflake as the catalog](tables-iceberg-conversion.md).

## Query a table

To query an Iceberg table, a user must be granted or inherit the following privileges:

* The USAGE privilege on the database and schema that contain the table
* The SELECT privilege on the table

You can query an Iceberg table using a SELECT statement. For example:

```sqlexample
SELECT col1, col2 FROM my_iceberg_table;
```

> **Note:**
>
> Along with Snowflake, you can also use an external query engine to query Iceberg tables. For more information,
> see [Use an external query engine with Apache Iceberg™ tables](tables-iceberg-use-external-query-engine.md).

## Use DML commands

Iceberg tables that use Snowflake as the catalog support full [Data Manipulation Language (DML) commands](../sql-reference/sql-dml.md),
including the following:

* [INSERT](../sql-reference/sql/insert.md)
* [MERGE](../sql-reference/sql/merge.md)
* [UPDATE](../sql-reference/sql/update.md)
* [DELETE](../sql-reference/sql/delete.md)
* [TRUNCATE TABLE](../sql-reference/sql/truncate-table.md)

Snowflake-managed tables also support efficient bulk loading using features such as [COPY INTO <table>](../sql-reference/sql/copy-into-table.md)
and [Snowpipe](data-load-snowpipe-intro.md). For more information,
see [Load data into Apache Iceberg™ tables](tables-iceberg-load.md).

> **Note:**
>
> * Snowflake also supports writing to externally managed Iceberg tables. For more information, see [Write support for externally managed Apache Iceberg™ tables](tables-iceberg-externally-managed-writes.md)
>   and [Writing to externally managed Iceberg tables](tables-iceberg-externally-managed-writes.md).
> * For Snowflake-managed Iceberg tables, if a DML operation fails unexpectedly and rolls back, some Parquet files might get written to your
>   external cloud storage but won’t be tracked or referenced by your Iceberg table metadata. These Parquet files are orphan files.
>
>   If you see a mismatch between storage usage for your
>   external cloud storage and Snowflake, you might have orphan files in your external cloud storage. To see your storage usage for Snowflake,
>   you can use the [TABLE_STORAGE_METRICS view](../sql-reference/info-schema/table_storage_metrics.md) or [TABLE_STORAGE_METRICS view](../sql-reference/account-usage/table_storage_metrics.md).
>   If you see a mismatch, contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support) for assistance with determining whether you have orphan files and removing them.

### Example: Update a table

You can use [INSERT](../sql-reference/sql/insert.md) and [UPDATE](../sql-reference/sql/update.md) statements to modify Snowflake-managed Iceberg tables.

The following example inserts a new value into an Iceberg table named `store_sales`,
then updates the `cola` column to 1 if the value is currently -99.

```sqlexample
INSERT INTO store_sales VALUES (-99);

UPDATE store_sales
  SET cola = 1
  WHERE cola = -99;
```

## Generate snapshots of DML changes

For tables that use Snowflake as the catalog, Snowflake automatically generates the Iceberg metadata. Snowflake writes
the metadata to a folder named `metadata` on your external volume. To find the `metadata` folder,
see [Data and metadata directories](tables-iceberg-storage.md).

Alternatively, you can call the [SYSTEM$GET_ICEBERG_TABLE_INFORMATION](../sql-reference/functions/system_get_iceberg_table_information.md) function to generate Iceberg metadata
for any new changes.

For tables that aren’t managed by Snowflake, the function returns information about the latest refreshed snapshot.

For example:

```sqlexample
SELECT SYSTEM$GET_ICEBERG_TABLE_INFORMATION('db1.schema1.it1');
```

Output:

```output
+-----------------------------------------------------------------------------------------------------------+
| SYSTEM$GET_ICEBERG_TABLE_INFORMATION('DB1.SCHEMA1.IT1')                                                   |
|-----------------------------------------------------------------------------------------------------------|
| {"metadataLocation":"s3://mybucket/metadata/v1.metadata.json","status":"success"}                         |
+-----------------------------------------------------------------------------------------------------------+
```

## Use row-level deletes

Snowflake supports querying tables with row-level deletes and writing to tables by using row-level deletes.

### Query tables

Snowflake supports querying [externally managed Iceberg tables](tables-iceberg.md) when you’ve configured
[row-level deletes](https://iceberg.apache.org/spec/#row-level-deletes) for update, delete, and merge operations.

To configure row-level deletes, see
[Write properties](https://iceberg.apache.org/docs/latest/configuration/#write-properties) in the Apache Iceberg documentation.

### Write to tables by using positional delete files

> **Note:**
>
> * Supported for externally managed Iceberg tables only.
> * To use position row-level deletes, ensure that the Iceberg version for Iceberg tables is set to v2, which is the default. For
>   more information, see [ICEBERG_VERSION_DEFAULT](../sql-reference/parameters.md). If
>   the Iceberg version is set to v3, the merge-on-read behavior in Snowflake is to use deletion vectors.

Snowflake supports position row-level deletes for writing to externally managed Iceberg tables stored on Amazon S3, Azure, or
Google Cloud. To turn off position deletes, which enable running the DML operations in copy-on-write mode, set the
`ENABLE_ICEBERG_MERGE_ON_READ` parameter to FALSE at the table, schema, or database level.

### Write to tables by using deletion vectors

To optimize row-level data
modifications, Snowflake supports deletion vectors for writing to externally managed and Snowflake-managed Iceberg tables stored on Amazon
S3, Azure, or
Google Cloud. With deletion vectors, Snowflake can perform “merge-on-read” (MOR) operations, which improve write performance
for the following DML statements:

* DELETE
* UPDATE
* MERGE

Snowflake achieves this performance by writing small vector files instead of rewriting large data files. For more information, see
[Deletion vectors](https://iceberg.apache.org/spec/#deletion-vectors) in the Apache Iceberg specification.

#### Enable deletion vectors

To enable deletion vectors, complete the following steps:

1. Set the default Iceberg version for Iceberg tables to v3 by following the instructions in [Configure the default Iceberg version](tables-iceberg-v3-specification-support.md).

   > **Note:**
   >
   > If the default Iceberg version for Iceberg tables is v2, Snowflake performs “merge-on-read” (MOR) operations by using
   > positional delete files.
2. Set the `ENABLE_ICEBERG_MERGE_ON_READ` parameter to `TRUE`, which is the default, by following the instructions in [ENABLE_ICEBERG_MERGE_ON_READ](../sql-reference/parameters.md).
3. To run DML operations in copy-on-write mode, set the `ENABLE_ICEBERG_MERGE_ON_READ` parameter to FALSE.

#### Usage notes for deletion vectors

* **Default behavior**

  * The system default for ENABLE_ICEBERG_MERGE_ON_READ is TRUE.
* **Write method heuristics**

  * When ENABLE_ICEBERG_MERGE_ON_READ is set to TRUE, Snowflake uses heuristics to decide per-file whether to use merge-on-read or
    copy-on-write:

    * **Row count:** Snowflake only writes a deletion vector if fewer than ~5% of rows in a data file are deleted. If ≥5% are deleted, Snowflake
      rewrites the file by using copy-on-write.
    * **File size:** For Snowflake to write deletion vectors, the data file must be larger than approximately 1.6 MB.
* **Compatibility**

  * If you use compute engines that don’t yet support Iceberg v3 deletion vectors, set ENABLE_ICEBERG_MERGE_ON_READ to FALSE to enforce
    copy-on-write for all writes.
* **Parameter precedence**

  * Snowflake only checks the ENABLE_ICEBERG_MERGE_ON_READ parameter to determine the write method. It doesn’t recognize the following Iceberg
    table properties:

    * write.delete.mode
    * write.update.mode
    * write.merge.mode

### Copy-on-write vs. merge-on-read

Iceberg provides two modes for configuring how compute engines handle row-level operations for externally
managed tables. Snowflake supports both of these modes.

The following table describes when you might want to use each mode:

| Mode | Description |
| --- | --- |
| Copy-on-write (default) | This mode prioritizes read time and affects write speed.  When you perform an update, delete, or merge operation, your compute engine rewrites the entire affected Parquet data file. This can result in slow writes, especially if you have large data files, but doesn’t impact read time.  This is the default mode. |
| Merge-on-read | This mode prioritizes write speed and slightly affects read time.  When you perform an update, delete, or merge operation, your compute engine creates a delete file that contains information about only the changed rows.  When you read from a table, your query engine merges delete files with data files. Merging can increase read time. However, you can optimize read performance by scheduling regular compaction and table maintenance. |

For more information about row-level changes for Iceberg, see [Row-level deletes](https://iceberg.apache.org/spec/#row-level-deletes) in the
Apache Iceberg documentation.

### Considerations and limitations

Consider the following information when you use row-level deletes with Iceberg tables:

* Snowflake supports [position deletes](https://iceberg.apache.org/spec/#position-delete-files) only for v2 Iceberg tables, and
  [deletion vectors](https://iceberg.apache.org/spec/#deletion-vectors) for v3 Iceberg tables.
* Snowflake only supports position deletes with externally managed Iceberg tables.
* For the best read performance when you use row-level deletes, perform regular compaction and table maintenance to remove old delete files. For
  information, see Maintain tables that use an external catalog.
* Excessive position deletes, especially dangling position deletes, might prevent table creation and refresh operations.
  To avoid this issue, perform table maintenance to remove extra position deletes.

  The table maintenance method to use depends on your external Iceberg engine. For example, you can use the `rewrite_data_files` method
  for Spark with the `delete-file-threshold` or `rewrite-all` options. For more information, see
  [rewrite_data_files](https://iceberg.apache.org/docs/latest/spark-procedures/#rewrite_data_files) in the Apache Iceberg™ documentation.

## Set a target file size

To improve query performance for external Iceberg engines such as
Spark or Trino, you can configure a target file size for both Snowflake-managed and
[externally managed Iceberg tables with write support](tables-iceberg-externally-managed-writes.md). You can either set a
specific size (16MB, 32MB, 64MB, or 128MB), or use the AUTO option. AUTO works differently, depending on the table type:

* Snowflake-managed tables: AUTO specifies that Snowflake should choose the file size for the table based on table characteristics
  such as size, DML patterns, ingestion workload, and clustering configuration. Snowflake automatically
  adjusts the file size, starting at 16 MB, for better read and write performance in Snowflake.
* Externally managed tables: AUTO specifies that Snowflake should aggressively scale to a larger file size.

You can set the target file size when you create an Iceberg table, or run the ALTER ICEBERG TABLE command
to change the target file size for an existing Iceberg table.
Snowflake attempts to maintain file sizes close to the target size when writing Parquet files for a table.

After you set a target file size, Snowflake immediately starts to create larger files for new Data Manipulation Language (DML) operations.
Snowflake’s table maintenance operations asynchronously change the existing table files according to the target file size.

The following example uses TARGET_FILE_SIZE to set a target file size of 128 MB for a Snowflake-managed table:

```sqlexample
CREATE ICEBERG TABLE my_iceberg_table (col1 INT)
  CATALOG = 'SNOWFLAKE'
  EXTERNAL_VOLUME = 'my_external_volume'
  BASE_LOCATION = 'my_iceberg_table'
  TARGET_FILE_SIZE = '128MB';
```

Alternatively, use [ALTER ICEBERG TABLE](../sql-reference/sql/alter-iceberg-table.md) to set the TARGET_FILE_SIZE property for an existing table:

```sqlexample
ALTER ICEBERG TABLE my_iceberg_table
  SET TARGET_FILE_SIZE = '32MB';
```

To check the value of the TARGET_FILE_SIZE property for a table, use the [SHOW PARAMETERS](../sql-reference/sql/show-parameters.md) command:

```sqlexample
SHOW PARAMETERS LIKE 'target_file_size' FOR my_iceberg_table;
```

## Table optimization for Snowflake-managed Iceberg tables

Table optimization automatically performs maintenance to improve the performance and reduce the storage costs of your Snowflake-managed Iceberg tables.

> **Note:**
>
> * Snowflake doesn’t support orphan file deletion for Snowflake-managed Iceberg tables. If you see a mismatch between storage usage for your
>   external cloud storage and Snowflake, you might have orphan files in your external cloud storage. To see your storage usage for Snowflake,
>   you can use the [TABLE_STORAGE_METRICS view](../sql-reference/info-schema/table_storage_metrics.md) or [TABLE_STORAGE_METRICS view](../sql-reference/account-usage/table_storage_metrics.md).
>   If you see a mismatch, contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support) for assistance with determining whether you have orphan files and removing them.
> * To improve query performance, you can also set a target file size. For more information, see Set a target file size.

Snowflake supports the Iceberg table optimization features summarized in the following table:

| Feature | Improves query performance | Reduces storage costs | Notes |
| --- | --- | --- | --- |
| Automatic Clustering [1] | ✔ | ✔ | *Billed.* Disabled by default. |
| Data compaction | ✔ | ✔ | *Billed.* Enabled by default. |
| Manifest compaction | ✔ | ✔ | *No cost.* Enabled automatically; you can’t disable it. |
| Snapshot expiry | ✔ | ✔ | *No cost.* Enabled automatically; you can’t disable it. |

[1] Unlike the other table optimization features, Automatic Clustering is billed separately as a standalone feature.

### Automatic Clustering

Automatic Clustering reorganizes data within files or partitions based on frequently queried columns. The file size for Iceberg tables is
based on your clustering configuration, unless you set a target file size. If you do, the file size is the
specific size you set. For more information, see Set a target file size.

To set Automatic Clustering,
specify the CLUSTER BY parameter when you create a Snowflake-managed Iceberg table or modify an existing table. For more information, see:

* [CREATE ICEBERG TABLE (Snowflake as the Iceberg catalog)](../sql-reference/sql/create-iceberg-table-snowflake.md)
* [ALTER ICEBERG TABLE](../sql-reference/sql/alter-iceberg-table.md)

For more information about Automatic Clustering, see [Automatic Clustering](tables-auto-reclustering.md).

### Data compaction

Data compaction combines small files into larger, more efficient files to manage storage, maintain an optimal file size, and improve query
performance.

In most cases, data compaction doesn’t have a significant effect on compute costs, but if these costs are a concern, you
can disable compaction. For example, you might want to disable compaction on a table if you rarely query it. To disable or enable data
compaction, see Set data compaction.

> **Note:**
>
> * To query data compaction jobs for Iceberg tables, see [ICEBERG_STORAGE_OPTIMIZATION_HISTORY view](../sql-reference/account-usage/iceberg_storage_optimization_history.md).
>   This view includes the number of credits that are billed for data compaction.
> * If you have [Automatic Clustering](tables-auto-reclustering.md) enabled, clustering performs data compaction on the table. This is
>   true, regardless of whether data compaction is enabled or disabled on the table.
> * You also have the option to set a target file size. For more information, see
>   Set a target file size.

### Manifest compaction

Manifest compaction optimizes the metadata layer by reorganizing and combining smaller manifest files. This compaction reduces metadata
overhead and improves query performance.

This feature is enabled automatically and you can’t disable it.

### Snapshot expiry

Snapshot expiry systematically deletes old snapshots and their unique data and metadata files from the table’s history. This deletion is
based on predefined retention policies.

This feature is enabled automatically and you can’t disable it.

## Maintain tables that use an external catalog

You can perform maintenance operations on Iceberg tables that use an external catalog.

Maintenance operations include the following:

* Expiring snapshots
* Removing old metadata files
* Compacting data files

> **Important:**
>
> To keep your Iceberg table in sync with external changes, it’s important to align your Snowflake refresh schedule with table maintenance.
> Refresh the table each time you perform a maintenance operation.

To learn about maintenance for Iceberg tables that aren’t managed by Snowflake,
see [Maintenance](https://iceberg.apache.org/docs/latest/maintenance/) in the Apache Iceberg documentation.

## Refresh the table metadata

When you use an external Iceberg catalog, you can refresh the table metadata using the [ALTER ICEBERG TABLE … REFRESH](../sql-reference/sql/alter-iceberg-table-refresh.md) command.
Refreshing the table metadata synchronizes the metadata with the most recent table changes.

> **Note:**
>
> We recommend setting up [automated refresh](tables-iceberg-auto-refresh.md) for supported externally managed tables.

### Refresh the metadata for a table

The following example manually refreshes the metadata for a table that uses an external catalog (for example, AWS Glue or Delta).
Refreshing the table keeps the table in sync with any changes that have occurred in the remote catalog.

With this type of Iceberg table, you don’t specify a metadata file path in the command.

```sqlexample
ALTER ICEBERG TABLE my_iceberg_table REFRESH;
```

To keep a table updated automatically, you can set up [automated refresh](tables-iceberg-auto-refresh.md).
Use the [ALTER ICEBERG TABLE](../sql-reference/sql/alter-iceberg-table.md) command.

For example:

```sqlexample
ALTER ICEBERG TABLE my_iceberg_table SET AUTO_REFRESH = TRUE;
```

### Refresh the metadata for a table created from Iceberg files

The following example manually refreshes a table created from *Iceberg metadata files* in an external cloud storage location,
specifying the relative path to a metadata file without the leading forward slash (`/`).
The metadata file defines the data in the table after refreshing.

```sqlexample
ALTER ICEBERG TABLE my_iceberg_table REFRESH 'metadata/v1.metadata.json';
```

## Retrieve storage metrics

Snowflake does not bill your account for Iceberg table storage costs. However, you can track how much storage an Iceberg table occupies
by querying the TABLE_STORAGE_METRICS and TABLES views in the [Snowflake Information Schema](../sql-reference/info-schema.md) or [Account Usage](../sql-reference/account-usage.md) schema.

The following example query joins the ACCOUNT_USAGE.TABLE_STORAGE_METRICS view with the ACCOUNT_USAGE.TABLES view, filtering on
the TABLES.IS_ICEBERG column.

```sqlexample
SELECT metrics.* FROM
  snowflake.account_usage.table_storage_metrics metrics
  INNER JOIN snowflake.account_usage.tables tables
  ON (
    metrics.id = tables.table_id
    AND metrics.table_schema_id = tables.table_schema_id
    AND metrics.table_catalog_id = tables.table_catalog_id
  )
  WHERE tables.is_iceberg='YES';
```

## Set data compaction

You can set data compaction on Snowflake-managed Iceberg tables when you create a database, schema, or table, or run the ALTER command to
change the setting for an existing database, schema, or table. You can also set data compaction at the account level by using the [ALTER ACCOUNT](../sql-reference/sql/alter-account.md)
command. For more information about data compaction, see Data compaction.

The following example uses ENABLE_DATA_COMPACTION to disable data compaction for a Snowflake-managed table:

```sqlexample
CREATE ICEBERG TABLE my_iceberg_table (col1 INT)
  CATALOG = 'SNOWFLAKE'
  EXTERNAL_VOLUME = 'my_external_volume'
  BASE_LOCATION = 'my_iceberg_table'
  ENABLE_DATA_COMPACTION = FALSE;
```

Alternatively, use [ALTER ICEBERG TABLE](../sql-reference/sql/alter-iceberg-table.md) to disable it for an existing table.

```sqlexample
ALTER ICEBERG TABLE my_iceberg_table
  SET ENABLE_DATA_COMPACTION = FALSE;
```

For more information, see:

* [ENABLE_DATA_COMPACTION](../sql-reference/parameters.md)
* [ALTER ACCOUNT](../sql-reference/sql/alter-account.md)
* [CREATE DATABASE](../sql-reference/sql/create-database.md)
* [ALTER DATABASE](../sql-reference/sql/alter-database.md)
* [CREATE SCHEMA](../sql-reference/sql/create-schema.md)
* [ALTER SCHEMA](../sql-reference/sql/alter-schema.md)
* [CREATE ICEBERG TABLE (Snowflake as the Iceberg catalog)](../sql-reference/sql/create-iceberg-table-snowflake.md)
* [ALTER ICEBERG TABLE](../sql-reference/sql/alter-iceberg-table.md)

## Use default values with Iceberg tables

> **Note:**
>
> For the other Iceberg v3 features that are supported in this preview, see
> [Apache Iceberg™ tables: Support for Apache Iceberg™ v3 (Preview)](tables-iceberg-v3-specification-support.md).

This preview introduces support for the default values feature for Apache Iceberg™ tables in accordance with the Iceberg v3 specification.

> **Important:**
>
> To use default values with Iceberg tables, the tables must conform to v3 of the Apache Iceberg™ table specification.
> For instructions on how to configure the Iceberg version for tables, see [Configure the default Iceberg version](tables-iceberg-v3-specification-support.md).

This feature lets you to set default values for
existing and new records without having to rewrite existing data files. You can set the following default values for table columns:

* An initial default, which provides a default value for *existing* records when a field is added.
* A write default, which provides a default value for *new* records if the field with the default value isn’t specified during writes.

With this feature, you can evolve schemas while presenting values for historical data and provide a fallback value for future writes.
For more information, see [Default values](https://iceberg.apache.org/spec/#default-values).

You can specify a default value when you create or modify a table:

* To create a table with a default value for a column, use the DEFAULT keyword with your column definition. The value you specify
  is set as both the initial default and write default for the column. You can’t change the initial default for the column.
* To add a column with a default value to a table, use the DEFAULT keyword with the column definition in your ALTER ICEBERG TABLE command.
  The value you specify
  is set as both the initial default and write default for the column. You can’t change the initial default for the column.
* To change the write default for a column, use the WRITE DEFAULT keywords with the ALTER ICEBERG TABLE command.

> **Important:**
>
> When you specify a default value for a column, you must specify a static value; you can’t specify an expression or
> function for the value. This requirement is in accordance with the Iceberg v3 specification and applies to both the initial default
> and write default.

The following sections include examples of how to specify default values and change the default write value.

### Example: Create a table with a default value

To create an Iceberg table with default values, use the
[CREATE ICEBERG TABLE](../sql-reference/sql/create-iceberg-table.md) command.

In the following example, you first set a default value for a column when you create a Snowflake-managed Iceberg table. Next, you insert a
record into the table without specifying a value for the column with the default value.

1. Create a `user_events` table, which includes an `event_version` column with a default value of `2`:

   ```sqlexample
   CREATE ICEBERG TABLE user_events (
       event_id INT,
       user_id INT,
       event_type STRING,
       event_time TIMESTAMP,
       event_version INT DEFAULT 2
     )
     CATALOG = 'SNOWFLAKE'
     EXTERNAL_VOLUME = 'my_external_volume'
     BASE_LOCATION = 'database/schema/user_event'
     ICEBERG_VERSION = 3;
   ```

   Setting a default value in the table definition sets an initial default and a write default. Because the column has a write default,
   the value `2` will be used for new records if the `event_version` isn’t specified during writes.
2. Add a login event with `event_version` specified:

   ```sqlexample
   INSERT INTO user_events VALUES
     (1, 101, 'login', '2025-11-01 10:00:00', 1);
   ```

3. Add a purchase event, but don’t specify an `event_version`:

   ```sqlexample
   INSERT INTO user_events VALUES
   (1, 101, 'purchase', '2025-11-01 10:01:00');
   ```

   As a result, Snowflake inputs the value for `event_version` into the table as `2`.
4. Query the table:

   ```sqlexample
   SELECT * FROM user_events;
   ```

   Output:

   ```output
   +-----------+----------+-------------+---------------------+----------------+
   | event_id  | user_id  | event_type  | event_time          | event_version  |
   +-----------+----------+-------------+---------------------+----------------+
   | 1         | 101      | login       | 2025-11-01 10:00:00 | 1              |
   | 1         | 101      | purchase    | 2025-11-01 10:01:00 | 2              |
   +-----------+----------+-------------+---------------------+----------------+
   ```

### Example: Add a column with a default value to an existing table

To add a new column with a default value to an Iceberg table, use the [ALTER ICEBERG TABLE](../sql-reference/sql/alter-iceberg-table.md) command.

In the following example, you modify the `user_events` table by adding an `event_version` column, which has a default value of `2`:

```sqlexample
ALTER ICEBERG TABLE user_events ADD COLUMN event_version INT DEFAULT 2;
```

In addition to setting a write default, adding a column with a default value also sets an initial default for the column. As a
result, the default value for existing records for the `event_version` column is `2`.

### Example: Change the write default for a column

The following example changes the write default for the `event_version` column of the `user_events` table to `3`:

```sqlexample
ALTER ICEBERG TABLE user_events ALTER COLUMN event_version SET WRITE DEFAULT 3;
```

### View the default values defined for a table

To view the default value for a table column in a Snowflake-managed or externally managed Iceberg table,
run the [DESCRIBE ICEBERG TABLE](../sql-reference/sql/desc-iceberg-table.md) command, and then view the `DEFAULT` column and `WRITE DEFAULT` column in the output:

* The `DEFAULT` column maps to the `initial-default` value in the Apache Iceberg specification.
* The `WRITE DEFAULT` column maps to the `write-default` value in the Apache Iceberg specification.

These columns return in the output, regardless of whether the table is a v2 Iceberg table or a v3 Iceberg table.

The following example describes the columns for the `user_events` table. This table has an initial default and write default specified for
the `event_version` column:

```sqlexample
DESC ICEBERG TABLE user_events
  ->> SELECT
    "name",
    "kind",
    "default",
    "write default"
      FROM $1;
```

Output:

```output
+-----------------+---------+---------+---------------+
| name            | kind    | default | write default |
+-----------------+---------+-------------------------+
| EVENT_ID        | COLUMN  |         |               |
| USER_ID         | COLUMN  |         |               |
| EVENT_TYPE      | COLUMN  |         |               |
| EVENT_TIME      | COLUMN  |         |               |
| EVENT_VERSION   | COLUMN  | 2       | 3             |
+-----------------+---------+---------+---------------+
```

### Drop the write default

To drop the write default for a column, use the `DROP WRITE DEFAULT` keywords with the ALTER ICEBERG TABLE command.

The following example drops the default write value for the `event_version` column:

```sqlexample
ALTER ICEBERG TABLE user_events ALTER COLUMN event_version DROP WRITE DEFAULT;
```

### Considerations and limitations for default values

Consider the following items when you use default values with Snowflake-managed and externally managed Iceberg tables:

#### Snowflake-managed and externally managed Iceberg tables

* You can’t later add or change an initial default for a column after you create it. Therefore, you need to drop the column and add the
  column by using ALTER TABLE … DROP COLUMN and ALTER TABLE … ADD COLUMN commands.
* The maximum size for a default value is 128|~|MB.
* Default values can’t use data types that can’t be represented as constants, so you can’t use the following data types with a default value:

  * map
  * list
  * struct
  * variant

#### Snowflake-managed Iceberg tables

* The `write-default` value is always initialized to the `initial-default` value. To see the default for both of these values, run the
  DESCRIBE ICEBERG TABLE command, and then view the `WRITE DEFAULT` and `DEFAULT` columns in the output.
* You can’t specify a default value that uses the TIMESTAMP_NTZ(9) or TIMESTAMP_LTZ(9) data type.
* You can only set a default value to an expression, such as `DEFAULT pi()`, when you *create* a table; you can’t set a default value to an
  expression when you *modify* a table by using the ALTER ICEBERG TABLE command.
* Sequences aren’t supported.

  For example, the following CREATE ICEBERG TABLE command fails because it includes `LOG_ID NUMBER(38,0) NOT NULL autoincrement order`:

  > ```sqlexample
  > CREATE OR REPLACE ICEBERG TABLE CDC_RUN_LOG (
  >     LOG_ID NUMBER(38,0) NOT NULL autoincrement order,
  >     ENTITY_NAME VARCHAR(100),
  >     LAST_RUN TIMESTAMP_NTZ(9),
  >     DAG_NAME VARCHAR(100)
  >     )
  >     CATALOG = 'SNOWFLAKE'
  >     EXTERNAL_VOLUME = 'my_external_volume'
  >     BASE_LOCATION = 'my_iceberg_table';
  >     COMMENT='CDC table to manage log of runs'
  >     ICEBERG_VERSION = 3;
  > ```

#### Externally managed Iceberg tables

* You can’t specify a default value that uses the TIMESTAMP_NTZ(9) or TIMESTAMP_LTZ(9) data type.

These considerations and limitations apply to default values, which are features of Iceberg v3. For a list of considerations and limitations that apply
to all Iceberg v3 tables, see [Considerations and limitations for Iceberg v3 features](tables-iceberg-v3-specification-support.md).

## Use row lineage with Iceberg tables

> **Note:**
>
> For the other Iceberg v3 features that are supported in this preview, see
> [Apache Iceberg™ tables: Support for Apache Iceberg™ v3 (Preview)](tables-iceberg-v3-specification-support.md).

This preview introduces support for the row lineage feature for Apache Iceberg™ tables. With this feature,
the following columns are automatically written by Snowflake to an Iceberg table:

* `_row_id`
* `_last_updated_sequence_number`

This feature lets
query engines to reliably match the same row across snapshots and detect row-level changes. For more information,
see [Row lineage](https://iceberg.apache.org/spec/#row-lineage).

This feature is supported with both Snowflake-managed
and externally managed Iceberg tables.

> **Important:**
>
> To use row lineage with Iceberg tables, the tables must conform to v3 of the Apache Iceberg™ table specification.
> For instructions on how to configure the Iceberg version for tables, see [Configure the default Iceberg version](tables-iceberg-v3-specification-support.md).

### Considerations and limitations for row lineage

Row lineage is supported in streams with the following considerations:

* Append-only streams and standard streams are supported on Snowflake-managed Iceberg v3 tables.
* Insert-only streams and standard streams are supported on externally managed Iceberg v3 tables.

  * To have standard streams produce the correct results, the external engine must write to Iceberg v3 tables with respect to the Iceberg v3
    specification. Specifically, newly inserted rows should have `_row_id=NULL`. Rows that are copied during copy-on-write should maintain the `_row_id`.
  * MAX_DATA_EXTENSION_TIME_IN_DAYS doesn’t work on externally managed Iceberg v3 tables.
* When DMLs are committed over multi-statement transactions, append-only streams on Iceberg v3 tables have different semantics compared to Iceberg v2 tables:

  * On Iceberg v2, for append-only streams, if a row is added and then deleted in a multi-statement transaction, this row is considered an
    insertion.
  * On Iceberg v3, for append-only streams, this row isn’t treated as an insertion.

These considerations and limitations apply to row lineage, which is a feature from Iceberg v3. For a list of considerations and limitations
that apply to all Iceberg v3 tables, see [Considerations and limitations for Iceberg v3 features](tables-iceberg-v3-specification-support.md).
