# Source: https://docs.api7.ai/apisix/getting-started/configure-routes.md

# Configure Routes

Apache APISIX provides flexible gateway management capabilities based on routes, in which routing paths and target upstreams are defined.

A *route* is a routing path to upstream targets. In [Apache APISIX](https://api7.ai/apisix), routes are responsible for matching client requests based on defined rules, loading and executing the corresponding plugins, as well as forwarding requests to the specified upstream services. A simple route can be set up with a path-matching URI and a corresponding upstream address.

An *upstream* is a set of target nodes with the same work. It defines a virtual host abstraction that performs load balancing on a given set of service nodes according to the configured rules.

This tutorial guides you through how to create a route and verify it. You will:

1. Create a [route](https://docs.api7.ai/apisix/key-concepts/routes.md) with a sample [upstream](https://docs.api7.ai/apisix/key-concepts/upstreams.md) that points to an httpbin service.
2. Send a request to the route to see how APISIX proxies the request.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

1. Complete [Get APISIX](https://docs.api7.ai/apisix/getting-started/.md) to install APISIX in Docker.
2. Install [ADC](https://docs.api7.ai/apisix/reference/adc.md) or [APISIX-MCP](https://docs.api7.ai/apisix/reference/apisix-mcp.md) if you are using these tools.

## Create a Route[â](#create-a-route "Direct link to Create a Route")

In this section, you will create a route that forwards client requests to [httpbin](https://httpbin.org), an HTTP request and response service.

* Admin API
* ADC
* APISIX-MCP

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "getting-started-ip",
  "uri": "/ip",
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "httpbin.org:80": 1
    }
  }
}'
```

You will receive an `HTTP/1.1 201 Created` response if the route was created successfully.

adc.yaml

```
services:
  - name: httpbin Service
    routes:
      - uris:
          - /ip
        name: getting-started-ip
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

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
Create a route with the ID getting-started-ip that matches requests to the URI /ip, and forwards them to an upstream using round-robin load balancing with a single node at httpbin.org on port 80.
```

You should see a response similar to the following:

```
Successfully created route "getting-started-ip" with the following configuration:

URI: /ip
Upstream: http://httpbin.org:80 (roundrobin load balancing)
Route ID: getting-started-ip
Status: Active (1)
Created at: 1744183830 (2025-04-09 07:30:30 UTC)
The route is now ready to accept requests at the /ip path, which will be forwarded to httpbin.org on port 80.
```

## Verify[â](#verify "Direct link to Verify")

* Admin API
* ADC
* APISIX-MCP

Send a request to the route:

```
curl "http://127.0.0.1:9080/ip"
```

You should see a response similar to the following:

```
{
  "origin": "183.94.122.205"
}
```

Send a request to the route:

```
curl "http://127.0.0.1:9080/ip"
```

You should see a response similar to the following:

```
{
  "origin": "183.94.122.205"
}
```

Enter the following prompt in your AI client:

```
Send a request to the route for verification.
```

You should see a response similar to the following:

```
Successfully verified the route "getting-started-ip":

Received HTTP 200 response from httpbin.org
Response shows origin IP address (192.168.107.1, 103.97.2.159)
The route is properly configured and forwarding requests to httpbin.org
The upstream service is responding correctly to requests
```

## What's Next[â](#whats-next "Direct link to What's Next")

This tutorial creates a route pointing to one upstream node. In the next tutorial, you will learn how to configure load balancing with multiple upstream nodes.
