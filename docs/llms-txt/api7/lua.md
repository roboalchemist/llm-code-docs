# Source: https://docs.api7.ai/ingress-controller/custom-plugins/lua.md

# Deploy Lua Custom Plugins

When built-in plugins are not sufficient, you can extend gateway capabilities by developing custom plugins.

This guide explains how to load Lua custom plugins into gateways on Kubernetes and use APISIX or the API7 Ingress Controller to enable the plugin on a route.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. Complete [Set Up Ingress Controller and Gateway](https://docs.api7.ai/ingress-controller/set-up-ingress-controller-and-gateway.md).
2. Review the [Develop File Proxy Plugin](https://docs.api7.ai/apisix/how-to-guide/custom-plugins/create-plugin-in-lua.md#develop-file-proxy-plugin) section and save `file-proxy.lua` as an example custom plugin file.

## Load Custom Plugin[â](#load-custom-plugin "Direct link to Load Custom Plugin")

* APISIX
* API7 Enterprise

Generate a ConfigMap from your custom plugin file:

```
# Replace with your file path
FILE_PATH="/path/to/file-proxy.lua"

kubectl create configmap custom-file-proxy --from-file="$FILE_PATH"
```

Upgrade the installation to mount a custom ConfigMap containing the `file-proxy.lua` plugin and enable it along with the default plugins:

```
helm upgrade -n aic apisix apisix/apisix \
  --set ... \ # add other parameters
  --set "apisix.customPlugins.enabled=true" \
  --set "apisix.customPlugins.plugins[0].name=file-proxy" \
  --set "apisix.customPlugins.plugins[0].attrs={}" \
  --set "apisix.customPlugins.plugins[0].configMap.name=custom-file-proxy" \
  --set "apisix.customPlugins.plugins[0].configMap.mounts[0].key=file-proxy.lua" \
  --set "apisix.customPlugins.plugins[0].configMap.mounts[0].path=/usr/local/apisix/apisix/plugins/file-proxy.lua" \
  --set "apisix.plugins={file-proxy}"
```

Caution about `apisix.plugins={file-proxy}`

This flag adds only the `file-proxy` plugin to the plugin list, overriding all default plugins. To add the custom plugin without removing existing plugins, include the existing plugin names in the `apisix.plugins` list.

Alternatively, you could also update these values in the values file. Export all values (including defaults):

```
helm get values -n aic apisix --all > values.yaml
```

Update the following sections:

values.yaml

```
apisix:
  ...
  customPlugins:
    enabled: true
    plugins:
      - name: "file-proxy"
        attrs: {}
        configMap:
          name: "file-proxy-config"
          mounts:
            - key: "file-proxy.lua"
              path: "/usr/local/apisix/apisix/plugins/file-proxy.lua"
  plugins:
    - ...  # make sure to include other plugins
    - file-proxy
```

Upgrade the release:

```
helm upgrade -n aic apisix apisix/apisix -f values.yaml
```

If you are using API7 Enterprise, you can [load the custom plugin on the API7 Dashboard](https://docs.api7.ai/enterprise/best-practices/custom-plugin.md).

## Test Custom Plugin[â](#test-custom-plugin "Direct link to Test Custom Plugin")

Store a static `openapi.yaml` file on the gateway instance:

```
kubectl exec -it <your-gateway-pod-name> -- /bin/sh -c "echo '
openapi: 3.0.1
info:
  title: OpenAPI Spec
  description: OpenAPI Spec file description.
' > /usr/local/apisix/openapi.yaml"
```

Create a route with the custom plugin that uses the `openapi.yaml` file:

* Gateway API
* APISIX CRD

file-proxy-route.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: file-proxy-plugin-config
spec:
  plugins:
    - name: file-proxy
      config:
        path: /usr/local/apisix/openapi.yaml
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: openapi-file-proxy
spec:
  parentRefs:
  - name: apisix
  rules:
  - matches: 
    - path:
        type: Exact
        value: /openapi.yaml
    filters:
    - type: ExtensionRef
      extensionRef:
        group: apisix.apache.org
        kind: PluginConfig
        name: file-proxy-plugin-config
```

file-proxy-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: openapi-file-proxy
spec:
  ingressClassName: apisix
  http:
    - name: openapi-file-proxy
      match:
        paths:
          - /openapi.yaml
      plugins:
      - name: file-proxy
        enable: true
        config:
          path: /usr/local/apisix/openapi.yaml
```

Apply the configuration to your cluster:

```
kubectl apply -f file-proxy-route.yaml
```

Send a request to the route:

```
curl "http://127.0.0.1:9080/openapi.yaml"
```

You should receive a response with the content of the file `openapi.yaml`:

```
openapi: 3.0.1
info:
  title: OpenAPI Spec
  description: OpenAPI Spec file description.
```

This verifies that the custom plugin is loaded and working correctly.
