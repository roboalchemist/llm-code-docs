# Source: https://docs.api7.ai/ingress-controller/detect-upstream-protocol-appprotocol.md

# Detect Upstream Protocol with appProtocol

`appProtocol` is an optional field on a Service port that indicates the type of traffic the backend expects. The Ingress Controller can use this value to automatically determine the upstream protocol.

This guide explains how the Ingress Controller reads the `appProtocol` field from Kubernetes Services and translates it into the appropriate upstream configuration in the gateway.

## Supported appProtocol Values[â](#supported-appprotocol-values "Direct link to Supported appProtocol Values")

The Ingress Controller supports the following `appProtocol` values for Service ports:

| Value               | Explanation                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------- |
| `http`              | The option sets the upstream scheme to `http`.                                                |
| `https`             | The option sets the upstream scheme to `https`.                                               |
| `kubernetes.io/ws`  | The option sets the upstream scheme to `http` and `enable_websocket` to `true` on the route.  |
| `kubernetes.io/wss` | The option sets the upstream scheme to `https` and `enable_websocket` to `true` on the route. |

When `appProtocol` is not specified, `http` is used as the default protocol.

## Kubernetes Service Definition[â](#kubernetes-service-definition "Direct link to Kubernetes Service Definition")

Suppose you want to expose an upstream service `httpbin`. You can define the Service to indicate the expected protocol for each port using `appProtocol`:

httpbin-service.yaml

```
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: httpbin
spec:
  selector:
    app: httpbin
  ports:
    - name: http
      port: 80
      targetPort: 80
      appProtocol: http
    - name: https
      port: 443
      targetPort: 443
      appProtocol: https
```

## Create a Route[â](#create-a-route "Direct link to Create a Route")

Create a route that references a specific Service port. The Ingress Controller reads the `appProtocol` value associated with the referenced port and uses it to configure the upstream protocol automatically.

In this example, the route will point to the Service port `443`, which was configured with `appProtocol: https`. The upstream scheme will then be automatically set to `https` without any additional configuration.

* Gateway API
* Ingress
* APISIX CRD

httpbin-https.yaml

```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: httpbin-route
spec:
  parentRefs:
  - name: apisix
  rules:
  - matches:
    - path:
        type: Exact
        value: /anything
    backendRefs:
    - name: httpbin
      port: 443
```

httpbin-https.yaml

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  namespace: aic
  name: httpbin-route
spec:
  ingressClassName: apisix
  rules:
    - http:
        paths:
          - path: /anything
            pathType: Exact
            backend:
              service:
                name: httpbin
                port:
                  number: 443
```

httpbin-https.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: httpbin-route
spec:
  ingressClassName: apisix
  http:
  - name: httpbin-route
    match:
      paths:
      - /anything
    backends:
    - serviceName: httpbin
      servicePort: 443
```

Apply the configuration to your cluster:

```
kubectl apply -f httpbin-https.yaml
```

## Verify Upstream Scheme[â](#verify-upstream-scheme "Direct link to Verify Upstream Scheme")

If you are working with API7 Enterprise, you should see in the API7 Dashboard that the upstream scheme of the service has been set to `https`.

If you are working with APISIX, you can examine the upstream scheme using the Admin API. Forward the Admin API's service port to your local machine:

```
kubectl port-forward service/apisix-admin 9180:9180 &
```

Assume that APISIX is started in standalone mode. Send a request to `/apisix/admin/configs` to view all configurations synchronized to the gateway:

```
curl "http://127.0.0.1:9180/apisix/admin/configs" -H "X-API-KEY: ${ADMIN_API_KEY}" | jq
```

You should see that the upstream scheme of the service has been set to `https`:

```
{
  "services_conf_version": 1767088219134,
  "consumers_conf_version": 0,
  "X-Last-Modified": 1767088880,
  "X-Digest": "6cfa92e8e40d2554c621a72fb62311edc16c741d",
  "services": [
    {
      "name": "aic_httpbin-route_0",
      "upstream_id": "ee55f349",
      ...
    }
  ],
  "secrets_conf_version": 0,
  "plugins_conf_version": 0,
  "routes": [
    {
      ...
    }
  ],
  "upstreams_conf_version": 1767088880723,
  "global_rules_conf_version": 0,
  "protos_conf_version": 0,
  "routes_conf_version": 1767088219134,
  "stream_routes_conf_version": 0,
  "upstreams": [
    {
      "scheme": "https",
      "labels": {
        "managed-by": "apisix-ingress-controller"
      },
      "name": "aic_httpbin-route_0",
      "id": "ee55f349"
      ...
    }
  ],
  "plugin_configs_conf_version": 0,
  "consumer_groups_conf_version": 0,
  "ssls_conf_version": 0,
  "plugin_metadata_conf_version": 0
}
```
