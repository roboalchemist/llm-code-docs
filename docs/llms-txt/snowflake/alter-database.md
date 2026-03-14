# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-database.md

# ALTER DATABASE

Modifies the properties for an existing database.

Database modifications include the following:

* Changing the name of the database or changing the Time Travel data retention period (if you are using Snowflake Enterprise Edition or higher).
* Enabling and managing database replication and failover.

See also:
:   [CREATE DATABASE](create-database.md) , [DESCRIBE DATABASE](desc-database.md) , [DROP DATABASE](drop-database.md) , [SHOW DATABASES](show-databases.md) , [UNDROP DATABASE](undrop-database.md)

## Syntax

```sqlsyntax
ALTER DATABASE [ IF EXISTS ] <name> RENAME TO <new_db_name>

ALTER DATABASE [ IF EXISTS ] <name> SWAP WITH <target_db_name>

ALTER DATABASE [ IF EXISTS ] <name> SET [ DATA_RETENTION_TIME_IN_DAYS = <integer> ]
                                        [ MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer> ]
                                        [ EXTERNAL_VOLUME = <external_volume_name> ]
                                        [ CATALOG = <catalog_integration_name> ]
                                        [ ICEBERG_VERSION_DEFAULT = <integer> ]
                                        [ ENABLE_ICEBERG_MERGE_ON_READ = { TRUE | FALSE } ]
                                        [ REPLACE_INVALID_CHARACTERS = { TRUE | FALSE } ]
                                        [ DEFAULT_DDL_COLLATION = '<collation_specification>' ]
                                        [ DEFAULT_NOTEBOOK_COMPUTE_POOL_CPU = '<compute_pool_name>' ]
                                        [ DEFAULT_NOTEBOOK_COMPUTE_POOL_GPU = '<compute_pool_name>' ]
                                        [ OBJECT_VISIBILITY = { <object_visibility_spec> | PRIVILEGED } ]
                                        [ LOG_LEVEL = '<log_level>' ]
                                        [ METRIC_LEVEL = '<metric_level>' ]
                                        [ TRACE_LEVEL = '<trace_level>' ]
                                        [ STORAGE_SERIALIZATION_POLICY = { COMPATIBLE | OPTIMIZED } ]
                                        [ EVENT_TABLE = <event_table_name> ]
                                        [ COMMENT = '<string_literal>' ]
                                        [ CATALOG_SYNC = '<snowflake_open_catalog_integration_name>' ]
                                        [ REPLICABLE_WITH_FAILOVER_GROUPS = { 'YES' | 'NO' } ]
                                        [ BASE_LOCATION_PREFIX = '<string>' ]
                                        [ DEFAULT_STREAMLIT_NOTEBOOK_WAREHOUSE = <warehouse_name> ]
                                        [ CLASSIFICATION_PROFILE = '<profile_name>' ]
                                        [ CONTACT <purpose> = <contact_name> [ , <purpose> = <contact_name> ... ] ]
                                        [ ENABLE_DATA_COMPACTION = { TRUE | FALSE } ]
                                        [ DATA_QUALITY_MONITORING_SETTINGS = <yaml_spec> ]

ALTER DATABASE <name> SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER DATABASE <name> UNSET TAG <tag_name> [ , <tag_name> ... ]

ALTER DATABASE [ IF EXISTS ] <name> UNSET { DATA_RETENTION_TIME_IN_DAYS         |
                                            MAX_DATA_EXTENSION_TIME_IN_DAYS     |
                                            EXTERNAL_VOLUME                     |
                                            CATALOG                             |
                                            ICEBERG_VERSION_DEFAULT             |
                                            ENABLE_ICEBERG_MERGE_ON_READ        |
                                            DEFAULT_DDL_COLLATION               |
                                            DEFAULT_NOTEBOOK_COMPUTE_POOL_CPU   |
                                            DEFAULT_NOTEBOOK_COMPUTE_POOL_GPU   |
                                            OBJECT_VISIBILITY                   |
                                            STORAGE_SERIALIZATION_POLICY        |
                                            EVENT_TABLE = <event_table_name>    |
                                            COMMENT                             |
                                            CATALOG_SYNC                        |
                                            REPLICABLE_WITH_FAILOVER_GROUPS     |
                                            BASE_LOCATION_PREFIX                |
                                            DEFAULT_STREAMLIT_NOTEBOOK_WAREHOUSE|
                                            CLASSIFICATION_PROFILE              |
                                            CONTACT <purpose>                   |
                                            ENABLE_DATA_COMPACTION
                                          }
                                          [ , ... ]
```

