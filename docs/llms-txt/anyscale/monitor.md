# Source: https://docs.anyscale.com/jobs/monitor.md

# Monitor a job

[View Markdown](/jobs/monitor.md)

# Monitor a job

Anyscale jobs provides several tools to monitor your jobs:

1. [Job detail page](#job-details)
2. [Metrics](#metrics)
3. [Logs](#logs)
4. [Notifications](#notifications)
5. [Alerts](#alerts)
6. [Ray Dashboard](#ray-dashboard)
7. [Workloads dashboard](#workloads-dashboard)
8. [Exporting logs and metrics](#exporting-logs)

This document describes each use case and provides suggestions for when to use each tool.

## Job detail page[​](#job-details "Direct link to Job detail page")

The job detail page contains the status of the job, information about your job's configuration, details about each job attempt, events of the job, and links to various other tools.

![Job detail page](/assets/images/job-details-e6b445961a1140237509fac1723b3f98.png)

The job events log is at the bottom of the page. This log lists events of your job and includes events about your job lifecycle and errors.

## Metrics[​](#metrics "Direct link to Metrics")

Access metrics related to your job in the Metrics tab of the job detail page.

![Job metrics](/assets/images/job-metrics-04062be113d44bb5a271677f0c4fed57.png)

Job metrics tracks hardware metrics and system-level metrics such as CPU or network utilization, memory, or disk usage, node count, number of Ray tasks, and number of active Ray actors.

Metrics are also available in [Grafana](https://grafana.com/) for a more advanced UI, which allows you to create custom dashboards for visualizing the metrics, including [custom metrics](https://docs.ray.io/en/latest/ray-observability/user-guides/add-app-metrics.html#adding-application-level-metrics).

Access Grafana by clicking the **View in Grafana** button in the **Metrics** tab.

## Logs[​](#logs "Direct link to Logs")

Logs are another source of information when debugging issues with your job. You can view the logs of your job by clicking the "Logs" tab in the job detail page.

By default, you can will see the driver logs of your job. If the job is still running, you can also view the Ray logs of the job through the [Ray Dashboard](#ray-dashboard).

### Log viewer[​](#log-viewer "Direct link to Log viewer")

If you have enabled log ingestion, you have access to the [Anyscale log viewer](/monitoring/accessing-logs.md#log-viewer)

![Job logs](/assets/images/job-logs-0c3fb13c38d2250063cbd63331519b2c.png)

With the Anyscale log viewer, you have access to all Ray logs of your jobs and can search and filter by time, text, or labels such as task name, node ID, and more.

By default, the logs are filtered to the time range of the job with no filters. You can change the time range by clicking the time range dropdown and select an end time and time window to look back. Anyscale stores up to 30 days of logs for your job. You're able to debug issues even after the job terminates.

To filter the logs, use the search bar to search for specific keywords. Enter a request ID in the search bar to filter logs for a specific request. You can also use `regex` to filter logs if your logs contain a specific pattern.

## Notifications[​](#notifications "Direct link to Notifications")

Anyscale jobs have a built-in alert for when a job succeeds, fails, or retries. The creator of the job receives an email notification when the job completes. As an admin, you can also create [Custom notifications](/administration/resource-management/custom-notifications.md) such as additional emails or slack channels.

## Alerts[​](#alerts "Direct link to Alerts")

To set up metric-based alerts based on your own criteria, see [Custom dashboards and alerting guide](/monitoring/custom-dashboards-and-alerting.md). These alerts are useful for tracking the health of your jobs or job queues.

## Ray Dashboard[​](#ray-dashboard "Direct link to Ray Dashboard")

The Ray Dashboard is scoped to a single Ray cluster. Each job attempt launches a new Ray cluster unless [Job queues](/jobs/queues.md) are used. To access this dashboard, click the "Ray Dashboard" tab in the job detail page.

To learn more about how to use the Ray Dashboard, see the [Ray documentation](https://docs.ray.io/en/latest/ray-observability/getting-started.html#jobs-view).

## Workloads Dashboard[​](#workloads-dashboard "Direct link to Workloads Dashboard")

Click the **Ray Workloads** tab in the Job details page to access the workloads dashboard.

To learn more about the workloads dashboard, see the [Workloads dashboard documentation](/monitoring/workload-debugging.md).

## Exporting logs and metrics[​](#exporting-logs "Direct link to Exporting logs and metrics")

If you want to push logs to [Vector](https://vector.dev/), a tool to ship logs to Amazon CloudWatch, Google Cloud Monitoring, Datadog, or other observability tools, see [Exporting logs and metrics with Vector](/monitoring/exporting-logs.md).

## More info[​](#more-info "Direct link to More info")

* To learn more details about the Ray Dashboard, see the [Ray Dashboard documentation](https://docs.ray.io/en/latest/ray-core/ray-dashboard.html)
* To learn more about Grafana and how to use it, see the official [Grafana documentation](https://grafana.com/docs/grafana/v7.5/)
* To learn more about the metrics that Ray emits, see the [System Metrics documentation](https://docs.ray.io/en/latest/ray-observability/reference/system-metrics.html)
