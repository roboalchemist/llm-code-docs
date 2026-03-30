# Source: https://docs.snowflake.com/en/user-guide/dynamic-tables-performance-optimize.md

# Optimize dynamic table performance

This topic covers techniques for optimizing dynamic table performance, organized into
design changes and adjustments.

Before you optimize a dynamic table, you might want to diagnose the cause of slow refreshes. See
[Diagnose slow refreshes](dynamic-tables-performance-monitor.md) for a step-by-step workflow.

For background on performance categories, see
[Performance decisions](dynamic-tables-performance.md).

## Design changes

Design changes require you to recreate a dynamic table, but have greater impact on performance.

> **Note:**
>
> We recommend that you group changes and recreate tables together instead of making incremental modifications.

### Choose a refresh mode

The refresh mode you choose has a significant impact on performance because it determines
how much data Snowflake processes during each refresh. For information about how each mode
works, see [Dynamic table refresh modes](dynamic-tables-refresh.md).

> **Important:**
>
> Dynamic tables with incremental refresh can’t be downstream from dynamic tables that use
> full refresh.

Use the following decision process to select a refresh mode:

1. Review your query against the list of [supported query constructs](dynamic-tables-supported-queries.md).
   Not all query operators support incremental refresh. For operators that *are* supported,
   see [Optimize queries for incremental refresh](dynamic-tables-performance-optimize-query.md) to understand how
   they affect performance.
2. Estimate your change volume, which is the percentage of your data that changes between
   refreshes. Incremental refresh, for example, works best when less than five percent of data changes.
3. Evaluate your data locality. Check whether your source tables are clustered by the keys
   that you plan to use in joins, GROUP BY, or PARTITION BY clauses in your dynamic table query.
   Poor locality reduces incremental refresh efficiency. To improve locality,
   see Improve data locality.
4. Choose a mode based on the following table:

   | Mode | When to use |
   | --- | --- |
   | **Incremental** | Your query uses supported operators, less than five percent of data changes between refreshes, and your source tables have good data locality.  **Note:** Incremental refresh can still scan source tables, not just the rows that changed. For example, a new row in one side of a join must match against all rows in the other table. Even a small number of changes can trigger significant work. |
   | **Full** | A large percentage of data changes, your query uses unsupported operators, or your data lacks locality. |
   | **Auto** | You’re prototyping or testing. Avoid AUTO in production because its behavior might change between Snowflake releases. |

5. When you create a dynamic table, specify the mode with `REFRESH_MODE = INCREMENTAL` or
   `REFRESH_MODE = FULL` in your CREATE DYNAMIC TABLE statement.

To check which refresh mode a dynamic table uses, see [Refresh mode](dynamic-tables-performance-monitor.md).

### Optimize your queries and pipeline

The structure of your dynamic table queries and pipeline directly affects refresh performance. Use the
following guidelines to reduce the work during each refresh.

#### Simplify individual queries

* Use inner joins instead of outer joins. Inner joins perform better with incremental
  refresh. Verify referential integrity in your source data so that you can avoid outer joins.
* Avoid unnecessary operations. Remove redundant DISTINCT clauses and unused columns.
  Exclude wide columns (like large JSON blobs) that aren’t frequently queried.
* Remove duplicates efficiently. Use ranking functions instead of DISTINCT where possible.

For detailed guidance on how specific SQL operators affect incremental refresh performance,
see [Optimize queries for incremental refresh](dynamic-tables-performance-optimize-query.md).

> **Note:**
>
> For a comprehensive example, see [Tutorial: Optimize dynamic table performance for SCD Type 1 workloads](tutorials/optimize-dynamic-table-performance.md).

#### Split transformations across dynamic tables

Breaking complex transformations into multiple dynamic tables makes it easier to identify
bottlenecks and improves debugging. With immutability constraints,
you can also use different refresh modes for different stages.

* Add filters early. Apply `WHERE` clauses in the dynamic tables closest to your source
  data so that downstream tables process fewer rows.
* To avoid repeated `DISTINCT` operations in downstream tables, remove duplicate rows earlier in your pipeline.
* Reduce the number of operations per table. Move joins, aggregations, or window functions
  into intermediate dynamic tables instead of combining them all in one query.
* Materialize compound expressions (like `DATE_TRUNC('minute', ts)`) in an intermediate
  table before grouping by them. For details, see [Optimize aggregations](dynamic-tables-performance-optimize-query.md).

