# Source: https://configcat.com/docs/advanced/proxy/monitoring.md

# Monitoring

The ConfigCat Proxy provides diagnostic data via its `/status` and a Prometheus-compatible `/metrics` endpoint. These endpoints are served on a specific port, so you can separate them from the public HTTP communication.

The following diagnostics related configuration options are available:

| Option                                                                                                                            | Default | Description                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------ |
| - YAML<br />- Environment variable```
diag:
  enabled: <true|false>
``````
CONFIGCAT_DIAG_ENABLED=<true|false>
```                     | `true`  | Turns the diagnostics HTTP server on/off.                                                  |
| - YAML<br />- Environment variable```
diag:
  port: 8051
``````
CONFIGCAT_DIAG_PORT=8051
```                                           | `8051`  | The port used by the diagnostics HTTP server.                                              |
| - YAML<br />- Environment variable```
diag:
  status:
    enabled: <true|false>
``````
CONFIGCAT_DIAG_STATUS_ENABLED=<true|false>
```   | `true`  | Turns the hosting of the [status endpoint](#status) on the diagnostics HTTP server on/off. |
| - YAML<br />- Environment variable```
diag:
  metrics:
    enabled: <true|false>
``````
CONFIGCAT_DIAG_METRICS_ENABLED=<true|false>
``` | `true`  | Turns the [Prometheus metrics](#prometheus-metrics) on the diagnostics HTTP server on/off. |

## Status Endpoint[​](#status "Direct link to Status Endpoint")

The Proxy provides status information (health check) about its components on the following endpoint:

GETOPTIONS/status

The Proxy regularly checks whether the underlying SDKs can communicate with their configured source and with the cache. This endpoint returns the actual state of these checks.

**Responses**:

* 200: The status returned successfully.
* 204: In response to an `OPTIONS` request.

**Example Response**:

```
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

note

You can enable the status endpoint on the main HTTP port (default: `8050`) with the [HTTP configuration options](https://configcat.com/docs/docs/advanced/proxy/proxy-overview/.md#http).

## Prometheus Metrics[​](#prometheus-metrics "Direct link to Prometheus Metrics")

You can set up the Proxy to export metrics about its internal state in Prometheus format. These metrics are served via the `/metrics` endpoint.

The following metrics are exported:

| Name                                          | Type      | Description                                                                                                                                                                                                              |
| --------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `configcat_http_request_duration_seconds`     | Histogram | Histogram of Proxy HTTP response time in seconds.<br /><br />Tags:- `route`: The request's URL path.<br />- `method`: The request's HTTP method.<br />- `status`: The response's HTTP status.                            |
| `configcat_grpc_rpc_duration_seconds`         | Histogram | Histogram of RPC call latency in seconds.<br /><br />Tags:- `method`: The RPCs name.<br />- `code`: The RPCs response code.                                                                                              |
| `configcat_sdk_http_request_duration_seconds` | Histogram | Histogram of ConfigCat CDN HTTP response time in seconds.<br /><br />Tags:- `sdk`: The SDK's identifier that initiated the request.<br />- `route`: The request's URL path.<br />- `status`: The response's HTTP status. |
| `configcat_stream_connections`                | Gauge     | Number of active client connections per stream.<br /><br />Tags:- `sdk`: The SDK's identifier that handles the connection.<br />- `type`: `sse` or `grpc`.<br />- `flag`: The streamed feature flag's key.               |
| `configcat_stream_msg_sent_total`             | Counter   | Total number of all messages sent with streaming.<br /><br />Tags:- `sdk`: The related SDK's identifier.<br />- `type`: `sse` or `grpc`.<br />- `flag`: The evaluated feature flag's key.                                |

info

The Proxy also exports metrics about the Go environment, e.g., `go_goroutines` or `go_memstats_alloc_bytes`, and process-related stats, e.g., `process_cpu_seconds_total`.

To integrate with Prometheus, put the following scrape config—that points to the Proxy—into your Prometheus configuration:

```
scrape_configs:
  - job_name: configcat_proxy
    metrics_path: /metrics
    static_configs:
      - targets:
          - <proxy-host>:8051
```
