# Source: https://docs.api7.ai/ingress-controller/proxy-to-weighted-backends.md

# Proxy Requests to Weighted Backends

Weighted routing enables load balancing by distributing traffic across multiple upstream services according to assigned weights. This allows you to direct more traffic to certain backends while sending less to others, optimizing resource use and improving service reliability.

In this guide, you will learn how to configure weighted routing using the Ingress Controller.

## Prerequisite[â](#prerequisite "Direct link to Prerequisite")

1. Complete [Set Up Ingress Controller and Gateway](https://docs.api7.ai/ingress-controller/set-up-ingress-controller-and-gateway.md).

## Start Example Upstream Services[â](#start-example-upstream-services "Direct link to Start Example Upstream Services")

Create a Kubernetes manifest file for two example upstream services `echo-1` and `echo-2`:

lb-two-http-echo.yaml

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: echo-1
  namespace: aic
spec:
  replicas: 1
  selector:
    matchLabels:
      app: echo-1
  template:
    metadata:
      labels:
        app: echo-1
    spec:
      containers:
      - name: http-echo
        image: hashicorp/http-echo:0.2.3
        args:
          - "-text=Hello from pod $(POD_NAME) in upstream 1"
        env:
          - name: POD_NAME
            valueFrom:
              fieldRef:
                fieldPath: metadata.name
        ports:
          - containerPort: 5678
---
apiVersion: v1
kind: Service
metadata:
  name: echo-1
  namespace: aic
spec:
  selector:
    app: echo-1
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5678
  type: ClusterIP
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: echo-2
  namespace: aic
spec:
  replicas: 1
  selector:
    matchLabels:
      app: echo-2
  template:
    metadata:
      labels:
        app: echo-2
    spec:
      containers:
      - name: http-echo
        image: hashicorp/http-echo:0.2.3
        args:
          - "-text=Hello from pod $(POD_NAME) in upstream 2"
        env:
          - name: POD_NAME
            valueFrom:
              fieldRef:
                fieldPath: metadata.name
        ports:
          - containerPort: 5678
---
apiVersion: v1
kind: Service
metadata:
  name: echo-2
  namespace: aic
spec:
  selector:
    app: echo-2
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5678
  type: ClusterIP
```

When requested at `/`, each will return its pod name and upstream number so that it can be identified.

Apply the configuration to your cluster:

```
kubectl apply -f lb-two-http-echo.yaml
```

## Create a Route[â](#create-a-route "Direct link to Create a Route")

Create a Kubernetes manifest to configure a route that load balances requests between two upstream services, based on the assigned weights:

* Gateway API
* APISIX CRD

lb-route.yaml

```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: lb-route
spec:
  parentRefs:
  - name: apisix
  rules:
  - matches:
    - path:
        type: Exact
        value: /
    backendRefs:
    - name: echo-1
      port: 80
      weight: 1
    - name: echo-2
      port: 80
      weight: 4
```

lb-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: lb-route
spec:
  ingressClassName: apisix
  http:
    - name: lb-route
      match:
        paths:
          - /
      backends:
        - serviceName: echo-1
          servicePort: 80
          weight: 1
        - serviceName: echo-2
          servicePort: 80
          weight: 4
```

Apply the configuration to your cluster:

```
kubectl apply -f lb-route.yaml
```

## Verify[â](#verify "Direct link to Verify")

Expose the gatewayâs service port to your local machine:

```
# replace with your gatewayâs service name
kubectl port-forward svc/<gateway-service-name> 9080:80 &
```

Generate 50 consecutive requests to the route to see the load-balancing effect:

```
resp=$(seq 50 | xargs -I{} curl "http://127.0.0.1:9080/" -sL) && \
  count_echo1=$(echo "$resp" | grep "upstream 1" | wc -l) && \
  count_echo2=$(echo "$resp" | grep "upstream 2" | wc -l) && \
  echo "echo-1: $count_echo1, echo-2: $count_echo2"
```

The command counts how many requests were handled by each of the two services, for example:

```
echo-1: 9, echo-2: 41
```

The distribution of requests across services should be close to 1:4 but might not always result in a perfect ratio. The slight deviation is due to the gateway operating with multiple workers.
