# Source: https://docs.api7.ai/hub/public-api.md

# public-api

The `public-api` plugin exposes an internal API endpoint, making it publicly accessible. One of the primary use cases of this plugin is to expose internal endpoints created by other plugins.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `public-api` in different scenarios.

### Expose Prometheus Metrics at Custom Endpoint[â](#expose-prometheus-metrics-at-custom-endpoint "Direct link to Expose Prometheus Metrics at Custom Endpoint")

The following example demonstrates how you can disable the Prometheus export server that, by default, exposes an endpoint on port `9091`, and expose APISIX Prometheus metrics on a new public API endpoint on port `9080`, which APISIX uses to listen to other client requests.

You will also configure the route such that the internal endpoint `/apisix/prometheus/metrics` is exposed at a custom endpoint.

caution

If a large quantity of metrics is being collected, the plugin could take up a significant amount of CPU resources for metric computations and negatively impact the processing of regular requests.

To address this issue, APISIX uses [privileged agent](https://github.com/openresty/lua-resty-core/blob/master/lib/ngx/process.md#enable_privileged_agent) and offloads the metric computations to a separate process. This optimization applies automatically if you use the metric endpoint configured under `plugin_attr.prometheus.export_addr` in the configuration file. If you expose the metric endpoint with the `public-api` plugin, you will not benefit from this optimization.

Disable the Prometheus export server in the configuration file and [reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for changes to take effect:

conf/config.yaml

```
plugin_attr:
  prometheus:
    enable_export_server: false
```

Next, create a route with `public-api` plugin and expose a public API endpoint for APISIX metrics:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "prometheus-metrics",
    "uri": "/prometheus_metrics",
    "plugins": {
      "public-api": {
        "uri": "/apisix/prometheus/metrics"
      }
    }
  }'
```

â¶ Set the route `uri` to the custom endpoint path.

â· Set the plugin `uri` to the internal endpoint to be exposed.

Send a request to the custom metrics endpoint:

```
curl "http://127.0.0.1:9080/prometheus_metrics"
```

You should see an output similar to the following:

```
# HELP apisix_http_requests_total The total number of client requests since APISIX started
# TYPE apisix_http_requests_total gauge
apisix_http_requests_total 1
# HELP apisix_nginx_http_current_connections Number of HTTP connections
# TYPE apisix_nginx_http_current_connections gauge
apisix_nginx_http_current_connections{state="accepted"} 1
apisix_nginx_http_current_connections{state="active"} 1
apisix_nginx_http_current_connections{state="handled"} 1
apisix_nginx_http_current_connections{state="reading"} 0
apisix_nginx_http_current_connections{state="waiting"} 0
apisix_nginx_http_current_connections{state="writing"} 1
...
```

### Expose Batch Requests Endpoint[â](#expose-batch-requests-endpoint "Direct link to Expose Batch Requests Endpoint")

The following example demonstrates how you can use the `public-api` plugin to expose an endpoint for the `batch-requests` plugin, which is used for assembling multiple requests into one single request before sending them to the gateway.

Create a sample route to httpbin's `/anything` endpoint for verification purpose:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "httpbin-anything",
    "uri": "/anything",
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

Create a route with `public-api` plugin and set the route `uri` to the internal endpoint to be exposed:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "batch-requests",
    "uri": "/apisix/batch-requests",
    "plugins": {
      "public-api": {}
    }
  }'
```

Send a pipelined request consisting of a GET and a POST request to the exposed batch requests endpoint:

```
curl "http://127.0.0.1:9080/apisix/batch-requests" -X POST -d '
{
  "pipeline": [
    {
      "method": "GET",
      "path": "/anything"
    },
    {
      "method": "POST",
      "path": "/anything",
      "body": "a post request"
    }
  ]
}'
```

You should receive responses from both requests, similar to the following:

```
[
  {
    "reason": "OK",
    "body": "{\n  \"args\": {}, \n  \"data\": \"\", \n  \"files\": {}, \n  \"form\": {}, \n  \"headers\": {\n    \"Accept\": \"*/*\", \n    \"Host\": \"127.0.0.1\", \n    \"User-Agent\": \"curl/8.6.0\", \n    \"X-Amzn-Trace-Id\": \"Root=1-67b6e33b-5a30174f5534287928c54ca9\", \n    \"X-Forwarded-Host\": \"127.0.0.1\"\n  }, \n  \"json\": null, \n  \"method\": \"GET\", \n  \"origin\": \"192.168.107.1, 43.252.208.84\", \n  \"url\": \"http://127.0.0.1/anything\"\n}\n",
    "headers": {
      ...
    },
    "status": 200
  },
  {
    "reason": "OK",
    "body": "{\n  \"args\": {}, \n  \"data\": \"a post request\", \n  \"files\": {}, \n  \"form\": {}, \n  \"headers\": {\n    \"Accept\": \"*/*\", \n    \"Content-Length\": \"14\", \n    \"Host\": \"127.0.0.1\", \n    \"User-Agent\": \"curl/8.6.0\", \n    \"X-Amzn-Trace-Id\": \"Root=1-67b6e33b-0eddcec07f154dac0d77876f\", \n    \"X-Forwarded-Host\": \"127.0.0.1\"\n  }, \n  \"json\": null, \n  \"method\": \"POST\", \n  \"origin\": \"192.168.107.1, 43.252.208.84\", \n  \"url\": \"http://127.0.0.1/anything\"\n}\n",
    "headers": {
      ...
    },
    "status": 200
  }
]
```

If you would like to expose the batch requests endpoint at a custom endpoint, create a route with `public-api` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "batch-requests",
    "uri": "/batch-requests",
    "plugins": {
      "public-api": {
        "uri": "/apisix/batch-requests"
      }
    }
  }'
```

â¶ Set the route `uri` to the custom endpoint path.

â· Set the plugin `uri` to the internal endpoint to be exposed.

The batch requests endpoint should now be exposed as `/batch-requests`, instead of `/apisix/batch-requests`.

Send a pipelined request consisting of a GET and a POST request to the exposed batch requests endpoint:

```
curl "http://127.0.0.1:9080/batch-requests" -X POST -d '
{
  "pipeline": [
    {
      "method": "GET",
      "path": "/anything"
    },
    {
      "method": "POST",
      "path": "/anything",
      "body": "a post request"
    }
  ]
}'
```

You should receive responses from both requests, similar to the following:

```
[
  {
    "reason": "OK",
    "body": "{\n  \"args\": {}, \n  \"data\": \"\", \n  \"files\": {}, \n  \"form\": {}, \n  \"headers\": {\n    \"Accept\": \"*/*\", \n    \"Host\": \"127.0.0.1\", \n    \"User-Agent\": \"curl/8.6.0\", \n    \"X-Amzn-Trace-Id\": \"Root=1-67b6e33b-5a30174f5534287928c54ca9\", \n    \"X-Forwarded-Host\": \"127.0.0.1\"\n  }, \n  \"json\": null, \n  \"method\": \"GET\", \n  \"origin\": \"192.168.107.1, 43.252.208.84\", \n  \"url\": \"http://127.0.0.1/anything\"\n}\n",
    "headers": {
      ...
    },
    "status": 200
  },
  {
    "reason": "OK",
    "body": "{\n  \"args\": {}, \n  \"data\": \"a post request\", \n  \"files\": {}, \n  \"form\": {}, \n  \"headers\": {\n    \"Accept\": \"*/*\", \n    \"Content-Length\": \"14\", \n    \"Host\": \"127.0.0.1\", \n    \"User-Agent\": \"curl/8.6.0\", \n    \"X-Amzn-Trace-Id\": \"Root=1-67b6e33b-0eddcec07f154dac0d77876f\", \n    \"X-Forwarded-Host\": \"127.0.0.1\"\n  }, \n  \"json\": null, \n  \"method\": \"POST\", \n  \"origin\": \"192.168.107.1, 43.252.208.84\", \n  \"url\": \"http://127.0.0.1/anything\"\n}\n",
    "headers": {
      ...
    },
    "status": 200
  }
]
```
