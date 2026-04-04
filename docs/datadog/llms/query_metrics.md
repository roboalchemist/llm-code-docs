# Source: https://docs.datadoghq.com/database_monitoring/query_metrics.md

---
title: Exploring Query Metrics
description: Explore and dig into your database and query performance metrics
breadcrumbs: Docs > Database Monitoring > Exploring Query Metrics
---

# Exploring Query Metrics

The Query Metrics view shows historical query performance for normalized queries. Visualize performance trends by infrastructure or custom tags such as data center availability zone, and get alerted for anomalies.

Navigate to [the Query Metrics page](https://app.datadoghq.com/databases/queries) in Datadog.

The view shows 200 *top* queries, that is the 200 queries with the most total time running in the selected time frame. See [which queries are tracked](https://docs.datadoghq.com/database_monitoring/data_collected/#which-queries-are-tracked) for more details. Metrics aggregation for one-off or seldom-run fast queries isn't shown in the Query Metrics view, but you can find snapshots of them represented in [Query Samples](https://docs.datadoghq.com/database_monitoring/query_samples/), if they have run in the last 15 days.

## Filtering and grouping{% #filtering-and-grouping %}

Select your database source (for example, Postgres) from the **source** selector at the top. Specify search tags to filter the list of queries (or list of [stored procedures](https://docs.datadoghq.com/database_monitoring/database_hosts/#stored-procedures), where available), and group by tags to organize the list.

For example, it's often useful to group by host or cluster, to quickly see what infrastructure the queries are running on.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm-qm-group-by-2.1cc70f95c5a04e28f7e37e7908fbbdb0.png?auto=format"
   alt="Group by env tag" /%}

You can group by up to three things (for example, host, env, and datacenter) to get grouped sets of filtered results.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm-qm-group-by-three-2.a046344b5ff268a22416cb9ed8469a3e.png?auto=format"
   alt="Grouping by three tags" /%}

Expand the group to see the list of queries, and click **View all queries in this group** to move that group-by criteria into the Search field in the filter bar, filtering the page content to that search result.

## Filtering by facets{% #filtering-by-facets %}

On the left side of the view are lists of facets for filtering the list of queries. The facets include:

- **Core**: Services, hosts, environments.
- **Database**: Postgres has `database` and `user` facets. MySQL has `schema` facets.
- **Infrastructure**: Traditional Datadog infrastructure tags collected by the Agent.

Select or clear facets to find the list of queries you're interested in.

### Filtering the Query Metrics view to a single query{% #filtering-the-query-metrics-view-to-a-single-query %}

If you want to filter the contents of the Query Metrics view to just one [normalized query](https://docs.datadoghq.com/database_monitoring/data_collected/#normalized-queries), filter on the `query_signature`, not `query`. Tag names are truncated at 200 characters, and because queries can be long, their `query` tags aren't necessarily unique. The `query_signature` is a hash of a normalized query and serves as a unique ID for the normalized query.

One way to filter to a specific query without looking up its query signature value is to click the query from the list. This opens its Query Details page, where you click **Filter to This Query**. This filters the Query Metrics page by the `query_signature` facet.

## Exploring the metrics{% #exploring-the-metrics %}

The Query Metrics list shows Requests, Average latency, Total time, and Percent time metrics, plus others that depend on your database product. Click the **Options** menu to control which metrics are displayed in the list. Hover over the column heading to see a description for each type of metric. Click the column heading to sort the list by that metric.

To see a complete list of metrics collected, see the integration Data Collected documentation for your database product:

- [Postgres](https://docs.datadoghq.com/integrations/postgres/#data-collected)
- [MySQL](https://docs.datadoghq.com/integrations/mysql/#data-collected)
- [SQL Server](https://docs.datadoghq.com/integrations/sqlserver/#data-collected)
- [Oracle](https://docs.datadoghq.com/integrations/oracle/#data-collected)
- [Oracle](https://docs.datadoghq.com/integrations/mongodb/#data-collected)



The metrics used for Database Monitoring views are, primarily:

- **MySQL**: `mysql.queries.*`
- **Postgres**: `postgresql.queries.*`
- **SQL Server**: `sqlserver.queries.*`
- **Oracle**: `oracle.queries.*`

## Query details page{% #query-details-page %}

When you click a query in the Query Metrics list, the Query Details page for that query opens. The top of the page shows the full text of the [normalized query](https://docs.datadoghq.com/database_monitoring/data_collected/#normalized-queries), and a list of all tags associated with the query. The list of tags is the union of all tags from each host that the query runs on. Browse the list to see information such as what server the query is running on:

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_qd_tags.2af3fec11d1daa57eae5959513bb18fb.png?auto=format"
   alt="Tags list for a query" /%}

Stay in the context of this query and navigate to the [Query Samples page](https://docs.datadoghq.com/database_monitoring/query_samples/) with the **View Query Samples** button, or back to Query Metrics filtered by this query with the **Filter by This Query** button.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_qd_jump_buttons.bfdf466ec054ef2e829719c4f273d5da.png?auto=format"
   alt="Quickly see query sample or metrics for this query" /%}

When you're looking at a query's details and want to find the hosts it's running on, click **Filter by This Query** and then group by hosts. The metrics list shows each host the query is running on. Sort by **Percent time** to see if a particular host is responsible for a large percentage of a query's execution.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_qm_by_host_usecase.47a12764151b1e9069ef9fedde24e93b.png?auto=format"
   alt="A query's metrics grouped by host" /%}

Sort by **Rows/Query** to see if a particular host tends to return a lot more rows, indicating that sharding is unbalanced across the hosts.

### Metrics graphs{% #metrics-graphs %}

The graphs show metrics for this query compared to all queries except this query. Maybe this query's average latency is a lot higher than the average of other queries, but also it is executed infrequently so its total impact is minor. You can see how much of the database's time it is consuming when it does run, compared to all other queries.

Click the **Metrics** tab to see more graphs of metrics for this query.

### Explain plans{% #explain-plans %}

Datadog collects explain plans continuously, so a given query can have multiple plans. Those plans are normalized and shown separately so that you can see if a query has plans that perform better or have higher relative cost than others. For example, the following explain plan contains information for a query:

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm-qd-explain-plans-2.6d86532ee5b560d1686c9e4c6d07936e.png?auto=format"
   alt="Explain plans information for a query" /%}

Select a plan to see cost metrics or its JSON. Click **View All Samples for This Plan** to navigate to Query Samples view for [the samples associated with it](https://docs.datadoghq.com/database_monitoring/query_samples/#sample-details).

Not all queries have explain plans, for various reasons, including what type of query it is, or various configuration settings. See [Troubleshooting](https://docs.datadoghq.com/database_monitoring/troubleshooting/#queries-are-missing-explain-plans) for more details.

### Hosts running this query{% #hosts-running-this-query %}

The **Hosts Running This Query** tab lists the hosts that run this query, with a context menu that lets you navigate to related information for the hosts, such as logs or the network data, which can be useful for troubleshooting where latency problems are coming from.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_qd_hosts_running_query_menu.ed7e28b58db326c6a4d688e7a207ca23.png?auto=format"
   alt="Host action menu for pivoting to more information" /%}

## Database Monitoring dashboards{% #database-monitoring-dashboards %}

For quick access to dashboards that showcase database-related infrastructure and query metrics visualizations, click the **Dashboards** link at the top of the page. Use the out-of-the-box dashboards, or clone and customize them to suit your needs.

## Further Reading{% #further-reading %}

- [Database Monitoring](https://docs.datadoghq.com/database_monitoring/)
- [Postgres integration](https://docs.datadoghq.com/integrations/postgres/)
- [MySQL integration](https://docs.datadoghq.com/integrations/mysql/)
- [SQL Server integration](https://docs.datadoghq.com/integrations/sqlserver/)
- [Oracle integration](https://docs.datadoghq.com/integrations/oracle/)
- [Data Collected](https://docs.datadoghq.com/database_monitoring/data_collected/)
- [Troubleshooting](https://docs.datadoghq.com/database_monitoring/troubleshooting/)
