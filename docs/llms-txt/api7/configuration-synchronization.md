# Source: https://docs.api7.ai/ingress-controller/troubleshoot/configuration-synchronization.md

# Troubleshoot Manifest Translation and Synchronization

Troubleshooting is required if the applied behavior does not match expectations, such as routes not being created correctly, plugins not being applied, or services failing to route traffic.

When you apply a Kubernetes resourceâwhether a Gateway API, Ingress, or APISIX CRDâthe Ingress Controller translates it into [ADC YAML](https://docs.api7.ai/apisix/reference/adc.md), which is then applied to the gateway:

<!-- -->

This document explains how to inspect the translated ADC configurations in memory and check the configurations actually applied to the gateway.

## Inspect Translated ADC Configurations[â](#inspect-translated-adc-configurations "Direct link to Inspect Translated ADC Configurations")

Ingress Controller provides a browser-accessible debug API that displays the translated ADC configurations, derived from the last applied Gateway API, Ingress, and APISIX CRD resources, in JSON format. It helps inspect the **in-memory state before the configurations are synchronized with the gateway**.

To use the debug API, configure these values in the ingress controller's [configuration file](https://docs.api7.ai/ingress-controller/reference/configuration-file.md):

config.yaml

```
enable_server: true             # Enable the debug API server
server_addr: "127.0.0.1:9092"   # Server address
```

These values are not yet available in the Helm chart. To apply the changes, modify the ConfigMap and restart the controller Deployment.

Once the debug API is enabled, you can access it by forwarding the controller podâs port to your local machine:

```
kubectl port-forward pod/<ingress-controller-pod-name> 9092:9092 &
```

You can now access the debug API in browser at [`127.0.0.1:9092/debug`](http://127.0.0.1:9092/debug/) and inspect the translated resources by resource type, such as routes and services.

## Inspect Synchronized Gateway Configurations[â](#inspect-synchronized-gateway-configurations "Direct link to Inspect Synchronized Gateway Configurations")

If you are using API7 Enterprise, you can view synchronized resources directly on the API7 Dashboard. Resources created by the Ingress Controller are read-only and cannot be edited from the Dashboard.

If you are using APISIX, you can inspect the synchronized resources using the Admin API. First, forward the Admin API service port to your local machine:

```
kubectl port-forward service/apisix-admin 9180:9180 &
```

If you have deployed APISIX in [standalone mode](https://docs.api7.ai/apisix/reference/api-standalone-usage.md), you can send a request to `/apisix/admin/configs` to view all configurations synchronized to the gateway:

```
curl "http://127.0.0.1:9180/apisix/admin/configs" -H "X-API-KEY: ${ADMIN_API_KEY}"
```

If you have deployed APISIX with etcd, you can send a request to `/apisix/admin/<resource>` to view the synchronized configurations of specific resources. For instance, to view the route configuration:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -H "X-API-KEY: ${ADMIN_API_KEY}"
```

For reference, see [Admin API](https://docs.api7.ai/apisix/reference/admin-api/.md).
