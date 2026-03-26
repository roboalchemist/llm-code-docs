# Source: https://docs.api7.ai/ingress-controller/troubleshoot/gateway-debug-mode.md

# Enable Gateway Debug Mode

The gateway provides a debug mode to help developers better understand and troubleshoot the runtime behavior of the gateway. The debug mode configuration can be found in [`debug.yaml`](https://github.com/apache/apisix/blob/master/conf/debug.yaml).

This guide will show you how to enable the gateway basic debug mode in a Kubernetes environment to inspect what plugins are enabled on the requested route. For information about the advanced debug mode, see [Advanced Debug Mode](https://docs.api7.ai/apisix/how-to-guide/troubleshooting/debug-mode.md#configure-advanced-debug-mode).

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. Complete [Set Up Ingress Controller and Gateway](https://docs.api7.ai/ingress-controller/set-up-ingress-controller-and-gateway.md).

## Enable Basic Debug Mode[â](#enable-basic-debug-mode "Direct link to Enable Basic Debug Mode")

Enabling the basic debug mode will allow you to inspect what plugins are enabled on the requested route in the `Apisix-Plugins` header.

By default, the debug mode is turned off. To enable the debug mode, you can set `basic.enable` to `true` in your `debug.yaml` file.

Create a ConfigMap:

apisix-debug-cm.yaml

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: apisix-debug
  namespace: aic
data:
  debug.yaml: |
    basic:
      enable: true
    #END
```

Apply the ConfigMap to your cluster:

```
kubectl apply -f apisix-debug-cm.yaml
```

To mount the ConfigMap, first export all values (including defaults):

```
helm get values -n aic apisix --all > values.yaml
```

In the values file, update the following section values as such:

values.yaml

```
extraVolumes:
  - name: debug-config
    configMap:
      name: apisix-debug
extraVolumeMounts:
  - name: debug-config
    mountPath: /usr/local/apisix/conf/debug.yaml
    subPath: debug.yaml
```

Upgrade the release:

```
helm upgrade -n aic apisix apisix/apisix -f values.yaml
```

info

The `debug.yaml` configurations should end with `#END`, or else the gateway will not load the configurations. This means you can also use the `#END` flag as a breakpoint for the gateway to only load configurations up to the specified point.

## Verify[â](#verify "Direct link to Verify")

To verify, create a route without any plugin:

* Gateway API
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
  name: getting-started-anything
spec:
  parentRefs:
  - name: apisix
  rules:
  - matches:
    - path:
        type: Exact
        value: /anything
    backendRefs:
    - name: httpbin-external-domain
      port: 80
```

httpbin-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  externalNodes:
  - type: Domain
    name: httpbin.org
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: getting-started-anything
spec:
  ingressClassName: apisix
  http:
    - name: getting-started-anything
      match:
        paths:
          - /anything
      upstreams:
      - name: httpbin-external-domain
```

Apply the configuration to your cluster:

```
kubectl apply -f httpbin-route.yaml
```

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response and observe the following headers:

```
Content-Type: application/json
Content-Length: 390
Connection: keep-alive
Apisix-Plugins: no plugin
...
```

* Gateway API
* APISIX CRD

Update the route with a plugin:

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
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: limit-count-plugin-config
spec:
  plugins:
    - name: limit-count
      config:
        count: 5
        time_window: 10
        rejected_code: 429
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: getting-started-anything
spec:
  parentRefs:
  - name: apisix
  rules:
  - matches:
    - path:
        type: Exact
        value: /anything
    filters:
    - type: ExtensionRef
      extensionRef:
        group: apisix.apache.org
        kind: PluginConfig
        name: limit-count-plugin-config
    backendRefs:
    - name: httpbin-external-domain
      port: 80
```

Additionally, update your GatewayProxy manifest to enable `prometheus` as a global plugin:

tip

To view the current GatewayProxy configuration before adding additional configuration, run:

```
kubectl get gatewayproxy apisix-config -o yaml
```

gateway-proxy.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: GatewayProxy
metadata:
  namespace: aic
  name: apisix-config
spec:
  provider:
    type: ControlPlane
    controlPlane:
      auth:
        adminKey:
          value: edd1c9f034335f136f87ad84b625c8f1
        type: AdminKey
      service:
        name: apisix-admin
        port: 9180
  plugins:
  - name: prometheus
    enabled: true
```

Apply the configuration to your cluster:

```
kubectl apply -f httpbin-route.yaml -f gateway-proxy.yaml
```

Update the route with a plugin:

httpbin-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  externalNodes:
  - type: Domain
    name: httpbin.org
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: getting-started-anything
spec:
  ingressClassName: apisix
  http:
    - name: getting-started-anything
      match:
        paths:
          - /anything
      upstreams:
      - name: httpbin-external-domain
      plugins:
      - name: limit-count
        enable: true
        config:
          count: 5
          time_window: 10
          rejected_code: 429
```

Additionally, create a Kubernetes manifest file for a global Prometheus plugin:

global-prometheus.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixGlobalRule
metadata:
  namespace: aic
  name: global-prometheus
spec:
  ingressClassName: apisix
  plugins:
    - name: prometheus
      enable: true
```

Apply the configuration to your cluster:

```
kubectl apply -f httpbin-route.yaml -f global-prometheus.yaml
```

Send another request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response with headers similar to the following:

```
Content-Type: application/json
Content-Length: 388
Connection: keep-alive
X-RateLimit-Limit: 5
X-RateLimit-Remaining: 4
X-RateLimit-Reset: 10
Apisix-Plugins: limit-count, prometheus
...
```

info

If the plugin information cannot be included in a response header (e.g. L4 stream plugins), the debug information will be logged in the error log at the `warn` severity level.
