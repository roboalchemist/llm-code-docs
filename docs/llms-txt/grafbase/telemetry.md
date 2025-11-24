# Source: https://grafbase.com/docs/gateway/configuration/telemetry.md

# Telemetry

Configure telemetry settings to send traces, metrics, and logs to your preferred observability platform. The Grafbase Gateway automatically collects traces and metrics to the Grafbase dashboard when you run it with a valid Grafbase access token.

```toml
[telemetry]
service_name = "my-service"
```

- `service_name`: Set the service name to identify the Grafbase Gateway in the OpenTelemetry collector.

## Resource Attributes

Grafbase includes a standard set of resource attributes for every user. Define your own attributes to include them in all logs, traces, and metrics:

```toml
[telemetry.resource_attributes]
custom_key = "custom_value"
other_key = "other_value"
```

- `custom_key` and `other_key`: Define custom key-value pairs to include in all telemetry data.


## Global Exporters

To send traces to an OpenTelemetry endpoint, configure the OpenTelemetry exporter:

```toml
[telemetry.exporters.otlp]
enabled = true
endpoint = "http://localhost:1234"
protocol = "grpc"
timeout = "5s"
```

- `enabled`: Enables or disables the OpenTelemetry exporter. Default value is `false`.
- `endpoint`: Specifies the OpenTelemetry endpoint to send traces to.
- `protocol`: Specifies the protocol to use for the OpenTelemetry exporter. Either `http` or `grpc`. Default value is `grpc`.
- `timeout`: Specifies the timeout for the OpenTelemetry exporter. Default value is `60s`.

### Batch Exporter

Don't trigger a request for every span, trace, and metric event. Use batch processing to send requests at regular intervals. Configure the OpenTelemetry batch settings:

```toml
[telemetry.exporters.otlp.batch_export]
scheduled_delay = "5s"
max_queue_size = 2048
max_export_batch_size = 512
max_concurrent_exports = 1
```

- `scheduled_delay`: Specifies the delay, in seconds, between each batch export. Default value is `"5s"`.
- `max_queue_size`: Specifies the maximum number of items in the queue. Default value is `2048`.
- `max_export_batch_size`: Specifies the maximum number of items to export in a single batch. Default value is `512`.
- `max_concurrent_exports`: Specifies the maximum number of concurrent exports. Default value is `1`.

### gRPC Exporter

If using `grpc` as the `protocol`, the Gateway will use the following settings.

If you use TLS with a custom certificate for collectors, specify these TLS settings:

```toml
[telemetry.exporters.otlp.grpc.tls]
domain_name = "custom_name"
key = "/path/to/key.pem"
cert = "/path/to/cert.pem"
ca = "/path/to/ca.crt"
```

- `domain_name`: Identifies the domain name of the server's TLS certificate.
- `key`: Specifies the path to the secret key.
- `cert`: Specifies the path to the X509 certificate file in PEM format.
- `ca`: Specifies the path to the X509 CA certificate file in PEM format.

Define custom headers for gRPC collectors when needed:

```toml
[[telemetry.exporters.otlp.grpc.headers]]
authorization = "Bearer {{ env.GRPC_TOKEN }}"

[[telemetry.exporters.otlp.grpc.headers]]
custom = "static value"
```

### HTTP Exporter

If you set the `protocol` to `http`, the Gateway will use the following settings.

Define custom headers to send with every request:

```toml
[[telemetry.exporters.otlp.http.headers]]
authorization = "Bearer {{ env.GRPC_TOKEN }}"

[[telemetry.exporters.otlp.http.headers]]
custom = "static value"
```

The `http` exporter doesn't support TLS. Use the `grpc` exporter if you need TLS.

## Grafbase

The gateway exports telemetry data to the Grafbase Platform which can be configured similarly to `telemetry.exporters.oltp`:

```toml
[telemetry.grafbase]
# Custom endpoint for self-hosted platform
endpoint = "..."
# By default, "grpc" protocol is used. But if you need to, "http" is also supported.
protocol = "grpc"
```

## Response Extension

The gateway returns the query plan and trace id in the GraphQL response extensions under `grafbase` for Pathfinder, our GraphQL query tool. The gateway enables this by default and returns it whenever it sees the `x-grafbase-telemetry` request header:

```toml
[telemetry.exporters.response_extension]
trace_id = true
query_plan = true
```

- `trace_id`: The response extension includes the current trace ID. Default value is `true`.
- `query_plan`: The response extension includes the query plan. Default value is `true`.

Define a special header to enable returning the response extension:

```toml
# Defines who can access the grafbase response extension.
[[telemetry.exporters.response_extension.access_control]]
rule = "header"
name = "x-grafbase-telemetry"
```

