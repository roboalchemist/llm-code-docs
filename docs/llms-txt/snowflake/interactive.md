# Source: https://docs.snowflake.com/en/user-guide/interactive.md

# Snowflake interactive tables and interactive warehouses

This topic introduces Snowflake *interactive tables* and *interactive warehouses*. They deliver low-latency query performance for
high-concurrency, interactive workloads.

> **Note:**
>
> Interactive tables now support join queries.

## Overview of interactive warehouses and interactive tables

The following are the new kinds of Snowflake objects that you use with this feature.
When you run queries on interactive tables using interactive warehouses,
query performance is generally better than it would be with standard Snowflake tables.

Interactive warehouse
:   A specialized type of warehouse that’s optimized for low-latency, interactive workloads.

    An interactive warehouse tunes the Snowflake engine specially for low-latency, interactive workloads.
    It leverages additional metadata and index information in the underlying interactive tables to accelerate queries.
    This type of warehouse is optimized to run continuously, serving high volumes of concurrent queries.
    All interactive warehouses run on the latest generation of hardware.

Interactive table
:   A specialized type of Snowflake table that’s optimized for low-latency, interactive queries.

    You get the best performance gains when you query these tables through interactive warehouses.
    Interactive tables have different methods for data ingestion and support a more limited set of SQL
    statements and query operators than standard Snowflake tables.

## Use cases for interactive tables

Snowflake interactive tables are optimized for fast, simple queries when you require consistent
low-latency responses. Interactive warehouses provide the compute resources required to serve these
queries efficiently. Together, they enable use cases such as real-time dashboards, data-powered
APIs, and serving high-concurrency workloads.

The simple queries that work best with interactive tables are usually SELECT statements with
selective WHERE clauses, optionally including a GROUP BY clause on a few dimensions. Avoid queries
involving large joins and large subqueries. The performance of queries that use other features, such
as window functions, is highly dependent on the data shapes that you are querying.

## Region availability

Interactive tables and interactive warehouses are available in the following Amazon Web Services (AWS),
Google Cloud Platform (GCP), and Microsoft Azure regions. For more information about Snowflake regions,
see [Supported cloud regions](intro-regions.md).

* `us-east-1` - AWS US East (N. Virginia)
* `us-west-2` - AWS US West (Oregon)
* `us-east-2` - AWS US East (Ohio)
* `ca-central-1` - AWS Canada (Central)
* `ap-northeast-1` - AWS Asia Pacific (Tokyo)
* `ap-southeast-2` - AWS Asia Pacific (Sydney)
* `eu-central-1` - AWS EU (Frankfurt)
* `eu-west-1` - AWS EU (Ireland)
* `eu-west-2` - AWS Europe (London)
* `us-central1` - GCP US Central1 (Iowa)
* `us-east4` - GCP US East4 (N. Virginia)
* `europe-west2` - GCP Europe West2 (London)
* `europe-west3` - GCP Europe West3 (Frankfurt)
* `europe-west4` - GCP Europe West4 (Netherlands)
* `australia-southeast2` - GCP Australia Southeast2 (Melbourne)
* Azure: all Azure regions.

## Limitations of interactive warehouses and interactive tables

The following limitations apply to interactive warehouses and interactive tables. Some limitations
are due to architectural differences between interactive tables and standard Snowflake tables;
those limitations are intended to be permanent.

### Limitations of interactive warehouses

* Snowflake interactive warehouses don’t support long-running queries. The query timeout for SELECT
  commands defaults to five seconds. After five seconds, the query is canceled. You can reduce the
  query timeout value, but you can’t increase it. Other kinds of commands, such as SHOW and INSERT
  OVERWRITE, aren’t subject to the five-second timeout interval.

  If a query consistently times out, that’s a signal that it might not be suitable for use with
  interactive warehouses. Otherwise, you need to apply some of the performance tuning techniques to
  reduce the time to less than five seconds.
* Interactive warehouses support auto-suspend and auto-resume with a minimum auto-suspend interval
  of 24 hours (86400 seconds). Expect significant query latency when you resume an interactive
  warehouse, because the cache needs to warm up again. For more information, see
  Resuming and suspending an interactive warehouse.
* You can’t query standard Snowflake tables from an interactive warehouse. To query both standard
  tables and interactive tables in the same session, run [USE WAREHOUSE](../sql-reference/sql/use-warehouse.md)
  to switch to the appropriate warehouse type depending on the type of table.
