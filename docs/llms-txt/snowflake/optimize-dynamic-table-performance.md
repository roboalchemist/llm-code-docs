# Source: https://docs.snowflake.com/en/user-guide/tutorials/optimize-dynamic-table-performance.md

Snowflake

Dynamic Tables

Performance

# Tutorial: Optimize dynamic table performance for SCD Type 1 workloads

## Introduction

This tutorial shows you how to identify and resolve performance bottlenecks in a [dynamic table](../dynamic-tables-about.md)
pipeline for slowly changing dimension (SCD) Type 1 workloads. Dynamic tables automatically materialize query
results and handle scheduling and orchestration for your data pipelines. Optimizing dynamic table performance
helps you maintain data freshness and control costs.

### About SCD Type 1 tables

Slowly changing dimension (SCD) tables store data that changes occasionally and unpredictably over time.
Common examples include tables that track changes to customer addresses or product prices.

This tutorial implements an SCD Type 1 table, often called an “SCD-1 live” table.
This type overwrites old data with new data and doesn’t keep a history of past values.
SCD Type 1 tables are useful when you only care about the latest state of each record, such as a customer’s current phone
number or a product’s current category.

In real-world data pipelines, you typically build a Type 1 SCD table by consuming a changelog table.

### What you’ll learn

In this tutorial, you’ll learn how to complete the following tasks:

* Create a sample source table with product change data.
* Build two SCD Type 1 dynamic tables: one with a suboptimal SQL pattern and one with an optimized pattern with
  the [QUALIFY](../../sql-reference/constructs/qualify.md) clause.
* Understand how the `QUALIFY` clause enables efficient incremental processing and significantly reduces refresh time.
* Monitor key performance metrics like refresh duration and partition scans to identify optimization opportunities.
* Compare the incremental refresh performance of both dynamic tables on the same data.

### Prerequisites

You need access to a Snowflake environment with the following resources:

* A [warehouse](../warehouses-overview.md) for compute resources. We recommend using an x-small warehouse.
* The privileges required to create databases, schemas, and dynamic tables.
  For more information, see [Access control privileges](../security-access-control-privileges.md).

If you don’t have a user with the necessary permissions, ask someone who does to create one for you.
Users with the ACCOUNTADMIN role can create new users and grant them the required privileges.

> **Note:**
>
> For the best experience, complete this tutorial in Snowsight so that you can quickly view the query history
> and monitor your dynamic table performance.

## Step 1: Create the source data

Start by setting up a source table with sample data that simulates streaming product changes.

Create a database and schema for the tutorial, then create a source table:

```sqlexample
CREATE DATABASE IF NOT EXISTS dt_perf_demo_db;
CREATE SCHEMA IF NOT EXISTS dt_perf_demo_db.tutorial;

USE SCHEMA dt_perf_demo_db.tutorial;

CREATE OR REPLACE TABLE product_changes (
    product_code VARCHAR(50),
    product_name VARCHAR(200),
    price NUMBER(10, 2),
    price_start_date TIMESTAMP_NTZ(9)
);
```

Next, insert sample data into the `product_changes` source table. The following command
generates 100 million rows of sample product data by repeating 10,000 unique product codes and names.
It assigns each product a price that changes slightly with each row, and sets a timestamp that increases by a few minutes
for each new entry.

```sqlexample
INSERT INTO product_changes (product_code, product_name, price, price_start_date)
  SELECT
      'PC-' || LPAD(TO_VARCHAR(MOD(SEQ4(), 10000) + 1), 3, '0') AS product_code,
      'Product ' || LPAD(TO_VARCHAR(MOD(SEQ4(), 10000) + 1), 3, '0') AS product_name,
      ROUND(10.00 + (MOD(SEQ4(), 10000) * 5) + (SEQ4() * 0.01), 2) AS price,
      DATEADD(MINUTE, SEQ4() * 5, '2025-01-01 00:00:00') AS PRICE_START_DATE
  FROM
      TABLE(GENERATOR(ROWCOUNT => 100000000));
```

## Step 2: Create dynamic tables for comparison

In this step, you create two SCD Type 1 dynamic tables that consume from the source table. The first dynamic table
uses a suboptimal SQL pattern to find the most recent price change for every product, while the second uses an
optimized pattern. Creating both tables simultaneously lets you directly compare their refresh performance
on the same data.

### Create a suboptimal dynamic table

Create a dynamic table by using an INNER JOIN with a subquery that gets the latest timestamp for each product code.
This is a common but inefficient pattern that triggers costly re-computation on every update.

> **Note:**
>
> Replace `my_warehouse` with the name of your warehouse.

```sqlexample
CREATE DYNAMIC TABLE product_current_price_v1
    TARGET_LAG = DOWNSTREAM
    WAREHOUSE = <my_warehouse>
    INITIALIZE = ON_SCHEDULE
    REFRESH_MODE = INCREMENTAL
  AS
  SELECT
      h.product_code,
      h.product_name,
      h.price,
      h.price_start_date
  FROM product_changes h
  INNER JOIN (
      SELECT product_code, MAX(price_start_date) max_price_start_date
      FROM product_changes
      GROUP BY product_code
  ) m ON h.price_start_date = m.max_price_start_date AND h.product_code = m.product_code;
```

