# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-database-catalog-linked.md

# ALTER DATABASE (catalog-linked)

Modifies the properties for an existing [catalog-linked database](../../user-guide/tables-iceberg-catalog-linked-database.md).

Database modifications include the following actions:

* Enabling or turning off automatic discovery.
* Changing the allowed and blocked namespaces.
* Changing the time interval that Snowflake should use for automatically discovering schemas and tables in your remote catalog.
* Changing whether your remote catalog is read only or writable.

## Syntax

```sqlsyntax
ALTER DATABASE [ IF EXISTS ] <name> RENAME TO <new_name>

ALTER DATABASE [ IF EXISTS ] <name> SUSPEND DISCOVERY

ALTER DATABASE [ IF EXISTS ] <name> RESUME DISCOVERY

ALTER DATABASE [ IF EXISTS ] <name> UPDATE LINKED_CATALOG
  ADD ( '<namespace>' [ , ... ] ) TO ALLOWED_NAMESPACES

ALTER DATABASE [ IF EXISTS ] <name> UPDATE LINKED_CATALOG
  REMOVE ( '<namespace>' [ , ... ] ) FROM ALLOWED_NAMESPACES

ALTER DATABASE [ IF EXISTS ] <name> UPDATE LINKED_CATALOG
  UNSET ALLOWED_NAMESPACES

ALTER DATABASE [ IF EXISTS ] <name> UPDATE LINKED_CATALOG
  ADD ( '<namespace>' [ , ... ] ) TO BLOCKED_NAMESPACES

ALTER DATABASE [ IF EXISTS ] <name> UPDATE LINKED_CATALOG
  REMOVE ( '<namespace>' [ , ... ] ) FROM BLOCKED_NAMESPACES

ALTER DATABASE [ IF EXISTS ] <name> UPDATE LINKED_CATALOG
  UNSET BLOCKED_NAMESPACES

ALTER DATABASE [ IF EXISTS ] <name> UPDATE LINKED_CATALOG
  SET SYNC_INTERVAL_SECONDS = <value>

ALTER DATABASE [ IF EXISTS ] <name> UPDATE LINKED_CATALOG
  SET ALLOWED_WRITE_OPERATIONS = { NONE | ALL }

ALTER DATABASE [ IF EXISTS ] <name> SET [ BASE_LOCATION_PREFIX = '<string>' ]
                                        [ COMMENT = '<string_literal>' ]
                                        [ CONTACT <purpose> = <contact_name> [ , <purpose> = <contact_name> ... ] ]
                                        [ ICEBERG_VERSION_DEFAULT = <integer> ]
                                        [ ENABLE_ICEBERG_MERGE_ON_READ = { TRUE | FALSE } ]

ALTER DATABASE [ IF EXISTS ] <name> UNSET { BASE_LOCATION_PREFIX         |
                                            COMMENT                      |
                                            CONTACT                      |
                                            ICEBERG_VERSION_DEFAULT      |
                                            ENABLE_ICEBERG_MERGE_ON_READ
                                          }
```

## Parameters

`name`
:   Specifies the identifier for the catalog-linked database to alter.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`RENAME TO new_name`
:   Changes the name of the catalog-linked database to `new_name`. The new identifier must be unique for the account.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

    When an object is renamed, other objects that reference it must be updated with the new name.

`SUSPEND DISCOVERY`
:   Suspends automatic discovery. You might want to suspend automatic discovery to prevent consuming unnecessary credits or
    resources if an underlying issue is preventing Snowflake from discovering the tables in your remote catalog. For example,
    you might want to suspend automatic discovery because there is an underlying issue with missing permissions or a misconfiguration.
    After you resolve the issue, run ALTER DATABASE … RESUME DISCOVERY to resume discovery.

    To confirm that automatic discovery is suspended, call the [SYSTEM$CATALOG_LINK_STATUS](../functions/system_catalog_link_status.md) function and
    verify that the `executionState` field is set to `SUSPENDED`. If you suspend automatic discovery but an automatic discovery task is
    currently running, the execution state won’t change to suspended until the task is complete.

    > **Note:**
    >
    > Suspending automatic discovery doesn’t turn off automated refresh. To turn off automated refresh for an existing
    > Iceberg table, see [Enable or turn off automated refresh](../../user-guide/tables-iceberg-auto-refresh.md).

`RESUME DISCOVERY`
:   Resumes automatic discovery. You might want to resume discovery for the following reasons:

    * You suspended discovery to resolve an issue and now you’re ready to resume discovery.
    * You want to force an immediate discovery run to ensure that recent changes, such as fixed permissions, are picked up.

    To confirm that automatic discovery is resumed, call the [SYSTEM$CATALOG_LINK_STATUS](../functions/system_catalog_link_status.md) function, and then
    verify that the `executionState` field is set to `RUNNING`.

