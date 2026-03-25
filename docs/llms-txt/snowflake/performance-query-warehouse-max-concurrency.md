# Source: https://docs.snowflake.com/en/user-guide/performance-query-warehouse-max-concurrency.md

# Limiting concurrently running queries

This topic discusses how a warehouse owner or administrator can reduce the number of queries that are running concurrently on a warehouse
in order to improve the performance of those queries.

Queries running concurrently in a warehouse must share the warehouse’s resources, meaning each query might be granted fewer
resources. You can use the [MAX_CONCURRENCY_LEVEL](../sql-reference/parameters.md) parameter to limit the number of concurrent queries
running in a warehouse. Because fewer queries are competing for the warehouse’s resources, a query can potentially be given more resources.

Lowering the concurrency level may boost performance for individual queries, especially large, complex, or multi-statement queries, but
these adjustments should be thoroughly tested to ensure they have the desired effect.

Be aware that lowering the MAX_CONCURRENCY_LEVEL for a warehouse can lead to more queries being placed in a queue, which has a performance
implication for those queries. Other strategies such as using a dedicated warehouse or using the
[Query Acceleration Service](performance-query-warehouse-qas.md) can boost the performance of a large or complex query without impacting
the rest of the workload.

For more information, see [MAX_CONCURRENCY_LEVEL](../sql-reference/parameters.md).

> **Note:**
> > Adjusting the [STATEMENT_QUEUED_TIMEOUT_IN_SECONDS](../sql-reference/parameters.md) parameter can cancel queries rather than let them remain in the queue for an extended period of time.

## How to lower MAX_CONCURRENCY_LEVEL

The default maximum concurrency level is 8. To lower the level, use the [ALTER WAREHOUSE](../sql-reference/sql/alter-warehouse.md) command to specify a
lower number. For example:

> ```sqlexample
> ALTER WAREHOUSE my_wh SET MAX_CONCURRENCY_LEVEL = 4;
> ```