* You can’t run [CALL commands](../sql-reference/sql/call.md) to call stored procedures in an interactive warehouse.
* You can’t use the `->>` [pipe operator](../sql-reference/operators-flow.md). That operator uses stored procedures behind the scenes.
* Interactive warehouses currently don’t support [replication](account-replication-intro.md). They aren’t included in failover
  groups and replication groups.

### Limitations of interactive tables

* Interactive tables don’t support the following features:

  * [Data manipulation language (DML) commands](../sql-reference/sql-dml.md) such as UPDATE and DELETE.
    The only DML that you can perform is INSERT OVERWRITE.
  * Fail-safe. This data recovery mechanism isn’t available for interactive tables. You can still
    use Time Travel with interactive tables.
  * [Row timestamps](data-engineering/row-timestamps.md). You can’t enable row timestamps on an interactive table.
  * [Query insights](query-insights.md). They currently aren’t collected or available for queries executing on
    interactive tables.
* You can’t perform the following operations:

  * Use an interactive table as the source for a standard (non-interactive) materialized view. To create a materialized view
    on an interactive table, use the INTERACTIVE keyword. See Materialized view support for interactive tables.
  * Modify properties of an interactive table by using
    [ALTER TABLE](../sql-reference/sql/alter-table.md) clauses such as ADD COLUMN or REMOVE COLUMN.
    ALTER TABLE operations that you **can** perform include:

    * Renaming the table.
    * Modifying columns to set or unset comments.
    * Setting or unsetting masking policies on columns.
    * Adding or unsetting a [masking policy](security-column-ddm-use.md),
      [join policy](join-policies.md), [aggregation policy](aggregation-policies.md),
      or [row access policy](security-row-intro.md) on the table.
    * Adding a [storage lifecycle policy](storage-management/storage-lifecycle-policies.md)
      to the table, or dropping a storage lifecycle policy from the table.
  * Use [streams](streams-intro.md) with an interactive table.
  * Create a [dynamic table](dynamic-tables-about.md) with an interactive table as a base table.
  * Use the [RESAMPLE clause](../sql-reference/constructs/resample.md) for queries on an interactive table.
  * Set the Time Travel retention period using CREATE INTERACTIVE TABLE or ALTER TABLE.
    Interactive tables inherit the DATA_RETENTION_TIME_IN_DAYS value from their parent
    schema, database, or account.

## Getting started with interactive tables

To get started with interactive tables, complete the following sequence of steps:

1. Create an interactive table, using a standard warehouse. For more information, see
   Creating an interactive table.
2. Create an interactive warehouse. For more information, see
   Creating an interactive warehouse.
3. Resume the interactive warehouse. For more information, see
   Resuming and suspending an interactive warehouse.
4. Add the interactive table to the interactive warehouse. For more information, see
   Adding an interactive table to an interactive warehouse.
5. Start querying the interactive table through the interactive warehouse. For more information, see
   Querying an interactive table.

## Working with interactive tables and interactive warehouses

The following procedures explain how to create and manage all the required
objects to run queries using interactive tables. When you are trying this
feature for the first time, perform these procedures in the following order.

### Creating an interactive table

Table creation follows the standard CTAS ([CREATE TABLE AS SELECT](../sql-reference/sql/create-table.md)) syntax,
with the additional INTERACTIVE keyword that defines the table type.

The CREATE INTERACTIVE TABLE command also requires a CLUSTER BY clause.
Specify one or more columns in the CLUSTER BY clause to match the WHERE clauses in your most time-critical queries.
The columns you specify in the CLUSTER BY clause can significantly affect the performance
of queries on the interactive table. Therefore, choose the clustering columns carefully.
For more information about choosing the best clustering columns, see [Clustering Keys & Clustered Tables](tables-clustering-keys.md).

> **Note:**
>
> You run the CREATE INTERACTIVE TABLE command with a standard warehouse.
> You only use the interactive warehouse in later steps, to query the interactive table.

The following command creates an interactive table containing the same columns and data
as a standard table. The CLUSTER BY clause refers to a column named `id` from the source table.

```sqlexample
CREATE INTERACTIVE TABLE
  IF NOT EXISTS orders
  CLUSTER BY (id)
AS
  SELECT * FROM demoSource;
```

#### Specifying auto-refresh for an interactive table

To make an interactive table automatically refresh using data from some
other table, specify the TARGET_LAG clause with an interval.
When you specify TARGET_LAG, you must also specify the WAREHOUSE clause
and the name of a standard warehouse that Snowflake will use to perform
refresh operations.

