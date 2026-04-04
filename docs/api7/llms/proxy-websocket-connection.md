# Source: https://docs.api7.ai/ingress-controller/proxy-websocket-connection.md

# Proxy WebSocket Connection

WebSocket is a protocol that provides a bidirectional channel between a client and a server over a single TCP connection. It revolutionized real-time communication on the web where data can be sent and received in real-time. The protocol is widely used in a variety of interactive applications, including chat applications, collaborative editing tools, multiplayer gaming, and more.

This guide will show you how to configure the gateway to proxy WebSocket connections using the Ingress Controller. If you would like to apply rate limiting to WebSocket connections, see the [`limit-conn`](https://docs.api7.ai/hub/limit-conn.md#rate-limit-websocket-connections) plugin.

## Prerequisite[â](#prerequisite "Direct link to Prerequisite")

1. Complete [Set Up Ingress Controller and Gateway](https://docs.api7.ai/ingress-controller/set-up-ingress-controller-and-gateway.md).

## Start an Example Upstream Service[â](#start-an-example-upstream-service "Direct link to Start an Example Upstream Service")

Create a Kubernetes manifest file for the deployment and service of a WebSocket server. The server has a WebSocket endpoint at `/.ws` that echoes back any message received.

ws-echo.yaml

```
apiVersion: apps/v1
kind: Deployment
metadata:
  namespace: aic
  name: websocket-server
spec:
  replicas: 1
  selector:
    matchLabels:
      app: websocket-server
  template:
    metadata:
  namespace: aic
      labels:
        app: websocket-server
    spec:
      containers:
      - name: echo-server
        image: jmalloc/echo-server
        ports:
        - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: websocket-server
spec:
  selector:
    app: websocket-server
  ports:
  - protocol: TCP
    port: 8080
    targetPort: 8080
  type: ClusterIP
```

Apply the configuration to your cluster:

```
kubectl apply -f ws-echo.yaml
```

## Create a Route[â](#create-a-route "Direct link to Create a Route")

Create a route to the WebSocket upstream service:

* Gateway API
* APISIX CRD

ws-route.yaml

```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: ws-route
spec:
  parentRefs:
  - name: apisix
  rules:
  - matches: 
    - path:
        type: Exact
        value: /.ws
    backendRefs:
    - name: websocket-server
      port: 8080
```

ws-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: ws-route
spec:
  ingressClassName: apisix
  http:
    - name: ws-route
      match:
        paths:
          - /.ws
      websocket: true
      backends:
      - serviceName: websocket-server
        servicePort: 8080
```

Apply the configuration to your cluster:

```
kubectl apply -f ws-route.yaml
```

## Verify Connections[â](#verify-connections "Direct link to Verify Connections")

Expose the gatewayâs service port to your local machine:

```
# replace with your gatewayâs service name
kubectl port-forward svc/<gateway-service-name> 9080:80 &
```

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
