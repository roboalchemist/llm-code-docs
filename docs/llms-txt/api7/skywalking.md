# Source: https://docs.api7.ai/hub/skywalking.md

# skywalking

The `skywalking` plugin supports the integrating with [Apache SkyWalking](https://skywalking.apache.org) for request tracing.

SkyWalking uses its native Nginx Lua tracer to provide tracing, topology analysis, and metrics from both service and URI perspectives. APISIX supports HTTP protocol to interact with the SkyWalking server.

## Example[â](#example "Direct link to Example")

To follow along the example, start a storage, OAP and Booster UI with Docker Compose, following [Skywalking's documentation](https://skywalking.apache.org/docs/main/next/en/setup/backend/backend-docker/). Once set up, the OAP server should be listening on `12800` and you should be able to access the UI at <http://localhost:8080>.

Update APISIX [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample) to enable the `skywalking` plugin, which is disabled by default, and update the endpoint address:

config.yaml

```
plugins:
  - skywalking
  - ...

plugin_attr:
  skywalking:
    report_interval: 3
    service_name: APISIX
    service_instance_name: APISIX Instance
    endpoint_addr: http://192.168.2.103:12800
```

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for configuration changes to take effect.

### Trace All Requests[â](#trace-all-requests "Direct link to Trace All Requests")

The following example demonstrates how you can trace all requests passing through a route.

Create a route with `skywalking` and configure the sampling ratio to be 1 to trace all requests:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "skywalking-route",
    "uri": "/anything",
    "plugins": {
      "skywalking": {
        "sample_ratio": 1
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

Send a few requests to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive `HTTP/1.1 200 OK` responses.

In [Skywalking UI](http://localhost:8080), navigate to **General Service** > **Services**. You should see a service called `APISIX` with traces corresponding to your requests:

![SkyWalking APISIX traces](https://static.api7.ai/uploads/2025/01/15/UdwiO8NJ_skywalking-traces.png)

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
