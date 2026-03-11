# Source: https://docs.anyscale.com/monitoring/grafana-dashboards.md

# Ray Grafana dashboards

[View Markdown](/monitoring/grafana-dashboards.md)

# Ray Grafana dashboards

Anyscale and Ray provide many Grafana dashboards out of the box. You can use these dashboards as a starting points for creating your own custom dashboards. When editing dashboards, duplicate them first because Anyscale may update and replace them over time, overwriting your changes. Anyscale may also share these dashboards across multiple Ray apps and clusters, so it's important to duplicate them to avoid affecting other apps accidentally.

These dashboards visualize metrics exported by the Ray Core and Ray libraries. A common modification you may want to make is the addition of graphs to visualize [custom application metrics](/monitoring/metrics.md#custom-metrics) defined by your Ray app.

## Ray Core dashboard[​](#ray-core-dashboard "Direct link to Ray Core dashboard")

The Ray Core dashboard provides visualizations of system level Ray metrics and hardware metrics. This dashboard is useful for monitoring the health of the Ray cluster.

System-level graphs include information about Ray tasks, Ray actors, nodes, the autoscaler, and more. Hardware metrics include CPU, GPU, memory, disk, and network utilization. See the [Ray system metrics documentation](https://docs.ray.io/en/latest/ray-observability/reference/system-metrics.html) for more information.

![Ray Core dashboard](/assets/images/core-dashboard-8cd4a3e1d1d0e41d355a1b11bdda6a1d.png)

## Ray Data dashboard[​](#ray-data-dashboard "Direct link to Ray Data dashboard")

The Ray Data dashboard provides visualizations of Ray Data metrics. This dashboard is useful for monitoring the health and performance of your Ray Data workloads. Dataset-level graphs include information about dataset outputs (rows, blocks, bytes, tasks), dataset iteration metrics, as well as internal operator metrics (internal queues, object store usage, and more). See the [Ray Data monitoring docs](https://docs.ray.io/en/latest/data/monitoring-your-workload.html) for more information.

![Ray Data dashboard](/assets/images/data-dashboard-3a292bdb0afa2bacbab4c896ac1237ae.png)

## Ray Serve[​](#ray-serve "Direct link to Ray Serve")

### Ray Serve dashboard[​](#serve-dashboard "Direct link to Ray Serve dashboard")

The Ray Serve dashboard provides visualizations of Ray Serve metrics. This dashboard is useful for monitoring the health of your Ray Serve apps. It includes service metrics such as request latency, request throughput, and service health. It also includes service rollout metrics to track and compare the different service versions. See the [Ray Serve monitoring documentation](https://docs.ray.io/en/latest/serve/monitoring.html) for more information.

Anyscale aggregates the service metrics at the app and route level. To look at metrics grouped by individual replicas, use the [Ray Serve deployment dashboard](#deployment-dashboard).

![Ray Serve dashboard](/assets/images/serve-dashboard-5ce3285fae4e1258e5a1132064d5d2d2.png)

### Ray Serve deployment dashboard[​](#deployment-dashboard "Direct link to Ray Serve deployment dashboard")

The Ray Serve deployment dashboard provides visualizations of Ray Serve deployment metrics. This dashboard is useful for monitoring the health of your Ray Serve deployments. It includes service metrics such as request latency, request throughput, and deployment health. See the [Ray Serve monitoring documentation](https://docs.ray.io/en/latest/serve/monitoring.html) for more information.

Anyscale aggregates the service metrics at the deployment level. Anyscale groups metrics by replica ID so you can compare the relative health of different replicas.

![Ray Serve deployment dashboard](/assets/images/serve-deployment-dashboard-1dc8d6ada4d1722a01d2ddf3882be9cc.png)
