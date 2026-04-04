# Source: https://docs.startree.ai/corecapabilities/query_data/query_languages/msqe.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Multi-Stage Query Engine

## Overview and Purpose

The Multi-Stage Query Engine (MSQE) is StarTree Cloud's advanced query processing system that enables complex analytical operations such as joins, window functions, and set operations across multiple tables. Unlike the traditional single-stage engine that uses a simple scatter-gather approach, MSQE breaks queries into multiple processing stages that can be efficiently executed across distributed servers.

<img src="https://mintcdn.com/startree/Pjfn0BG5VkJp2RKX/images/Multi-stage-query-engine-1.svg?fit=max&auto=format&n=Pjfn0BG5VkJp2RKX&q=85&s=a3fbdef2c57f2fe2f27a67364954bad3" alt="Multi Stage Query Engine 1 Sv" width="464" height="460" data-path="images/Multi-stage-query-engine-1.svg" />

MSQE is particularly valuable for:

* Joining data across multiple tables
* Complex analytical queries requiring multi-step processing
* Queries involving window functions and advanced aggregations
* Set operations (UNION, INTERSECT, MINUS)
* Applications requiring insights from related data in separate tables

**Note:** MSQE is the primary query mode in StarTree Cloud and is recommended for most analytical workloads, especially those involving joins or complex processing.

## Enabling MSQE

To query using distributed joins, window functions, and other multi-stage operators, you need to enable the multi-stage query engine. There are several ways to do this:

### Using the Query Console

In the StarTree Cloud Query Console, simply select the **Use Multi-Stage Engine** checkbox before running your query.

### Using REST APIs

When using the Controller Admin API:

```bash  theme={null}
curl -X POST http://localhost:9000/sql -d '
{
  "sql": "select * from baseballStats limit 10",
  "trace": false,
  "queryOptions": "useMultistageEngine=true"
}'
```

When using the Broker Query API:

```bash  theme={null}
curl -X POST http://localhost:8000/query/sql -d '
{
  "sql": "select * from baseballStats limit 10",
  "trace": false,
  "queryOptions": "useMultistageEngine=true"
}'
```

### Using the SET Command

You can enable MSQE directly in your SQL query by adding a SET command at the beginning:

```
SET useMultistageEngine=true;
SELECT * from baseballStats limit 10
```

## Key Capabilities

### Table Joins

MSQE supports joining tables in a distributed manner using various strategies:

```
SELECT customer.name, orders.amount
FROM customer
JOIN orders ON customer.id = orders.customer_id
WHERE orders.amount > 100
```

Join strategies include:

* Lookup joins (for small dimension tables)
* Colocated joins (when data is partitioned on join keys)
* Query-time partition joins
* Broadcast joins

### Window Functions

MSQE enables analytical functions over partitions of result sets:

```
SELECT product_id, 
       date, 
       sales, 
       SUM(sales) OVER (PARTITION BY product_id ORDER BY date 
                         ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS rolling_7day_sales
FROM sales
```

### Set Operations

MSQE supports operations across multiple query results:

```
SELECT customer_id FROM active_customers
UNION
SELECT customer_id FROM new_signups
```

## How MSQE Works

MSQE processes queries through a multi-stage execution pipeline:

1. **Query Planning**: The query is parsed and transformed into a logical plan
2. **Stage Assignment**: The plan is divided into multiple execution stages
3. **Distributed Execution**: Stages are distributed across servers for parallel processing
4. **Data Shuffling**: When needed, data is moved between stages using optimized shuffling
5. **Result Collection**: Final results are gathered at the root stage and returned

Each stage serves a specific purpose:

* **Leaf Stages**: Read data directly from tables
* **Intermediate Stages**: Process operations like joins and aggregations
* **Root Stage**: Collects and finalizes results for the client

## Using MSQE

### Checking Execution Plans

To understand how a query will be executed, use the EXPLAIN PLAN command:

```sql  theme={null}
EXPLAIN PLAN FOR
SELECT customer.name, SUM(orders.amount)
FROM customer
JOIN orders ON customer.id = orders.customer_id
GROUP BY customer.name
```

The output shows the logical plan with stages indicated by `PinotLogicalExchange` operators.

### Optimization Tips

1. **Join Key Selection**: Choose join keys that match table partitioning when possible
2. **Filtering Early**: Apply filters before joins to reduce data movement
3. **Dimension Table Design**: Keep dimension tables small for efficient lookup joins
4. **Column Selection**: Select only necessary columns to minimize data transfer

## Performance Considerations

1. **Join Complexity**: Performance scales with join complexity and table sizes
2. **Data Distribution**: Evenly distributed data performs better than skewed distributions
3. **Partitioning Strategy**: Align table partitioning with common join keys
4. **Memory Requirements**: Complex joins may require additional memory

Built with [Mintlify](https://mintlify.com).
