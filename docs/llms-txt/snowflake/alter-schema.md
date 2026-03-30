# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-schema.md

# ALTER SCHEMA

Modifies the properties for an existing schema, including renaming the schema or swapping it with another schema, and changing the Time Travel
data retention period (if you are using Snowflake Enterprise Edition or higher).

See also:
:   [CREATE SCHEMA](create-schema.md) , [DESCRIBE SCHEMA](desc-schema.md) , [DROP SCHEMA](drop-schema.md) , [SHOW SCHEMAS](show-schemas.md) , [UNDROP SCHEMA](undrop-schema.md)

## Syntax

```sqlsyntax
ALTER SCHEMA [ IF EXISTS ] <name> RENAME TO <new_schema_name>

ALTER SCHEMA [ IF EXISTS ] <name> SWAP WITH <target_schema_name>

ALTER SCHEMA [ IF EXISTS ] <name> SET {
                                      [ DATA_RETENTION_TIME_IN_DAYS = <integer> ]
                                      [ MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer> ]
                                      [ EXTERNAL_VOLUME = <external_volume_name> ]
                                      [ CATALOG = <catalog_integration_name> ]
                                      [ ICEBERG_VERSION_DEFAULT = <integer> ]
                                      [ ENABLE_ICEBERG_MERGE_ON_READ = { TRUE | FALSE } ]
                                      [ REPLACE_INVALID_CHARACTERS = { TRUE | FALSE } ]
                                      [ DEFAULT_DDL_COLLATION = '<collation_specification>' ]
                                      [ DEFAULT_NOTEBOOK_COMPUTE_POOL_CPU = '<compute_pool_name>' ]
                                      [ DEFAULT_NOTEBOOK_COMPUTE_POOL_GPU = '<compute_pool_name>' ]
                                      [ LOG_LEVEL = '<log_level>' ]
                                      [ TRACE_LEVEL = '<trace_level>' ]
                                      [ STORAGE_SERIALIZATION_POLICY = { COMPATIBLE | OPTIMIZED } ]
                                      [ CLASSIFICATION_PROFILE = '<profile_name>' ]
                                      [ COMMENT = '<string_literal>' ]
                                      [ CATALOG_SYNC = '<snowflake_open_catalog_integration_name>' ]
                                      [ REPLICABLE_WITH_FAILOVER_GROUPS = { 'YES' | 'NO' } ]
                                      [ BASE_LOCATION_PREFIX = '<string>']
                                      [ DEFAULT_STREAMLIT_NOTEBOOK_WAREHOUSE = '<warehouse_name>']
                                      [ CONTACT <purpose> = <contact_name> [ , <purpose> = <contact_name> ... ] ]
                                      [ OBJECT_VISIBILITY = PRIVILEGED } ]
                                      [ ENABLE_DATA_COMPACTION = { TRUE | FALSE } ]
                                      }

ALTER SCHEMA [ IF EXISTS ] <name> SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER SCHEMA [ IF EXISTS ] <name> UNSET TAG <tag_name> [ , <tag_name> ... ]

ALTER SCHEMA [ IF EXISTS ] <name> UNSET {
                                        DATA_RETENTION_TIME_IN_DAYS         |
                                        MAX_DATA_EXTENSION_TIME_IN_DAYS     |
                                        EXTERNAL_VOLUME                     |
                                        CATALOG                             |
                                        ICEBERG_VERSION_DEFAULT             |
                                        ENABLE_ICEBERG_MERGE_ON_READ        |
                                        REPLACE_INVALID_CHARACTERS          |
                                        DEFAULT_DDL_COLLATION               |
                                        LOG_LEVEL                           |
                                        TRACE_LEVEL                         |
                                        STORAGE_SERIALIZATION_POLICY        |
                                        COMMENT                             |
                                        CATALOG_SYNC                        |
                                        REPLICABLE_WITH_FAILOVER_GROUPS     |
                                        BASE_LOCATION_PREFIX                |
                                        DEFAULT_STREAMLIT_NOTEBOOK_WAREHOUSE|
                                        CONTACT <purpose>
                                        CLASSIFICATION_PROFILE
                                        OBJECT_VISIBILITY                   |
                                        CONTACT <purpose>                   |
                                        CLASSIFICATION_PROFILE              |
                                        ENABLE_DATA_COMPACTION
                                        }
                                        [ , ... ]

ALTER SCHEMA [ IF EXISTS ] <name> { ENABLE | DISABLE } MANAGED ACCESS
```

## Parameters

