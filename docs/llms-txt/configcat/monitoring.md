# Source: https://configcat.com/docs/advanced/proxy/monitoring.md

# Monitoring

Copy page

The ConfigCat Proxy provides diagnostic data including health status, metrics, and traces.

info

Exposed endpoints (`/status` and `/metrics`) are served on a specific port, so you can separate them from the public HTTP communication.

These are the basic diagnostic-related options:

| Option                                                                                                                 | Default | Description                                     |
| ---------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------------------------------- |
| - YAML<br />- Environment variable```yaml
diag:
  enabled: <true|false>

``````shell
CONFIGCAT_DIAG_ENABLED=<true|false>

``` | `true`  | Turns the collection of diagnostic data on/off. |
| - YAML<br />- Environment variable```yaml
diag:
  port: 8051

``````shell
CONFIGCAT_DIAG_PORT=8051

```                       | `8051`  | The port used by the diagnostics HTTP server.   |

## Status Endpoint[​](#status "Direct link to Status Endpoint")

The Proxy provides status information (health check) about its components on the following endpoint:

GETOPTIONS/status

The Proxy regularly checks whether the underlying SDKs can communicate with their configured source and with the cache. This endpoint returns the actual state of these checks.

**Responses**:

* 200: The status returned successfully.
* 204: In response to an `OPTIONS` request.

**Example Response**:

```json
{
  "status": "healthy",
  "sdks": {
    "my_sdk": {
      "key": "****************************************hwTYg",
      "mode": "online",
      "source": {
        "type": "remote",
        "status": "healthy",
        "records": [
          "Mon, 29 May 2023 16:36:40 UTC: [ok] config fetched"
        ]
      }
    },
    "another_sdk": {
      "key": "****************************************ovVnQ",
      "mode": "offline",
      "source": {
        "type": "cache",
        "status": "healthy",
        "records": [
          "Mon, 29 May 2023 16:36:40 UTC: [ok] reload from cache succeeded",
          "Mon, 29 May 2023 16:36:45 UTC: [ok] config from cache not modified"
        ]
      }
    }
  },
  "cache": {
    "status": "healthy",
    "records": [
      "Mon, 29 May 2023 16:36:40 UTC: [ok] cache read succeeded",
      "Mon, 29 May 2023 16:36:40 UTC: [ok] cache write succeeded",
      "Mon, 29 May 2023 16:36:40 UTC: [ok] cache read succeeded",
      "Mon, 29 May 2023 16:36:45 UTC: [ok] cache read succeeded"
    ]
  }
}

```

**Details**:

If everything is operational, each `status` node shows the value `healthy`. If a component encounters a failure, it'll put an error to its `records` collection. If a component's last two records are errors, its `status` will switch to `degraded`. If a component becomes operational again it'll put an `[ok]` to the `records` and will switch back to `healthy`.

If an SDK couldn't initialize itself neither from an external cache nor from the ConfigCat CDN, its status will be `down`. It means, this SDK is not able to accept evaluation requests because it doesn't have a valid *config JSON* to work with.

If an SDK was able to initialize from its configured source, but its last two attempts to refresh has been failed (either from cache or from the ConfigCat CDN), it will become `degraded` because each refresh attempt will put an error to its `records` collection. This means, it's still able to evaluate feature flags, but it might work on a stale *config JSON*.

The root `status` is `healthy` if all of the SDKs are `healthy`. If any of the SDKs become `degraded` or `down`, the root will also switch to `degraded` (or `down` if each SDK is `down`).

You can control whether metrics collection should be enabled with the following configuration option:

