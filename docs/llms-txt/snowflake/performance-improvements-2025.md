# Source: https://docs.snowflake.com/en/release-notes/performance-improvements-2025.md

# 2025 Performance improvements

> **Important:**
>
> Performance improvements often target specific query patterns or workloads. These improvements might or might not have a material impact
> on a specific workload.

The following performance improvements were introduced in 2025:

| Released | Description | Impact |
| --- | --- | --- |
| November 2025 | Enhanced [Query Acceleration Service (QAS)](../user-guide/query-acceleration-service.md) to intelligently determine when queries with LIMIT clauses can be accelerated. | More queries with LIMIT clauses (including those without ORDER BY) are now eligible for acceleration. QAS automatically determines when accelerating these queries improves performance, broadening the scope of queries that benefit from QAS. |
| October 2025 | [Insights about query performance provided in Snowsight](../user-guide/query-insights.md) (General Availability). | You can use these [query insights](../user-guide/query-insights.md) to identify queries where you can improve performance. |
| September 2025 | More efficient workload distribution. | Improves query execution time by detecting and adaptively redistributing workloads across nodes in the warehouse, without user intervention. |
| September 2025 | [Insights about query performance provided in Snowsight](../user-guide/query-insights.md) (Preview). | You can use these [query insights](../user-guide/query-insights.md) to identify queries where you can improve performance. |
| August 2025 | More efficient and accurate NDV estimations that lead to more effective query plans. | Improves query compilation and execution times, especially for DML statements. |
| August 2025 | Improved filters that eliminate irrelevant data early, thereby reducing the volume of data that needs to be buffered to memory or storage. These filters reduce the amount of data processed before it’s used in a sub-query or Common Table Expression (CTE). | Improves query performance for complex queries where the same data is needed across different parts of the query plan. Subsequent filter operations are more efficient, saving time and compute resources. |
| August 2025 | Improved query performance with [Snowflake Optima](../user-guide/snowflake-optima.md), which continuously analyzes your workload patterns and automatically applies workload-specific optimizations. Snowflake Optima is only available on [Snowflake generation 2 standard warehouses (Gen2)](../user-guide/warehouses-gen2.md). | Improves performance of queries that include frequently used selective predicate patterns. |
| July 2025 | Insights about query performance provided in the [QUERY_INSIGHTS view](../sql-reference/account-usage/query_insights.md). | You can use these [query insights](../user-guide/query-insights.md) to identify queries where you can improve performance. |
| June 2025 | Expands coverage of the [Query Acceleration Service (QAS)](../user-guide/query-acceleration-service.md) to [Apache Iceberg™ tables](../user-guide/tables-iceberg.md). | QAS can now improve the performance of queries on Iceberg tables. |
| May 2025 | Search optimization update: [Support for Apache Iceberg™ tables](../user-guide/search-optimization/queries-that-benefit.md). | Improves the performance of queries on Iceberg tables. |
| May 2025 | Improved performance of dynamic table refreshes that contain top-level QUALIFY clauses with RANK or ROW_NUMBER ranking window functions, specifically when the rank value is 1. | Dynamic tables using `QUALIFY RANK() = 1` or `ROW_NUMBER = 1` now refresh more quickly, improving performance for common deduplication and top-N use cases. |
| May 2025 | Enhanced vectorized scanner availability for improved performance | Previously, [the vectorized scanner](../sql-reference/sql/copy-into-table.md) could only be used with specific `ON_ERROR` settings (`ABORT_STATEMENT` or `SKIP_FILE`). This restriction has been removed. Now, you can enable the vectorized scanner with any `ON_ERROR` option, including `CONTINUE`, `SKIP_FILE_num`, and `'SKIP_FILE_num%'`. This change allows the performance-enhancing vectorized scanner to be used in more situations. You may see faster data processing as a result. |
| April 2025 | Expands coverage of the [Query Acceleration Service (QAS)](../user-guide/query-acceleration-service.md) to more queries. | Improves the heuristics that QAS uses to determine whether or not a query will benefit from acceleration. As a result, more queries are eligible for acceleration by QAS. |
| March 2025 | Improves the batching of files during replication refresh operations. | Replication refresh jobs that replicate up to 8 GB of data will have less variance and more predictability. |
| March 2025 | Improves performance for dynamic tables with incremental refresh mode using left outer joins. | Provides faster incremental refresh performance for dynamic tables that contain one or more left outer joins. Performance gains can be substantial depending on the workload. |
| March 2025 | Adaptively optimizes compute and I/O resources for queries executed against Apache Iceberg™ tables. | Improves Apache Iceberg™ query performance and memory efficiency in high-concurrency scenarios. |
| February 2025 | [Tasks](../user-guide/tasks-intro.md) can be scheduled to run as frequently as every 10 seconds. | Reduces the time required between scheduled task executions. |
