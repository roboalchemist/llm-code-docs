# Source: https://docs.api7.ai/ingress-controller/reference/ingress-and-gateway-api-support.md

# Source: https://docs.api7.ai/enterprise/3.8.x/reference/api7-ingress-controller/ingress-and-gateway-api-support.md

# Ingress and Gateway API Support

This document outlines the Kubernetes Gateway API and Ingress API resources supported by the API7 Ingress Controller. Use this as a reference to understand which resources are currently implemented.

See the [configuration examples](https://docs.api7.ai/enterprise/3.8.x/reference/api7-ingress-controller/examples.md) to learn when and how to use these resources.

## Gateway API[â](#gateway-api "Direct link to Gateway API")

### Packages[â](#packages "Direct link to Packages")

* [gateway.networking.k8s.io/v1](https://gateway-api.sigs.k8s.io/reference/1.3/spec/#gatewaynetworkingk8siov1)
* [gateway.networking.k8s.io/v1beta1](https://gateway-api.sigs.k8s.io/reference/1.3/spec/#gatewaynetworkingk8siov1beta1)

### Resource Support Levels[â](#resource-support-levels "Direct link to Resource Support Levels")

The table below outlines the support levels for Kubernetes Gateway API resources in the current implementation. Each resource is categorized by its level of core, extended, and implementation-specific support, along with the corresponding API version.

| Resource         | Core                | Extended            | Implementation-Specific | API Version |
| ---------------- | ------------------- | ------------------- | ----------------------- | ----------- |
| GatewayClass     | Supported           | N/A                 | Not supported           | v1          |
| Gateway          | Partially supported | Partially supported | Not supported           | v1          |
| HTTPRoute        | Supported           | Partially supported | Not supported           | v1          |
| GRPCRoute        | Supported           | Supported           | Not supported           | v1          |
| ReferenceGrant   | Supported           | Not supported       | Not supported           | v1beta1     |
| TLSRoute         | Supported           | Supported           | Not supported           | v1alpha2    |
| TCPRoute         | Supported           | Supported           | Not supported           | v1alpha2    |
| UDPRoute         | Supported           | Supported           | Not supported           | v1alpha2    |
| BackendTLSPolicy | Not supported       | Not supported       | Not supported           | v1alpha3    |

For a complete list of configuration options, refer to the [Gateway API Reference](https://gateway-api.sigs.k8s.io/reference/1.3/spec/). Be aware that some fields are not supported, or partially supported.

### Unsupported / Partially Supported Fields[â](#unsupported--partially-supported-fields "Direct link to Unsupported / Partially Supported Fields")

The fields below are specified in the Gateway API specification but are either partially implemented or not yet supported in the APISIX Ingress Controller.

#### HTTPRoute[â](#httproute "Direct link to HTTPRoute")

| Fields                                 | Status        | Notes                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `spec.timeouts`                        | Not supported | The field is unsupported because ADC provides finer-grained timeout configuration (connect, read, write), whereas `spec.timeouts` only allows a general total timeout and upstream timeout, so it cannot be directly mapped. To configure route timeouts, you can use [BackendTrafficPolicy](https://docs.api7.ai/enterprise/3.8.x/reference/api7-ingress-controller/api-reference.md#backendtrafficpolicyspec). |
| `spec.retries`                         | Not supported | The field is unsupported because APISIX does not support the features in retries. To configure route retries, you can use [BackendTrafficPolicy](https://docs.api7.ai/enterprise/3.8.x/reference/api7-ingress-controller/api-reference.md#backendtrafficpolicyspec).                                                                                                                                             |
| `spec.sessionPersistence`              | Not supported | APISIX does not support the configuration of cookie lifetimes. As an alternative, you can use [`chash` load balancer](https://docs.api7.ai/enterprise/3.8.x/reference/api7-ingress-controller/api-reference.md#loadbalancer).                                                                                                                                                                                    |
| `spec.rules[].backendRefs[].filters[]` | Not supported | BackendRef-level filters are not implemented as data plane does not support filtering at this level; only rule-level filters (`spec.rules[].filters[]`) are supported.                                                                                                                                                                                                                                           |

#### Gateway[â](#gateway "Direct link to Gateway")

| Fields                                         | Status              | Notes                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `spec.listeners[].port`                        | Not supported\*     | The configuration is required but ignored. This is due to limitations in the data plane: it cannot dynamically open new ports. Since the Ingress Controller does not manage the data plane deployment, it cannot automatically update the configuration or restart the data plane to apply port changes. |
| `spec.listeners[].tls.certificateRefs[].group` | Partially supported | Only `""` is supported; other group values cause validation failure.                                                                                                                                                                                                                                     |
| `spec.listeners[].tls.certificateRefs[].kind`  | Partially supported | Only `Secret` is supported.                                                                                                                                                                                                                                                                              |
| `spec.listeners[].tls.mode`                    | Partially supported | `Terminate` is implemented; `Passthrough` is effectively unsupported for Gateway listeners.                                                                                                                                                                                                              |
| `spec.addresses`                               | Not supported       | Controller does not read or act on `spec.addresses`.                                                                                                                                                                                                                                                     |

### HTTP Route Filters[â](#http-route-filters "Direct link to HTTP Route Filters")

Ingress Controller maps standard Gateway API filters in HTTPRoute resources to corresponding plugins:

| Gateway API Filter       | APISIX Plugin                            |
| ------------------------ | ---------------------------------------- |
| `RequestHeaderModifier`  | `proxy-rewrite`                          |
| `RequestRedirect`        | `redirect`                               |
| `RequestMirror`          | `proxy-mirror`                           |
| `URLRewrite`             | `proxy-rewrite`                          |
| `ResponseHeaderModifier` | `response-rewrite`                       |
| `CORS`                   | `cors`                                   |
| `ExtensionRef`           | user-defined plugin through PluginConfig |

When both standard filters and `ExtensionRef` (referencing a PluginConfig CRD) are used:

* If standard filters are applied first, the PluginConfig overrides any overlapping plugin settings.
* If PluginConfig is applied first, the standard filters are merged into its configuration, and any overlapping fields are overridden by the filters.

## Ingress[â](#ingress "Direct link to Ingress")

### Package[â](#package "Direct link to Package")

* networking.k8s.io/v1

### Supported Resources[â](#supported-resources "Direct link to Supported Resources")

The controller supports the standard Kubernetes Ingress API, including:

* [IngressClass](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/ingress-class-v1/)
* [Ingress](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/ingress-v1/)

Basic host- and path-based routing is supported. Advanced annotations or non-standard extensions may not be implemented.

Refer to [Ingress Annotations](https://docs.api7.ai/enterprise/3.8.x/reference/api7-ingress-controller/annotation.md) for a complete list of supported annotations.
