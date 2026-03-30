# Source: https://docs.api7.ai/apisix/how-to-guide/authentication/secure-websocket-traffic.md

# Secure WebSocket Traffic

WebSocket is a widely used protocol designed to facilitate real-time, bidirectional communication between a client and a server over a single TCP connection. Unlike traditional HTTP, WebSocket enables persistent communication, allowing data to flow seamlessly in both directions without the overhead of repeated HTTP requests. This makes it ideal for applications such as live chat, collaborative tools, multiplayer games, and other interactive platforms that require low-latency data exchange.

WebSocket is efficient for real-time communication, but it has a limitation: it does not support setting custom headers during the HTTP handshake, including the commonly used `Authorization` header. This creates a challenge when securing WebSocket connections, as the protocol itself lacks built-in authentication mechanisms. Without proper safeguards, WebSocket endpoints could become vulnerable to unauthorized access and abuse.

APISIX addresses this gap for WebSocket traffic by enabling authentication mechanisms during the initial handshake. In this guide, you will learn how to configure APISIX to authenticate and proxy WebSocket connections.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Install [websocat](https://github.com/vi/websocat) to establish WebSocket connections with a WebSocket server.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Start WebSocket Sample Server[â](#start-websocket-sample-server "Direct link to Start WebSocket Sample Server")

Start a [sample upstream server](https://hub.docker.com/r/jmalloc/echo-server) with WebSocket support.

```
docker run -d \
  -p 8080:8080 \
  --name websocket-server \
  --network=apisix-quickstart-net \
  jmalloc/echo-server
```

The server has a WebSocket endpoint at `/.ws` that echoes back any message received.

## Create a Route[â](#create-a-route "Direct link to Create a Route")

Create a route to the sample upstream server, and enable WebSocket and `key-auth` plugin. You can use other authentication plugins as well.

* Admin API
* ADC

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "ws-route",
  "uri": "/.ws",
  "enable_websocket": true,
  "plugins": {
    "key-auth": {}
  },
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "websocket-server:8080": 1
    }
  }
}'
```

route.yaml

```
services:
  - name: websocket Service
    routes:
      - uris:
          - /.ws
        name: ws-route
        enable_websocket: true
        plugins:
          key-auth: {}
    upstream:
      type: roundrobin
      nodes:
        - host: websocket-server:8080
          port: 8080
          weight: 1
```

Synchronize the configuration to APISIX:

```
adc sync -f route.yaml
```

## Create Consumers[â](#create-consumers "Direct link to Create Consumers")

Create at least one consumer and their credential.

* Admin API
* ADC

Create a consumer `john`:

```
curl -i "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT -d '
{
  "username": "john"
}'
```

Configure `key-auth` credential for `john`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/john/credentials" -X PUT -d '
{
  "id": "cred-john-key-auth",
  "plugins": {
    "key-auth": {
      "key": "john-key"
    }
  }
}'
```

Create a consumer `john` and configure their `key-auth` credential:

consumer.yaml

```
consumers:
  - username: john
    credentials:
      - name: john-key
        type: key-auth
        config:
          key: john-key
```

Synchronize the configurations to APISIX:

```
adc sync -f route.yaml -f consumer.yaml
```

## Verify Connections[â](#verify-connections "Direct link to Verify Connections")

Establish a connection with the WebSocket server through the route, without any credentials:

```
websocat "ws://127.0.0.1:9080/.ws"
```

You should see a `401 Unauthorized` response.

Establish a connection with the WebSocket server through the route with `john`'s credential:

```
websocat "ws://127.0.0.1:9080/.ws" -H 'apikey: john-key'
```

You should see the server is ready to serve incoming requests. Send a "hello" message in the terminal. You should see the WebSocket server echoes back the same message:

```
Request served by 510852d98edc
hello
hello
```

You can continue to send more messages and the WebSocket server will echo back any message you sent. This shows the bidirectional connection is successful and persistent.

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned how to authenticate and proxy WebSocket connections with APISIX. If you would like to rate-limit the number of WebSocket connections, see the [`limit-conn`](https://docs.api7.ai/hub/limit-conn.md) plugin doc for more information.
