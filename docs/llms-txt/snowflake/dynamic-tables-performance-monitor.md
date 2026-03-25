# Source: https://docs.snowflake.com/en/user-guide/dynamic-tables-performance-monitor.md

# Monitor dynamic table performance

Performance monitoring helps you with the following tasks:

* Identify slow or costly dynamic table refreshes.
* Diagnose bottlenecks.
* Measure the impact of optimizations.

This topic explains what to look for to monitor dynamic table performance and how to diagnose issues.
For information about monitoring tools, see [Monitor dynamic tables](dynamic-tables-monitor.md).

> **Tip:**
>
> For a hands-on example, see
> [Tutorial: Optimize dynamic table performance for SCD Type 1 workloads](tutorials/optimize-dynamic-table-performance.md).

## Key performance indicators

To monitor dynamic table performance, focus on the metrics described in this section.

### Refresh duration

Refresh duration measures how long each refresh takes to complete. To spot performance
degradation, track refresh duration over time.

Warning signs:

* **Duration increases over time**: Growing data volumes or degrading
  [data locality](dynamic-tables-performance-optimize.md) can cause refresh times to steadily increase.
* **Duration approaches target lag**: When refreshes take nearly as long as your target lag,
  you might not meet data freshness requirements.
* **High variance in duration**: Large swings in refresh time might indicate workload spikes or
  resource contention.

To view refresh duration, see [Monitor the refresh status for your dynamic tables](dynamic-tables-monitor.md).

### Lag metrics

Lag metrics show how well your dynamic table meets its freshness target. For information about
how target lag works, see [Understanding dynamic table target lag](dynamic-tables-target-lag.md).

Key metrics:

* **Actual lag**: The time between when source data changed and when the dynamic table
  reflected those changes.
* **Time within target lag ratio**: The percentage of time a table stayed within its target lag.
  A ratio below one indicates that the pipeline isn’t meeting its freshness goal.
* **Maximum lag**: The longest actual lag during a given period.

To view lag metrics, see [Monitor the refresh status for your dynamic tables](dynamic-tables-monitor.md).

### Partition statistics

For incremental refreshes, the number of partitions scanned should be proportional to the
data that changed, not the total table size. High partition scans indicate poor data locality.

Warning signs:

* Scanning a large percentage of total partitions during incremental refresh.
* Partition scans increasing over time without corresponding data growth.

To view partition statistics, see Analyze query profiles.

For guidance on improving data locality, see [Improve data locality](dynamic-tables-performance-optimize.md).

### Refresh mode

The refresh mode directly affects performance. Verify that your dynamic table uses the
expected mode.

To check refresh mode, use [SHOW DYNAMIC TABLES](../sql-reference/sql/show-dynamic-tables.md) and review the
`refresh_mode` and `refresh_mode_reason` columns. In Snowsight, view the
refresh mode in the object header.

For guidance on choosing the right refresh mode, see [Choose a refresh mode](dynamic-tables-performance-optimize.md).

## Diagnose slow refreshes

When refreshes take longer than expected, follow these steps to identify the cause:

1. Check the refresh history for trends in refresh duration, such as gradual increases or sudden spikes
   ([Monitor the refresh status for your dynamic tables](dynamic-tables-monitor.md)).
2. Review the query profile to identify bottlenecks (Analyze query profiles):

   * High partition scans suggest poor [data locality](dynamic-tables-performance-optimize.md).
   * Bytes spilled suggest that the warehouse is too small.
   * Specific operators taking a long time might indicate an opportunity to [optimize your dynamic table
     query](dynamic-tables-performance-optimize.md).
3. Check whether lag consistently exceeds your target, which indicates that refreshes might not keep up
   with your data volume ([Monitor the refresh status for your dynamic tables](dynamic-tables-monitor.md)).
4. Review upstream dependencies to check whether upstream tables cause delays or produce
   large volumes of changes.

   In the Graph view in Snowsight, look for the following conditions:

   * Upstream tables executing a refresh (shown with `executing` status).
   * Failed or suspended upstream tables.
   * Upstream tables taking longer than usual to refresh.

   To access the Graph view, see [View the graph of tables connected to your dynamic tables](dynamic-tables-monitor.md).
5. Check the volume of changes that the dynamic table processes, because large volumes of changes
   from upstream dependencies can slow down refreshes.

   Use the [DYNAMIC_TABLE_REFRESH_HISTORY](../sql-reference/functions/dynamic_table_refresh_history.md)
   function to see how many rows changed in recent refreshes:

   ```sqlexample
   SELECT
     name,
     data_timestamp,
     statistics:numInsertedRows::INT AS rows_inserted,
     statistics:numDeletedRows::INT AS rows_deleted,
     refresh_action
   FROM TABLE(INFORMATION_SCHEMA.DYNAMIC_TABLE_REFRESH_HISTORY(
     NAME => 'my_dynamic_table'
   ))
   ORDER BY data_timestamp DESC
   LIMIT 10;
   ```

   When change volume is high relative to total table size (more than five percent of the table rows), consider
   using full refresh mode instead.

### Common patterns and recommended actions

* **Refresh duration is stable, but lag is high**: Your target lag is probably too aggressive for
  the current warehouse size and data volume. Refreshes finish successfully but can’t keep up with incoming
  changes. Check whether your [target lag](dynamic-tables-performance-optimize.md) and
  [warehouse resources](dynamic-tables-performance-optimize.md) match your data volume.