Deny access to everyone with:

```toml
[[telemetry.exporters.response_extension.access_control]]
rule = "deny"
```

You can require a specific value for the header. The Grafbase extension only accepts requests with the correct header value and rejects all others.

```toml
[[telemetry.exporters.response_extension.access_control]]
rule = "header"
name = "x-grafbase-telemetry"
value = "must-be-this-value"
```

Use environment variables to parameterize the configuration:

```toml
[[telemetry.exporters.response_extension.access_control]]
rule = "header"
name = "{{ env.HEADER_NAME }}"
value = "{{ env.SECRET }}"
```

## Log Exporter

The system logs are sent to the given global OpenTelemetry endpoint. If you want to send logs to a different endpoint, configure the OpenTelemetry logs exporter:

```toml
[telemetry.logs.exporters.otlp]
enabled = true
endpoint = "http://localhost:1235"
```

- `enabled`: Enables or disables the OpenTelemetry logs exporter. Default value is `true`.
- `endpoint`: Specifies the OpenTelemetry logs endpoint to send logs to.

Read more about OpenTelemetry options in the [global configuration section](#global-exporters).

## Traces

Change tracing settings in the gateway configuration:

```toml
[telemetry.tracing]
sampling = 1
parent_based_sampler = false
```

- `sampling`: The percentage of requests to trace as a floating point from 0 to 1. For high traffic, sampling every request can be expensive. Defaults to `0.15`.
- `parent_based_sampler`: Enables the [parent based sampler](https://opentelemetry.io/docs/specs/otel/trace/tracestate-probability-sampling/#parent-based-sampler) mechanism. When enabled, the gateway looks at the request headers to make trace sampling decisions. It falls back to its default sampling strategy when the request doesn't specify a sampling strategy. This option is disabled by default. Only enable it if you control all the clients, because malicious actors could create more load by manipulating sampling. Defaults to `false`.

### Collect Configuration

Configure limits for trace collection in this section.

```toml
[telemetry.tracing.collect]
max_events_per_span = 128
max_attributes_per_span = 128
max_links_per_span = 128
max_attributes_per_event = 128
max_attributes_per_link = 128
```

- `max_events_per_span`: Maximum number of events recorded per span. Defaults to `128`.
- `max_attributes_per_span`: Maximum number of attributes recorded per span. Defaults to `128`.
- `max_links_per_span`: Maximum number of links recorded per span. Defaults to `128`.
- `max_attributes_per_event`: Maximum number of attributes one event can have. Defaults to `128`.
- `max_attributes_per_link`: Maximum number of attributes one link can have. Defaults to `128`.

### Trace Exporter

Send traces to a custom endpoint independent of the global endpoint configuration:

```toml
[telemetry.tracing.exporters.otlp]
enabled = true
endpoint = "http://localhost:1235"
```

- `enabled`: Enables or disables the OpenTelemetry exporter. Default value is `true`.
- `endpoint`: Specifies the OpenTelemetry endpoint to send traces to.

Read more about OpenTelemetry options in the [global configuration section](#global-exporters).

### Propagation

Use `propagation` options to configure how tracing context (trace id, parent span id, and extra context) flows between incoming requests and subgraphs. The router has built-in support for multiple common standards. If you need support for additional formats, contact us.

You can use propagation to connect spans between the gateway and other services to get end-to-end visibility into request lifecycles for debugging and monitoring. The Grafbase dashboard doesn't handle trace propagation directly - to propagate traces, you must configure an additional OpenTelemetry endpoint in your gateway settings.

```toml
[telemetry.tracing.propagation]
trace_context = true
baggage = true
aws_xray = false
```

- `trace_context`: Enable [TraceContext](https://www.w3.org/TR/trace-context/) propagation through the `traceparent` header. This is the standard trace parent propagation mechanism in OpenTelemetry. Defaults to `false`.
- `baggage`: Enable [Baggage](https://opentelemetry.io/docs/concepts/signals/baggage/) context propagation through the `baggage` header. This is the standard context propagation mechanism in OpenTelemetry. Defaults to `false`.
- `aws_xray`: Enable [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-tracingheader) propagation through the `x-amzn-trace-id` header. This is the builtin trace propagation mechanism in AWS X-Ray. Defaults to `false`.

## Metrics Exporter

Send metrics to a separate endpoint:

```toml
[telemetry.metrics.exporters.otlp]
enabled = true
endpoint = "http://localhost:1235"
```

- `enabled`: Enables or disables the OpenTelemetry metrics exporter. Default value is `true`.
- `endpoint`: Specifies the OpenTelemetry metrics endpoint to send metrics to.

Read more about OpenTelemetry options in the [global configuration section](#global-exporters).