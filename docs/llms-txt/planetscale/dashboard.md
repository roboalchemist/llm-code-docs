# Source: https://planetscale.com/docs/postgres/dashboard.md

# PlanetScale Postgres database dashboard

> When you navigate to a database in your PlanetScale organization, you'll see a comprehensive view of your cluster health, performance metrics, and management options. You can filter this view by [branch](/docs/postgres/branching) by selecting from the branch dropdown at the top.

From the dashboard you can review:

* Your cluster's topology diagram
* Real-time performance metrics
* Summary and statistics
* Connection management
* Branch-specific views and controls

## Cluster topology

The cluster topology diagram provides a visual representation of your PostgreSQL database infrastructure, including:

* **Primary node**: The main database instance that handles all write operations
* **Replica nodes**: Read-only copies of your primary database for improved read performance and high availability

Each node includes information about the region, instance type, real-time resource utilization (CPU and memory percentage), and cluster size.

If you had additional replicas beyond the 2 default, you'll see them in this diagram.

## Database summary

The database summary section on the right-hand side displays key statistics about your PostgreSQL environment, including:

* **PostgreSQL version**: Shows the current PostgreSQL version (e.g., "17.4")
* **Tables**: Total number of tables across all schemas
* **Branches**: Count of database branches in your environment
* **CPU utilization**: Percentage of CPU currently used
* **Next backup**: Shows when the next scheduled backup will occur (e.g., "in 8 hours")
* **Total storage**: Amount of storage currently used

Production branches are clearly marked with visual indicators and badges to distinguish them from development branches. The summary also shows the current state and health of each branch, making it easy to assess your database environment at a glance.

## Performance metrics

The performance metrics section includes a dropdown to select different metrics and a time-series graph showing data over the selected time period. Available metrics include:

* Query latency (shown as p95, p99, p50, and p99.9 percentiles)
* Queries per second
* Rows read
* Rows written
* Query errors

You can select each metric from the dropdown to update the graph. There's also a "View all query insights" link to access more detailed query performance data.

### Slowest queries

The "Slowest queries during the last 24 hours" section at the bottom of the dashboard shows a detailed table with:

* **Query**: The actual SQL query text
* **Count**: Number of times the query was executed
* **p50 latency (ms)**: The median query execution time in milliseconds

This helps you identify performance bottlenecks and queries that may need optimization.

## Connecting to your database

The "**Connect**" button allows you to generate or reset your default credentials for your Postgres database. For more information, see the [Connecting documentation](/docs/postgres/connecting).

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt