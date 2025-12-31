# Source: https://planetscale.com/docs/vitess/monitoring/query-insights.md

# Source: https://planetscale.com/docs/postgres/monitoring/query-insights.md

# Query Insights

> PlanetScale Insights gives you a detailed look into **all active queries** running against your database.

export const YouTubeEmbed = ({id, title}) => {
  return <Frame>
      <iframe src={`https://www.youtube-nocookie.com/embed/${id}?rel=0`} title={title} className="aspect-video w-full" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" />
    </Frame>;
};

## Overview

This in-dashboard tool allows you to identify queries that are running too often, too long, returning too much data, producing errors, and more. You can scroll through the performance graph to detect the time of impacted performance, quickly identifying any recent issues.

You can also see a [list of all queries](#queries-overview) performed on your database in the last 24 hours. For further analysis, you can sort these by metrics like amount of rows read, time per query, and more.

With this built-in tool, you can easily diagnose issues with your queries, allowing you to optimize individual queries without much digging. We will also alert you of any active issues your database may be having in the [Anomalies](/docs/postgres/monitoring/anomalies) tab. This feature flags queries that are running significantly slower than expected.

<YouTubeEmbed id="4ymmF-Fedcw" title="Data drop: Query Insights for Postgres" />

## Insights page overview

To view Insights for your database, head to the [PlanetScale dashboard](https://app.planetscale.com), select your database, and click the "**Insights**" tab.

The dropdown on the top right lets you select which branch you want to analyze. You can also choose which servers you want to view insights for: primary or replicas.

<Frame><img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/monitoring/query-insights-overview.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=2e54ec60ade18a3f2221e09e6496a19e" alt="PlanetScale Insights overview page" data-og-width="2892" width="2892" data-og-height="1736" height="1736" data-path="docs/postgres/monitoring/query-insights-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/monitoring/query-insights-overview.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=37532bfb9291a19c8ed5b5b682912193 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/monitoring/query-insights-overview.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=ae56ab37d1558387e9fd6b8550e8e314 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/monitoring/query-insights-overview.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=027741ef2aac0a500abf6dafe9f13168 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/monitoring/query-insights-overview.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=4b699ef96388c6af389df52e1f4ca86e 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/monitoring/query-insights-overview.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=4e4703a4ba2a49bd4f28a16a82033032 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/monitoring/query-insights-overview.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=bc997b20fd142523983164c113f6b0b7 2500w" /></Frame>

You can click the dates listed above the graph to scroll through the past seven days. To further narrow down query analysis, you can select a time range by clicking on the graph and dragging the cursor across. This will zoom in on the selected timeframe.

You also have the option to save a screenshot of the graph by clicking "Save".

### Queries overview table

The table underneath the graph shows all queries performed on your database in the selected timeframe (last 24 hours by default).

For more information about how to read and interpret this data, see the [Queries overview](#queries-overview) section.

### Insights graph tabs

Once you have selected the branch and server you want to analyze, you can begin exploring the insights for them in the following tabs:

<Columns cols={2}>
  <Card title="Query latency" icon="code" horizontal href="#query-latency" />

  <Card title="Anomalies" icon="triangle-exclamation" horizontal href="/docs/postgres/monitoring/anomalies" />

  <Card title="Queries" icon="code" horizontal href="#queries" />

  <Card title="Rows read" icon="code" horizontal href="#rows-read" />

  <Card title="Rows written" icon="code" horizontal href="#rows-written" />

  <Card title="Errors" icon="circle-exclamation" horizontal href="#errors" />
</Columns>

The remaining sections of this doc walk through how to interpret and act on the data in each tab. If you'd like to see a practical example of how to use Insights to debug a performance issue, check out our [Announcing Insights blog post](https://planetscale.com/blog/introducing-planetscale-insights-advanced-query-monitoring) or [this YouTube video](https://www.youtube.com/watch?v=kkjAxSViOAA) walking you through an example.

## Query latency

The default tab depicts your database's query latency in milliseconds over the last 24 hours.

By default, the graph contains two line charts showing `p50` and `p95` latency. This means 50% and 95% of requests, respectively, completed faster than the time listed. You can also click on the `p99` and `p99.9` pills to toggle those on, or click `p50` or `p95` to toggle those off.

## Queries

The Queries tab displays insights about all active running queries in your database. The graph displays total queries per second against the specified time period.

## Rows read

The Rows read tab displays the total number of rows read per second across the selected time period.

## Rows written

The Rows written tab displays the total number of rows written per second across the selected time period.

## Errors

The Errors tab surfaces any errors that have been captured on your database in a 24 hour period.

Underneath the graph, you'll find a list of database error messages that have been captured over the selected period.

You can click on any of the error messages on the Errors tab to open a more detailed view. This view shows you the individual queries that produced the error, when they ran, how long they ran, and any query tags attached to them.

## Queries overview

The table underneath the graph shows queries performed on your database in the selected timeframe (last 24 hours by default).

<Note>
  The queries table does not show following statements types: `BEGIN`, `COMMIT`, `RELEASE`, `ROLLBACK`, `SAVEPOINT`, `SAVEPOINT_ROLLBACK`, `SET`.
</Note>

Queries are listed with literals replaced by ordinal placeholder values (e.g. `$1`). Normalizing queries in this way allows them to be grouped together into patterns, irrespective of the specific parameters used in the underlying query.

You may also see one or more orange icons next to some queries.

* An exclamation point icon indicates that the query is not currently using an index and requires a full table scan.

Hovering over the icon will show a tooltip with information about the meaning of the icon.

The query overview table shows the same data for all graph tabs except for [Anomalies](/docs/vitess/monitoring/anomalies) and [Errors](#errors). For more information about the content for each of those, refer to each Anomalies and Errors sections above.

### Available query statistics

You can customize the metrics that show up on the Queries list by selecting columns in the "View options" dropdown.

* **Query** - The query that was run.
* **Schema** - The default database and schema associated with the connection that issued the query, in the format `database.schema`.
* **Qualified table** — The table(s) referenced in the query, in the format `database.schema.table_name`.
* **Table schema** — The schema(s) associated with the tables referenced in the query, in the format `database.schema`. (This may differ from the connection schema.)
* **Table** — The table(s) being queried or modified.
* **% of runtime** — The percent of the total runtime the query pattern is responsible for (query pattern time divided by the cumulative time of all query patterns on your database).
* **% of CPU** — The percent of the total CPU time the query pattern is responsible for (query pattern CPU time divided by the cumulative CPU time of all query patterns on your database).
* **% of I/O** — The percent of the total I/O time the query pattern is responsible for (query pattern IO time divided by the cumulative IO time of all query patterns on your database). This column is only present if `track_io_timing` parameter is set in your database's cluster configuration.
* **Count** — The number of times this query has run.
* **Total time (s)** — The total time the query has run in seconds.
* **CPU time (s)** — The cumulative CPU time the query has consumed in seconds.
* **I/O time (s)** — The cumulative I/O time the query has consumed in seconds. This column is only present if `track_io_timing` parameter is set in your database's cluster configuration.
* **`p50` latency** — The `p50` latency for the query in milliseconds. This means that 50% of requests completed faster than the time listed.
* **`p99` latency** — The `p99` latency for the query in milliseconds. This means that 99% of requests completed faster than the time listed.
* **Max latency** — The maximum observed latency for the query in milliseconds.
* **Rows returned** — The total number of rows fetched by a `SELECT` statement. This includes all times the query has run in the displayed time frame.
* **Rows read** — The total number of rows read. This includes all times the query has run in the displayed time frame.
* **Rows read/rows returned** — The result of dividing total rows read by rows returned in a query. A high number can indicate that your database is reading unnecessary rows, and the query may be improved by adding an index.
* **Rows affected** — The total number of rows modified by an `INSERT`, `UPDATE`, or `DELETE` statement. This includes all times the query has run in the displayed time frame.
* **Block cache hit ratio** – The percentage of blocks read from the shared buffers cache for this query during its execution, avoiding more costly disk reads.
* **Blocks hit** – The total number of blocks read from the shared buffers cache when executing this query.
* **Blocks read** – The total number of blocks read from disk when executing this query.
* **Blocks dirtied** – The total number of blocks modified (but not necessarily flushed to disk) during query execution.
* **Blocks written** – The total number of blocks written to disk during query execution.
* **Bytes returned** – The total number of bytes returned to clients in query responses.
* **Bytes returned per query** — The total number of bytes returned to clients in query responses divided by the number of queries.
* **Last run** — The last time a query was run.

You can also sort the columns for quick analysis by clicking on the title at the top of each column.

If `Show sparklines` is selected, numeric columns in the queries table show a time series graph of the value within the selected time period.

#### Enabling I/O columns

The **% of I/O** and **I/O time** columns require the `track_io_timing` PostgreSQL config setting to be set to 'on'. This setting can be changed in the "Parameters" tab of the datatbase's cluster configuration. Note that we only begin collection I/O query performance after `track_io_timing` is enabled. Enabling `track_io_timing` may impact query performance.

### Query filtering

The search bar above the table allows you to filter queries as needed. You can filter for query SQL, schema (connection schema, and/or schema of tables referenced by the query), table name, query count, query latency, index name, and if the query was indexed. Click on the `?` next to the search bar for the full list of search syntax.

### Query deep dive

Clicking on a query in the Queries list will open a new page with more information about that query.

You'll first see the full query pattern, which displays the query with data normalized away. This query may run several times with different values, which Insights combines into a single query pattern.

You can display an LLM-generated summary of the query by clicking "Summarize query."

#### Additional query information

Beneath the query pattern is a graph with more information about the query. The set of available metrics/tabs include: Query latency, Queries, Rows read, Rows written, Errors and Indexes. The Indexes graph (which is not shown on the database-level page) shows the percentage of queries that used each of the listed indexes in each time bucket.

Beneath the time series graphs you will see summary statistics for the query pattern. These data are scoped to the same time period shown in the main query pattern graphs. The available metrics have the same definitions as the query statistics listed in the main insights tab.

Queries that use an index include a horizontal bar graph that shows the cumulative usage of each index over the complete time period shown in the main query pattern graphs.

To change the time period reflected in the graphs and summary statistics, click and drag to restrict the time window, or click on one of the day icons above the graph to select a different day.

#### Notable queries

Underneath the graph, you'll see a table with more information about notable instances of the query, which are defined as queries that took longer than 1s, read more than 10,000 rows, or produced an error.

If any of the selected queries have [SQL comment tags](https://google.github.io/sqlcommenter/) attached, you'll see the key-value pairs in the table under `Tags`.

The table also surfaces when the query started, rows returned, rows read, rows affected, the time it took the query to run (in ms), and the user associated with the query.

## Extension configuration

This section describes the configuration parameters available for the `pginsights` extension, which is responsible for sending query telemetry to the PlanetScale Insights pipeline. These settings can be changed in the Extensions tab on your database's Clusters page.

### Raw query collection

* **Setting:** `pginsights.raw_queries`
* **Default:** `false` (disabled)

When enabled, Insights collects the full query text for notable queries, including all literal values. When disabled, only the normalized SQL, with literals removed, will be collected.

Enabling complete query collection can be helpful when performance varies significantly within the same query pattern, and you need to see the full SQL statement without placeholders to troubleshoot the underlying issue.

<Note>
  Enabling this setting may result in sensitive data that appears in queries being sent to PlanetScale, where it will be processed and stored in accordance with our privacy policy.
</Note>

### Schema name normalization

* **Setting:** `pginsights.normalize_schema_names`
* **Default:** `false` (disabled)

When enabled, [schema](https://www.postgresql.org/docs/current/ddl-schemas.html) names appearing in queries are normalized as if they were literal values.

Consider the following example query: `select * from myschema.users where id = 1`.

* With `pginsights.normalize_schema_names` set to false, the query will be reported in insights as `select * from myschema.users where id = $1`
* With `pginsights.normalize_schema_names` set to true, the query will be reported in insights as `select * from $1.users where id = $2`

This setting is useful for databases using a schema-per-tenant design, where each user or tenant's data is stored in an isolated Postgres schema. With this feature enabled, query patterns that are identical except for the namespace will be grouped together, resulting in fewer distinct query patterns and more navigable insights. If you are concerned that performance problems may be isolated to only particular schemas, we recommend enabling the `pginsights.raw_queries` setting so that the full query text (including namespaces) is reported along with slow queries.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt