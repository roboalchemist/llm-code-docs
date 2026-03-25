# Source: https://docs.snowflake.com/en/sql-reference/sql/create-iceberg-table-snowflake.md

# CREATE ICEBERG TABLE (Snowflake as the Iceberg catalog)

Creates or replaces an [Apache Iceberg™ table](../../user-guide/tables-iceberg.md) that uses
[Snowflake as the Iceberg catalog](../../user-guide/tables-iceberg.md)
in the current/specified schema.

This command supports the following variants:

* CREATE ICEBERG TABLE … AS SELECT (creates a populated table; also referred to as CTAS)
* CREATE ICEBERG TABLE … LIKE (creates an empty copy of an existing table)

This topic refers to Iceberg tables as simply “tables” except where specifying *Iceberg tables* avoids confusion.

> **Note:**
>
> Before creating a table, you must create the [external volume](create-external-volume.md) where the Iceberg metadata
> and data files are stored.
> For instructions, see [Configure an external volume](../../user-guide/tables-iceberg-configure-external-volume.md).

See also:
:   [ALTER ICEBERG TABLE](alter-iceberg-table.md) , [DROP ICEBERG TABLE](drop-iceberg-table.md) , [SHOW ICEBERG TABLES](show-iceberg-tables.md) , [DESCRIBE ICEBERG TABLE](desc-iceberg-table.md) , [UNDROP ICEBERG TABLE](undrop-iceberg-table.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] ICEBERG TABLE [ IF NOT EXISTS ] <table_name> (
    -- Column definition
    <col_name> <col_type> [ DEFAULT <col_default> ]
      [ inlineConstraint ]
      [ NOT NULL ]
      [ [ WITH ] MASKING POLICY <policy_name> [ USING ( <col_name> , <cond_col1> , ... ) ] ]
      [ [ WITH ] PROJECTION POLICY <policy_name> ]
      [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
      [ COMMENT '<string_literal>' ]

    -- Additional column definitions
    [ , <col_name> <col_type> [ DEFAULT <col_default> ] [ ... ] ]

    -- Out-of-line constraints
    [ , outoflineConstraint [ ... ] ]
  )
  [ PARTITION BY ( partitionExpression [, partitionExpression , ...] ) ]
  [ PATH_LAYOUT = { FLAT | HIERARCHICAL } ]
  [ CLUSTER BY ( <expr> [ , <expr> , ... ] ) ]
  [ EXTERNAL_VOLUME = '<external_volume_name>' ]
  [ CATALOG = 'SNOWFLAKE' ]
  [ BASE_LOCATION = '<directory_for_table_files>' ]
  [ TARGET_FILE_SIZE = '{ AUTO | 16MB | 32MB | 64MB | 128MB }' ]
  [ CATALOG_SYNC = '<open_catalog_integration_name>']
  [ STORAGE_SERIALIZATION_POLICY = { COMPATIBLE | OPTIMIZED } ]
  [ DATA_RETENTION_TIME_IN_DAYS = <integer> ]
  [ MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer> ]
  [ CHANGE_TRACKING = { TRUE | FALSE } ]
  [ COPY GRANTS ]
  [ COMMENT = '<string_literal>' ]
  [ ICEBERG_VERSION = <integer> ]
  [ ENABLE_ICEBERG_MERGE_ON_READ = { TRUE | FALSE } ]
  [ [ WITH ] ROW ACCESS POLICY <policy_name> ON ( <col_name> [ , <col_name> ... ] ) ]
  [ [ WITH ] AGGREGATION POLICY <policy_name> ]
  [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
  [ WITH CONTACT ( <purpose> = <contact_name> [ , <purpose> = <contact_name> ... ] ) ]
  [ ENABLE_DATA_COMPACTION = { TRUE | FALSE } ]
```

Where:

> ```sqlsyntax
> inlineConstraint ::=
>   [ CONSTRAINT <constraint_name> ]
>   { UNIQUE
>     | PRIMARY KEY
>     | [ FOREIGN KEY ] REFERENCES <ref_table_name> [ ( <ref_col_name> ) ]
>   }
>   [ <constraint_properties> ]
> ```
>
> For additional inline constraint details, see [CREATE | ALTER TABLE … CONSTRAINT](create-table-constraint.md).
>
> ```sqlsyntax
> outoflineConstraint ::=
>   [ CONSTRAINT <constraint_name> ]
>   { UNIQUE [ ( <col_name> [ , <col_name> , ... ] ) ]
>     | PRIMARY KEY [ ( <col_name> [ , <col_name> , ... ] ) ]
>     | [ FOREIGN KEY ] [ ( <col_name> [ , <col_name> , ... ] ) ]
>       REFERENCES <ref_table_name> [ ( <ref_col_name> [ , <ref_col_name> , ... ] ) ]
>   }
>   [ <constraint_properties> ]
> ```
>
> > **Note:**
> >
> > * Snowflake represents columns defined as PRIMARY KEY as identifier fields in the Iceberg metadata. The IDs for these columns are populated
> >   in the metadata as [identifier field IDs](https://iceberg.apache.org/spec/#identifier-field-ids).
> > * Snowflake doesn’t enforce NOT NULL and UNIQUE constraints on PRIMARY KEY columns for Iceberg tables.
>
> For additional out-of-line constraint details, see [CREATE | ALTER TABLE … CONSTRAINT](create-table-constraint.md).
>
> ```sqlsyntax
> partitionExpression ::=
>   <col_name> -- identity transform
>   | BUCKET ( <num_buckets> , <col_name> )
>   | TRUNCATE ( <width> , <col_name> )
>   | YEAR ( <col_name> )
>   | MONTH ( <col_name> )
>   | DAY ( <col_name> )
>   | HOUR ( <col_name> )
> ```

## Variant syntax

### CREATE ICEBERG TABLE … AS SELECT (also referred to as CTAS)

Creates a new table populated with the data returned by a query. Place the AS SELECT clause at the end of the statement.

> ```sqlsyntax
> CREATE [ OR REPLACE ] ICEBERG TABLE <table_name> [ ( <col_name> [ <col_type> ] [ DEFAULT <col_default> ] , <col_name> [ <col_type> ] [ DEFAULT <col_default> ] , ... ) ]
>   [ CLUSTER BY ( <expr> [ , <expr> , ... ] ) ]
>   [ EXTERNAL_VOLUME = '<external_volume_name>' ]
>   [ CATALOG = 'SNOWFLAKE' ]
>   [ BASE_LOCATION = '<relative_path_from_external_volume>' ]
>   [ COPY GRANTS ]
>   [ ICEBERG_VERSION = <integer> ]
>   [ ENABLE_ICEBERG_MERGE_ON_READ = { TRUE | FALSE } ]
>   [ ... ]
>   AS SELECT <query>
> ```

A masking policy can be applied to a column in a CTAS statement. Specify the masking policy after the column data type. Similarly, a
row access policy can be applied to the table. For example:

> ```sqlsyntax
> CREATE ICEBERG TABLE <table_name> ( <col1> <data_type> [ DEFAULT <col_default> ] [ WITH ] MASKING POLICY <policy_name> [ , ... ] )
>   [ EXTERNAL_VOLUME = '<external_volume_name>' ]
>   [ CATALOG = 'SNOWFLAKE' ]
>   [ BASE_LOCATION = '<directory_for_table_files>' ]
>   [ ICEBERG_VERSION = <integer> ]
>   [ ENABLE_ICEBERG_MERGE_ON_READ = { TRUE | FALSE } ]
>   [ WITH ] ROW ACCESS POLICY <policy_name> ON ( <col1> [ , ... ] )
>   [ ... ]
>   AS SELECT <query>
> ```

> **Note:**
>
> In a CTAS, the COPY GRANTS parameter is valid only when combined with the OR REPLACE clause. COPY GRANTS copies
> privileges from the table being replaced with CREATE OR REPLACE (if it already exists), not from the source
> table(s) being queried in the SELECT statement. CTAS with COPY GRANTS lets you overwrite a table with a new
> set of data while keeping existing grants on that table.
>
> For more information about the COPY GRANTS parameter, see COPY GRANTS in this document.

For more information about this variant syntax, see the usage notes.

### CREATE ICEBERG TABLE … LIKE

Creates a new table with the same column definitions as an existing table, but without copying data from the existing table. Column
names, types, defaults, and constraints are copied to the new table:

> ```sqlsyntax
> CREATE [ OR REPLACE ] ICEBERG TABLE <table_name> LIKE <source_table>
>   [ CLUSTER BY ( <expr> [ , <expr> , ... ] ) ]
>   [ COPY GRANTS ]
>   [ ... ]
> ```

For more information about the COPY GRANTS parameter, see COPY GRANTS in this document.

> > **Note:**
> >
> > CREATE TABLE … LIKE isn’t supported for tables with an auto-increment sequence accessed through a data share.

For more information about this variant syntax, see the usage notes.

### CREATE ICEBERG TABLE … CLONE

Creates a new Iceberg table with the same column definitions and containing all the existing data from the source table, without actually
copying the data. You can also use this variant to clone a table at a specific time or point in the past (using
[Time Travel](../../user-guide/data-time-travel.md)):

> ```sqlsyntax
> CREATE [ OR REPLACE ] ICEBERG TABLE [ IF NOT EXISTS ] <name>
>   CLONE <source_iceberg_table>
>     [ { AT | BEFORE } ( { TIMESTAMP => <timestamp> | OFFSET => <time_difference> | STATEMENT => <id> } ) ]
>     [COPY GRANTS]
>     ...
> ```

> **Note:**
>
> If the statement replaces an existing Iceberg table of the same name, Snowflake copies the grants from the table
> being replaced. If there is no existing table of that name, Snowflake copies the grants from the source table
> being cloned.

For more information about the COPY GRANTS parameter, see COPY GRANTS in this document.

For more information about cloning, see [CREATE <object> … CLONE](create-clone.md) and [Cloning and Apache Iceberg™ tables](../../user-guide/object-clone.md).

## Required parameters

`table_name`
:   Specifies the identifier (name) for the table; must be unique for the schema in which the table is created.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`col_name`
:   Specifies the column identifier (name). All the requirements for table identifiers also apply to column identifiers.

    For more information, see [Identifier requirements](../identifiers-syntax.md) and [Reserved & limited keywords](../reserved-keywords.md).

    > **Note:**
    >
    > In addition to the standard reserved keywords, the following keywords cannot be used as column identifiers because they are
    > reserved for ANSI-standard context functions:
    >
    > * `CURRENT_DATE`
    > * `CURRENT_ROLE`
    > * `CURRENT_TIME`
    > * `CURRENT_TIMESTAMP`
    > * `CURRENT_USER`
    >
    > For the list of reserved keywords, see [Reserved & limited keywords](../reserved-keywords.md).

`col_type`
:   Specifies the data type for the column.

    For information about the data types that can be specified for table columns, see [Data types for Apache Iceberg™ tables](../../user-guide/tables-iceberg-data-types.md).

    > **Note:**
    >
    > You can’t use `float` or `double` as primary keys (in accordance with the
    > [Apache Iceberg spec](https://iceberg.apache.org/spec/#identifier-field-ids)).

## Optional parameters

`col_name col_type DEFAULT col_default`
:   [Preview feature](../../release-notes/preview-features.md) — Open

    Available to all accounts.

    For a table that conforms to Iceberg v3, specifies both the initial default and write default for the specified column. If the data type for the
    column is string, you must surround the default value with single quotes.

    > **Important:**
    >
    > When you specify a default value for a column, you must specify a static value; you can’t specify an expression or
    > function for the value. This requirement is in accordance with the Iceberg v3 specification and applies to both the initial default
    > and write default.

    Default values is an Iceberg v3 feature, so you can’t specify a default value for a table that conforms to Iceberg v2. For more
    information about using default values with Iceberg tables, see [Use default values with Iceberg tables](../../user-guide/tables-iceberg-manage.md).

    > **Note:**
    >
    > To change the write default for the column after you create the table, run [ALTER ICEBERG TABLE … ALTER COLUMN … SET WRITE DEFAULT](alter-iceberg-table.md).

`BASE_LOCATION = 'directory_for_table_files'`
:   The path to a directory, which Snowflake uses to construct write paths for the table’s data and metadata files.
    Specify a relative path from the table’s `EXTERNAL_VOLUME` location.

    If not specified, Snowflake constructs a write path
    using attributes such as the value of the [BASE_LOCATION_PREFIX](../parameters.md) parameter and
    the table name.

    For more information, see [Data and metadata directories](../../user-guide/tables-iceberg-storage.md).

    This directory can’t be changed after you create a table.

`TARGET_FILE_SIZE = '{ AUTO | 16MB | 32MB | 64MB | 128MB }'`
:   Specifies a target Parquet file size for the table.

    * `'{ 16MB | 32MB | 64MB | 128MB }'` specifies a fixed target file size for the table.
    * `'AUTO'` works differently, depending on the table type:

      + Snowflake-managed tables: AUTO specifies that Snowflake should choose the file size for the table based on table characteristics
        such as size, DML patterns, ingestion workload, and clustering configuration. Snowflake automatically
        adjusts the file size, starting at 16 MB, for better read and write performance in Snowflake. Use this option to optimize table performance
        in Snowflake.
      + Externally managed tables: AUTO specifies that Snowflake should aggressively scale to the largest file size (128 MB).

    For more information, see [Set a target file size](../../user-guide/tables-iceberg-manage.md).

    Default: AUTO

`CONSTRAINT ...`
:   Defines an inline or out-of-line constraint for the specified column(s) in the table.

    For syntax information, see [CREATE | ALTER TABLE … CONSTRAINT](create-table-constraint.md). For more information about constraints, see [Constraints](../constraints.md).

`MASKING POLICY = policy_name`
:   Specifies the [masking policy](../../user-guide/security-column-intro.md) to set on a column.

`PROJECTION POLICY policy_name`
:   Specifies the [projection policy](../../user-guide/projection-policies.md) to set on a column.

`COMMENT 'string_literal'`
:   Specifies a comment for the column.

    (Note that comments can be specified at the column level or the table level. The syntax for each is slightly different.)

`USING ( col_name , cond_col_1 ... )`
:   Specifies the arguments to pass into the SQL expression for the conditional masking policy.

    The first column in the list specifies the column for the policy conditions to mask or tokenize the data and must match the
    column to which the masking policy is set.

    The additional columns specify the columns to evaluate to determine whether to mask or tokenize the data in each row of the query result
    when a query selects from the first column.

    If the USING clause is omitted, Snowflake treats the conditional masking policy as a normal
    [masking policy](../../user-guide/security-column-intro.md).

`PARTITION BY = ( partitionExpression [ , partitionExpression , ... ] )`
:   Specifies one or more partition expressions.

`PATH_LAYOUT = { FLAT | HIERARCHICAL }`
:   [Preview Feature](../../release-notes/preview-features.md) — Open

    Available to all accounts.

    Specifies the path layout that Snowflake uses when writing Parquet data files to the table:

    * `FLAT`: Snowflake writes all Parquet data files under the `data/` directory for the table.
    * `HIERARCHICAL`: Snowflake writes partitioned data under the `data/` directory for the table by using a hierarchical
      path layout. With this layout, each partition column is represented
      as a directory level in the path. To define these partition
      columns, use the PARTITION BY parameter. This layout is also called “Hive-style” partitioning.

      If you specify PATH_LAYOUT = HIERARCHICAL without a PARTITION BY clause,
      Snowflake stores the Parquet data files by using a flat layout path. You can’t
      modify the path layout for an existing table, so you might set this
      parameter to HIERARCHICAL without specifying a PARTITION BY clause if you don’t want to use partitioning with
      hierarchical paths now but you might in the future.

    > **Note:**
    >
    > For externally managed tables that you create in a standard Snowflake database, Snowflake infers and honors the partitioning scheme
    > that is specified by the remote catalog.

    Default: `FLAT`

`CLUSTER BY ( expr [ , expr , ... ] )`
:   Specifies one or more columns or column expressions in the table as the clustering key. For more information, see
    [Clustering Keys & Clustered Tables](../../user-guide/tables-clustering-keys.md).

    When using variant syntax (LIKE, AS SELECT), see the variant syntax usage notes.

    Default: No value (no clustering key is defined for the table)

    > **Important:**
    >
    > Clustering keys are not intended or recommended for all tables; they typically benefit very large (that is, multi-terabyte)
    > tables.
    >
    > Before you specify a clustering key for a table, you should understand micro-partitions.
    > For more information, see [Understanding Snowflake Table Structures](../../user-guide/tables-micro-partitions.md).

`EXTERNAL_VOLUME = 'external_volume_name'`
:   Specifies the identifier (name) for the external volume where the Iceberg table stores its metadata files and data in Parquet
    format. Iceberg metadata and manifest files store the table schema, partitions, snapshots, and other metadata.

    If you don’t specify this parameter, the Iceberg table defaults to the external volume for the schema, database, or account.
    The schema takes precedence over the database, and the database takes precedence over the account.

`CATALOG = 'SNOWFLAKE'`
:   Specifies Snowflake as the Iceberg catalog. Snowflake handles all life-cycle maintenance, such as compaction, for the table.

`CATALOG_SYNC = 'open_catalog_integration_name'`
:   Optionally specifies the name of a catalog integration configured for [Snowflake Open Catalog](https://other-docs.snowflake.com/en/opencatalog/overview). If specified, Snowflake syncs
    the table with an external catalog in your Snowflake Open Catalog account. For more information about syncing Snowflake-managed Iceberg tables with Open Catalog, see [Sync a Snowflake-managed table with Snowflake Open Catalog](../../user-guide/tables-iceberg-open-catalog-sync.md).

    For more information about this parameter, see [CATALOG_SYNC](../parameters.md).

`ICEBERG_VERSION = integer`
:   [Preview feature](../../release-notes/preview-features.md) — Open

    Available to all accounts.

    Specifies the version of the Apache Iceberg™ specification that the table conforms to.

    > **Caution:**
    >
    > Before you use other engines to upgrade an Iceberg tables format-version in table properties to v3, ensure that the table isn’t used by
    > engines or applications that don’t yet support v3. Downgrading format versions isn’t supported in the Apache Iceberg specification. Therefore, all
    > readers and writers must support v3. The default version for Iceberg tables in Snowflake is v2, which can be configured to v3 if
    > needed. Using Snowflake to perform in-place version upgrades isn’t supported at this time.

    If you don’t set this parameter, the Iceberg table defaults to the Iceberg version for the schema, database, or account. The schema
    takes precedence over the database, and the database takes precedence over the account.

    > * `2`: The table conforms with Iceberg version 2.
    > * `3`: The table conforms with Iceberg version 3.
    >
    > Default: `2`
    >
    > For more information about this parameter, see [ICEBERG_VERSION](../parameters.md).

`ENABLE_ICEBERG_MERGE_ON_READ = { TRUE | FALSE }`
:   [Preview feature](../../release-notes/preview-features.md) — Open

    Available to all accounts.

    Specifies whether the table uses merge-on-read behavior.

    If you don’t set this parameter, the Iceberg table defaults to the merge-on-read behavior that is specified for the schema, database,
    or account. The schema takes precedence over the database, and the database takes precedence over the account.

    Values:

    `TRUE`: The table uses merge-on-read behavior. Depending on whether the table conforms to v2 or v3 of the
    Apache Iceberg™ table specification, the behavior is as described in the following list:

    * If the table conforms with v2, use positional delete files.
    * If the table conforms with v3, use deletion vectors.

    `FALSE`: The table uses copy-on-write behavior.

    Default: `TRUE`

    For a detailed description of this parameter, see [ENABLE_ICEBERG_MERGE_ON_READ](../parameters.md).

`STORAGE_SERIALIZATION_POLICY = { COMPATIBLE | OPTIMIZED }`
:   Specifies the storage serialization policy for the table.
    If not specified at table creation, the table inherits the value set at the schema, database, or account level. If the value isn’t
    specified at any level, the table uses the default value.

    You can’t change the value of this parameter after table creation.

    * `COMPATIBLE`: Snowflake performs encoding and compression that ensures interoperability with third-party compute engines.
    * `OPTIMIZED`: Snowflake performs encoding and compression that ensures the best table performance within Snowflake.

    Default: `OPTIMIZED`

`DATA_RETENTION_TIME_IN_DAYS = integer`
:   Specifies the retention period for a Snowflake-managed table so that Time Travel actions (SELECT, CLONE, UNDROP) can be performed on historical
    data in the table. For more information, see [Understanding & using Time Travel](../../user-guide/data-time-travel.md).

    For a detailed description of this object-level parameter, as well as more information about object parameters, see
    [Parameters](../parameters.md).

    Values:

    > * Standard Edition: `0` or `1`
    > * Enterprise Edition: `0` to `90` for permanent tables

    Default:

    > * Standard Edition: `1`
    > * Enterprise Edition (or higher): `1` (unless a different default value was specified at the schema, database, or account level)

    > **Note:**
    >
    > A value of `0` effectively disables Time Travel for the table.

`MAX_DATA_EXTENSION_TIME_IN_DAYS = integer`
:   Object parameter that specifies the maximum number of days for which Snowflake can extend the data retention period for the table to
    prevent streams on the table from becoming stale.

    For a detailed description of this parameter, see [MAX_DATA_EXTENSION_TIME_IN_DAYS](../parameters.md).

`CHANGE_TRACKING = { TRUE | FALSE }`
:   Specifies whether to enable change tracking on the table.

    * `TRUE` enables change tracking on the table. This setting adds a pair of hidden columns to the source table and begins
      storing change tracking metadata in the columns. These columns consume a small amount of storage.

      The change tracking metadata can be queried using the [CHANGES](../constructs/changes.md) clause for
      [SELECT](select.md) statements, or by creating and querying one or more streams on the table.
    * `FALSE` does not enable change tracking on the table.

    Default: FALSE

`COPY GRANTS`
:   Specifies to retain the access privileges from the original table when a new table is created using any of the following
    CREATE TABLE variants:

    > * CREATE OR REPLACE TABLE
    > * CREATE TABLE … LIKE
    > * CREATE TABLE … CLONE

    The parameter copies all privileges, except OWNERSHIP, from the existing table to the new table. The new table does not
    inherit any future grants defined for the object type in the schema. By default, the role that executes the CREATE TABLE statement
    owns the new table.

    If the parameter is not included in the CREATE ICEBERG TABLE statement, then the new table does not inherit any explicit access
    privileges granted on the original table, but does inherit any future grants defined for the object type in the schema.

    Note:

    > * With [data sharing](../../guides-overview-sharing.md):
    >
    >   > + If the existing table was shared to another account, the replacement table is also shared.
    >   > + If the existing table was shared with your account as a data consumer, and access was further granted to other roles in
    >   >   the account (using `GRANT IMPORTED PRIVILEGES` on the parent database), access is also granted to the replacement
    >   >   table.
    > * The [SHOW GRANTS](show-grants.md) output for the replacement table lists the grantee for the copied privileges as the
    >   role that executed the CREATE ICEBERG TABLE statement, with the current timestamp when the statement was executed.
    > * The operation to copy grants occurs atomically in the CREATE ICEBERG TABLE command (that is, within the same transaction).

`COMMENT = 'string_literal'`
:   Specifies a comment. You can specify a comment at the column level or the table level.
    The syntax for each is slightly different.

    Default: No value

`WITH CONTACT ( purpose = contact [ , purpose = contact ...] )`
:   Associate the new object with one or more [contacts](../../user-guide/contacts-using.md).

    Specify the WITH CONTACT clause after all other clauses except the AS clause (if that clause is supported by this command).

`ROW ACCESS POLICY policy_name ON ( col_name [ , col_name ... ] )`
:   Specifies the [row access policy](../../user-guide/security-row-intro.md) to set on a table.

`AGGREGATION POLICY policy_name`
:   Specifies the [aggregation policy](../../user-guide/aggregation-policies.md) to set on a table.

`TAG ( tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ] )`
:   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

    The tag value is always a string, and the maximum number of characters for the tag value is 256.

    For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

`ENABLE_DATA_COMPACTION = { TRUE | FALSE }`
:   Specifies whether Snowflake should enable data compaction on the table.

    * `TRUE`: Snowflake performs data compaction on the table.
    * `FALSE`: Snowflake doesn’t perform data compaction on the table.

    Default: `TRUE`

    For more information, see [ENABLE_DATA_COMPACTION](../parameters.md) and [Set data compaction](../../user-guide/tables-iceberg-manage.md).

`ICEBERG_VERSION = integer`
:   [Preview feature](../../release-notes/preview-features.md) — Open

    Available to all accounts.

    Specifies the version of the Apache Iceberg™ specification that the table conforms to.

    > **Caution:**
    >
    > Before you use other engines to upgrade an Iceberg tables format-version in table properties to v3, ensure that the table isn’t used by
    > engines or applications that don’t yet support v3. Downgrading format versions isn’t supported in the Apache Iceberg specification. Therefore, all
    > readers and writers must support v3. The default version for Iceberg tables in Snowflake is v2, which can be configured to v3 if
    > needed. Using Snowflake to perform in-place version upgrades isn’t supported at this time.

    If you don’t set this parameter, the Iceberg table defaults to the Iceberg version for the schema, database, or account. The schema
    takes precedence over the database, and the database takes precedence over the account.

    > * `2`: The table conforms with Iceberg version 2.
    > * `3`: The table conforms with Iceberg version 3.
    >
    > Default: `2`
    >
    > For more information about this parameter, see [ICEBERG_VERSION](../parameters.md).

`ENABLE_ICEBERG_MERGE_ON_READ = { TRUE | FALSE }`
:   [Preview feature](../../release-notes/preview-features.md) — Open

    Available to all accounts.

    Specifies whether to enable merge-on-read behavior for Apache Iceberg™ tables.

    Values:
    :   `TRUE`: New tables use merge-on-read behavior.

        `FALSE`: New tables use copy-on-write behavior.

    Default:
    :   `TRUE`

    For a detailed description of this parameter, see [ENABLE_ICEBERG_MERGE_ON_READ](../parameters.md). For more information about merge-on-read
    and copy-on-write behavior in Snowflake, see [Use row-level deletes](../../user-guide/tables-iceberg-manage.md).

## Partition expression parameters (`partitionExpression`)

Snowflake supports all partition transforms in version 2 of the Apache Iceberg specification. For more information, see
[Partition Transforms](https://iceberg.apache.org/spec/#partition-transforms) in the Apache Iceberg specification.

For more information about partitioning Iceberg tables, see [Iceberg partitioning](../../user-guide/tables-iceberg-metadata.md).

`col_name`
:   Specifies the identifier (name) for the source column to partition.

    When used alone, without a transform such as YEAR, specifies an identity transform on the source column.
    For more information, see [identity](https://iceberg.apache.org/spec/#partition-transforms).

`BUCKET`
:   Specifies a bucket transform. For more information, see [Bucket Transform Details](https://iceberg.apache.org/spec/#bucket-transform-details).

    `num_buckets` is the number of buckets to group the data into.

`TRUNCATE`
:   Specifies a truncate transform, which partitions the data based on the truncated values of the specified source column.
    For more information, see [Truncate Transform Details](https://iceberg.apache.org/spec/#truncate-transform-details).

`YEAR`
:   Specifies a year transform, which extracts the year from a date or timestamp source-column value.
    For more information, see [Partition Transforms](https://iceberg.apache.org/spec/#partition-transforms).

`MONTH`
:   Specifies a month transform.
    For more information, see [Partition Transforms](https://iceberg.apache.org/spec/#partition-transforms).

`DAY`
:   Specifies a day transform, which extracts the day from a date or timestamp source-column value.
    For more information, see [Partition Transforms](https://iceberg.apache.org/spec/#partition-transforms).

`HOUR`
:   Specifies an hour transform, which extracts the hour from a timestamp source-column value.
    For more information, see [Partition Transforms](https://iceberg.apache.org/spec/#partition-transforms).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE ICEBERG TABLE | Schema |  |
| CREATE EXTERNAL VOLUME | Account | Required to create a new external volume. |
| USAGE | External Volume | Required to reference an existing external volume. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Considerations for running this command:

  * Cross-cloud and cross-region Iceberg tables are not currently supported when you use Snowflake as the Iceberg catalog.
    If CREATE ICEBERG TABLE returns an error message like `"External volume <volume_name> must have a STORAGE_LOCATION
    defined in the local region ..."`, make sure that your external volume uses an active storage location
    in the same region as your Snowflake account.
  * If you created your external volume using a double-quoted identifier,
    you must specify the identifier exactly as created (including the double quotes) in your CREATE ICEBERG TABLE statement.
    Failure to include the quotes might result in an `Object does not exist` error (or
    similar type of error).

    To view an example, see the Examples (in this topic) section.
  * To create an [Iceberg table](../../user-guide/tables-iceberg.md) with the USING TEMPLATE clause (and column definitions derived from
    INFER_SCHEMA output), you must specify `KIND => 'ICEBERG'` for the [INFER_SCHEMA](../functions/infer_schema.md) function.
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

* Using variant syntax:

  * CREATE ICEBERG TABLE … LIKE:

    > * If you don’t specify a clustering key, the table inherits the clustering key of the source table (if one exists).
    > * By default, [Automatic Clustering](../../user-guide/tables-auto-reclustering.md) is not suspended for the new table even if Automatic Clustering is
    >   suspended for the source table.
    > * For [partitioned Iceberg tables](../../user-guide/tables-iceberg-metadata.md), the partitioning of the source table is ignored. To override this behavior, specify the PARTITION BY clause with the command.
  * CREATE ICEBERG TABLE … AS SELECT (CTAS):

    When clustering keys are specified in a CTAS statement:

    * Column definitions are required and must be explicitly specified in the statement.
    * By default, [Automatic Clustering](../../user-guide/tables-auto-reclustering.md) is enabled for the new table even if Automatic Clustering is
      suspended for the source table.
    * The data is clustered when the new table is created. A clustered table generates a query plan
      that includes a sort operation and takes longer to create than an equivalent table that is not clustered.

      Alternatively, you can create a table with rows in sorted order by using an ORDER BY clause in the CTAS query.
  * CREATE ICEBERG TABLE … CLONE:

    * For [partitioned Iceberg tables](../../user-guide/tables-iceberg-metadata.md), the cloned table retains the partitioning information of
      the source table.
* Using default values:

  * You can’t use expressions or functions, such as CURRENT_TIMESTAMP(), for default values on v3 Iceberg tables. Only constant values are
    permitted in the Apache Iceberg v3 table specification.

    * For v2 Iceberg tables, you can use expressions such as CURRENT_TIMESTAMP() with Snowflake. However, this property isn’t persisted into
      Iceberg metadata because the default values specification was introduced in version 3. Columns in v2 Iceberg tables with default values as
      expressions are only used with Snowflake, but the table remains interoperable with other engines and compliant with the
      version 2 specification.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).