The time interval for the TARGET_LAG clause lets you specify the maximum
lag in terms of some number of seconds, minutes, hours, or days:

```sqlsyntax
TARGET_LAG = '<num> { seconds | minutes | hours | days }'
```

If you don’t specify a unit, the number represents seconds. The minimum value
is 60 seconds, or 1 minute.

For example, the following CREATE INTERACTIVE TABLE statement defines a dynamic interactive table
that lags no more than 20 minutes behind a specified source table, and uses a standard warehouse
named `my_standard_warehouse` to perform refresh operations:

```sqlexample
CREATE INTERACTIVE TABLE my_dynamic_interactive_table
  CLUSTER BY (c1, c2)
  TARGET_LAG = '20 minutes'
  WAREHOUSE = my_standard_warehouse
AS SELECT c1, SUM(c2) FROM my_source_table GROUP BY c1;
```

For more information about choosing an appropriate lag time that balances costs and freshness of data,
see [How Snowflake schedules refreshes](dynamic-tables-target-lag.md). Similar considerations apply to interactive tables as to
dynamic tables.

### Creating an interactive warehouse

After you create an interactive table, querying that table with optimal performance requires an interactive warehouse.
Specify the keyword INTERACTIVE in the [CREATE WAREHOUSE](../sql-reference/sql/create-warehouse.md) or CREATE OR REPLACE WAREHOUSE command.

Optionally, you can specify a TABLES clause with a comma-separated list of interactive table names.
Using that clause immediately associates those interactive tables with the interactive warehouse.

The following command creates an interactive warehouse that’s associated with the interactive table
named `orders`. In this case, you can immediately run a [USE WAREHOUSE](../sql-reference/sql/use-warehouse.md)
command for the interactive warehouse, and begin running queries for the interactive table:

```sqlexample
CREATE OR REPLACE INTERACTIVE WAREHOUSE interactive_demo
  TABLES (orders)
  WAREHOUSE_SIZE = 'XSMALL';
```

The following command creates an interactive warehouse with no associated interactive tables.
In this case, you run ALTER WAREHOUSE commands afterward to associate interactive tables
with the interactive warehouse:

```sqlexample
CREATE OR REPLACE INTERACTIVE WAREHOUSE interactive_demo
  WAREHOUSE_SIZE = 'XSMALL';
```

After you create an interactive warehouse, it remains in a suspended state until you resume it.
You can configure auto-suspend and auto-resume for interactive warehouses. The minimum
auto-suspend interval for an interactive warehouse is 24 hours (86400 seconds). For details,
see Resuming and suspending an interactive warehouse.

## Materialized view support for interactive tables

You can create materialized views on interactive tables. An *interactive materialized view*
precomputes and stores the results of a query on an interactive table, which can further improve
query performance for common aggregation patterns.

To create an interactive materialized view, use the INTERACTIVE keyword in the
[CREATE MATERIALIZED VIEW](../sql-reference/sql/create-materialized-view.md) statement:

```sqlexample
CREATE INTERACTIVE MATERIALIZED VIEW IF NOT EXISTS mv_order_summary
  AS
    SELECT region, SUM(quantity) AS total_quantity, SUM(net_paid) AS total_net_paid
      FROM orders
      GROUP BY region;
```

After you create the interactive materialized view, you must add **both** the materialized view
and the underlying base table to your interactive warehouse:

```sqlexample
ALTER WAREHOUSE interactive_demo ADD TABLES (mv_order_summary, orders);
```

### Best practices for interactive materialized views

Follow these guidelines when you create materialized views using interactive tables:

* Base the interactive materialized view on a single interactive table. Also, add the base table
  to the same interactive warehouse as the materialized view. These requirements are mandatory.
* Joins aren’t supported in materialized views, whether interactive or standard. Structure your
  queries to aggregate or filter from a single base table.
* You can’t use an interactive table or an interactive materialized view as the source for a
  [dynamic table](dynamic-tables-about.md).
* When you’re considering candidates for interactive materialized views,
  choose aggregation queries that are frequently run and expensive to compute

## Interactive table performance considerations

The following sections explain how to solve performance issues that you might encounter due to
the special characteristics of interactive tables and the workloads they’re best suited for.

### Query best practices for interactive warehouses

Interactive warehouses are optimized for queries with **selective workloads**. This means queries
with good selectivity see substantially more improvements on performance than other query types.

