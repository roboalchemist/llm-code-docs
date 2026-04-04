# Source: https://docs.anyscale.com/services/monitoring.md

# Source: https://docs.anyscale.com/monitoring.md

# Monitor and debug Anyscale workloads

[View Markdown](/monitoring.md)

# Monitor and debug Anyscale workloads

After launching your Ray application, you can rely on Anyscale's observability tools to monitor performance and debug issues. This section provides an introduction to the available dashboards and debugging tools.

For more details on monitoring and debugging Anyscale workspace, jobs, or services, see the following pages:

* [Debug in workspaces](/platform/workspaces/workspaces-debugging.md)
* [Monitor a job](/jobs/monitor.md)
* [Monitor a service](/services/monitoring.md)

## Monitoring[​](#monitoring "Direct link to Monitoring")

In the top navigation menu, you find tabs for a few different dashboards. You may already be familiar with the Ray Dashboard, which you can use to view the cluster's state and the progress of submitted Ray Jobs. Anyscale's dashboards expand upon the Ray Dashboard to provide more details on your clusters and workloads.

The usual starting point for monitoring is the Metrics tab. Here you find hardware metrics like the number of nodes and the available memory. If you want to further dive into the data, click **View in Grafana** to open the metrics directly in Grafana. From there, you can also build custom data visualizations to monitor your applications. See [Metrics](/monitoring/metrics.md).

Aside from the general Metrics dashboard, Anyscale also provides dashboards for specific Ray Workloads like Ray Data and Ray Train. See [Workload dashboards](/monitoring/workload-debugging.md).

![The Metrics dashboard](/assets/images/monitor-metrics-c73c5930d3b1f151fb2ffb3f3ba43886.png)

## Debugging[​](#debugging "Direct link to Debugging")

To debug issues with your application, you can rely on the Logs view. Anyscale splits logs into two categories: Application logs and Workspace events.

Application logs show logs from the code that you execute on your cluster. Logs are categorized by component, and you can use filters or the search box to find specific logs. The logs exist in the cluster's storage, so they disappear when the cluster is terminated. To retain the logs, you can either download them while the cluster is running, or set up log ingestion.

The Workspace events pertain to the hardware of the cluster. The logs here show data like when the cluster comes online, goes offline, scaling events, and spot preemptions. Anyscale retains the workspace events even after the cluster terminates.

See [Accessing logs](/monitoring/accessing-logs.md).

![Application logs](/assets/images/monitor-logs-a621f27474c6a4b8ad97f2b50dd521fc.png)

## Timezones in dashboards and logs[​](#timezones-in-dashboards-and-logs "Direct link to Timezones in dashboards and logs")

Your local browser settings control most of the timezones displayed in the Anyscale console. The following table provides more details on timezones for console elements, dashboards, and logs:

| Element                                                         | Applicable timezone                                  | Notes                                                                                                                                           |
| --------------------------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Anyscale console artifacts (workspaces, jobs, container images) | Determined by your web browser settings.             |                                                                                                                                                 |
| Grafana dashboards                                              | Determined by your web browser settings.             | You can change this in the Grafana settings.                                                                                                    |
| Ray OSS dashboards                                              | Determined by your web browser settings.             | You can change timezone in the settings. If you select **Ray cluster timezone**, it infers the timezone from Ray settings. Ray defaults to UTC. |
| Anyscale unified log viewer                                     | Determined by your web browser settings.             |                                                                                                                                                 |
| OSS Ray log viewer                                              | Uses your local web browser settings when available. |                                                                                                                                                 |
| Timestamps printed directly in logs                             | Use the timezone settings for the Ray cluster.       | Ray defaults to UTC, but you can change this by setting the `TZ` environment variable.                                                          |
| Downloaded logs                                                 | UTC                                                  |                                                                                                                                                 |
