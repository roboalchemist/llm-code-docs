# Source: https://www.apollographql.com/docs/graphos/routing/observability/router-telemetry-otel/apm-guides/datadog/connecting-to-datadog/datadog-agent/datadog-agent-metrics.md

# Datadog configuration of OTLP exporter

This guide walks through configuring the Apollo Router to send metrics to Datadog via the Datadog Agent.
For an overview of all available connection methods, see [Connecting to Datadog](https://www.apollographql.com/docs/graphos/routing/observability/router-telemetry-otel/apm-guides/datadog/connecting-to-datadog).

This metrics exporter is a configuration of the [OTLP exporter](https://www.apollographql.com/docs/router/configuration/telemetry/exporters/metrics/otlp) to use with [Datadog](https://www.datadoghq.com/).

For general metrics configuration, refer to [Router Metrics Configuration](https://www.apollographql.com/docs/router/configuration/telemetry/exporters/metrics/overview).
For router instrumentation with Datadog-specific attributes, see the [Router Instrumentation guide](https://www.apollographql.com/docs/graphos/routing/observability/router-telemetry-otel/apm-guides/datadog/router-instrumentation).

## Configuration

To export metrics to Datadog, you must configure both the router to send traces to the Datadog agent and the Datadog agent to accept OpenTelemetry Protocol (OTLP) metrics.

### Router configuration

You should enable the [OTLP exporter](https://www.apollographql.com/docs/router/configuration/telemetry/exporters/metrics/otlp#configuration) and set both `temporality: delta` and `endpoint: <datadog-agent-endpoint>`. For example:

```yaml title=router.yaml
telemetry:
  exporters:
    metrics:
      otlp:
        enabled: true
        # Temporality MUST be set to delta. Failure to do this will result in incorrect metrics.
        temporality: delta
        # Optional endpoint, either 'default' or a URL (Defaults to http://127.0.0.1:4317)
        endpoint: "${env.DATADOG_AGENT_HOST}:4317"
```

You must set `temporality: delta`, otherwise the router generates incorrect metrics.

### Datadog agent configuration

To configure the Datadog agent, add OTLP configuration (`otlp_config`) to your `datadog.yaml`. For example:

```yaml title=datadog.yaml
otlp_config:
  receiver:
    protocols:
      grpc:
        endpoint: <dd-agent-ip>:4317
```

For more details about Datadog configuration, see [Datadog's docs on Agent configuration](https://docs.datadoghq.com/opentelemetry/otlp_ingest_in_the_agent/?tab=host).