| Expect more performance benefits with interactive warehouses | Expect limited performance benefits with interactive warehouses |
| --- | --- |
| ```sqlexample SELECT col1, col4, AVG(col_x)   FROM my_table   GROUP BY col1, col4;```  This query is highly selective because it only requires a few columns. Snowflake can optimize loading only columns required for this one query. | ```sqlexample SELECT * FROM my_table;```  This query processes all columns. Although the query is simple, Snowflake must process a large amount of data, which might exceed the size of the cache. Even if the contents of the table can fit in the cache, that leaves less room to cache data from other queries, leading to lower concurrency. |
| ```sqlexample SELECT col1, col2   FROM my_table   WHERE     col_x IN (1,4,7,8)     AND event_time >=       DATEADD(hour, -1, CURRENT_TIMESTAMP());```  The conditions in the WHERE clause make this query highly selective. The IN clause limits the results to a relatively few items, and the time comparison further limits the data to a certain time period. | ```sqlexample SELECT col1, col2   FROM my_table   WHERE     event_time >=       DATEADD(day, -365, CURRENT_TIMESTAMP());```  Asking for data for an entire year makes this query less selective. If your dataset is big, this query might process all rows in the table. |

Other complexities such as large joins (for example, by joining two fact tables), or compute-intensive expressions such
as regular expressions, might result in lower concurrency due to higher use of compute resources.
See Choosing a size for an interactive warehouse for information about optimizing for
those situations.

### Data layout best practices for interactive tables

Interactive tables follow standard Snowflake best practices for performance. In particular,
interactive tables benefit from a **well-clustered table**, a table that’s sorted based on the same
column or columns that you are filtering on. For example, if your query often filters on a TIMESTAMP
column such as `sale_date`, then it makes sense to use that column as the clustering key when creating
the interactive table. For example, you might create the interactive table as follows:

```sqlexample
CREATE INTERACTIVE TABLE product_sales (<column definitions>) CLUSTER BY (sale_date);
```

That way, SELECT queries that filter on `sale_date` can quickly skip all irrelevant data
and return results. For example, the following query filters on a date range by testing the
`sale_date` column:

```sqlexample
SELECT ... WHERE sale_date > '2025-10-24' AND ...
```

For more details about choosing the best clustering keys, see
[Clustering Keys & Clustered Tables](tables-clustering-keys.md).

### Using search optimization for point lookups

We recommend adding [search optimization](search-optimization/enabling.md) when you
perform point lookup queries on your interactive table. Point lookups are queries that filter on a
single column to retrieve one or a few rows of data. A good example is `WHERE some_id =
some_UUID`.

### Choosing a size for an interactive warehouse

Once you’ve completed all your queries and layout optimizations, consider **scaling your warehouse**
to meet demand. Interactive warehouses have a range of sizes from XSMALL to 3XLARGE, as well as
[Multi-cluster warehouses](warehouses-multicluster.md).

We recommend that you start by sizing your warehouse based on the approximate size of the *working
data set* in the interactive table. The working data set refers to the portion of the data that is
frequently queried. For example, if your queries typically only query the last seven days of sales data,
the working set is the fraction of the interactive table corresponding to those seven days.

This is because the interactive warehouse utilizes *local storage caching*. While the data for
your entire data set (table) is always accessible, accessing non-cached data does incur higher read
latency on the first read.

Choose a warehouse size to fit the needs of your workloads. Experiment with your particular data and
workload to determine the optimal size for your interactive warehouse.

> **Tip:**
>
> For good performance, you don’t need to fit the entire working set of your queries in the cache.
> Pick a cache size that’s sufficient to hold your *hot data*, that is, the data from your
> frequently accessed rows.

We recommend starting with the following warehouse sizes based on the working data set size.

| Working Set | Warehouse Size |
| --- | --- |
| Less than 500 GB | XSMALL |
| 500 GB to 1 TB | SMALL |
| 1 TB to 2 TB | MEDIUM |
| 2 TB to 4 TB | LARGE |
| 4 TB to 8 TB | XLARGE |
| 8 TB to 16 TB | 2XLARGE |
| Greater than 16 TB | 3XLARGE |

#### Performance troubleshooting for interactive tables

##### Problem 1: My single query is taking too long

This is likely due to your query requiring more computing resources to finish. It’s possible that your
query has a lot of complex processing, thus requiring more CPUs. For example, queries with a lot of
regular expression filters and CASE clauses. It’s also possible that your queries require a lot of memory, such
as queries that do a lot of `COUNT(DISTINCT ...)`. To lower the run time of a single query,
consider a **larger warehouse size**. Start with the recommended size above, and keep
increasing the size of the warehouse until you are satisfied with a single query’s latency.