| Option                                                                                                                                   | Default | Description                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------ |
| - YAML<br />- Environment variable```yaml
diag:
  status:
    enabled: <true|false>

``````shell
CONFIGCAT_DIAG_STATUS_ENABLED=<true|false>

``` | `true`  | Turns the hosting of the [status endpoint](#status) on the diagnostics HTTP server on/off. |

info

You can enable the status endpoint on the main HTTP port (default: `8050`) with the [HTTP configuration options](https://configcat.com/docs/advanced/proxy/proxy-overview.md#http).

## Metrics[​](#metrics "Direct link to Metrics")

If enabled, the Proxy collects various metrics. These can be either exported in Prometheus format or sent to an OTLP-compatible observability backend.

You can control whether metric collection should be enabled with the following configuration option:

| Option                                                                                                                                     | Default | Description                      |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------- | -------------------------------- |
| - YAML<br />- Environment variable```yaml
diag:
  metrics:
    enabled: <true|false>

``````shell
CONFIGCAT_DIAG_METRICS_ENABLED=<true|false>

``` | `true`  | Turns metrics collection on/off. |

### Prometheus[​](#prometheus-metrics "Direct link to Prometheus")

You can set up the Proxy to export metrics about its internal state in Prometheus format. These metrics are served on the `/metrics` endpoint.

#### Custom Metrics[​](#custom-metrics "Direct link to Custom Metrics")

| Name                              | Type    | Description                                                                                                                                                                                                |
| --------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `configcat_stream_connections`    | Gauge   | Number of active client connections per stream.<br /><br />Tags:- `sdk`: The SDK's identifier that handles the connection.<br />- `type`: `sse` or `grpc`.<br />- `flag`: The streamed feature flag's key. |
| `configcat_stream_msg_sent_total` | Counter | Total number of all messages sent with streaming.<br /><br />Tags:- `sdk`: The related SDK's identifier.<br />- `type`: `sse` or `grpc`.<br />- `flag`: The evaluated feature flag's key.                  |

The Proxy also exports metrics about the Go environment, e.g., `go_goroutines` or `go_memstats_alloc_bytes`, and process-related stats, e.g., `process_cpu_seconds_total`.

#### Integration[​](#integration "Direct link to Integration")

To integrate with Prometheus, put the following scrape config—that points to the Proxy—into your Prometheus configuration:

```yaml
scrape_configs:
  - job_name: configcat_proxy
    metrics_path: /metrics
    static_configs:
      - targets:
          - <proxy-host>:8051

```

#### Configuration Options[​](#configuration-options "Direct link to Configuration Options")

| Option                                                                                                                                                                 | Default | Description                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------ |
| - YAML<br />- Environment variable```yaml
diag:
  metrics:
    prometheus:
      enabled: <true|false>

``````shell
CONFIGCAT_DIAG_METRICS_PROMETHEUS_ENABLED=<true|false>

``` | `true`  | Turns the Prometheus compatible `/metrics` endpoint on the diagnostics HTTP server on/off. |

### OTLP[​](#otlp "Direct link to OTLP")

You can set up the Proxy to send metrics via [OTLP](https://opentelemetry.io/docs/specs/otlp/) to a compatible collector such as [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPEndpoint.html), [NewRelic](https://docs.newrelic.com/docs/opentelemetry/get-started/apm-monitoring/opentelemetry-apm-intro/), [DataDog](https://docs.datadoghq.com/opentelemetry/setup/otlp_ingest_in_the_agent), or [Honeycomb](https://docs.honeycomb.io/send-data/opentelemetry/).

#### Custom Metrics[​](#custom-metrics-1 "Direct link to Custom Metrics")

| Name                    | Type    | Description                                                                                                                                                                                                |
| ----------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `stream.connections`    | Gauge   | Number of active client connections per stream.<br /><br />Tags:- `sdk`: The SDK's identifier that handles the connection.<br />- `type`: `sse` or `grpc`.<br />- `flag`: The streamed feature flag's key. |
| `stream.msg.sent.total` | Counter | Total number of all messages sent with streaming.<br /><br />Tags:- `sdk`: The related SDK's identifier.<br />- `type`: `sse` or `grpc`.<br />- `flag`: The evaluated feature flag's key.                  |

#### Configuration Options[​](#configuration-options-1 "Direct link to Configuration Options")

| Option                                                                                                                                                                     | Default          | Description                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------ |
| - YAML<br />- Environment variable```yaml
diag:
  metrics:
    otlp:
      enabled: <true|false>

``````shell
CONFIGCAT_DIAG_METRICS_OTLP_ENABLED=<true|false>

```                 | `false`          | Turns the sending of metrics via OTLP on/off.                                              |
| - YAML<br />- Environment variable```yaml
diag:
  metrics:
    otlp:
      protocol: "<http|https|grpc>"

``````shell
CONFIGCAT_DIAG_METRICS_OTLP_PROTOCOL="<http|https|grpc>"

``` | `http`           | The protocol used to send metrics over OTLP. Possible values: `http`, `https`, and `grpc`. |
| - YAML<br />- Environment variable```yaml
diag:
  metrics:
    otlp:
      endpoint: "localhost:4318"

``````shell
CONFIGCAT_DIAG_METRICS_OTLP_ENDPOINT="localhost:4318"

```       | `localhost:4318` | The OTLP collector's endpoint.                                                             |

Additional OTLP-related options can be set by using the default [OpenTelemetry environment variables](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/). For example, to set custom headers for each OTLP request, you can use the `OTEL_EXPORTER_OTLP_HEADERS` environment variable.

```shell
OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer <token>"

```

## Traces[​](#traces "Direct link to Traces")

The Proxy is able to send traces via [OTLP](https://opentelemetry.io/docs/specs/otlp/) to a compatible collector such as [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPEndpoint.html), [NewRelic](https://docs.newrelic.com/docs/opentelemetry/get-started/apm-monitoring/opentelemetry-apm-intro/), [DataDog](https://docs.datadoghq.com/opentelemetry/setup/otlp_ingest_in_the_agent), or [Honeycomb](https://docs.honeycomb.io/send-data/opentelemetry/).

You can control whether trace collection should be enabled with the following configuration option:

| Option                                                                                                                                   | Default | Description                    |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------ |
| - YAML<br />- Environment variable```yaml
diag:
  traces:
    enabled: <true|false>

``````shell
CONFIGCAT_DIAG_TRACES_ENABLED=<true|false>

``` | `false` | Turns trace collection on/off. |

#### OTLP-related Options[​](#otlp-related-options "Direct link to OTLP-related Options")

| Option                                                                                                                                                                   | Default          | Description                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- | ----------------------------------------------------------------------------------------- |
| - YAML<br />- Environment variable```yaml
diag:
  traces:
    otlp:
      enabled: <true|false>

``````shell
CONFIGCAT_DIAG_TRACES_OTLP_ENABLED=<true|false>

```                 | `false`          | Turns the sending of traces via OTLP on/off.                                              |
| - YAML<br />- Environment variable```yaml
diag:
  traces:
    otlp:
      protocol: "<http|https|grpc>"

``````shell
CONFIGCAT_DIAG_TRACES_OTLP_PROTOCOL="<http|https|grpc>"

``` | `http`           | The protocol used to send traces over OTLP. Possible values: `http`, `https`, and `grpc`. |
| - YAML<br />- Environment variable```yaml
diag:
  traces:
    otlp:
      endpoint: "localhost:4318"

``````shell
CONFIGCAT_DIAG_TRACES_OTLP_ENDPOINT="localhost:4318"

```       | `localhost:4318` | The OTLP collector's endpoint.                                                            |

Additional OTLP-related options can be set by using the default [OpenTelemetry environment variables](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/). For example, to set custom headers for each OTLP request, you can use the `OTEL_EXPORTER_OTLP_HEADERS` environment variable.

```shell
OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer <token>"

```

## OpenTelemetry Instrumentation Libraries[​](#opentelemetry-instrumentation-libraries "Direct link to OpenTelemetry Instrumentation Libraries")

Metrics and traces are also exported by the following official OpenTelemetry instrumentation libraries:

* [otelhttp](https://github.com/open-telemetry/opentelemetry-go-contrib/tree/main/instrumentation/net/http/otelhttp)
* [otelgrpc](https://github.com/open-telemetry/opentelemetry-go-contrib/tree/main/instrumentation/google.golang.org/grpc/otelgrpc)
* [redisotel](https://github.com/redis/go-redis/tree/master/extra/redisotel)
* [otelmongo](https://github.com/open-telemetry/opentelemetry-go-contrib/tree/main/instrumentation/go.mongodb.org/mongo-driver/v2/mongo/otelmongo)
* [otelaws](https://github.com/open-telemetry/opentelemetry-go-contrib/tree/main/instrumentation/github.com/aws/aws-sdk-go-v2/otelaws)