Key details about this dynamic table configuration:

* This dynamic table uses `TARGET_LAG = DOWNSTREAM`, which means it refreshes only when downstream
  tables or queries need fresh data. This setting works well for intermediate tables in a pipeline.
* The `REFRESH_MODE = INCREMENTAL` setting tells Snowflake to process only changed data instead of
  recomputing the entire table.

### Create an optimized dynamic table

Now create a second dynamic table named `product_current_price_v2` with an optimized SQL pattern.
This table uses the `QUALIFY` clause to efficiently filter to the latest price for each product:

```sqlexample
CREATE DYNAMIC TABLE product_current_price_v2
    TARGET_LAG = DOWNSTREAM
    WAREHOUSE = <my_warehouse>
    REFRESH_MODE = INCREMENTAL
    INITIALIZE = ON_SCHEDULE
  AS
  SELECT
      product_code,
      product_name,
      price,
      price_start_date
  FROM product_changes
  QUALIFY RANK() OVER (PARTITION BY product_code ORDER BY price_start_date DESC) = 1;
```

Using the `QUALIFY` clause with a ranking window function like `RANK()` lets Snowflake efficiently detect which
product partitions changed. Instead of rescanning all historical data, the engine finds affected partitions
and recalculates rankings only for those specific products. This results in more efficient incremental refreshes.

This optimization works because of the following factors:

* Ranking functions like `RANK`, `ROW_NUMBER`, or `DENSE_RANK` used with `PARTITION BY` let the engine isolate changes by product.
* Filtering to `RANK() ... = 1` keeps only the latest record for each product, which is what SCD Type 1 tables require.
* Placing the `QUALIFY RANK() ... = 1` clause at the top level of the dynamic table query, not within a subquery,
  ensures that the optimization applies.
* Persisting the `product_code` and `price_start_date` keys as columns in the dynamic table lets the engine track partition changes between
  refreshes and avoids full table scans.

This pattern also demonstrates good *data locality*, which describes how closely Snowflake stores rows
with matching keys together. The pattern isolates changes to specific partition keys, which avoids
full table scans.

### Refresh both dynamic tables

To fill in the initial data for both tables, manually refresh them. This establishes a baseline for comparing
their incremental refresh performance in the next step:

```sqlexample
ALTER DYNAMIC TABLE product_current_price_v1 REFRESH;

ALTER DYNAMIC TABLE product_current_price_v2 REFRESH;
```

## Step 3: Compare incremental refresh performance

Now compare how each table handles incremental refreshes.

### Add new data to the source table

This step simulates new data arriving in the source table,
as would happen in a real-world streaming scenario. Insert 1,000 new rows into the `product_changes` source table
that update the price for five of the existing products:

```sqlexample
INSERT INTO product_changes (product_code, product_name, price, price_start_date)
  SELECT
      'PC-' || LPAD(TO_VARCHAR(MOD(SEQ4(), 5) + 1), 3, '0') AS product_code,
      'Product ' || LPAD(TO_VARCHAR(MOD(SEQ4(), 5) + 1), 3, '0') AS product_name,
      ROUND(50.00 + (MOD(SEQ4(), 10) * 5) + ((SEQ4() + 100000000) * 0.01), 2) AS price,
      DATEADD(MINUTE, (SEQ4() + 100000000) * 5, '2025-01-01 00:00:00') AS price_start_date
  FROM
      TABLE(GENERATOR(ROWCOUNT => 1000));
```

### Monitor refresh performance

Dynamic table performance depends on several factors: how you write queries, how you organize data,
and the resources you allocate. The key metrics to monitor are refresh duration, partition scans,
and bytes spilled. In this step, you’ll compare these metrics between the two dynamic table implementations.

To pick up the changes, start by refreshing the suboptimal dynamic table:

```sqlexample
ALTER DYNAMIC TABLE product_current_price_v1 REFRESH;
```

Check the execution time and scan metrics:

1. Navigate to Transformation » Dynamic Tables.
2. Filter the list by selecting the `dt_perf_demo_db` database, then select `product_current_price_v1`.
3. Select the Refresh History tab and notice the REFRESH DURATION value for the most recent refresh.
4. Select Show query profile for the latest refresh entry.
5. Find the Statistics section and notice the Partitions scanned value.

   The `product_current_price_v1` table is inefficient because the subquery recalculates the maximum timestamp for all 10,000 products,
   even though only five products received new price changes. This forces the dynamic table engine to scan many more partitions than necessary,
   driving up both time and cost as the source table grows. This pattern demonstrates poor data locality
   because changes don’t align well with how the data is organized for incremental processing.
6. Now refresh the optimized `product_current_price_v2` dynamic table:

   ```sqlexample
   ALTER DYNAMIC TABLE product_current_price_v2 REFRESH;
   ```

