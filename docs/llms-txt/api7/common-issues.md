# Source: https://docs.api7.ai/ingress-controller/troubleshoot/common-issues.md

# Common Issues and Solutions

When issues arise while working with the Ingress Controller, the gateway and controller logs are usually the best place to start, as they often reveal the underlying issue quickly.

This document covers common issues you may encounter and provides practical guidance to troubleshoot and resolve them efficiently.

## GatewayProxy Missing or Misconfigured[â](#gatewayproxy-missing-or-misconfigured "Direct link to GatewayProxy Missing or Misconfigured")

GatewayProxy defines the Control Plane endpoint and Admin API key used by the Ingress Controller to communicate with the Control Plane. If your resources are not being synchronized to the gateway, a common cause is that the GatewayProxy resource is either missing or incorrectly configured.

Verify that the GatewayProxy resource exists and is created in the correct namespace:

```
kubectl get gatewayproxy --all-namespaces
```

If GatewayProxy exists, review the GatewayProxy configuration:

```
kubectl describe gatewayproxy <gatewayproxy-name> -n <namespace>
```

## IngressClassName Missing or Unspecified[â](#ingressclassname-missing-or-unspecified "Direct link to IngressClassName Missing or Unspecified")

For the following resources, the Ingress Controller only processes them when the ingressClassName matches the controllerâs configured IngressClass:

* `Ingress`
* `ApisixRoute`
* `ApisixUpstream`
* `ApisixTLS`
* `ApisixPluginConfig`
* `ApisixGlobalRule`
* `ApisixConsumer`

If the ingressClassName is missing or specified incorrectly, the resource will not be synchronized to the gateway.

ingress annotation

For `Ingress` resources, the controller first checks `spec.ingressClassName`. If it is not set, it falls back to the `kubernetes.io/ingress.class` annotation, which is supported for backward compatibility.

Verify which IngressClass resources (cluster-scoped) exist:

```
kubectl get ingressclass
```

Review the IngressClass configuration to ensure it references the intended Ingress Controller:

```
kubectl describe ingressclass <ingressclass-name>
```

Verify that your resources have specified the correct `ingressClassName`, for instance:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
spec:
  ingressClassName: apisix
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: example-service
            port:
              number: 80
```

## etcd Failures[â](#etcd-failures "Direct link to etcd Failures")

When running APISIX on Kubernetes in a deployment mode that uses etcd as the configuration backend, you may encounter etcd pods that repeatedly restart (`CrashLoopBackOff`) or fail to reach a healthy state. Hosting etcd as a Kubernetes StatefulSet can introduce operational challenges: pods may crash when they restart, scale, or lose access to persistent storage, and cluster membership can become unstable.

Because of these risks, **it is generally recommended to run APISIX in standalone mode**, which does not require etcd. This mode simplifies the deployment and avoids the complexity of managing an etcd cluster inside Kubernetes.

For deployments that truly require etcd, it is generally more reliable to host the etcd cluster on separate virtual machines or dedicated infrastructure outside of Kubernetes.

## Route Priority Across Resources[â](#route-priority-across-resources "Direct link to Route Priority Across Resources")

A higher value indicates a higher route priority. When multiple resource types are used together (Ingress, HTTPRoute, and APISIXRoute), routing behavior may be affected by differences in how route priorities are assigned and evaluated.

The following explains how priority is handled for each resource type:

* **Ingress:** Does not support explicit route priorities. Routes generated from Ingress resources are assigned a default priority of `0`, which is generally the lowest.
* **HTTPRoute:** Uses a dynamically computed [38-bit priority](https://github.com/apache/apisix-ingress-controller/blob/c48e9b3fb8d269b04b440c6fc5ed6880c05456f3/internal/adc/translator/httproute.go#L455-L472). Because this value is derived from multiple attributes, the resulting priority is not fixed and cannot be reliably predicted.
* **APISIXRoute:** Allows explicit configuration of route priority. To guarantee that an APISIXRoute is matched before an HTTPRoute, its priority must be set higher than 274,877,906,943 (2^38 â 1).

## HTTPRoute Filter and PluginConfig[â](#httproute-filter-and-pluginconfig "Direct link to HTTPRoute Filter and PluginConfig")

When both HTTPRoute filters and PluginConfig CRDs are applied to the same route, you may experience unexpected plugin behavior. Understanding how these interact helps avoid configuration conflicts.

The Ingress Controller maps built-in Gateway API HTTPRoute filters to specific plugins:

* `RequestHeaderModifier` â [`proxy-rewrite`](https://docs.api7.ai/hub/proxy-rewrite.md)
* `RequestRedirect` â [`redirect`](https://docs.api7.ai/hub/redirect)
* `RequestMirror` â [`proxy-mirror`](https://docs.api7.ai/hub/proxy-mirror.md)
* `URLRewrite` â [`proxy-rewrite`](https://docs.api7.ai/hub/proxy-rewrite.md)
* `ResponseHeaderModifier` â [`response-rewrite`](https://docs.api7.ai/hub/response-rewrite.md)
* `CORS` â [`cors`](https://docs.api7.ai/hub/cors.md)
* `ExtensionRef` â user-defined plugin reference

When both filters and a PluginConfig CRD are applied:

* If filters are applied first, PluginConfig overrides any overlapping plugin settings.
* If PluginConfig is applied first, filters merge with PluginConfig settings, and overlapping fields from filters take precedence.

## Controller Error Due to Experimental Gateway API Resources[â](#controller-error-due-to-experimental-gateway-api-resources "Direct link to Controller Error Due to Experimental Gateway API Resources")

In 2.0.0 release candidates of APISIX Ingress Controller and in API7 Ingress Controller versions prior to 2.0.16, the controller would fail to start if it attempted to set up controllers for Gateway API types whose CRDs were not present in the cluster (for example, experimental resources such as TCPRoute, UDPRoute, and TLSRoute). This occurred because OpenShift does not install experimental Gateway API resources by default and the controller attempts to initialize watches for those kinds even when the CRDs were not installed, leading to errors like:

```
Error: no matches for kind "TCPRoute" in version "gateway.networking.k8s.io/v1alpha2"
```

In later versions, the controller automatically detects available Gateway API resources and only sets up controllers for resources that exist in the cluster. This means core Gateway API resources like Gateway and HTTPRoute will still work on OpenShift, while experimental resources like TCPRoute are safely skipped.

Alternatively, you can also configure the controller to disable Gateway API entirely:

config.yaml

```
disable_gateway_api: true    # default is false
```
