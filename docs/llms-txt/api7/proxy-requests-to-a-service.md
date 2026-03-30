# Source: https://docs.api7.ai/ingress-controller/proxy-requests-to-a-service.md

# Proxy Requests to a Service

This tutorial shows you how to create a basic route with the Ingress Controller that proxies requests to a sample service running in the cluster and verify that the routing functions correctly.

## Prerequisite[â](#prerequisite "Direct link to Prerequisite")

1. Complete [Set Up Ingress Controller and Gateway](https://docs.api7.ai/ingress-controller/set-up-ingress-controller-and-gateway.md).

## Start an Example Upstream Service[â](#start-an-example-upstream-service "Direct link to Start an Example Upstream Service")

Start an [HTTPBIN](https://kennethreitz.org/software/websites/httpbin) service named `httpbin` in the current namespace to use as the sample upstream service:

```
kubectl apply -f https://raw.githubusercontent.com/apache/apisix-ingress-controller/refs/heads/v2.0.0/examples/httpbin/deployment.yaml
```

## Create a Route[â](#create-a-route "Direct link to Create a Route")

Create a Kubernetes manifest file for a route that will proxy requests to the HTTPBIN sample upstream service:

* Gateway API
* Ingress
* APISIX CRD

httpbin-route.yaml

```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: getting-started-ip
spec:
  parentRefs:
  - name: apisix
  rules:
  - matches:
    - path:
        type: Exact
        value: /ip
    backendRefs:
    - name: httpbin
      port: 80
```

httpbin-route.yaml

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  namespace: aic
  name: getting-started-ip
spec:
  ingressClassName: apisix
  rules:
    - http:
        paths:
          - backend:
              service:
                name: httpbin
                port:
                  number: 80
            path: /ip
            pathType: Exact
```

httpbin-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: getting-started-ip
spec:
  ingressClassName: apisix
  http:
    - name: getting-started-ip
      match:
        paths:
          - /ip
      backends:
        - serviceName: httpbin
          servicePort: 80
```

Apply the configurations to your cluster:

```
kubectl apply -f httpbin-route.yaml
```

## Verify Routing[â](#verify-routing "Direct link to Verify Routing")

Expose the gatewayâs service port to your local machine:

```
# replace with your gatewayâs service name
kubectl port-forward svc/<gateway-service-name> 9080:80 &
```

Send a request to the route:

```
curl "http://127.0.0.1:9080/ip"
```

You should see a response of the following:

```
{
  "origin": "127.0.0.1"
}
```

## Delete the Route[â](#delete-the-route "Direct link to Delete the Route")

To remove the previously created route, run the following command:

```
kubectl delete -f httpbin-route.yaml
```

## Next Step[â](#next-step "Direct link to Next Step")

You have now learned the basics of proxying requests with a route. Next, you will explore the broader capabilities provided by the plugin ecosystem.