> **Note:**
>
> Finding optimal split points requires trial and error.
>
> Consider splitting between operations
> that shuffle data on different keys, such as `GROUP BY`, `DISTINCT`, window functions
> with `PARTITION BY`, and joins. This lets each dynamic table maintain better data
> locality for its key operation. For operator-specific guidance, see
> [Optimize queries for incremental refresh](dynamic-tables-performance-optimize-query.md).

The following example shows how to split a complex query into intermediate dynamic tables.

Initial complex query:

```sqlexample
CREATE DYNAMIC TABLE final_result
  TARGET_LAG = '1 hour'
  WAREHOUSE = my_warehouse
AS
  SELECT ...
  FROM large_table a
  JOIN dimension_table b ON ...
  JOIN another_table c ON ...
  GROUP BY ...;
```

Split the complex pipeline by adding an intermediate dynamic table:

```sqlexample
CREATE DYNAMIC TABLE intermediate_joined
  TARGET_LAG = DOWNSTREAM
  WAREHOUSE = my_warehouse
AS
  SELECT ...
  FROM large_table a
  JOIN dimension_table b ON ...;

CREATE DYNAMIC TABLE final_result
  TARGET_LAG = '1 hour'
  WAREHOUSE = my_warehouse
AS
  SELECT ...
  FROM intermediate_joined
  JOIN another_table c ON ...
  GROUP BY ...;
```

For detailed information and examples of how operators affect performance, see
[Optimize queries for incremental refresh](dynamic-tables-performance-optimize-query.md).

### Mark historical data immutable

Use the `IMMUTABLE WHERE` clause to tell Snowflake that certain rows won’t change. This
reduces the scope of work during each refresh.

For syntax, examples, and detailed guidance, see
[Use immutability constraints](dynamic-tables-performance-optimize-immutability.md).

## Adjustments

Adjustments don’t require you to recreate dynamic tables. You can make adjustments while your pipeline is running.

### Adjust your warehouse configuration

The warehouse that you specify in your CREATE DYNAMIC TABLE statement runs all refreshes for that
table. Warehouse size and configuration directly affect refresh duration and cost.

For more information about warehouses and dynamic tables, see [Understand warehouse usage for dynamic tables](dynamic-tables-warehouses.md).
For general warehouse performance optimization strategies, see [Optimizing warehouses for performance](performance-query-warehouse.md).

#### Use a separate warehouse for initialization

Initial refreshes often process significantly more data than incremental refreshes. Use
INITIALIZATION_WAREHOUSE to run initializations on a larger warehouse. Reserve a
smaller, more cost-effective warehouse for regular refreshes:

```sqlexample
CREATE DYNAMIC TABLE my_dynamic_table
  TARGET_LAG = 'DOWNSTREAM'
  WAREHOUSE = 'XS_WAREHOUSE'
  INITIALIZATION_WAREHOUSE = '4XL_WAREHOUSE'
  AS <query>;
```

To add or change the initialization warehouse for an existing dynamic table:

```sqlexample
ALTER DYNAMIC TABLE my_dynamic_table SET INITIALIZATION_WAREHOUSE = '4XL_WAREHOUSE';
```

To remove the initialization warehouse and use the primary warehouse for all refreshes:

```sqlexample
ALTER DYNAMIC TABLE my_dynamic_table UNSET INITIALIZATION_WAREHOUSE;
```

To view the warehouse configuration, use [SHOW DYNAMIC TABLES](../sql-reference/sql/show-dynamic-tables.md) or
check the [DYNAMIC_TABLE_REFRESH_HISTORY](../sql-reference/functions/dynamic_table_refresh_history.md)
table function.

#### Resize when needed

To balance cost and performance, choose a warehouse size that prevents bytes from being spilled but doesn’t
exceed what your workload can use in parallel. When faster refreshes are critical, increase the
size slightly beyond the cost-optimal point.

Considerations for dynamic table refreshes:

* **Bytes spilled**: When query history shows bytes spilled to local or remote storage, the warehouse
  ran out of memory during refresh. A larger warehouse provides more memory to prevent spilling.
  For details, see [Queries too large to fit in memory](performance-query-warehouse-memory.md).
