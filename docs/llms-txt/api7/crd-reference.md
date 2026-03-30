# Source: https://docs.api7.ai/ingress-controller/reference/crd-reference.md

# Custom Resource Definitions API Reference

This document provides the API resource description for the Ingress Controller custom resource definitions (CRDs).

## Packages[â](#packages "Direct link to Packages")

* [apisix.apache.org/v1alpha1](#apisixapacheorgv1alpha1)
* [apisix.apache.org/v2](#apisixapacheorgv2)

## apisix.apache.org/v1alpha1[â](#apisixapacheorgv1alpha1 "Direct link to apisix.apache.org/v1alpha1")

Package v1alpha1 contains API Schema definitions for the apisix.apache.org v1alpha1 API group.

* [BackendTrafficPolicy](#backendtrafficpolicy)
* [Consumer](#consumer)
* [GatewayProxy](#gatewayproxy)
* [HTTPRoutePolicy](#httproutepolicy)
* [PluginConfig](#pluginconfig)

### BackendTrafficPolicy[â](#backendtrafficpolicy "Direct link to BackendTrafficPolicy")

BackendTrafficPolicy defines configuration for traffic handling policies applied to backend services.

| Field                                                                                                              | Description                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `apiVersion` *string*                                                                                              | `apisix.apache.org/v1alpha1`                                                                                                                                         |
| `kind` *string*                                                                                                    | `BackendTrafficPolicy`                                                                                                                                               |
| `metadata` *[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#objectmeta-v1-meta)* | Please refer to the Kubernetes API documentation for details on the `metadata` field.                                                                                |
| `spec` *[BackendTrafficPolicySpec](#backendtrafficpolicyspec)*                                                     | BackendTrafficPolicySpec defines traffic handling policies applied to backend services, such as load balancing strategy, connection settings, and failover behavior. |

### Consumer[â](#consumer "Direct link to Consumer")

Consumer defines configuration for a consumer.

| Field                                                                                                              | Description                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| `apiVersion` *string*                                                                                              | `apisix.apache.org/v1alpha1`                                                                                                 |
| `kind` *string*                                                                                                    | `Consumer`                                                                                                                   |
| `metadata` *[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#objectmeta-v1-meta)* | Please refer to the Kubernetes API documentation for details on the `metadata` field.                                        |
| `spec` *[ConsumerSpec](#consumerspec)*                                                                             | ConsumerSpec defines configuration for a consumer, including consumer name, authentication credentials, and plugin settings. |

### GatewayProxy[â](#gatewayproxy "Direct link to GatewayProxy")

GatewayProxy defines configuration for the gateway proxy instances used to route traffic to services.

| Field                                                                                                              | Description                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| `apiVersion` *string*                                                                                              | `apisix.apache.org/v1alpha1`                                                                                                           |
| `kind` *string*                                                                                                    | `GatewayProxy`                                                                                                                         |
| `metadata` *[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#objectmeta-v1-meta)* | Please refer to the Kubernetes API documentation for details on the `metadata` field.                                                  |
| `spec` *[GatewayProxySpec](#gatewayproxyspec)*                                                                     | GatewayProxySpec defines configuration of gateway proxy instances, including networking settings, global plugins, and plugin metadata. |

### HTTPRoutePolicy[â](#httproutepolicy "Direct link to HTTPRoutePolicy")

HTTPRoutePolicy defines configuration of traffic policies.

| Field                                                                                                              | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| `apiVersion` *string*                                                                                              | `apisix.apache.org/v1alpha1`                                                                                              |
| `kind` *string*                                                                                                    | `HTTPRoutePolicy`                                                                                                         |
| `metadata` *[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#objectmeta-v1-meta)* | Please refer to the Kubernetes API documentation for details on the `metadata` field.                                     |
| `spec` *[HTTPRoutePolicySpec](#httproutepolicyspec)*                                                               | HTTPRoutePolicySpec defines configuration of a HTTPRoutePolicy, including route priority and request matching conditions. |

### PluginConfig[â](#pluginconfig "Direct link to PluginConfig")

PluginConfig defines plugin configuration.

| Field                                                                                                              | Description                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| `apiVersion` *string*                                                                                              | `apisix.apache.org/v1alpha1`                                                                                          |
| `kind` *string*                                                                                                    | `PluginConfig`                                                                                                        |
| `metadata` *[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#objectmeta-v1-meta)* | Please refer to the Kubernetes API documentation for details on the `metadata` field.                                 |
| `spec` *[PluginConfigSpec](#pluginconfigspec)*                                                                     | PluginConfigSpec defines the desired state of a PluginConfig, in which plugins and their configuration are specified. |

### Types[â](#types "Direct link to Types")

This section describes the types used by the CRDs.

#### AdminKeyAuth[â](#adminkeyauth "Direct link to AdminKeyAuth")

AdminKeyAuth defines the admin key authentication configuration.

| Field                                                 | Description                                                                 |
| ----------------------------------------------------- | --------------------------------------------------------------------------- |
| `value` *string*                                      | Value sets the admin key value explicitly (not recommended for production). |
| `valueFrom` *[AdminKeyValueFrom](#adminkeyvaluefrom)* | ValueFrom specifies the source of the admin key.                            |

*Appears in:*

* [ControlPlaneAuth](#controlplaneauth)

#### AdminKeyValueFrom[â](#adminkeyvaluefrom "Direct link to AdminKeyValueFrom")

AdminKeyValueFrom defines the source of the admin key.

| Field                                                    | Description                                |
| -------------------------------------------------------- | ------------------------------------------ |
| `secretKeyRef` *[SecretKeySelector](#secretkeyselector)* | SecretKeyRef references a key in a Secret. |

*Appears in:*

* [AdminKeyAuth](#adminkeyauth)

#### AuthType[â](#authtype "Direct link to AuthType")

*Base type:* `string`

AuthType defines the type of authentication.

*Appears in:*

* [ControlPlaneAuth](#controlplaneauth)

#### BackendPolicyTargetReferenceWithSectionName[â](#backendpolicytargetreferencewithsectionname "Direct link to BackendPolicyTargetReferenceWithSectionName")

*Base type:* `LocalPolicyTargetReferenceWithSectionName`

| Field                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `group` *[Group](#group)*                   | Group is the group of the target resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `kind` *[Kind](#kind)*                      | Kind is kind of the target resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `name` *[ObjectName](#objectname)*          | Name is the name of the target resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `sectionName` *[SectionName](#sectionname)* | SectionName is the name of a section within the target resource. When unspecified, this targetRef targets the entire resource. In the following resources, SectionName is interpreted as the following:<br /><br />â¢ Gateway: Listener name<br />â¢ HTTPRoute: HTTPRouteRule name<br />â¢ Service: Port name<br /><br />If a SectionName is specified, but does not exist on the targeted object, the Policy must fail to attach, and the policy implementation should record a `ResolvedRefs` or similar Condition in the Policy's status. |

*Appears in:*

* [BackendTrafficPolicySpec](#backendtrafficpolicyspec)

#### BackendTrafficPolicySpec[â](#backendtrafficpolicyspec "Direct link to BackendTrafficPolicySpec")

| Field                                                                                                            | Description                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `targetRefs` *[BackendPolicyTargetReferenceWithSectionName](#backendpolicytargetreferencewithsectionname) array* | TargetRef identifies an API object to apply policy to. Currently, Backends (i.e. Service, ServiceImport, or any implementation-specific backendRef) are the only valid API target references.                                                                                                                           |
| `loadbalancer` *[LoadBalancer](#loadbalancer)*                                                                   | LoadBalancer represents the load balancer configuration for Kubernetes Service. The default strategy is round robin.                                                                                                                                                                                                    |
| `scheme` *string*                                                                                                | Scheme is the protocol used to communicate with the upstream. Default is `http`. Can be `http`, `https`, `grpc`, or `grpcs`.                                                                                                                                                                                            |
| `retries` *integer*                                                                                              | Retries specify the number of times the gateway should retry sending requests when errors such as timeouts or 502 errors occur.                                                                                                                                                                                         |
| `timeout` *[Timeout](#timeout)*                                                                                  | Timeout sets the read, send, and connect timeouts to the upstream.                                                                                                                                                                                                                                                      |
| `passHost` *string*                                                                                              | PassHost configures how the host header should be determined when a request is forwarded to the upstream. Default is `pass`. Can be `pass`, `node` or `rewrite`:<br />â¢ `pass`: preserve the original Host header<br />â¢ `node`: use the upstream nodeâs host<br />â¢ `rewrite`: set to a custom host via `upstreamHost` |
| `upstreamHost` *[Hostname](#hostname)*                                                                           | UpstreamHost specifies the host of the Upstream request. Used only if passHost is set to `rewrite`.                                                                                                                                                                                                                     |

*Appears in:*

* [BackendTrafficPolicy](#backendtrafficpolicy)

#### ConsumerSpec[â](#consumerspec "Direct link to ConsumerSpec")

| Field                                           | Description                                                 |
| ----------------------------------------------- | ----------------------------------------------------------- |
| `gatewayRef` *[GatewayRef](#gatewayref)*        | GatewayRef specifies the gateway details.                   |
| `credentials` *[Credential](#credential) array* | Credentials specifies the credential details of a consumer. |
| `plugins` *[Plugin](#plugin) array*             | Plugins define the plugins associated with a consumer.      |

*Appears in:*

* [Consumer](#consumer)

#### ControlPlaneAuth[â](#controlplaneauth "Direct link to ControlPlaneAuth")

ControlPlaneAuth defines the authentication configuration for control plane.

| Field                                      | Description                                                        |
| ------------------------------------------ | ------------------------------------------------------------------ |
| `type` *[AuthType](#authtype)*             | Type specifies the type of authentication. Can only be `AdminKey`. |
| `adminKey` *[AdminKeyAuth](#adminkeyauth)* | AdminKey specifies the admin key authentication configuration.     |

*Appears in:*

* [ControlPlaneProvider](#controlplaneprovider)

#### ControlPlaneProvider[â](#controlplaneprovider "Direct link to ControlPlaneProvider")

ControlPlaneProvider defines configuration for control plane provider.

| Field                                           | Description                                                                                |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `mode` *string*                                 | Mode specifies the mode of control plane provider. Can be `apisix` or `apisix-standalone`. |
| `endpoints` *string array*                      | Endpoints specifies the list of control plane endpoints.                                   |
| `service` *[ProviderService](#providerservice)* |                                                                                            |
| `tlsVerify` *boolean*                           | TlsVerify specifies whether to verify the TLS certificate of the control plane.            |
| `auth` *[ControlPlaneAuth](#controlplaneauth)*  | Auth specifies the authentication configuration.                                           |

*Appears in:*

* [GatewayProxyProvider](#gatewayproxyprovider)

#### Credential[â](#credential "Direct link to Credential")

| Field                                                                                                                | Description                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `type` *string*                                                                                                      | Type specifies the type of authentication to configure credentials for. Can be `jwt-auth`, `basic-auth`, `key-auth`, or `hmac-auth`. |
| `config` *[JSON](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#json-v1-apiextensions-k8s-io)* | Config specifies the credential details for authentication.                                                                          |
| `secretRef` *[SecretReference](#secretreference)*                                                                    | SecretRef references to the Secret that contains the credentials.                                                                    |
| `name` *string*                                                                                                      | Name is the name of the credential.                                                                                                  |

*Appears in:*

* [ConsumerSpec](#consumerspec)

#### GatewayProxyPlugin[â](#gatewayproxyplugin "Direct link to GatewayProxyPlugin")

GatewayProxyPlugin contains plugin configuration.

| Field                                                                                                                | Description                                        |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| `name` *string*                                                                                                      | Name is the name of the plugin.                    |
| `enabled` *boolean*                                                                                                  | Enabled defines whether the plugin is enabled.     |
| `config` *[JSON](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#json-v1-apiextensions-k8s-io)* | Config defines the plugin's configuration details. |

*Appears in:*

* [GatewayProxySpec](#gatewayproxyspec)

#### GatewayProxyProvider[â](#gatewayproxyprovider "Direct link to GatewayProxyProvider")

GatewayProxyProvider defines the provider configuration for GatewayProxy.

| Field                                                          | Description                                                          |
| -------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type` *[ProviderType](#providertype)*                         | Type specifies the type of provider. Can only be `ControlPlane`.     |
| `controlPlane` *[ControlPlaneProvider](#controlplaneprovider)* | ControlPlane specifies the configuration for control plane provider. |

*Appears in:*

* [GatewayProxySpec](#gatewayproxyspec)

#### GatewayProxySpec[â](#gatewayproxyspec "Direct link to GatewayProxySpec")

GatewayProxySpec defines the desired state of GatewayProxy.

| Field                                                                                                                                                                     | Description                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `publishService` *string*                                                                                                                                                 | PublishService specifies the LoadBalancer-type Service whose external address the controller uses to update the status of Ingress resources.                           |
| `statusAddress` *string array*                                                                                                                                            | StatusAddress specifies the external IP addresses that the controller uses to populate the status field of GatewayProxy or Ingress resources for developers to access. |
| `provider` *[GatewayProxyProvider](#gatewayproxyprovider)*                                                                                                                | Provider configures the provider details.                                                                                                                              |
| `plugins` *[GatewayProxyPlugin](#gatewayproxyplugin) array*                                                                                                               | Plugins configure global plugins.                                                                                                                                      |
| `pluginMetadata` *object (keys<!-- -->:string<!-- -->, values:[JSON](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#json-v1-apiextensions-k8s-io))* | PluginMetadata configures common configuration shared by all plugin instances of the same name.                                                                        |

*Appears in:*

* [GatewayProxy](#gatewayproxy)

#### GatewayRef[â](#gatewayref "Direct link to GatewayRef")

| Field                | Description                                                                             |
| -------------------- | --------------------------------------------------------------------------------------- |
| `name` *string*      | Name is the name of the gateway.                                                        |
| `kind` *string*      | Kind is the type of Kubernetes object. Default is `Gateway`.                            |
| `group` *string*     | Group is the API group the resource belongs to. Default is `gateway.networking.k8s.io`. |
| `namespace` *string* | Namespace is namespace of the resource.                                                 |

*Appears in:*

* [ConsumerSpec](#consumerspec)

#### HTTPRoutePolicySpec[â](#httproutepolicyspec "Direct link to HTTPRoutePolicySpec")

HTTPRoutePolicySpec defines the desired state of HTTPRoutePolicy.

| Field                                                                                                                    | Description                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `targetRefs` *LocalPolicyTargetReferenceWithSectionName array*                                                           | TargetRef identifies an API object (i.e. HTTPRoute, Ingress) to apply HTTPRoutePolicy to.                                                   |
| `priority` *integer*                                                                                                     | Priority sets the priority for route. when multiple routes have the same URI path, a higher value sets a higher priority in route matching. |
| `vars` *[JSON](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#json-v1-apiextensions-k8s-io) array* | Vars sets the request matching conditions.                                                                                                  |

*Appears in:*

* [HTTPRoutePolicy](#httproutepolicy)

#### Hostname[â](#hostname "Direct link to Hostname")

*Base type:* `string`

*Appears in:*

* [BackendTrafficPolicySpec](#backendtrafficpolicyspec)

#### LoadBalancer[â](#loadbalancer "Direct link to LoadBalancer")

LoadBalancer describes the load balancing parameters.

| Field             | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type` *string*   | Type specifies the load balancing algorithms to route traffic to the backend. Default is `roundrobin`. Can be `roundrobin`, `chash`, `ewma`, or `least_conn`.                                                                                                                                                                                                                                                         |
| `hashOn` *string* | HashOn specified the type of field used for hashing, required when type is `chash`. Default is `vars`. Can be `vars`, `header`, `cookie`, `consumer`, or `vars_combinations`.                                                                                                                                                                                                                                         |
| `key` *string*    | Key is used with HashOn, generally required when type is `chash`. When HashOn is `header` or `cookie`, specifies the name of the header or cookie. When HashOn is `consumer`, key is not required, as the consumer name is used automatically. When HashOn is `vars` or `vars_combinations`, key refers to one or a combination of [built-in variables](https://docs.api7.ai/apisix/reference/built-in-variables.md). |

*Appears in:*

* [BackendTrafficPolicySpec](#backendtrafficpolicyspec)

#### Plugin[â](#plugin "Direct link to Plugin")

| Field                                                                                                                | Description                             |
| -------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| `name` *string*                                                                                                      | Name is the name of the plugin.         |
| `config` *[JSON](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#json-v1-apiextensions-k8s-io)* | Config is plugin configuration details. |

*Appears in:*

* [ConsumerSpec](#consumerspec)
* [PluginConfigSpec](#pluginconfigspec)

#### PluginConfigSpec[â](#pluginconfigspec "Direct link to PluginConfigSpec")

PluginConfigSpec defines the desired state of PluginConfig.

| Field                               | Description                                                            |
| ----------------------------------- | ---------------------------------------------------------------------- |
| `plugins` *[Plugin](#plugin) array* | Plugins are an array of plugins and their configuration to be applied. |

*Appears in:*

* [PluginConfig](#pluginconfig)

#### ProviderService[â](#providerservice "Direct link to ProviderService")

| Field            | Description                       |
| ---------------- | --------------------------------- |
| `name` *string*  | Name is the name of the provider. |
| `port` *integer* | Port is the port of the provider. |

*Appears in:*

* [ControlPlaneProvider](#controlplaneprovider)

#### ProviderType[â](#providertype "Direct link to ProviderType")

*Base type:* `string`

ProviderType defines the type of provider.

*Appears in:*

* [GatewayProxyProvider](#gatewayproxyprovider)

#### SecretKeySelector[â](#secretkeyselector "Direct link to SecretKeySelector")

SecretKeySelector defines a reference to a specific key within a Secret.

| Field           | Description                                               |
| --------------- | --------------------------------------------------------- |
| `name` *string* | Name is the name of the secret.                           |
| `key` *string*  | Key is the key in the secret to retrieve the secret from. |

*Appears in:*

* [AdminKeyValueFrom](#adminkeyvaluefrom)

#### SecretReference[â](#secretreference "Direct link to SecretReference")

| Field                | Description                               |
| -------------------- | ----------------------------------------- |
| `name` *string*      | Name is the name of the secret.           |
| `namespace` *string* | Namespace is the namespace of the secret. |

*Appears in:*

* [Credential](#credential)

#### Status[â](#status "Direct link to Status")

| Field                                                                                                                    | Description |
| ------------------------------------------------------------------------------------------------------------------------ | ----------- |
| `conditions` *[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#condition-v1-meta) array* |             |

*Appears in:*

* [ConsumerStatus](#consumerstatus)

#### Timeout[â](#timeout "Direct link to Timeout")

| Field                                                                                                         | Description                           |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| `connect` *[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#duration-v1-meta)* | Connection timeout. Default is `60s`. |
| `send` *[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#duration-v1-meta)*    | Send timeout. Default is `60s`.       |
| `read` *[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#duration-v1-meta)*    | Read timeout. Default is `60s`.       |

*Appears in:*

* [BackendTrafficPolicySpec](#backendtrafficpolicyspec)

## apisix.apache.org/v2[â](#apisixapacheorgv2 "Direct link to apisix.apache.org/v2")

Package v2 contains API Schema definitions for the apisix.apache.org v2 API group.

* [ApisixConsumer](#apisixconsumer)
* [ApisixGlobalRule](#apisixglobalrule)
* [ApisixPluginConfig](#apisixpluginconfig)
* [ApisixRoute](#apisixroute)
* [ApisixTls](#apisixtls)
* [ApisixUpstream](#apisixupstream)

### ApisixConsumer[â](#apisixconsumer "Direct link to ApisixConsumer")

ApisixConsumer defines configuration of a consumer and their authentication details.

| Field                                                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| `apiVersion` *string*                                                                                              | `apisix.apache.org/v2`                                                                |
| `kind` *string*                                                                                                    | `ApisixConsumer`                                                                      |
| `metadata` *[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#objectmeta-v1-meta)* | Please refer to the Kubernetes API documentation for details on the `metadata` field. |
| `spec` *[ApisixConsumerSpec](#apisixconsumerspec)*                                                                 | ApisixConsumerSpec defines the consumer authentication configuration.                 |

### ApisixGlobalRule[â](#apisixglobalrule "Direct link to ApisixGlobalRule")

ApisixGlobalRule defines configuration for global plugins.

| Field                                                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| `apiVersion` *string*                                                                                              | `apisix.apache.org/v2`                                                                |
| `kind` *string*                                                                                                    | `ApisixGlobalRule`                                                                    |
| `metadata` *[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#objectmeta-v1-meta)* | Please refer to the Kubernetes API documentation for details on the `metadata` field. |
| `spec` *[ApisixGlobalRuleSpec](#apisixglobalrulespec)*                                                             | ApisixGlobalRuleSpec defines the global plugin configuration.                         |

### ApisixPluginConfig[â](#apisixpluginconfig "Direct link to ApisixPluginConfig")

ApisixPluginConfig defines a reusable set of plugin configuration that can be referenced by routes.

| Field                                                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| `apiVersion` *string*                                                                                              | `apisix.apache.org/v2`                                                                |
| `kind` *string*                                                                                                    | `ApisixPluginConfig`                                                                  |
| `metadata` *[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#objectmeta-v1-meta)* | Please refer to the Kubernetes API documentation for details on the `metadata` field. |
| `spec` *[ApisixPluginConfigSpec](#apisixpluginconfigspec)*                                                         | ApisixPluginConfigSpec defines the plugin config configuration.                       |

### ApisixRoute[â](#apisixroute "Direct link to ApisixRoute")

ApisixRoute defines configuration for HTTP and stream routes.

| Field                                                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| `apiVersion` *string*                                                                                              | `apisix.apache.org/v2`                                                                |
| `kind` *string*                                                                                                    | `ApisixRoute`                                                                         |
| `metadata` *[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#objectmeta-v1-meta)* | Please refer to the Kubernetes API documentation for details on the `metadata` field. |
| `spec` *[ApisixRouteSpec](#apisixroutespec)*                                                                       | ApisixRouteSpec defines HTTP and stream route configuration.                          |

### ApisixTls[â](#apisixtls "Direct link to ApisixTls")

ApisixTls defines configuration for TLS and mutual TLS (mTLS).

| Field                                                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| `apiVersion` *string*                                                                                              | `apisix.apache.org/v2`                                                                |
| `kind` *string*                                                                                                    | `ApisixTls`                                                                           |
| `metadata` *[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#objectmeta-v1-meta)* | Please refer to the Kubernetes API documentation for details on the `metadata` field. |
| `spec` *[ApisixTlsSpec](#apisixtlsspec)*                                                                           | ApisixTlsSpec defines the TLS configuration.                                          |

### ApisixUpstream[â](#apisixupstream "Direct link to ApisixUpstream")

ApisixUpstream defines configuration for upstream services.

| Field                                                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| `apiVersion` *string*                                                                                              | `apisix.apache.org/v2`                                                                |
| `kind` *string*                                                                                                    | `ApisixUpstream`                                                                      |
| `metadata` *[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#objectmeta-v1-meta)* | Please refer to the Kubernetes API documentation for details on the `metadata` field. |
| `spec` *[ApisixUpstreamSpec](#apisixupstreamspec)*                                                                 | ApisixUpstreamSpec defines the upstream configuration.                                |

### Types[â](#types-1 "Direct link to Types")

This section describes the types used by the CRDs.

#### ActiveHealthCheck[â](#activehealthcheck "Direct link to ActiveHealthCheck")

ActiveHealthCheck defines the active upstream health check configuration.

| Field                                                                   | Description                                                               |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `type` *string*                                                         | Type is the health check type. Can be `http`, `https`, or `tcp`.          |
| `timeout` *[Duration](#duration)*                                       | Timeout sets health check timeout in seconds.                             |
| `concurrency` *integer*                                                 | Concurrency sets the number of targets to be checked at the same time.    |
| `host` *string*                                                         | Host sets the upstream host.                                              |
| `port` *integer*                                                        | Port sets the upstream port.                                              |
| `httpPath` *string*                                                     | HTTPPath sets the HTTP probe request path.                                |
| `strictTLS` *boolean*                                                   | StrictTLS sets whether to enforce TLS.                                    |
| `requestHeaders` *string array*                                         | RequestHeaders sets the request headers.                                  |
| `healthy` *[ActiveHealthCheckHealthy](#activehealthcheckhealthy)*       | Healthy configures the rules that define an upstream node as healthy.     |
| `unhealthy` *[ActiveHealthCheckUnhealthy](#activehealthcheckunhealthy)* | Unhealthy configures the rules that define an upstream node as unhealthy. |

*Appears in:*

* [HealthCheck](#healthcheck)

#### ActiveHealthCheckHealthy[â](#activehealthcheckhealthy "Direct link to ActiveHealthCheckHealthy")

UpstreamActiveHealthCheckHealthy defines the conditions used to actively determine whether an upstream node is healthy.

| Field                                                                                                          | Description                                                                  |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `httpCodes` *integer array*                                                                                    | HTTPCodes define a list of HTTP status codes that are considered healthy.    |
| `successes` *integer*                                                                                          | Successes define the number of successful probes to define a healthy target. |
| `interval` *[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#duration-v1-meta)* | Interval defines the time interval for checking targets, in seconds.         |

*Appears in:*

* [ActiveHealthCheck](#activehealthcheck)

#### ActiveHealthCheckUnhealthy[â](#activehealthcheckunhealthy "Direct link to ActiveHealthCheckUnhealthy")

UpstreamActiveHealthCheckHealthy defines the conditions used to actively determine whether an upstream node is unhealthy.

| Field                                                                                                          | Description                                                                    |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| `httpCodes` *integer array*                                                                                    | HTTPCodes define a list of HTTP status codes that are considered unhealthy.    |
| `httpFailures` *integer*                                                                                       | HTTPFailures define the number of HTTP failures to define an unhealthy target. |
| `tcpFailures` *integer*                                                                                        | TCPFailures define the number of TCP failures to define an unhealthy target.   |
| `timeout` *integer*                                                                                            | Timeout sets the number of timeouts to define an unhealthy target.             |
| `interval` *[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#duration-v1-meta)* | Interval defines the time interval for checking targets, in seconds.           |

*Appears in:*

* [ActiveHealthCheck](#activehealthcheck)

#### ApisixConsumerAuthParameter[â](#apisixconsumerauthparameter "Direct link to ApisixConsumerAuthParameter")

| Field                                                             | Description                                               |
| ----------------------------------------------------------------- | --------------------------------------------------------- |
| `basicAuth` *[ApisixConsumerBasicAuth](#apisixconsumerbasicauth)* | BasicAuth configures the basic authentication details.    |
| `keyAuth` *[ApisixConsumerKeyAuth](#apisixconsumerkeyauth)*       | KeyAuth configures the key authentication details.        |
| `wolfRBAC` *[ApisixConsumerWolfRBAC](#apisixconsumerwolfrbac)*    | WolfRBAC configures the Wolf RBAC authentication details. |
| `jwtAuth` *[ApisixConsumerJwtAuth](#apisixconsumerjwtauth)*       | JwtAuth configures the JWT authentication details.        |
| `hmacAuth` *[ApisixConsumerHMACAuth](#apisixconsumerhmacauth)*    | HMACAuth configures the HMAC authentication details.      |
| `ldapAuth` *[ApisixConsumerLDAPAuth](#apisixconsumerldapauth)*    | LDAPAuth configures the LDAP authentication details.      |

*Appears in:*

* [ApisixConsumerSpec](#apisixconsumerspec)

#### ApisixConsumerBasicAuth[â](#apisixconsumerbasicauth "Direct link to ApisixConsumerBasicAuth")

ApisixConsumerBasicAuth defines configuration for basic authentication.

| Field                                                                                                                                   | Description                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `secretRef` *[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#localobjectreference-v1-core)* | SecretRef references a Kubernetes Secret containing the basic authentication credentials. |
| `value` *[ApisixConsumerBasicAuthValue](#apisixconsumerbasicauthvalue)*                                                                 | Value specifies the basic authentication credentials.                                     |

*Appears in:*

* [ApisixConsumerAuthParameter](#apisixconsumerauthparameter)

#### ApisixConsumerBasicAuthValue[â](#apisixconsumerbasicauthvalue "Direct link to ApisixConsumerBasicAuthValue")

ApisixConsumerBasicAuthValue defines the username and password configuration for basic authentication.

| Field               | Description                                    |
| ------------------- | ---------------------------------------------- |
| `username` *string* | Username is the basic authentication username. |
| `password` *string* | Password is the basic authentication password. |

*Appears in:*

* [ApisixConsumerBasicAuth](#apisixconsumerbasicauth)

#### ApisixConsumerHMACAuth[â](#apisixconsumerhmacauth "Direct link to ApisixConsumerHMACAuth")

ApisixConsumerHMACAuth defines configuration for the HMAC authentication.

| Field                                                                                                                                   | Description                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `secretRef` *[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#localobjectreference-v1-core)* | SecretRef references a Kubernetes Secret containing the HMAC credentials. |
| `value` *[ApisixConsumerHMACAuthValue](#apisixconsumerhmacauthvalue)*                                                                   | Value specifies HMAC authentication credentials.                          |

*Appears in:*

* [ApisixConsumerAuthParameter](#apisixconsumerauthparameter)

#### ApisixConsumerHMACAuthValue[â](#apisixconsumerhmacauthvalue "Direct link to ApisixConsumerHMACAuthValue")

ApisixConsumerHMACAuthValue defines configuration for HMAC authentication.

| Field                             | Description                                                                                                                         |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `key_id` *string*                 | KeyID is the identifier used to look up the HMAC secret.                                                                            |
| `secret_key` *string*             | SecretKey is the HMAC secret used to sign the request.                                                                              |
| `access_key` *string*             | AccessKey is the identifier used to look up the HMAC secret. Deprecated from consumer configuration                                 |
| `algorithm` *string*              | Algorithm specifies the hashing algorithm (e.g., "hmac-sha256"). Deprecated from consumer configuration                             |
| `clock_skew` *integer*            | ClockSkew is the allowed time difference (in seconds) between client and server clocks. Deprecated from consumer configuration      |
| `signed_headers` *string array*   | SignedHeaders lists the headers that must be included in the signature. Deprecated from consumer configuration                      |
| `keep_headers` *boolean*          | KeepHeaders determines whether the HMAC signature headers are preserved after verification. Deprecated from consumer configuration  |
| `encode_uri_params` *boolean*     | EncodeURIParams indicates whether URI parameters are encoded when calculating the signature. Deprecated from consumer configuration |
| `validate_request_body` *boolean* | ValidateRequestBody enables HMAC validation of the request body. Deprecated from consumer configuration                             |
| `max_req_body` *integer*          | MaxReqBody sets the maximum size (in bytes) of the request body that can be validated. Deprecated from consumer configuration       |

*Appears in:*

* [ApisixConsumerHMACAuth](#apisixconsumerhmacauth)

#### ApisixConsumerJwtAuth[â](#apisixconsumerjwtauth "Direct link to ApisixConsumerJwtAuth")

ApisixConsumerJwtAuth defines configuration for JWT authentication.

| Field                                                                                                                                   | Description                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `secretRef` *[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#localobjectreference-v1-core)* | SecretRef references a Kubernetes Secret containing JWT authentication credentials. |
| `value` *[ApisixConsumerJwtAuthValue](#apisixconsumerjwtauthvalue)*                                                                     | Value specifies JWT authentication credentials.                                     |

*Appears in:*

* [ApisixConsumerAuthParameter](#apisixconsumerauthparameter)

#### ApisixConsumerJwtAuthValue[â](#apisixconsumerjwtauthvalue "Direct link to ApisixConsumerJwtAuthValue")

ApisixConsumerJwtAuthValue defines configuration for JWT authentication.

| Field                             | Description                                                                                                                                                                                                                                                                               |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key` *string*                    | Key is the unique identifier for the JWT credential.                                                                                                                                                                                                                                      |
| `secret` *string*                 | Secret is the shared secret used to sign the JWT (for symmetric algorithms).                                                                                                                                                                                                              |
| `public_key` *string*             | PublicKey is the public key used to verify JWT signatures (for asymmetric algorithms).                                                                                                                                                                                                    |
| `private_key` *string*            | PrivateKey is the private key used to sign the JWT (for asymmetric algorithms).                                                                                                                                                                                                           |
| `algorithm` *string*              | Algorithm specifies the signing algorithm. Can be `HS256`, `HS384`, `HS512`, `RS256`, `RS384`, `RS512`, `ES256`, `ES384`, `ES512`, `PS256`, `PS384`, `PS512`, or `EdDSA`. Currently APISIX only supports `HS256`, `HS512`, `RS256`, and `ES256`. API7 Enterprise supports all algorithms. |
| `exp` *integer*                   | Exp is the token expiration period in seconds.                                                                                                                                                                                                                                            |
| `base64_secret` *boolean*         | Base64Secret indicates whether the secret is base64-encoded.                                                                                                                                                                                                                              |
| `lifetime_grace_period` *integer* | LifetimeGracePeriod is the allowed clock skew in seconds for token expiration.                                                                                                                                                                                                            |

*Appears in:*

* [ApisixConsumerJwtAuth](#apisixconsumerjwtauth)

#### ApisixConsumerKeyAuth[â](#apisixconsumerkeyauth "Direct link to ApisixConsumerKeyAuth")

ApisixConsumerKeyAuth defines configuration for the key auth.

| Field                                                                                                                                   | Description                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `secretRef` *[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#localobjectreference-v1-core)* | SecretRef references a Kubernetes Secret containing the key authentication credentials. |
| `value` *[ApisixConsumerKeyAuthValue](#apisixconsumerkeyauthvalue)*                                                                     | Value specifies the key authentication credentials.                                     |

*Appears in:*

* [ApisixConsumerAuthParameter](#apisixconsumerauthparameter)

#### ApisixConsumerKeyAuthValue[â](#apisixconsumerkeyauthvalue "Direct link to ApisixConsumerKeyAuthValue")

ApisixConsumerKeyAuthValue defines configuration for key authentication.

| Field          | Description                                        |
| -------------- | -------------------------------------------------- |
| `key` *string* | Key is the credential used for key authentication. |

*Appears in:*

* [ApisixConsumerKeyAuth](#apisixconsumerkeyauth)

#### ApisixConsumerLDAPAuth[â](#apisixconsumerldapauth "Direct link to ApisixConsumerLDAPAuth")

ApisixConsumerLDAPAuth defines configuration for the LDAP authentication.

| Field                                                                                                                                   | Description                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `secretRef` *[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#localobjectreference-v1-core)* | SecretRef references a Kubernetes Secret containing the LDAP credentials. |
| `value` *[ApisixConsumerLDAPAuthValue](#apisixconsumerldapauthvalue)*                                                                   | Value specifies LDAP authentication credentials.                          |

*Appears in:*

* [ApisixConsumerAuthParameter](#apisixconsumerauthparameter)

#### ApisixConsumerLDAPAuthValue[â](#apisixconsumerldapauthvalue "Direct link to ApisixConsumerLDAPAuthValue")

ApisixConsumerLDAPAuthValue defines configuration for LDAP authentication.

| Field              | Description                                             |
| ------------------ | ------------------------------------------------------- |
| `user_dn` *string* | UserDN is the distinguished name (DN) of the LDAP user. |

*Appears in:*

* [ApisixConsumerLDAPAuth](#apisixconsumerldapauth)

#### ApisixConsumerSpec[â](#apisixconsumerspec "Direct link to ApisixConsumerSpec")

ApisixConsumerSpec defines the desired state of ApisixConsumer.

| Field                                                                         | Description                                                                                                                                        |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ingressClassName` *string*                                                   | IngressClassName is the name of an IngressClass cluster resource. The controller uses this field to decide whether the resource should be managed. |
| `authParameter` *[ApisixConsumerAuthParameter](#apisixconsumerauthparameter)* | AuthParameter defines the authentication credentials and configuration for this consumer.                                                          |

*Appears in:*

* [ApisixConsumer](#apisixconsumer)

#### ApisixConsumerWolfRBAC[â](#apisixconsumerwolfrbac "Direct link to ApisixConsumerWolfRBAC")

ApisixConsumerWolfRBAC defines configuration for the Wolf RBAC authentication.

| Field                                                                                                                                   | Description                                                              |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `secretRef` *[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#localobjectreference-v1-core)* | SecretRef references a Kubernetes Secret containing the Wolf RBAC token. |
| `value` *[ApisixConsumerWolfRBACValue](#apisixconsumerwolfrbacvalue)*                                                                   | Value specifies the Wolf RBAC token.                                     |

*Appears in:*

* [ApisixConsumerAuthParameter](#apisixconsumerauthparameter)

#### ApisixConsumerWolfRBACValue[â](#apisixconsumerwolfrbacvalue "Direct link to ApisixConsumerWolfRBACValue")

ApisixConsumerWolfRBACValue defines configuration for Wolf RBAC authentication.

| Field                    | Description                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------- |
| `server` *string*        | Server is the URL of the Wolf RBAC server.                                             |
| `appid` *string*         | Appid is the application identifier used when communicating with the Wolf RBAC server. |
| `header_prefix` *string* | HeaderPrefix is the prefix added to request headers for RBAC enforcement.              |

*Appears in:*

* [ApisixConsumerWolfRBAC](#apisixconsumerwolfrbac)

#### ApisixGlobalRuleSpec[â](#apisixglobalrulespec "Direct link to ApisixGlobalRuleSpec")

ApisixGlobalRuleSpec defines configuration for global plugins.

| Field                                                     | Description                                                                                                                                        |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ingressClassName` *string*                               | IngressClassName is the name of an IngressClass cluster resource. The controller uses this field to decide whether the resource should be managed. |
| `plugins` *[ApisixRoutePlugin](#apisixrouteplugin) array* | Plugins contain a list of global plugins.                                                                                                          |

*Appears in:*

* [ApisixGlobalRule](#apisixglobalrule)

#### ApisixMutualTlsClientConfig[â](#apisixmutualtlsclientconfig "Direct link to ApisixMutualTlsClientConfig")

ApisixMutualTlsClientConfig describes the mutual TLS CA and verification settings.

| Field                                      | Description                                                                                     |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| `caSecret` *[ApisixSecret](#apisixsecret)* | CASecret references the secret containing the CA certificate for client certificate validation. |
| `depth` *integer*                          | Depth specifies the maximum verification depth for the client certificate chain.                |
| `skip_mtls_uri_regex` *string array*       | SkipMTLSUriRegex contains RegEx patterns for URIs to skip mutual TLS verification.              |

*Appears in:*

* [ApisixTlsSpec](#apisixtlsspec)

#### ApisixPluginConfigSpec[â](#apisixpluginconfigspec "Direct link to ApisixPluginConfigSpec")

ApisixPluginConfigSpec defines the desired state of ApisixPluginConfigSpec.

| Field                                                     | Description                                                                                                                                        |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ingressClassName` *string*                               | IngressClassName is the name of an IngressClass cluster resource. The controller uses this field to decide whether the resource should be managed. |
| `plugins` *[ApisixRoutePlugin](#apisixrouteplugin) array* | Plugins contain a list of plugins.                                                                                                                 |

*Appears in:*

* [ApisixPluginConfig](#apisixpluginconfig)

#### ApisixRouteAuthentication[â](#apisixrouteauthentication "Direct link to ApisixRouteAuthentication")

ApisixRouteAuthentication represents authentication-related configuration in ApisixRoute.

| Field                                                                                | Description                                             |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| `enable` *boolean*                                                                   | Enable toggles authentication on or off.                |
| `type` *string*                                                                      | Type specifies the authentication type.                 |
| `keyAuth` *[ApisixRouteAuthenticationKeyAuth](#apisixrouteauthenticationkeyauth)*    | KeyAuth defines configuration for key authentication.   |
| `jwtAuth` *[ApisixRouteAuthenticationJwtAuth](#apisixrouteauthenticationjwtauth)*    | JwtAuth defines configuration for JWT authentication.   |
| `ldapAuth` *[ApisixRouteAuthenticationLDAPAuth](#apisixrouteauthenticationldapauth)* | LDAPAuth defines configuration for LDAP authentication. |

*Appears in:*

* [ApisixRouteHTTP](#apisixroutehttp)

#### ApisixRouteAuthenticationJwtAuth[â](#apisixrouteauthenticationjwtauth "Direct link to ApisixRouteAuthenticationJwtAuth")

ApisixRouteAuthenticationJwtAuth defines JWT authentication configuration in ApisixRouteAuthentication.

| Field             | Description                                                             |
| ----------------- | ----------------------------------------------------------------------- |
| `header` *string* | Header specifies the HTTP header name to look for the JWT token.        |
| `query` *string*  | Query specifies the URL query parameter name to look for the JWT token. |
| `cookie` *string* | Cookie specifies the cookie name to look for the JWT token.             |

*Appears in:*

* [ApisixRouteAuthentication](#apisixrouteauthentication)

#### ApisixRouteAuthenticationKeyAuth[â](#apisixrouteauthenticationkeyauth "Direct link to ApisixRouteAuthenticationKeyAuth")

ApisixRouteAuthenticationKeyAuth defines key authentication configuration in ApisixRouteAuthentication.

| Field             | Description                                                                     |
| ----------------- | ------------------------------------------------------------------------------- |
| `header` *string* | Header specifies the HTTP header name to look for the key authentication token. |

*Appears in:*

* [ApisixRouteAuthentication](#apisixrouteauthentication)

#### ApisixRouteAuthenticationLDAPAuth[â](#apisixrouteauthenticationldapauth "Direct link to ApisixRouteAuthenticationLDAPAuth")

ApisixRouteAuthenticationLDAPAuth defines LDAP authentication configuration in ApisixRouteAuthentication.

| Field               | Description                                                   |
| ------------------- | ------------------------------------------------------------- |
| `base_dn` *string*  | BaseDN is the base distinguished name (DN) for LDAP searches. |
| `ldap_uri` *string* | LDAPURI is the URI of the LDAP server.                        |
| `use_tls` *boolean* | UseTLS indicates whether to use TLS for the LDAP connection.  |
| `uid` *string*      | UID is the user identifier attribute in LDAP.                 |

*Appears in:*

* [ApisixRouteAuthentication](#apisixrouteauthentication)

#### ApisixRouteHTTP[â](#apisixroutehttp "Direct link to ApisixRouteHTTP")

ApisixRouteHTTP represents a single HTTP route configuration.

| Field                                                                             | Description                                                                                                                                                                                   |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name` *string*                                                                   | Name is the unique rule name and cannot be empty.                                                                                                                                             |
| `priority` *integer*                                                              | Priority defines the route priority when multiple routes share the same URI path. Higher values mean higher priority in route matching.                                                       |
| `timeout` *[UpstreamTimeout](#upstreamtimeout)*                                   | Timeout specifies upstream timeout settings.                                                                                                                                                  |
| `match` *[ApisixRouteHTTPMatch](#apisixroutehttpmatch)*                           | Match defines the HTTP request matching criteria.                                                                                                                                             |
| `backends` *[ApisixRouteHTTPBackend](#apisixroutehttpbackend) array*              | Backends lists potential backend services to proxy requests to. If more than one backend is specified, the `traffic-split` plugin is used to distribute traffic according to backend weights. |
| `upstreams` *[ApisixRouteUpstreamReference](#apisixrouteupstreamreference) array* | Upstreams references ApisixUpstream CRDs.                                                                                                                                                     |
| `websocket` *boolean*                                                             | Websocket enables or disables websocket support for this route.                                                                                                                               |
| `plugin_config_name` *string*                                                     | PluginConfigName specifies the name of the plugin config to apply.                                                                                                                            |
| `plugin_config_namespace` *string*                                                | PluginConfigNamespace specifies the namespace of the plugin config. Defaults to the namespace of the ApisixRoute if not set.                                                                  |
| `plugins` *[ApisixRoutePlugin](#apisixrouteplugin) array*                         | Plugins lists additional plugins applied to this route.                                                                                                                                       |
| `authentication` *[ApisixRouteAuthentication](#apisixrouteauthentication)*        | Authentication holds authentication-related configuration for this route.                                                                                                                     |

*Appears in:*

* [ApisixRouteSpec](#apisixroutespec)

#### ApisixRouteHTTPBackend[â](#apisixroutehttpbackend "Direct link to ApisixRouteHTTPBackend")

ApisixRouteHTTPBackend represents an HTTP backend (Kubernetes Service).

| Field                                                                                                                       | Description                                                                                                                                                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `serviceName` *string*                                                                                                      | ServiceName is the name of the Kubernetes Service. Cross-namespace references are not supportedâensure the ApisixRoute and the Service are in the same namespace.                                                                                              |
| `servicePort` *[IntOrString](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#intorstring-intstr-util)* | ServicePort is the port of the Kubernetes Service. This can be either the port name or port number.                                                                                                                                                            |
| `resolveGranularity` *string*                                                                                               | ResolveGranularity determines how the backend service is resolved. Valid values are `endpoints` and `service`. When set to `endpoints`, individual pod IPs will be used; otherwise, the Service's ClusterIP or ExternalIP is used. The default is `endpoints`. |
| `weight` *integer*                                                                                                          | Weight specifies the relative traffic weight for this backend.                                                                                                                                                                                                 |
| `subset` *string*                                                                                                           | Subset specifies a named subset of the target Service. The subset must be pre-defined in the corresponding ApisixUpstream resource.                                                                                                                            |

*Appears in:*

* [ApisixRouteHTTP](#apisixroutehttp)

#### ApisixRouteHTTPMatch[â](#apisixroutehttpmatch "Direct link to ApisixRouteHTTPMatch")

ApisixRouteHTTPMatch defines the conditions used to match incoming HTTP requests.

| Field                                                             | Description                                                                                                                                                                                            |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `paths` *string array*                                            | Paths is a list of URI path patterns to match. At least one path must be specified. Supports exact matches and prefix matches. For prefix matches, append `*` to the path, such as `/foo*`.            |
| `methods` *string array*                                          | Methods specifies the HTTP methods to match.                                                                                                                                                           |
| `hosts` *string array*                                            | Hosts specifies Host header values to match. Supports exact and wildcard domains. Only one level of wildcard is allowed (e.g., `*.example.com` is valid, but `*.*.example.com` is not).                |
| `remoteAddrs` *string array*                                      | RemoteAddrs is a list of source IP addresses or CIDR ranges to match. Supports both IPv4 and IPv6 formats.                                                                                             |
| `exprs` *[ApisixRouteHTTPMatchExprs](#apisixroutehttpmatchexprs)* | NginxVars defines match conditions based on Nginx variables.                                                                                                                                           |
| `filter_func` *string*                                            | FilterFunc is a user-defined function for advanced request filtering. The function can use Nginx variables through the `vars` parameter. This field is supported in APISIX but not in API7 Enterprise. |

*Appears in:*

* [ApisixRouteHTTP](#apisixroutehttp)

#### ApisixRouteHTTPMatchExpr[â](#apisixroutehttpmatchexpr "Direct link to ApisixRouteHTTPMatchExpr")

ApisixRouteHTTPMatchExpr represents a binary expression used to match requests based on Nginx variables.

| Field                                                                           | Description                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `subject` *[ApisixRouteHTTPMatchExprSubject](#apisixroutehttpmatchexprsubject)* | Subject defines the left-hand side of the expression. It can be any [built-in variable](https://docs.api7.ai/apisix/reference/built-in-variables.md) or string literal.                                                                                     |
| `op` *string*                                                                   | Op specifies the operator used in the expression. Can be `Equal`, `NotEqual`, `GreaterThan`, `GreaterThanEqual`, `LessThan`, `LessThanEqual`, `RegexMatch`, `RegexNotMatch`, `RegexMatchCaseInsensitive`, `RegexNotMatchCaseInsensitive`, `In`, or `NotIn`. |
| `set` *string array*                                                            | Set provides a list of acceptable values for the expression. This should be used when Op is `In` or `NotIn`.                                                                                                                                                |
| `value` *string*                                                                | Value defines a single value to compare against the subject. This should be used when Op is not `In` or `NotIn`. Set and Value are mutually exclusiveâonly one should be set at a time.                                                                     |

*Appears in:*

* [ApisixRouteHTTPMatchExprs](#apisixroutehttpmatchexprs)

#### ApisixRouteHTTPMatchExprSubject[â](#apisixroutehttpmatchexprsubject "Direct link to ApisixRouteHTTPMatchExprSubject")

ApisixRouteHTTPMatchExprSubject describes the subject of a route matching expression.

| Field            | Description                                                                                                            |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `scope` *string* | Scope specifies the subject scope and can be `Header`, `Query`, or `Path`. When Scope is `Path`, Name will be ignored. |
| `name` *string*  | Name is the name of the header or query parameter.                                                                     |

*Appears in:*

* [ApisixRouteHTTPMatchExpr](#apisixroutehttpmatchexpr)

#### ApisixRouteHTTPMatchExprs[â](#apisixroutehttpmatchexprs "Direct link to ApisixRouteHTTPMatchExprs")

*Base type:* [ApisixRouteHTTPMatchExpr](#apisixroutehttpmatchexpr)

| Field                                                                           | Description                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `subject` *[ApisixRouteHTTPMatchExprSubject](#apisixroutehttpmatchexprsubject)* | Subject defines the left-hand side of the expression. It can be any [built-in variable](https://docs.api7.ai/apisix/reference/built-in-variables.md) or string literal.                                                                                     |
| `op` *string*                                                                   | Op specifies the operator used in the expression. Can be `Equal`, `NotEqual`, `GreaterThan`, `GreaterThanEqual`, `LessThan`, `LessThanEqual`, `RegexMatch`, `RegexNotMatch`, `RegexMatchCaseInsensitive`, `RegexNotMatchCaseInsensitive`, `In`, or `NotIn`. |
| `set` *string array*                                                            | Set provides a list of acceptable values for the expression. This should be used when Op is `In` or `NotIn`.                                                                                                                                                |
| `value` *string*                                                                | Value defines a single value to compare against the subject. This should be used when Op is not `In` or `NotIn`. Set and Value are mutually exclusiveâonly one should be set at a time.                                                                     |

*Appears in:*

* [ApisixRouteHTTPMatch](#apisixroutehttpmatch)

#### ApisixRoutePlugin[â](#apisixrouteplugin "Direct link to ApisixRoutePlugin")

ApisixRoutePlugin represents an APISIX plugin.

| Field                                                                                                                | Description                                     |
| -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| `name` *string*                                                                                                      | The plugin name.                                |
| `enable` *boolean*                                                                                                   | Whether this plugin is in use, default is true. |
| `config` *[JSON](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#json-v1-apiextensions-k8s-io)* | Plugin configuration.                           |
| `secretRef` *string*                                                                                                 | Plugin configuration secretRef.                 |

*Appears in:*

* [ApisixGlobalRuleSpec](#apisixglobalrulespec)
* [ApisixPluginConfigSpec](#apisixpluginconfigspec)
* [ApisixRouteHTTP](#apisixroutehttp)
* [ApisixRouteStream](#apisixroutestream)

#### ApisixRouteSpec[â](#apisixroutespec "Direct link to ApisixRouteSpec")

ApisixRouteSpec is the spec definition for ApisixRoute. It defines routing rules for both HTTP and stream traffic.

| Field                                                    | Description                                                                                                                                     |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `ingressClassName` *string*                              | IngressClassName is the name of the IngressClass this route belongs to. It allows multiple controllers to watch and reconcile different routes. |
| `http` *[ApisixRouteHTTP](#apisixroutehttp) array*       | HTTP defines a list of HTTP route rules. Each rule specifies conditions to match HTTP requests and how to forward them.                         |
| `stream` *[ApisixRouteStream](#apisixroutestream) array* | Stream defines a list of stream route rules. Each rule specifies conditions to match TCP/UDP traffic and how to forward them.                   |

*Appears in:*

* [ApisixRoute](#apisixroute)

#### ApisixRouteStream[â](#apisixroutestream "Direct link to ApisixRouteStream")

ApisixRouteStream defines the configuration for a Layer 4 (TCP/UDP) route.

| Field                                                             | Description                                                                     |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `name` *string*                                                   | Name is a unique identifier for the route. This field must not be empty.        |
| `protocol` *string*                                               | Protocol specifies the L4 protocol to match. Can be `TCP` or `UDP`.             |
| `match` *[ApisixRouteStreamMatch](#apisixroutestreammatch)*       | Match defines the criteria used to match incoming TCP or UDP connections.       |
| `backend` *[ApisixRouteStreamBackend](#apisixroutestreambackend)* | Backend specifies the destination service to which traffic should be forwarded. |
| `plugins` *[ApisixRoutePlugin](#apisixrouteplugin) array*         | Plugins defines a list of plugins to apply to this route.                       |

*Appears in:*

* [ApisixRouteSpec](#apisixroutespec)

#### ApisixRouteStreamBackend[â](#apisixroutestreambackend "Direct link to ApisixRouteStreamBackend")

ApisixRouteStreamBackend represents the backend service for a TCP or UDP stream route.

| Field                                                                                                                       | Description                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `serviceName` *string*                                                                                                      | ServiceName is the name of the Kubernetes Service. Cross-namespace references are not supportedâensure the ApisixRoute and the Service are in the same namespace.                                                                                           |
| `servicePort` *[IntOrString](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#intorstring-intstr-util)* | ServicePort is the port of the Kubernetes Service. This can be either the port name or port number.                                                                                                                                                         |
| `resolveGranularity` *string*                                                                                               | ResolveGranularity determines how the backend service is resolved. Valid values are `endpoint` and `service`. When set to `endpoint`, individual pod IPs will be used; otherwise, the Service's ClusterIP or ExternalIP is used. The default is `endpoint`. |
| `subset` *string*                                                                                                           | Subset specifies a named subset of the target Service. The subset must be pre-defined in the corresponding ApisixUpstream resource.                                                                                                                         |

*Appears in:*

* [ApisixRouteStream](#apisixroutestream)

#### ApisixRouteStreamMatch[â](#apisixroutestreammatch "Direct link to ApisixRouteStreamMatch")

ApisixRouteStreamMatch represents the matching conditions for a stream route.

| Field                   | Description                                                                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ingressPort` *integer* | IngressPort is the port on which the APISIX Ingress proxy server listens. This must be a statically configured port, as APISIX does not support dynamic port binding. |
| `host` *string*         | Host is the destination host address used to match the incoming TCP/UDP traffic.                                                                                      |

*Appears in:*

* [ApisixRouteStream](#apisixroutestream)

#### ApisixRouteUpstreamReference[â](#apisixrouteupstreamreference "Direct link to ApisixRouteUpstreamReference")

ApisixRouteUpstreamReference references an ApisixUpstream CRD to be used as a backend. It can be used in traffic-splitting scenarios or to select a specific upstream configuration.

| Field              | Description                                      |
| ------------------ | ------------------------------------------------ |
| `name` *string*    | Name is the name of the ApisixUpstream resource. |
| `weight` *integer* | Weight is the weight assigned to this upstream.  |

*Appears in:*

* [ApisixRouteHTTP](#apisixroutehttp)

#### ApisixSecret[â](#apisixsecret "Direct link to ApisixSecret")

ApisixSecret describes a reference to a Kubernetes Secret, including its name and namespace. This is used to locate secrets such as certificates or credentials for plugins or TLS configuration.

| Field                | Description                                                        |
| -------------------- | ------------------------------------------------------------------ |
| `name` *string*      | Name is the name of the Kubernetes Secret.                         |
| `namespace` *string* | Namespace is the namespace where the Kubernetes Secret is located. |

*Appears in:*

* [ApisixMutualTlsClientConfig](#apisixmutualtlsclientconfig)
* [ApisixTlsSpec](#apisixtlsspec)
* [ApisixUpstreamConfig](#apisixupstreamconfig)
* [ApisixUpstreamSpec](#apisixupstreamspec)
* [PortLevelSettings](#portlevelsettings)

#### ApisixTlsSpec[â](#apisixtlsspec "Direct link to ApisixTlsSpec")

ApisixTlsSpec defines configurations for TLS and mutual TLS.

| Field                                                                  | Description                                                                                                                                                          |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ingressClassName` *string*                                            | IngressClassName specifies which IngressClass this resource is associated with. The APISIX controller only processes this resource if the class matches its own.     |
| `hosts` *[HostType](#hosttype) array*                                  | Hosts lists the SNI (Server Name Indication) hostnames that this TLS configuration applies to. Must contain at least one host.                                       |
| `secret` *[ApisixSecret](#apisixsecret)*                               | Secret refers to the Kubernetes TLS secret containing the certificate and private key. This secret must exist in the specified namespace and contain valid TLS data. |
| `client` *[ApisixMutualTlsClientConfig](#apisixmutualtlsclientconfig)* | Client defines mutual TLS (mTLS) settings, such as the CA certificate and verification depth.                                                                        |

*Appears in:*

* [ApisixTls](#apisixtls)

#### ApisixUpstreamConfig[â](#apisixupstreamconfig "Direct link to ApisixUpstreamConfig")

ApisixUpstreamConfig defines configuration for upstream services.

| Field                                                           | Description                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `loadbalancer` *[LoadBalancer](#loadbalancer)*                  | LoadBalancer specifies the load balancer configuration for Kubernetes Service.                                                                                                                                                                                                                                        |
| `scheme` *string*                                               | Scheme is the protocol used to communicate with the upstream. Default is `http`. Can be `http`, `https`, `grpc`, or `grpcs`.                                                                                                                                                                                          |
| `retries` *integer*                                             | Retries defines the number of retry attempts APISIX should make when a failure occurs. Failures include timeouts, network errors, or 5xx status codes.                                                                                                                                                                |
| `timeout` *[UpstreamTimeout](#upstreamtimeout)*                 | Timeout specifies the connection, send, and read timeouts for upstream requests.                                                                                                                                                                                                                                      |
| `healthCheck` *[HealthCheck](#healthcheck)*                     | HealthCheck defines the active and passive health check configuration for the upstream.                                                                                                                                                                                                                               |
| `tlsSecret` *[ApisixSecret](#apisixsecret)*                     | TLSSecret references a Kubernetes Secret that contains the client certificate and key for mutual TLS when connecting to the upstream.                                                                                                                                                                                 |
| `subsets` *[ApisixUpstreamSubset](#apisixupstreamsubset) array* | Subsets defines labeled subsets of service endpoints, typically used for service versioning or canary deployments.                                                                                                                                                                                                    |
| `passHost` *string*                                             | PassHost configures how the host header should be determined when a request is forwarded to the upstream. Default is `pass`. Can be `pass`, `node` or `rewrite`:<br />â¢ `pass`: preserve the original Host header<br />â¢ `node`: use the upstream nodeâs host<br />â¢ `rewrite`: set to a custom host via upstreamHost |
| `upstreamHost` *string*                                         | UpstreamHost sets a custom Host header when passHost is set to `rewrite`.                                                                                                                                                                                                                                             |
| `discovery` *[Discovery](#discovery)*                           | Discovery configures service discovery for the upstream.                                                                                                                                                                                                                                                              |

*Appears in:*

* [ApisixUpstreamSpec](#apisixupstreamspec)
* [PortLevelSettings](#portlevelsettings)

#### ApisixUpstreamExternalNode[â](#apisixupstreamexternalnode "Direct link to ApisixUpstreamExternalNode")

ApisixUpstreamExternalNode defines configuration for an external upstream node. This allows referencing services outside the cluster.

| Field                                                              | Description                                                                                                           |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| `name` *string*                                                    | Name is the hostname or IP address of the external node.                                                              |
| `type` *[ApisixUpstreamExternalType](#apisixupstreamexternaltype)* | Type indicates the kind of external node. Can be `Domain`, or `Service`.                                              |
| `weight` *integer*                                                 | Weight defines the load balancing weight of this node. Higher values increase the share of traffic sent to this node. |
| `port` *integer*                                                   | Port specifies the port number on which the external node is accepting traffic.                                       |

*Appears in:*

* [ApisixUpstreamSpec](#apisixupstreamspec)

#### ApisixUpstreamExternalType[â](#apisixupstreamexternaltype "Direct link to ApisixUpstreamExternalType")

*Base type:* `string`

ApisixUpstreamExternalType is the external service type

*Appears in:*

* [ApisixUpstreamExternalNode](#apisixupstreamexternalnode)

#### ApisixUpstreamSpec[â](#apisixupstreamspec "Direct link to ApisixUpstreamSpec")

ApisixUpstreamSpec describes the desired configuration of an ApisixUpstream resource. It defines how traffic should be routed to backend services, including upstream node definitions and custom configuration.

| Field                                                                             | Description                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ingressClassName` *string*                                                       | IngressClassName is the name of an IngressClass cluster resource. Controller implementations use this field to determine whether they should process this ApisixUpstream resource.                                                                                                                                    |
| `externalNodes` *[ApisixUpstreamExternalNode](#apisixupstreamexternalnode) array* | ExternalNodes defines a static list of backend nodes. These can be external hosts outside the cluster or cluster-internal Services specified by their DNS name. When this field is set, the upstream will route traffic directly to these nodes without DNS resolution or service discovery.                          |
| `loadbalancer` *[LoadBalancer](#loadbalancer)*                                    | LoadBalancer specifies the load balancer configuration for Kubernetes Service.                                                                                                                                                                                                                                        |
| `scheme` *string*                                                                 | Scheme is the protocol used to communicate with the upstream. Default is `http`. Can be `http`, `https`, `grpc`, or `grpcs`.                                                                                                                                                                                          |
| `retries` *integer*                                                               | Retries defines the number of retry attempts APISIX should make when a failure occurs. Failures include timeouts, network errors, or 5xx status codes.                                                                                                                                                                |
| `timeout` *[UpstreamTimeout](#upstreamtimeout)*                                   | Timeout specifies the connection, send, and read timeouts for upstream requests.                                                                                                                                                                                                                                      |
| `healthCheck` *[HealthCheck](#healthcheck)*                                       | HealthCheck defines the active and passive health check configuration for the upstream.                                                                                                                                                                                                                               |
| `tlsSecret` *[ApisixSecret](#apisixsecret)*                                       | TLSSecret references a Kubernetes Secret that contains the client certificate and key for mutual TLS when connecting to the upstream.                                                                                                                                                                                 |
| `subsets` *[ApisixUpstreamSubset](#apisixupstreamsubset) array*                   | Subsets defines labeled subsets of service endpoints, typically used for service versioning or canary deployments.                                                                                                                                                                                                    |
| `passHost` *string*                                                               | PassHost configures how the host header should be determined when a request is forwarded to the upstream. Default is `pass`. Can be `pass`, `node` or `rewrite`:<br />â¢ `pass`: preserve the original Host header<br />â¢ `node`: use the upstream nodeâs host<br />â¢ `rewrite`: set to a custom host via upstreamHost |
| `upstreamHost` *string*                                                           | UpstreamHost sets a custom Host header when passHost is set to `rewrite`.                                                                                                                                                                                                                                             |
| `discovery` *[Discovery](#discovery)*                                             | Discovery configures service discovery for the upstream.                                                                                                                                                                                                                                                              |
| `portLevelSettings` *[PortLevelSettings](#portlevelsettings) array*               | PortLevelSettings allows fine-grained upstream configuration for specific ports, useful when a backend service exposes multiple ports with different behaviors or protocols.                                                                                                                                          |

*Appears in:*

* [ApisixUpstream](#apisixupstream)

#### ApisixUpstreamSubset[â](#apisixupstreamsubset "Direct link to ApisixUpstreamSubset")

ApisixUpstreamSubset defines a single endpoints group of one Service.

| Field                                                                          | Description                             |
| ------------------------------------------------------------------------------ | --------------------------------------- |
| `name` *string*                                                                | Name is the name of subset.             |
| `labels` *object (keys<!-- -->:string<!-- -->, values<!-- -->:string<!-- -->)* | Labels is the label set of this subset. |

*Appears in:*

* [ApisixUpstreamConfig](#apisixupstreamconfig)
* [ApisixUpstreamSpec](#apisixupstreamspec)
* [PortLevelSettings](#portlevelsettings)

#### Discovery[â](#discovery "Direct link to Discovery")

Discovery defines the service discovery configuration for dynamically resolving upstream nodes. This is used when APISIX integrates with a service registry such as Nacos, Consul, or Eureka.

| Field                                                                        | Description                                                                                                                |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `serviceName` *string*                                                       | ServiceName is the name of the service to discover.                                                                        |
| `type` *string*                                                              | Type is the name of the service discovery provider.                                                                        |
| `args` *object (keys<!-- -->:string<!-- -->, values<!-- -->:string<!-- -->)* | Args contains additional configuration parameters required by the discovery provider. These are passed as key-value pairs. |

*Appears in:*

* [ApisixUpstreamConfig](#apisixupstreamconfig)
* [ApisixUpstreamSpec](#apisixupstreamspec)
* [PortLevelSettings](#portlevelsettings)

#### HealthCheck[â](#healthcheck "Direct link to HealthCheck")

HealthCheck defines the health check configuration for upstream nodes. It includes active checks (proactively probing the nodes) and optional passive checks (monitoring based on traffic).

| Field                                                 | Description                                                                                           |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `active` *[ActiveHealthCheck](#activehealthcheck)*    | Active health checks proactively send requests to upstream nodes to determine their availability.     |
| `passive` *[PassiveHealthCheck](#passivehealthcheck)* | Passive health checks evaluate upstream health based on observed traffic, such as timeouts or errors. |

*Appears in:*

* [ApisixUpstreamConfig](#apisixupstreamconfig)
* [ApisixUpstreamSpec](#apisixupstreamspec)
* [PortLevelSettings](#portlevelsettings)

#### HostType[â](#hosttype "Direct link to HostType")

*Base type:* `string`

*Appears in:*

* [ApisixTlsSpec](#apisixtlsspec)

#### LoadBalancer[â](#loadbalancer-1 "Direct link to LoadBalancer")

LoadBalancer defines the load balancing strategy for distributing traffic across upstream nodes.

| Field             | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type` *string*   | Type specifies the load balancing algorithms to route traffic to the backend. Default is `roundrobin`. Can be `roundrobin`, `chash`, `ewma`, or `least_conn`.                                                                                                                                                                                                                                                         |
| `hashOn` *string* | HashOn specified the type of field used for hashing, required when type is `chash`. Default is `vars`. Can be `vars`, `header`, `cookie`, `consumer`, or `vars_combinations`.                                                                                                                                                                                                                                         |
| `key` *string*    | Key is used with HashOn, generally required when type is `chash`. When HashOn is `header` or `cookie`, specifies the name of the header or cookie. When HashOn is `consumer`, key is not required, as the consumer name is used automatically. When HashOn is `vars` or `vars_combinations`, key refers to one or a combination of [built-in variables](https://docs.api7.ai/apisix/reference/built-in-variables.md). |

*Appears in:*

* [ApisixUpstreamConfig](#apisixupstreamconfig)
* [ApisixUpstreamSpec](#apisixupstreamspec)
* [PortLevelSettings](#portlevelsettings)

#### PassiveHealthCheck[â](#passivehealthcheck "Direct link to PassiveHealthCheck")

PassiveHealthCheck defines the conditions used to determine whether an upstream node is healthy or unhealthy based on passive observations. Passive health checks rely on real traffic responses instead of active probes.

| Field                                                                     | Description                                                                            |
| ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `type` *string*                                                           | Type specifies the type of passive health check. Can be `http`, `https`, or `tcp`.     |
| `healthy` *[PassiveHealthCheckHealthy](#passivehealthcheckhealthy)*       | Healthy defines the conditions under which an upstream node is considered healthy.     |
| `unhealthy` *[PassiveHealthCheckUnhealthy](#passivehealthcheckunhealthy)* | Unhealthy defines the conditions under which an upstream node is considered unhealthy. |

*Appears in:*

* [HealthCheck](#healthcheck)

#### PassiveHealthCheckHealthy[â](#passivehealthcheckhealthy "Direct link to PassiveHealthCheckHealthy")

PassiveHealthCheckHealthy defines the conditions used to passively determine whether an upstream node is healthy.

| Field                       | Description                                                                  |
| --------------------------- | ---------------------------------------------------------------------------- |
| `httpCodes` *integer array* | HTTPCodes define a list of HTTP status codes that are considered healthy.    |
| `successes` *integer*       | Successes define the number of successful probes to define a healthy target. |

*Appears in:*

* [ActiveHealthCheckHealthy](#activehealthcheckhealthy)
* [PassiveHealthCheck](#passivehealthcheck)

#### PassiveHealthCheckUnhealthy[â](#passivehealthcheckunhealthy "Direct link to PassiveHealthCheckUnhealthy")

UpstreamPassiveHealthCheckUnhealthy defines the conditions used to passively determine whether an upstream node is unhealthy.

| Field                       | Description                                                                    |
| --------------------------- | ------------------------------------------------------------------------------ |
| `httpCodes` *integer array* | HTTPCodes define a list of HTTP status codes that are considered unhealthy.    |
| `httpFailures` *integer*    | HTTPFailures define the number of HTTP failures to define an unhealthy target. |
| `tcpFailures` *integer*     | TCPFailures define the number of TCP failures to define an unhealthy target.   |
| `timeout` *integer*         | Timeout sets the number of timeouts to define an unhealthy target.             |

*Appears in:*

* [ActiveHealthCheckUnhealthy](#activehealthcheckunhealthy)
* [PassiveHealthCheck](#passivehealthcheck)

#### PortLevelSettings[â](#portlevelsettings "Direct link to PortLevelSettings")

PortLevelSettings configures the ApisixUpstreamConfig for each individual port. It inherits configuration from the outer level (the whole Kubernetes Service) and overrides some of them if they are set on the port level.

| Field                                                           | Description                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `loadbalancer` *[LoadBalancer](#loadbalancer)*                  | LoadBalancer specifies the load balancer configuration for Kubernetes Service.                                                                                                                                                                                                                                        |
| `scheme` *string*                                               | Scheme is the protocol used to communicate with the upstream. Default is `http`. Can be `http`, `https`, `grpc`, or `grpcs`.                                                                                                                                                                                          |
| `retries` *integer*                                             | Retries defines the number of retry attempts APISIX should make when a failure occurs. Failures include timeouts, network errors, or 5xx status codes.                                                                                                                                                                |
| `timeout` *[UpstreamTimeout](#upstreamtimeout)*                 | Timeout specifies the connection, send, and read timeouts for upstream requests.                                                                                                                                                                                                                                      |
| `healthCheck` *[HealthCheck](#healthcheck)*                     | HealthCheck defines the active and passive health check configuration for the upstream.                                                                                                                                                                                                                               |
| `tlsSecret` *[ApisixSecret](#apisixsecret)*                     | TLSSecret references a Kubernetes Secret that contains the client certificate and key for mutual TLS when connecting to the upstream.                                                                                                                                                                                 |
| `subsets` *[ApisixUpstreamSubset](#apisixupstreamsubset) array* | Subsets defines labeled subsets of service endpoints, typically used for service versioning or canary deployments.                                                                                                                                                                                                    |
| `passHost` *string*                                             | PassHost configures how the host header should be determined when a request is forwarded to the upstream. Default is `pass`. Can be `pass`, `node` or `rewrite`:<br />â¢ `pass`: preserve the original Host header<br />â¢ `node`: use the upstream nodeâs host<br />â¢ `rewrite`: set to a custom host via upstreamHost |
| `upstreamHost` *string*                                         | UpstreamHost sets a custom Host header when passHost is set to `rewrite`.                                                                                                                                                                                                                                             |
| `discovery` *[Discovery](#discovery)*                           | Discovery configures service discovery for the upstream.                                                                                                                                                                                                                                                              |
| `port` *integer*                                                | Port is a Kubernetes Service port.                                                                                                                                                                                                                                                                                    |

*Appears in:*

* [ApisixUpstreamSpec](#apisixupstreamspec)

#### UpstreamTimeout[â](#upstreamtimeout "Direct link to UpstreamTimeout")

UpstreamTimeout defines timeout settings for connecting, sending, and reading from the upstream.

| Field                                                                                                         | Description                                                    |
| ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| `connect` *[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#duration-v1-meta)* | Connect timeout for establishing a connection to the upstream. |
| `send` *[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#duration-v1-meta)*    | Send timeout for sending data to the upstream.                 |
| `read` *[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#duration-v1-meta)*    | Read timeout for reading data from the upstream.               |

*Appears in:*

* [ApisixRouteHTTP](#apisixroutehttp)
* [ApisixUpstreamConfig](#apisixupstreamconfig)
* [ApisixUpstreamSpec](#apisixupstreamspec)
* [PortLevelSettings](#portlevelsettings)
