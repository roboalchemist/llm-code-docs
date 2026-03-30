# Source: https://docs.api7.ai/hub/loki-logger.md

# loki-logger

The `loki-logger` plugin pushes request and response logs in batches to [Grafana Loki](https://grafana.com/oss/loki/), via the [Loki HTTP API](https://grafana.com/docs/loki/latest/reference/loki-http-api/#loki-http-api) `/loki/api/v1/push`. When enabled, the plugin will serialize the request context information to [JSON objects](https://grafana.com/docs/loki/latest/api/#push-log-entries-to-loki) and add them to the queue, before they are pushed to Loki. The plugin also supports the customization of log formats.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `loki-logger` plugin for different scenarios.

To follow along the examples, start a sample Loki instance in Docker:

```
wget https://raw.githubusercontent.com/grafana/loki/v3.0.0/cmd/loki/loki-local-config.yaml -O loki-config.yaml
docker run --name loki -d -v $(pwd):/mnt/config -p 3100:3100 grafana/loki:3.2.1 -config.file=/mnt/config/loki-config.yaml
```

Additionally, start a Grafana instance to view and visualize the logs:

```
docker run -d --name=apisix-quickstart-grafana \
  -p 3000:3000 \
  grafana/grafana-oss
```

To connect Loki and Grafana, visit Grafana at [`http://localhost:3000`](http://localhost:3000). Under **Connections > Data sources**, add a new data source and select Loki. Your connection URL should follow the format of `http://{your_ip_address}:3100`. When saving the new data source, Grafana should also test the connection, and you are expected to see Grafana notifying the data source is successfully connected.

### Log Requests and Responses in Default Log Format[â](#log-requests-and-responses-in-default-log-format "Direct link to Log Requests and Responses in Default Log Format")

The following example demonstrates how you can configure the `loki-logger` plugin on a route to log requests and responses going through the route.

Create a route with the `loki-logger` plugin and configure the address of Loki:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "loki-logger-route",
    "uri": "/anything",
    "plugins": {
      "loki-logger": {
        "endpoint_addrs": ["http://192.168.1.5:3100"]
      }
    },
    "upstream": {
      "nodes": {
        "httpbin.org:80": 1
      },
      "type": "roundrobin"
    }
  }'
```

â¶ Replace with your IP address.

Send a few requests to the route to generate log entries:

```
curl "http://127.0.0.1:9080/anything"
```

You should receive `HTTP/1.1 200 OK` responses for all requests.

Navigate to the [Grafana explore view](http://localhost:3000/explore) and run a query `job = apisix`. You should see a number of logs corresponding to your requests, such as the following:

```
{
  "route_id": "loki-logger-route",
  "response": {
    "status": 200,
    "headers": {
      "date": "Fri, 03 Jan 2025 03:54:26 GMT",
      "server": "APISIX/3.13.0",
      "access-control-allow-credentials": "true",
      "content-length": "391",
      "access-control-allow-origin": "*",
      "content-type": "application/json",
      "connection": "close"
    },
    "size": 619
  },
  "start_time": 1735876466,
  "client_ip": "192.168.65.1",
  "service_id": "",
  "apisix_latency": 5.0000038146973,
  "upstream": "34.197.122.172:80",
  "upstream_latency": 666,
  "server": {
    "hostname": "0b9a772e68f8",
    "version": "3.13.0"
  },
  "request": {
    "headers": {
      "user-agent": "curl/8.6.0",
      "accept": "*/*",
      "host": "127.0.0.1:9080"
    },
    "size": 85,
    "method": "GET",
    "url": "http://127.0.0.1:9080/anything",
    "querystring": {},
    "uri": "/anything"
  },
  "latency": 671.0000038147
}
```

This verifies that Loki has been receiving logs from APISIX. You may also create dashboards in Grafana to further visualize and analyze the logs.

### Customize Log Format with Plugin Metadata[â](#customize-log-format-with-plugin-metadata "Direct link to Customize Log Format with Plugin Metadata")

The following example demonstrates how you can customize log format using [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md).

Create a route with the `loki-logger` plugin:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "loki-logger-route",
    "uri": "/anything",
    "plugins": {
      "loki-logger": {
        "endpoint_addrs": ["http://192.168.1.5:3100"]
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

Configure plugin metadata for `loki-logger`, which will update the log format for all routes of which requests would be logged:

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/loki-logger" -X PUT \
  -H 'X-API-KEY: ${ADMIN_API_KEY}' \
  -d '{
    "log_format": {
      "host": "$host",
      "client_ip": "$remote_addr",
      "route_id": "$route_id",
      "@timestamp": "$time_iso8601"
    }
  }'
```

Send a request to the route to generate a new log entry:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

Navigate to the [Grafana explore view](http://localhost:3000/explore) and run a query `job = apisix`. You should see a log entry corresponding to your request, similar to the following:

```
{
  "@timestamp":"2025-01-03T21:11:34+00:00",
  "client_ip":"192.168.65.1",
  "route_id":"loki-logger-route",
  "host":"127.0.0.1"
}
```

If the plugin on a route specifies a specific log format, it will take precedence over the log format specified in the plugin metadata. For instance, update the plugin on the previous route as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes/loki-logger-route" -X PATCH \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "plugins": {
      "loki-logger": {
        "log_format": {
          "route_id": "$route_id",
          "client_ip": "$remote_addr",
          "@timestamp": "$time_iso8601"
        }
      }
    }
  }'
