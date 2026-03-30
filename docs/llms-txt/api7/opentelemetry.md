# Source: https://docs.api7.ai/hub/opentelemetry.md

# OpenTelemetry

The `opentelemetry` plugin instruments APISIX and sends traces to OpenTelemetry collector based on the [OpenTelemetry specification](https://opentelemetry.io/docs/reference/specification/), in binary-encoded [OTLP over HTTP](https://opentelemetry.io/docs/reference/specification/protocol/otlp/#otlphttp).

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can work with the `opentelemetry` plugin for different scenarios.

### Enable `opentelemetry` Plugin[â](#enable-opentelemetry-plugin "Direct link to enable-opentelemetry-plugin")

If you are using API7 Enterprise, you may skip this section as there is no need to manually enable the plugin.

By default, the `opentelemetry` plugin is disabled in APISIX. To enable, add the plugin to your [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample) as such:

config.yaml

```
plugins:
  - ...
  - opentelemetry
```

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for changes to take effect.

### Send Traces to OpenTelemetry[â](#send-traces-to-opentelemetry "Direct link to Send Traces to OpenTelemetry")

The following example demonstrates how to trace requests to a route and send traces to OpenTelemetry.

Start an OpenTelemetry collector instance in Docker:

```
docker run -d --name otel-collector -p 4318:4318 otel/opentelemetry-collector-contrib
```

The collector should start listening on `127.0.0.1:4318`. If you would like to update the collector, you can configure the plugin metadata as such:

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/opentelemetry" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "collector": {
      "address": "127.0.0.1:4318"
    }
  }'
```

Create a route with `opentelemetry` plugin:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "otel-tracing-route",
    "uri": "/anything",
    "plugins": {
      "opentelemetry": {
        "sampler": {
          "name": "always_on"
        }
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org": 1
      }
    }
  }'
```

Send a request to the route:

```
curl "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

In OpenTelemetry collector's log, you should see information similar to the following:

```
2024-02-18T17:14:03.825Z info ResourceSpans #0
Resource SchemaURL: 
Resource attributes:
     -> telemetry.sdk.language: Str(lua)
     -> telemetry.sdk.name: Str(opentelemetry-lua)
     -> telemetry.sdk.version: Str(0.1.1)
     -> hostname: Str(e34673e24631)
     -> service.name: Str(APISIX)
ScopeSpans #0
ScopeSpans SchemaURL: 
InstrumentationScope opentelemetry-lua 
Span #0
    Trace ID       : fbd0a38d4ea4a128ff1a688197bc58b0
    Parent ID      : 
    ID             : af3dc7642104748a
    Name           : GET /anything
    Kind           : Server
    Start time     : 2024-02-18 17:14:03.763244032 +0000 UTC
    End time       : 2024-02-18 17:14:03.920229888 +0000 UTC
    Status code    : Unset
    Status message : 
Attributes:
     -> net.host.name: Str(127.0.0.1)
     -> http.method: Str(GET)
     -> http.scheme: Str(http)
     -> http.target: Str(/anything)
     -> http.user_agent: Str(curl/7.64.1)
     -> apisix.route_id: Str(otel-tracing-route)
     -> apisix.route_name: Empty()
     -> http.route: Str(/anything)
     -> http.status_code: Int(200)
{"kind": "exporter", "data_type": "traces", "name": "debug"}
```

To visualize these traces, you can export your telemetry to backend services, such as Zipkin and Prometheus. See [exporters](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter) for more details.

### Using Trace Variables in Logging[â](#using-trace-variables-in-logging "Direct link to Using Trace Variables in Logging")

The following example demonstrates how to configure the `opentelemetry` plugin to set the following built-in variables, which can be used in logger plugins or access logs:

* `opentelemetry_context_traceparent`: [trace parent](https://www.w3.org/TR/trace-context/#trace-context-http-headers-format) ID
* `opentelemetry_trace_id`: trace ID of the current span
* `opentelemetry_span_id`: span ID of the current span

Configure the plugin metadata to set `set_ngx_var` as true:

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/opentelemetry" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "set_ngx_var": true
  }'
```

Update the access log format in [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample) to use the `opentelemetry` plugin variables as such:

conf/config.yaml

```
nginx_config:
  http:
    enable_access_log: true
    access_log_format: '{"time": "$time_iso8601","opentelemetry_context_traceparent": "$opentelemetry_context_traceparent","opentelemetry_trace_id": "$opentelemetry_trace_id","opentelemetry_span_id": "$opentelemetry_span_id","remote_addr": "$remote_addr"}'
    access_log_format_escape: json
```

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for configuration changes to take effect.

You should see access log entries similar to the following when you generate requests:

```
{"time": "18/Feb/2024:15:09:00 +0000","opentelemetry_context_traceparent": "00-fbd0a38d4ea4a128ff1a688197bc58b0-8f4b9d9970a02629-01","opentelemetry_trace_id": "fbd0a38d4ea4a128ff1a688197bc58b0","opentelemetry_span_id": "af3dc7642104748a","remote_addr": "172.10.0.1"}
```
