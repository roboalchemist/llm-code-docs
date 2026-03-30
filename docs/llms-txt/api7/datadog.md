# Source: https://docs.api7.ai/hub/datadog.md

# datadog

The `datadog` plugin supports the integration with [Datadog](https://www.datadoghq.com), one of the most used observability service for cloud applications. When enabled, the plugin pushes metrics to [DogStatsD](https://docs.datadoghq.com/developers/dogstatsd/?tab=hostagent) server, which comes bundled with the [Datadog agent](https://docs.datadoghq.com/agent), over UDP protocol.

## Metrics[â](#metrics "Direct link to Metrics")

The plugin exports the following metrics by default.

All metrics will be prefixed by the `namespace` configured in metadata. For example, if the `namespace` is configured to be `apisix`, you will see the `request.counter` metric exported as `apisix.request.counter` in Datadog.

| Name             | Type      | Description                                                                                           |
| ---------------- | --------- | ----------------------------------------------------------------------------------------------------- |
| request.counter  | counter   | Number of requests received.                                                                          |
| request.latency  | histogram | Time taken to process the request, in milliseconds.                                                   |
| upstream.latency | histogram | Time taken to proxy the request to the upstream server until a response is received, in milliseconds. |
| apisix.latency   | histogram | Time taken by APISIX agent to process the request, in milliseconds.                                   |
| ingress.size     | timer     | Request body size in bytes.                                                                           |
| egress.size      | timer     | Response body size in bytes.                                                                          |

## Tags[â](#tags "Direct link to Tags")

The plugin exports metrics with the following [tags](https://docs.datadoghq.com/getting_started/tagging).

When there are no suitable values for any particular tag, the tag will be omitted.

| Name                    | Description                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| route\_name             | Name of the route. If not present or if the attribute `prefer_name` is set to false, fall back to the route ID.                                                     |
| service\_name           | Name of the service. If not present or if the attribute `prefer_name` is set to false, fall back to the service ID.                                                 |
| consumer                | Username of the consumer if the route is connected to a consumer.                                                                                                   |
| balancer\_ip            | IP address of the upstream balancer that processes the current request.                                                                                             |
| response\_status        | HTTP response status code, such as `201`, `404`, or `503`.                                                                                                          |
| response\_status\_class | HTTP response status code class, such as `2xx`, `4xx`, or `5xx`. Available in APISIX from version 3.14.0 and API7 Enterprise from version 3.9.0.                    |
| scheme                  | Request scheme, such as HTTP and gRPC.                                                                                                                              |
| path                    | HTTP path pattern. Only available if the parameter `include_path` is set to `true`. Available in APISIX from version 3.14.0 and API7 Enterprise from version 3.9.0. |
| method                  | HTTP method. Only available if the attribute `include_method` is set to true. Available in APISIX from version 3.14.0 and API7 Enterprise from version 3.9.0.       |

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `datadog` plugin for different scenarios.

Before proceeding, please make sure you have installed [Datadog agent](https://docs.datadoghq.com/agent) which collects events and metrics from monitored objects and sends them to Datadog.

Start the Datadog agent in Docker:

```
docker run -d \
  --name dogstatsd-agent \
  -e DD_API_KEY=35ebe12345678dec56218930b79fdb4cf \
  -e DD_SITE="us5.datadoghq.com" \
  -e DD_HOSTNAME=apisix.quickstart \
  -e DD_DOGSTATSD_NON_LOCAL_TRAFFIC=true \
  -p 8125:8125/udp \
  datadog/dogstatsd:latest
```

â¶ `DD_API_KEY`: replace with your API key.

â· `DD_SITE`: replace with your Datadog site.

â¸ `DD_HOSTNAME`: replace with your hostname.

â¹ `DD_DOGSTATSD_NON_LOCAL_TRAFFIC`: set to true to listen to DogStatsD packets from other containers.

You can configure most options in the agentâs main configuration file `datadog.yaml` through environment variables, prefixed with `DD_`. For more information, see [agent environment variables](https://docs.datadoghq.com/agent/guide/environment-variables).

### Update Datadog Agent Address and Other Metadata[â](#update-datadog-agent-address-and-other-metadata "Direct link to Update Datadog Agent Address and Other Metadata")

By default, the plugin expects the DogStatsD server to be available at `127.0.0.1:8125`. To customize the address and other metadata, update the [plugin metadata](https://docs.api7.ai/hub/datadog/configuration.md#metadata) as such:

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/datadog" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "host": "192.168.0.90",
    "port": 8125,
    "namespace": "apisix",
    "constant_tags": [
      "source:apisix",
      "service:custom"
    ]
  }'
```

â¶ Replace with your private IP address if you are running both APISIX and Datadog agent in Docker.

â· Set to Datadog agent listening port.

â¸ Set namespace which prefixes all metrics.

â¹ Configure constant tags.

To reset to default configuration, send a request to the `datadog` plugin metadata with an empty body:

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/datadog" -X PUT -d '{}'
```

### Monitor Route Metrics[â](#monitor-route-metrics "Direct link to Monitor Route Metrics")

The example below shows how you can send the metrics of a particular route to Datadog.

Create a route with the `datadog` plugin and a few optional configuration options:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "datadog-route",
    "uri": "/anything",
    "plugins": {
      "datadog": {
        "batch_max_size" : 1,
        "max_retry_count": 0
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

â¶ `batch_max_size`: set to 1 to send the metric immediately.

â· `max_retry_count`: set to 0 to disallow retries if metrics were unsuccessfully sent.

Generate a few requests to the previously created route:

```
curl "http://127.0.0.1:9080/anything"
```

In Datadog, Select **Metrics** from the left menu and go to **Explorer**. Select `apisix.ingress.size.count` as the metric. You should see the count reflecting the number of requests generated:

![apisix-datadog-ingress-size-count](https://static.api7.ai/uploads/2024/01/17/Y0uHlIeS_dd-count.png)