* **Slow initial refresh**: When the initial refresh is slow, consider setting INITIALIZATION_WAREHOUSE
  for the initial creation, or temporarily resize the warehouse and then resize it down after the table
  is created.
* **Saturated parallelism**: Beyond a certain point, additional parallelism provides diminishing
  returns. Doubling warehouse size might double cost without halving runtime. To check how your
  refresh uses parallelism, review the [query profile](dynamic-tables-performance-monitor.md).

To resize a warehouse, see [Increasing warehouse size](performance-query-warehouse-size.md).

For cost considerations, see [Virtual warehouse credit usage](cost-understanding-compute.md) and
[Working with warehouses](warehouses-tasks.md).

#### Handle concurrent refreshes with multi-cluster warehouses

If multiple dynamic tables share a warehouse and refreshes frequently queue, consider using a
[multi-cluster warehouse](warehouses-multicluster.md). Multi-cluster warehouses
automatically add clusters when queries queue and remove them when demand drops. This improves
refresh latency during peak periods without paying for unused capacity during quiet periods.

For guidance on identifying and reducing queues, see [Reducing queues](performance-query-warehouse-queue.md).

Multi-cluster warehouses require Enterprise Edition or higher. For cost considerations, see
[Setting the scaling policy for a multi-cluster warehouse](warehouses-multicluster.md).

### Identify the right target lag

Target lag controls how often your dynamic table refreshes. Shorter target lag means fresher
data but more frequent refreshes and higher compute cost. For more information about how target lag works,
see [Understanding dynamic table target lag](dynamic-tables-target-lag.md).

Use the following recommendations to optimize target lag for your workload:

* **Use DOWNSTREAM for intermediate tables** that don’t need independent freshness guarantees.
  These tables refresh only when downstream tables need them.
* **Check the refresh history to find the right lag**: Use
  [DYNAMIC_TABLE_REFRESH_HISTORY](../sql-reference/functions/dynamic_table_refresh_history.md) or [Snowsight](ui-snowsight-gs.md) to
  analyze refresh durations and skipped refreshes. Set the target lag slightly higher than your
  typical refresh duration.

#### Change target lag

```sqlexample
ALTER DYNAMIC TABLE my_dynamic_table SET TARGET_LAG = '1 hour';
```

To set a dynamic table to refresh based on downstream demand:

```sqlexample
ALTER DYNAMIC TABLE my_dynamic_table SET TARGET_LAG = DOWNSTREAM;
```

### Improve data locality

*Locality* describes how closely Snowflake stores rows that share the same key values. When
rows with matching keys span fewer micro-partitions (good locality), incremental refreshes scan
less data. When matching keys span many micro-partitions (poor locality), incremental refresh
can take longer than full refresh.

For more information about how Snowflake stores data, see
[Micro-partitions & Data Clustering](tables-clustering-micropartitions.md).

#### Cluster source tables

The most effective way to improve locality is to cluster your source tables by the keys used in
your dynamic table query (JOIN, GROUP BY, or PARTITION BY keys):

```sqlexample
ALTER TABLE my_source_table CLUSTER BY (join_key_column);
```

When you join on multiple columns and can’t cluster by all of them:

* Prioritize clustering larger tables by the most selective keys.
* Consider creating separate copies of the same data clustered by different keys for use in
  different dynamic tables.

For more information, see [Clustering Keys & Clustered Tables](tables-clustering-keys.md). To enable automatic
reclustering, see [Automatic Clustering](tables-auto-reclustering.md).

#### Factors that affect locality

Beyond source table clustering, two other factors affect locality. These depend on your data
patterns and are harder to change directly:

* **How new data aligns with partition keys**: Incremental refresh is faster when new rows
  affect only a small portion of the table. This depends on your data ingestion patterns, not
  your query structure.

  For example, time-series data grouped by hour has good locality because
  new rows share recent timestamps. Data grouped by a column with values spread across the
  entire table has poor locality.
* **How changes align with dynamic table clustering**: When Snowflake applies updates or
  deletions to a dynamic table, it must locate the affected rows. This is faster when the changed rows are stored
  close together.

  For example, updates to recent rows perform well when the dynamic table is
  naturally ordered by time. Updates scattered across the entire table are slower. This factor
  depends on your workload patterns, including which rows change and how often.

When you experience poor locality because of these factors, consider whether you can adjust your data model or
ingestion patterns upstream.