## Database replication and failover syntax

> **Important:**
>
> This section describes a limited database replication feature that is different from the
> [account replication feature](../../user-guide/account-replication-intro.md). Snowflake strongly
> recommends using the account replication feature to replicate and failover databases.

**Database Replication**

```sqlsyntax
ALTER DATABASE <name> ENABLE REPLICATION TO ACCOUNTS <account_identifier> [ , <account_identifier> ... ] [ IGNORE EDITION CHECK ]

ALTER DATABASE <name> DISABLE REPLICATION [ TO ACCOUNTS <account_identifier> [ , <account_identifier> ... ] ]

ALTER DATABASE <name> REFRESH
```

**Database Failover**

```sqlsyntax
ALTER DATABASE <name> ENABLE FAILOVER TO ACCOUNTS <account_identifier> [ , <account_identifier> ... ]

ALTER DATABASE <name> DISABLE FAILOVER [ TO ACCOUNTS <account_identifier> [ , <account_identifier> ... ] ]

ALTER DATABASE <name> PRIMARY
```

## Parameters

`name`
:   Specifies the identifier for the database to alter. If the identifier contains spaces, special characters, or mixed-case characters, the entire
    string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

`RENAME TO new_db_name`
:   Specifies the new identifier for the database; must be unique for your account.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

    When an object is renamed, other objects that reference it must be updated with the new name.

`SWAP WITH target_db_name`
:   Swaps all objects (schemas, tables, views, etc.) and metadata, including identifiers, between the two specified databases. Also swaps all access
    control privileges granted on the databases and objects they contain. `SWAP WITH` essentially performs a rename of both databases as a
    single operation.

