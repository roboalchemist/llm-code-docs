# Source: https://docs.snowflake.com/en/user-guide/dynamic-tables-cost.md

# Understanding costs for dynamic tables

This topic provides an overview of the compute and storage costs associated with dynamic tables. For
general information about Snowflake costs, see [Understanding overall cost](cost-understanding-overall.md).

## Compute costs

There are two compute costs associated with dynamic tables: virtual warehouses and Cloud Services compute.

Dynamic tables require at least one [virtual warehouse](cost-understanding-compute.md) to perform [refreshes](dynamic-tables-refresh.md).
You can optionally assign a second warehouse if you want to separate compute costs for different operations. For more information, see
[Understand warehouse usage for dynamic tables](dynamic-tables-warehouses.md).

Dynamic table refreshes consume [compute credits](cost-understanding-compute.md), and their frequency is determined by the configured
[target lag](dynamic-tables-target-lag.md): lower target lag values trigger more frequent refreshes and therefore higher
compute costs.

Dynamic tables also require [Cloud Services compute](cost-understanding-compute.md) to identify changes in underlying base objects
and determine whether a virtual warehouse must run. If Cloud Services compute finds no changes, no warehouse compute credits are consumed
because there’s no new data to refresh. If changes do exist, even if the dynamic table query filters them, the virtual warehouse consumes
credits because the dynamic table refreshes to evaluate whether those changes apply.

If the associated virtual warehouses are suspended and Cloud Services compute detects no changes in the base tables, the warehouses remain
suspended and the dynamic tables don’t consume any credits. When Cloud Services compute identifies changes in the base tables, the appropriate
warehouse automatically resumes. If the changes support incremental refresh, the dynamic table refreshes by using the WAREHOUSE parameter. If
reinitialization is required — for example, because of a base table schema change — the dynamic table uses the INITIALIZATION_WAREHOUSE to
perform a full reinitialization. For information on how dynamic tables automatically suspend, see [Automatic dynamic table suspension](dynamic-tables-suspend-resume.md).

### Check your consumption of virtual warehouse credits

To check whether your dynamic table refreshes consumed virtual warehouse credits, use the Refresh History tab in Snowsight:

1. In the navigation menu, select Transformation » Dynamic tables.
2. Select your dynamic table, and then select the Refresh History tab.
3. To view refreshes that used the warehouse to update, select the Warehouse used only checkbox.

> **Tip:**
>
> To better understand costs related to your dynamic table pipelines, Snowflake recommends that you test dynamic tables by using dedicated
> warehouses. This way, you can isolate the virtual warehouse consumption that is attributed to dynamic tables. You can move your dynamic
> tables to a shared warehouse after you establish a cost baseline.

For more information, see [Understand warehouse usage for dynamic tables](dynamic-tables-warehouses.md).

### Compute cost for immutability constraints

If you use the IMMUTABLE WHERE constraint, Snowflake recomputes only the rows that don’t match the immutability condition, which helps reduce
reinitialization costs. This is useful in situations where reinitialization can occur, such as the following scenarios:

* Recreating upstream tables or views.
* Changes in upstream data governance policies.
* Failover to a secondary region in a failover group.

Using the IMMUTABLE WHERE constraint can help you reduce the cost of incremental and full refresh because the constraint ignores changes and
data that match its predicate.

Adding immutability constraints to a dynamic table doesn’t trigger extra computation, but removing them does because it causes
[reinitialization](dynamic-tables-refresh.md) on the next refresh. Modifying the predicate in an IMMUTABLE WHERE constraint
might trigger reinitialization depending on whether Snowflake can determine the rows that are returned with the original condition are still
returned with the new condition.

For example, the following modifications don’t trigger reinitialization:

* From `(ts < CURRENT_TIMESTAMP() - INTERVAL '2 days')` to `(ts < CURRENT_TIMESTAMP() - INTERVAL '1 days')`
* From `(year <= 2023)` to `(year <= 2024)`

The following modifications trigger reinitialization:

* From `(ts < '2025-01-02')` to `(ts < '2025-01-01')`
* From `(year < 2024)` to `(month < 10)`

## Storage cost

Dynamic tables require storage to store the materialized results. Similar to regular tables, you might incur additional storage cost for Time
Travel, fail-safe storage, and cloning features.

