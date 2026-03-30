# Source: https://www.apollographql.com/docs/graphos/routing/observability/router-telemetry-otel/apm-guides/new-relic/new-relic-otlp-metrics.md

# New Relic configuration of OTLP exporter

This metrics exporter is a configuration of the [OTLP exporter](https://www.apollographql.com/docs/router/configuration/telemetry/exporters/metrics/otlp) to use with [New Relic](https://newrelic.com/).

For general tracing configuration, refer to [Router Metrics Configuration](https://www.apollographql.com/docs/router/configuration/telemetry/exporters/metrics/overview).

## New Relic configuration

To configure the router, enable the [OTLP exporter](https://www.apollographql.com/docs/router/configuration/telemetry/exporters/metrics/otlp#configuration) with `temporality: delta` and the appropriate endpoint and New Relic API key.

For New Relic, `temporality: delta` must be set and the value of the `endpoint` **must** end with `/v1/metrics`.  The example below uses a common default for New Relic.  Check your New Relic account to verify the correct value as the actual domain may vary by region.

For example:

```yaml title=router.yaml
telemetry:
  exporters:
    metrics:
      otlp:
        enabled: true
        protocol: grpc

        # Temporality MUST be set to delta. Failure to do this will result in incorrect metrics.
        temporality: delta

        # Ensure the endpoint provided ends with "/v1/metrics"
        # Be sure to use the correct URL for your region.
        endpoint: https://otlp.nr-data.net:4317/v1/metrics
        grpc:
          metadata:
            api-key: "<new-relic-api-key>"
```

For more details about New Relic configuration, see [New Relic's docs on OpenTelemetry configuration](https://docs.newrelic.com/docs/more-integrations/open-source-telemetry-integrations/opentelemetry/get-started/opentelemetry-set-up-your-app/#review-settings).
