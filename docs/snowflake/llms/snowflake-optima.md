# Source: https://docs.snowflake.com/en/user-guide/snowflake-optima.md

# Snowflake Optima

Snowflake Optima extends Snowflake’s core principles of performance and simplicity by applying an
intelligent approach to workload optimization. Instead of requiring manual tuning, Snowflake Optima continuously analyzes
workload patterns and implements the most effective strategies automatically. Snowflake Optima ensures that queries run faster
and more cost-efficiently, without added configuration or maintenance. By anticipating and adapting to the evolving
nature of SQL workloads, Snowflake Optima automatically improves performance.

> **Note:**
>
> * Snowflake Optima is included in all [Snowflake editions](intro-editions.md).
> * Snowflake Optima is only available on
>   [Snowflake generation 2 standard warehouses](warehouses-gen2.md).

The following sections describe Snowflake Optima in more detail:

## Optima Indexing

*Optima Indexing* is a Snowflake Optima feature that automatically analyzes workloads to create and maintain
indexes in the background. Optima Indexing is built on top of the
[search optimization service](search-optimization-service.md).

By continuously monitoring SQL workloads, Optima Indexing identifies opportunities to improve performance — such
as repetitive point-lookup queries on a table — and automatically generates hidden indexes to accelerate those workloads.
These indexes are built and maintained on a best-effort basis, without requiring user intervention.

There are no additional costs for Optima Indexing, and because it is fully integrated into Snowflake, no additional
configuration or effort is required to benefit from improved performance.

For specialized workloads that demand guaranteed performance — for example, threat detection in the cybersecurity industry —
you can still directly apply search optimization. This option provides consistent index freshness and ultimately consistent
performance for scenarios where near real-time results are critical.

## Optima Metadata

*Optima Metadata* is a Snowflake Optima feature that automatically optimizes your workloads without any user input.
Snowflake Optima analyzes your query patterns, identifies inefficient usage of columns in pruning, and creates additional
metadata to optimize these queries. Even if you don’t know all the nuances of Snowflake’s query engine, Optima still ensures
that you prune unused micro-partitions as effectively as possible.

For example, one of the scenarios that Snowflake Optima has optimized is usage of the [UPPER](../sql-reference/functions/upper.md) and
[LOWER](../sql-reference/functions/lower.md) functions in the WHERE clause. These functions are inefficient in pruning. So, if Snowflake
Optima observes frequent use of these functions in your query filter predicates, it automatically creates metadata to aid in
pruning.

In general, the best practice is to avoid scenarios that lead to inefficient pruning. However, Snowflake Optima can improve
performance when these scenarios occur. That is, you should continue to follow all existing query performance best practices and think of Optima
Metadata as a feature that works in the background to catch optimizations you might have missed.

## Monitor Snowflake Optima use

You can monitor Snowflake Optima use on the following panes in the [Query Profile tab](ui-snowsight-activity.md)
under Query History in Snowsight:

* Query insights pane
* Statistics pane

You can also monitor Snowflake Optima use by querying the [QUERY_INSIGHTS view](../sql-reference/account-usage/query_insights.md).
For more information about query insights, see [Using query insights to improve performance](query-insights.md).

### Query insights pane

The [Query insights](query-insights.md) pane displays each type of insight detected
for a query and lists each instance of that insight type.

* To learn more about the condition that was detected, select View next to an entry in the
  Query insights pane.

If Snowflake Optima was used to optimize the given query, Snowflake Optima used appears and the details
are displayed.

The following image shows an example of the Query insights pane that indicates that Snowflake Optima was used:

### Statistics pane

To view pruning statistics for Snowflake Optima, open the
[Statistics](search-optimization/monitoring-search-optimization.md) pane on the Query Profile tab.
Look for the row labeled Partitions pruned by Snowflake Optima. This row shows the number of partitions skipped during
query execution, indicating how Snowflake Optima improved performance by reducing the amount of data scanned.

The following image shows an example of the Statistics pane that indicates that Snowflake Optima was used:
