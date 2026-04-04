# Source: https://www.apollographql.com/docs/graphos/routing/observability/router-telemetry-otel/apm-guides/new-relic/new-relic-otlp-traces.md

# New Relic configuration of OTLP exporter

This tracing exporter is a configuration of the [OTLP exporter](https://www.apollographql.com/docs/graphos/routing/observability/telemetry/trace-exporters/otlp) to use with [New Relic](https://newrelic.com/).

For general tracing configuration, refer to [Router Tracing Configuration](https://www.apollographql.com/docs/router/configuration/telemetry/exporters/tracing/overview).

## New Relic configuration

To configure the router, enable the [OTLP exporter](https://www.apollographql.com/docs/router/configuration/telemetry/exporters/tracing/otlp/#otlp-configuration) and set both `endpoint: <new-relic-endpoint>` and `api-key: <new-relic-api-key>`. For example:

```yaml title=router.yaml
telemetry:
  exporters:
    tracing:
      otlp:
        enabled: true
        # Endpoint for your region.
        endpoint: <new-relic-endpoint>
        protocol: grpc
        grpc:
          metadata:
            api-key: <new-relic-api-key>

```

For more details about New Relic configuration, see [New Relic's docs on OpenTelemetry configuration](https://docs.newrelic.com/docs/more-integrations/open-source-telemetry-integrations/opentelemetry/get-started/opentelemetry-set-up-your-app/#review-settings).
