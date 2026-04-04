# Source: https://uptrace.dev/raw/ingest/logs/loki.md

# Ingesting logs using Grafana Loki push API

> Bridge Promtail or Grafana Agent into Uptrace by enabling the Loki receiver on OpenTelemetry Collector and exporting via OTLP.

You can receive logs from Grafana Agent or Promtail using the OpenTelemetry Collector Loki receiver and then export the data to Uptrace using the OpenTelemetry protocol.

## OpenTelemetry Collector

[OpenTelemetry Collector](/opentelemetry/collector) is an agent that pulls telemetry data from systems you want to monitor and sends it to [tracing tools](/tools/distributed-tracing-tools) using the OpenTelemetry protocol (OTLP).

You can use OpenTelemetry Collector to monitor [host metrics](/opentelemetry/collector/host-metrics), [PostgreSQL](/guides/opentelemetry-postgresql), [MySQL](/guides/opentelemetry-mysql), [Redis](/guides/opentelemetry-redis), and more.

## Loki receiver

The Loki [receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/lokireceiver) implements the [Loki push api](https://grafana.com/docs/loki/latest/clients/promtail/#loki-push-api) as specified [here](https://grafana.com/docs/loki/latest/api/#push-log-entries-to-loki). It allows Promtail instances to specify the Open telemetry Collector as their `lokiAddress`.

To receive logs from Promtail and export them to Uptrace, add the following to your OpenTelemetry Collector configuration file:

```yaml
receivers:
  loki:
    protocols:
      http:
      grpc:
    use_incoming_timestamp: true

exporters:
  otlp/uptrace:
    endpoint: api.uptrace.dev:4317
    headers:
      uptrace-dsn: '<FIXME>'

processors:
  batch:

service:
  pipelines:
    logs:
      receivers: [loki]
      processors: [batch]
      exporters: [otlp/uptrace]
```

You can then configure Promtail to export data to OpenTelemetry Collector:

```yaml
clients:
  - url: http://otelcol:3500/loki/api/v1/push
```

- [OpenTelemetry Logs](/opentelemetry/logs)
- [Structured logging](/glossary/structured-logging)
