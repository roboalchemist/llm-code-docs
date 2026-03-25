# Source: https://docs.snowflake.com/en/user-guide/tables-clustering-manual.md

# Manual Reclustering — *Deprecated*

If manual reclustering is still available in your account, you can use the [ALTER TABLE](../sql-reference/sql/alter-table.md) command with a `RECLUSTER` clause to manually recluster
a clustered table at any time.

## What is Manual Reclustering?

The `RECLUSTER` clause instructs Snowflake to perform immediate reclustering of the specified table. Unlike Automatic Clustering, this DML operation requires a virtual
warehouse in your account and locks the table for the duration of the operation.

Also, after a period of significant/sustained DML activity on a clustered table that does not have Automatic Clustering enabled, manual reclustering may need to be performed
multiple times on the table to achieve the desired results.

For these reasons, as well as other benefits, we recommend using [Automatic Clustering](tables-auto-reclustering.md) instead of manual reclustering.

> **Tip:**
>
> As a general rule of thumb and best practice, we recommend manual reclustering after performing significant DML on a clustered table. You can use the
> [clustering information](../sql-reference/functions/system_clustering_information.md) for the table to measure whether clustering on the table has degraded due to DML.

## Performance Impact of Manual Reclustering

The grouping/sorting that Snowflake performs during manual reclustering can impact the performance of the virtual warehouse used to perform the reclustering.

Due to this impact, if you chose to perform manual reclustering, we recommend using a separate, dedicated warehouse, and ensuring that the warehouse is of sufficient size.

## Switching from Manual Reclustering to Automatic Clustering

If manual reclustering is still available in your account, [Automatic Clustering](tables-auto-reclustering.md) may not be enabled yet for your account.

You can request Automatic Clustering to be enabled for your account; however, it will only affect clustered tables that are defined from the time after the feature is
enabled.

For clustered tables that were defined before the feature is enabled, you must explicitly “resume” Automatic Clustering for each table. You can use SQL to determine whether
Automatic Clustering is enabled for a given table.

For more details, see:

* [Viewing the Automatic Clustering status for a table](tables-auto-reclustering.md).
* [Resuming Automatic Clustering for a table](tables-auto-reclustering.md).

## Manually Reclustering a Table

Use [ALTER TABLE](../sql-reference/sql/alter-table.md) with a `RECLUSTER` clause to manually recluster a table for which a clustering key have been defined. You can use a `WHERE`
clause to specify a condition or range on which to recluster data in the table.

For example:

* To recluster table `t1`:

  > ```sqlexample
  > ALTER TABLE t1 RECLUSTER;
  > ```
>
* To recluster data that was inserted into table `t1` in the first week of 2016:

  > ```sqlexample
  > ALTER TABLE t2 RECLUSTER WHERE CREATE_DATE BETWEEN ('2016-01-01') AND ('2016-01-07');
  > ```

These examples use the current warehouse (for the session) to recluster the table. The amount of resources allocated to manual reclustering is based on the size of the warehouse.
The larger the warehouse, the more resources are allocated to the recluster command, which results in more effective reclustering.

> **Note:**
>
> Manual reclustering can only be performed on clustered tables (i.e. tables that have a clustering key defined).
