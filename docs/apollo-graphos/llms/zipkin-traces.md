# Source: https://www.apollographql.com/docs/graphos/routing/observability/router-telemetry-otel/apm-guides/zipkin/zipkin-traces.md

# Zipkin tracing

Enable and configure tracing for [Zipkin](https://zipkin.io/) in GraphOS Router or Apollo Router Core.

For general tracing configuration, refer to [Router Tracing Configuration](https://www.apollographql.com/docs/router/configuration/telemetry/exporters/tracing/overview).

## OTLP configuration (recommended)

Zipkin supports OTLP ingestion via [zipkin-otel](https://github.com/openzipkin-contrib/zipkin-otel), and OpenTelemetry is [deprecating the native Zipkin exporters](https://opentelemetry.io/blog/2025/deprecating-zipkin-exporters/) in favor of OTLP. Using the OTLP exporter is recommended:

```yaml title=router.yaml
telemetry:
  exporters:
    tracing:
      otlp:
        enabled: true
        endpoint: "http://${env.ZIPKIN_HOST}:9411"
        protocol: http
```

This sends traces to Zipkin using the OTLP protocol.

See [OTLP configuration](https://www.apollographql.com/docs/router/configuration/telemetry/exporters/tracing/otlp#configuration) for more details on settings.

## Zipkin native configuration

The native Zipkin exporter is deprecated and will be removed in the next major version of Router. Zipkin supports OTLP ingestion, and OpenTelemetry is [deprecating native Zipkin exporters](https://opentelemetry.io/blog/2025/deprecating-zipkin-exporters/) in favor of OTLP. Use [OTLP configuration](https://www.apollographql.com/docs/graphos/routing/observability/router-telemetry-otel/apm-guides/zipkin/zipkin-traces.md#otlp-configuration-recommended) instead.

Zipkin native exporter does not currently support setting the service name on the Zipkin native exports.

You can configure the router to export tracing data to Zipkin using the native Zipkin exporter:

```yaml title=router.yaml
telemetry:
  exporters:
     tracing:
       zipkin:
         enabled: true
         # Optional endpoint (defaults to http://127.0.0.1:9411/api/v2/spans)
         endpoint: "http://${env.ZIPKIN_HOST}:9411/api/v2/spans"
```

### `enabled`

Set to true to enable the Zipkin exporter. Defaults to false.

### `endpoint`

The Zipkin collector endpoint address. Defaults to `http://127.0.0.1:9411/api/v2/spans`.

### `batch_processor`

All exporters support configuration of a batch span processor with `batch_processor`.

You must tune your `batch_processor` configuration if you see any of the following messages in your logs:

* `OpenTelemetry trace error occurred: cannot send message to batch processor '<provider>-tracing' as the channel is full`

* `OpenTelemetry metrics error occurred: cannot send span to the batch span processor because the channel is full`

The exact settings depend on the bandwidth available for you to send data to your application performance monitor (APM) and the bandwidth configuration of your APM. Expect to tune these settings over time as your application changes.

You can see how many spans are being dropped by enabling metrics export and looking at the:

* `apollo.router.telemetry.batch_processor.errors` - The number of errors encountered by exporter batch processors.
  * `name`: One of `apollo-tracing`, `datadog-tracing`, `otlp-tracing`, `zipkin-tracing`.
  * `error` = One of `channel closed`, `channel full`.

By looking at the rate of batch processor errors you can decide how to tune your batch processor settings.

```yaml title=router.yaml
telemetry:
  exporters:
    tracing:
      zipkin:
        enabled: true
        batch_processor:
          max_export_batch_size: 512
          max_concurrent_exports: 1
          max_export_timeout: 30s
          max_queue_size: 2048
          scheduled_delay: 5s
```

#### `batch_processor` configuration reference

| Attribute                | Default | Description                                                                               |
| ------------------------ | ------- | ----------------------------------------------------------------------------------------- |
| `scheduled_delay`        | 5s      | The delay in seconds from receiving the first span to sending the batch.                  |
| `max_concurrent_exports` | 1       | The maximum number of overlapping export requests.                                        |
| `max_export_batch_size`  | 512     | The number of spans to include in a batch. May be limited by maximum message size limits. |
| `max_export_timeout`     | 30s     | The timeout in seconds for sending spans before dropping the data.                        |
| `max_queue_size`         | 2048    | The maximum number of spans to be buffered before dropping span data.                     |

## Zipkin native configuration reference

| Attribute         | Default                              | Description                    |
| ----------------- | ------------------------------------ | ------------------------------ |
| `enabled`         | `false`                              | Enable the Zipkin exporter.    |
| `endpoint`        | `http://127.0.0.1:9411/api/v2/spans` | The endpoint to send spans to. |
| `batch_processor` |                                      | The batch processor settings.  |
