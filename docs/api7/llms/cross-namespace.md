# Source: https://docs.api7.ai/ingress-controller/production/cross-namespace.md

# Configure Cross-Namespace References

In production environments, cross-namespace references enable centralized infrastructure management while allowing application teams to operate independently. For instance, platform teams can manage shared backend services in dedicated namespaces, while application teams deploy their own routes in separate namespaces. Enabling cross-namespace references allows controlled resource sharing across namespaces without duplicating configuration, improving security boundaries, governance, and operational scalability.

Cross-namespace references are supported only through Gateway API resources. The Ingress resource and APISIX CRDs do not support cross-namespace references. Cross-namespace reference capability relies on two mechanisms:

1. **ReferenceGrant**: Required when a route in one namespace references a backend resource in another namespace. Supported route types include HTTPRoute, GRPCRoute, TCPRoute, UDPRoute, and TLSRoute.
2. **Gateway listener's `allowedRoutes`**: Required when a route from a different namespace needs to attach to a Gateway listener.

This guide provides an example of how to configure cross-namespace references using Gateway API resources, as illustrated in the diagram below. The example assumes that the Ingress Controller has been deployed in the `aic` namespace. If you use a different namespace, adjust the configuration accordingly to match your deployment.

<!-- -->

## Create Namespaces[â](#create-namespaces "Direct link to Create Namespaces")

Create the tenant and backend namespaces:

```
kubectl create namespace backend-ns
kubectl create namespace tenant-a
```

Label the `tenant-a` namespace for use with Gateway selector-based route selection:

```
kubectl label namespace tenant-a tenant=tenant-a
```

## Create a Backend Service[â](#create-a-backend-service "Direct link to Create a Backend Service")

Create a deployment and service in the backend namespace:

httpbin-deployment.yaml

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: httpbin
  namespace: backend-ns
spec:
  replicas: 1
  selector:
    matchLabels:
      app: httpbin
  template:
    metadata:
      labels:
        app: httpbin
    spec:
      containers:
      - name: httpbin
        image: kennethreitz/httpbin
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: httpbin
  namespace: backend-ns
spec:
  ports:
  - port: 80
    targetPort: 80
    protocol: TCP
  selector:
    app: httpbin
```

Apply the configuration to your cluster:

```
kubectl apply -f httpbin-deployment.yaml
```

## Create a ReferenceGrant[â](#create-a-referencegrant "Direct link to Create a ReferenceGrant")

In ReferenceGrant, the `from` field specifies which resources are allowed to reference objects in the target namespace, while the `to` field defines which resources in that namespace can be referenced.

Create a ReferenceGrant in the backend namespace `backend-ns` to permit references from the tenant namespace `tenant-a`:

referencegrant.yaml

```
apiVersion: gateway.networking.k8s.io/v1beta1
kind: ReferenceGrant
metadata:
  name: allow-from-tenant-a
  namespace: backend-ns
spec:
  from:
  - group: gateway.networking.k8s.io
    kind: HTTPRoute
    namespace: tenant-a
  to:
  - group: ""
    kind: Service
    name: httpbin
```

â¶ `from.group`: API group of the referring resource.

â· `from.kind`: The kind of the referring resource. Supported resource kinds are HTTPRoute, GRPCRoute, TCPRoute, UDPRoute, and TLSRoute.

â¸ `from.namespace`: Namespace where the referring resource is located.

â¹ `to.group`: API group of the target resource (use `""` for core resources like Service).

âº `to.kind`: Kind of the target resource (e.g. Service, Secret).

â» `to.name`: Name of the resource to allow.

info

`to.name` is an optional field. If omitted, the ReferenceGrant allows references to all resources of the specified `to.group` and `to.kind` within the target namespace.

Apply the configuration to your cluster:

```
kubectl apply -f referencegrant.yaml
```

## Create a Route[â](#create-a-route "Direct link to Create a Route")

Create an HTTPRoute in the tenant namespace `tenant-a` that references the backend service in `backend-ns`. The HTTPRoute will be attached to the `apisix` Gateway resource in the `aic` namespace.

httpbin-route.yaml

```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: httpbin-route
  namespace: tenant-a
spec:
  parentRefs:
  - name: apisix
    namespace: aic
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /ip
    backendRefs:
    - kind: Service
      name: httpbin
      namespace: backend-ns
      port: 80
      weight: 1
```

Apply the configuration to your cluster:

```
kubectl apply -f httpbin-route.yaml
```

## Configure Gateway to Allow Cross-Namespace Routes[â](#configure-gateway-to-allow-cross-namespace-routes "Direct link to Configure Gateway to Allow Cross-Namespace Routes")

By default, Gateway listeners only allow routes from the same namespace as the Gateway (`from: Same`). To allow routes from other namespaces, update the Gateway listener with `allowedRoutes`:

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
    allowedRoutes:
      namespaces:
        from: Selector
        selector:
          matchLabels:
            tenant: tenant-a
  infrastructure:
    parametersRef:
      group: apisix.apache.org
      kind: GatewayProxy
      name: apisix-config
```

â¶ `allowedRoutes`: Configuration that defines which routes are permitted to attach to this listener.

â· `namespaces`: Namespace selection mechanism for determining eligible routes.

â¸ `from: Selector`: Selector-based namespace filtering that allows only matching namespaces.

â¹ `selector`: Label-based selection criteria used to match namespaces.

âº `matchLabels`: Key-value label requirements that a namespace must satisfy.

â» `tenant`: Namespace label indicating membership.

Apply the configuration to your cluster:

```
kubectl apply -f gateway.yaml
```

Alternatively, you can configure the Gateway listener to allow routes from all namespaces:

```
allowedRoutes:
  namespaces:
    from: All
```

Security Warning

Using `from: All` in a multi-tenant or untrusted environment allows any namespace to attach HTTPRoutes to this Gateway listener. This can let untrusted namespaces hijack traffic or expose backends they should not have access to.

## Verify[â](#verify "Direct link to Verify")

Expose the gatewayâs service port to your local machine:

```
# replace with your gatewayâs service name
kubectl port-forward svc/<gateway-service-name> 9080:80 &
```

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/ip"
```

You should receive an `HTTP/1.1 200 OK` response similar to the following:

```
{
  "origin": "127.0.0.1"
}
```

This verifies that the request was successfully routed across namespaces.