`name`
:   Specifies the identifier for the schema to alter. If the identifier contains spaces, special characters, or mixed-case characters, the entire
    string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

`RENAME TO new_schema_name`
:   Specifies the new identifier for the schema; must be unique for the database.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

    You can move the object to a different database while optionally renaming the schema. To do so, specify a qualified
    `new_schema_name` value that includes the new database name in the form `db_name.new_schema_name`.

    > **Note:**
    >
    > The destination database must already exist. In addition, a schema with the same name cannot already exist in the new location;
    > otherwise, the statement returns an error.

    When an object is renamed, other objects that reference it must be updated with the new name.

`SWAP WITH target_schema_name`
:   Swaps all objects (tables, views, etc.) and metadata, including identifiers, between the two specified schemas. Also swaps all access control
    privileges granted on the schemas and objects they contain. `SWAP WITH` essentially performs a rename of both schemas as a single operation.

`SET ...`
:   Specifies one (or more) properties to set for the schema (separated by blank spaces, commas, or new lines):

    `DATA_RETENTION_TIME_IN_DAYS = integer`
    :   Specifies the number of days for which Time Travel actions (CLONE and UNDROP) can be performed on the schema, as well as specifying the
        default Time Travel retention time for all tables created in the schema.

        The value you can specify depends on the Snowflake Edition you are using:

        * Standard Edition: `0` or `1`
        * Enterprise Edition (or higher): `0` to `90`

    `MAX_DATA_EXTENSION_TIME_IN_DAYS = integer`
    :   Object parameter that specifies the maximum number of days for which Snowflake can extend the data retention period for tables in the schema
        to prevent streams on the tables from becoming stale.

        For a detailed description of this parameter, see [MAX_DATA_EXTENSION_TIME_IN_DAYS](../parameters.md).

    `EXTERNAL_VOLUME = external_volume_name`
    :   Object parameter that specifies the default external volume to use for [Apache Iceberg™ tables](../../user-guide/tables-iceberg.md).

        For more information about this parameter, see [EXTERNAL_VOLUME](../parameters.md).

    `CATALOG = catalog_integration_name`
    :   Object parameter that specifies the default catalog integration to use for [Apache Iceberg™ tables](../../user-guide/tables-iceberg.md).

        For more information about this parameter, see [CATALOG](../parameters.md).

    `ICEBERG_VERSION_DEFAULT = integer`
    :   [Preview feature](../../release-notes/preview-features.md) — Open

        Available to all accounts.

        Specifies the version of the Apache Iceberg™ table specification that Iceberg tables conform to.

        Values:
        :   `2`: New tables conform with Iceberg version 2.

            `3`: New tables conform with Iceberg version 3.

        > **Caution:**
        >
        > Before you use other engines to upgrade an Iceberg tables format-version in table properties to v3, ensure that the table isn’t used by
        > engines or applications that don’t yet support v3. Downgrading format versions isn’t supported in the Apache Iceberg specification. Therefore, all
        > readers and writers must support v3. The default version for Iceberg tables in Snowflake is v2, which can be configured to v3 if
        > needed. Using Snowflake to perform in-place version upgrades isn’t supported at this time.

        Default:
        :   `2`

        For more information about this parameter, see [ICEBERG_VERSION_DEFAULT](../parameters.md).

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

    `REPLACE_INVALID_CHARACTERS = { TRUE | FALSE }`
    :   Specifies whether to replace invalid UTF-8 characters with the Unicode replacement character (�) in query results for an
        [Iceberg table](create-iceberg-table.md).
        You can only set this parameter for tables that use an external Iceberg catalog.

        * `TRUE` replaces invalid UTF-8 characters with the Unicode replacement character.
        * `FALSE` leaves invalid UTF-8 characters unchanged. Snowflake returns a user error message when it encounters invalid UTF-8
          characters in a Parquet data file.

        Default: `FALSE`

    `DEFAULT_DDL_COLLATION = 'collation_specification'`
    :   Specifies a default [collation specification](../collation.md) for:

        * Any new columns added to existing tables in the schema.
        * All columns in new tables added to the schema.

        Setting the parameter does not change the collation specification for any existing columns.

        For more details about the parameter, see [DEFAULT_DDL_COLLATION](../parameters.md).

    `DEFAULT_NOTEBOOK_COMPUTE_POOL_CPU = compute_pool_name`
    :   CPU compute pool name that overrides the default CPU compute pool Snowflake provisioned in your account for running Notebooks. For more information, see [System compute pools](../../developer-guide/snowpark-container-services/working-with-compute-pool.md).

    `DEFAULT_NOTEBOOK_COMPUTE_POOL_GPU = compute_pool_name`
    :   GPU compute pool name that overrides the default GPU compute pool Snowflake provisioned in your account for running Notebooks. For more information, see [System compute pools](../../developer-guide/snowpark-container-services/working-with-compute-pool.md).

    `LOG_LEVEL = 'log_level'`
    :   Specifies the severity level of messages that should be ingested and made available in the active event table. Messages at
        the specified level (and at more severe levels) are ingested.

        For more information about levels, see [LOG_LEVEL](../parameters.md). For information about setting log level, see
        [Setting levels for logging, metrics, and tracing](../../developer-guide/logging-tracing/telemetry-levels.md).

    `TRACE_LEVEL = 'trace_level'`
    :   Controls how trace events are ingested into the event table.

        For information about levels, see [TRACE_LEVEL](../parameters.md). For information about setting trace level, see
        [Setting levels for logging, metrics, and tracing](../../developer-guide/logging-tracing/telemetry-levels.md).

    `STORAGE_SERIALIZATION_POLICY = { COMPATIBLE | OPTIMIZED }`
    :   Specifies the storage serialization policy for [Apache Iceberg™ tables](../../user-guide/tables-iceberg.md) that use Snowflake as the catalog.

        * `COMPATIBLE`: Snowflake performs encoding and compression of data files that ensures interoperability with third-party compute engines.
        * `OPTIMIZED`: Snowflake performs encoding and compression of data files that ensures the best table performance within Snowflake.

        Default: `OPTIMIZED`

    `TAG tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ]`
    :   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

        The tag value is always a string, and the maximum number of characters for the tag value is 256.

        For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

    `CONTACT purpose = contact [ , purpose = contact ... ]`
    :   Associate the existing object with one or more [contacts](../../user-guide/contacts-using.md).

        You cannot set the CONTACT property with other properties in the same statement.

    `CLASSIFICATION_PROFILE = 'profile_name'`
    :   Associates the schema with a classification profile so that sensitive data in the schema is
        [automatically classified](../../user-guide/classify-auto.md).

    `COMMENT = 'string_literal'`
    :   Adds a comment or overwrites an existing comment for the schema.

    `CATALOG_SYNC = 'snowflake_open_catalog_integration_name'`
    :   Specifies the name of a catalog integration configured for [Snowflake Open Catalog](https://other-docs.snowflake.com/en/opencatalog/overview).
        If specified, Snowflake syncs Snowflake-managed Apache Iceberg™ tables in the schema with an external catalog in your Snowflake Open Catalog account.
        For more information about syncing Snowflake-managed Iceberg tables with Open Catalog, see [Sync a Snowflake-managed table with Snowflake Open Catalog](../../user-guide/tables-iceberg-open-catalog-sync.md).

        For more information about this parameter, see [CATALOG_SYNC](../parameters.md).

        Default: No value

    `REPLICABLE_WITH_FAILOVER_GROUPS = { 'YES' | 'NO' }`
    :   Specifies if this schema is eligible for replication.
        You can set this property to `NO` to prevent individual schemas
        within a database from being replicated.

        For more information about this parameter, see [Schema-level replication for failover groups](../../user-guide/account-replication-config.md).

        Default: `'YES'`

    `DEFAULT_STREAMLIT_NOTEBOOK_WAREHOUSE = 'warehouse_name'`
    :   Specifies the default warehouse to use when you create a notebook using SQL.

    `BASE_LOCATION_PREFIX = 'string'`
    :   Specifies a prefix for Snowflake to use in the write path for Snowflake-managed Apache Iceberg™ tables.
        For more information,
        see [data and metadata directories for Iceberg tables](../../user-guide/tables-iceberg-storage.md) and
        [BASE_LOCATION_PREFIX](../parameters.md) in the Snowflake Parameters topic.

        Default: No value

`OBJECT_VISIBILITY = PRIVILEGED`
:   [Preview Feature](../../release-notes/preview-features.md) — Open

    Available to all accounts.

    Specifies that only roles within the current account that are granted an explicit privilege on the object can see the object. This is the default behavior in Snowflake.

    For examples, see [Make database objects discoverable in Universal Search](../../user-guide/ui-snowsight/object-visibility-universal-search.md).

`ENABLE_DATA_COMPACTION = { TRUE | FALSE }`
:   Specifies whether Snowflake should enable data compaction on Snowflake-managed [Apache Iceberg™ tables](../../user-guide/tables-iceberg.md).

    * `TRUE`: Snowflake performs data compaction on the tables.
    * `FALSE`: Snowflake doesn’t perform data compaction on the tables.

    Default: `TRUE`

    For more information, see [ENABLE_DATA_COMPACTION](../parameters.md) and [Set data compaction](../../user-guide/tables-iceberg-manage.md).

`UNSET ...`
:   Specifies one (or more) properties and/or parameters to unset for the database, which resets them to the defaults:

    * `DATA_RETENTION_TIME_IN_DAYS`
    * `MAX_DATA_EXTENSION_TIME_IN_DAYS`
    * `EXTERNAL_VOLUME`
    * `CATALOG`
    * `ICEBERG_VERSION_DEFAULT`
    * `ENABLE_ICEBERG_MERGE_ON_READ`
    * `REPLACE_INVALID_CHARACTERS`
    * `DEFAULT_DDL_COLLATION`
    * `TAG tag_name [ , tag_name ... ]`
    * `LOG_LEVEL`
    * `TRACE_LEVEL`
    * `STORAGE_SERIALIZATION_POLICY`
    * `COMMENT`
    * `CATALOG_SYNC`
    * `REPLICABLE_WITH_FAILOVER_GROUPS`
    * `BASE_LOCATION_PREFIX`
    * `DEFAULT_STREAMLIT_NOTEBOOK_WAREHOUSE`
    * `CONTACT purpose`
    * `CLASSIFICATION_PROFILE`
    * `OBJECT_VISIBILITY`
    * `ENABLE_DATA_COMPACTION`

    You can reset multiple properties/parameters with a single ALTER statement; however, each property/parameter must be separated by a
    comma. When resetting a property/parameter, specify only the name; specifying a value for the property will return an error.

`{ ENABLE | DISABLE } MANAGED ACCESS`
:   Enable managed access for a schema, or disable to convert a managed access schema to a regular schema. Managed access schemas centralize
    privilege management with the schema owner.

    In regular schemas, the owner of an object (i.e. the role that has the OWNERSHIP privilege on the object) can grant further privileges on
    their objects to other roles. In managed access schemas, the schema owner manages all privilege grants, including
    [future grants](../../user-guide/security-access-control-configure.md), on objects in the schema. Object owners retain the OWNERSHIP privileges
    on the objects; however, only the schema owner can manage privilege grants on the objects.

## Usage notes

* To rename a schema, the role used to perform the operation must have the CREATE SCHEMA privilege on the database for the schema and OWNERSHIP
  privileges on the schema.
* To swap two schemas, the role used to perform the operation must have OWNERSHIP privileges on both schemas.
* To convert a regular schema to a managed access schema:

  * The schema owner (i.e. the role that has the OWNERSHIP privileges on the schema) must also have the global MANAGE GRANTS privilege. The
    MANAGE GRANTS privilege is required because another role with this privilege could have defined future grants on objects of a specified
    type in the schema. After a regular schema becomes a managed access schema, the schema owner could revoke the future grants without
    understanding why a role with the MANAGE GRANTS privilege granted them.
  * All open future grants must be revoked using [REVOKE <privileges> … FROM ROLE](revoke-privilege.md) with the FUTURE keyword.

  After a regular schema is converted to a managed access schema, all privileges previously granted on individual objects are retained; however,
  the object owners cannot grant further privileges on those objects.
* To convert a managed access schema to a regular schema, the schema owner must also have the global MANAGE GRANTS privilege only if the
  current schema has future privilege grants defined.
* For schemas in a [catalog-linked database](../../user-guide/tables-iceberg-catalog-linked-database.md), this command only supports
  the following parameters:

  * SET/UNSET with the following options:

    * CLASSIFICATION_PROFILE
    * COMMENT
    * CONTACT
    * STORAGE_SERIALIZATION_POLICY
    * TAG
  * ENABLE MANAGED ACCESS and DISABLE MANAGED ACCESS.
* To specify the default version of the Apache Iceberg™ specification that Iceberg tables conform to, the role used to perform the operation
  must have the OWNERSHIP privilege on the schema.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

Rename schema `schema1` to `schema2`:

> ```sqlexample
> ALTER SCHEMA IF EXISTS schema1 RENAME TO schema2;
> ```

Convert a regular schema to a managed access schema:

> ```sqlexample
> ALTER SCHEMA schema2 ENABLE MANAGED ACCESS;
> ```
