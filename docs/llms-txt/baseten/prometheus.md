# Source: https://docs.baseten.co/observability/export-metrics/prometheus.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Export to Prometheus

> Export metrics from Baseten to Prometheus

To integrate with Prometheus, specify the Baseten metrics endpoint in a scrape config. For example:

```yaml prometheus.yml theme={"system"}
global:
  scrape_interval: 60s
scrape_configs:
  - job_name: 'baseten'
    metrics_path: '/metrics'
    authorization:
      type: "Api-Key"
      credentials: "{BASETEN_API_KEY}"
    static_configs:
      - targets: ['app.baseten.co']
    scheme: https
```

See the Prometheus docs for more details on [getting started](https://prometheus.io/docs/prometheus/latest/getting_started/) and [configuration options](https://prometheus.io/docs/prometheus/latest/configuration/configuration/).