`SET ...`
:   Specifies one (or more) properties to set for the database (separated by blank spaces, commas, or new lines):

    `DATA_RETENTION_TIME_IN_DAYS = num`
    :   Specifies the number of days for which Time Travel actions (CLONE and UNDROP) can be performed on the database, as well as specifying the
        default Time Travel retention time for all schemas created in the database.

        The value you can specify depends on the Snowflake Edition you are using:

        * Standard Edition: `0` or `1`
        * Enterprise Edition (or higher): `0` to `90`

    `MAX_DATA_EXTENSION_TIME_IN_DAYS = integer`
    :   Object parameter that specifies the maximum number of days for which Snowflake can extend the data retention period for tables in the database
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

        * Any new columns added to existing tables in the database.
        * All columns in new tables added to the database.

        Setting the parameter does not change the collation specification for any existing columns.

        For more information about the parameter, see [DEFAULT_DDL_COLLATION](../parameters.md).

    `DEFAULT_NOTEBOOK_COMPUTE_POOL_CPU = compute_pool_name`
    :   CPU compute pool name that overrides the default CPU compute pool Snowflake provisioned in your account for running Notebooks. For more information, see [System compute pools](../../developer-guide/snowpark-container-services/working-with-compute-pool.md).

    `DEFAULT_NOTEBOOK_COMPUTE_POOL_GPU = compute_pool_name`
    :   GPU compute pool name that overrides the default GPU compute pool Snowflake provisioned in your account for running Notebooks. For more information, see [System compute pools](../../developer-guide/snowpark-container-services/working-with-compute-pool.md).

    `OBJECT_VISIBILITY = {object_visibility_spec | PRIVILEGED }`
    :   [Preview Feature](../../release-notes/preview-features.md) — Open

        Available to all accounts.

        Specifies the visibility of objects in the database, which controls the [discoverability of the objects](../../user-guide/ui-snowsight/object-visibility-universal-search.md)
        and enables users without explicit access privileges to find objects and request access.

        * A YAML specification describing the visibility in one of the following formats:

          ```sqlexample-yaml
          $$
          organization_targets:
            - all_accounts_including_external
          $$
          ```

          Or

          ```sqlexample-yaml
          $$
          organization_targets:
            - account: <account_name_1>
            - account: <account_name_2>
            - ...
            - organization_user_group: <org_user_group_1>
            - organization_user_group: <org_user_group_2>
          $$
          ```

          In the syntax above:

          + `all_accounts_including_external`: Specifies that all users in all accounts in the organization can see the object. This includes
            all accounts within the organization, even those to which external parties may have been given access, such as
            [reader accounts](../../user-guide/data-sharing-reader-create.md).
          + `account: account_name`: Specifies that all users in the specified account can see the object. You can specify multiple accounts.
            Note that `account` is the account name, not the account locator. You must specify only the account name, excluding the organization name.09-22
          + `organization_user_group: org_user_group`: Specifies that the specified [organization user group](../../user-guide/organization-users.md) can
            see the object in all accounts in the organization where the [organization user group has been imported](../../user-guide/organization-users.md).
        * `PRIVILEGED`: Specifies that only roles within the current account that are granted an explicit privilege on the object can see the object.
          This is the default behavior in Snowflake.

        For examples, see [Make database objects discoverable in Universal Search](../../user-guide/ui-snowsight/object-visibility-universal-search.md).

        Default: `'PRIVILEGED'`

    `LOG_LEVEL = 'log_level'`
    :   Specifies the severity level of messages that should be ingested and made available in the active event table. Messages at
        the specified level (and at more severe levels) are ingested.

        For more information about levels, see [LOG_LEVEL](../parameters.md). For information about setting the log level, see
        [Setting levels for logging, metrics, and tracing](../../developer-guide/logging-tracing/telemetry-levels.md).

    `METRIC_LEVEL = 'metric_level'`
    :   Specifies whether metrics data should be ingested and made available in the active event table.

        For more information, see [METRIC_LEVEL](../parameters.md) and [Setting levels for logging, metrics, and tracing](../../developer-guide/logging-tracing/telemetry-levels.md).

    `TRACE_LEVEL = 'trace_level'`
    :   Controls how trace events are ingested into the event table.

        For information about levels, see [TRACE_LEVEL](../parameters.md). For information about setting the trace level, see
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

    `EVENT_TABLE = event_table_name`
    :   Specifies the fully-qualified name of the event table that should collect telemetry data from objects in the database, such as
        procedures and UDFs.

        For more information, see [Associate an event table with an object](../../developer-guide/logging-tracing/event-table-setting-up.md).

        Associating an event table with a database is available in [Enterprise Edition or higher](../../user-guide/intro-editions.md).

    `CLASSIFICATION_PROFILE = 'profile_name'`
    :   Sets a classification profile on the database to implement [sensitive data classification](../../user-guide/classify-auto.md)
        for all of the tables and views in the database.

        Specify `profile_name` as a fully qualified name of a classification profile (that is, an instance of the
        CLASSIFICATION_PROFILE class).

    `COMMENT = 'string_literal'`
    :   Adds a comment or overwrites an existing comment for the database.

    `CATALOG_SYNC = 'snowflake_open_catalog_integration_name'`
    :   Specifies the name of a catalog integration configured for [Snowflake Open Catalog](https://other-docs.snowflake.com/en/opencatalog/overview).
        If specified, Snowflake syncs Snowflake-managed Apache Iceberg™ tables in the database with an external catalog in your Snowflake Open Catalog account. For more
        information about syncing Snowflake-managed Iceberg tables with Open Catalog, see [Sync a Snowflake-managed table with Snowflake Open Catalog](../../user-guide/tables-iceberg-open-catalog-sync.md).

        For more information about this parameter, see [CATALOG_SYNC](../parameters.md).

        Default: No value

    `REPLICABLE_WITH_FAILOVER_GROUPS = { 'YES' | 'NO' }`
    :   Specifies if all the schemas in the database are eligible for replication.
        You can set this property to `NO` for a database, and then allow some schemas
        to be replicated by setting the equivalent property to `YES` for those schemas.

        For more information about this parameter, see [Schema-level replication for failover groups](../../user-guide/account-replication-config.md).

        Default: `'YES'`

    `DEFAULT_STREAMLIT_NOTEBOOK_WAREHOUSE`
    :   Specifies the default warehouse to be used when creating a notebook using SQL.

    `BASE_LOCATION_PREFIX = 'string'`
    :   Specifies a prefix for Snowflake to use in the write path for Snowflake-managed Apache Iceberg™ tables.
        For more information,
        see [data and metadata directories for Iceberg tables](../../user-guide/tables-iceberg-storage.md) and
        [BASE_LOCATION_PREFIX](../parameters.md) in the Snowflake Parameters topic.

        Default: No value

    `ENABLE_DATA_COMPACTION = { TRUE | FALSE }`
    :   Specifies whether Snowflake should enable data compaction on Snowflake-managed [Apache Iceberg™ tables](../../user-guide/tables-iceberg.md).

        * `TRUE`: Snowflake performs data compaction on the tables.
        * `FALSE`: Snowflake doesn’t perform data compaction on the tables.

        Default: `TRUE`

        For more information, see [ENABLE_DATA_COMPACTION](../parameters.md) and [Set data compaction](../../user-guide/tables-iceberg-manage.md).

    `DATA_QUALITY_MONITORING_SETTINGS = yaml_spec`
    :   [Preview Feature](../../release-notes/preview-features.md) — Open

        Available to all accounts that are Enterprise Edition (or higher).

        To inquire about upgrading, please contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).

        Specifies settings that control whether notifications are sent when data quality issues are detected in the database. Set the property
        to a [dollar-quoted](../data-types-text.md) YAML specification in the following format:

        ```sqlexample-yaml
        $$
        notification:
          enabled: <boolean>
          integrations:
            - <notification_integration>
          metadata_included: <boolean>
        $$
        ```

        In the syntax above:

        * `enabled`: If `true`, notifications are sent when there is a data quality issue.
        * `integrations`: Specifies a list of [notification integrations](create-notification-integration.md) that
          provide an interface between Snowflake and a third-party messaging service that sends the notifications.
        * `metadata_included`: If `true`, the notification includes metadata that identifies which object within the database had
          the data quality issue. If `false`, the notification is sent, but it doesn’t identify which object had the issue.

        For more information about setting this parameter, including an example, see [Configure database settings for data quality notifications](../../user-guide/data-quality-notifications.md).

