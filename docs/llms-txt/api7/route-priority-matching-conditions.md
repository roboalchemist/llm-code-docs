# Source: https://docs.api7.ai/enterprise/3.8.x/best-practices/route-priority-matching-conditions.md

# Set Route Priority and Matching Conditions (Ingress Controller)

API7 Gateway supports configuring route priorities and advanced matching conditions to control how requests are routed to backend services.

This tutorial walks through how you can define route priority and matching rules with API7 Ingress Controller to achieve fine-grained request routing based on headers, query parameters, and more.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.8.x/getting-started/install-api7-ee.md).
2. Install [API7 Ingress Controller](https://docs.api7.ai/enterprise/3.8.x/deployment/ingress-controller.md) and start a gateway.

## Configure Route and Rules[â](#configure-route-and-rules "Direct link to Configure Route and Rules")

Create a Kubernetes manifest file for an HTTPRoute as such:

httpbin-route.yaml

```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: api7
  name: httpbin
spec:
  parentRefs:
  - name: apisix
  rules:
  - matches: 
    - path:
        type: PathPrefix
        value: /*
    backendRefs:
    - name: httpbin
      port: 80
```

Create another Kubernetes manifest file to configure route priority and request matching conditions on the targeted HTTPRoute:

route-policy.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: HTTPRoutePolicy
metadata:
  namespace: api7
  name: http-route-policy
spec:
  targetRefs:
  - group: gateway.networking.k8s.io
    kind: HTTPRoute
    name: httpbin
  priority: 10
  vars:
  - - http_x_test_name
    - ==
    - http-route-policy
  - - arg_test
    - ==
    - http-route-policy
```

â¶ Configure the `name` to be the target HTTPRoute metadata name.

â· Configure the priority for the target HTTPRoute. High numeric value corresponds to a higher priority.

â¸ Match requests with HTTP header `X-Test-Name: http-route-policy`

â¹ Match requests with query parameter `test=http-route-policy`.

A request will only be matched to this route if both conditions in `vars` are satisfied. For more information on these expressions, see [Built-In Variables](https://docs.api7.ai/enterprise/3.8.x/reference/built-in-variables.md) and [API7 Expressions](https://docs.api7.ai/enterprise/3.8.x/reference/expressions.md).

Apply the configurations to your cluster:

```
kubectl apply -f httpbin-route.yaml -f route-policy.yaml
```

## Configure Multiple Targets[â](#configure-multiple-targets "Direct link to Configure Multiple Targets")

If you would like to target routes in multiple HTTPRoute, you can configure more targets:

route-policy.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: HTTPRoutePolicy
metadata:
  namespace: api7
  name: http-route-policy
spec:
  targetRefs:
  - group: gateway.networking.k8s.io
    kind: HTTPRoute
    name: httpbin
  - group: gateway.networking.k8s.io
    kind: HTTPRoute
    name: httpbin-1
  priority: 10
  vars:
  - - http_x_test_name
    - ==
    - http-route-policy
  - - arg_test
    - ==
    - http-route-policy
```

## Verify[â](#verify "Direct link to Verify")

Expose the gateway service port to your local machine by port forwarding:

```
kubectl port-forward svc/api7-ee-3-gateway-gateway 9081:9081 &
```

Send a request to the route matching none of the conditions:

```
curl "http://127.0.0.1:9080/ip"
```

You should see a `HTTP/1.1 404 Not Found` response.

Send another request to the route matching one of the conditions:

```
curl "http://127.0.0.1:9080/ip?test=http-route-policy"
```

You should also see a `HTTP/1.1 404 Not Found` response.

Finally, send a request to the route matching all conditions:

```
curl "http://127.0.0.1:9080/ip?test=http-route-policy" -H "X-Test-Name: http-route-policy"
```

You should see a response similar to the following:

```
{
  "origin": "127.0.0.1"
}
```
