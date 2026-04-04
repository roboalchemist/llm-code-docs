# Source: https://docs.api7.ai/apisix/how-to-guide/observability/monitor-apisix-with-prometheus.md

# Monitor APISIX Metrics with Prometheus

Prometheus is a popular systems monitoring and alerting toolkit. It collects and stores multi-dimensional time series data like metrics with key-value paired labels.

APISIX offers the capability to expose a significant number of metrics to Prometheus [with low latency](https://api7.ai/blog/1s-to-10ms-reducing-prometheus-delay-in-api-gateway), allowing for continuous monitoring and diagnostics.

This guide will show you how to enable the [`prometheus`](https://docs.api7.ai/hub/prometheus.md) plugin to integrate with Prometheus and Grafana services, where APISIX HTTP metrics are collected and visualized.

<br />

![APISIX Prometheus Grafana flow diagram](https://static.api7.ai/uploads/2023/05/16/5Z5bIUwF_grafana-prometheus.jpg)

<br />

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Enable Prometheus Plugin[â](#enable-prometheus-plugin "Direct link to Enable Prometheus Plugin")

Enable the `prometheus` plugin globally. Alternatively, you can enable the plugin on a route.

* Admin API
* ADC

```
curl -i "http://127.0.0.1:9180/apisix/admin/global_rules" -X PUT -d '{
  "id": "rule-for-metrics",
  "plugins": {
    "prometheus":{}
  }
}'
```

APISIX gathers internal runtime metrics and exposes them through port `9091` and path `/apisix/prometheus/metrics` by default. The port and the path can be [customized in the configuration file](https://docs.api7.ai/hub/prometheus/configuration.md#static-configurations).

adc.yaml

```
global_rules:
  prometheus: {}
```

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

APISIX gathers internal runtime metrics and exposes them through port `9091` and path `/apisix/prometheus/metrics` by default. The port and the path can be [customized in the configuration file](https://docs.api7.ai/hub/prometheus/configuration.md#static-configurations).

Send a request to the route `/apisix/prometheus/metrics` to fetch metrics from APISIX:

```
curl "http://127.0.0.1:9091/apisix/prometheus/metrics"
```

You should see a list of metrics similar to the following:

```
# HELP apisix_etcd_modify_indexes Etcd modify index for APISIX keys
# TYPE apisix_etcd_modify_indexes gauge
apisix_etcd_modify_indexes{key="consumers"} 0
apisix_etcd_modify_indexes{key="global_rules"} 0
apisix_etcd_modify_indexes{key="max_modify_index"} 16
apisix_etcd_modify_indexes{key="prev_index"} 15
apisix_etcd_modify_indexes{key="protos"} 0
apisix_etcd_modify_indexes{key="routes"} 16
apisix_etcd_modify_indexes{key="services"} 0
apisix_etcd_modify_indexes{key="ssls"} 0
apisix_etcd_modify_indexes{key="stream_routes"} 0
apisix_etcd_modify_indexes{key="upstreams"} 0
apisix_etcd_modify_indexes{key="x_etcd_index"} 16
# HELP apisix_etcd_reachable Config server etcd reachable from APISIX, 0 is unreachable
# TYPE apisix_etcd_reachable gauge
apisix_etcd_reachable 1
...
# HELP apisix_http_status HTTP status codes per service in APISIX
# TYPE apisix_http_status counter
apisix_http_status{code="200",route="ip",matched_uri="/ip",matched_host="",service="",consumer="",node="52.20.124.211"} 1
...
```

## Configure Prometheus[â](#configure-prometheus "Direct link to Configure Prometheus")

In Prometheus, targets are the endpoints that Prometheus scrapes for metrics. You can configure the APISIX metrics endpoint as a target in Prometheus to collect metrics from it.

Create a configuration file `prometheus.yml`:

```
echo 'scrape_configs:
  - job_name: "apisix"
    scrape_interval: 15s
    metrics_path: "/apisix/prometheus/metrics"
    static_configs:
      - targets: ["apisix-quickstart:9091"]
' > prometheus.yml
```

Start a Prometheus instance in Docker. The exposed port is mapped to `9092` on the host because `9090` is reserved for APISIX. The local configuration file `prometheus.yml` is mounted to the Prometheus container.

```
docker run -d --name apisix-quickstart-prometheus \
  -p 9092:9090 \
  --network=apisix-quickstart-net \
  -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus:latest
```

You can now check if the APISIX metric endpoint state is `UP` on the Prometheus [targets page](http://localhost:9092/targets). Prometheus will collect metrics from APISIX by scraping this endpoint.

![Prometheus](https://static.api7.ai/uploads/2023/03/02/mRbZ4Hxm_prometheus.png)

## Configure Grafana[â](#configure-grafana "Direct link to Configure Grafana")

Grafana can visualize metrics stored in Prometheus.

Start a Grafana instance on port `3000` in Docker:

```
docker run -d --name=apisix-quickstart-grafana \
  -p 3000:3000 \
  --network=apisix-quickstart-net \
  grafana/grafana-oss
```

Visit [Grafana console](http://localhost:3000) and add the Prometheus instance created above to Grafana as a data source. Configure `http://127.0.0.1:9092` in the URL.

![Grafana Data Source](https://static.api7.ai/uploads/2023/03/02/E9PNMkdv_grafana-data-source.png)

The official APISIX metric dashboard is published to [Grafana dashboards](https://grafana.com/grafana/dashboards/) with ID [11719](https://grafana.com/grafana/dashboards/11719-apache-apisix/). You can then import the dashboard into Grafana with the ID.

![Import Dashboard](https://static.api7.ai/uploads/2023/03/02/21YcUlui_grafana-import-dashboard.png)

If everything is OK, the dashboard will automatically visualize metrics in real time.

![Grafana Dashboard](https://static.api7.ai/uploads/2023/03/02/8hcTkwWW_grafana-dashboard.png)

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned how to monitor APISIX metrics with Prometheus and visualize them in Grafana. See the [`prometheus`](https://docs.api7.ai/hub/prometheus.md) plugin documentation for more configuration options.