`UNSET ...`
:   Specifies one (or more) properties and/or parameters to unset for the database, which resets them to the defaults:

    * `DATA_RETENTION_TIME_IN_DAYS`
    * `MAX_DATA_EXTENSION_TIME_IN_DAYS`
    * `EXTERNAL_VOLUME`
    * `CATALOG`
    * `ICEBERG_VERSION_DEFAULT`
    * `ENABLE_ICEBERG_MERGE_ON_READ`
    * `DEFAULT_DDL_COLLATION`
    * `TAG tag_name [ , tag_name ... ]`
    * `DEFAULT_NOTEBOOK_COMPUTE_POOL_CPU`
    * `DEFAULT_NOTEBOOK_COMPUTE_POOL_GPU`
    * `STORAGE_SERIALIZATION_POLICY`
    * `EVENT_TABLE = event_table_name`
    * `COMMENT`
    * `CATALOG_SYNC`
    * `REPLICABLE_WITH_FAILOVER_GROUPS`
    * `BASE_LOCATION_PREFIX`
    * `DEFAULT_STREAMLIT_NOTEBOOK_WAREHOUSE`
    * `CLASSIFICATION_PROFILE`
    * `CONTACT purpose`
    * `ENABLE_DATA_COMPACTION`

    You can reset multiple properties/parameters with a single ALTER statement; however, each property/parameter must be separated by a
    comma. When resetting a property/parameter, specify only the name; specifying a value for the property will return an error.

    You cannot unset the CONTACT property with other properties in the same statement.

## Database replication and failover parameters

> **Important:**
>
> This section describes a limited database replication feature that is different from the
> [account replication feature](../../user-guide/account-replication-intro.md). Snowflake strongly
> recommends using the account replication feature to replicate and failover databases.

`ENABLE REPLICATION TO ACCOUNTS account_identifier [ , account_identifier ... ]`
:   Promotes a local database to serve as a primary database for replication. A primary database can be replicated in one or more accounts,
    allowing users in those accounts to query objects in each *secondary* (i.e. replica) database.

    Alternatively, modify an existing primary database to add to or remove from the list of accounts that can store a replica of the database.

    Provide a comma-separated list of accounts in your organization that can store a replica of this database.

    `account_identifier`
    :   Unique identifier of the account. The preferred identifier is `organization_name.account_name`. To view the list of accounts
        enabled for replication in your organization, query [SHOW REPLICATION ACCOUNTS](show-replication-accounts.md).

        Though the legacy account locator can also be used as the account identifier, its use is discouraged as it may not work in the future.
        For more information about using the account locator as an account identifier, see Database Replication and Failover Usage Notes.

    `IGNORE EDITION CHECK`
    :   Allows replicating data to accounts on lower editions in either of the following scenarios:

        * The primary database is in a Business Critical (or higher) account but one or more of the accounts approved for replication are on lower
          editions. Business Critical Edition is intended for Snowflake accounts with extremely sensitive data.
        * The primary database is in a Business Critical (or higher) account and a signed business associate agreement is in place to store PHI data
          in the account per HIPAA and [HITRUST](../../user-guide/intro-cloud-platforms.md) regulations, but no such agreement is in place for one or more of the
          accounts approved for replication, regardless if they are Business Critical (or higher) accounts.

        Both scenarios are prohibited by default in an effort to help prevent account administrators for Business Critical (or higher) accounts from
        inadvertently replicating sensitive data to accounts on lower editions.

