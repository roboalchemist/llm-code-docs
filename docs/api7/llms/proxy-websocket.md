# Source: https://docs.api7.ai/apisix/how-to-guide/traffic-management/proxy-websocket.md

# Proxy WebSocket Connections

WebSocket is a protocol that provides a bidirectional channel between a client and a server over a single TCP connection. It revolutionizes real-time communication on the web where data can be sent and received in real-time. The protocol is widely used in a variety of interactive applications, including chat applications, collaborative editing tools, multiplayer gaming, and more.

This guide will show you how you can use APISIX to proxy WebSocket connections.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Install [websocat](https://github.com/vi/websocat) to establish WebSocket connections with a WebSocket server.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Start WebSocket Sample Server[â](#start-websocket-sample-server "Direct link to Start WebSocket Sample Server")

Start a [sample upstream server](https://hub.docker.com/r/jmalloc/echo-server) with WebSocket support:

```
docker run -d \
  -p 8080:8080 \
  --name websocket-server \
  --network=apisix-quickstart-net \
  jmalloc/echo-server
```

The server has a WebSocket endpoint at `/.ws` that echoes back any message received.

## Create Route in APISIX[â](#create-route-in-apisix "Direct link to Create Route in APISIX")

Create a route to the sample upstream server and enable WebSocket:

* Admin API
* ADC

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "ws-route",
  "uri": "/.ws",
  "enable_websocket": true,
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "websocket-server:8080": 1
    }
  }
}'
```

adc.yaml

```
services:
  - name: websocket Service
    routes:
      - uris:
          - /.ws
        name: ws-route
        enable_websocket: true
    upstream:
      type: roundrobin
      nodes:
        - host: websocket-server:8080
          port: 8080
          weight: 1
```

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

## Verify Connections[â](#verify-connections "Direct link to Verify Connections")

Establish a connection with the WebSocket server through the route:

```
websocat "ws://127.0.0.1:9080/.ws"
```

Send a "hello" message in the terminal. You should see the WebSocket server echoes back the same message:

```
Request served by 1cd244052136
hello
hello
```

You can continue to send more messages and the WebSocket server will echo back any message you sent. This shows the bidirectional connection is successful and persistent.

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned how to proxy WebSocket connections with APISIX. If you would like to rate limit the number of WebSocket connections, see the `limit-conn` plugin doc for [more information](https://docs.api7.ai/hub/limit-conn.md#rate-limit-websocket-connections).
