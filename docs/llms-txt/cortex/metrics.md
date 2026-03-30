# Source: https://docs.cortexlabs.com/workloads/realtime/metrics.md

# Source: https://docs.cortexlabs.com/clusters/observability/metrics.md

# Source: https://docs.cortexlabs.com/0.41/workloads/realtime/metrics.md

# Source: https://docs.cortexlabs.com/0.41/clusters/observability/metrics.md

# Source: https://docs.cortexlabs.com/0.40/workloads/realtime/metrics.md

# Source: https://docs.cortexlabs.com/0.40/clusters/observability/metrics.md

# Source: https://docs.cortexlabs.com/0.39/workloads/realtime/metrics.md

# Source: https://docs.cortexlabs.com/0.39/clusters/observability/metrics.md

# Source: https://docs.cortexlabs.com/0.38/workloads/realtime/metrics.md

# Source: https://docs.cortexlabs.com/0.38/clusters/observability/metrics.md

# Source: https://docs.cortexlabs.com/0.37/workloads/realtime/metrics.md

# Source: https://docs.cortexlabs.com/0.37/clusters/observability/metrics.md

# Source: https://docs.cortexlabs.com/0.36/workloads/realtime/metrics.md

# Source: https://docs.cortexlabs.com/0.36/clusters/observability/metrics.md

# Source: https://docs.cortexlabs.com/0.35/workloads/task-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.35/workloads/batch-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.35/workloads/async-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.35/workloads/realtime-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.35/clusters/observability/metrics.md

# Source: https://docs.cortexlabs.com/0.34/workloads/task-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.34/workloads/batch-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.34/workloads/async-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.34/workloads/realtime-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.34/clusters/observability/metrics.md

# Source: https://docs.cortexlabs.com/0.33/workloads/task-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.33/workloads/batch-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.33/workloads/async-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.33/workloads/realtime-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.33/clusters/observability/metrics.md

# Source: https://docs.cortexlabs.com/0.32/workloads/task-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.32/workloads/batch-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.32/workloads/async-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.32/workloads/realtime-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.32/clusters/observability/metrics.md

# Source: https://docs.cortexlabs.com/0.31/workloads/observability/metrics.md

# Source: https://docs.cortexlabs.com/0.31/workloads/task-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.31/workloads/batch-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.31/workloads/introduction/metrics.md

# Source: https://docs.cortexlabs.com/0.31/workloads/realtime-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.30/workloads/observability/metrics.md

# Source: https://docs.cortexlabs.com/0.30/workloads/realtime-apis/metrics.md

# Source: https://docs.cortexlabs.com/0.29/workloads/realtime-apis/metrics.md

# Metrics

The `cortex get` and `cortex get API_NAME` commands display the request time (averaged over the past 2 weeks) and response code counts (summed over the past 2 weeks) for your APIs:

```bash
$ cortex get

env   api                         status   up-to-date   requested   last update   avg request   2XX
aws   iris-classifier             live     1            1           17m           24ms          1223
aws   text-generator              live     1            1           8m            180ms         433
aws   image-classifier-resnet50   live     2            2           1h            32ms          1121126
```

The `cortex get API_NAME` command also provides a link to a Grafana dashboard:

![dashboard](https://user-images.githubusercontent.com/7456627/107253455-9c6b7b80-6a36-11eb-8600-f36a7bab6d3b.png)

## Metrics in the dashboard

| Panel             | Description                                                                        | Note                                                                                               |
| ----------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Request Rate      | Request rate, computed over every minute, of an API                                |                                                                                                    |
| In Flight Request | Active in-flight requests for an API.                                              | In-flight requests are recorded every 10 seconds, which will correspond to the minimum resolution. |
| Active Replicas   | Active replicas for an API                                                         |                                                                                                    |
| 2XX Responses     | Request rate, computed over a minute, for responses with status code 2XX of an API |                                                                                                    |
| 4XX Responses     | Request rate, computed over a minute, for responses with status code 4XX of an API |                                                                                                    |
| 5XX Responses     | Request rate, computed over a minute, for responses with status code 5XX of an API |                                                                                                    |
| p99 Latency       | 99th percentile latency, computed over a minute, for an API                        | Value might not be accurate because the histogram buckets are not dynamically set.                 |
| p90 Latency       | 90th percentile latency, computed over a minute, for an API                        | Value might not be accurate because the histogram buckets are not dynamically set.                 |
| p50 Latency       | 50th percentile latency, computed over a minute, for an API                        | Value might not be accurate because the histogram buckets are not dynamically set.                 |
| Average Latency   | Average latency, computed over a minute, for an API                                |                                                                                                    |

## Accessing the dashboard

The dashboard URL is displayed once you run a `cortex get <api_name>` command.

Alternatively, you can access it on `http://<operator_url>/dashboard`. Run the following command to get the operator URL:

```
cortex env list
```

### Default credentials

The dashboard is protected with username / password authentication, which by default are:

* Username: admin
* Password: admin

You will be prompted to change the admin user password in the first time you log in.

Grafana allows managing the access of several users and managing teams. For more information on this topic check the [grafana documentation](https://grafana.com/docs/grafana/latest/manage-users/).

### Selecting an API

You can select one or more APIs to visualize in the top left corner of the dashboard.

![](https://user-images.githubusercontent.com/7456627/107375721-57545180-6ae9-11eb-9474-ba58ad7eb0c5.png)

### Selecting a time range

Grafana allows you to select a time range on which the metrics will be visualized. You can do so in the top right corner of the dashboard.

![](https://user-images.githubusercontent.com/7456627/107376148-d9dd1100-6ae9-11eb-8c2b-c678b41ade01.png)

**Note: Cortex only retains a maximum of 2 weeks worth of data at any moment in time**

### Available dashboards

There are more than one dashboard available by default. You can view the available dashboards by accessing the Grafana menu: `Dashboards -> Manage -> Cortex folder`.

## Exposed metrics

Cortex exposes more metrics with Prometheus, that can be potentially useful. To check the available metrics, access the `Explore` menu in grafana and press the `Metrics` button.

![](https://user-images.githubusercontent.com/7456627/107377492-515f7000-6aeb-11eb-9b46-909120335060.png)

You can use any of these metrics to set up your own dashboards.
