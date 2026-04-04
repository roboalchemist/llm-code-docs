# Source: https://docs.api7.ai/ingress-controller/reference/examples.md

# Source: https://docs.api7.ai/enterprise/3.8.x/reference/api7-ingress-controller/examples.md

# Configuration Examples

API7 Ingress Controller supports both [Ingress resources and Gateway API](https://docs.api7.ai/enterprise/3.8.x/reference/api7-ingress-controller/ingress-and-gateway-api-support.md) for traffic management in Kubernetes. While both are supported, the Gateway API provides greater flexibility and extensibility. New users are encouraged to adopt Gateway API for future deployments.

In addition to these standard Kubernetes APIs, the API7 Ingress Controller also supports a set of [CRDs (Custom Resource Definitions)](https://docs.api7.ai/enterprise/3.8.x/reference/api7-ingress-controller/api-reference.md) designed specifically for APISIX-native functionality.

This document provides examples of common configurations covering how and when to use these resources. Be sure to replace any placeholder values (such as namespaces, route URI, and credentials) with those that match your own environment.

note

Currently, there are no functional differences between APISIX Ingress Controller and API7 Ingress Controller, although they may be released on different schedules.

## Configure CP Endpoint and Admin Key[â](#configure-cp-endpoint-and-admin-key "Direct link to Configure CP Endpoint and Admin Key")

To update the Control Plane endpoint and admin key for connectivity between API7 Ingress Controller and Control Plane at runtime:

```
apiVersion: apisix.apache.org/v1alpha1
kind: GatewayProxy
metadata:
  namespace: api7
  name: apisix-proxy-config
spec:
  provider:
    type: ControlPlane
    controlPlane:
      endpoints:
      - https://xxx.xxx.xxx.xxx:7443  # update with your CP endpoint
      auth:
        type: AdminKey
        adminKey:
          value: xxxxxxxxxxx          # update with your admin key
```

important

All resources within the same gateway group must use the same IngressClass (for Ingress / APISIX CRDs) or Gateway (for Gateway API), each of which points to a single GatewayProxy.

Using multiple GatewayProxy, IngressClass, or Gateway resources for a single gateway group can lead to conflicts and unintended resource overwrites.

## Define Controller and Gateway[â](#define-controller-and-gateway "Direct link to Define Controller and Gateway")

To specify the controller responsible for handling resources before applying further configurations:

* Gateway API
* Ingress
* APISIX CRD

```
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: apisix
spec:
  controllerName: "apisix.apache.org/apisix-ingress-controller"
---
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  namespace: api7
  name: apisix
spec:
  gatewayClassname: apisix
  listeners:
  - name: http
    protocol: HTTP
    port: 80
  infrastructure:
    parametersRef:
      group: apisix.apache.org
      kind: GatewayProxy
      name: apisix-proxy-config
```

â¶ The controller name should be customized if you are running multiple distinct instances of the APISIX Ingress Controller in the same cluster (not a single instance with multiple replicas). Each ingress controller instance must use a unique controllerName in its [configuration file](https://docs.api7.ai/enterprise/3.8.x/reference/api7-ingress-controller/configuration-file.md), and the corresponding GatewayClass should reference that value.

â· API group of the referenced resource.

â¸ Kind of the referenced resource.

â¹ Name of the referenced resource. Should match the `metadata.name` of the GatewayProxy resource.

note

The `port` in the Gateway listener is required but ignored. This is due to limitations in the data plane: it cannot dynamically open new ports. Since the Ingress Controller does not manage the data plane deployment, it cannot automatically update the configuration or restart the data plane to apply port changes.

```
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: apisix
spec:
  controller: "apisix.apache.org/apisix-ingress-controller"
  parameters:
    apiGroup: apisix.apache.org
    kind: GatewayProxy
    name: apisix-proxy-config
    namespace: api7
    scope: Namespace
```

â¶ The controller name should be customized if you are running multiple distinct instances of the APISIX Ingress Controller in the same cluster (not a single instance with multiple replicas). Each ingress controller instance must use a unique controllerName in its [configuration file](https://docs.api7.ai/enterprise/3.8.x/reference/api7-ingress-controller/configuration-file.md), and the corresponding IngressClass should reference that value.

â· API group of the referenced resource.

â¸ Kind of the referenced resource.

â¹ Name of the referenced resource. Should match the `metadata.name` of the GatewayProxy resource.

âº Namespace where the referenced resource is defined.

â» Scope of the referenced resource.

```
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: apisix
spec:
  controller: "apisix.apache.org/apisix-ingress-controller"
  parameters:
    apiGroup: apisix.apache.org
    kind: GatewayProxy
    name: apisix-proxy-config
    namespace: api7
    scope: Namespace
```

â¶ The controller name should be customized if you are running multiple distinct instances of the APISIX Ingress Controller in the same cluster (not a single instance with multiple replicas). Each ingress controller instance must use a unique controllerName in its [configuration file](https://docs.api7.ai/enterprise/3.8.x/reference/api7-ingress-controller/configuration-file.md), and the corresponding IngressClass should reference that value.

â· API group of the referenced resource.

â¸ Kind of the referenced resource.

â¹ Name of the referenced resource. Should match the `metadata.name` of the GatewayProxy resource.

âº Namespace where the referenced resource is defined.

â» Scope of the referenced resource.

## Route to K8s Services[â](#route-to-k8s-services "Direct link to Route to K8s Services")

To create a route that proxies requests to a service on K8s:

* Gateway API
* Ingress
* APISIX CRD

```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: api7
  name: httpbin
spec:
  parentRefs:
  - name: apisix
  hostnames:
  - httpbin.example.com
  rules:
  - matches:
    - path:
        type: Exact
        value: /ip
    backendRefs:
    - name: httpbin
      port: 80
```

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  namespace: api7
  name: httpbin
spec:
  ingressClassName: apisix
  rules:
  - host: httpbin.example.com
    http:
      paths:
      - path: /ip
        pathType: Exact
        backend:
          service:
            name: httpbin
            port:
              number: 80
```

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: api7
  name: httpbin
spec:
  ingressClassName: apisix
  http:
  - name: httpbin
    match:
      paths:
      - /ip
    backends:
    - serviceName: httpbin
      servicePort: 80
```

## Route to External Services[â](#route-to-external-services "Direct link to Route to External Services")

To create a route that proxies requests to a service publicly hosted:

* Gateway API
* Ingress
* APISIX CRD

```
apiVersion: v1
kind: Service
metadata:
  namespace: api7
  name: httpbin-external-domain
spec:
  type: ExternalName
  externalName: httpbin.org
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: api7
  name: get-ip
spec:
  parentRefs:
  - name: apisix
  hostnames:
  - httpbin.external
  rules:
  - matches:
    - path:
        type: Exact
        value: /ip
    backendRefs:
    - name: httpbin-external-domain
      port: 80
```

```
apiVersion: v1
kind: Service
metadata:
  namespace: api7
  name: httpbin-external-domain
spec:
  type: ExternalName
  externalName: httpbin.org
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  namespace: api7
  name: get-ip
spec:
  rules:
  - host: httpbin.external
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: httpbin-external-domain
            port:
              number: 80
```

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: api7
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
  namespace: api7
  name: get-ip
spec:
  ingressClassName: apisix
  http:
    - name: get-ip
      match:
        hosts:
        - httpbin.external
        paths:
          - /ip
      upstreams:
      - name: httpbin-external-domain
```

## Configure Weighted Services[â](#configure-weighted-services "Direct link to Configure Weighted Services")

To create a route that proxies traffic to upstream services by weight:

* Gateway API
* APISIX CRD

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
        type: Exact
        value: /ip
    backendRefs:
    - name: httpbin-1
      port: 80
      weight: 3
    - name: httpbin-2
      port: 80
      weight: 7
```

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: api7
  name: httpbin
spec:
  ingressClassName: apisix
  http:
  - name: httpbin
    match:
      hosts:
      - httpbin
      paths:
      - /ip
    backends:
    - serviceName: httpbin-1
      servicePort: 80
      weight: 3
    - serviceName: httpbin-2
      servicePort: 80
      weight: 7
```

This configuration is not supported by the Ingress resource.

## Configure Upstream[â](#configure-upstream "Direct link to Configure Upstream")

To configure upstream related configurations, including load balancing algorithm, how the host header is passed to upstream, service timeout, and more:

* Gateway API
* APISIX CRD

```
apiVersion: apisix.apache.org/v1alpha1
kind: BackendTrafficPolicy
metadata:
  namespace: api7
  name: httpbin
spec:
  targetRefs:
  - name: httpbin
    kind: Service
    group: ""
  timeout:
    send: 10s
    read: 10s
    connect: 10s
  scheme: http
  retries: 10
  loadbalancer:
    type: roundrobin
  passHost: rewrite
  upstreamHost: httpbin.example.com
```

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: api7
  name: httpbin
spec:
  ingressClassName: apisix
  timeout:
    send: 10s
    read: 10s
    connect: 10s
  scheme: http
  retries: 10
  loadbalancer:
    type: roundrobin
  passHost: rewrite
  upstreamHost: httpbin.example.com
```

## Detect Upstream Protocol with appProtocol[â](#detect-upstream-protocol-with-appprotocol "Direct link to Detect Upstream Protocol with appProtocol")

The `appProtocol` field on a Service port tells the gateway how to communicate with the backend.<br /><!-- -->The upstream scheme will be automatically configured based on this value. If not set, the default scheme is `http`.

API7 Ingress Controller supports the following appProtocol values for Service ports:

| Value               | Description                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------- |
| `http`              | The option sets the upstream scheme to `http`.                                                |
| `https`             | The option sets the upstream scheme to `https`.                                               |
| `kubernetes.io/ws`  | The option sets the upstream scheme to `http` and `enable_websocket` to `true` on the route.  |
| `kubernetes.io/wss` | The option sets the upstream scheme to `https` and `enable_websocket` to `true` on the route. |

Here is an example of a Service configured with appProtocol values for HTTP and HTTPS ports:

```
apiVersion: v1
kind: Service
metadata:
  namespace: api7
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

You can then create a route that points to the Service port, allowing APISIX to detect the upstream protocol automatically. With the below configuration, APISIX automatically sets the upstream scheme to `https`:

* Gateway API
* Ingress
* APISIX CRD

```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: api7
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

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  namespace: api7
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

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: api7
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

## Configure Consumer and Credentials[â](#configure-consumer-and-credentials "Direct link to Configure Consumer and Credentials")

* Gateway API
* APISIX CRD

To create a consumer and configure the authentication credentials directly on the consumer:

```
apiVersion: apisix.apache.org/v1alpha1
kind: Consumer
metadata:
  namespace: api7
  name: alice
spec:
  gatewayRef:
    name: apisix
  credentials:
    - type: key-auth
      name: primary-key
      config:
        key: alice-primary-key
```

You can also use the secret CRD, where the credential should be base64 encoded:

```
apiVersion: v1
kind: Secret
metadata:
  namespace: api7
  name: key-auth-primary
data:
  key: YWxpY2UtcHJpbWFyeS1rZXk=
---
apiVersion: apisix.apache.org/v1alpha1
kind: Consumer
metadata:
  namespace: api7
  name: alice
spec:
  gatewayRef:
    name: apisix
  credentials:
    - type: key-auth
      name: key-auth-primary
      secretRef:
        name: key-auth-primary
```

To create a consumer and configure the authentication credentials directly on the consumer:

```
apiVersion: apisix.apache.org/v2
kind: ApisixConsumer
metadata:
  namespace: api7
  name: alice
spec:
  ingressClassName: apisix
  authParameter:
    keyAuth:
      value:
        key: alice-primary-key
```

You can also use the secret CRD, where the credential should be base64 encoded:

```
apiVersion: v1
kind: Secret
metadata:
  namespace: api7
  name: key-auth-primary
data:
  key: YWxpY2UtcHJpbWFyeS1rZXk=
---
apiVersion: apisix.apache.org/v2
kind: ApisixConsumer
metadata:
  namespace: api7
  name: alice
spec:
  ingressClassName: apisix
  authParameter:
    keyAuth:
      secretRef:
        name: key-auth-primary
```

## Configure Plugin on Consumer[â](#configure-plugin-on-consumer "Direct link to Configure Plugin on Consumer")

To configure plugin(s) on a consumer, such as a rate limiting plugin:

* Gateway API
* APISIX CRD

```
apiVersion: apisix.apache.org/v1alpha1
kind: Consumer
metadata:
  namespace: api7
  name: alice
spec:
  gatewayRef:
    name: apisix
  credentials:
    - type: key-auth
      name: alice-key
      config:
        key: alice-key
  plugins:
    - name: limit-count
      config:
        count: 3
        time_window: 60
        key: remote_addr
        key_type: var
        policy: local
        rejected_code: 429
        rejected_msg: Too many requests
        show_limit_quota_header: true
        allow_degradation: false
```

ApisixConsumer currently does not support configuring plugins on consumers.

## Configure Route Priority and Matching Conditions[â](#configure-route-priority-and-matching-conditions "Direct link to Configure Route Priority and Matching Conditions")

To configure route priority and request matching conditions on a targeted route:

* Gateway API
* APISIX CRD

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
    - new_name
  - - arg_test
    - ==
    - test_name
```

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: api7
  name: httpbin
spec:
  ingressClassName: apisix
  http:
  - name: httpbin
    match:
      paths:
      - /*
      exprs:
      - subject:
          scope: Header
          name: X-Test-Name
        op: Equal
        value: new_name
      - subject:
          scope: Query
          name: test
        op: Equal
        value: test_name
    priority: 10
    backends:
    - serviceName: httpbin
      servicePort: 80
```

## Configure Plugin on a Service/Route[â](#configure-plugin-on-a-serviceroute "Direct link to Configure Plugin on a Service/Route")

* Gateway API
* APISIX CRD

Gateway API currently does not support enabling a plugin on a route. To enable a plugin on a service:

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: api7
  name: auth-plugin-config
spec:
  plugins:
    - name: key-auth
      config:
        _meta:
          disable: false
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: api7
  name: get-ip
spec:
  parentRefs:
  - name: apisix
  rules:
  - matches: 
    - path:
        type: Exact
        value: /ip
    filters:
    - type: ExtensionRef
      extensionRef:
        group: apisix.apache.org
        kind: PluginConfig
        name: auth-plugin-config
    backendRefs:
    - name: httpbin
      port: 80
```

APISIX CRD currently does not support enabling plugins on a service. To enable a plugin on a route:

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: api7
  name: get-ip
spec:
  ingressClassName: apisix
  http:
    - name: get-ip
      match:
        paths:
          - /ip
      plugins:
      - name: limit-count
        enable: true
        config:
          count: 2
          time_window: 10
          rejected_code: 429
      backends:
      - serviceName: httpbin
        servicePort: 80
```

## Configure Global Plugin[â](#configure-global-plugin "Direct link to Configure Global Plugin")

To configure a global plugin:

* Gateway API
* APISIX CRD

```
apiVersion: apisix.apache.org/v1alpha1
kind: GatewayProxy
metadata:
  namespace: api7
  name: apisix-proxy-config
spec:
  provider:
    type: ControlPlane
    controlPlane:
      endpoints:
        - https://xxx.xxx.xxx.xxx:7443  # update with your CP endpoint
      auth:
        type: AdminKey
        adminKey:
          value: xxxxxxxxxxx            # update with your admin key
  plugins:
  - name: clickhouse-logger
    config:
      endpoint_addr: http://clickhouse-clickhouse-installation.apisix.svc.cluster.local:8123
      user: quickstart-user
      password: quickstart-pass
      logtable: test
      database: quickstart_db
```

```
apiVersion: apisix.apache.org/v2
kind: ApisixGlobalRule
metadata:
  namespace: api7
  name: apisix-global-rule-logging
spec:
  ingressClassName: apisix
  plugins:
  - name: clickhouse-logger
    enable: true
    config:
      endpoint_addr: http://clickhouse-clickhouse-installation.apisix.svc.cluster.local:8123
      user: quickstart-user
      password: quickstart-pass
      logtable: test
      database: quickstart_db
```

## Configure Plugin Metadata[â](#configure-plugin-metadata "Direct link to Configure Plugin Metadata")

To configure plugin metadata:

* Gateway API
* APISIX CRD

```
apiVersion: apisix.apache.org/v1alpha1
kind: GatewayProxy
metadata:
  namespace: api7
  name: apisix-proxy-config
spec:
  provider:
    type: ControlPlane
    controlPlane:
      endpoints:
        - https://xxx.xxx.xxx.xxx:7443  # update with your CP endpoint
      auth:
        type: AdminKey
        adminKey:
          value: xxxxxxxxxxx            # update with your admin key
  pluginMetadata:
    opentelemetry: {
      "trace_id_source": "x-request-id",
      "resource": {
        "service.name": "APISIX"
      },
      "collector": {
        "address": "simplest-collector:4318",
        "request_timeout": 3,
        "request_headers": {
          "Authorization": "token"
        }
      },
      "batch_span_processor": {
        "drop_on_queue_full": false,
        "max_queue_size": 1024,
        "batch_timeout": 2,
        "inactive_timeout": 1,
        "max_export_batch_size": 16
      },
      "set_ngx_var": true
    }
```

## Configure Plugin Config[â](#configure-plugin-config "Direct link to Configure Plugin Config")

To create a plugin config and reference it in a route:

* Gateway API
* APISIX CRD

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: api7
  name: example-plugin-config
spec:
  plugins:
  - name: response-rewrite
    enable: true
    config:
      headers:
        X-Plugin-Config: "example-response-rewrite"
        X-Plugin-Test: "enabled"
---
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
        type: Exact
        value: /ip
    filters:
    - type: ExtensionRef
      extensionRef:
        group: apisix.apache.org
        kind: PluginConfig
        name: example-plugin-config
    backendRefs:
    - name: httpbin
      port: 80
```

```
apiVersion: apisix.apache.org/v2
kind: ApisixPluginConfig
metadata:
  namespace: api7
  name: example-plugin-config
spec:
  ingressClassName: apisix
  plugins:
  - name: response-rewrite
    enable: true
    config:
      headers:
        X-Plugin-Config: "example-response-rewrite"
        X-Plugin-Test: "enabled"
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: api7
  name: httpbin
spec:
  ingressClassName: apisix
  http:
  - name: get-ip
    match:
      paths:
      - /ip
    backends:
    - serviceName: httpbin
      servicePort: 80
    plugin_config_name: example-plugin-config
```

## Configure Downstream (m)TLS[â](#configure-downstream-mtls "Direct link to Configure Downstream (m)TLS")

To configure downstream TLS:

* Gateway API
* APISIX CRD

```
apiVersion: v1
kind: Secret
metadata:
  namespace: api7
  name: test-tls-secret
type: kubernetes.io/tls
data:
  tls.crt: <base64-encoded cert>
  tls.key: <base64-encoded key>
---
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  namespace: api7
  name: apisix
spec:
  gatewayClassName: apisix
  listeners:
    - name: https
      protocol: HTTPS
      port: 443
      hostname: apisix.test
      tls:
        certificateRefs:
        - kind: Secret
          group: ""
          name: test-tls-secret
  infrastructure:
    parametersRef:
      group: apisix.apache.org
      kind: GatewayProxy
      name: apisix-proxy-config
```

note

The `port` in the Gateway listener is required but ignored. This is due to limitations in the data plane: it cannot dynamically open new ports. Since the Ingress Controller does not manage the data plane deployment, it cannot automatically update the configuration or restart the data plane to apply port changes.

```
apiVersion: v1
kind: Secret
metadata:
  namespace: api7
  name: test-tls-secret
type: kubernetes.io/tls
data:
  tls.crt: <base64-encoded cert>
  tls.key: <base64-encoded key>
---
apiVersion: apisix.apache.org/v2
kind: ApisixTls
metadata:
  namespace: api7
  name: test-tls
spec:
  ingressClassName: apisix-tls
  hosts:
  - apisix.test
  secret:
    name: test-tls-secret
    namespace: api7
```

To configure downstream mTLS:

* Gateway API
* APISIX CRD

Not supported.

```
apiVersion: v1
kind: Secret
metadata:
  namespace: api7
  name: test-mtls-secret
type: kubernetes.io/tls
data:
  tls.crt: <base64-encoded cert>
  tls.key: <base64-encoded key>
---
apiVersion: v1
kind: Secret
metadata:
  namespace: api7
  name: test-ca-secret
data:
  cert: <base64-encoded caCert>
---
apiVersion: apisix.apache.org/v2
kind: ApisixTls
metadata:
  namespace: api7
  name: test-mtls
spec:
  ingressClassName: apisix-tls
  hosts:
  - apisix.test
  secret:
    name: test-mtls-secret
    namespace: api7
  client:
    caSecret:
      name: test-ca-secret
      namespace: api7
    depth: 1
```

## Configure Gateway Access Information[â](#configure-gateway-access-information "Direct link to Configure Gateway Access Information")

These configurations allow Ingress Controller users to access the gateway.

* Gateway API
* Ingress
* APISIX CRD

To configure the `statusAddress`:

```
apiVersion: apisix.apache.org/v1alpha1
kind: GatewayProxy
metadata:
  namespace: api7
  name: apisix-proxy-config
spec:
  provider:
    type: ControlPlane
    controlPlane:
      endpoints:
        - https://xxx.xxx.xxx.xxx:7443  # update with your CP endpoint
      auth:
        type: AdminKey
        adminKey:
          value: xxxxxxxxxxx            # update with your admin key
  statusAddress:
    - 10.24.87.13
```

If you are using Ingress resources, you can configure either `statusAddress` or `publishService`.

To configure the `statusAddress`:

```
apiVersion: apisix.apache.org/v1alpha1
kind: GatewayProxy
metadata:
  namespace: api7
  name: apisix-proxy-config
spec:
  provider:
    type: ControlPlane
    controlPlane:
      endpoints:
        - https://xxx.xxx.xxx.xxx:7443  # update with your CP endpoint
      auth:
        type: AdminKey
        adminKey:
          value: xxxxxxxxxxx            # update with your admin key
  statusAddress:
    - 10.24.87.13
```

To configure the `publishService`:

```
apiVersion: apisix.apache.org/v1alpha1
kind: GatewayProxy
metadata:
  namespace: api7
  name: apisix-proxy-config
spec:
  provider:
    type: ControlPlane
    controlPlane:
      endpoints:
        - https://xxx.xxx.xxx.xxx:7443  # update with your CP endpoint
      auth:
        type: AdminKey
        adminKey:
          value: xxxxxxxxxxx            # update with your admin key
  publishService: apisix-ee-3-gateway-gateway
```

When using `publishService`, make sure your gateway Service is of `LoadBalancer` type the address can be populated. The controller will use the endpoint of this Service to update the status information of the Ingress resource. The format can be either `namespace/svc-name` or simply `svc-name` if the default namespace is correctly set.

Not supported.
