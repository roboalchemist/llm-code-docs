# Source: https://docs.api7.ai/apisix/how-to-guide/observability/trace-with-zipkin.md

# Trace Requests with Zipkin

Traces are one of the three pillars of observability, along with metrics and logs. A trace tracks the journey of a request as it traverses through various parts of a system. It is an effective mechanism that helps developers and administrators monitor system performance, identify bottlenecks, and improve user experience.

This guide will walk you through how to trace requests to APISIX using the `zipkin` plugin and send traces to [Zipkin](https://zipkin.io).

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Start Zipkin Instance[â](#start-zipkin-instance "Direct link to Start Zipkin Instance")

Start a Zipkin instance:

```
docker run -d --name zipkin -p 9411:9411 openzipkin/zipkin
```

## Configure APISIX[â](#configure-apisix "Direct link to Configure APISIX")

Enable `zipkin` globally and create a sample route to generate traces. Alternatively, you can enable the plugin on a route.

* Admin API
* ADC

Configure `zipkin` to be a global plugin:

```
curl "http://127.0.0.1:9180/apisix/admin/global_rules/zipkin" -X PUT -d '
{
  "plugins": {
    "zipkin": {
      "endpoint": "http://192.168.42.145:9411/api/v2/spans",
      "sample_ratio": 1
    }
  }
}'
```

â¶ Set to the `/spans` [Zipkin endpoint](https://zipkin.io/zipkin-api). Update with your IP address.

â· Configure the sample ratio to 1 to trace every request.

Create a sample route where requests through the route will be traced:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "zipkin-tracing-route",
  "uri": "/anything",
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "httpbin.org": 1
    }
  }
}'
```

Configure `zipkin` to be a global plugin and create a sample route where requests through the route will be traced:

adc-route.yaml

```
global_rules:
  zipkin:
    endpoint: "http://192.168.42.145:9411/api/v2/spans"
    sample_ratio: 1
services:
  - name: httpbin Service
    routes:
      - uris:
          - /anything
        name: zipkin-tracing-route
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          weight: 1
```

â¶ Set to the `/spans` [Zipkin endpoint](https://zipkin.io/zipkin-api).

â· Configure the sample ratio to 1 to trace every request.

Synchronize the configuration to APISIX:

```
adc sync -f adc-route.yaml
```

## Trace Requests[â](#trace-requests "Direct link to Trace Requests")

Send a request to the route:

```
curl "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response similar to the following, with trace information in the headers:

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
    "X-Amzn-Trace-Id": "Root=1-65b1dd40-339dc8832b4b78d36703cbc0", 
    "X-B3-Parentspanid": "6ca01ad46bdb0198", 
    "X-B3-Sampled": "1", 
    "X-B3-Spanid": "f02ab1a9b2d5c3e4", 
    "X-B3-Traceid": "ef5b16781c7ad00ea2e3efa6f784031a", 
    "X-Forwarded-Host": "127.0.0.1"
  }, 
  ...
}
```

Navigate to the Zipkin web UI at <http://127.0.0.1:9411/zipkin> and click **Run Query**, you should see a trace corresponding to the request:

![trace-from-request](https://static.api7.ai/uploads/2024/01/23/MaXhacYO_zipkin-run-query.png)

Click **Show** to see more tracing details:

![v2-trace-spans](https://static.api7.ai/uploads/2024/01/23/3SmfFq9f_trace-details.png)

By default, the plugin uses span version 2, where every traced request has `proxy` and `response` spans. More specifically:

* `proxy` represents the time from the beginning of the request to the beginning of `header_filter`
* `response` represents the time from the beginning of `header_filter` to the beginning of `log`

To understand the differences between different span versions, see the [plugin doc](https://docs.api7.ai/hub/zipkin.md#send-traces-to-zipkin).

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now integrated Zipkin with APISIX for tracing. In addition to sending traces to Zipkin, the `zipkin` plugin can also send traces to [Jaeger](https://www.jaegertracing.io/docs/1.51/getting-started/#migrating-from-zipkin) and other compatible collectors. See the `zipkin` [plugin doc](https://docs.api7.ai/hub/zipkin.md#send-traces-to-jaeger) for more details.