7. Repeat the previous steps to check the Refresh History for the optimized table:

   Compare the two refresh operations. The optimized `product_current_price_v2` dynamic table should complete significantly faster
   than the suboptimal `product_current_price_v1` dynamic table. In the example results, the suboptimal table took 2.8 seconds
   while the optimized table took only 804 milliseconds.

   Open the Query Profile and compare the Statistics section:

   The `product_current_price_v2` uses the `QUALIFY` clause with a ranking window function, which lets the engine
   efficiently identify and process only the five products that changed, resulting in a much faster incremental refresh.
   This query pattern has good data locality because Snowflake can isolate which partition keys (product codes) contain changes.

> **Tip:**
>
> Even at the small scale used in this tutorial, this optimization leads to noticeable performance improvements.
> In production, with millions of products and billions of records,
> this optimization can cut refresh times from hours to seconds.
> Performance depends on the percentage of changed products, so efficiency remains high as your data grows.
>
> Faster refreshes translate directly to fresher data. If you need data fresh within minutes,
> optimizing query patterns like this helps you meet aggressive target lag requirements without
> oversizing warehouses.

## Clean up

To delete all objects created for this tutorial, run the following DROP statement:

```sqlexample
DROP DATABASE dt_perf_demo_db;
```

## Summary and additional resources

In this tutorial, you optimized a [dynamic table](../dynamic-tables-about.md) pipeline by replacing
a suboptimal subquery pattern with the highly efficient `QUALIFY RANK() = 1` pattern for an SCD Type 1 table.
This lets the dynamic table engine apply performance optimizations for
[incremental refresh](../dynamic-tables-refresh.md) and leads to faster and cheaper pipeline runs.
Faster refreshes mean you can maintain data freshness with tighter
[target lag](../dynamic-tables-target-lag.md) requirements without increasing cost.

Along the way, you completed the following tasks:

* **Created a source table** with sample product data simulating a changelog.
* **Created a suboptimal SCD Type 1 dynamic table** that demonstrated the common pitfall of using
  a nested query with `MAX()` to find the latest records.
* **Applied the QUALIFY optimization** to significantly improve dynamic table refresh performance with
  efficient [incremental processing](../dynamic-tables-refresh.md). This pattern improves
  [data locality](../dynamic-tables-performance-optimize.md) by letting the engine isolate changes to
  specific partition keys.
* **Monitored refresh performance** by comparing partition scans and execution times between different
  implementations using the [query profile](../dynamic-tables-performance-monitor.md). These metrics
  help you identify whether your queries work efficiently with incremental refresh.

**Key performance concepts demonstrated:**

* **Incremental refresh efficiency**: The [optimized query](../dynamic-tables-performance-optimize-query.md)
  processes only changed data, while the suboptimal query rescans the entire dataset.
* **Data locality**: When changes align with partition keys (product codes),
  [incremental refresh](../dynamic-tables-refresh.md) performs well. When changes scatter across
  many keys or require full rescans, performance suffers. See [Improve data locality](../dynamic-tables-performance-optimize.md) for more details.
* **Target lag and freshness**: Optimizing query patterns lets you meet tighter
  [data freshness requirements](../dynamic-tables-target-lag.md) without oversizing
  [warehouses](../dynamic-tables-warehouses.md).

For more information about dynamic tables and optimization techniques, explore the following resources:

**Query and pipeline optimization:**

* **Query optimization for incremental refresh**: Learn which operators perform well with incremental
  refresh and how to restructure queries for better performance. See
  [Optimize queries for incremental refresh](../dynamic-tables-performance-optimize-query.md).
* **Data locality**: Understand how data organization affects incremental refresh performance and
  how to cluster source tables. See [Improve data locality](../dynamic-tables-performance-optimize.md).
* **Immutability constraints**: To avoid reprocessing unchanged historical data, use the
  [IMMUTABLE WHERE](../dynamic-tables-performance-optimize-immutability.md)
  option. This can greatly reduce refresh costs and time.

**Infrastructure and monitoring:**

* **Target lag**: Learn how to balance data freshness requirements with compute costs by choosing
  appropriate target lag settings. See [Understanding dynamic table target lag](../dynamic-tables-target-lag.md).
* **Warehouse sizing**: Learn how warehouse size affects refresh performance and cost. See
  [Adjust your warehouse configuration](../dynamic-tables-performance-optimize.md).
* **Performance monitoring**: Track key metrics like refresh duration, partition scans, and warehouse
  utilization to identify optimization opportunities. See [Monitor dynamic table performance](../dynamic-tables-performance-monitor.md).
* **Refresh modes**: Understand when to use incremental vs. full refresh mode and how Snowflake chooses
  between them. See [Understanding dynamic table initialization and refresh](../dynamic-tables-refresh.md).
* **Dynamic Iceberg tables**: Use dynamic tables with Apache Iceberg™ tables to build interoperable data pipelines
  for your data lake. See [Create dynamic Apache Iceberg™ tables](../dynamic-tables-create-iceberg.md).
