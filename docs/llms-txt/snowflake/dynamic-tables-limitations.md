# Source: https://docs.snowflake.com/en/user-guide/dynamic-tables-limitations.md

# Dynamic table limitations

This topic describes general and cross-feature limitations on dynamic tables.

## General limitations

The following general limitations apply to using dynamic tables:

* A single account can hold a maximum of 50,000 dynamic tables.
* You can’t truncate data from a dynamic table.
* You can’t create a temporary dynamic table.
* When you use a dynamic table to [ingest shared data](dynamic-tables-data-sharing.md), the query can’t select from a shared
  dynamic table or a shared secure view that references an upstream dynamic table.
* You can’t use secondary roles with dynamic tables because dynamic table refreshes act as their owner role. For more information, see
  [Authorization through primary role and secondary roles](security-access-control-overview.md).
* You can’t use dynamic SQL (for example, session variables or unbound variables of anonymous blocks) in the dynamic table’s definition.
* In a dynamic table definition, SELECT blocks that read from user-defined table functions (UDTF) must explicitly specify columns and can’t
  use `*`.
* Dynamic tables can become stale if they are not refreshed within the [MAX_DATA_EXTENSION_TIME_IN_DAYS](../sql-reference/parameters.md) period of the input
  tables. Once stale, they must be recreated to resume refreshes.
* When creating a dynamic table that uses a warehouse named DEFAULT, you must use double quotes around the name, following the
  [double-quoted identifier requirements](../sql-reference/identifiers-syntax.md). For example, `CREATE DYNAMIC TABLE ... WAREHOUSE = "DEFAULT"`.
  For more information on creating dynamic tables, see [Create dynamic tables](dynamic-tables-create.md).
* Dynamic tables don’t support sources that include directory tables, external tables, streams, and materialized views.
* You can’t create dynamic tables that read from views that query other dynamic tables.
* You can’t clone dynamic Iceberg tables. Additionally, cloning a database or schema containing a dynamic Iceberg table does not clone the
  table to the new location.
* You can’t set the [DATA_RETENTION_TIME_IN_DAYS](../sql-reference/parameters.md) object parameter to zero if your base table is a shared table.

## Immutability constraints

The following limitations apply when you work with [immutability constraints](dynamic-tables-immutability-constraints.md)
and backfilled data:

* Currently, only regular and dynamic tables can be used for backfilling.
* You can’t specify policies or tags in the new dynamic table because they are copied from the backfill table.
* Clustering keys in the new dynamic table and backfill table must be the same.

## Support for cross-feature interactions

The following cross-feature interactions are not supported:

* Using the query acceleration service (QAS) for dynamic table refreshes.
* Masking policies with database roles on shared tables.
* Aggregation and projection policies cannot be applied to the base tables of dynamic tables. If a base table has aggregation or projection
  policies associated with it, the dynamic table will fail to create.

## Support for incremental refresh

Dynamic tables support two refresh modes: incremental and full. You can either set the refresh mode to AUTO or set it explicitly. For more
information, see [Dynamic table refresh modes](dynamic-tables-refresh.md) and [Choose a refresh mode](dynamic-tables-performance-optimize.md).

### Masking and row access policies

Masking or row access policies on a dynamic table don’t affect its refresh mode. However, policies applied on base tables might affect the
refresh mode:

> * Incremental refresh is supported if the policies on base tables use the [CURRENT_ROLE](../sql-reference/functions/current_role.md) or
>   [IS_ROLE_IN_SESSION](../sql-reference/functions/is_role_in_session.md) function.
> * Incremental refresh isn’t supported if the policies on base tables use any other functions, INFORMATION_SCHEMA views, or query a table
>   (for example, a [mapping table lookup](security-row-using.md)).
> * Changes to the policies on base objects of dynamic tables with incremental refresh trigger reinitialization.

### Replication

Replicated dynamic tables with incremental refresh reinitialize after failover before they can resume incremental refresh.

For more information, see [Replication and dynamic tables](account-replication-considerations.md).

### Cloning

[Cloned incremental dynamic tables](../sql-reference/sql/create-dynamic-table.md) might need to reinitialize during their first refresh after being
created.

If a dynamic table is cloned from another dynamic table with dropped base tables, the clone will be suspended and can’t be resumed or
refreshed.