`DISABLE REPLICATION [ TO ACCOUNTS account_identifier [ , account_identifier ... ] ]`
:   Disables replication for this primary database, meaning no replica of this database (i.e. secondary database) in another account can be refreshed.
    Any secondary databases remain linked to the primary database, but requests to refresh a secondary database are denied.

    Note that disabling replication for a primary database does not prevent it from being replicated to the same account; therefore, the database
    continues to be listed in the [SHOW REPLICATION DATABASES](show-replication-databases.md) output.

    Optionally provide a comma-separated list of accounts in your organization to disable replication for this database only in the specified
    accounts.

    `account_identifier`
    :   Unique identifier of the account. The preferred identifier is `organization_name.account_name`. To view the list of accounts
        enabled for replication in your organization, query [SHOW REPLICATION ACCOUNTS](show-replication-accounts.md).

        Though the legacy account locator can also be used as the account identifier, its use is discouraged as it may not work in the future.
        For more information about using the account locator as an account identifier, see Database Replication and Failover Usage Notes.

`REFRESH`
:   Refreshes a secondary database from a snapshot of its primary database. A snapshot includes changes to the objects and data.

`ENABLE FAILOVER TO ACCOUNTS account_identifier [ , account_identifier ... ]`
:   Specifies a comma-separated list of accounts in your organization where a replica of this primary database can be promoted to serve as the
    primary database.

    `account_identifier`
    :   Unique identifier of the account. The preferred identifier is `organization_name.account_name`. To view the list of accounts
        enabled for replication in your organization, query [SHOW REPLICATION ACCOUNTS](show-replication-accounts.md).

        Though the legacy account locator can also be used as the account identifier, its use is discouraged as it may not work in the future.
        For more information about using the account locator as an account identifier, see Database Replication and Failover Usage Notes.

`DISABLE FAILOVER [ TO ACCOUNTS account_identifier [ , account_identifier ... ] ]`
:   Disables failover for this primary database, meaning no replica of this database (i.e. secondary database) can be promoted to serve as the
    primary database.

    Optionally provide a comma-separated list of accounts in your organization to disable failover for this database only in the specified
    accounts.

    `account_identifier`
    :   Unique identifier of the account. The preferred identifier is `organization_name.account_name`. To view the list of accounts
        enabled for replication in your organization, query [SHOW REPLICATION ACCOUNTS](show-replication-accounts.md).

        Though the legacy account locator can also be used as the account identifier, its use is discouraged as it may not work in the future.
        For more information about using the account locator as an account identifier, see Database Replication and Failover Usage Notes.

`PRIMARY`
:   Promotes the specified secondary (replica) database to serve as the primary database. When promoted, the database becomes writeable. At the same
    time, the previous primary database becomes a read-only secondary database.

## Usage notes

* To rename a database, the role used to perform the operation must have the CREATE DATABASE global privilege and OWNERSHIP privilege on
  the database.
* To swap two databases, the role used to perform the operation must have OWNERSHIP privileges on both databases.
* To update a comment, the role used to perform the operation must be granted or inherit the MODIFY privilege on the database.
* To specify the default version of the Apache Iceberg™ specification that Iceberg tables conform to, you must use a role that has been granted the OWNERSHIP privilege on the database.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Database replication and failover usage notes

> **Important:**
>
> This section describes a limited database replication feature that is different from the
> [account replication feature](../../user-guide/account-replication-intro.md). Snowflake strongly
> recommends using the account replication feature to replicate and failover databases.

* Only account administrators (users with the ACCOUNTADMIN role) can enable and manage database replication and failover.
* A default 10 TB size limit is applied when a primary database is initially replicated to a secondary database. To change or remove the size limit,
  set the [INITIAL_REPLICATION_SIZE_LIMIT_IN_TB](../parameters.md) parameter at the account level.

  Note that there is currently no default size limit applied to subsequent refreshes of a secondary database.
* The preferred method of identifying an account uses the organization name and account name as the account
  identifier. If you decide to use the legacy account locator instead, see [Account identifiers for replication and failover](../../user-guide/admin-account-identifier.md).

## General examples

Rename database `db1` to `db2`:

> ```sqlexample
> ALTER DATABASE IF EXISTS db1 RENAME TO db2;
> ```

## Database replication examples

> **Important:**
>
> This section describes a limited database replication feature that is different from the
> [account replication feature](../../user-guide/account-replication-intro.md). Snowflake strongly
> recommends using the account replication feature to replicate and failover databases.

Use a replication or failover group to replicate and failover a single database. For examples, see one of the following:

* [Create a failover group to enable replication and failover for a database](create-failover-group.md).
* [Replicate a single database](create-replication-group.md).
