# Source: https://docs.api7.ai/hub/http-logger.md

# http-logger

The `http-logger` plugin pushes request and response logs as JSON objects to HTTP(S) servers in batches and supports the customization of log formats.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `http-logger` plugin for different scenarios.

To follow along the examples, start a mock HTTP logging endpoint using [mockbin](https://mockbin.io) and note down the mockbin URL.

### Log Requests in Default Log Format[â](#log-requests-in-default-log-format "Direct link to Log Requests in Default Log Format")

The following example demonstrates how you can configure the `http-logger` plugin on a route to log information of requests hitting the route.

Create a route with the `http-logger` plugin and configure the plugin with your server URI:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "http-logger-route",
    "uri": "/anything",
    "plugins": {
      "http-logger": {
        "uri": "https://669f05eb10ca49f18763e023312c3d77.api.mockbin.io/"
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
curl "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response. In your mockbin, you should see a log entry similar to the following:

```
[
  {
    "upstream": "3.213.1.197:80",
    "server": {
      "hostname": "7d8d831179d4",
      "version": "3.9.0"
    },
    "start_time": 1718291190508,
    "client_ip": "192.168.65.1",
    "response": {
      "status": 200,
      "headers": {
        "server": "APISIX/3.9.0",
        "content-length": "390",
        "access-control-allow-credentials": "true",
        "connection": "close",
        "date": "Thu, 13 Jun 2024 15:06:31 GMT",
        "access-control-allow-origin": "*",
        "content-type": "application/json"
      },
      "size": 617
    },
    "latency": 1200.0000476837,
    "upstream_latency": 1133,
    "apisix_latency": 67.000047683716,
    "request": {
      "url": "http://127.0.0.1:9080/anything",
      "querystring": {},
      "method": "GET",
      "uri": "/anything",
      "headers": {
        "accept": "*/*",
        "user-agent": "curl/8.6.0",
        "host": "127.0.0.1:9080"
      },
      "size": 85
    },
    "service_id": "",
    "route_id": "http-logger-route"
  }
]
```

### Log Request and Response Headers With Plugin Metadata[â](#log-request-and-response-headers-with-plugin-metadata "Direct link to Log Request and Response Headers With Plugin Metadata")

The following example demonstrates how you can customize log format using [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) and [built-in variables](https://docs.api7.ai/apisix/reference/built-in-variables.md) to log specific headers from request and response.

In APISIX, [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) is used to configure the common metadata fields of all plugin instances of the same plugin. It is useful when a plugin is enabled across multiple resources and requires a universal update to their metadata fields.

First, create a route with the `http-logger` plugin and configure the plugin with your server URI:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "http-logger-route",
    "uri": "/anything",
    "plugins": {
      "http-logger": {
        "uri": "https://669f05eb10ca49f18763e023312c3d77.api.mockbin.io/"
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

Next, configure the plugin metadata for `http-logger`:

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/http-logger" -X PUT \
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
curl "http://127.0.0.1:9080/anything" -H "env: dev"
```

You should receive an `HTTP/1.1 200 OK` response. In your mockbin, you should see a log entry similar to the following:

```
[
  {
    "route_id": "http-logger-route",
    "client_ip": "192.168.65.1",
    "@timestamp": "2024-06-13T15:19:34+00:00",
    "host": "127.0.0.1",
    "env": "dev",
    "resp_content_type": "application/json"
  }
]
```

### Log Request Bodies Conditionally[â](#log-request-bodies-conditionally "Direct link to Log Request Bodies Conditionally")

The following example demonstrates how you can conditionally log request body.

Create a route with the `http-logger` plugin as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "http-logger-route",
    "uri": "/anything",
    "plugins": {
      "http-logger": {
        "uri": "https://669f05eb10ca49f18763e023312c3d77.api.mockbin.io/",
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

You should see the request body logged:

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

You should not observe the request body in the log.

info

If you have customized the `log_format` in addition to setting `include_req_body` or `include_resp_body` to `true`, the plugin would not include the bodies in the logs.

As a workaround, you may be able to use the NGINX variable `$request_body` in the log format, such as:

```
{
  "http-logger": {
    ...,
    "log_format": {"body": "$request_body"}
  }
}
```