##### Problem 2: My queries are suddenly taking a long time to run (High tail latency, high P95 latency)

A sudden increase in query time is likely due to insufficient caching. Each warehouse size has a
local SSD cache that Snowflake uses to cache the most recently used data. Snowflake manages the cache to
only store parts of the table that are accessed frequently. If your queries are selective, then
increasing warehouse size can potentially reduce tail latency.

Also note, the newly spun-up warehouse takes a while to **warm the cache**. Snowflake proactively
warms the newly added data. For benchmarking, wait for a while before starting the benchmark so that
the cache has time to warm up. Cache warm-up speed is based on warehouse size and table size. The
bigger your interactive table is, the longer Snowflake takes to warm the cache. On the other hand,
the larger the size you specify for the interactive warehouse, the shorter the warming time.

##### Problem 3: My query is queuing or I’m not able to achieve the expected concurrency

You can scale out your warehouse by setting the MIN_CLUSTER_COUNT and MAX_CLUSTER_COUNT parameters.
That way, you can create a multi-cluster interactive warehouse.

### Adding an interactive table to an interactive warehouse

To get optimal query performance for an interactive table, you should use an interactive warehouse.

Before you can query the interactive table from an interactive warehouse, you must perform a
one-time operation to add the interactive table to the interactive warehouse. Otherwise, you’ll see
an `object not found` error when running a query against such a table from the interactive
warehouse. If you didn’t specify the interactive tables to associate with the interactive warehouses
by using the TABLES clause in your CREATE INTERACTIVE WAREHOUSE command, you can do that later by
using an [ALTER WAREHOUSE](../sql-reference/sql/alter-warehouse.md) command.

The following command associates the `orders` table with the `interactive_demo` warehouse. You can specify multiple table
names, separated by commas, with the ADD TABLES clause.

```sqlexample
ALTER WAREHOUSE interactive_demo ADD TABLES (orders);
```

This action starts the cache-warming process. That process might take significant time.

If the interactive table is already associated with the interactive warehouse, the command
succeeds but has no effect.

You can associate an interactive table with multiple interactive warehouses.

### Removing an interactive table from an interactive warehouse

You can detach one or more interactive tables from an interactive warehouse by running an [ALTER WAREHOUSE](../sql-reference/sql/alter-warehouse.md) command
with the DROP TABLES clause.

```sqlexample
ALTER WAREHOUSE interactive_demo DROP TABLES (orders, customers);
```

> **Note:**
>
> The interactive tables still exist after this operation. This ALTER WAREHOUSE clause isn’t the same as performing the SQL command DROP TABLE.

### Resuming and suspending an interactive warehouse

The following command resumes an interactive warehouse. You must do this after creating the warehouse, because it’s
created in a suspended state:

```sqlexample
ALTER WAREHOUSE interactive_demo RESUME;
```

You also do this to start running queries through the warehouse, if you manually suspended the warehouse.

Queries will be slow while the cache is being warmed after resuming. It might take a
few minutes to an hour or so, depending on how much data you have in that table.

The following command suspends an interactive warehouse:

```sqlexample
ALTER WAREHOUSE interactive_demo SUSPEND;
```

#### Auto-suspend and auto-resume for interactive warehouses

Interactive warehouses support auto-suspend and auto-resume. You can set the AUTO_SUSPEND
and AUTO_RESUME properties when creating or altering an interactive warehouse.

The minimum AUTO_SUSPEND value for an interactive warehouse is 86400 seconds (24 hours).
This minimum ensures that the cache stays warm long enough to provide consistent low-latency
performance. If you specify a value less than 86400, Snowflake uses 86400 instead.

The following example creates an interactive warehouse with auto-suspend after 24 hours of
inactivity, and auto-resume enabled:

```sqlexample
CREATE INTERACTIVE WAREHOUSE interactive_demo
  WAREHOUSE_SIZE = 'XSMALL'
  AUTO_SUSPEND = 86400
  AUTO_RESUME = TRUE;
```

You can also set these properties on an existing interactive warehouse:

```sqlexample
ALTER WAREHOUSE interactive_demo SET
  AUTO_SUSPEND = 86400
  AUTO_RESUME = TRUE;
```

> **Note:**
>
> In a production environment, you typically use interactive warehouses for workloads running
> many concurrent queries 24x7, or where low latency is crucial for queries. Suspending and
> resuming an interactive warehouse (whether manually or through auto-suspend) incurs
> significant cache warm-up time, so evaluate whether auto-suspend is appropriate for your
> workload pattern.

