# Source: https://docs.snowflake.com/en/sql-reference/sql/create-dynamic-table.md

# CREATE DYNAMIC TABLE

Creates a [dynamic table](../../user-guide/dynamic-tables-about.md), based on a specified query.

This command supports the following variants:

* CREATE OR ALTER DYNAMIC TABLE: Creates a dynamic table if it doesn’t exist or alters an existing dynamic table.
* CREATE DYNAMIC TABLE FROM BACKUP SET: Restores a dynamic table from a back up.
* CREATE DYNAMIC TABLE … CLONE: Creates a clone of an existing dynamic table.
* CREATE DYNAMIC ICEBERG TABLE: Creates a dynamic Apache Iceberg™ table.

See also:
:   [ALTER DYNAMIC TABLE](alter-dynamic-table.md), [DESCRIBE DYNAMIC TABLE](desc-dynamic-table.md), [DROP DYNAMIC TABLE](drop-dynamic-table.md) , [SHOW DYNAMIC TABLES](show-dynamic-tables.md),
    [CREATE OR ALTER <object>](create-or-alter.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] [ TRANSIENT ] DYNAMIC TABLE [ IF NOT EXISTS ] <name> (
    -- Column definition
    <col_name> <col_type>
      [ [ WITH ] MASKING POLICY <policy_name> [ USING ( <col_name> , <cond_col1> , ... ) ] ]
      [ [ WITH ] PROJECTION POLICY <policy_name> ]
      [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
      [ COMMENT '<string_literal>' ]
      [ WITH CONTACT ( <purpose> = <contact_name> [ , <purpose> = <contact_name> ... ] ) ]

    -- Additional column definitions
    [ , <col_name> <col_type> [ ... ] ]

  )
  TARGET_LAG = { '<num> { seconds | minutes | hours | days }' | DOWNSTREAM }
  WAREHOUSE = <warehouse_name>
  [ INITIALIZATION_WAREHOUSE = <warehouse_name> ]
  [ REFRESH_MODE = { AUTO | FULL | INCREMENTAL } ]
  [ INITIALIZE = { ON_CREATE | ON_SCHEDULE } ]
  [ CLUSTER BY ( <expr> [ , <expr> , ... ] ) ]
  [ DATA_RETENTION_TIME_IN_DAYS = <integer> ]
  [ MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer> ]
  [ COMMENT = '<string_literal>' ]
  [ COPY GRANTS ]
  [ [ WITH ] ROW ACCESS POLICY <policy_name> ON ( <col_name> [ , <col_name> ... ] ) ]
  [ [ WITH ] AGGREGATION POLICY <policy_name> [ ENTITY KEY ( <col_name> [ , <col_name> ... ] ) ] ]
  [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
  [ REQUIRE USER ]
  [ IMMUTABLE WHERE ( <expr> ) ]
  [ BACKFILL FROM ]
  [ EXECUTE AS USER <user_name>
    [ USE SECONDARY ROLES { ALL | NONE | <role> [ , ... ] } ]
  ]
  [ ROW_TIMESTAMP = { TRUE | FALSE } ]
  AS <query>
```

## Variant syntax

### CREATE OR ALTER DYNAMIC TABLE

```sqlsyntax
CREATE OR ALTER DYNAMIC TABLE <name> (
  -- Column definition
  <col_name> <col_type>
    [ COLLATE '<collation_specification>' ]
    [ COMMENT '<string_literal>' ]

  -- Additional column definitions
  [ , <col_name> <col_type> [ ... ] ]
  )
  TARGET_LAG = { '<num> { seconds | minutes | hours | days }' | DOWNSTREAM }
  WAREHOUSE = <warehouse_name>
  [ REFRESH_MODE = FULL | INCREMENTAL | AUTO ]
  [ IMMUTABLE WHERE ( <expr> ) ]
  [ CLUSTER BY ( <expr> [ , <expr> , ... ] ) ]
  [ DATA_RETENTION_TIME_IN_DAYS = <integer> ]
  [ MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer> ]
  [ COMMENT = '<string_literal>' ]
  [ ROW_TIMESTAMP = { TRUE | FALSE } ]
```

Creates a dynamic table if it doesn’t exist, or alters it according to the dynamic table
definition. The CREATE OR ALTER DYNAMIC TABLE syntax follows the rules of a
CREATE DYNAMIC TABLE statement and has the same limitations as
an [ALTER DYNAMIC TABLE](alter-dynamic-table.md) statement.

For more information, see [CREATE OR ALTER <object>](create-or-alter.md).

Changes to the following dynamic table properties and parameters preserve data:

* TARGET_LAG
* WAREHOUSE
* CLUSTER BY
* DATA_RETENTION_TIME_IN_DAYS
* MAX_DATA_EXTENSION_TIME_IN_DAYS
* COMMENT
* IMMUTABLE WHERE

  * When specified, only the mutable region is reinitialized and data in the immutable region is preserved. For more information, see [Understanding immutability constraints](../../user-guide/dynamic-tables-immutability-constraints.md).

Changes to the following dynamic table properties and parameters trigger a [reinitialization](../../user-guide/dynamic-tables-refresh.md):

* REFRESH_MODE
* Changes to the query or column list:

  * Dropping existing columns is supported.
  * Adding new columns is supported, but they can only be added at the end of existing columns.
  * Dropping columns that are used in an IMMUTABLE WHERE predicate or as clustering keys isn’t supported.

For more information, see [CREATE OR ALTER TABLE usage notes](create-table.md).

### CREATE DYNAMIC TABLE FROM BACKUP SET

```sqlsyntax
CREATE DYNAMIC TABLE <name> FROM BACKUP SET <backup_set> IDENTIFIER '<backup_id>'
```

The FROM BACKUP SET clause restores a dynamic table from a backup. You don’t specify other table
properties because they’re all the same as in the backed-up table.

This form doesn’t have a CREATE OR REPLACE clause. You typically either restore the
dynamic table under a new name and recover any data or other objects from this new table,
or rename the original table and then restore the table under the original name.

> **Note:**
>
> The backup set is associated with the internal table ID of the original table.
> Any more backups you add to the backup set use the original table, even if you
> changed its name. If you want to make backups of the newly restored table, create a
> new backup set for it.
>
> When you restore a dynamic table from a backup, Snowflake
> [automatically initializes](../../user-guide/dynamic-tables-refresh.md)
> the new table during its first refresh.

For more information about backups, see [Backups for disaster recovery and immutable storage](../../user-guide/backups.md).

`backup_set`
:   Specifies the name of a backup set created for a specific dynamic table.
    You can use the SHOW BACKUP SETS command to locate the right backup set.

`backup_id`
:   Specifies the identifier of a specific backup within that backup set.
    You can use the SHOW BACKUPS IN BACKUP SET command to locate the right identifier within the backup
    set, based on the creation date and time for the backup.

### CREATE DYNAMIC TABLE … CLONE

Creates a new dynamic table with the same column definitions and containing all the
existing data from the source dynamic table, without actually copying the data.

Cloned dynamic tables, whether cloned directly or as part of a cloned database or schema, are suspended by default. In [DYNAMIC_TABLE_GRAPH_HISTORY](../functions/dynamic_table_graph_history.md),
this appears as CLONED_AUTO_SUSPENDED in the SCHEDULING_STATE column. Any downstream dynamic tables are also suspended, shown as UPSTREAM_CLONED_AUTO_SUSPENDED.
For more information, see [Automatic dynamic table suspension](../../user-guide/dynamic-tables-suspend-resume.md).

You can also clone a dynamic table as it existed at a specific point in the past. For
more information, see [Cloning considerations](../../user-guide/object-clone.md).

```sqlsyntax
CREATE [ OR REPLACE ] [ TRANSIENT ] DYNAMIC TABLE <name>
  CLONE <source_dynamic_table>
        [ { AT | BEFORE } ( { TIMESTAMP => <timestamp> | OFFSET => <time_difference> | STATEMENT => <id> } ) ]
  [
    COPY GRANTS
    TARGET_LAG = { '<num> { seconds | minutes | hours | days }' | DOWNSTREAM }
    WAREHOUSE = <warehouse_name>
    EXECUTE AS USER <user_name>
      USE SECONDARY ROLES { ALL | NONE | <role> [ , ... ] }
  ]
```

If the source dynamic table has clustering keys, then the cloned dynamic table has
clustering keys. By default, Automatic Clustering is suspended for the new table, even
if Automatic Clustering was not suspended for the source table.

For more details about cloning, see [CREATE <object> … CLONE](create-clone.md).

### CREATE DYNAMIC ICEBERG TABLE

Creates a new dynamic Apache Iceberg™ table. For information about Iceberg tables, see
[Apache Iceberg™ tables](../../user-guide/tables-iceberg.md) and [CREATE ICEBERG TABLE (Snowflake as the Iceberg catalog)](create-iceberg-table-snowflake.md).

```sqlsyntax
CREATE [ OR REPLACE ] DYNAMIC ICEBERG TABLE <name> (
  -- Column definition
  <col_name> <col_type>
    [ [ WITH ] MASKING POLICY <policy_name> [ USING ( <col_name> , <cond_col1> , ... ) ] ]
    [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
    [ COMMENT '<string_literal>' ]

  -- Additional column definitions
  [ , <col_name> <col_type> [ ... ] ]

)
TARGET_LAG = { '<num> { seconds | minutes | hours | days }' | DOWNSTREAM }
WAREHOUSE = <warehouse_name>
[ EXTERNAL_VOLUME = '<external_volume_name>' ]
[ CATALOG = 'SNOWFLAKE' ]
[ BASE_LOCATION = '<optional_directory_for_table_files>' ]
[ ICEBERG_VERSION = <integer> ]
[ REFRESH_MODE = { AUTO | FULL | INCREMENTAL } ]
[ INITIALIZE = { ON_CREATE | ON_SCHEDULE } ]
[ CLUSTER BY ( <expr> [ , <expr> , ... ] ) ]
[ DATA_RETENTION_TIME_IN_DAYS = <integer> ]
[ MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer> ]
[ COMMENT = '<string_literal>' ]
[ COPY GRANTS ]
[ [ WITH ] ROW ACCESS POLICY <policy_name> ON ( <col_name> [ , <col_name> ... ] ) ]
[ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
[ REQUIRE USER ]
[ EXECUTE AS USER <user_name>
  [ USE SECONDARY ROLES { ALL | NONE | <role> [ , ... ] } ]
]
AS <query>
```

For more information about usage and limitations, see
[Create dynamic Apache Iceberg™ tables](../../user-guide/dynamic-tables-create-iceberg.md).

## Required parameters

`name`
:   Specifies the identifier (i.e. name) for the dynamic table; must be unique for the schema in which the dynamic table is created.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

`TARGET_LAG = { num { seconds | minutes | hours | days } | DOWNSTREAM }`
:   Specifies the lag for the dynamic table:

    > `'num seconds | minutes | hours | days'`
    > :   Specifies the maximum amount of time that the dynamic table’s content should lag behind updates to the source tables.
    >
    >     For example:
    >
    >     * If the data in the dynamic table should lag by no more than 5 minutes, specify `5 minutes`.
    >     * If the data in the dynamic table should lag by no more than 5 hours, specify `5 hours`.
    >
    >     Must be a minimum of 60 seconds. If the dynamic table depends on another dynamic table, the minimum target lag must
    >     be greater than or equal to the target lag of the dynamic table it depends on.
    >
    > `DOWNSTREAM`
    > :   Specifies that the dynamic table should be refreshed only when dynamic tables that depend on it are refreshed.

    For information on how target lag affects refresh frequency and costs, see [Identify the right target lag](../../user-guide/dynamic-tables-performance-optimize.md).

`WAREHOUSE = warehouse_name`
:   Specifies the name of the warehouse that provides the compute resources for refreshing the dynamic table.

    You must use a role that has the USAGE privilege on this warehouse in order to create the dynamic table. For limitations and more
    information, see [Privileges to create a dynamic table](../../user-guide/dynamic-tables-privileges.md).

    For guidance on choosing a warehouse for optimal refresh performance, see [Adjust your warehouse configuration](../../user-guide/dynamic-tables-performance-optimize.md).

`AS query`
:   Specifies the query whose results the dynamic table should contain.

## Optional parameters

`INITIALIZATION_WAREHOUSE = warehouse_name`
:   Specifies a warehouse to use for all dynamic table [initializations and reinitializations](../../user-guide/dynamic-tables-refresh.md).

    If this parameter isn’t included in the CREATE DYNAMIC TABLE statement, the dynamic table uses the warehouse that is specified by the
    required WAREHOUSE parameter for all refreshes.

    You must use a role that has the USAGE privilege on this warehouse for you to create the dynamic table. For limitations and more
    information, see [Privileges to create a dynamic table](../../user-guide/dynamic-tables-privileges.md).

`TRANSIENT`
:   Specifies that the table is transient.

    Like permanent dynamic tables, [transient](../../user-guide/tables-temp-transient.md) dynamic tables exist until
    they’re explicitly dropped, and are available to any user with the appropriate privileges. Transient dynamic
    tables don’t retain data in fail-safe storage, which helps reduce storage costs, especially for tables that
    refresh frequently. Due to this reduced level of durability, transient dynamic tables are best used for
    transitory data that doesn’t need the same level of data protection and recovery provided by permanent tables.

    Default: No value. If a dynamic table is not declared as `TRANSIENT`, it is permanent.

`REFRESH_MODE = { AUTO | FULL | INCREMENTAL }`
:   Specifies the [refresh mode](../../user-guide/dynamic-tables-refresh.md) for the dynamic table.

    This property cannot be altered after you create the dynamic table. To modify the property, recreate the dynamic table with a CREATE OR
    REPLACE DYNAMIC TABLE command.

    > `AUTO`
    > :   When refresh mode is `AUTO`, the system attempts to apply an incremental refresh by default. However, when incremental refresh isn’t
    >     supported or expected to perform well, the dynamic table automatically selects full refresh instead. For more information, see
    >     [Dynamic table refresh modes](../../user-guide/dynamic-tables-refresh.md) and [Choose a refresh mode](../../user-guide/dynamic-tables-performance-optimize.md).
    >
    >     To determine the best mode for your use case, experiment with refresh modes and automatic recommendations. For consistent behavior across
    >     Snowflake releases, explicitly set the refresh mode on all dynamic tables.
    >
    >     To verify the refresh mode for your dynamic tables, see [Refresh mode](../../user-guide/dynamic-tables-performance-monitor.md).
    >
    > `FULL`
    > :   Enforces a full refresh of the dynamic table, even if the dynamic table can be incrementally refreshed.
    >
    > `INCREMENTAL`
    > :   Enforces an incremental refresh of the dynamic table. If the query that underlies the dynamic table can’t perform an incremental refresh,
    >     dynamic table creation fails and displays an error message.
    >
    >     For information about how operators affect incremental refresh, see [Optimize queries for incremental refresh](../../user-guide/dynamic-tables-performance-optimize-query.md).
    >
    > Default: `AUTO`

`INITIALIZE`
:   Specifies the behavior of the [initial refresh](../../user-guide/dynamic-tables-refresh.md) of the dynamic table. This property cannot be
    altered after you create the dynamic table. To modify the property, replace the dynamic table with a CREATE OR REPLACE DYNAMIC TABLE command.

    > `ON_CREATE`
    > :   Refreshes the dynamic table synchronously at creation. If this refresh fails, dynamic table creation fails and displays an error message.
    >
    > `ON_SCHEDULE`
    > :   Refreshes the dynamic table at the next scheduled refresh.
    >
    >     The dynamic table is populated when the refresh schedule process runs. No data is populated when the dynamic table is created. If you try to
    >     query the table using `SELECT * FROM DYNAMIC TABLE`, you might see the following error because the first scheduled refresh has not yet
    >     occurred.
    >
    >     ```output
    >     Dynamic Table is not initialized. Please run a manual refresh or wait for a scheduled refresh before querying.
    >     ```
    >
    > Default: `ON_CREATE`

`COMMENT 'string_literal'`
:   Specifies a comment for the column.

    (Note that comments can be specified at the column level or the table level. The syntax for each is slightly different.)

`MASKING POLICY = policy_name`
:   Specifies the [masking policy](../../user-guide/security-column-intro.md) to set on a column.

`PROJECTION POLICY policy_name`
:   Specifies the [projection policy](../../user-guide/projection-policies.md) to set on a column.

    This parameter is not supported by the CREATE OR ALTER variant syntax.

`column_list`
:   If you want to change the name of a column or add a comment to a column in the dynamic table,
    include a column list that specifies the column names and, if needed, comments about
    the columns. You do not need to specify the data types of the columns.

    If any of the columns in the dynamic table are based on expressions - for example, not simple column names -
    then you must supply a column name for each column in the dynamic table. For instance, the column names are
    required in the following case:

    ```sqlexample
    CREATE DYNAMIC TABLE my_dynamic_table (pre_tax_profit, taxes, after_tax_profit)
      TARGET_LAG = '20 minutes'
        WAREHOUSE = mywh
        AS
          SELECT revenue - cost, (revenue - cost) * tax_rate, (revenue - cost) * (1.0 - tax_rate)
          FROM staging_table;
    ```

    You can specify an optional comment for each column. For example:

    ```sqlexample
    CREATE DYNAMIC TABLE my_dynamic_table (pre_tax_profit COMMENT 'revenue minus cost',
                    taxes COMMENT 'assumes taxes are a fixed percentage of profit',
                    after_tax_profit)
      TARGET_LAG = '20 minutes'
        WAREHOUSE = mywh
        AS
          SELECT revenue - cost, (revenue - cost) * tax_rate, (revenue - cost) * (1.0 - tax_rate)
          FROM staging_table;
    ```

`WITH CONTACT ( purpose = contact [ , purpose = contact ...] )`
:   Associate the new object with one or more [contacts](../../user-guide/contacts-using.md).

    Specify the WITH CONTACT clause after all other clauses except the AS clause (if that clause is supported by this command).

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

`CLUSTER BY ( expr [ , expr , ... ] )`
:   Specifies one or more columns or column expressions in the dynamic table as the clustering key. Before you specify a clustering
    key for a dynamic table, you should understand micro-partitions. For more information, see [Understanding Snowflake Table Structures](../../user-guide/tables-micro-partitions.md).

    Note the following when using clustering keys with dynamic tables:

    * Column definitions are required and must be explicitly specified in the statement.
    * By default, Automatic Clustering is not suspended for the new dynamic table, even if Automatic Clustering is suspended for the
      source table.
    * Clustering keys are not intended or recommended for all tables; they typically benefit very large (for example
      multi-terabyte) tables.
    * Specifying CLUSTER BY doesn’t cluster the data at creation time; instead, CLUSTER BY relies on
      Automatic Clustering to recluster the data over time.

    For more information, see [Clustering Keys & Clustered Tables](../../user-guide/tables-clustering-keys.md).

    Default: No value (no clustering key is defined for the table)

`DATA_RETENTION_TIME_IN_DAYS = integer`
:   Specifies the retention period for the dynamic table so that Time Travel actions (SELECT, CLONE) can be performed on historical
    data in the dynamic table. Time Travel behaves the same way for dynamic tables as it behaves for traditional tables. For more
    information, see [Understanding & using Time Travel](../../user-guide/data-time-travel.md).

    For a detailed description of this object-level parameter, as well as more information about object parameters, see
    [Parameters](../parameters.md).

    Values:

    * Standard Edition: `0` or `1`
    * Enterprise Edition:

      + `0` to `90` for permanent tables
      + `0` or `1` for temporary and transient tables

    Default:

    * Standard Edition: `1`
    * Enterprise Edition (or higher): `1` (unless a different default value was specified at the schema, database, or account level)

    > **Note:**
    >
    > A value of `0` effectively disables Time Travel for the table.

`MAX_DATA_EXTENSION_TIME_IN_DAYS = integer`
:   An object parameter that sets the maximum number of days Snowflake can extend the data retention period to prevent streams on the dynamic
    table from becoming stale.

    For a detailed description of this parameter, see [MAX_DATA_EXTENSION_TIME_IN_DAYS](../parameters.md).

`COMMENT = 'string_literal'`
:   Specifies a comment for the dynamic table.

    (Note that comments can be specified at the column level or the table level. The syntax for each is slightly different.)

    Default: No value.

`COPY GRANTS`
:   Specifies to retain the access privileges from the original table when a new dynamic table is created using any of the following CREATE DYNAMIC TABLE variants:

    * CREATE OR REPLACE DYNAMIC TABLE
    * CREATE OR REPLACE DYNAMIC ICEBERG TABLE
    * CREATE OR REPLACE DYNAMIC TABLE … CLONE

    This parameter copies all privileges except OWNERSHIP from the existing dynamic table to the new dynamic table. The new dynamic
    table does not inherit any future grants defined for the object type in the schema. By default, the role that executes the
    CREATE DYNAMIC TABLE statement owns the new dynamic table.

    If this parameter is not included in the CREATE DYNAMIC TABLE statement, then the new table does not inherit any explicit access
    privileges granted on the original dynamic table, but does inherit any future grants defined for the object type in the schema.

    If the statement is replacing an existing table of the same name, then the grants are copied from the table being replaced. If there is
    no existing table of that name, then the grants are copied.

    For example, the following statement creates a dynamic table `dt1` cloned from `dt0` with all grants copied from `dt0`. The first
    time you run the command, `dt1` copies all grants from `dt0`. If you run the same command again, `dt1` will copy all grants from
    `dt1` and not `dt0`.

    ```sqlexample
    CREATE OR REPLACE DYNAMIC TABLE dt1 CLONE dt0
      COPY GRANTS;
    ```

    Note the following:

    * With [data sharing](../../guides-overview-sharing.md):

      + If the existing dynamic table was shared to another account, the replacement dynamic table is also shared.
      + If the existing dynamic table was shared with your account as a data consumer, and access was further granted to other roles in
        the account (using `GRANT IMPORTED PRIVILEGES` on the parent database), access is also granted to the replacement dynamic
        table.
    * The [SHOW GRANTS](show-grants.md) output for the replacement dynamic table lists the grantee for the copied privileges as the
      role that executed the CREATE TABLE statement, with the current timestamp when the statement was executed.
    * The operation to copy grants occurs atomically in the CREATE DYNAMIC TABLE command (i.e. within the same transaction).

    > **Important:**
    >
    > The COPY GRANTS parameter can be placed anywhere in a CREATE [ OR REPLACE ] DYNAMIC TABLE command, except after the query
    > definition.
    >
    > For example, the following dynamic table will fail to create:
    >
    > ```sqlexample
    > CREATE OR REPLACE DYNAMIC TABLE my_dynamic_table
    >   TARGET_LAG = DOWNSTREAM
    >   WAREHOUSE = mywh
    >   AS
    >     SELECT * FROM staging_table
    >     COPY GRANTS;
    > ```

`ROW ACCESS POLICY policy_name ON ( col_name [ , col_name ... ] )`
:   Specifies the [row access policy](../../user-guide/security-row-intro.md) to set on a dynamic table.

`TAG ( tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ] )`
:   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

    The tag value is always a string, and the maximum number of characters for the tag value is 256.

    For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

`AGGREGATION POLICY policy_name [ ENTITY KEY ( col_name [ , col_name ... ] ) ]`
:   Specifies an [aggregation policy](../../user-guide/aggregation-policies.md) to set on a dynamic table. You can apply one or more aggregation
    policies on a table.

    Use the optional ENTITY KEY parameter to define which columns uniquely identity an entity within the dynamic table. For more information,
    see [Implementing entity-level privacy with aggregation policies](../../user-guide/aggregation-policies-entity-privacy.md). You can specify one or more entity keys for an aggregation policy.

    This parameter is not supported by the CREATE OR ALTER variant syntax.

`REQUIRE USER`
:   When specified, the dynamic table cannot run unless a user is specified. The dynamic table is not able to refresh unless a user is set
    in a manual refresh with the [COPY SESSION](alter-dynamic-table.md) parameter specified.

    If this option is enabled, the dynamic table must be created with the ON_SCHEDULE parameter for
    `INITIALIZE`.

`IMMUTABLE WHERE`
:   Specifies a condition that defines the immutable portion of the dynamic table. For more information, see [Understanding immutability constraints](../../user-guide/dynamic-tables-immutability-constraints.md).

`BACKFILL FROM <name>`
:   Specifies the table to backfill data from.

    Only data defined by the [IMMUTABLE WHERE immutability constraint](../../user-guide/dynamic-tables-immutability-constraints.md) can be backfilled because
    the backfill data must remain unchanged, even if it differs from the upstream source.

    For more information, see [Backfill examples](../../user-guide/dynamic-tables-performance-optimize-immutability.md).

`EXECUTE AS USER user_name`
:   Refreshes the dynamic table as the specified user.

    To specify EXECUTE AS USER, you must use a role that has been granted the IMPERSONATE privilege on the `user_name` user. To grant this privilege,
    run the [GRANT <privileges> … TO ROLE](grant-privilege.md) command.

    `USE SECONDARY ROLES { ALL | NONE | <role> [ , ... ] }`
    :   Specifies the secondary roles to use on the dynamic table. Can be used to override the default secondary roles that are otherwise used in execution.

        Can only be used with the EXECUTE AS USER option.

    For more information, see [Refresh dynamic tables with specific user privileges and secondary roles](../../user-guide/dynamic-tables-privileges.md).

`ROW_TIMESTAMP = { TRUE | FALSE }`
:   Specifies whether to enable row timestamps on the table. You must use a role with the OWNERSHIP privilege.

    For more information, see [Use row timestamps to measure latency in your pipelines](../../user-guide/data-engineering/row-timestamps.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE DYNAMIC TABLE | Schema in which you plan to create the dynamic table. |  |
| SELECT | Tables, views, and dynamic tables that you plan to query for the new dynamic table. |  |
| USAGE | Warehouse that you plan to use to refresh the table. |  |
| IMPERSONATE | User specified in EXECUTE AS USER | To refresh the dynamic table as a user, you must use a role that has been granted the IMPERSONATE privilege on that user. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* When you execute the CREATE DYNAMIC TABLE command, the current role in use becomes
  the owner of the dynamic table. This role is used to perform refreshes of the dynamic
  table in the background.
* You cannot make changes to the schema after you create a dynamic table.
* Dynamic tables are updated as underlying database objects change. Change tracking must
  be enabled on all underlying objects used by a dynamic table. See
  [Enable change tracking](../../user-guide/dynamic-tables-create.md).
* If you want to replace an existing dynamic table and need to see its current definition,
  call the [GET_DDL](../functions/get_ddl.md) function.
* Using [ORDER BY](../constructs/order-by.md) in the definition of a dynamic table
  might produce results sorted in an unexpected order. You can use ORDER BY when querying
  your dynamic table to ensure that rows selected return in a specific order.
* Snowflake doesn’t support using ORDER BY to create a view that selects from a dynamic
  table.
* To influence the order in which rows are stored in a dynamic table, consider enabling clustering.
* Some expressions, clauses, and functions are not currently supported in dynamic tables.
  For a complete list, see [Dynamic table limitations](../../user-guide/dynamic-tables-limitations.md).
* Using `OR REPLACE` is the equivalent to using DROP DYNAMIC TABLE on the existing dynamic table and then creating a new
  dynamic table with the same name. However, Snowflake doesn’t drop the old dynamic table until it has created the new dynamic table,
  including the initial refresh if `INITIALIZE = ON_CREATE` is specified. Instead, the new dynamic table is created as a
  hidden table, the refresh is run, then Snowflake atomically swaps it in for the existing dynamic table.
* Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## CREATE OR ALTER DYNAMIC TABLE usage notes

* All limitations of the [ALTER DYNAMIC TABLE](alter-dynamic-table.md) command apply.

### Limitations

The following actions *aren’t* supported:

> * Swapping dynamic tables by using the SWAP WITH parameter.
> * Renaming a dynamic table by using the RENAME TO parameter.
> * Creating a clone of a dynamic table by using the CLONE parameter.
> * Suspending or resuming by using the SUSPEND and RESUME parameters.
> * Converting a TRANSIENT dynamic table into a non-TRANSIENT dynamic table, or vice versa.
> * Adding or changing tags and policies. Any existing tags and policies are preserved,
>   and other statements might still add or remove tags and policies.
> * Creating or altering dynamic Apache Iceberg™ tables.
> * Time Travel clone for times that are before the latest definition or refresh mode change.

Additionally, modifying the values for the REFRESH_MODE and INITIALIZE properties after
the dynamic table has been created isn’t supported. You can switch between the `AUTO`
refresh mode and the specific `INCREMENTAL` and `FULL` refresh modes, but doing so
doesn’t change the actual physical refresh mode of the dynamic table.

For example:

* If you create a dynamic table with `AUTO` refresh mode, the system immediately assigns
  a concrete mode (`INCREMENTAL` or `FULL`). When you run a subsequent CREATE OR ALTER
  DYNAMIC TABLE statement, you can specify `AUTO` or the concrete refresh mode that is chosen by
  the engine at creation. However, this doesn’t alter the assigned refresh mode; it
  remains the same.
* If you create a dynamic table with a specific refresh mode (`INCREMENTAL` or `FULL`),
  you can later specify `AUTO` in a CREATE OR ALTER DYNAMIC TABLE statement to enable
  forward compatibility. For example, if your dynamic table was created with `FULL`
  mode and is version-controlled, specifying `AUTO` in a CREATE OR ALTER DYNAMIC TABLE
  statement enables new tables to use `AUTO`, while existing tables remain in `FULL`
  mode without breaking compatibility.

### No implicit refreshes

If you change an existing dynamic table by using the CREATE OR ALTER DYNAMIC TABLE
command, the command doesn’t trigger a refresh of the dynamic table. The dynamic table is
refreshes according to its normal schedule.

However, if you create a new dynamic table by using the CREATE OR ALTER DYNAMIC TABLE
command and you specify `INITIALIZE = ON_CREATE`, the command triggers a refresh of the
dynamic table.

### Atomicity

The CREATE OR ALTER DYNAMIC TABLE command doesn’t guarantee *atomicity*. This means that if
a CREATE OR ALTER DYNAMIC TABLE statement fails during execution, it’s possible that a
subset of changes might have been applied to the table. If there’s a possibility of
partial changes, in most cases, the error message includes the following text:

```output
CREATE OR ALTER execution failed. Partial updates may have been applied.
```

For example, suppose that you wanted to change the `TARGET_LAG` property and add a
clustering key for a dynamic table, but you change your mind and terminate the statement. In
this case, the `TARGET_LAG` property might still change while the clustering key isn’t
applied.

When changes are partially applied, the resulting table is in a valid state. In the
previous example, you can use additional ALTER DYNAMIC TABLE statements to complete the
original set of changes.

To recover from partial updates, try the following recovery methods:

* **Fix forward**: Re-execute the CREATE OR ALTER DYNAMIC TABLE statement. If the
  statement succeeds on the second attempt, the target state is achieved.

  If the statement doesn’t succeed, investigate the error message. If possible, fix the
  error and re-execute the CREATE OR ALTER DYNAMIC TABLE statement.
* **Roll back**: If it isn’t possible to fix forward, manually roll back the partial
  changes:

  * Investigate the state of the table by using the [DESCRIBE DYNAMIC TABLE](desc-dynamic-table.md)
    and [SHOW DYNAMIC TABLES](show-dynamic-tables.md) commands. Determine which partial
    changes were applied, if any.

    If partial changes were applied, execute the appropriate ALTER DYNAMIC TABLE
    statements to transform the dynamic table back to its original statement.

For additional help, contact [Snowflake Support](../../user-guide/contacting-support.md).

## IMMUTABLE WHERE usage notes

* You can set only one IMMUTABLE WHERE predicate per dynamic table. Setting another predicate
  replaces the existing one.
* IMMUTABLE WHERE constraints can’t contain:

  * Subqueries
  * Nondeterministic functions (except timestamp functions like CURRENT_TIMESTAMP or
    CURRENT_DATE)
  * User-defined or external functions
  * Metadata columns (those starting with `METADATA$`)
  * Columns that result from aggregates, window functions, or nondeterministic functions
* When you use timestamp functions, the immutable region can’t shrink over time. For example,
  `TIMESTAMP_COL < CURRENT_TIMESTAMP()` is allowed, but
  `TIMESTAMP_COL > CURRENT_TIMESTAMP()` is not.
* Columns referenced in the IMMUTABLE WHERE condition must be columns in the dynamic table,
  not columns from the base table.
* The following limitations apply when you work with [immutability constraints](../../user-guide/dynamic-tables-immutability-constraints.md)
  and backfilled data:

  * Currently, only regular and dynamic tables can be used for backfilling.
  * You can’t specify policies or tags in the new dynamic table because they are copied from the backfill table.
  * Clustering keys in the new dynamic table and backfill table must be the same.

## Examples

Create a dynamic table named `my_dynamic_table`:

```sqlexample
CREATE OR REPLACE DYNAMIC TABLE my_dynamic_table
  TARGET_LAG = '20 minutes'
  WAREHOUSE = mywh
  AS
    SELECT product_id, product_name FROM staging_table;
```

In the example above:

* The dynamic table materializes the results of a query of the `product_id` and `product_name` columns of the
  `staging_table` table.
* The target lag time is 20 minutes, which means that the data in the dynamic table should ideally be no more than 20 minutes
  older than the data in `staging_table`.
* The automated refresh process uses the compute resources in warehouse `mywh` to refresh the data in the dynamic table.

Create a dynamic Iceberg table named `my_dynamic_table` that reads from `my_iceberg_table`:

```sqlexample
CREATE DYNAMIC ICEBERG TABLE my_dynamic_table (date TIMESTAMP_NTZ, id NUMBER, content STRING)
  TARGET_LAG = '20 minutes'
  WAREHOUSE = mywh
  EXTERNAL_VOLUME = 'my_external_volume'
  CATALOG = 'SNOWFLAKE'
  BASE_LOCATION = 'my_iceberg_table'
  AS
    SELECT product_id, product_name FROM staging_table;
```

Create a dynamic table with a multi-column clustering key:

```sqlexample
CREATE DYNAMIC TABLE my_dynamic_table (date TIMESTAMP_NTZ, id NUMBER, content VARIANT)
  TARGET_LAG = '20 minutes'
  WAREHOUSE = mywh
  CLUSTER BY (date, id)
  AS
    SELECT product_id, product_name FROM staging_table;
```

Clone a dynamic table as it existed exactly at the date and time of the specified timestamp:

```sqlexample
CREATE DYNAMIC TABLE my_cloned_dynamic_table CLONE my_dynamic_table AT (TIMESTAMP => TO_TIMESTAMP_TZ('04/05/2013 01:02:03', 'mm/dd/yyyy hh24:mi:ss'));
```

Configure a dynamic table to require a user for refreshes and then refresh the dynamic table:

```sqlexample
CREATE DYNAMIC TABLE my_dynamic_table
  TARGET_LAG = 'DOWNSTREAM'
  WAREHOUSE = mywh
  INITIALIZE = on_schedule
  REQUIRE USER
  AS
    SELECT product_id, product_name FROM staging_table;
```

```sqlexample
ALTER DYNAMIC TABLE my_dynamic_table REFRESH COPY SESSION;
```

Create a dynamic table with an immutability constraint:

```sqlexample
CREATE DYNAMIC TABLE my_dynamic_table
  TARGET_LAG = '1 hour'
  WAREHOUSE = my_warehouse
  IMMUTABLE WHERE (ts < CURRENT_TIMESTAMP() - INTERVAL '1 day')
AS
  SELECT * FROM source_table;
```

Create a dynamic table by using the CREATE OR ALTER DYNAMIC TABLE command:

```sqlexample
CREATE OR ALTER DYNAMIC TABLE my_dynamic_table
  TARGET_LAG = DOWNSTREAM
  WAREHOUSE = mywh
  AS
    SELECT a, b FROM t;
```

> **Note:**
>
> CREATE OR ALTER TABLE statements for existing tables can only be executed by a role with the OWNERSHIP privilege on `my_dynamic_table`.

Alter a dynamic table to set the DATA_RETENTION_TIME_IN_DAYS parameter and add a clustering key:

```sqlexample
CREATE OR ALTER DYNAMIC TABLE my_dynamic_table
 TARGET_LAG = DOWNSTREAM
 WAREHOUSE = mywh
 DATA_RETENTION_TIME_IN_DAYS = 2
 CLUSTER BY (a)
 AS
   SELECT a, b FROM t;
```

Modify the target lag and change the warehouse:

```sqlexample
CREATE OR ALTER DYNAMIC TABLE my_dynamic_table
 TARGET_LAG = '5 minutes'
 WAREHOUSE = my_other_wh
 DATA_RETENTION_TIME_IN_DAYS = 2
 CLUSTER BY (a)
 AS
   SELECT a, b FROM t;
```

Unset the DATA_RETENTION_TIME_IN_DAYS parameter. The absence of a parameter in the
modified CREATE OR ALTER DYNAMIC TABLE statement results in unsetting it. In this case,
unsetting the DATA_RETENTION_TIME_IN_DAYS parameter for the dynamic table resets it to
the default value of 1:

```sqlexample
CREATE OR ALTER DYNAMIC TABLE my_dynamic_table
 TARGET_LAG = '5 minutes'
 WAREHOUSE = my_other_wh
 CLUSTER BY (a)
 AS
   SELECT a, b FROM t;
```

**Write a v3 Snowflake-managed Iceberg table**

The following example writes a v3 Snowflake-managed Iceberg table as the output of a dynamic table:

```sqlexample
CREATE DYNAMIC ICEBERG TABLE my_dynamic_iceberg_v3_table (
    num_orders NUMBER(10,0),
    order_day
  )
  TARGET_LAG = '20 minutes'
  WAREHOUSE = my_warehouse
  EXTERNAL_VOLUME = 'my_external_volume'
  CATALOG = 'SNOWFLAKE'
  BASE_LOCATION = 'my_dynamic_iceberg_v3_table'
  ICEBERG_VERSION = 3
  AS
    SELECT
        COUNT(DISTINCT order_id)
        DATE_TRUNC('DAY', order_timestamp_ns) AS order_day
      FROM staging_v3_iceberg_table;
```

> **Note:**
>
> Writing either a v2 or v3 externally managed Iceberg table as the target of a dynamic table isn’t supported. The output of a dynamic
> Iceberg table can only be Snowflake-managed.