* **Refresh duration suddenly spikes and bytes spilled are high**: The warehouse doesn’t have enough memory
  to process the refresh, either because the warehouse is too small or because other queries are running at
  the same time. [Increase the warehouse size](dynamic-tables-performance-optimize.md) or move dynamic table
  refreshes to a dedicated warehouse.
* **Partition scans increase over time, but data volume stays the same**: Your data locality is poor, which
  forces Snowflake to scan more partitions than necessary. Check your
  [clustering keys and data locality](dynamic-tables-performance-optimize.md). Also check whether upstream changes
  affect many scattered partitions instead of a few contiguous ones.
* **Each refresh processes a large portion of the table (more than five percent of rows or partitions)**:
  Incremental refresh provides little benefit when most of the table changes frequently.
  [Switch to full refresh mode](dynamic-tables-performance-optimize.md) or redesign your pipeline to reduce the
  amount of data that changes with each refresh.

Based on your findings, apply appropriate fixes from
[Optimize dynamic table performance](dynamic-tables-performance-optimize.md).

> **Note:**
>
> *Skipped or failed refreshes* are typically caused by configuration issues, not
> performance problems. See [Troubleshooting skipped or failed dynamic table refreshes](dynamic-tables-troubleshoot-refresh.md).

## Analyze query profiles

The [query profile](ui-snowsight-activity.md) shows detailed execution statistics for
each refresh. When a refresh is slow, the query profile helps you identify opportunities for optimization.

To access the query profile:

SnowsightSQL

1. Navigate to Transformation » Dynamic Tables.
2. Select the dynamic table and go to the Refresh History tab.
3. Select Show query profile next to the refresh you want to analyze.

First, get the query ID from refresh history:

```sqlexample
SELECT
  name,
  refresh_start_time,
  query_id
FROM TABLE(INFORMATION_SCHEMA.DYNAMIC_TABLE_REFRESH_HISTORY(
  NAME => 'my_dynamic_table'
))
WHERE state = 'SUCCEEDED'
ORDER BY refresh_start_time DESC
LIMIT 5;
```

Then analyze the query profile with the [GET_QUERY_OPERATOR_STATS](../sql-reference/functions/get_query_operator_stats.md)
function:

```sqlexample
SELECT *
FROM TABLE(GET_QUERY_OPERATOR_STATS('<query_id>'));
```

### What to look for

* **Partitions scanned vs. pruned**: When partition scans are high relative to the total number of partitions,
  the cause is usually poor [data locality](dynamic-tables-performance-optimize.md) or missing clustering.
* **Time distribution**: Check which operators consume the most time. Operators that take
  disproportionately long might indicate an opportunity to optimize your query. See
  [Optimize queries for incremental refresh](dynamic-tables-performance-optimize-query.md) for operator-specific guidance.
* **Bytes spilled to local or remote storage**: High bytes spilled often indicate that the warehouse
  is too small for the refresh workload or that other queries running on the same warehouse
  reduce the memory available for refreshes. Consider [increasing the warehouse size](dynamic-tables-performance-optimize.md)
  or running dynamic table refreshes on a dedicated warehouse to reduce contention.

For more guidance on how to address issues found in the query profile, see
[Optimize dynamic table performance](dynamic-tables-performance-optimize.md).

## Monitor warehouse usage

To check whether your warehouse can handle your dynamic table workload and
find ways to reduce costs, monitor warehouse usage.

### Key metrics to monitor

* **Bytes spilled**: Bytes spilled to local or remote storage means that the warehouse might be too small.
  Consider [increasing warehouse size](dynamic-tables-performance-optimize.md). For more details on identifying
  and troubleshooting bytes spilled, see [Finding queries that spill to storage](performance-query-warehouse-memory.md).
* **Warehouse utilization**: Check whether the warehouse has enough resources for refresh workloads.
  Low utilization means you might have an oversized warehouse. High queue times mean your warehouse
  is too small or runs too many concurrent queries.
* **Query queuing**: Queued queries delay refreshes. If refreshes frequently queue,
  [increase warehouse size](dynamic-tables-performance-optimize.md), use a dedicated warehouse for
  dynamic table refreshes, or consider a multi-cluster warehouse to handle variable workloads.
* **Credit usage**: Track credits to balance performance with costs. Monitor regularly to find
  opportunities to right-size warehouses or adjust refresh schedules.

To view warehouse usage and queue times, see [Reducing queues](performance-query-warehouse-queue.md).
Optimize warehouse configuration for dynamic tables with
[Optimize dynamic table performance](dynamic-tables-performance-optimize.md).

## Monitor dependencies

Dependencies between dynamic tables can affect performance. Performance issues in upstream
tables cascade to downstream tables because a downstream table must wait for upstream tables to
complete their refreshes before it can start its own refresh.

To diagnose performance issues related to upstream dependencies, see
Diagnose slow refreshes.

To view the graph of dependencies, see [View the graph of tables connected to your dynamic tables](dynamic-tables-monitor.md).

## Set up alerts for performance issues

You can set up alerts to notify you when performance degrades. We recommend creating alerts
for the following conditions:

* Refresh duration exceeds a threshold.
* Lag consistently misses the target.

Alerts use event tables to track refresh events. For setup instructions, see
[Event table monitoring and alerts for dynamic tables](dynamic-tables-monitor-event-table-alerts.md).
