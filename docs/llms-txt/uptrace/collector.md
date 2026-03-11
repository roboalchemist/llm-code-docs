# Source: https://uptrace.dev/raw/opentelemetry/collector.md

# Source: https://uptrace.dev/raw/ingest/collector.md

# Ingesting telemetry using OpenTelemetry Collector

> Send telemetry from OpenTelemetry Collector to Uptrace using OTLP exporters for traces, metrics, and logs.

[OpenTelemetry Collector](/opentelemetry/collector) is an agent that pulls telemetry data from systems you want to monitor and sends it to [tracing tools](/tools/distributed-tracing-tools) using the OpenTelemetry protocol (OTLP).

You can use OpenTelemetry Collector to monitor [host metrics](/opentelemetry/collector/host-metrics), [PostgreSQL](/guides/opentelemetry-postgresql), [MySQL](/guides/opentelemetry-mysql), [Redis](/guides/opentelemetry-redis), and more.

Out of the box, Uptrace accepts data from OpenTelemetry Collector using OTLP and automatically creates [dashboards](/features/querying/metrics#dashboards) for the available metrics.

## Sending data from Collector to Uptrace

If you are already using [OpenTelemetry Collector](/opentelemetry/collector), you can configure it to send data to Uptrace using OpenTelemetry Protocol (OTLP).

<alert type="info">

Don't forget to add Uptrace exporter to `service.pipelines` section. Unused receivers and exporters are silently ignored.

</alert>

### Cloud

To send data to [Uptrace Cloud](/):

<code-group>

```yaml [gRPC]
processors:
  resourcedetection:
    detectors: [env, system]
  cumulativetodelta:
  batch:
    send_batch_size: 10000
    timeout: 10s

exporters:
  otlp/uptrace:
    endpoint: api.uptrace.dev:4317
    headers:
      uptrace-dsn: '<FIXME>'

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp/uptrace]
    metrics:
      receivers: [otlp]
      processors: [cumulativetodelta, batch, resourcedetection]
      exporters: [otlp/uptrace]
    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp/uptrace]
```

```yaml [HTTP]
processors:
  resourcedetection:
    detectors: [env, system]
  cumulativetodelta:
  batch:
    send_batch_size: 10000
    timeout: 10s

exporters:
  otlphttp/uptrace:
    endpoint: https://api.uptrace.dev
    headers:
      uptrace-dsn: '<FIXME>'

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp/uptrace]
    metrics:
      receivers: [otlp]
      processors: [cumulativetodelta, batch, resourcedetection]
      exporters: [otlphttp/uptrace]
    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp/uptrace]
```

</code-group>

### Debugging issues

If otelcol is not working as expected, you can check the log output for potential issues. The logging verbosity level defaults to `INFO`, but you can change it using the configuration file:

```yaml
service:
  telemetry:
    logs:
      level: 'debug'
```

## Sending data from Uptrace distros to Collector

Sometimes it might be useful to send data from Uptrace distros to an OpenTelemetry Collector acting as a middle-man that forwards the received data to Uptrace.

For example, you can use OpenTelemetry Collector in such a manner for [tail-based sampling](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/tailsamplingprocessor) or [redacting](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/redactionprocessor) span attributes.

Assuming your local OpenTelemetry Collector is listening on `localhost:4317` (OTLP/gRPC) and `localhost:4318` (OTLP/HTTP), use the following Uptrace DSN to configure Uptrace distros:

```shell
# For distros that use OTLP/gRPC exporter.
UPTRACE_DSN=http://localhost:4317

# or

# For distros that use OTLP/HTTP exporter.
UPTRACE_DSN=http://localhost:4318
```

If the Collector supports TLS, replace `http` with `https`.

## Host metrics

`hostmetricsreceiver` is an OpenTelemetry Collector plugin that gathers various metrics about the host system, for example, CPU, RAM, disk metrics and other system-level metrics.

See [OpenTelemetry Host Metrics receiver](/opentelemetry/collector/host-metrics) for details.

## Dashboards

Once everything is configured properly, Uptrace will automatically create dashboards using pre-built [templates](https://github.com/uptrace/uptrace/tree/master/config/dashboard-templates):

![Dashboard](/opentelemetry/host-metrics/metrics.png)

## What's next?

Next, learn more about [OpenTelemetry Collector](/opentelemetry/collector) or browse available [receivers](/opentelemetry/collector/config).

- [OTel Arrow](/ingest/otelarrow) - Reduce bandwidth by up to 50% using Apache Arrow columnar format
- [OpenTelemetry Kubernetes](/get/kubernetes)
- [OpenTelemetry Docker](/guides/opentelemetry-docker)
- [OpenTelemetry Redis](/guides/opentelemetry-redis)
- [OpenTelemetry PostgreSQL](/guides/opentelemetry-postgresql)
- [OpenTelemetry MySQL](/guides/opentelemetry-mysql)
- [OpenTelemetry Kafka](/guides/opentelemetry-kafka)
- [OpenTelemetry PHP-FPM](/guides/opentelemetry-php-fpm)
