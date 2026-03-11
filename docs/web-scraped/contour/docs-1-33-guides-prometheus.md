# Source: https://projectcontour.io/docs/1.33/guides/prometheus//

Title: Collecting Metrics with Prometheus

URL Source: https://projectcontour.io/docs/1.33/guides/prometheus/

Markdown Content:
Envoy Metrics
-------------

Envoy typically [exposes metrics](https://www.envoyproxy.io/docs/envoy/v1.15.0/configuration/http/http_conn_man/stats#config-http-conn-man-stats) through an endpoint on its admin interface. To avoid exposing the entire admin interface to Prometheus (and other workloads in the cluster), Contour configures a static listener that sends traffic to the stats endpoint and nowhere else.

Envoy supports Prometheus-compatible `/stats/prometheus` endpoint for metrics on port `8002`.

Contour Metrics
---------------

Contour exposes a Prometheus-compatible `/metrics` endpoint that defaults to listening on port 8000. This can be configured by using the `--http-address` and `--http-port` flags for the `serve` command.

**Note:** the `Service` deployment manifest when installing Contour must be updated to represent the same port as the configured flag.

**The metrics endpoint exposes the following metrics:**

| Name | Type | Labels | Description |
| --- | --- | --- | --- |
| contour_build_info | [GAUGE](https://prometheus.io/docs/concepts/metric_types/#gauge) | branch, revision, version | Build information for Contour. Labels include the branch and git SHA that Contour was built from, and the Contour version. |
| contour_cachehandler_onupdate_duration_seconds | [SUMMARY](https://prometheus.io/docs/concepts/metric_types/#summary) |  | Histogram for the runtime of xDS cache regeneration. |
| contour_dag_cache_object | [GAUGE](https://prometheus.io/docs/concepts/metric_types/#gauge) | kind | Total number of items that are currently in the DAG cache. |
| contour_dagrebuild_seconds | [SUMMARY](https://prometheus.io/docs/concepts/metric_types/#summary) |  | Duration in seconds of DAG rebuilds |
| contour_dagrebuild_timestamp | [GAUGE](https://prometheus.io/docs/concepts/metric_types/#gauge) |  | Timestamp of the last DAG rebuild. |
| contour_dagrebuild_total | [COUNTER](https://prometheus.io/docs/concepts/metric_types/#counter) |  | Total number of times DAG has been rebuilt since startup |
| contour_eventhandler_operation_total | [COUNTER](https://prometheus.io/docs/concepts/metric_types/#counter) | kind, op | Total number of Kubernetes object changes Contour has received by operation and object kind. |
| contour_httpproxy | [GAUGE](https://prometheus.io/docs/concepts/metric_types/#gauge) | namespace | Total number of HTTPProxies that exist regardless of status. |
| contour_httpproxy_invalid | [GAUGE](https://prometheus.io/docs/concepts/metric_types/#gauge) | namespace, vhost | Total number of invalid HTTPProxies. |
| contour_httpproxy_orphaned | [GAUGE](https://prometheus.io/docs/concepts/metric_types/#gauge) | namespace | Total number of orphaned HTTPProxies which have no root delegating to them. |
| contour_httpproxy_root | [GAUGE](https://prometheus.io/docs/concepts/metric_types/#gauge) | namespace | Total number of root HTTPProxies. Note there will only be a single root HTTPProxy per vhost. |
| contour_httpproxy_valid | [GAUGE](https://prometheus.io/docs/concepts/metric_types/#gauge) | namespace, vhost | Total number of valid HTTPProxies. |
| contour_status_update_conflict_total | [COUNTER](https://prometheus.io/docs/concepts/metric_types/#counter) | kind | Number of status update conflicts encountered by object kind. |
| contour_status_update_duration_seconds | [SUMMARY](https://prometheus.io/docs/concepts/metric_types/#summary) | error, kind | How long a status update takes to finish. |
| contour_status_update_failed_total | [COUNTER](https://prometheus.io/docs/concepts/metric_types/#counter) | kind | Number of status updates that failed by object kind. |
| contour_status_update_noop_total | [COUNTER](https://prometheus.io/docs/concepts/metric_types/#counter) | kind | Number of status updates that are no-ops by object kind. This is a subset of successful status updates. |
| contour_status_update_success_total | [COUNTER](https://prometheus.io/docs/concepts/metric_types/#counter) | kind | Number of status updates that succeeded by object kind. |
| contour_status_update_total | [COUNTER](https://prometheus.io/docs/concepts/metric_types/#counter) | kind | Total number of status updates by object kind. |

Deploy Sample Monitoring Stack
------------------------------

Follow the instructions [here](https://prometheus-operator.dev/docs/prologue/quick-start/) to install a monitoring stack to your cluster using the [kube-prometheus](https://github.com/prometheus-operator/kube-prometheus) project sample manifests. These instructions install the [Prometheus Operator](https://github.com/prometheus-operator/prometheus-operator), a [Prometheus](https://prometheus.io/) instance, a [Grafana](https://grafana.com/)`Deployment`, and other components. Note that this is a quickstart installation, see documentation [here](https://github.com/prometheus-operator/kube-prometheus?tab=readme-ov-file#getting-started) for more details on customizing the installation for production usage.

The instructions above show how to access the Prometheus and Grafana web interfaces using `kubectl port-forward`. Sample `HTTPProxy` resources in the `examples/` directory can also be used to access these through your Contour installation:

```
kubectl apply -f examples/prometheus/httpproxy.yaml
kubectl apply -f examples/grafana/httpproxy.yaml
```

### Scrape Contour and Envoy metrics

To enable Prometheus to scrape metrics from the Contour and Envoy pods, we can add some RBAC customizations with a `Role` and `RoleBinding` in the `projectcontour` namespace:

```
kubectl apply -f examples/prometheus/rbac.yaml
```

Now add [`PodMonitor`](https://prometheus-operator.dev/docs/operator/design/#podmonitor) resources for scraping metrics from Contour and Envoy pods in the `projectcontour` namespace:

```
kubectl apply -f examples/prometheus/podmonitors.yaml
```

You should now be able to browse Contour and Envoy Prometheus metrics in the Prometheus and Grafana web interfaces to create dashboards and alerts.

### Apply Contour and Envoy Grafana Dashboards

Some sample Grafana dashboards are provided as `ConfigMap` resources in the `examples/grafana` directory. To use them with your Grafana installation, apply the resources:

```
kubectl apply -f examples/grafana/dashboards.yaml
```

And update the Grafana `Deployment`:

```
kubectl -n monitoring patch deployment grafana --type=json --patch-file examples/grafana/deployment-patch.json
```

You should now see dashboards for Contour and Envoy metrics available in the Grafana web interface.
