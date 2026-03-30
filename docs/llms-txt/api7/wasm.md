# Source: https://docs.api7.ai/ingress-controller/custom-plugins/wasm.md

# Deploy Wasm Plugins

APISIX supports [WebAssembly (Wasm)](https://webassembly.org) plugins developed following the [Proxy-Wasm specification](https://github.com/proxy-wasm/spec), a specification that extends Wasm capabilities to proxies.

This guide explains how to load WebAssembly (Wasm) plugins into gateways on Kubernetes and use APISIX Ingress Controller to enable the plugin on a route.

note

API7 Enterprise currently does not support custom Wasm plugins.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. Complete [Set Up Ingress Controller and Gateway](https://docs.api7.ai/ingress-controller/set-up-ingress-controller-and-gateway.md).
2. Follow the [Write Plugin Logic in Go](https://docs.api7.ai/apisix/how-to-guide/custom-plugins/wasm-plugins.md#write-plugin-logic-in-go) and [Compile the Code into Wasm](https://docs.api7.ai/apisix/how-to-guide/custom-plugins/wasm-plugins.md#compile-the-code-into-wasm) sections to prepare the `log.go.wasm` example plugin.

## Load Wasm Plugin[â](#load-wasm-plugin "Direct link to Load Wasm Plugin")

Create a ConfigMap from the `log.go.wasm` file:

```
kubectl create configmap wasm-log --from-file=log.go.wasm
```

To mount the ConfigMap, first export all values (including defaults):

```
helm get values -n aic apisix --all > values.yaml
```

In the values file, update the following section values as such:

values.yaml

```
extraVolumes:
  - name: wasm-log
    configMap:
      name: wasm-log
extraVolumeMounts:
  - name: wasm-log
    mountPath: /usr/local/bin/log.go.wasm
    subPath: log.go.wasm
...
apisix:
  wasm:
    enabled: true
    plugins:
      - name: wasm_log
        priority: 7999
        file: /usr/local/bin/log.go.wasm
```

Upgrade the release:

```
helm upgrade -n aic apisix apisix/apisix -f values.yaml
```

## Test Wasm Plugin[â](#test-wasm-plugin "Direct link to Test Wasm Plugin")

Create a route with the `wasm_log` plugin:

* Gateway API
* APISIX CRD

wasm-route.yaml

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
  name: wasm-log-plugin-config
spec:
  plugins:
    - name: wasm_log
      config:
        conf: hello apisix
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: wasm-log-plugin
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
        name: wasm-log-plugin-config
    backendRefs:
    - name: httpbin-external-domain
      port: 80
```

wasm-route.yaml

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
  name: wasm-log-plugin
spec:
  ingressClassName: apisix
  http:
    - name: wasm-log-plugin
      match:
        paths:
          - /anything
      plugins:
      - name: wasm_log
        enable: true
        config:
          conf: hello apisix
      upstreams:
      - name: httpbin-external-domain
```

Apply the configuration to your cluster:

```
kubectl apply -f wasm-route.yaml
```

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

In the gateway log, you should see the following log entry created by the `wasm_log` plugin:

```
2025/09/04 09:58:54 [warn] 53#53: *3331 run plugin ctx 1 with conf hello apisix in http ctx 2, client: 127.0.0.1, server: _, request: "GET /anything HTTP/1.1", host: "127.0.0.1:9080"
```
