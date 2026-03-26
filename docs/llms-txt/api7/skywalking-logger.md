# Source: https://docs.api7.ai/hub/skywalking-logger.md

# skywalking-logger

The `skywalking-logger` plugin pushes request and response logs as JSON objects to SkyWalking OAP server in batches and supports the customization of log formats.

If there is an existing tracing context, it sets up the trace-log correlation automatically and relies on [SkyWalking Cross Process Propagation Headers Protocol](https://skywalking.apache.org/docs/main/next/en/api/x-process-propagation-headers-v3/).

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `skywalking-logger` plugin for different scenarios.

To follow along the example, start a storage, OAP and Booster UI with Docker Compose, following [Skywalking's documentation](https://skywalking.apache.org/docs/main/next/en/setup/backend/backend-docker/). Once set up, the OAP server should be listening on `12800` and you should be able to access the UI at <http://localhost:8080>.

### Log Requests in Default Log Format[â](#log-requests-in-default-log-format "Direct link to Log Requests in Default Log Format")

The following example demonstrates how you can configure the `skywalking-logger` plugin on a route to log information of requests hitting the route.

Create a route with the `skywalking-logger` plugin and configure the plugin with your OAP server URI:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "skywalking-logger-route",
    "uri": "/anything",
    "plugins": {
      "skywalking-logger": {
        "endpoint_addr": "http://192.168.2.103:12800"
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

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

In [Skywalking UI](http://localhost:8080), navigate to **General Service** > **Services**. You should see a service called `APISIX` with a log entry corresponding to your request:

```
{
  "upstream_latency": 674,
  "request": {
    "method": "GET",
    "headers": {
      "user-agent": "curl/8.6.0",
      "host": "127.0.0.1:9080",
      "accept": "*/*"
    },
    "url": "http://127.0.0.1:9080/anything",
    "size": 85,
    "querystring": {},
    "uri": "/anything"
  },
  "client_ip": "192.168.65.1",
  "route_id": "skywalking-logger-route",
  "start_time": 1736945107345,
  "upstream": "3.210.94.60:80",
  "server": {
    "version": "3.13.0",
    "hostname": "7edbcebe8eb3"
  },
  "service_id": "",
  "response": {
    "size": 619,
    "status": 200,
    "headers": {
      "content-type": "application/json",
      "date": "Thu, 16 Jan 2025 12:45:08 GMT",
      "server": "APISIX/3.13.0",
      "access-control-allow-origin": "*",
      "connection": "close",
      "access-control-allow-credentials": "true",
      "content-length": "391"
    }
  },
  "latency": 764.9998664856,
  "apisix_latency": 90.999866485596
}
```

### Log Request and Response Headers With Plugin Metadata[â](#log-request-and-response-headers-with-plugin-metadata "Direct link to Log Request and Response Headers With Plugin Metadata")

The following example demonstrates how you can customize log format using [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) and [built-in variables](https://docs.api7.ai/apisix/reference/built-in-variables.md) to log specific headers from request and response.

In APISIX, [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) is used to configure the common metadata fields of all plugin instances of the same plugin. It is useful when a plugin is enabled across multiple resources and requires a universal update to their metadata fields.

First, create a route with the `skywalking-logger` plugin and configure the plugin with your OAP server URI:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "skywalking-logger-route",
    "uri": "/anything",
    "plugins": {
      "skywalking-logger": {
        "endpoint_addr": "http://192.168.2.103:12800"
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

Next, configure the plugin metadata for `skywalking-logger`:

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/skywalking-logger" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "log_format": {
      "host": "$host",
      "@timestamp": "$time_iso8601",
      "client_ip": "$remote_addr",
      "env": "$http_env",
      "resp_content_type": "$sent_http_Content_Type"
    }
  }'
```

â¶ log the custom request header `env`.

â· log the response header `Content-Type`.

Send a request to the route with the `env` header:

```
curl -i "http://127.0.0.1:9080/anything" -H "env: dev"
```

You should receive an `HTTP/1.1 200 OK` response. In [Skywalking UI](http://localhost:8080), navigate to **General Service** > **Services**. You should see a service called `APISIX` with a log entry corresponding to your request:

```
[
  {
    "route_id": "skywalking-logger-route",
    "client_ip": "192.168.65.1",
    "@timestamp": "2025-01-16T12:51:53+00:00",
    "host": "127.0.0.1",
    "env": "dev",
    "resp_content_type": "application/json"
  }
]
```

### Log Request Bodies Conditionally[â](#log-request-bodies-conditionally "Direct link to Log Request Bodies Conditionally")

The following example demonstrates how you can conditionally log request body.

Create a route with the `skywalking-logger` plugin as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "skywalking-logger-route",
    "uri": "/anything",
    "plugins": {
      "skywalking-logger": {
        "endpoint_addr": "http://192.168.2.103:12800",
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

You should receive an `HTTP/1.1 200 OK` response. In [Skywalking UI](http://localhost:8080), navigate to **General Service** > **Services**. You should see a service called `APISIX` with a log entry corresponding to your request, with the request body logged:

```
[
  {
    "request": {
      "url": "http://127.0.0.1:9080/anything?log_body=yes",
      "querystring": {
        "log_body": "yes"
      },
      "uri": "/anything?log_body=yes",
      ...,
      "body": "{\"env\": \"dev\"}",
    },
    ...
  }
]
```

Send a request to the route without any URL query string:

```
curl -i "http://127.0.0.1:9080/anything" -X POST -d '{"env": "dev"}'
```

You should not observe a log entry without the request body.

info

If you have customized the `log_format` in addition to setting `include_req_body` or `include_resp_body` to `true`, the plugin would not include the bodies in the logs.

As a workaround, you may be able to use the NGINX variable `$request_body` in the log format, such as:

```
{
  "skywalking-logger": {
    ...,
    "log_format": {"body": "$request_body"}
  }
}
```

### Associate Traces with Logs[â](#associate-traces-with-logs "Direct link to Associate Traces with Logs")

The following example demonstrates how you can configure the `skywalking-logger` plugin on a route to log information of requests hitting the route.

Create a route with the `skywalking-logger` plugin and configure the plugin with your OAP server URI:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "skywalking-logger-route",
    "uri": "/anything",
    "plugins": {
      "skywalking": {
        "sample_ratio": 1
      },
      "skywalking-logger": {
        "endpoint_addr": "http://192.168.2.103:12800"
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

Generate a few requests to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive `HTTP/1.1 200 OK` responses.

In [Skywalking UI](http://localhost:8080), navigate to **General Service** > **Services**. You should see a service called `APISIX` with a trace corresponding to your request, where you can view the associated logs:

![trace context](https://static.api7.ai/uploads/2025/01/16/soUpXm6b_trace-view-logs.png)

![associated log](https://static.api7.ai/uploads/2025/01/16/XD934LvU_associated-logs.png)