[Dynamic Apache Iceberg™ tables](dynamic-tables-create-iceberg.md) don’t incur Snowflake storage costs. For more information,
see [Billing](tables-iceberg.md).

This section discusses the following storage considerations for dynamic tables:

* Time Travel and fail-safe storage
* Replication of dynamic tables
* Suspended dynamic tables
* Transient dynamic tables
* Additional storage for incremental refresh operations

For detailed information about how this storage incurs cost, see [Understanding storage cost](cost-understanding-data-storage.md)
and [Data storage considerations](tables-storage-considerations.md).

### Time Travel and fail-safe storage

With Snowflake Time Travel, you can access and query historical versions of dynamic tables at specific points in time, which can help provide
insights into historical trends, changes, and anomalies in your data.

Frequent refreshes can increase buildup of Time Travel data, which adds to your overall storage usage. For more information, see
[Understanding & using Time Travel](data-time-travel.md).

Fail-safe features help protect your dynamic tables from data loss or corruption. Based on the configured fail-safe period, additional storage
charges might apply.

### Replication of dynamic tables

Dynamic tables support cross-account, cross-region replication, which lets you copy data from a primary database to a secondary database for
either disaster recovery or data sharing. It can serve as either a failover preparation strategy for disaster recovery or as a means of
sharing data across deployments for read-only purposes. Using replication with dynamic tables is subject to
[replication costs](account-replication-cost.md). For more information, see [Replication and dynamic tables](account-replication-considerations.md).

### Suspended dynamic tables

Suspended dynamic tables don’t incur additional costs beyond standard storage fees and don’t consume compute resources. If you have ongoing
maintenance tasks or scheduled jobs that interact with the suspended table, your dynamic tables might consume compute resources.

### Transient dynamic tables

Snowflake supports [transient](tables-temp-transient.md) dynamic tables, similar to regular tables, that persist until
explicitly dropped, and are available to all users with the appropriate privileges without a fail-safe period. Transient dynamic tables are
best used for transitory data that doesn’t need the same level of data protection and recovery that permanent tables provide. Using them
helps you save on storage charges for fail-safe storage.

### Additional storage for incremental refresh operations

For incremental refresh operations, dynamic tables maintain an additional internal metadata column for identifying each row within the table.
Internal row identifiers consume a constant amount of storage per row and increase storage cost linearly to the number of rows in the table,
independent of the number of columns.

For tables with very few columns, the increase in storage compared to an equivalent [CTAS](../sql-reference/sql/create-table.md) table can be significant,
or even dominant. In wider dynamic tables, this effect is less pronounced.

## Refresh schedule cost

The schedule at which a dynamic table refreshes, whether [full or incremental](dynamic-tables-refresh.md), has an effect
on its overall cost. This section discusses the factors that you should consider when you decide on a refresh schedule, with the assumption
that every refresh is non-empty:

* Full refresh schedule
* Incremental refresh schedule

> **Note:**
>
> Refreshes are relatively inexpensive if the sources haven’t changed. For more information, see Compute costs (in this topic).

### Full refresh schedule

The cost of a full refresh typically depends on how much data your dynamic table scans and how often it refreshes. To save on costs, you can
refresh your dynamic tables only when you need to; for example, you can suspend your dynamic tables outside of business hours. For precise
timing control, set the [downstream target lag](dynamic-tables-target-lag.md) for your dynamic tables and use
[manual refresh](../sql-reference/sql/alter-dynamic-table.md) from a [task](tasks-intro.md) to automate your custom schedules.

### Incremental refresh schedule

The cost of an incremental refresh is typically proportional to the volume of changes in the source objects, plus some fixed overhead.

If the overhead is low, you can set a high refresh frequency without much downside. This means that you can refresh often for best results.
For instance, a simple `SELECT ... FROM ... WHERE` dynamic table only processes changed rows between refreshes, which has minimal
overhead and the dynamic table can run frequently at low added cost.

If the overhead is high, you must balance the credit consumption of high refresh frequency with the business benefits of freshness. For
example, in a dynamic table with a join, you must join the changes in one table with the other table. No matter how small the set of changes,
this join usually involves a minimum cost for you to execute. If this overhead is significant, it can accumulate as the refresh frequency
increases.

To reduce overhead and optimize incremental refresh performance, see
[Optimize queries for incremental refresh](dynamic-tables-performance-optimize-query.md).
