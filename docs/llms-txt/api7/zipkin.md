# Source: https://docs.api7.ai/hub/zipkin.md

# zipkin

[Zipkin](https://github.com/openzipkin/zipkin) is an open-source distributed tracing system. The `zipkin` plugin instruments APISIX and sends traces to Zipkin based on the [Zipkin API specification](https://zipkin.io/pages/instrumenting.html).

The plugin can also sends traces to other compatible collectors, such as [Jaeger](https://www.jaegertracing.io/docs/1.51/getting-started/#migrating-from-zipkin) and [Apache SkyWalking](https://skywalking.apache.org/docs/main/latest/en/setup/backend/zipkin-trace/#zipkin-receiver), both of which support Zipkin [v1](https://zipkin.io/zipkin-api/zipkin-api.yaml) and [v2](https://zipkin.io/zipkin-api/zipkin2-api.yaml) APIs.

## Examples[â](#examples "Direct link to Examples")

The examples below shows different use cases for using the `zipkin` plugin.

### Send Traces to Zipkin[â](#send-traces-to-zipkin "Direct link to Send Traces to Zipkin")

The following example demonstrates how to trace requests to a route and send traces to Zipkin using [Zipkin API v2](https://zipkin.io/zipkin-api/zipkin2-api.yaml). You will also understand the differences between span version 2 and span version 1.

Start a Zipkin instance in Docker:

```
docker run -d --name zipkin -p 9411:9411 openzipkin/zipkin
```

Create a route with `zipkin` and use the default span version 2:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "zipkin-tracing-route",
    "uri": "/anything",
    "plugins": {
      "zipkin": {
        "endpoint": "http://127.0.0.1:9411/api/v2/spans",
        "sample_ratio": 1,
        "span_version": 2
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

â¶ Adjust the IP address as needed for Zipkin HTTP endpoint.

â· Configure the sample ratio to 1 to trace every request.

â¸ Set span version to 2.

Send a request to the route:

```
curl "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response similar to the following:

```
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Host": "127.0.0.1", 
    "User-Agent": "curl/7.64.1", 
    "X-Amzn-Trace-Id": "Root=1-65af2926-497590027bcdb09e34752b78", 
    "X-B3-Parentspanid": "347dddedf73ec176", 
    "X-B3-Sampled": "1", 
    "X-B3-Spanid": "429afa01d0b0067c", 
    "X-B3-Traceid": "aea58f4b490766eccb08275acd52a13a", 
    "X-Forwarded-Host": "127.0.0.1"
  }, 
  ...
}
```

Navigate to the Zipkin web UI at <http://127.0.0.1:9411/zipkin> and click **Run Query**, you should see a trace corresponding to the request:

![trace-from-request](https://static.api7.ai/uploads/2024/01/23/MaXhacYO_zipkin-run-query.png)

Click **Show** to see more tracing details:

![v2-trace-spans](https://static.api7.ai/uploads/2024/01/23/3SmfFq9f_trace-details.png)

Note that with span version 2, every traced request creates the following spans:

```
request
âââ proxy
âââ response
```

where `proxy` represents the time from the beginning of the request to the beginning of `header_filter`, and `response` represents the time from the beginning of `header_filter` to the beginning of `log`.

Now, update the plugin on the route to use span version 1:

```
curl "http://127.0.0.1:9180/apisix/admin/routes/zipkin-tracing-route" -X PATCH \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "plugins": {
      "zipkin": {
        "span_version": 1
      }
    }
  }'
```

Send another request to the route:

```
curl "http://127.0.0.1:9080/anything"
```

In the Zipkin web UI, you should a new trace with details similar to the following:

![v1-trace-spans](https://static.api7.ai/uploads/2024/01/23/OPw2sTPa_v1-trace-spans.png)

Note that with the older span version 1, every traced request creates the following spans:

```
request
âââ rewrite
âââ access
âââ proxy
    âââ body_filter
```

### Send Traces to Jaeger[â](#send-traces-to-jaeger "Direct link to Send Traces to Jaeger")

The following example demonstrates how to trace requests to a route and send traces to Jaeger.

Start a Jaeger instance in Docker:

```
docker run -d --name jaeger \
  -e COLLECTOR_ZIPKIN_HOST_PORT=9411 \
  -p 16686:16686 \
  -p 9411:9411 \
  jaegertracing/all-in-one
```

Create a route with `zipkin`:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "zipkin-tracing-route",
    "uri": "/anything",
    "plugins": {
      "zipkin": {
        "endpoint": "http://127.0.0.1:9411/api/v2/spans",
        "sample_ratio": 1
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

â¶ Adjust the IP address as needed for Zipkin HTTP endpoint.

â· Configure the sample ratio to 1 to trace every request.

Send a request to the route:

```
curl "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

Navigate to the Jaeger web UI at <http://127.0.0.1:16686>, select APISIX as the service, and click **Find Traces**, you should see a trace corresponding to the request:

![jaeger-traces](https://static.api7.ai/uploads/2024/01/23/X6QdLN3l_jaeger.png)

Similarly, you should find more span details once you click into a trace:

![jaeger-details](https://static.api7.ai/uploads/2024/01/23/iP9fXI2A_jaeger-details.png)

### Using Trace Variables in Logging[â](#using-trace-variables-in-logging "Direct link to Using Trace Variables in Logging")

The following example demonstrates how to configure the `zipkin` plugin to set the following built-in variables, which can be used in logger plugins or access logs:

* `zipkin_context_traceparent`: [trace parent](https://www.w3.org/TR/trace-context/#trace-context-http-headers-format) ID
* `zipkin_trace_id`: trace ID of the current span
* `zipkin_span_id`: span ID of the current span

Update the [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample) as such:

conf/config.yaml

```
nginx_config:
  http:
    enable_access_log: true
    access_log_format: '{"time": "$time_iso8601","zipkin_context_traceparent": "$zipkin_context_traceparent","zipkin_trace_id": "$zipkin_trace_id","zipkin_span_id": "$zipkin_span_id","remote_addr": "$remote_addr"}'
    access_log_format_escape: json
plugin_attr:
  zipkin:
    set_ngx_var: true
```

â¶ `access_log_format`: customize the access log format to use the `zipkin` plugin variables.

â· `set_ngx_var`: set `zipkin` variables.

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for configuration changes to take effect.

You should see access log entries similar to the following when you generate requests:

```
{"time": "23/Jan/2024:06:28:00 +0000","zipkin_context_traceparent": "00-61bce33055c56f5b9bec75227befd142-13ff3c7370b29925-01","zipkin_trace_id": "61bce33055c56f5b9bec75227befd142","zipkin_span_id": "13ff3c7370b29925","remote_addr": "172.28.0.1"}
```
