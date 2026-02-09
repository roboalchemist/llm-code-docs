# Source: https://docs.datadoghq.com/database_monitoring/query_samples.md

---
title: Exploring Query Samples
description: Get information about queries currently running and find problematic outliers
breadcrumbs: Docs > Database Monitoring > Exploring Query Samples
---

# Exploring Query Samples

The [Samples page](https://app.datadoghq.com/databases/samples) helps you understand which queries were running at a given time. Compare each execution to the average performance of the query and related queries.

The Samples page shows a snapshot in time of running and recently finished queries. Because it's a snapshot in time, it doesn't necessarily show a representation of *all* queries, but can indicate proportions.

## Search and filter{% #search-and-filter %}

The Samples page shows queries on all supported database products together (unlike on the Query Metrics page where you select which database you want to dive into). Filter on the `source` facet to see data for a particular database (Postgres or MySQL).

Enter tags into the Search field to filter the list of query samples, or use the facets listed on the left side. The facets include:

- **Core**: Services, database product sources (Postgres or MySQL), host, and duration.
- **Network**: Client IP address and ports for applications or proxies that connect to the database.
- **Database**: Database names, an explain plan cost slider, indexes, a row count slider for the number of rows returned or affected by queries, query statements, and users.
- **Postgres and MySQL specific facets**

Click **Options** to add columns to the table. Click on column headers to sort by a particular metric.

### Explain plan cost{% #explain-plan-cost %}

Explain plan cost is a unitless measure that the database uses to compare two plans with each other. It roughly corresponds to number of *things* on the databaseâblocks or pagesâbut it is primarily useful for relative comparisons of two plans, not in absolute terms for a single plan. Explain plan cost calculation helps the database choose which plan it's going to use.

The Query Samples page lets you filter, sort, and compare the explain plan costs of multiple queries. In this context, explain plan cost is not to be taken absolutely. A query with an explain plan cost of 8.5 is not necessarily performing better than one with a cost of 8.7. But if two queries have vastly different costs when you'd expect them to be similar, it can be beneficial to investigate why. Also, you can sort your queries by cost to see what your expensive queries are, separate from external factors like network latency.

### Indexes{% #indexes %}

You can filter queries that have explain plans by database index, so you can see which queries are using a specific index. Alternatively, you can find infrequently used indexes by selecting a long time frame such as a week (so a good representation of query samples over time), and looking at least used indexes (the lowest number in the list of index facets). You can then consider whether the performance gained from having that index is worth the cost of keeping it in the database.

### Row count{% #row-count %}

Filter or sort to find queries that return or affect a large number of rows, over the time frame selected.

### Duration{% #duration %}

Filter or sort to find queries that take the longest to run over the time frame selected. If you're looking to optimize your overall performance, you can track down the owner of these slow queries and discuss improving them.

### Sample details{% #sample-details %}

Click on a query in the table to open its Sample Details page. Use the Source, Host, and Client IP tiles at the top to filter the Sample Queries page by the values for this sample, or to navigate to other Datadog information such as the host's dashboard or Network traffic metrics for the client IP.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_sd_actions.7ee020748834b8a28b07d02f5e65e6e0.png?auto=format"
   alt="Sample details action tiles" /%}

For example, by opening the Network traffic page and grouping by service, you can see what service is running the query from that IP.

Graphs show the query's performance metricsânumber of executions, duration, and rows per queryâover the specified time frame *if it is a [top query](https://docs.datadoghq.com/database_monitoring/data_collected/#which-queries-are-tracked)*, with a line indicating the performance for the sample snapshot you're looking at. If metrics aren't available because it's not a top query, the graphs are blank.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_sd_graphs.225e05c2752b055f73ceb23a40d14a0b.png?auto=format"
   alt="Query performance metrics graphs with This Query indicator" /%}

The Explain Plan section shows Duration and Cost stats for the current sample *and* averages and p90 for all collected snapshots across the time frame.

The explain plan also shows measures for each node (step) in the plan: startup cost, total cost, plan rows, and plan width. Hover over the column heading to see a description of each measure.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_sd_explain_plan.a387f0bca934d5eb9a1ed90a80b4da19.png?auto=format"
   alt="Explain plan samples statistics and step metrics" /%}

## Explore other visualizations{% #explore-other-visualizations %}

Besides the default list view, you can view query samples data as timeseries, top lists, or tables by clicking one of the **Visualize as** buttons. This can bring to light powerful ways of looking at the data. For example, to see the slowest queries running in a data center, select **Timeseries**, group by `Statement` and graph the average duration:

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_qs_timeseries_viz.d0ce27bcec4d4a904290320e6092cf56.png?auto=format"
   alt="Finding slowest queries" /%}

Or find an outlier such as a query that *usually* runs quickly, but occasionally runs slowly by graphing its p90 or p99 duration.

Use table visualizations to produce report-like summaries to share with others. For example, create a table of worst-performing queries (p75 Duration), and include the average plan cost values for each query:

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_qs_p75_duration_table.dc3b166271222663374a28a170539f8c.png?auto=format"
   alt="Table of p75 duration queries" /%}

Use the **Export** button to share the data with your engineering team to start a discussion about where to focus improvement efforts.

## Database Monitoring dashboards{% #database-monitoring-dashboards %}

For quick access to dashboards that showcase database-related infrastructure and query metrics visualizations, click the **Dashboards** link at to top of the page. Use the out-of-the-box dashboards, or clone and customize them to suit your needs.

## Further Reading{% #further-reading %}

- [Database Monitoring](https://docs.datadoghq.com/database_monitoring/)
- [Data Collected](https://docs.datadoghq.com/database_monitoring/data_collected/)
- [Troubleshooting](https://docs.datadoghq.com/database_monitoring/troubleshooting/)
