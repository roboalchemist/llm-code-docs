# Source: https://fly.io/docs/mpg/metrics/

Title: Monitoring and Metrics

URL Source: https://fly.io/docs/mpg/metrics/

Markdown Content:
[Docs](https://fly.io/docs/)[Managed Postgres](https://fly.io/docs/mpg)Monitoring and Metrics![Image 1: Illustration by Annie Ruygt of a balloon doing a lot of tasks](https://fly.io/static/images/Managed_Postgres.png)
[](https://fly.io/docs/mpg/metrics/#performance-monitoring)Performance Monitoring
---------------------------------------------------------------------------------

The Managed Postgres dashboard provides comprehensive performance monitoring and metrics for your PostgreSQL clusters. The **Metrics** tab gives you real-time visibility into your database’s performance, helping you identify bottlenecks and optimize your applications.

### [](https://fly.io/docs/mpg/metrics/#accessing-metrics)Accessing Metrics

To view metrics for your cluster:

1.   Navigate to your MPG cluster in the Fly.io dashboard 
2.   Click the **Metrics** tab 
3.   Optionally filter by specific database using the database dropdown 
4.   Select your desired time range (15 minutes, 1 hour, 6 hours, 24 hours, or 2 days) 

### [](https://fly.io/docs/mpg/metrics/#available-charts-and-metrics)Available Charts and Metrics

The metrics dashboard provides detailed insights through various charts and gauges organized into categories:

#### [](https://fly.io/docs/mpg/metrics/#system-resource-metrics)System Resource Metrics

| Metric | Description |
| --- | --- |
| **Database CPU Utilization** | CPU usage percentage for each database instance, labeled with Primary (P) and Replica ® badges. Shows individual instance IDs and averages over the selected time period |
| **Database Memory Utilization** | Memory usage for Primary and Replica database instances. Displays current usage and average consumption per instance |
| **Pooler CPU Utilization** | CPU usage percentage for PGBouncer connection pooler instances. Typically remains low under normal operations |
| **Pooler Memory Utilization** | Memory consumption in MB for connection pooler instances. Shows usage for each pooler with instance IDs |

#### [](https://fly.io/docs/mpg/metrics/#connection-metrics)Connection Metrics

| Metric | Description |
| --- | --- |
| **Database Connections** | Shows active and idle database connections over time |
| **Pooler Connections** | Tracks active and waiting connections through PGBouncer |
|  |  |

#### [](https://fly.io/docs/mpg/metrics/#database-operations)Database Operations

| Metric | Description |
| --- | --- |
| **Database Operations** | Row-level operations per second broken down by type (inserts, updates, deletes, and fetches). Shows throughput patterns and workload distribution across operation types |
| **Cache Hit Ratio** | Percentage of data requests served from memory versus disk. Higher percentages (95%+) indicate efficient memory usage. Lower values suggest queries are hitting disk frequently |
| **Deadlocks** | Count of database deadlocks detected when two or more transactions are waiting for each other to release locks. Shows frequency and timing of these mutual blocking situations |

#### [](https://fly.io/docs/mpg/metrics/#storage)Storage

| Metric | Description |
| --- | --- |
| **Database Size** | Current storage usage across databases |

#### [](https://fly.io/docs/mpg/metrics/#replication-metrics)Replication Metrics

| Metric | Description |
| --- | --- |
| **Replication Delay Bytes** | Amount of WAL (Write-Ahead Log) data in bytes that the replica is behind the primary. Measures the volume of changes waiting to be applied |
| **Replication Delay Seconds** | Time in seconds that the replica lags behind the primary database. Represents how long ago the replica’s current state reflects the primary |
