# Source: https://docs.anyscale.com/monitoring/accessing-logs.md

# Accessing logs

[View Markdown](/monitoring/accessing-logs.md)

# Accessing logs

Anyscale offers multiple ways to access logs for your Ray clusters.

## Log viewer[​](#log-viewer "Direct link to Log viewer")

The log viewer allows you to view and download log files generated from your Ray apps. To access the log viewer UI, select the **Logs** tab in the workspace, job or service detail page.

![Services logs without log query](/assets/images/services-logs-without-query-9324f5dc1c5f5cbe98c51f7c32380732.png)

The limit of this basic log viewer is that you can only view logs from individual log files. When you download logs, all the log files on the cluster will be downloaded.

### Log ingestion and query[​](#log-ingestion-and-query "Direct link to Log ingestion and query")

Log ingestion and query is an optional feature that allows you to search, filter, query logs more easily. Any cluster created after enabling this feature sends logs to the Anyscale Control Plane, where they're retained for 30 days. You may incur extra data transfer costs from your cloud provider by enabling this feature.

It is enabled by default for Anyscale Hosted clouds. For self-hosted clouds, you must opt-in with the following command:

```
# Change the `cloud_id` to your cloud ID
anyscale cloud config update --cloud-id CLOUD_ID --enable-log-ingestion
```

See the [CLI reference](/reference/cloud.md#anyscale-cloud-update) for more information.

To query logs, select the **Logs** tab in the workspace,job or service detail page.

![Service logs](/assets/images/services-logs-8b9d2ef7fe8afecfa059a41cfd9bffe1.png)

By default, the logs shown are from the last hour with no filters. You can change the time range by selecting an end time and window to look back.

To filter the logs, use the search bar to find specific keywords, request IDs, and regular expression patterns.

![Log query example](/assets/images/log-query-example-69b98ec66694714884f3cd85d46a96cf.png)

note

To disable log ingestion and query, run `anyscale cloud config update --cloud-id CLOUD_ID --disable-log-ingestion`. Subsequently, created Ray clusters won't send logs to the Anyscale Control Plane, however, Anyscale retains previously sent logs for 30 days.

## Ray Dashboard[​](#ray-dashboard "Direct link to Ray Dashboard")

Ray Dashboard is a consolidated tool for monitoring and debugging your applications available when the Ray cluster is running. To access the logs, select the **Ray Dashboard** tab and then **Logs** tab.

For information on the log files, see [Configuring logging](https://docs.ray.io/en/latest/ray-observability/user-guides/configure-logging.html#configuring-logging).

## Logs CLI[​](#logs-cli "Direct link to Logs CLI")

To download logs, even after the cluster has terminated, run the following CLI command:

```
# Change `cluster_id` to your cluster ID
anyscale logs cluster --id CLUSTER_ID --download --download-dir /tmp
```

See the [CLI reference](/reference/logs.md#anyscale-logs-cluster) for more information and options.

## Find logs[​](#find-logs "Direct link to Find logs")

Anyscale stores logs in `{organization_id}/{cloud_id}/logs` and `/logs` folders. The `/logs` folder is a legacy location. Anyscale sends most logs to the `{organization_id}/{cloud_id}/logs` folder. Anyscale stores all job logs, web terminal command logs, and Ray logs. For performance reasons, Anyscale stores logs in various formats for different use cases. For example, when streaming logs, Anyscale may produce many small files to allow for fresher data to be downloaded by the user.