```

Send a request to the route to generate a new log entry:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

Navigate to the [Grafana explore view](http://localhost:3000/explore) and re-run the query `job = apisix`. You should see a log entry corresponding to your request, consistent with the format configured on the route, similar to the following:

```
{
  "client_ip":"192.168.65.1",
  "route_id":"loki-logger-route",
  "@timestamp":"2025-01-03T21:19:45+00:00"
}
```

### Log Request Bodies Conditionally[â](#log-request-bodies-conditionally "Direct link to Log Request Bodies Conditionally")

The following example demonstrates how you can conditionally log request body.

Create a route with `loki-logger` as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "loki-logger-route",
    "uri": "/anything",
    "plugins": {
      "loki-logger": {
        "endpoint_addrs": ["http://192.168.1.5:3100"],
        "include_req_body": true,
        "include_req_body_expr": [["arg_log_body", "==", "yes"]]
      }
    },
    "upstream": {
      "nodes": {
        "httpbin.org:80": 1
      },
      "type": "roundrobin"
    }
  }'
```

â¶ `include_req_body`: set to true to include request body.

â· `include_req_body_expr`: only include request body if the URL query string `log_body` is `yes`.

Send a request to the route with a URL query string satisfying the condition:

```
curl -i "http://127.0.0.1:9080/anything?log_body=yes" -X POST -d '{"env": "dev"}'
```

Navigate to the [Grafana explore view](http://localhost:3000/explore) and run the query `job = apisix`. You should see a log entry corresponding to your request, where the request body is logged:

```
{
  "route_id": "loki-logger-route",
  ...,
  "request": {
    "headers": {
      ...
    },
    "body": "{\"env\": \"dev\"}",
    "size": 182,
    "method": "POST",
    "url": "http://127.0.0.1:9080/anything?log_body=yes",
    "querystring": {
      "log_body": "yes"
    },
    "uri": "/anything?log_body=yes"
  },
  "latency": 809.99994277954
}
```

Send a request to the route without any URL query string:

```
curl -i "http://127.0.0.1:9080/anything" -X POST -d '{"env": "dev"}'
```

Navigate to the [Grafana explore view](http://localhost:3000/explore) and run the query `job = apisix`. You should see a log entry corresponding to your request, where the request body is not logged:

```
{
  "route_id": "loki-logger-route",
  ...,
  "request": {
    "headers": {
      ...
    },
    "size": 169,
    "method": "POST",
    "url": "http://127.0.0.1:9080/anything",
    "querystring": {},
    "uri": "/anything"
  },
  "latency": 557.00016021729
}
```

info

If you have customized the `log_format` in addition to setting `include_req_body` or `include_resp_body` to `true`, the plugin would not include the bodies in the logs.

As a workaround, you may be able to use the NGINX variable `$request_body` in the log format, such as:

```
{
  "kafka-logger": {
    ...,
    "log_format": {"body": "$request_body"}
  }
}
```
