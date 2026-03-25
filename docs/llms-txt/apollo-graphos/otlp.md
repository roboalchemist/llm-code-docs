# Source: https://www.apollographql.com/docs/graphos/routing/observability/router-telemetry-otel/telemetry-pipelines/trace-exporters/otlp.md

# Source: https://www.apollographql.com/docs/graphos/routing/observability/router-telemetry-otel/telemetry-pipelines/metrics-exporters/otlp.md

# OpenTelemetry Protocol (OTLP) exporter

Enable and configure the [OpenTelemetry Protocol (OTLP)](https://www.opentelemetry.io/) exporter for metrics in the GraphOS Router or Apollo Router Core.

For general metrics configuration, refer to [Router Metrics Configuration](https://www.apollographql.com/docs/router/configuration/telemetry/exporters/metrics/overview).

Using the OTLP protocol, you can export metrics to any OTLP compatible receiver, including:

* [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/)
* [Datadog](https://www.datadoghq.com/) (see [configuration instructions](https://www.apollographql.com/docs/router/configuration/telemetry/exporters/metrics/datadog))
* [Dynatrace](https://www.dynatrace.com/) (see [configuration instructions](https://www.apollographql.com/docs/router/configuration/telemetry/exporters/metrics/dynatrace))
* [New Relic](https://www.newrelic.com/) (see [configuration instructions](https://www.apollographql.com/docs/router/configuration/telemetry/exporters/metrics/new-relic))

## OTLP configuration

The router can be configured to export metrics data using OTLP over either HTTP or gRPC.

An example router configuration using OTLP with gRPC:

```yaml title=router.yaml
telemetry:
  exporters:
    metrics:
      otlp:
        # Enable the OpenTelemetry exporter
        enabled: true
  
        # Optional endpoint, either 'default' or a URL (Defaults to http://127.0.0.1:4317 for gRPC and http://127.0.0.1:4318 for HTTP)
        endpoint: default
  
        # Optional protocol
        protocol: grpc
  
        # Optional gRPC configuration
        grpc:
          metadata:
            foo: bar
  
        # Optional batch_processor configuration
        batch_processor:
          scheduled_delay: 100ms
          max_concurrent_exports: 1000
          max_export_batch_size: 10000
          max_export_timeout: 100s
          max_queue_size: 10000
```

### `enabled`

Flag to enable the OTLP exporter.

Set to true to enable the OTLP exporter. Defaults to false.

### `endpoint`

The OTLP endpoint address.

Defaults to:

* [http://127.0.0.1:4317](http://127.0.0.1:4317/) for gRPC
* [http://127.0.0.1:4318](http://127.0.0.1:4318/) for HTTP

The following OpenTelemetry (OTEL) environment variables will override router's built-in telemetry configuration:

* `OTEL_EXPORTER_OTLP_ENDPOINT`
* `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT`
* `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT`

In Apollo Router v2.12.0 and earlier, these variables will override router's telemetry settings and may cause traces or metrics to be sent to an unintended destination.

In Apollo Router v2.13.0 and later, your router will not start if any of these variables are set. Remove them from your environment before launching.

### `grpc`

Settings specific to the gRPC protocol for setting a custom SSL certificate, domain name, and metadata.

```yaml
telemetry:
  exporters:
    tracing:
      otlp:
        grpc:
          domain_name: "<my-domain>"
          key: "<key>"
          ca: "<certificate-authority>"
          cert: "<certificate>"
          metadata:
            key1: value1
            key2: value2    
```

Use the [variable expansion feature](https://www.apollographql.com/docs/router/configuration/overview#variable-expansion) for referencing environment variables and file paths in YAML configuration files. Use `env.` and `file.` prefixes, for example `${file.ca.txt}`.

See [gRPC Authentication](https://grpc.io/docs/guides/auth/) for more information.

#### gRPC configuration reference

| Attribute     | Description                            |
| ------------- | -------------------------------------- |
| `domain_name` | An optional domain name                |
| `key`         | An optional key                        |
| `ca`          | An optional certificate authority      |
| `cert`        | An optional certificate                |
| `metadata`    | A map of headers to send with requests |

### `http`

Settings specific to the HTTP protocol for setting custom headers.

```yaml
http:
  headers:
    key1: value1
    key2: value2    
```

#### HTTP configuration reference

| Attribute | Description                            |
| --------- | -------------------------------------- |
| `headers` | A map of headers to send with requests |

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

An example configuration using OTLP with `batch_processor`:

```yaml
telemetry:
  exporters:
    metrics:
      otlp: 
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

## OTLP configuration reference

| Attribute     | Values                | Default                                                               | Description                                                           |
| ------------- | --------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `enabled`     |                       | `false`                                                               | Enable the OTLP exporter.                                             |
| `protocol`    | `grpc`\|`http`        | `grpc`                                                                | The protocol to use.                                                  |
| `endpoint`    |                       | `http://127.0.0.1:4317` for gRPC and `http://127.0.0.1:4318` for HTTP | The endpoint to send spans to.                                        |
| `grpc`        |                       |                                                                       | Configuration specific to gRPC protocol.                              |
| `http`        |                       |                                                                       | Configuration specific to HTTP protocol.                              |
| `temporality` | `delta`\|`cumulative` |                                                                       | See the documentation for your APM to see what this should be set to. |
