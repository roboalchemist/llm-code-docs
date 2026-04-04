# Source: https://docs.api7.ai/ingress-controller/tls-and-mtls/proxy-to-https-upstream.md

# Proxy Requests to HTTPS Upstream Services

This guide explains how to use the Ingress Controller to configure the gateway to proxy requests to upstream services over HTTPS.

<!-- -->

## Prerequisite[â](#prerequisite "Direct link to Prerequisite")

1. Complete [Set Up Ingress Controller and Gateway](https://docs.api7.ai/ingress-controller/set-up-ingress-controller-and-gateway.md).

## Create a Route[â](#create-a-route "Direct link to Create a Route")

To proxy requests to an HTTPS upstream, create a route that forwards traffic to an upstream service over TLS. The following example configures a route to the public upstream service [httpbin.org](https://httpbin.org) on its HTTPS port `443`.

* Gateway API
* APISIX CRD

https-route.yaml

```
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  type: ExternalName
  externalName: httpbin.org
---
apiVersion: apisix.apache.org/v1alpha1
kind: BackendTrafficPolicy
metadata:
  namespace: aic
  name: passhost-node
spec:
  targetRefs:
  - name: httpbin-external-domain
    kind: Service
    group: ""
  passHost: node
  scheme: https
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: httpbin-tls
spec:
  parentRefs:
  - name: apisix
  rules:
  - matches:
    - path:
        type: Exact
        value: /ip
    backendRefs:
    - name: httpbin-external-domain
      port: 443
```

https-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  ingressClassName: apisix
  scheme: https
  passHost: node
  externalNodes:
  - type: Domain
    name: httpbin.org
    port: 443
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: httpbin-tls
spec:
  ingressClassName: apisix
  http:
    - name: httpbin-tls
      match:
        paths:
          - /ip
      upstreams:
      - name: httpbin-external-domain
```

Apply the configuration to your cluster:

```
kubectl apply -f https-route.yaml
```

## Verify[â](#verify "Direct link to Verify")

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/ip"
```

An `HTTP/1.1 200 OK` response verifies that the gateway has successfully established a connection and communicated with the upstream service over HTTPS.
