# Source: https://docs.api7.ai/hub/syslog.md

# syslog

The `syslog` plugin pushes request and response logs as JSON objects to syslog servers in batches and supports the customization of log formats.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `syslog` plugin for different scenarios.

To follow along the examples, you should have your syslog server running, or start an example rsyslog server in Docker:

```
docker run -d -p 514:514 --name example-rsyslog-server rsyslog/syslog_appliance_alpine
```

### Push Log to Syslog Server[â](#push-log-to-syslog-server "Direct link to Push Log to Syslog Server")

The following example demonstrates how you can enable the `syslog` plugin on a route, which logs client requests to the route and pushes logs to syslog server.

Create a route with `syslog` as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "syslog-route",
    "uri": "/anything",
    "plugins": {
      "syslog": {
        "host" : "172.0.0.1",
        "port" : 514,
        "flush_limit" : 1
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

â¶ `host`: replace with the address of your syslog server.

â· `port`: replace with the port of your syslog server.

â¸ `flush_limit`: set to 1 to push log to the syslog server immediately.

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

In the syslog server, you should see a log entry similar to the following:

```
{
  "response": {
    "status": 200,
    "headers": {
      "access-control-allow-credentials": "true",
      "connection": "close",
      "date": "Sat, 02 Mar 2024 00:14:19 GMT",
      "access-control-allow-origin": "*",
      "server": "APISIX/3.8.0",
      "content-type": "application/json",
      "content-length": "387"
    },
    "size": 614
  },
  "service_id": "",
  "client_ip": "172.19.0.1",
  "server": {
    "hostname": "eff61bf7be4d",
    "version": "3.8.0"
  },
  "upstream": "35.171.123.176:80",
  "apisix_latency": 13.999900817871,
  "request": {
    "method": "GET",
    "url": "http://127.0.0.1:9080/anything",
    "querystring": {},
    "size": 86,
    "uri": "/anything",
    "headers": {
      "host": "127.0.0.1:9080",
      "accept": "*/*",
      "user-agent": "curl/7.29.0"
    }
  },
  "route_id": "syslog-route",
  "upstream_latency": 165,
  "latency": 178.99990081787,
  "start_time": 1709334859598
}
```

### Customize Log Format With Plugin Metadata[â](#customize-log-format-with-plugin-metadata "Direct link to Customize Log Format With Plugin Metadata")

The following example demonstrates how you can customize log format using [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md). The log format configured in plugin metadata will apply to all syslog plugin instances.

Create a route with the `syslog` plugin:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "syslog-route",
    "uri": "/anything",
    "plugins": {
      "syslog": {
        "host" : "172.0.0.1",
        "port" : 514,
        "flush_limit" : 1
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

Configure plugin metadata for `syslog`:

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/syslog" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "log_format": {
      "host": "$host",
      "@timestamp": "$time_iso8601",
      "route_id": "$route_id",
      "client_ip": "$remote_addr",
      "resp_content_type": "$sent_http_Content_Type"
    }
  }'
```

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

In the syslog server, you should see a log entry similar to the following:

```
{
  "@timestamp": "2024-03-02T00:00:31+00:00",
  "resp_content_type": "application/json",
  "host": "127.0.0.1",
  "route_id": "syslog-route",
  "client_ip": "172.19.0.1"
}
```

### Log Request Bodies Conditionally[â](#log-request-bodies-conditionally "Direct link to Log Request Bodies Conditionally")

The following example demonstrates how you can conditionally log request body.

Create a route with the `syslog` plugin as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "syslog-route",
    "uri": "/anything",
    "plugins": {
      "syslog": {
        "host" : "172.0.0.1",
        "port" : 514,
        "flush_limit" : 1,
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
{
  "response": {
    "status": 200,
    "headers": {
      "connection": "close",
      "server": "APISIX/3.8.0",
      "date": "Sat, 02 Mar 2024 00:46:04 GMT",
      "access-control-allow-origin": "*",
      "access-control-allow-credentials": "true",
      "content-type": "application/json",
      "content-length": "545"
    },
    "size": 772
  },
  "service_id": "",
  "client_ip": "172.19.0.1",
  "server": {
    "hostname": "eff61bf7be4d",
    "version": "3.8.0"
  },
  "upstream": "35.171.123.176:80",
  "apisix_latency": 0,
  "request": {
    "method": "POST",
    "url": "http://127.0.0.1:9080/anything?log_body=yes",
    "querystring": {
      "log_body": "yes"
    },
    "size": 183,
    "body": "{\"env\": \"dev\"}",
    "uri": "/anything?log_body=yes",
    "headers": {
      "accept": "*/*",
      "user-agent": "curl/7.29.0",
      "host": "127.0.0.1:9080",
      "content-type": "application/x-www-form-urlencoded",
      "content-length": "14"
    }
  },
  "route_id": "syslog-route",
  "upstream_latency": 165,
  "latency": 164.99996185303,
  "start_time": 1709340364390
}
```

Send a request to the route without any URL query string:

```
curl -i "http://127.0.0.1:9080/post" -X POST -d '{"env": "dev"}'
```

You should not observe the request body in the log.

info

If you have customized the `log_format` in addition to setting `include_req_body` or `include_resp_body` to `true`, the plugin would not include the bodies in the logs.

As a workaround, you may be able to use the NGINX variable `$request_body` in the log format, such as:

```
{
  "syslog": {
    ...,
    "log_format": {"body": "$request_body"}
  }
}
```
