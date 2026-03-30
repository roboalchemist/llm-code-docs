# Source: https://docs.api7.ai/apisix/getting-started/load-balancing.md

# Load Balancing

Load balancing is a technique used to distribute network request loads. It is a key consideration in designing systems that need to handle a large volume of traffic, allowing for improved system performance, scalability, and reliability.

Apache APISIX supports a number of [load balancing algorithms](https://docs.api7.ai/apisix/key-concepts/upstreams.md#load-balancing), one of which is the weighted round-robin algorithm. This algorithm distributes incoming requests over a set of servers in a cyclical pattern.

In this tutorial, you will create a route with two upstream services and use the round-robin load balancing algorithm to load balance requests.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

1. Complete [Get APISIX](https://docs.api7.ai/apisix/getting-started/.md) to install APISIX in Docker.
2. Understand APISIX [routes](https://docs.api7.ai/apisix/key-concepts/routes.md) and [upstreams](https://docs.api7.ai/apisix/key-concepts/upstreams.md).
3. Install [ADC](https://docs.api7.ai/apisix/reference/adc.md) or [APISIX-MCP](https://docs.api7.ai/apisix/reference/apisix-mcp.md) if you are using these tools.

## Enable Load Balancing[â](#enable-load-balancing "Direct link to Enable Load Balancing")

* Admin API
* ADC
* APISIX-MCP

Create a route with two upstream services, [httpbin.org](https://httpbin.org/headers) and [mock.api7.ai](https://mock.api7.ai/headers), to distribute requests across. Both services respond with the request headers when receiving a request at `/headers`:

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "getting-started-headers",
  "uri": "/headers",
  "upstream" : {
    "type": "roundrobin",
    "nodes": {
      "httpbin.org:443": 1,
      "mock.api7.ai:443": 1
    },
    "pass_host": "node",
    "scheme": "https"
  }
}'
```

â¶ `type`: use `roundrobin` as the load balancing algorithm.

â· `nodes`: upstream services.

â¸ `pass_host`: use `node` to pass the host header to the upstream.

â¹ `scheme`: use `https` to enable TLS with upstream.

You should receive an `HTTP/1.1 201 Created` response if the route was created successfully.

Create an ADC configuration file containing a route pointing to two upstream services, [httpbin.org](https://httpbin.org/headers) and [mock.api7.ai](https://mock.api7.ai/headers). Both services will respond with the request headers when receiving a request at `/headers`.

adc.yaml

```
services:
  - name: httpbin Service
    routes:
      - uris:
          - /headers
        name: getting-started-headers
    upstream:
      type: roundrobin
      nodes:
        - host: mock.api7.ai
          port: 443
          weight: 1
        - host: httpbin.org
          port: 443
          weight: 1
      pass_host: node
      scheme: https
```

â¶ `type`: use `roundrobin` as the load balancing algorithm.

â· `nodes`: upstream services.

â¸ `pass_host`: use `node` to pass the host header to the upstream.

â¹ `scheme`: use `https` to enable TLS with upstream.

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

You will receive a similar response if the configuration was synchronized successfully:

```
[11:25:49 AM] [ADC] âº â  success   Sync configuration
[11:25:49 AM] [ADC] âº â  star      All is well, see you next time!
```

Enter the following prompt in your AI client:

```
Create a route with the ID getting-started-headers that matches requests to the URI /headers, and forward them to two upstream nodes â httpbin.org and mock.api7.ai â both on 443. Use roundrobin algorithm for load balancing. The route should use HTTPS scheme and pass the original host of each upstream node in the request.
```

You should see a response similar to the following:

```
Successfully created route "getting-started-headers" with:

URI: /headers
Two upstream nodes:
https://httpbin.org:443
https://mock.api7.ai:443
Round-robin load balancing
Original host headers preserved (pass_host: node)
Route ID: getting-started-headers
Status: Active (1)
Created at: 1744189246 (2025-04-09 09:00:46 UTC)
The route is now ready to distribute requests between the two upstream endpoints while maintaining the original host headers.
```

## Verify[â](#verify "Direct link to Verify")

* Admin API
* ADC
* APISIX-MCP

Generate 50 consecutive requests to APISIX `/headers` route to see the load-balancing effect:

```
resp=$(seq 50 | xargs -I{} curl "http://127.0.0.1:9080/headers" -sL) && \
  count_httpbin=$(echo "$resp" | grep "httpbin.org" | wc -l) && \
  count_mockapi7=$(echo "$resp" | grep "mock.api7.ai" | wc -l) && \
  echo httpbin.org: $count_httpbin, mock.api7.ai: $count_mockapi7
```

The command keeps count of the number of requests that were handled by the two services respectively. The output shows that requests were distributed over to the two services:

```
httpbin.org: 23, mock.api7.ai: 27
```

Generate 50 consecutive requests to APISIX `/headers` route to see the load-balancing effect:

```
resp=$(seq 50 | xargs -I{} curl "http://127.0.0.1:9080/headers" -sL) && \
  count_httpbin=$(echo "$resp" | grep "httpbin.org" | wc -l) && \
  count_mockapi7=$(echo "$resp" | grep "mock.api7.ai" | wc -l) && \
  echo httpbin.org: $count_httpbin, mock.api7.ai: $count_mockapi7
```

The command keeps count of the number of requests that were handled by the two services respectively. The output shows that requests were distributed over to the two services:

```
httpbin.org: 23, mock.api7.ai: 27
```

Enter the following prompt in your AI client:

```
Generate 50 consecutive requests to the APISIX /headers route to observe the load-balancing behavior, then count how many responses came from httpbin.org and how many came from mock.api7.ai.
```

You should see a response similar to the following:

```
Load balancing test results for 50 requests to /headers route:

httpbin.org responses: 23 (46%)
mock.api7.ai responses: 27 (54%)
The round-robin load balancing is working as expected, distributing requests between the two upstream nodes. The slight imbalance (46/54 split) could be due to connection timing or other network factors, but overall demonstrates effective load distribution.
```

The distribution of requests across services should be close to 1:1 but might not always result in a perfect 1:1 ratio. The slight deviation is due to APISIX operating with multiple workers.

## What's Next[â](#whats-next "Direct link to What's Next")

You have learned how to configure load balancing. In the next tutorial, you will learn how to configure key authentication.
