# Source: https://docs.api7.ai/ingress-controller/proxy-udp-traffic.md

# Proxy UDP Traffic by Port

This guide explains how to define routing rules for UDP traffic based on the incoming port through the Ingress Controller. A UDP echo server is used as the example upstream.

## Prerequisite[â](#prerequisite "Direct link to Prerequisite")

1. Complete [Set Up Ingress Controller and Gateway](https://docs.api7.ai/ingress-controller/set-up-ingress-controller-and-gateway.md).

## Start an Example Upstream Service[â](#start-an-example-upstream-service "Direct link to Start an Example Upstream Service")

Create a Kubernetes manifest for a UDP echo server that listens on port `9000`:

udp-echo.yaml

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: udp-echo
  namespace: aic
spec:
  replicas: 1
  selector:
    matchLabels:
      app: udp-echo
  template:
    metadata:
      labels:
        app: udp-echo
    spec:
      containers:
        - name: udp-echo
          image: python:3-alpine
          command: ["python", "-u", "-c"]
          args:
            - |
              import socket
              sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
              sock.bind(('', 9000))
              print("UDP echo server listening on port 9000")
              while True:
                  data, addr = sock.recvfrom(1024)
                  sock.sendto(data, addr)
          ports:
            - containerPort: 9000
              protocol: UDP
---
apiVersion: v1
kind: Service
metadata:
  name: udp-echo
  namespace: aic
spec:
  selector:
    app: udp-echo
  ports:
    - name: udp
      port: 9000
      targetPort: 9000
      protocol: UDP
```

Apply the configuration to your cluster:

```
kubectl apply -f udp-echo.yaml
```

## Enable Gateway Stream Proxy[â](#enable-gateway-stream-proxy "Direct link to Enable Gateway Stream Proxy")

Upgrade your gateway to enable stream mode and set UDP listening port `9300`:

* APISIX Gateway
* API7 Gateway

```
helm upgrade -n aic apisix apisix/apisix \
  --set ... \ # add other parameters
  --set "service.stream.enabled=true" \
  --set "service.stream.udp[0]=9300"
```

```
helm upgrade -n aic api7-ee-3-gateway api7/gateway \
  --set ... \ # add other parameters
  --set "gateway.stream.enabled=true" \
  --set "gateway.stream.only=false" \
  --set "gateway.stream.udp[0]=9300"
```

## Configure UDP Routing[â](#configure-udp-routing "Direct link to Configure UDP Routing")

In this section, you will configure a route that listens for UDP traffic on port `9300`.

* Gateway API
* APISIX CRD

Update your Gateway manifest file to define a listener for UDP traffic:

gateway.yaml

```
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  namespace: aic
  name: apisix
spec:
  gatewayClassName: apisix
  listeners:
  - name: http
    protocol: HTTP
    port: 80
  - name: udp
    protocol: UDP
    port: 9300
    allowedRoutes:
      kinds:
      - kind: UDPRoute
  infrastructure:
    parametersRef:
      group: apisix.apache.org
      kind: GatewayProxy
      name: apisix-config
```

Create a Kubernetes manifest for a UDPRoute:

udp-route.yaml

```
apiVersion: gateway.networking.k8s.io/v1alpha2
kind: UDPRoute
metadata:
  name: stream-route-udp
  namespace: aic
spec:
  parentRefs:
  - name: apisix
    sectionName: udp
  rules:
  - backendRefs:
    - name: udp-echo
      port: 9000
```

Apply the configuration to your cluster:

```
kubectl apply -f gateway.yaml -f udp-route.yaml
```

Create a Kubernetes manifest file for a stream route:

udp-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  name: stream-route-udp
  namespace: aic
spec:
  ingressClassName: apisix
  stream:
    - name: stream-route-udp
      protocol: UDP
      match:
        ingressPort: 9300
      backend:
        serviceName: udp-echo
        servicePort: 9000
```

Apply the configuration to your cluster:

```
kubectl apply -f udp-route.yaml
```

## Verify[â](#verify "Direct link to Verify")

Since `kubectl port-forward` supports only TCP and cannot be used to verify UDP proxying, run a temporary pod inside the cluster and use it to send UDP packets to the gateway for testing:

```
kubectl run -it --rm test-udp-proxy --image=busybox --namespace=aic -- /bin/sh
```

Once inside the pod, execute the following command to send a UDP datagram to the gateway:

```
echo "UDP Testing" | nc -u -w1 <gateway-service-name> 9300
```

You should see the message `UDP Testing` echoed back.