### Dropping an interactive warehouse

You can run the [DROP WAREHOUSE](../sql-reference/sql/drop-warehouse.md) command to remove an interactive warehouse entirely. Dropping an
interactive warehouse removes the associations between that warehouse and any interactive tables. However, you can still use other
interactive warehouses to query those same interactive tables.

### Querying an interactive table

In your query session, make sure that the warehouse for your current session is an interactive warehouse:

```sqlexample
USE WAREHOUSE interactive_demo;
```

After this, you can query your interactive table normally.

> **Note:**
>
> * In an interactive warehouse, you can only query interactive tables. To query other types of Snowflake tables, such as standard
>   tables or hybrid tables, switch to a standard warehouse first.
> * Certain types of queries are especially suited for interactive tables. For more information, see
>   Use cases for interactive tables.

### Benchmarking best practices

When assessing the performance of interactive tables in a test environment, follow these
best practices to avoid inconsistent or misleading results:

* Turn off the query result cache to make the benchmark results consistent between multiple
  benchmark runs. You can turn off the query result cache at the account, user, and session level by
  setting the [USE_CACHED_RESULT](../sql-reference/parameters.md) session parameter. That way, the
  queries only use the table data cache from the interactive warehouse. When you turn result caching
  on in your production environment, you can expect equal or better performance than in your
  benchmark testing.
* Because an interactive warehouse takes some time to warm the table data cache, wait for a while
  after you create or resume an interactive warehouse before testing query performance. This
  simulates the typical production configuration, where the warehouse remains active for long
  periods. Snowflake applies optimizations to the cache warming process. Therefore, it’s more
  efficient to let Snowflake complete this process than to warm the cache yourself by running sample
  queries.
* When comparing performance of interactive tables against standard Snowflake tables, don’t
  interleave the queries between standard and interactive tables. Instead, run the full benchmark on
  standard tables, then run the same tests on interactive tables.
* When doing comparative benchmarks with other database systems, make sure that the clustering
  columns in your interactive tables match the WHERE clause predicates in your queries. For more
  information about choosing the best clustering columns, see
  [Clustering Keys & Clustered Tables](tables-clustering-keys.md). In particular, don’t cluster on columns with
  high cardinality, such as unique IDs or timestamps.
* If your queries are short and simple, you can achieve higher concurrency by setting the
  [MAX_CONCURRENCY_LEVEL](../sql-reference/parameters.md) parameter to a higher value for
  your interactive warehouse.

## Interactive tables and storage lifecycle policies

You can use [storage lifecycle policies](storage-management/storage-lifecycle-policies.md) to
archive or expire specific table rows based on conditions that you define, such as data age or other criteria.

Currently, you can’t use storage lifecycle policies for interactive tables that use auto-refresh.
You can use the TARGET_LAG parameter, or a storage lifecycle policy, but not both.

## Cost and billing considerations

Interactive warehouses incur compute charges when active. The minimum billable period for
an interactive warehouse is one hour, and at one-second granularity thereafter.

> **Note:**
>
> If you resume an interactive warehouse that was suspended (whether manually or through
> auto-resume), that operation results in a new minimum billable period charge. That charge
> applies even if you were already being billed for that period because of other recent activity
> in the warehouse. Therefore, avoid suspending and resuming an interactive warehouse multiple
> times within a short period. The 24-hour minimum auto-suspend interval helps prevent
> excessive suspend/resume cycles.

Interactive tables incur standard storage costs. The price for storage of interactive tables is the
same as for standard tables. Interactive tables may be larger than equivalent standard tables, due to
differences in data encoding and additional indexes. The larger data size and indexes are factored into
the storage volume.

For more information about cost and billing for interactive warehouses and interactive tables, see the
[Snowflake service consumption table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).

## Affected SQL statements

This feature introduces changes to the following Snowflake SQL commands:

* [ALTER WAREHOUSE](../sql-reference/sql/alter-warehouse.md): new ADD TABLES and DROP TABLES clauses.
* [CREATE INTERACTIVE TABLE](../sql-reference/sql/create-interactive-table.md): creates interactive tables with required CLUSTER BY clause.
* [CREATE INTERACTIVE WAREHOUSE](../sql-reference/sql/create-interactive-warehouse.md): creates interactive warehouses with an
  optional TABLES clause.
* [CREATE MATERIALIZED VIEW](../sql-reference/sql/create-materialized-view.md): new optional INTERACTIVE keyword for creating
  materialized views on interactive tables.