`UPDATE LINKED_CATALOG`
:   Updates the properties that apply to catalog-linked databases. You can set the following properties:

    `ADD ( 'namespace1' [ , 'namespace2' ,  ... ] ) TO ALLOWED_NAMESPACES`
    :   Specifies one or more namespaces in your remote catalog to limit the scope of automatic discovery. Snowflake syncs the specified
        namespaces and all namespaces and tables that are nested under them.

        * If you created a catalog-linked database with an empty ALLOWED_NAMESPACES list, Snowflake syncs *all* of the namespaces and tables from the
          remote catalog.

          If you later alter the database by specifying the ALLOWED_NAMESPACES parameter to only allow a specific list of namespaces,
          Snowflake updates the catalog-linked database to only retain those namespaces you allow. All the other namespaces and tables are
          dropped from the catalog-linked database.
        * If you created a catalog-linked database with a list of ALLOWED_NAMESPACES, Snowflake only creates those allowed namespaces in
          the catalog-linked database.

          If you later alter the database to add namespaces to the ALLOWED_NAMESPACES list, Snowflake only creates the
          newly added namespaces and retains the existing allowed namespaces. If you remove namespaces from the ALLOWED_NAMESPACES list,
          Snowflake only drops the newly removed namespaces from the catalog-linked database and retains all of the remaining allowed namespaces.

        If a nested namespace is in the ALLOWED_NAMESPACES list but you set the
        NAMESPACE_MODE parameter to IGNORE_NESTED_NAMESPACE, Snowflake doesn’t sync the nested namespace or any schemas and tables under it.

    `REMOVE ( 'namespace1' [ , 'namespace2' ,  ... ] ) FROM ALLOWED_NAMESPACES`
    :   Specifies one or more namespaces in your remote catalog to remove from your list of allowed namespaces.

    `UNSET ALLOWED_NAMESPACES`
    :   Unsets your list of allowed namespaces to the default, which is all namespaces are allowed.

    `ADD ( 'namespace1' [ , 'namespace2' ,  ... ] ) TO BLOCKED_NAMESPACES`
    :   Specifies one or more namespaces in your remote catalog to block for automatic discovery.

        Snowflake blocks the specified namespaces and all namespaces and tables that are nested under them.

        If you specify both ALLOWED_NAMESPACES and BLOCKED_NAMESPACES, the BLOCKED_NAMESPACES list takes precedence.
        For example, if `ns1.ns2` is allowed, but `ns1` is blocked, then Snowflake won’t sync `ns1.ns2`.

    `REMOVE ( 'namespace1' [ , 'namespace2' ,  ... ] ) FROM BLOCKED_NAMESPACES`
    :   Specifies one or more namespaces in your remote catalog to remove from your list of blocked namespaces.

    `UNSET BLOCKED_NAMESPACES`
    :   Unsets your list of blocked namespaces to the default, which is zero namespaces are blocked.

    `SET SYNC_INTERVAL_SECONDS = value`
    :   Specifies the time interval in seconds that Snowflake should use for automatically discovering schemas and tables in your remote catalog.
        You can reduce your credit consumption by setting a longer time interval.

        Values: 30 to 86400 (1 day), inclusive

        Default: 30 seconds

    `SET ALLOWED_WRITE_OPERATIONS = { NONE | ALL }`
    :   Specifies whether your catalog-linked database is read-only or writable.

        * `NONE`: Your catalog-linked database is read-only.

          When your catalog-linked database is read only, any operation that you run that requires committing to the catalog fails. For
          example, DROP ICEBERG TABLE.
        * `ALL`: Your catalog-linked database is writable.

          > **Warning:**
          >
          > When your catalog-linked database has write permissions enabled, Snowflake propagates table drops to the remote catalog, which removes
          > the table and data from both systems.

        Default: `ALL`

`SET ...`
:   Specifies one or more properties or parameters to set for the catalog-linked database, separated by blank spaces, commas, or new lines:

    `BASE_LOCATION_PREFIX = 'string'`
    :   Specifies a prefix for Snowflake to use in the write path for externally managed Apache Iceberg™ tables.
        For more information,
        see [Data and metadata directories for Iceberg tables](../../user-guide/tables-iceberg-storage.md) and
        [BASE_LOCATION_PREFIX](../parameters.md).

        Default: No value

    `COMMENT = 'string_literal'`
    :   Adds a comment or overwrites an existing comment for the catalog-linked database.

    `CONTACT purpose = contact [ , purpose = contact ... ]`
    :   Associate the existing object with one or more [contacts](../../user-guide/contacts-using.md).

        You cannot set the CONTACT property with other properties in the same statement.

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

`UNSET ...`
:   Specifies one or more properties or parameters to unset for the database, which resets them to the defaults:

    * `BASE_LOCATION_PREFIX`
    * `COMMENT`
    * `CONTACT`
    * `ICEBERG_VERSION_DEFAULT`
    * `ENABLE_ICEBERG_MERGE_ON_READ`

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | The catalog-linked database being modified. | Required to suspend or resume automatic table discovery. |
| OWNERSHIP or MODIFY | The catalog-linked database being modified. | Required for all other operations. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Examples

Reset the list of allowed namespaces for a catalog-linked database named `my_linked_db` to the default.

```sqlexample
ALTER DATABASE IF EXISTS my_linked_db UPDATE LINKED_CATALOG
  UNSET ALLOWED_NAMESPACES;
```

Add `my_namespace` to the list of allowed namespaces for a catalog-linked database named `my_linked_db`.

```sqlexample
ALTER DATABASE IF EXISTS my_linked_db UPDATE LINKED_CATALOG
 ADD ('my_namespace') TO ALLOWED_NAMESPACES;
```
