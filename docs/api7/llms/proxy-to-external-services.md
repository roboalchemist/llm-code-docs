# Source: https://docs.api7.ai/ingress-controller/proxy-to-external-services.md

# Proxy Requests to External Services

In this guide, you will learn how to configure routing to external services hosted outside the Kubernetes cluster using the Ingress Controller.

## Prerequisite[â](#prerequisite "Direct link to Prerequisite")

1. Complete [Set Up Ingress Controller and Gateway](https://docs.api7.ai/ingress-controller/set-up-ingress-controller-and-gateway.md).

## Create a Route[â](#create-a-route "Direct link to Create a Route")

Create a Kubernetes manifest file for a route that proxies requests to [httpbin.org](https://httpbin.org):

* Gateway API
* Ingress
* APISIX CRD

httpbin-route.yaml

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
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: httpbin-ip
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
      port: 80
```

httpbin-route.yaml

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
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  namespace: aic
  name: httpbin-ip
spec:
  ingressClassName: apisix
  rules:
  - http:
      paths:
      - path: /ip
        pathType: Exact
        backend:
          service:
            name: httpbin-external-domain
            port:
              number: 80
```

httpbin-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  ingressClassName: apisix
  externalNodes:
  - type: Domain
    name: httpbin.org
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: httpbin-ip
spec:
  ingressClassName: apisix
  http:
    - name: httpbin-ip
      match:
        paths:
          - /ip
      upstreams:
      - name: httpbin-external-domain
```

Apply the configurations to your cluster:

```
kubectl apply -f httpbin-route.yaml
```

## Verify[â](#verify "Direct link to Verify")

Expose the gatewayâs service port to your local machine:

```
# replace with your gatewayâs service name
kubectl port-forward svc/<gateway-service-name> 9080:80 &
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