* If you’re creating a table that you will sync with Snowflake Open Catalog, keep the following in mind:

  > **Important:**
  >
  > To ensure that access privileges in Open Catalog are enforced correctly on the table, make sure the table meets certain conditions
  > before creating it. These conditions relate to the directory structure hierarchy for the catalog. For these conditions and instructions on
  > how to meet them, see the note in
  > [Organize catalog content](https://other-docs.snowflake.com/en/opencatalog/organize-catalog-content#conditions-correct-access-privileges)
  > in the Snowflake Open Catalog documentation.

To troubleshoot issues with creating a Snowflake-managed table, see [You can’t create a Snowflake-managed table](../../user-guide/tables-iceberg-open-catalog-troubleshooting.md).

## Examples

### Create an Iceberg table with Snowflake as the catalog

This example creates an Iceberg table with Snowflake as the Iceberg catalog.
The resulting table is managed by Snowflake and supports read and write access.

The example sets the table name (`my_iceberg_table`) as the `BASE_LOCATION`. This way,
Snowflake writes data and metadata to a directory that uses the name of the table in your external volume
location.

```sqlexample
CREATE ICEBERG TABLE my_iceberg_table (amount int)
  CATALOG = 'SNOWFLAKE'
  EXTERNAL_VOLUME = 'my_external_volume'
  BASE_LOCATION = 'my_iceberg_table';
```

### Create a partitioned Iceberg table

The following example creates a Snowflake-managed Iceberg table by using the value of a column named `c_nationkey` to partition the table:

```sqlexample
CREATE OR REPLACE ICEBERG TABLE customer_iceberg_partitioned (
  c_custkey INTEGER,
  c_name STRING,
  c_address STRING,
  c_nationkey INTEGER,
  c_phone STRING,
  c_acctbal INTEGER,
  c_mktsegment STRING,
  c_comment STRING
)
  PARTITION BY (c_nationkey)
  EXTERNAL_VOLUME = 'my_ext_vol'
  CATALOG = 'SNOWFLAKE'
  BASE_LOCATION = 'customer_iceberg_partitioned';
```

For more information, see [Iceberg partitioning](../../user-guide/tables-iceberg-metadata.md).

### Create a partitioned Iceberg table with hierarchical layout

The following example creates a Snowflake-managed Iceberg table by using the value of a column named `c_nationkey` to
partition the table. Because PATH_LAYOUT = HIERARCHICAL, Snowflake writes data to the partitioned Iceberg table by using a hierarchical
path layout for files where partitioning information is included in the file paths:

```sqlexample
CREATE OR REPLACE ICEBERG TABLE customer_iceberg_partitioned (
  c_custkey INTEGER,
  c_name STRING,
  c_address STRING,
  c_nationkey INTEGER,
  c_phone STRING,
  c_acctbal INTEGER,
  c_mktsegment STRING,
  c_comment STRING
)
  PARTITION BY (c_nationkey)
  PATH_LAYOUT = HIERARCHICAL
  EXTERNAL_VOLUME = 'my_ext_vol'
  CATALOG = 'SNOWFLAKE'
  BASE_LOCATION = 'customer_iceberg_partitioned';
```

For more information, see [Partitioning with hierarchical paths](../../user-guide/tables-iceberg-metadata.md).

### Create an Iceberg table by using the CTAS variant syntax

This example use the CREATE ICEBERG TABLE … AS SELECT variant syntax to create a *new* Iceberg table from a table named
`base_iceberg_table`. The AS SELECT clause must be at the end of the statement.

```sqlexample
CREATE OR REPLACE ICEBERG TABLE iceberg_table_copy (column1 int)
  EXTERNAL_VOLUME = 'my_external_volume'
  CATALOG = 'SNOWFLAKE'
  BASE_LOCATION = 'iceberg_table_copy'
  AS SELECT * FROM base_iceberg_table;
```

### Specify an external volume with a double-quoted identifier

This example creates an Iceberg table with an external volume whose identifier contains double quotes.
Identifiers enclosed in double quotes are case-sensitive and often contain special characters.

The identifier `"external_volume_1"` is specified exactly as created (including the double quotes).
Failure to include the quotes might result in an `Object does not exist` error (or similar type of error).

To learn more, see [Double-quoted identifiers](../identifiers-syntax.md).

```sqlexample
CREATE OR REPLACE ICEBERG TABLE table_with_quoted_external_volume
  EXTERNAL_VOLUME = '"external_volume_1"'
  CATALOG = 'SNOWFLAKE'
  BASE_LOCATION = 'my/relative/path/from/external_volume';
```

### Create a v3 Iceberg table

The following example creates a Snowflake-managed Apache Iceberg™ table that conforms to v3 of the Apache Iceberg™ specification:

```sqlexample
CREATE ICEBERG TABLE my_v3_iceberg_table (
  record VARIANT,
  event_timestamp TIMESTAMP_LTZ(6)
)
  CATALOG = 'SNOWFLAKE'
  EXTERNAL_VOLUME = 'my_external_volume'
  BASE_LOCATION = 'my_iceberg_table'
  ICEBERG_VERSION = 3;
```
