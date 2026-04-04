# Source: https://docs.snowflake.com/en/release-notes/performance-improvements-2026.md

# 2026 Performance improvements

> **Important:**
>
> Performance improvements often target specific query patterns or workloads. These improvements might or might not have a material impact
> on a specific workload.

The following performance improvements were introduced in 2026:

| Released | Description | Impact |
| --- | --- | --- |
| January 2026 | Improved query performance with [Snowflake Optima Metadata](../user-guide/snowflake-optima.md), which continuously analyzes your workload patterns and creates metadata to optimize pruning of unused micro-partitions. Snowflake Optima is only available on [Snowflake generation 2 standard warehouses (Gen2)](../user-guide/warehouses-gen2.md). | Improves performance of queries by creating metadata for more efficient pruning. |
| January 2026 | Improved pruning for [join queries](../sql-reference/constructs/join.md) with inequality predicates. For example, the following join query uses the `>` operator in an inequality predicate:  ```sqlexample SELECT *   FROM employees e, managers m   WHERE e.employee_id = m.employee_id AND         e.salary > m.salary AND         m.level = 'M5';```  For this query, Snowflake prunes micro-partitions from the `employees` table where all salaries are below the lowest `M5` manager salary. | Improves the performance of join queries that have inequality predicates. |
