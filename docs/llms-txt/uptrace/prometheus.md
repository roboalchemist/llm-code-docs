# Source: https://uptrace.dev/raw/ingest/prometheus.md

# Ingesting Prometheus metrics into Uptrace

> Forward Prometheus data using remote write or Collector receivers, keeping PromQL queries compatible with Uptrace dashboards.

There are 2 ways to ingest Prometheus metrics into Uptrace:

- Using Prometheus Remote Write with the Uptrace endpoint.
- Using the OpenTelemetry Collector Prometheus receiver and the OTLP exporter.

## Prometheus remote write

<alert type="info">

Prometheus remote write is recommended over OTLP when using Uptrace as a [Grafana](/features/grafana) data source.

</alert>

Prometheus Remote Write allows Prometheus to send its collected metrics data to a long-term storage solution such as Uptrace.

You can configure Prometheus Remote Write using the following endpoint:

```yaml
remote_write:
  - url: 'https://api.uptrace.dev/api/v1/prometheus/write'
    headers: { 'uptrace-dsn': '<FIXME>' }
```

## OpenTelemetry Collector

[OpenTelemetry Collector](/opentelemetry/collector) acts as a central hub for receiving, processing, and exporting telemetry data to various backends or observability tools.

The Collector can receive telemetry data (traces, metrics, and logs) from multiple sources, including:

- Applications instrumented with OpenTelemetry SDKs.
- Other telemetry agents or collectors.
- Legacy systems using protocols like Jaeger, Zipkin, Prometheus, etc.

### Prometheus receiver

Prometheus uses a pull model for data collection. In a pull-based model, Prometheus acts as a client, actively retrieving metrics from the targets (servers, applications, or other data sources) it monitors.

You can use OpenTelemetry Collector instead of Prometheus to pull metrics using the [prometheus_simple](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/simpleprometheusreceiver) receiver:

```yaml
receivers:
  prometheus_simple:
    collection_interval: 10s
    endpoint: '172.17.0.5:9153'
    metrics_path: '/metrics'
    use_service_account: false
    tls:
      ca_file: '/path/to/ca'
      cert_file: '/path/to/cert'
      key_file: '/path/to/key'
      insecure_skip_verify: true
```

And then export the metrics to Uptrace using OpenTelemetry protocol:

```yaml
exporters:
  otlp:
    endpoint: https://api.uptrace.dev:4317
    headers:
      headers: { 'uptrace-dsn': '{{ dsn }}' }

service:
  pipelines:
    metrics:
      receivers: [prometheus_simple]
      exporters: [otlp]
```

See [OpenTelemetry Prometheus Metrics](/opentelemetry/collector/prometheus) for details.
