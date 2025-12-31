# Source: https://firebase.google.com/docs/database/usage/monitor-performance.md.txt

<br />

There are a few different ways to monitor yourFirebase Realtime Database's performance and spot potential problems in your app. Looking at your app's incoming and outgoing bandwidth and load can also give you an idea of what to expect on your bill. Additionally, if something seems off, getting a clear picture of your database's operations can be a helpful troubleshooting tool.

This page discussesRealtime Databaseperformance monitoring. For usage monitoring, see[Monitor Database Usage](https://firebase.google.com/docs/database/usage/monitor-usage).

## UseRealtime Databasemonitoring tools

You can gather data about yourRealtime Database's performance through a few different tools, depending on the level of granularity you need.

### Use theRealtime Databaseprofiler tool

The[Realtime Databaseprofiler tool](https://firebase.google.com/docs/database/usage/profile)provides a realtime overview of read/write operations on your database. The report includes information about the speed and payload size of each operation, in addition to unindexed queries. It doesn't include historical information or any statistics about connection overhead, however, and**should not be used to estimate billing costs**.

To learn more about using the profiler tool, see[Profile your database](https://firebase.google.com/docs/database/usage/profile).

### Use theFirebaseconsole

The**Usage** tab in the[Firebaseconsole](https://console.firebase.google.com/project/_/database/usage/current-billing/bandwidth)offers information about simultaneous connections to your database, how much data you're storing, outgoing bandwidth (including protocol and encryption overhead), and your database's load over 1-minute intervals. While the**Usage**tab gives you a more accurate overview of your database's overall performance, you might not be able to drill down enough to troubleshoot potential performance issues.

### UseCloud Monitoring

WithCloud MonitoringfromGoogle Cloud, you can use the Metrics Explorer to see individual performance metrics, or create different dashboards with charts that display various combinations of performance metrics over time. TheRealtime Databaseintegration withCloud Monitoringoffers the deepest level of granularity.

The steps for setting upCloud Monitoringare described in[Monitor Database Usage](https://firebase.google.com/docs/database/usage/monitor-usage#stackdriver-setup).

See the following sections for tips on using specificCloud Monitoringmetrics to spot performance issues.

## Monitor performance inCloud Monitoring

If you're experiencing issues with performance, including uptime or latency, you might want to useCloud Monitoringto monitor the following metrics. Note all metric type names are prefixed with`firebasedatabase.googleapis.com/`.

|          Metric Name          |                                                                                                                                                                                                                                                                                    Description                                                                                                                                                                                                                                                                                    |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Database Load                 | `io/database_load`. Use this metric to monitor how much of your available database bandwidth is in use processing requests over time. You might see performance issues as your database load approaches the total available bandwidth. You can also see which operation types are utilizing the most load, and troubleshoot accordingly. Reported load might exceed 100% on operations that take longer than a minute. This happens when the total bandwidth used across multiple minutes is condensed into the minute-long reporting interval after the operation has completed. |
| Network Disabled for Overages | `network/disabled_for_overages`. This metric reflects any outages that might have occurred if yourRealtime Databaseexceeded any bandwidth or network limits.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Storage Disabled for Overages | `storage/disabled_for_overages`. This metric reflects any outages that might have occurred if yourRealtime Databaseexceeded any storage limits.                                                                                                                                                                                                                                                                                                                                                                                                                                   |

Combine metrics in charts on your dashboard for helpful insights and overviews. For example, try the following combinations:

- **Operations:** Use the`io/database_load`metric to see how much of your total database load is used by each operation type. Make sure to group`io/database_load`by type to troubleshoot different operation types.
- **Storage:** Use the`storage/limit`and`storage/total_bytes`to monitor your storage utilization in relation to theRealtime Databasestorage limits. You can also add`storage/disabled_for_overages`to see if your app experienced any down time as a result of exceeded storage limits.
- **SSL overhead:** Use`network/https_requests_count`to monitor how many SSL connection requests your database received, and split out requests that reused an existing SSL session ticket with the`reused_ssl_session`filter. You can measure this against the`network/sent_bytes_count`and`network/sent_payload_and_protocol_bytes_count`to monitor whether or not your app is using SSL session tickets efficiently.

You can also set up[alerts](https://firebase.google.com/docs/database/usage/monitor-usage#stackdriver-alert-setup)throughCloud Monitoringand receive notifications based onRealtime Databasemetrics. For example, you can choose to receive a notification if your`io/database_load`is approaching a certain threshold.

See the[full list ofRealtime Databasemetrics available throughCloud Monitoring](https://cloud.google.com/monitoring/api/metrics_gcp_d_h#gcp-firebasedatabase).

### Database Load Types

The`io/database_load`metric also provides a label of which operation type caused the load. The following are the possible types of operations measured:

- `admin`: Admin operations like setting rules and reading project metadata.
- `auth`: Verifying authentication from service accounts or Firebase Authentication for a single client.
- `client_management`: Handling the addition and removal of concurrent connections this includes running disconnect operations on removal.
- `get_shallow`: Retrieving the data from a REST GET with`shallow=true`.
- `get`: Handling REST GET operations.
- `listen`: Retrieving the initial data for`on`and`once`operations from connected clients.
- `on_disconnect`: Registering on disconnect operations from clients.
- `put`: Handling`set`operations from clients or REST PUT operations.
- `transaction`: Performing transactions from conditional REST requests or a`transaction`operation from a client.
- `update`: Handling`update`operations or REST PATCH requests.

## Monitor Security Rules inCloud Monitoring

You can also analyze evaluation of Security Rules. Note all metric type names are prefixed with`firebasedatabase.googleapis.com/`.

|   Metric Name    |                                                                                                    Description                                                                                                    |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rule evaluations | `rules/evaluation_count`. The number of Realtime Database Rules evaluations performed in response to write or read requests. You can break this metric down by the result of the request (ALLOW, DENY, or ERROR). |

Tailor yourCloud Monitoringchart for Rules evaluations as needed, for example by filtering on particular evaluation results, ALLOW, DENY, or ERROR. Setting up and customizing charts is covered in[Monitor Database Usage](https://firebase.google.com/docs/database/usage/monitor-usage#stackdriver-add-chart).

See the[full list ofRealtime Databasemetrics available throughCloud Monitoring](https://cloud.google.com/monitoring/api/metrics_gcp_d_h#gcp-firebasedatabase).