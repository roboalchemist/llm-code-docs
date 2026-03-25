# Source: https://projectcontour.io/docs/1.33/config/api/

Title: Documentation

URL Source: https://projectcontour.io/docs/1.33/config/api/

Markdown Content:
Contour API Reference
---------------------

Packages:

* [projectcontour.io/v1](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io%2fv1)
* [projectcontour.io/v1alpha1](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io%2fv1alpha1)

projectcontour.io/v1
--------------------

Package v1 holds the specification for the projectcontour.io Custom Resource Definitions (CRDs).

In building this CRD, we’ve inadvertently overloaded the word “Condition”, so we’ve tried to make this spec clear as to which types of condition are which.

`MatchConditions` are used by `Routes` and `Includes` to specify rules to match requests against for either routing or inclusion.

`DetailedConditions` are used in the `Status` of these objects to hold information about the relevant state of the object and the world around it.

`SubConditions` are used underneath `DetailedConditions` to give more detail to errors or warnings.

Resource Types:

* [HTTPProxy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HTTPProxy)
* [TLSCertificateDelegation](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TLSCertificateDelegation)

### HTTPProxy

HTTPProxy is an Ingress CRD specification.

| Field | Description |
| --- | --- |
| `apiVersion` string | `projectcontour.io/v1` |
| `kind` string | `HTTPProxy` |
| `metadata` _[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec` _[HTTPProxySpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HTTPProxySpec)_ | `virtualhost` _[VirtualHost](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.VirtualHost)_ _(Optional)_ Virtualhost appears at most once. If it is present, the object is considered to be a “root” HTTPProxy. `routes` _[[]Route](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Route)_ _(Optional)_ Routes are the ingress routes. If TCPProxy is present, Routes is ignored. `tcpproxy` _[TCPProxy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TCPProxy)_ _(Optional)_ TCPProxy holds TCP proxy information. `includes` _[[]Include](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Include)_ _(Optional)_ Includes allow for specific routing configuration to be included from another HTTPProxy, possibly in another namespace. `ingressClassName` _string_ _(Optional)_ IngressClassName optionally specifies the ingress class to use for this HTTPProxy. This replaces the deprecated `kubernetes.io/ingress.class` annotation. For backwards compatibility, when that annotation is set, it is given precedence over this field. |
| `status` _[HTTPProxyStatus](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HTTPProxyStatus)_ | _(Optional)_ Status is a container for computed information about the HTTPProxy. |

### TLSCertificateDelegation

TLSCertificateDelegation is an TLS Certificate Delegation CRD specification. See design/tls-certificate-delegation.md for details.

| Field | Description |
| --- | --- |
| `apiVersion` string | `projectcontour.io/v1` |
| `kind` string | `TLSCertificateDelegation` |
| `metadata` _[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec` _[TLSCertificateDelegationSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TLSCertificateDelegationSpec)_ | `delegations` _[[]CertificateDelegation](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.CertificateDelegation)_ |
| `status` _[TLSCertificateDelegationStatus](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TLSCertificateDelegationStatus)_ | _(Optional)_ |

(_Appears on:_[AuthorizationServer](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.AuthorizationServer), [Route](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Route))

AuthorizationPolicy modifies how client requests are authenticated.

| Field | Description |
| --- | --- |
| `disabled` _bool_ | _(Optional)_ When true, this field disables client request authentication for the scope of the policy. |
| `context` _map[string]string_ | _(Optional)_ Context is a set of key/value pairs that are sent to the authentication server in the check request. If a context is provided at an enclosing scope, the entries are merged such that the inner scope overrides matching keys from the outer scope. |

### AuthorizationServer

(_Appears on:_[VirtualHost](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.VirtualHost), [ContourConfigurationSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfigurationSpec))

AuthorizationServer configures an external server to authenticate client requests. The external server must implement the v3 Envoy external authorization GRPC protocol ([https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/auth/v3/external_auth.proto](https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/auth/v3/external_auth.proto)).

| Field | Description |
| --- | --- |
| `extensionRef` _[ExtensionServiceReference](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.ExtensionServiceReference)_ | _(Optional)_ ExtensionServiceRef specifies the extension resource that will authorize client requests. |
| `authPolicy` _[AuthorizationPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.AuthorizationPolicy)_ | _(Optional)_ AuthPolicy sets a default authorization policy for client requests. This policy will be used unless overridden by individual routes. |
| `responseTimeout` _string_ | _(Optional)_ ResponseTimeout configures maximum time to wait for a check response from the authorization server. Timeout durations are expressed in the Go [Duration format](https://godoc.org/time#ParseDuration). Valid time units are “ns”, “us” (or “µs”), “ms”, “s”, “m”, “h”. The string “infinity” is also a valid input and specifies no timeout. |
| `failOpen` _bool_ | _(Optional)_ If FailOpen is true, the client request is forwarded to the upstream service even if the authorization server fails to respond. This field should not be set in most cases. It is intended for use only while migrating applications from internal authorization to Contour external authorization. |
| `withRequestBody` _[AuthorizationServerBufferSettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.AuthorizationServerBufferSettings)_ | _(Optional)_ WithRequestBody specifies configuration for sending the client request’s body to authorization server. |

### AuthorizationServerBufferSettings

(_Appears on:_[AuthorizationServer](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.AuthorizationServer))

AuthorizationServerBufferSettings enables ExtAuthz filter to buffer client request data and send it as part of authorization request

| Field | Description |
| --- | --- |
| `maxRequestBytes` _uint32_ | _(Optional)_ MaxRequestBytes sets the maximum size of message body ExtAuthz filter will hold in-memory. |
| `allowPartialMessage` _bool_ | _(Optional)_ If AllowPartialMessage is true, then Envoy will buffer the body until MaxRequestBytes are reached. |
| `packAsBytes` _bool_ | _(Optional)_ If PackAsBytes is true, the body sent to Authorization Server is in raw bytes. |

(_Appears on:_[CORSPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.CORSPolicy))

CORSHeaderValue specifies the value of the string headers returned by a cross-domain request.

### CORSPolicy

(_Appears on:_[VirtualHost](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.VirtualHost))

CORSPolicy allows setting the CORS policy

| Field | Description |
| --- | --- |
| `allowCredentials` _bool_ | _(Optional)_ Specifies whether the resource allows credentials. |
| `allowOrigin` _[]string_ | AllowOrigin specifies the origins that will be allowed to do CORS requests. Allowed values include “*” which signifies any origin is allowed, an exact origin of the form “scheme://host[:port]” (where port is optional), or a valid regex pattern. Note that regex patterns are validated and a simple “glob” pattern (e.g.*.foo.com) will be rejected or produce unexpected matches when applied as a regex. |
| `allowMethods` _[[]CORSHeaderValue](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.CORSHeaderValue)_ | AllowMethods specifies the content for the _access-control-allow-methods_ header. |
| `allowHeaders` _[[]CORSHeaderValue](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.CORSHeaderValue)_ | _(Optional)_ AllowHeaders specifies the content for the _access-control-allow-headers_ header. |
| `exposeHeaders` _[[]CORSHeaderValue](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.CORSHeaderValue)_ | _(Optional)_ ExposeHeaders Specifies the content for the _access-control-expose-headers_ header. |
| `maxAge` _string_ | _(Optional)_ MaxAge indicates for how long the results of a preflight request can be cached. MaxAge durations are expressed in the Go [Duration format](https://godoc.org/time#ParseDuration). Valid time units are “ns”, “us” (or “µs”), “ms”, “s”, “m”, “h”. Only positive values are allowed while 0 disables the cache requiring a preflight OPTIONS check for all cross-origin requests. |
| `allowPrivateNetwork` _bool_ | AllowPrivateNetwork specifies whether to allow private network requests. See [https://developer.chrome.com/blog/private-network-access-preflight](https://developer.chrome.com/blog/private-network-access-preflight). |

### CertificateDelegation

(_Appears on:_[TLSCertificateDelegationSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TLSCertificateDelegationSpec))

CertificateDelegation maps the authority to reference a secret in the current namespace to a set of namespaces.

| Field | Description |
| --- | --- |
| `secretName` _string_ | required, the name of a secret in the current namespace. |
| `targetNamespaces` _[]string_ | required, the namespaces the authority to reference the secret will be delegated to. If TargetNamespaces is nil or empty, the CertificateDelegation’ is ignored. If the TargetNamespace list contains the character, “*” the secret will be delegated to all namespaces. |

### ClientCertificateDetails

(_Appears on:_[DownstreamValidation](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.DownstreamValidation))

ClientCertificateDetails defines which parts of the client certificate will be forwarded.

| Field | Description |
| --- | --- |
| `subject` _bool_ | _(Optional)_ Subject of the client cert. |
| `cert` _bool_ | _(Optional)_ Client cert in URL encoded PEM format. |
| `chain` _bool_ | _(Optional)_ Client cert chain (including the leaf cert) in URL encoded PEM format. |
| `dns` _bool_ | _(Optional)_ DNS type Subject Alternative Names of the client cert. |
| `uri` _bool_ | _(Optional)_ URI type Subject Alternative Name of the client cert. |

### CookieDomainRewrite

(_Appears on:_[CookieRewritePolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.CookieRewritePolicy))

| Field | Description |
| --- | --- |
| `value` _string_ | Value is the value to rewrite the Domain attribute to. For now this is required. |

### CookiePathRewrite

(_Appears on:_[CookieRewritePolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.CookieRewritePolicy))

| Field | Description |
| --- | --- |
| `value` _string_ | Value is the value to rewrite the Path attribute to. For now this is required. |

### CookieRewritePolicy

(_Appears on:_[Route](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Route), [Service](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Service))

| Field | Description |
| --- | --- |
| `name` _string_ | Name is the name of the cookie for which attributes will be rewritten. |
| `pathRewrite` _[CookiePathRewrite](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.CookiePathRewrite)_ | _(Optional)_ PathRewrite enables rewriting the Set-Cookie Path element. If not set, Path will not be rewritten. |
| `domainRewrite` _[CookieDomainRewrite](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.CookieDomainRewrite)_ | _(Optional)_ DomainRewrite enables rewriting the Set-Cookie Domain element. If not set, Domain will not be rewritten. |
| `secure` _bool_ | _(Optional)_ Secure enables rewriting the Set-Cookie Secure element. If not set, Secure attribute will not be rewritten. |
| `sameSite` _string_ | _(Optional)_ SameSite enables rewriting the Set-Cookie SameSite element. If not set, SameSite attribute will not be rewritten. |

### DetailedCondition

(_Appears on:_[HTTPProxyStatus](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HTTPProxyStatus), [TLSCertificateDelegationStatus](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TLSCertificateDelegationStatus), [ContourConfigurationStatus](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfigurationStatus), [ExtensionServiceStatus](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ExtensionServiceStatus))

DetailedCondition is an extension of the normal Kubernetes conditions, with two extra fields to hold sub-conditions, which provide more detailed reasons for the state (True or False) of the condition.

`errors` holds information about sub-conditions which are fatal to that condition and render its state False.

`warnings` holds information about sub-conditions which are not fatal to that condition and do not force the state to be False.

Remember that Conditions have a type, a status, and a reason.

The type is the type of the condition, the most important one in this CRD set is `Valid`. `Valid` is a positive-polarity condition: when it is `status: true` there are no problems.

In more detail, `status: true` means that the object is has been ingested into Contour with no errors. `warnings` may still be present, and will be indicated in the Reason field. There must be zero entries in the `errors` slice in this case.

`Valid`, `status: false` means that the object has had one or more fatal errors during processing into Contour. The details of the errors will be present under the `errors` field. There must be at least one error in the `errors` slice if `status` is `false`.

For DetailedConditions of types other than `Valid`, the Condition must be in the negative polarity. When they have `status``true`, there is an error. There must be at least one entry in the `errors` Subcondition slice. When they have `status``false`, there are no serious errors, and there must be zero entries in the `errors` slice. In either case, there may be entries in the `warnings` slice.

Regardless of the polarity, the `reason` and `message` fields must be updated with either the detail of the reason (if there is one and only one entry in total across both the `errors` and `warnings` slices), or `MultipleReasons` if there is more than one entry.

| Field | Description |
| --- | --- |
| `Condition` _[Kubernetes meta/v1.Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta)_ | (Members of `Condition` are embedded into this type.) |
| `errors` _[[]SubCondition](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.SubCondition)_ | _(Optional)_ Errors contains a slice of relevant error subconditions for this object. Subconditions are expected to appear when relevant (when there is a error), and disappear when not relevant. An empty slice here indicates no errors. |
| `warnings` _[[]SubCondition](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.SubCondition)_ | _(Optional)_ Warnings contains a slice of relevant warning subconditions for this object. Subconditions are expected to appear when relevant (when there is a warning), and disappear when not relevant. An empty slice here indicates no warnings. |

### DownstreamValidation

(_Appears on:_[TLS](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TLS))

DownstreamValidation defines how to verify the client certificate.

| Field | Description |
| --- | --- |
| `caSecret` _string_ | _(Optional)_ Name of a Kubernetes secret that contains a CA certificate bundle. The secret must contain key named ca.crt. The client certificate must validate against the certificates in the bundle. If specified and SkipClientCertValidation is true, client certificates will be required on requests. The name can be optionally prefixed with namespace “namespace/name”. When cross-namespace reference is used, TLSCertificateDelegation resource must exist in the namespace to grant access to the secret. |
| `skipClientCertValidation` _bool_ | _(Optional)_ SkipClientCertValidation disables downstream client certificate validation. Defaults to false. This field is intended to be used in conjunction with external authorization in order to enable the external authorization server to validate client certificates. When this field is set to true, client certificates are requested but not verified by Envoy. If CACertificate is specified, client certificates are required on requests, but not verified. If external authorization is in use, they are presented to the external authorization server. |
| `forwardClientCertificate` _[ClientCertificateDetails](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.ClientCertificateDetails)_ | _(Optional)_ ForwardClientCertificate adds the selected data from the passed client TLS certificate to the x-forwarded-client-cert header. |
| `crlSecret` _string_ | _(Optional)_ Name of a Kubernetes opaque secret that contains a concatenated list of PEM encoded CRLs. The secret must contain key named crl.pem. This field will be used to verify that a client certificate has not been revoked. CRLs must be available from all CAs, unless crlOnlyVerifyLeafCert is true. Large CRL lists are not supported since individual secrets are limited to 1MiB in size. The name can be optionally prefixed with namespace “namespace/name”. When cross-namespace reference is used, TLSCertificateDelegation resource must exist in the namespace to grant access to the secret. |
| `crlOnlyVerifyLeafCert` _bool_ | _(Optional)_ If this option is set to true, only the certificate at the end of the certificate chain will be subject to validation by CRL. |
| `optionalClientCertificate` _bool_ | _(Optional)_ OptionalClientCertificate when set to true will request a client certificate but allow the connection to continue if the client does not provide one. If a client certificate is sent, it will be verified according to the other properties, which includes disabling validation if SkipClientCertValidation is set. Defaults to false. |

### ExtensionServiceReference

(_Appears on:_[AuthorizationServer](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.AuthorizationServer))

ExtensionServiceReference names an ExtensionService resource.

| Field | Description |
| --- | --- |
| `apiVersion` _string_ | _(Optional)_ API version of the referent. If this field is not specified, the default “projectcontour.io/v1alpha1” will be used |
| `namespace` _string_ | _(Optional)_ Namespace of the referent. If this field is not specifies, the namespace of the resource that targets the referent will be used. More info: [https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) |
| `name` _string_ | Name of the referent. More info: [https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names) |

### Feature (`string` alias)

(_Appears on:_[ContourSettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourSettings))

### GenericKeyDescriptor

(_Appears on:_[RateLimitDescriptorEntry](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RateLimitDescriptorEntry))

GenericKeyDescriptor defines a descriptor entry with a static key and value.

| Field | Description |
| --- | --- |
| `key` _string_ | _(Optional)_ Key defines the key of the descriptor entry. If not set, the key is set to “generic_key”. |
| `value` _string_ | Value defines the value of the descriptor entry. |

### GlobalRateLimitPolicy

(_Appears on:_[RateLimitPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RateLimitPolicy), [RateLimitServiceConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.RateLimitServiceConfig))

GlobalRateLimitPolicy defines global rate limiting parameters.

| Field | Description |
| --- | --- |
| `disabled` _bool_ | _(Optional)_ Disabled configures the HTTPProxy to not use the default global rate limit policy defined by the Contour configuration. |
| `descriptors` _[[]RateLimitDescriptor](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RateLimitDescriptor)_ | _(Optional)_ Descriptors defines the list of descriptors that will be generated and sent to the rate limit service. Each descriptor contains 1+ key-value pair entries. |

### HTTPDirectResponsePolicy

(_Appears on:_[Route](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Route))

| Field | Description |
| --- | --- |
| `statusCode` _int_ | StatusCode is the HTTP response status to be returned. |
| `body` _string_ | _(Optional)_ Body is the content of the response body. If this setting is omitted, no body is included in the generated response. Note: Body is not recommended to set too long otherwise it can have significant resource usage impacts. |

### HTTPHealthCheckPolicy

(_Appears on:_[Route](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Route))

HTTPHealthCheckPolicy defines health checks on the upstream service.

| Field | Description |
| --- | --- |
| `path` _string_ | HTTP endpoint used to perform health checks on upstream service |
| `host` _string_ | The value of the host header in the HTTP health check request. If left empty (default value), the name “contour-envoy-healthcheck” will be used. |
| `intervalSeconds` _int64_ | _(Optional)_ The interval (seconds) between health checks |
| `timeoutSeconds` _int64_ | _(Optional)_ The time to wait (seconds) for a health check response |
| `unhealthyThresholdCount` _int64_ | _(Optional)_ The number of unhealthy health checks required before a host is marked unhealthy |
| `healthyThresholdCount` _int64_ | _(Optional)_ The number of healthy health checks required before a host is marked healthy |
| `expectedStatuses` _[[]HTTPStatusRange](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HTTPStatusRange)_ | _(Optional)_ The ranges of HTTP response statuses considered healthy. Follow half-open semantics, i.e. for each range the start is inclusive and the end is exclusive. Must be within the range [100,600). If not specified, only a 200 response status is considered healthy. |

### HTTPInternalRedirectPolicy

(_Appears on:_[Route](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Route))

| Field | Description |
| --- | --- |
| `maxInternalRedirects` _uint32_ | _(Optional)_ MaxInternalRedirects An internal redirect is not handled, unless the number of previous internal redirects that a downstream request has encountered is lower than this value. |
| `redirectResponseCodes` _[[]RedirectResponseCode](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RedirectResponseCode)_ | _(Optional)_ RedirectResponseCodes If unspecified, only 302 will be treated as internal redirect. Only 301, 302, 303, 307 and 308 are valid values. |
| `allowCrossSchemeRedirect` _string_ | _(Optional)_ AllowCrossSchemeRedirect Allow internal redirect to follow a target URI with a different scheme than the value of x-forwarded-proto. SafeOnly allows same scheme redirect and safe cross scheme redirect, which means if the downstream scheme is HTTPS, both HTTPS and HTTP redirect targets are allowed, but if the downstream scheme is HTTP, only HTTP redirect targets are allowed. |
| `denyRepeatedRouteRedirect` _bool_ | _(Optional)_ If DenyRepeatedRouteRedirect is true, rejects redirect targets that are pointing to a route that has been followed by a previous redirect from the current route. |

### HTTPProxySpec

(_Appears on:_[HTTPProxy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HTTPProxy))

HTTPProxySpec defines the spec of the CRD.

| Field | Description |
| --- | --- |
| `virtualhost` _[VirtualHost](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.VirtualHost)_ | _(Optional)_ Virtualhost appears at most once. If it is present, the object is considered to be a “root” HTTPProxy. |
| `routes` _[[]Route](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Route)_ | _(Optional)_ Routes are the ingress routes. If TCPProxy is present, Routes is ignored. |
| `tcpproxy` _[TCPProxy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TCPProxy)_ | _(Optional)_ TCPProxy holds TCP proxy information. |
| `includes` _[[]Include](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Include)_ | _(Optional)_ Includes allow for specific routing configuration to be included from another HTTPProxy, possibly in another namespace. |
| `ingressClassName` _string_ | _(Optional)_ IngressClassName optionally specifies the ingress class to use for this HTTPProxy. This replaces the deprecated `kubernetes.io/ingress.class` annotation. For backwards compatibility, when that annotation is set, it is given precedence over this field. |

### HTTPProxyStatus

(_Appears on:_[HTTPProxy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HTTPProxy))

HTTPProxyStatus reports the current state of the HTTPProxy.

| Field | Description |
| --- | --- |
| `currentStatus` _string_ | _(Optional)_ |
| `description` _string_ | _(Optional)_ |
| `loadBalancer` _[Kubernetes core/v1.LoadBalancerStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#loadbalancerstatus-v1-core)_ | _(Optional)_ LoadBalancer contains the current status of the load balancer. |
| `conditions` _[[]DetailedCondition](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.DetailedCondition)_ | _(Optional)_ Conditions contains information about the current status of the HTTPProxy, in an upstream-friendly container. Contour will update a single condition, `Valid`, that is in normal-true polarity. That is, when `currentStatus` is `valid`, the `Valid` condition will be `status: true`, and vice versa. Contour will leave untouched any other Conditions set in this block, in case some other controller wants to add a Condition. If you are another controller owner and wish to add a condition, you _should_ namespace your condition with a label, like `controller.domain.com/ConditionName`. |

### HTTPRequestRedirectPolicy

(_Appears on:_[Route](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Route))

HTTPRequestRedirectPolicy defines configuration for redirecting a request.

| Field | Description |
| --- | --- |
| `scheme` _string_ | _(Optional)_ Scheme is the scheme to be used in the value of the `Location` header in the response. When empty, the scheme of the request is used. |
| `hostname` _string_ | _(Optional)_ Hostname is the precise hostname to be used in the value of the `Location` header in the response. When empty, the hostname of the request is used. No wildcards are allowed. |
| `port` _int32_ | _(Optional)_ Port is the port to be used in the value of the `Location` header in the response. When empty, port (if specified) of the request is used. |
| `statusCode` _[RedirectResponseCode](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RedirectResponseCode)_ | _(Optional)_ StatusCode is the HTTP status code to be used in response. |
| `path` _string_ | _(Optional)_ Path allows for redirection to a different path from the original on the request. The path must start with a leading slash. Note: Only one of Path or Prefix can be defined. |
| `prefix` _string_ | _(Optional)_ Prefix defines the value to swap the matched prefix or path with. The prefix must start with a leading slash. Note: Only one of Path or Prefix can be defined. |

### HTTPStatusRange

(_Appears on:_[HTTPHealthCheckPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HTTPHealthCheckPolicy))

| Field | Description |
| --- | --- |
| `start` _int64_ | The start (inclusive) of a range of HTTP status codes. |
| `end` _int64_ | The end (exclusive) of a range of HTTP status codes. |

(_Appears on:_[RequestHashPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RequestHashPolicy))

HeaderHashOptions contains options to configure a HTTP request header hash policy, used in request attribute hash based load balancing.

| Field | Description |
| --- | --- |
| `headerName` _string_ | HeaderName is the name of the HTTP request header that will be used to calculate the hash key. If the header specified is not present on a request, no hash will be produced. |

(_Appears on:_[MatchCondition](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.MatchCondition), [RequestHeaderValueMatchDescriptor](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RequestHeaderValueMatchDescriptor))

HeaderMatchCondition specifies how to conditionally match against HTTP headers. The Name field is required, only one of Present, NotPresent, Contains, NotContains, Exact, NotExact and Regex can be set. For negative matching rules only (e.g. NotContains or NotExact) you can set TreatMissingAsEmpty. IgnoreCase has no effect for Regex.

| Field | Description |
| --- | --- |
| `name` _string_ | Name is the name of the header to match against. Name is required. Header names are case insensitive. |
| `present` _bool_ | _(Optional)_ Present specifies that condition is true when the named header is present, regardless of its value. Note that setting Present to false does not make the condition true if the named header is absent. |
| `notpresent` _bool_ | _(Optional)_ NotPresent specifies that condition is true when the named header is not present. Note that setting NotPresent to false does not make the condition true if the named header is present. |
| `contains` _string_ | _(Optional)_ Contains specifies a substring that must be present in the header value. |
| `notcontains` _string_ | _(Optional)_ NotContains specifies a substring that must not be present in the header value. |
| `ignoreCase` _bool_ | _(Optional)_ IgnoreCase specifies that string matching should be case insensitive. Note that this has no effect on the Regex parameter. |
| `exact` _string_ | _(Optional)_ Exact specifies a string that the header value must be equal to. |
| `notexact` _string_ | _(Optional)_ NoExact specifies a string that the header value must not be equal to. The condition is true if the header has any other value. |
| `regex` _string_ | _(Optional)_ Regex specifies a regular expression pattern that must match the header value. |
| `treatMissingAsEmpty` _bool_ | _(Optional)_ TreatMissingAsEmpty specifies if the header match rule specified header does not exist, this header value will be treated as empty. Defaults to false. Unlike the underlying Envoy implementation this is **only** supported for negative matches (e.g. NotContains, NotExact). |

(_Appears on:_[HeadersPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HeadersPolicy), [LocalRateLimitPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.LocalRateLimitPolicy))

HeaderValue represents a header name/value pair

| Field | Description |
| --- | --- |
| `name` _string_ | Name represents a key of a header |
| `value` _string_ | Value represents the value of a header specified by a key |

(_Appears on:_[Route](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Route), [Service](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Service))

HeadersPolicy defines how headers are managed during forwarding. The `Host` header is treated specially and if set in a HTTP request will be used as the SNI server name when forwarding over TLS. It is an error to attempt to set the `Host` header in a HTTP response.

| Field | Description |
| --- | --- |
| `set` _[[]HeaderValue](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HeaderValue)_ | _(Optional)_ Set specifies a list of HTTP header values that will be set in the HTTP header. If the header does not exist it will be added, otherwise it will be overwritten with the new value. |
| `remove` _[]string_ | _(Optional)_ Remove specifies a list of HTTP header names to remove. |

### IPFilterPolicy

(_Appears on:_[Route](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Route), [VirtualHost](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.VirtualHost))

| Field | Description |
| --- | --- |
| `source` _[IPFilterSource](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.IPFilterSource)_ | Source indicates how to determine the ip address to filter on, and can be one of two values: - `Remote` filters on the ip address of the client, accounting for PROXY and X-Forwarded-For as needed. - `Peer` filters on the ip of the network request, ignoring PROXY and X-Forwarded-For. |
| `cidr` _string_ | CIDR is a CIDR block of ipv4 or ipv6 addresses to filter on. This can also be a bare IP address (without a mask) to filter on exactly one address. |

### IPFilterSource (`string` alias)

(_Appears on:_[IPFilterPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.IPFilterPolicy))

IPFilterSource indicates which IP should be considered for filtering

| Value | Description |
| --- | --- |
| "Peer" |  |
| "Remote" |  |

### Include

(_Appears on:_[HTTPProxySpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HTTPProxySpec))

Include describes a set of policies that can be applied to an HTTPProxy in a namespace.

| Field | Description |
| --- | --- |
| `name` _string_ | Name of the HTTPProxy |
| `namespace` _string_ | _(Optional)_ Namespace of the HTTPProxy to include. Defaults to the current namespace if not supplied. |
| `conditions` _[[]MatchCondition](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.MatchCondition)_ | _(Optional)_ Conditions are a set of rules that are applied to included HTTPProxies. In effect, they are added onto the Conditions of included HTTPProxy Route structs. When applied, they are merged using AND, with one exception: There can be only one Prefix MatchCondition per Conditions slice. More than one Prefix, or contradictory Conditions, will make the include invalid. Exact and Regex match conditions are not allowed on includes. |

### JWTProvider

(_Appears on:_[VirtualHost](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.VirtualHost))

JWTProvider defines how to verify JWTs on requests.

| Field | Description |
| --- | --- |
| `name` _string_ | Unique name for the provider. |
| `default` _bool_ | _(Optional)_ Whether the provider should apply to all routes in the HTTPProxy/its includes by default. At most one provider can be marked as the default. If no provider is marked as the default, individual routes must explicitly identify the provider they require. |
| `issuer` _string_ | _(Optional)_ Issuer that JWTs are required to have in the “iss” field. If not provided, JWT issuers are not checked. |
| `audiences` _[]string_ | _(Optional)_ Audiences that JWTs are allowed to have in the “aud” field. If not provided, JWT audiences are not checked. |
| `remoteJWKS` _[RemoteJWKS](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RemoteJWKS)_ | Remote JWKS to use for verifying JWT signatures. |
| `forwardJWT` _bool_ | _(Optional)_ Whether the JWT should be forwarded to the backend service after successful verification. By default, the JWT is not forwarded. |

### JWTVerificationPolicy

(_Appears on:_[Route](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Route))

| Field | Description |
| --- | --- |
| `require` _string_ | _(Optional)_ Require names a specific JWT provider (defined in the virtual host) to require for the route. If specified, this field overrides the default provider if one exists. If this field is not specified, the default provider will be required if one exists. At most one of this field or the “disabled” field can be specified. |
| `disabled` _bool_ | _(Optional)_ Disabled defines whether to disable all JWT verification for this route. This can be used to opt specific routes out of the default JWT provider for the HTTPProxy. At most one of this field or the “require” field can be specified. |

### LoadBalancerPolicy

(_Appears on:_[Route](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Route), [TCPProxy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TCPProxy), [ExtensionServiceSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ExtensionServiceSpec))

LoadBalancerPolicy defines the load balancing policy.

| Field | Description |
| --- | --- |
| `strategy` _string_ | Strategy specifies the policy used to balance requests across the pool of backend pods. Valid policy names are `Random`, `RoundRobin`, `WeightedLeastRequest`, `Cookie`, and `RequestHash`. If an unknown strategy name is specified or no policy is supplied, the default `RoundRobin` policy is used. |
| `requestHashPolicies` _[[]RequestHashPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RequestHashPolicy)_ | RequestHashPolicies contains a list of hash policies to apply when the `RequestHash` load balancing strategy is chosen. If an element of the supplied list of hash policies is invalid, it will be ignored. If the list of hash policies is empty after validation, the load balancing strategy will fall back to the default `RoundRobin`. |

### LocalRateLimitPolicy

(_Appears on:_[RateLimitPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RateLimitPolicy))

LocalRateLimitPolicy defines local rate limiting parameters.

| Field | Description |
| --- | --- |
| `requests` _uint32_ | Requests defines how many requests per unit of time should be allowed before rate limiting occurs. |
| `unit` _string_ | Unit defines the period of time within which requests over the limit will be rate limited. Valid values are “second”, “minute” and “hour”. |
| `burst` _uint32_ | _(Optional)_ Burst defines the number of requests above the requests per unit that should be allowed within a short period of time. |
| `responseStatusCode` _uint32_ | _(Optional)_ ResponseStatusCode is the HTTP status code to use for responses to rate-limited requests. Codes must be in the 400-599 range (inclusive). If not specified, the Envoy default of 429 (Too Many Requests) is used. |
| `responseHeadersToAdd` _[[]HeaderValue](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HeaderValue)_ | _(Optional)_ ResponseHeadersToAdd is an optional list of response headers to set when a request is rate-limited. |

### MatchCondition

(_Appears on:_[Include](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Include), [Route](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Route))

MatchCondition are a general holder for matching rules for HTTPProxies. One of Prefix, Exact, Regex, Header or QueryParameter must be provided.

| Field | Description |
| --- | --- |
| `prefix` _string_ | _(Optional)_ Prefix defines a prefix match for a request. |
| `exact` _string_ | _(Optional)_ Exact defines a exact match for a request. This field is not allowed in include match conditions. |
| `regex` _string_ | _(Optional)_ Regex defines a regex match for a request. This field is not allowed in include match conditions. |
| `header` _[HeaderMatchCondition](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HeaderMatchCondition)_ | _(Optional)_ Header specifies the header condition to match. |
| `queryParameter` _[QueryParameterMatchCondition](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.QueryParameterMatchCondition)_ | _(Optional)_ QueryParameter specifies the query parameter condition to match. |

### Namespace (`string` alias)

(_Appears on:_[ContourSettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourSettings))

Namespace refers to a Kubernetes namespace. It must be a RFC 1123 label.

This validation is based off of the corresponding Kubernetes validation: [https://github.com/kubernetes/apimachinery/blob/02cfb53916346d085a6c6c7c66f882e3c6b0eca6/pkg/util/validation/validation.go#L187](https://github.com/kubernetes/apimachinery/blob/02cfb53916346d085a6c6c7c66f882e3c6b0eca6/pkg/util/validation/validation.go#L187)

This is used for Namespace name validation here: [https://github.com/kubernetes/apimachinery/blob/02cfb53916346d085a6c6c7c66f882e3c6b0eca6/pkg/api/validation/generic.go#L63](https://github.com/kubernetes/apimachinery/blob/02cfb53916346d085a6c6c7c66f882e3c6b0eca6/pkg/api/validation/generic.go#L63)

Valid values include:

* “example”

Invalid values include:

* “example.com” - “.” is an invalid character

### PathRewritePolicy

(_Appears on:_[Route](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Route))

PathRewritePolicy specifies how a request URL path should be rewritten. This rewriting takes place after a request is routed and has no subsequent effects on the proxy’s routing decision. No HTTP headers or body content is rewritten.

Exactly one field in this struct may be specified.

| Field | Description |
| --- | --- |
| `replacePrefix` _[[]ReplacePrefix](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.ReplacePrefix)_ | _(Optional)_ ReplacePrefix describes how the path prefix should be replaced. |

### QueryParameterHashOptions

(_Appears on:_[RequestHashPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RequestHashPolicy))

QueryParameterHashOptions contains options to configure a query parameter based hash policy, used in request attribute hash based load balancing.

| Field | Description |
| --- | --- |
| `parameterName` _string_ | ParameterName is the name of the HTTP request query parameter that will be used to calculate the hash key. If the query parameter specified is not present on a request, no hash will be produced. |

### QueryParameterMatchCondition

(_Appears on:_[MatchCondition](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.MatchCondition))

QueryParameterMatchCondition specifies how to conditionally match against HTTP query parameters. The Name field is required, only one of Exact, Prefix, Suffix, Regex, Contains and Present can be set. IgnoreCase has no effect for Regex.

| Field | Description |
| --- | --- |
| `name` _string_ | Name is the name of the query parameter to match against. Name is required. Query parameter names are case insensitive. |
| `exact` _string_ | _(Optional)_ Exact specifies a string that the query parameter value must be equal to. |
| `prefix` _string_ | _(Optional)_ Prefix defines a prefix match for the query parameter value. |
| `suffix` _string_ | _(Optional)_ Suffix defines a suffix match for a query parameter value. |
| `regex` _string_ | _(Optional)_ Regex specifies a regular expression pattern that must match the query parameter value. |
| `contains` _string_ | _(Optional)_ Contains specifies a substring that must be present in the query parameter value. |
| `ignoreCase` _bool_ | _(Optional)_ IgnoreCase specifies that string matching should be case insensitive. Note that this has no effect on the Regex parameter. |
| `present` _bool_ | _(Optional)_ Present specifies that condition is true when the named query parameter is present, regardless of its value. Note that setting Present to false does not make the condition true if the named query parameter is absent. |

### RateLimitDescriptor

(_Appears on:_[GlobalRateLimitPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.GlobalRateLimitPolicy))

RateLimitDescriptor defines a list of key-value pair generators.

| Field | Description |
| --- | --- |
| `entries` _[[]RateLimitDescriptorEntry](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RateLimitDescriptorEntry)_ | Entries is the list of key-value pair generators. |

### RateLimitDescriptorEntry

(_Appears on:_[RateLimitDescriptor](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RateLimitDescriptor))

RateLimitDescriptorEntry is a key-value pair generator. Exactly one field on this struct must be non-nil.

| Field | Description |
| --- | --- |
| `genericKey` _[GenericKeyDescriptor](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.GenericKeyDescriptor)_ | _(Optional)_ GenericKey defines a descriptor entry with a static key and value. |
| `requestHeader` _[RequestHeaderDescriptor](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RequestHeaderDescriptor)_ | _(Optional)_ RequestHeader defines a descriptor entry that’s populated only if a given header is present on the request. The descriptor key is static, and the descriptor value is equal to the value of the header. |
| `requestHeaderValueMatch` _[RequestHeaderValueMatchDescriptor](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RequestHeaderValueMatchDescriptor)_ | _(Optional)_ RequestHeaderValueMatch defines a descriptor entry that’s populated if the request’s headers match a set of 1+ match criteria. The descriptor key is “header_match”, and the descriptor value is static. |
| `remoteAddress` _[RemoteAddressDescriptor](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RemoteAddressDescriptor)_ | _(Optional)_ RemoteAddress defines a descriptor entry with a key of “remote_address” and a value equal to the client’s IP address (from x-forwarded-for). |

### RateLimitPolicy

(_Appears on:_[Route](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Route), [VirtualHost](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.VirtualHost))

RateLimitPolicy defines rate limiting parameters.

| Field | Description |
| --- | --- |
| `local` _[LocalRateLimitPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.LocalRateLimitPolicy)_ | _(Optional)_ Local defines local rate limiting parameters, i.e. parameters for rate limiting that occurs within each Envoy pod as requests are handled. |
| `global` _[GlobalRateLimitPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.GlobalRateLimitPolicy)_ | _(Optional)_ Global defines global rate limiting parameters, i.e. parameters defining descriptors that are sent to an external rate limit service (RLS) for a rate limit decision on each request. |

### RedirectResponseCode (`uint32` alias)

(_Appears on:_[HTTPInternalRedirectPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HTTPInternalRedirectPolicy), [HTTPRequestRedirectPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HTTPRequestRedirectPolicy))

RedirectResponseCode is a uint32 type alias with validation to ensure that the value is valid.

### RemoteAddressDescriptor

(_Appears on:_[RateLimitDescriptorEntry](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RateLimitDescriptorEntry))

RemoteAddressDescriptor defines a descriptor entry with a key of “remote_address” and a value equal to the client’s IP address (from x-forwarded-for).

### RemoteJWKS

(_Appears on:_[JWTProvider](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.JWTProvider))

RemoteJWKS defines how to fetch a JWKS from an HTTP endpoint.

| Field | Description |
| --- | --- |
| `uri` _string_ | The URI for the JWKS. |
| `validation` _[UpstreamValidation](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.UpstreamValidation)_ | _(Optional)_ UpstreamValidation defines how to verify the JWKS’s TLS certificate. |
| `timeout` _string_ | _(Optional)_ How long to wait for a response from the URI. If not specified, a default of 1s applies. |
| `cacheDuration` _string_ | _(Optional)_ How long to cache the JWKS locally. If not specified, Envoy’s default of 5m applies. |
| `dnsLookupFamily` _string_ | _(Optional)_ The DNS IP address resolution policy for the JWKS URI. When configured as “v4”, the DNS resolver will only perform a lookup for addresses in the IPv4 family. If “v6” is configured, the DNS resolver will only perform a lookup for addresses in the IPv6 family. If “all” is configured, the DNS resolver will perform a lookup for addresses in both the IPv4 and IPv6 family. If “auto” is configured, the DNS resolver will first perform a lookup for addresses in the IPv6 family and fallback to a lookup for addresses in the IPv4 family. If not specified, the Contour-wide setting defined in the config file or ContourConfiguration applies (defaults to “auto”). See [https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/cluster/v3/cluster.proto.html#envoy-v3-api-enum-config-cluster-v3-cluster-dnslookupfamily](https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/cluster/v3/cluster.proto.html#envoy-v3-api-enum-config-cluster-v3-cluster-dnslookupfamily) for more information. |

### ReplacePrefix

(_Appears on:_[PathRewritePolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.PathRewritePolicy))

ReplacePrefix describes a path prefix replacement.

| Field | Description |
| --- | --- |
| `prefix` _string_ | _(Optional)_ Prefix specifies the URL path prefix to be replaced. If Prefix is specified, it must exactly match the MatchCondition prefix that is rendered by the chain of including HTTPProxies and only that path prefix will be replaced by Replacement. This allows HTTPProxies that are included through multiple roots to only replace specific path prefixes, leaving others unmodified. If Prefix is not specified, all routing prefixes rendered by the include chain will be replaced. |
| `replacement` _string_ | Replacement is the string that the routing path prefix will be replaced with. This must not be empty. |

### RequestHashPolicy

(_Appears on:_[LoadBalancerPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.LoadBalancerPolicy))

RequestHashPolicy contains configuration for an individual hash policy on a request attribute.

| Field | Description |
| --- | --- |
| `terminal` _bool_ | Terminal is a flag that allows for short-circuiting computing of a hash for a given request. If set to true, and the request attribute specified in the attribute hash options is present, no further hash policies will be used to calculate a hash for the request. |
| `headerHashOptions` _[HeaderHashOptions](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HeaderHashOptions)_ | _(Optional)_ HeaderHashOptions should be set when request header hash based load balancing is desired. It must be the only hash option field set, otherwise this request hash policy object will be ignored. |
| `queryParameterHashOptions` _[QueryParameterHashOptions](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.QueryParameterHashOptions)_ | _(Optional)_ QueryParameterHashOptions should be set when request query parameter hash based load balancing is desired. It must be the only hash option field set, otherwise this request hash policy object will be ignored. |
| `hashSourceIP` _bool_ | _(Optional)_ HashSourceIP should be set to true when request source IP hash based load balancing is desired. It must be the only hash option field set, otherwise this request hash policy object will be ignored. |

(_Appears on:_[RateLimitDescriptorEntry](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RateLimitDescriptorEntry))

RequestHeaderDescriptor defines a descriptor entry that’s populated only if a given header is present on the request. The value of the descriptor entry is equal to the value of the header (if present).

| Field | Description |
| --- | --- |
| `headerName` _string_ | HeaderName defines the name of the header to look for on the request. |
| `descriptorKey` _string_ | DescriptorKey defines the key to use on the descriptor entry. |

(_Appears on:_[RateLimitDescriptorEntry](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RateLimitDescriptorEntry))

RequestHeaderValueMatchDescriptor defines a descriptor entry that’s populated if the request’s headers match a set of 1+ match criteria. The descriptor key is “header_match”, and the descriptor value is statically defined.

| Field | Description |
| --- | --- |
| `headers` _[[]HeaderMatchCondition](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HeaderMatchCondition)_ | Headers is a list of 1+ match criteria to apply against the request to determine whether to populate the descriptor entry or not. |
| `expectMatch` _bool_ | ExpectMatch defines whether the request must positively match the match criteria in order to generate a descriptor entry (i.e. true), or not match the match criteria in order to generate a descriptor entry (i.e. false). The default is true. |
| `value` _string_ | Value defines the value of the descriptor entry. |

### RetryOn (`string` alias)

(_Appears on:_[RetryPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RetryPolicy))

RetryOn is a string type alias with validation to ensure that the value is valid.

### RetryPolicy

(_Appears on:_[Route](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Route))

RetryPolicy defines the attributes associated with retrying policy.

| Field | Description |
| --- | --- |
| `count` _int64_ | _(Optional)_ NumRetries is maximum allowed number of retries. If set to -1, then retries are disabled. If set to 0 or not supplied, the value is set to the Envoy default of 1. |
| `perTryTimeout` _string_ | _(Optional)_ PerTryTimeout specifies the timeout per retry attempt. Ignored if NumRetries is not supplied. |
| `retryOn` _[[]RetryOn](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RetryOn)_ | _(Optional)_ RetryOn specifies the conditions on which to retry a request. Supported [HTTP conditions](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/router_filter#x-envoy-retry-on): *`5xx`* `gateway-error` *`reset`* `reset-before-request` *`connect-failure`* `envoy-ratelimited` *`retriable-4xx`* `refused-stream` *`retriable-status-codes`* `retriable-headers` *`http3-post-connect-failure` Supported [gRPC conditions](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/router_filter#x-envoy-retry-grpc-on):* `cancelled` *`deadline-exceeded`* `internal` *`resource-exhausted`* `unavailable` |
| `retriableStatusCodes` _[]uint32_ | _(Optional)_ RetriableStatusCodes specifies the HTTP status codes that should be retried. This field is only respected when you include `retriable-status-codes` in the `RetryOn` field. |

### Route

(_Appears on:_[HTTPProxySpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HTTPProxySpec))

Route contains the set of routes for a virtual host.

| Field | Description |
| --- | --- |
| `conditions` _[[]MatchCondition](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.MatchCondition)_ | _(Optional)_ Conditions are a set of rules that are applied to a Route. When applied, they are merged using AND, with one exception: There can be only one Prefix, Exact or Regex MatchCondition per Conditions slice. More than one of these condition types, or contradictory Conditions, will make the route invalid. |
| `services` _[[]Service](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Service)_ | _(Optional)_ Services are the services to proxy traffic. |
| `enableWebsockets` _bool_ | _(Optional)_ Enables websocket support for the route. |
| `permitInsecure` _bool_ | _(Optional)_ Allow this path to respond to insecure requests over HTTP which are normally not permitted when a `virtualhost.tls` block is present. |
| `authPolicy` _[AuthorizationPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.AuthorizationPolicy)_ | _(Optional)_ AuthPolicy updates the authorization policy that was set on the root HTTPProxy object for client requests that match this route. |
| `timeoutPolicy` _[TimeoutPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TimeoutPolicy)_ | _(Optional)_ The timeout policy for this route. |
| `retryPolicy` _[RetryPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RetryPolicy)_ | _(Optional)_ The retry policy for this route. |
| `healthCheckPolicy` _[HTTPHealthCheckPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HTTPHealthCheckPolicy)_ | _(Optional)_ The health check policy for this route. |
| `loadBalancerPolicy` _[LoadBalancerPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.LoadBalancerPolicy)_ | _(Optional)_ The load balancing policy for this route. |
| `pathRewritePolicy` _[PathRewritePolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.PathRewritePolicy)_ | _(Optional)_ The policy for rewriting the path of the request URL after the request has been routed to a Service. |
| `requestHeadersPolicy` _[HeadersPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HeadersPolicy)_ | _(Optional)_ The policy for managing request headers during proxying. You may dynamically rewrite the Host header to be forwarded upstream to the content of a request header using the below format “%REQ(X-Header-Name)%”. If the value of the header is empty, it is ignored. *NOTE: Pay attention to the potential security implications of using this option. Provided header must come from trusted source. **NOTE: The header rewrite is only done while forwarding and has no bearing on the routing decision. |
| `responseHeadersPolicy` _[HeadersPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HeadersPolicy)_ | _(Optional)_ The policy for managing response headers during proxying. Rewriting the ‘Host’ header is not supported. |
| `cookieRewritePolicies` _[[]CookieRewritePolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.CookieRewritePolicy)_ | _(Optional)_ The policies for rewriting Set-Cookie header attributes. Note that rewritten cookie names must be unique in this list. Order rewrite policies are specified in does not matter. |
| `rateLimitPolicy` _[RateLimitPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RateLimitPolicy)_ | _(Optional)_ The policy for rate limiting on the route. |
| `requestRedirectPolicy` _[HTTPRequestRedirectPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HTTPRequestRedirectPolicy)_ | _(Optional)_ RequestRedirectPolicy defines an HTTP redirection. |
| `directResponsePolicy` _[HTTPDirectResponsePolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HTTPDirectResponsePolicy)_ | _(Optional)_ DirectResponsePolicy returns an arbitrary HTTP response directly. |
| `internalRedirectPolicy` _[HTTPInternalRedirectPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HTTPInternalRedirectPolicy)_ | _(Optional)_ The policy to define when to handle redirects responses internally. |
| `jwtVerificationPolicy` _[JWTVerificationPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.JWTVerificationPolicy)_ | _(Optional)_ The policy for verifying JWTs for requests to this route. |
| `ipAllowPolicy` _[[]IPFilterPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.IPFilterPolicy)_ | IPAllowFilterPolicy is a list of ipv4/6 filter rules for which matching requests should be allowed. All other requests will be denied. Only one of IPAllowFilterPolicy and IPDenyFilterPolicy can be defined. The rules defined here override any rules set on the root HTTPProxy. |
| `ipDenyPolicy` _[[]IPFilterPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.IPFilterPolicy)_ | IPDenyFilterPolicy is a list of ipv4/6 filter rules for which matching requests should be denied. All other requests will be allowed. Only one of IPAllowFilterPolicy and IPDenyFilterPolicy can be defined. The rules defined here override any rules set on the root HTTPProxy. |

### Service

(_Appears on:_[Route](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Route), [TCPProxy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TCPProxy))

Service defines an Kubernetes Service to proxy traffic.

| Field | Description |
| --- | --- |
| `name` _string_ | Name is the name of Kubernetes service to proxy traffic. Names defined here will be used to look up corresponding endpoints which contain the ips to route. |
| `port` _int_ | Port (defined as Integer) to proxy traffic to since a service can have multiple defined. |
| `healthPort` _int_ | _(Optional)_ HealthPort is the port for this service healthcheck. If not specified, Port is used for service healthchecks. |
| `protocol` _string_ | _(Optional)_ Protocol may be used to specify (or override) the protocol used to reach this Service. Values may be tls, h2, h2c. If omitted, protocol-selection falls back on Service annotations. |
| `weight` _int64_ | _(Optional)_ Weight defines percentage of traffic to balance traffic |
| `validation` _[UpstreamValidation](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.UpstreamValidation)_ | _(Optional)_ UpstreamValidation defines how to verify the backend service’s certificate |
| `mirror` _bool_ | If Mirror is true the Service will receive a read only mirror of the traffic for this route. If Mirror is true, then fractional mirroring can be enabled by optionally setting the Weight field. Legal values for Weight are 1-100. Omitting the Weight field will result in 100% mirroring. NOTE: Setting Weight explicitly to 0 will unexpectedly result in 100% traffic mirroring. This occurs since we cannot distinguish omitted fields from those explicitly set to their default values |
| `requestHeadersPolicy` _[HeadersPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HeadersPolicy)_ | _(Optional)_ The policy for managing request headers during proxying. |
| `responseHeadersPolicy` _[HeadersPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HeadersPolicy)_ | _(Optional)_ The policy for managing response headers during proxying. Rewriting the ‘Host’ header is not supported. |
| `cookieRewritePolicies` _[[]CookieRewritePolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.CookieRewritePolicy)_ | _(Optional)_ The policies for rewriting Set-Cookie header attributes. |
| `slowStartPolicy` _[SlowStartPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.SlowStartPolicy)_ | _(Optional)_ Slow start will gradually increase amount of traffic to a newly added endpoint. |

### SlowStartPolicy

(_Appears on:_[Service](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Service))

SlowStartPolicy will gradually increase amount of traffic to a newly added endpoint. It can be used only with RoundRobin and WeightedLeastRequest load balancing strategies.

| Field | Description |
| --- | --- |
| `window` _string_ | The duration of slow start window. Duration is expressed in the Go [Duration format](https://godoc.org/time#ParseDuration). Valid time units are “ns”, “us” (or “µs”), “ms”, “s”, “m”, “h”. |
| `aggression` _string_ | _(Optional)_ The speed of traffic increase over the slow start window. Defaults to 1.0, so that endpoint would get linearly increasing amount of traffic. When increasing the value for this parameter, the speed of traffic ramp-up increases non-linearly. The value of aggression parameter should be greater than 0.0. More info: [https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/load_balancing/slow_start](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/load_balancing/slow_start) |
| `minWeightPercent` _uint32_ | _(Optional)_ The minimum or starting percentage of traffic to send to new endpoints. A non-zero value helps avoid a too small initial weight, which may cause endpoints in slow start mode to receive no traffic in the beginning of the slow start window. If not specified, the default is 10%. |

### SubCondition

(_Appears on:_[DetailedCondition](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.DetailedCondition))

SubCondition is a Condition-like type intended for use as a subcondition inside a DetailedCondition.

It contains a subset of the Condition fields.

It is intended for warnings and errors, so `type` names should use abnormal-true polarity, that is, they should be of the form “ErrorPresent: true”.

The expected lifecycle for these errors is that they should only be present when the error or warning is, and should be removed when they are not relevant.

| Field | Description |
| --- | --- |
| `type` _string_ | Type of condition in `CamelCase` or in `foo.example.com/CamelCase`. This must be in abnormal-true polarity, that is, `ErrorFound` or `controller.io/ErrorFound`. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt) |
| `status` _[Kubernetes meta/v1.ConditionStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#conditionstatus-v1-meta)_ | Status of the condition, one of True, False, Unknown. |
| `reason` _string_ | Reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. |
| `message` _string_ | Message is a human readable message indicating details about the transition. This may be an empty string. |

### TCPHealthCheckPolicy

(_Appears on:_[TCPProxy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TCPProxy))

TCPHealthCheckPolicy defines health checks on the upstream service.

| Field | Description |
| --- | --- |
| `intervalSeconds` _int64_ | _(Optional)_ The interval (seconds) between health checks |
| `timeoutSeconds` _int64_ | _(Optional)_ The time to wait (seconds) for a health check response |
| `unhealthyThresholdCount` _uint32_ | _(Optional)_ The number of unhealthy health checks required before a host is marked unhealthy |
| `healthyThresholdCount` _uint32_ | _(Optional)_ The number of healthy health checks required before a host is marked healthy |

### TCPProxy

(_Appears on:_[HTTPProxySpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HTTPProxySpec))

TCPProxy contains the set of services to proxy TCP connections.

| Field | Description |
| --- | --- |
| `loadBalancerPolicy` _[LoadBalancerPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.LoadBalancerPolicy)_ | _(Optional)_ The load balancing policy for the backend services. Note that the `Cookie` and `RequestHash` load balancing strategies cannot be used here. |
| `services` _[[]Service](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Service)_ | _(Optional)_ Services are the services to proxy traffic |
| `include` _[TCPProxyInclude](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TCPProxyInclude)_ | _(Optional)_ Include specifies that this tcpproxy should be delegated to another HTTPProxy. |
| `includes` _[TCPProxyInclude](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TCPProxyInclude)_ | _(Optional)_ IncludesDeprecated allow for specific routing configuration to be appended to another HTTPProxy in another namespace. Exists due to a mistake when developing HTTPProxy and the field was marked plural when it should have been singular. This field should stay to not break backwards compatibility to v1 users. |
| `healthCheckPolicy` _[TCPHealthCheckPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TCPHealthCheckPolicy)_ | _(Optional)_ The health check policy for this tcp proxy |

### TCPProxyInclude

(_Appears on:_[TCPProxy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TCPProxy))

TCPProxyInclude describes a target HTTPProxy document which contains the TCPProxy details.

| Field | Description |
| --- | --- |
| `name` _string_ | Name of the child HTTPProxy |
| `namespace` _string_ | _(Optional)_ Namespace of the HTTPProxy to include. Defaults to the current namespace if not supplied. |

### TLS

(_Appears on:_[VirtualHost](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.VirtualHost))

TLS describes tls properties. The SNI names that will be matched on are described in the HTTPProxy’s Spec.VirtualHost.Fqdn field.

| Field | Description |
| --- | --- |
| `secretName` _string_ | SecretName is the name of a TLS secret. Either SecretName or Passthrough must be specified, but not both. If specified, the named secret must contain a matching certificate for the virtual host’s FQDN. The name can be optionally prefixed with namespace “namespace/name”. When cross-namespace reference is used, TLSCertificateDelegation resource must exist in the namespace to grant access to the secret. |
| `minimumProtocolVersion` _string_ | _(Optional)_ MinimumProtocolVersion is the minimum TLS version this vhost should negotiate. Valid options are `1.2` (default) and `1.3`. Any other value defaults to TLS 1.2. |
| `maximumProtocolVersion` _string_ | _(Optional)_ MaximumProtocolVersion is the maximum TLS version this vhost should negotiate. Valid options are `1.2` and `1.3` (default). Any other value defaults to TLS 1.3. |
| `passthrough` _bool_ | _(Optional)_ Passthrough defines whether the encrypted TLS handshake will be passed through to the backing cluster. Either Passthrough or SecretName must be specified, but not both. |
| `clientValidation` _[DownstreamValidation](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.DownstreamValidation)_ | _(Optional)_ ClientValidation defines how to verify the client certificate when an external client establishes a TLS connection to Envoy. This setting: 1. Enables TLS client certificate validation. 2. Specifies how the client certificate will be validated (i.e. validation required or skipped). Note: Setting client certificate validation to be skipped should be only used in conjunction with an external authorization server that performs client validation as Contour will ensure client certificates are passed along. |
| `enableFallbackCertificate` _bool_ | EnableFallbackCertificate defines if the vhost should allow a default certificate to be applied which handles all requests which don’t match the SNI defined in this vhost. |

### TLSCertificateDelegationSpec

(_Appears on:_[TLSCertificateDelegation](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TLSCertificateDelegation))

TLSCertificateDelegationSpec defines the spec of the CRD

| Field | Description |
| --- | --- |
| `delegations` _[[]CertificateDelegation](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.CertificateDelegation)_ |  |

### TLSCertificateDelegationStatus

(_Appears on:_[TLSCertificateDelegation](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TLSCertificateDelegation))

TLSCertificateDelegationStatus allows for the status of the delegation to be presented to the user.

| Field | Description |
| --- | --- |
| `conditions` _[[]DetailedCondition](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.DetailedCondition)_ | _(Optional)_ Conditions contains information about the current status of the HTTPProxy, in an upstream-friendly container. Contour will update a single condition, `Valid`, that is in normal-true polarity. That is, when `currentStatus` is `valid`, the `Valid` condition will be `status: true`, and vice versa. Contour will leave untouched any other Conditions set in this block, in case some other controller wants to add a Condition. If you are another controller owner and wish to add a condition, you _should_ namespace your condition with a label, like `controller.domain.com\ConditionName`. |

### TimeoutPolicy

(_Appears on:_[Route](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Route), [ExtensionServiceSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ExtensionServiceSpec))

TimeoutPolicy configures timeouts that are used for handling network requests.

TimeoutPolicy durations are expressed in the Go [Duration format](https://godoc.org/time#ParseDuration). Valid time units are “ns”, “us” (or “µs”), “ms”, “s”, “m”, “h”. The string “infinity” is also a valid input and specifies no timeout. A value of “0s” will be treated as if the field were not set, i.e. by using Envoy’s default behavior.

Example input values: “300ms”, “5s”, “1m”.

| Field | Description |
| --- | --- |
| `response` _string_ | _(Optional)_ Timeout for receiving a response from the server after processing a request from client. If not supplied, Envoy’s default value of 15s applies. |
| `idle` _string_ | _(Optional)_ Timeout for how long the proxy should wait while there is no activity during single request/response (for HTTP/1.1) or stream (for HTTP/2). Timeout will not trigger while HTTP/1.1 connection is idle between two consecutive requests. If not specified, there is no per-route idle timeout, though a connection manager-wide stream_idle_timeout default of 5m still applies. |
| `idleConnection` _string_ | _(Optional)_ Timeout for how long connection from the proxy to the upstream service is kept when there are no active requests. If not supplied, Envoy’s default value of 1h applies. |

### UpstreamValidation

(_Appears on:_[RemoteJWKS](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RemoteJWKS), [Service](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Service), [ExtensionServiceSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ExtensionServiceSpec))

UpstreamValidation defines how to verify the backend service’s certificate

| Field | Description |
| --- | --- |
| `caSecret` _string_ | Name or namespaced name of the Kubernetes secret used to validate the certificate presented by the backend. The secret must contain key named ca.crt. The name can be optionally prefixed with namespace “namespace/name”. When cross-namespace reference is used, TLSCertificateDelegation resource must exist in the namespace to grant access to the secret. Max length should be the actual max possible length of a namespaced name (63 + 253 + 1 = 317) |
| `subjectName` _string_ | Key which is expected to be present in the ‘subjectAltName’ of the presented certificate. Deprecated: migrate to using the plural field subjectNames. |
| `subjectNames` _[]string_ | _(Optional)_ List of keys, of which at least one is expected to be present in the ‘subjectAltName of the presented certificate. |

### VirtualHost

(_Appears on:_[HTTPProxySpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.HTTPProxySpec))

VirtualHost appears at most once. If it is present, the object is considered to be a “root”.

| Field | Description |
| --- | --- |
| `fqdn` _string_ | The fully qualified domain name of the root of the ingress tree all leaves of the DAG rooted at this object relate to the fqdn. |
| `tls` _[TLS](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TLS)_ | _(Optional)_ If present the fields describes TLS properties of the virtual host. The SNI names that will be matched on are described in fqdn, the tls.secretName secret must contain a certificate that itself contains a name that matches the FQDN. |
| `authorization` _[AuthorizationServer](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.AuthorizationServer)_ | _(Optional)_ This field configures an extension service to perform authorization for this virtual host. Authorization can only be configured on virtual hosts that have TLS enabled. If the TLS configuration requires client certificate validation, the client certificate is always included in the authentication check request. |
| `corsPolicy` _[CORSPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.CORSPolicy)_ | _(Optional)_ Specifies the cross-origin policy to apply to the VirtualHost. |
| `rateLimitPolicy` _[RateLimitPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.RateLimitPolicy)_ | _(Optional)_ The policy for rate limiting on the virtual host. |
| `jwtProviders` _[[]JWTProvider](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.JWTProvider)_ | _(Optional)_ Providers to use for verifying JSON Web Tokens (JWTs) on the virtual host. |
| `ipAllowPolicy` _[[]IPFilterPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.IPFilterPolicy)_ | IPAllowFilterPolicy is a list of ipv4/6 filter rules for which matching requests should be allowed. All other requests will be denied. Only one of IPAllowFilterPolicy and IPDenyFilterPolicy can be defined. The rules defined here may be overridden in a Route. |
| `ipDenyPolicy` _[[]IPFilterPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.IPFilterPolicy)_ | IPDenyFilterPolicy is a list of ipv4/6 filter rules for which matching requests should be denied. All other requests will be allowed. Only one of IPAllowFilterPolicy and IPDenyFilterPolicy can be defined. The rules defined here may be overridden in a Route. |

* * *

projectcontour.io/v1alpha1
--------------------------

Package v1alpha1 contains API Schema definitions for the projectcontour.io v1alpha1 API group

Resource Types:

* [ContourConfiguration](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfiguration)
* [ContourDeployment](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourDeployment)
* [ExtensionService](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ExtensionService)

### ContourConfiguration

ContourConfiguration is the schema for a Contour instance.

| Field | Description |
| --- | --- |
| `apiVersion` string | `projectcontour.io/v1alpha1` |
| `kind` string | `ContourConfiguration` |
| `metadata` _[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec` _[ContourConfigurationSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfigurationSpec)_ | `xdsServer` _[XDSServerConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.XDSServerConfig)_ _(Optional)_ XDSServer contains parameters for the xDS server. `ingress` _[IngressConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.IngressConfig)_ _(Optional)_ Ingress contains parameters for ingress options. `debug` _[DebugConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.DebugConfig)_ _(Optional)_ Debug contains parameters to enable debug logging and debug interfaces inside Contour. `health` _[HealthConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.HealthConfig)_ _(Optional)_ Health defines the endpoints Contour uses to serve health checks. Contour’s default is { address: “0.0.0.0”, port: 8000 }. `envoy` _[EnvoyConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyConfig)_ _(Optional)_ Envoy contains parameters for Envoy as well as how to optionally configure a managed Envoy fleet. `gateway` _[GatewayConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.GatewayConfig)_ _(Optional)_ Gateway contains parameters for the gateway-api Gateway that Contour is configured to serve traffic. `httpproxy` _[HTTPProxyConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.HTTPProxyConfig)_ _(Optional)_ HTTPProxy defines parameters on HTTPProxy. `enableExternalNameService` _bool_ _(Optional)_ EnableExternalNameService allows processing of ExternalNameServices Contour’s default is false for security reasons. `globalExtAuth` _[AuthorizationServer](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.AuthorizationServer)_ _(Optional)_ GlobalExternalAuthorization allows envoys external authorization filter to be enabled for all virtual hosts. `rateLimitService` _[RateLimitServiceConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.RateLimitServiceConfig)_ _(Optional)_ RateLimitService optionally holds properties of the Rate Limit Service to be used for global rate limiting. `policy` _[PolicyConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.PolicyConfig)_ _(Optional)_ Policy specifies default policy applied if not overridden by the user `metrics` _[MetricsConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.MetricsConfig)_ _(Optional)_ Metrics defines the endpoint Contour uses to serve metrics. Contour’s default is { address: “0.0.0.0”, port: 8000 }. `tracing` _[TracingConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.TracingConfig)_ Tracing defines properties for exporting trace data to OpenTelemetry. `featureFlags` _[FeatureFlags](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.FeatureFlags)_ FeatureFlags defines toggle to enable new contour features. |
| `status` _[ContourConfigurationStatus](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfigurationStatus)_ | _(Optional)_ |

### ContourDeployment

ContourDeployment is the schema for a Contour Deployment.

| Field | Description |
| --- | --- |
| `apiVersion` string | `projectcontour.io/v1alpha1` |
| `kind` string | `ContourDeployment` |
| `metadata` _[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec` _[ContourDeploymentSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourDeploymentSpec)_ | `contour` _[ContourSettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourSettings)_ _(Optional)_ Contour specifies deployment-time settings for the Contour part of the installation, i.e. the xDS server/control plane and associated resources, including things like replica count for the Deployment, and node placement constraints for the pods. `envoy` _[EnvoySettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoySettings)_ _(Optional)_ Envoy specifies deployment-time settings for the Envoy part of the installation, i.e. the xDS client/data plane and associated resources, including things like the workload type to use (DaemonSet or Deployment), node placement constraints for the pods, and various options for the Envoy service. `runtimeSettings` _[ContourConfigurationSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfigurationSpec)_ _(Optional)_ RuntimeSettings is a ContourConfiguration spec to be used when provisioning a Contour instance that will influence aspects of the Contour instance’s runtime behavior. `resourceLabels` _map[string]string_ _(Optional)_ ResourceLabels is a set of labels to add to the provisioned Contour resources. Deprecated: use Gateway.Spec.Infrastructure.Labels instead. This field will be removed in a future release. |
| `status` _[ContourDeploymentStatus](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourDeploymentStatus)_ |  |

### ExtensionService

ExtensionService is the schema for the Contour extension services API. An ExtensionService resource binds a network service to the Contour API so that Contour API features can be implemented by collaborating components.

| Field | Description |
| --- | --- |
| `apiVersion` string | `projectcontour.io/v1alpha1` |
| `kind` string | `ExtensionService` |
| `metadata` _[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec` _[ExtensionServiceSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ExtensionServiceSpec)_ | `services` _[[]ExtensionServiceTarget](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ExtensionServiceTarget)_ Services specifies the set of Kubernetes Service resources that receive GRPC extension API requests. If no weights are specified for any of the entries in this array, traffic will be spread evenly across all the services. Otherwise, traffic is balanced proportionally to the Weight field in each entry. `validation` _[UpstreamValidation](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.UpstreamValidation)_ _(Optional)_ UpstreamValidation defines how to verify the backend service’s certificate `protocol` _string_ _(Optional)_ Protocol may be used to specify (or override) the protocol used to reach this Service. Values may be h2 or h2c. If omitted, protocol-selection falls back on Service annotations. `loadBalancerPolicy` _[LoadBalancerPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.LoadBalancerPolicy)_ _(Optional)_ The policy for load balancing GRPC service requests. Note that the `Cookie` and `RequestHash` load balancing strategies cannot be used here. `timeoutPolicy` _[TimeoutPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TimeoutPolicy)_ _(Optional)_ The timeout policy for requests to the services. `protocolVersion` _[ExtensionProtocolVersion](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ExtensionProtocolVersion)_ _(Optional)_ This field sets the version of the GRPC protocol that Envoy uses to send requests to the extension service. Since Contour always uses the v3 Envoy API, this is currently fixed at “v3”. However, other protocol options will be available in future. `circuitBreakerPolicy` _[CircuitBreakers](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.CircuitBreakers)_ _(Optional)_ CircuitBreakerPolicy specifies the circuit breaker budget across the extension service. If defined this overrides the global circuit breaker budget. |
| `status` _[ExtensionServiceStatus](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ExtensionServiceStatus)_ |  |

### AccessLogFormatString (`string` alias)

### AccessLogJSONFields (`[]string` alias)

(_Appears on:_[EnvoyLogging](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyLogging))

### AccessLogLevel (`string` alias)

(_Appears on:_[EnvoyLogging](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyLogging))

| Value | Description |
| --- | --- |
| "critical" | Log only requests that result in an server error (i.e. 500+) response code. |
| "disabled" | Disable the access log. |
| "error" | Log only requests that result in a non-success (i.e. 300+) response code |
| "info" | Log all requests. This is the default. |

### AccessLogType (`string` alias)

(_Appears on:_[EnvoyLogging](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyLogging))

AccessLogType is the name of a supported access logging mechanism.

| Value | Description |
| --- | --- |
| "envoy" | DefaultAccessLogType is the default access log format. |
| "envoy" | Set the Envoy access logging to Envoy’s standard format. Can be customized using `accessLogFormatString`. |
| "json" | Set the Envoy access logging to a JSON format. Can be customized using `jsonFields`. |

### CircuitBreakers

(_Appears on:_[ClusterParameters](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ClusterParameters), [ExtensionServiceSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ExtensionServiceSpec))

| Field | Description |
| --- | --- |
| `maxConnections` _uint32_ | _(Optional)_ The maximum number of connections that a single Envoy instance allows to the Kubernetes Service; defaults to 1024. |
| `maxPendingRequests` _uint32_ | _(Optional)_ The maximum number of pending requests that a single Envoy instance allows to the Kubernetes Service; defaults to 1024. |
| `maxRequests` _uint32_ | _(Optional)_ The maximum parallel requests a single Envoy instance allows to the Kubernetes Service; defaults to 1024 |
| `maxRetries` _uint32_ | _(Optional)_ The maximum number of parallel retries a single Envoy instance allows to the Kubernetes Service; defaults to 3. |
| `perHostMaxConnections` _uint32_ | PerHostMaxConnections is the maximum number of connections that Envoy will allow to each individual host in a cluster. |

### ClusterDNSFamilyType (`string` alias)

(_Appears on:_[ClusterParameters](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ClusterParameters))

ClusterDNSFamilyType is the Ip family to use for resolving DNS names in an Envoy cluster config.

| Value | Description |
| --- | --- |
| "all" | DNS lookups will attempt both v4 and v6 queries. |
| "auto" | DNS lookups will do a v6 lookup first, followed by a v4 if that fails. |
| "v4" | DNS lookups will only attempt v4 queries. |
| "v6" | DNS lookups will only attempt v6 queries. |

### ClusterParameters

(_Appears on:_[EnvoyConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyConfig))

ClusterParameters holds various configurable cluster values.

| Field | Description |
| --- | --- |
| `dnsLookupFamily` _[ClusterDNSFamilyType](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ClusterDNSFamilyType)_ | _(Optional)_ DNSLookupFamily defines how external names are looked up When configured as V4, the DNS resolver will only perform a lookup for addresses in the IPv4 family. If V6 is configured, the DNS resolver will only perform a lookup for addresses in the IPv6 family. If AUTO is configured, the DNS resolver will first perform a lookup for addresses in the IPv6 family and fallback to a lookup for addresses in the IPv4 family. If ALL is specified, the DNS resolver will perform a lookup for both IPv4 and IPv6 families, and return all resolved addresses. When this is used, Happy Eyeballs will be enabled for upstream connections. Refer to Happy Eyeballs Support for more information. Note: This only applies to externalName clusters. See [https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/cluster/v3/cluster.proto.html#envoy-v3-api-enum-config-cluster-v3-cluster-dnslookupfamily](https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/cluster/v3/cluster.proto.html#envoy-v3-api-enum-config-cluster-v3-cluster-dnslookupfamily) for more information. Values: `auto` (default), `v4`, `v6`, `all`. Other values will produce an error. |
| `maxRequestsPerConnection` _uint32_ | _(Optional)_ Defines the maximum requests for upstream connections. If not specified, there is no limit. see [https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/core/v3/protocol.proto#envoy-v3-api-msg-config-core-v3-httpprotocoloptions](https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/core/v3/protocol.proto#envoy-v3-api-msg-config-core-v3-httpprotocoloptions) for more information. |
| `per-connection-buffer-limit-bytes` _uint32_ | _(Optional)_ Defines the soft limit on size of the cluster’s new connection read and write buffers in bytes. If unspecified, an implementation defined default is applied (1MiB). see [https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/cluster/v3/cluster.proto#envoy-v3-api-field-config-cluster-v3-cluster-per-connection-buffer-limit-bytes](https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/cluster/v3/cluster.proto#envoy-v3-api-field-config-cluster-v3-cluster-per-connection-buffer-limit-bytes) for more information. |
| `circuitBreakers` _[CircuitBreakers](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.CircuitBreakers)_ | _(Optional)_ GlobalCircuitBreakerDefaults specifies default circuit breaker budget across all services. If defined, this will be used as the default for all services. |
| `upstreamTLS` _[EnvoyTLS](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyTLS)_ | _(Optional)_ UpstreamTLS contains the TLS policy parameters for upstream connections |

### CompressionAlgorithm (`string` alias)

(_Appears on:_[EnvoyCompression](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyCompression))

CompressionAlgorithm defines the type of compression algorithm applied in default HTTP listener filter chain. Allowable values are defined as names of well known compression algorithms (plus “disabled”).

| Value | Description |
| --- | --- |
| "brotli" | BrotliCompression specifies brotli as the default HTTP filter chain compression mechanism |
| "disabled" | DisabledCompression specifies that there will be no compression in the default HTTP filter chain |
| "gzip" | GzipCompression specifies gzip as the default HTTP filter chain compression mechanism |
| "zstd" | ZstdCompression specifies zstd as the default HTTP filter chain compression mechanism |

### ContourConfigurationSpec

(_Appears on:_[ContourConfiguration](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfiguration), [ContourDeploymentSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourDeploymentSpec))

ContourConfigurationSpec represents a configuration of a Contour controller. It contains most of all the options that can be customized, the other remaining options being command line flags.

| Field | Description |
| --- | --- |
| `xdsServer` _[XDSServerConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.XDSServerConfig)_ | _(Optional)_ XDSServer contains parameters for the xDS server. |
| `ingress` _[IngressConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.IngressConfig)_ | _(Optional)_ Ingress contains parameters for ingress options. |
| `debug` _[DebugConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.DebugConfig)_ | _(Optional)_ Debug contains parameters to enable debug logging and debug interfaces inside Contour. |
| `health` _[HealthConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.HealthConfig)_ | _(Optional)_ Health defines the endpoints Contour uses to serve health checks. Contour’s default is { address: “0.0.0.0”, port: 8000 }. |
| `envoy` _[EnvoyConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyConfig)_ | _(Optional)_ Envoy contains parameters for Envoy as well as how to optionally configure a managed Envoy fleet. |
| `gateway` _[GatewayConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.GatewayConfig)_ | _(Optional)_ Gateway contains parameters for the gateway-api Gateway that Contour is configured to serve traffic. |
| `httpproxy` _[HTTPProxyConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.HTTPProxyConfig)_ | _(Optional)_ HTTPProxy defines parameters on HTTPProxy. |
| `enableExternalNameService` _bool_ | _(Optional)_ EnableExternalNameService allows processing of ExternalNameServices Contour’s default is false for security reasons. |
| `globalExtAuth` _[AuthorizationServer](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.AuthorizationServer)_ | _(Optional)_ GlobalExternalAuthorization allows envoys external authorization filter to be enabled for all virtual hosts. |
| `rateLimitService` _[RateLimitServiceConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.RateLimitServiceConfig)_ | _(Optional)_ RateLimitService optionally holds properties of the Rate Limit Service to be used for global rate limiting. |
| `policy` _[PolicyConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.PolicyConfig)_ | _(Optional)_ Policy specifies default policy applied if not overridden by the user |
| `metrics` _[MetricsConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.MetricsConfig)_ | _(Optional)_ Metrics defines the endpoint Contour uses to serve metrics. Contour’s default is { address: “0.0.0.0”, port: 8000 }. |
| `tracing` _[TracingConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.TracingConfig)_ | Tracing defines properties for exporting trace data to OpenTelemetry. |
| `featureFlags` _[FeatureFlags](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.FeatureFlags)_ | FeatureFlags defines toggle to enable new contour features. |

### ContourConfigurationStatus

(_Appears on:_[ContourConfiguration](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfiguration))

ContourConfigurationStatus defines the observed state of a ContourConfiguration resource.

| Field | Description |
| --- | --- |
| `conditions` _[[]DetailedCondition](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.DetailedCondition)_ | _(Optional)_ Conditions contains the current status of the Contour resource. Contour will update a single condition, `Valid`, that is in normal-true polarity. Contour will not modify any other Conditions set in this block, in case some other controller wants to add a Condition. |

### ContourDeploymentSpec

(_Appears on:_[ContourDeployment](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourDeployment))

ContourDeploymentSpec specifies options for how a Contour instance should be provisioned.

| Field | Description |
| --- | --- |
| `contour` _[ContourSettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourSettings)_ | _(Optional)_ Contour specifies deployment-time settings for the Contour part of the installation, i.e. the xDS server/control plane and associated resources, including things like replica count for the Deployment, and node placement constraints for the pods. |
| `envoy` _[EnvoySettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoySettings)_ | _(Optional)_ Envoy specifies deployment-time settings for the Envoy part of the installation, i.e. the xDS client/data plane and associated resources, including things like the workload type to use (DaemonSet or Deployment), node placement constraints for the pods, and various options for the Envoy service. |
| `runtimeSettings` _[ContourConfigurationSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfigurationSpec)_ | _(Optional)_ RuntimeSettings is a ContourConfiguration spec to be used when provisioning a Contour instance that will influence aspects of the Contour instance’s runtime behavior. |
| `resourceLabels` _map[string]string_ | _(Optional)_ ResourceLabels is a set of labels to add to the provisioned Contour resources. Deprecated: use Gateway.Spec.Infrastructure.Labels instead. This field will be removed in a future release. |

### ContourDeploymentStatus

(_Appears on:_[ContourDeployment](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourDeployment))

ContourDeploymentStatus defines the observed state of a ContourDeployment resource.

| Field | Description |
| --- | --- |
| `conditions` _[[]Kubernetes meta/v1.Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta)_ | _(Optional)_ Conditions describe the current conditions of the ContourDeployment resource. |

### ContourSettings

(_Appears on:_[ContourDeploymentSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourDeploymentSpec))

ContourSettings contains settings for the Contour part of the installation, i.e. the xDS server/control plane and associated resources.

| Field | Description |
| --- | --- |
| `replicas` _int32_ | _(Optional)_ Deprecated: Use `DeploymentSettings.Replicas` instead. Replicas is the desired number of Contour replicas. If if unset, defaults to 2. if both `DeploymentSettings.Replicas` and this one is set, use `DeploymentSettings.Replicas`. |
| `nodePlacement` _[NodePlacement](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.NodePlacement)_ | _(Optional)_ NodePlacement describes node scheduling configuration of Contour pods. |
| `kubernetesLogLevel` _byte_ | _(Optional)_ KubernetesLogLevel Enable Kubernetes client debug logging with log level. If unset, defaults to 0. |
| `logLevel` _[LogLevel](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.LogLevel)_ | _(Optional)_ LogLevel sets the log level for Contour Allowed values are “info”, “debug”. |
| `resources` _[Kubernetes core/v1.ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#resourcerequirements-v1-core)_ | _(Optional)_ Compute Resources required by contour container. Cannot be updated. More info: [https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) |
| `deployment` _[DeploymentSettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.DeploymentSettings)_ | _(Optional)_ Deployment describes the settings for running contour as a `Deployment`. |
| `podAnnotations` _map[string]string_ | _(Optional)_ PodAnnotations defines annotations to add to the Contour pods. the annotations for Prometheus will be appended or overwritten with predefined value. |
| `watchNamespaces` _[[]Namespace](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Namespace)_ | _(Optional)_ WatchNamespaces is an array of namespaces. Setting it will instruct the contour instance to only watch this subset of namespaces. |
| `disabledFeatures` _[[]Feature](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.Feature)_ | _(Optional)_ DisabledFeatures defines an array of resources that will be ignored by contour reconciler. |

### CustomTag

(_Appears on:_[TracingConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.TracingConfig))

CustomTag defines custom tags with unique tag name to create tags for the active span.

| Field | Description |
| --- | --- |
| `tagName` _string_ | TagName is the unique name of the custom tag. |
| `literal` _string_ | _(Optional)_ Literal is a static custom tag value. Precisely one of Literal, RequestHeaderName must be set. |
| `requestHeaderName` _string_ | _(Optional)_ RequestHeaderName indicates which request header the label value is obtained from. Precisely one of Literal, RequestHeaderName must be set. |

### DaemonSetSettings

(_Appears on:_[EnvoySettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoySettings))

DaemonSetSettings contains settings for DaemonSet resources.

| Field | Description |
| --- | --- |
| `updateStrategy` _[Kubernetes apps/v1.DaemonSetUpdateStrategy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#daemonsetupdatestrategy-v1-apps)_ | _(Optional)_ Strategy describes the deployment strategy to use to replace existing DaemonSet pods with new pods. |

### DebugConfig

(_Appears on:_[ContourConfigurationSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfigurationSpec))

DebugConfig contains Contour specific troubleshooting options.

| Field | Description |
| --- | --- |
| `address` _string_ | _(Optional)_ Defines the Contour debug address interface. Contour’s default is “127.0.0.1”. |
| `port` _int_ | _(Optional)_ Defines the Contour debug address port. Contour’s default is 6060. |

### DeploymentSettings

(_Appears on:_[ContourSettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourSettings), [EnvoySettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoySettings))

DeploymentSettings contains settings for Deployment resources.

| Field | Description |
| --- | --- |
| `replicas` _int32_ | Replicas is the desired number of replicas. |
| `strategy` _[Kubernetes apps/v1.DeploymentStrategy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#deploymentstrategy-v1-apps)_ | _(Optional)_ Strategy describes the deployment strategy to use to replace existing pods with new pods. |

### EnvoyCompression

(_Appears on:_[EnvoyListenerConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyListenerConfig))

EnvoyCompression defines configuration related to compression in the default HTTP Listener filter chain.

| Field | Description |
| --- | --- |
| `algorithm` _[CompressionAlgorithm](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.CompressionAlgorithm)_ | _(Optional)_ Algorithm selects the response compression type applied in the compression HTTP filter of the default Listener filters. Values: `gzip` (default), `brotli`, `zstd`, `disabled`. Setting this to `disabled` will make Envoy skip “Accept-Encoding: gzip,deflate” request header and always return uncompressed response. |

### EnvoyConfig

(_Appears on:_[ContourConfigurationSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfigurationSpec))

EnvoyConfig defines how Envoy is to be Configured from Contour.

| Field | Description |
| --- | --- |
| `listener` _[EnvoyListenerConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyListenerConfig)_ | _(Optional)_ Listener hold various configurable Envoy listener values. |
| `service` _[NamespacedName](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.NamespacedName)_ | _(Optional)_ Service holds Envoy service parameters for setting Ingress status. Contour’s default is { namespace: “projectcontour”, name: “envoy” }. |
| `http` _[EnvoyListener](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyListener)_ | _(Optional)_ Defines the HTTP Listener for Envoy. Contour’s default is { address: “0.0.0.0”, port: 8080, accessLog: “/dev/stdout” }. |
| `https` _[EnvoyListener](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyListener)_ | _(Optional)_ Defines the HTTPS Listener for Envoy. Contour’s default is { address: “0.0.0.0”, port: 8443, accessLog: “/dev/stdout” }. |
| `health` _[HealthConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.HealthConfig)_ | _(Optional)_ Health defines the endpoint Envoy uses to serve health checks. Contour’s default is { address: “0.0.0.0”, port: 8002 }. |
| `metrics` _[MetricsConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.MetricsConfig)_ | _(Optional)_ Metrics defines the endpoint Envoy uses to serve metrics. Contour’s default is { address: “0.0.0.0”, port: 8002 }. |
| `clientCertificate` _[NamespacedName](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.NamespacedName)_ | _(Optional)_ ClientCertificate defines the namespace/name of the Kubernetes secret containing the client certificate and private key to be used when establishing TLS connection to upstream cluster. |
| `logging` _[EnvoyLogging](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyLogging)_ | _(Optional)_ Logging defines how Envoy’s logs can be configured. |
| `defaultHTTPVersions` _[[]HTTPVersionType](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.HTTPVersionType)_ | _(Optional)_ DefaultHTTPVersions defines the default set of HTTPS versions the proxy should accept. HTTP versions are strings of the form “HTTP/xx”. Supported versions are “HTTP/1.1” and “HTTP/2”. Values: `HTTP/1.1`, `HTTP/2` (default: both). Other values will produce an error. |
| `timeouts` _[TimeoutParameters](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.TimeoutParameters)_ | _(Optional)_ Timeouts holds various configurable timeouts that can be set in the config file. |
| `cluster` _[ClusterParameters](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ClusterParameters)_ | _(Optional)_ Cluster holds various configurable Envoy cluster values that can be set in the config file. |
| `network` _[NetworkParameters](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.NetworkParameters)_ | _(Optional)_ Network holds various configurable Envoy network values. |
| `omEnforcedHealth` _[HealthConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.HealthConfig)_ | _(Optional)_ OMEnforcedHealth defines the endpoint Envoy uses to serve health checks with the envoy overload manager actions, such as global connection limits, enforced. The configured values must be different from the endpoints configured by [EnvoyConfig.Metrics] and [EnvoyConfig.Health] This is disabled by default |

### EnvoyListener

(_Appears on:_[EnvoyConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyConfig))

EnvoyListener defines parameters for an Envoy Listener.

| Field | Description |
| --- | --- |
| `address` _string_ | _(Optional)_ Defines an Envoy Listener Address. |
| `port` _int_ | _(Optional)_ Defines an Envoy listener Port. |
| `accessLog` _string_ | _(Optional)_ AccessLog defines where Envoy logs are outputted for this listener. |

### EnvoyListenerConfig

(_Appears on:_[EnvoyConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyConfig))

EnvoyListenerConfig hold various configurable Envoy listener values.

| Field | Description |
| --- | --- |
| `useProxyProtocol` _bool_ | _(Optional)_ Use PROXY protocol for all listeners. Contour’s default is false. |
| `compression` _[EnvoyCompression](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyCompression)_ | _(Optional)_ Compression defines configuration related to compression in the default HTTP Listener filters. |
| `disableAllowChunkedLength` _bool_ | _(Optional)_ DisableAllowChunkedLength disables the RFC-compliant Envoy behavior to strip the “Content-Length” header if “Transfer-Encoding: chunked” is also set. This is an emergency off-switch to revert back to Envoy’s default behavior in case of failures. Please file an issue if failures are encountered. See: [https://github.com/projectcontour/contour/issues/3221](https://github.com/projectcontour/contour/issues/3221) Contour’s default is false. |
| `disableMergeSlashes` _bool_ | _(Optional)_ DisableMergeSlashes disables Envoy’s non-standard merge_slashes path transformation option which strips duplicate slashes from request URL paths. Contour’s default is false. |
| `serverHeaderTransformation` _[ServerHeaderTransformationType](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ServerHeaderTransformationType)_ | _(Optional)_ Defines the action to be applied to the Server header on the response path. When configured as overwrite, overwrites any Server header with “envoy”. When configured as append_if_absent, if a Server header is present, pass it through, otherwise set it to “envoy”. When configured as pass_through, pass through the value of the Server header, and do not append a header if none is present. Values: `overwrite` (default), `append_if_absent`, `pass_through` Other values will produce an error. Contour’s default is overwrite. |
| `connectionBalancer` _string_ | _(Optional)_ ConnectionBalancer. If the value is exact, the listener will use the exact connection balancer See [https://www.envoyproxy.io/docs/envoy/latest/api-v2/api/v2/listener.proto#envoy-api-msg-listener-connectionbalanceconfig](https://www.envoyproxy.io/docs/envoy/latest/api-v2/api/v2/listener.proto#envoy-api-msg-listener-connectionbalanceconfig) for more information. Values: (empty string): use the default ConnectionBalancer, `exact`: use the Exact ConnectionBalancer. Other values will produce an error. |
| `maxRequestsPerConnection` _uint32_ | _(Optional)_ Defines the maximum requests for downstream connections. If not specified, there is no limit. see [https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/core/v3/protocol.proto#envoy-v3-api-msg-config-core-v3-httpprotocoloptions](https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/core/v3/protocol.proto#envoy-v3-api-msg-config-core-v3-httpprotocoloptions) for more information. |
| `per-connection-buffer-limit-bytes` _uint32_ | _(Optional)_ Defines the soft limit on size of the listener’s new connection read and write buffers in bytes. If unspecified, an implementation defined default is applied (1MiB). see [https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/listener/v3/listener.proto#envoy-v3-api-field-config-listener-v3-listener-per-connection-buffer-limit-bytes](https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/listener/v3/listener.proto#envoy-v3-api-field-config-listener-v3-listener-per-connection-buffer-limit-bytes) for more information. |
| `tls` _[EnvoyTLS](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyTLS)_ | _(Optional)_ TLS holds various configurable Envoy TLS listener values. |
| `socketOptions` _[SocketOptions](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.SocketOptions)_ | _(Optional)_ SocketOptions defines configurable socket options for the listeners. Single set of options are applied to all listeners. |
| `maxRequestsPerIOCycle` _uint32_ | _(Optional)_ Defines the limit on number of HTTP requests that Envoy will process from a single connection in a single I/O cycle. Requests over this limit are processed in subsequent I/O cycles. Can be used as a mitigation for CVE-2023-44487 when abusive traffic is detected. Configures the http.max_requests_per_io_cycle Envoy runtime setting. The default value when this is not set is no limit. |
| `httpMaxConcurrentStreams` _uint32_ | _(Optional)_ Defines the value for SETTINGS_MAX_CONCURRENT_STREAMS Envoy will advertise in the SETTINGS frame in HTTP/2 connections and the limit for concurrent streams allowed for a peer on a single HTTP/2 connection. It is recommended to not set this lower than 100 but this field can be used to bound resource usage by HTTP/2 connections and mitigate attacks like CVE-2023-44487. The default value when this is not set is unlimited. |
| `maxConnectionsPerListener` _uint32_ | _(Optional)_ Defines the limit on number of active connections to a listener. The limit is applied per listener. The default value when this is not set is unlimited. |

### EnvoyLogging

(_Appears on:_[EnvoyConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyConfig))

EnvoyLogging defines how Envoy’s logs can be configured.

| Field | Description |
| --- | --- |
| `accessLogFormat` _[AccessLogType](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.AccessLogType)_ | _(Optional)_ AccessLogFormat sets the global access log format. Values: `envoy` (default), `json`. Other values will produce an error. |
| `accessLogFormatString` _string_ | _(Optional)_ AccessLogFormatString sets the access log format when format is set to `envoy`. When empty, Envoy’s default format is used. |
| `accessLogJSONFields` _[AccessLogJSONFields](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.AccessLogJSONFields)_ | _(Optional)_ AccessLogJSONFields sets the fields that JSON logging will output when AccessLogFormat is json. |
| `accessLogLevel` _[AccessLogLevel](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.AccessLogLevel)_ | _(Optional)_ AccessLogLevel sets the verbosity level of the access log. Values: `info` (default, all requests are logged), `error` (all non-success requests, i.e. 300+ response code, are logged), `critical` (all 5xx requests are logged) and `disabled`. Other values will produce an error. |

### EnvoySettings

(_Appears on:_[ContourDeploymentSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourDeploymentSpec))

EnvoySettings contains settings for the Envoy part of the installation, i.e. the xDS client/data plane and associated resources.

| Field | Description |
| --- | --- |
| `workloadType` _[WorkloadType](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.WorkloadType)_ | _(Optional)_ WorkloadType is the type of workload to install Envoy as. Choices are DaemonSet and Deployment. If unset, defaults to DaemonSet. |
| `replicas` _int32_ | _(Optional)_ Deprecated: Use `DeploymentSettings.Replicas` instead. Replicas is the desired number of Envoy replicas. If WorkloadType is not “Deployment”, this field is ignored. Otherwise, if unset, defaults to 2. if both `DeploymentSettings.Replicas` and this one is set, use `DeploymentSettings.Replicas`. |
| `networkPublishing` _[NetworkPublishing](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.NetworkPublishing)_ | NetworkPublishing defines how to expose Envoy to a network. |
| `nodePlacement` _[NodePlacement](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.NodePlacement)_ | _(Optional)_ NodePlacement describes node scheduling configuration of Envoy pods. |
| `extraVolumes` _[[]Kubernetes core/v1.Volume](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#volume-v1-core)_ | _(Optional)_ ExtraVolumes holds the extra volumes to add. |
| `extraVolumeMounts` _[[]Kubernetes core/v1.VolumeMount](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#volumemount-v1-core)_ | _(Optional)_ ExtraVolumeMounts holds the extra volume mounts to add (normally used with extraVolumes). |
| `podAnnotations` _map[string]string_ | _(Optional)_ PodAnnotations defines annotations to add to the Envoy pods. the annotations for Prometheus will be appended or overwritten with predefined value. |
| `resources` _[Kubernetes core/v1.ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#resourcerequirements-v1-core)_ | _(Optional)_ Compute Resources required by envoy container. Cannot be updated. More info: [https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) |
| `logLevel` _[LogLevel](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.LogLevel)_ | _(Optional)_ LogLevel sets the log level for Envoy. Allowed values are “trace”, “debug”, “info”, “warn”, “error”, “critical”, “off”. |
| `daemonSet` _[DaemonSetSettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.DaemonSetSettings)_ | _(Optional)_ DaemonSet describes the settings for running envoy as a `DaemonSet`. if `WorkloadType` is `Deployment`,it’s must be nil |
| `deployment` _[DeploymentSettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.DeploymentSettings)_ | _(Optional)_ Deployment describes the settings for running envoy as a `Deployment`. if `WorkloadType` is `DaemonSet`,it’s must be nil |
| `baseID` _int32_ | _(Optional)_ The base ID to use when allocating shared memory regions. if Envoy needs to be run multiple times on the same machine, each running Envoy will need a unique base ID so that the shared memory regions do not conflict. defaults to 0. |
| `overloadMaxHeapSize` _uint64_ | _(Optional)_ OverloadMaxHeapSize defines the maximum heap memory of the envoy controlled by the overload manager. When the value is greater than 0, the overload manager is enabled, and when envoy reaches 95% of the maximum heap size, it performs a shrink heap operation, When it reaches 98% of the maximum heap size, Envoy Will stop accepting requests. More info: [https://projectcontour.io/docs/main/config/overload-manager/](https://projectcontour.io/docs/main/config/overload-manager/) |
| `overloadMaxDownstreamConnections` _uint64_ | _(Optional)_ OverloadMaxDownstreamConn defines the envoy global downstream connection limit controlled by the overload manager. When the value is greater than 0 the overload manager is enabled and listeners will begin rejecting connections when the the connection threshold is hit. Metrics and health listeners are not subject to the connection limits, however, they still count against the global limit. |

### EnvoyTLS

(_Appears on:_[ClusterParameters](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ClusterParameters), [EnvoyListenerConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyListenerConfig))

EnvoyTLS describes tls parameters for Envoy listneners.

| Field | Description |
| --- | --- |
| `minimumProtocolVersion` _string_ | _(Optional)_ MinimumProtocolVersion is the minimum TLS version this vhost should negotiate. Values: `1.2` (default), `1.3`. Other values will produce an error. |
| `maximumProtocolVersion` _string_ | _(Optional)_ MaximumProtocolVersion is the maximum TLS version this vhost should negotiate. Values: `1.2`, `1.3`(default). Other values will produce an error. |
| `cipherSuites` _[]string_ | _(Optional)_ CipherSuites defines the TLS ciphers to be supported by Envoy TLS listeners when negotiating TLS 1.2. Ciphers are validated against the set that Envoy supports by default. This parameter should only be used by advanced users. Note that these will be ignored when TLS 1.3 is in use. This field is optional; when it is undefined, a Contour-managed ciphersuite list will be used, which may be updated to keep it secure. Contour’s default list is: - “[ECDHE-ECDSA-AES128-GCM-SHA256|ECDHE-ECDSA-CHACHA20-POLY1305]” - “[ECDHE-RSA-AES128-GCM-SHA256|ECDHE-RSA-CHACHA20-POLY1305]” - “ECDHE-ECDSA-AES256-GCM-SHA384” - “ECDHE-RSA-AES256-GCM-SHA384” Ciphers provided are validated against the following list: - “[ECDHE-ECDSA-AES128-GCM-SHA256|ECDHE-ECDSA-CHACHA20-POLY1305]” - “[ECDHE-RSA-AES128-GCM-SHA256|ECDHE-RSA-CHACHA20-POLY1305]” - “ECDHE-ECDSA-AES128-GCM-SHA256” - “ECDHE-RSA-AES128-GCM-SHA256” - “ECDHE-ECDSA-AES128-SHA” - “ECDHE-RSA-AES128-SHA” - “AES128-GCM-SHA256” - “AES128-SHA” - “ECDHE-ECDSA-AES256-GCM-SHA384” - “ECDHE-RSA-AES256-GCM-SHA384” - “ECDHE-ECDSA-AES256-SHA” - “ECDHE-RSA-AES256-SHA” - “AES256-GCM-SHA384” - “AES256-SHA” Contour recommends leaving this undefined unless you are sure you must. See: [https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/transport_sockets/tls/v3/common.proto#extensions-transport-sockets-tls-v3-tlsparameters](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/transport_sockets/tls/v3/common.proto#extensions-transport-sockets-tls-v3-tlsparameters) Note: This list is a superset of what is valid for stock Envoy builds and those using BoringSSL FIPS. |

### ExtensionProtocolVersion (`string` alias)

(_Appears on:_[ExtensionServiceSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ExtensionServiceSpec))

ExtensionProtocolVersion is the version of the GRPC protocol used to access extension services. The only version currently supported is “v3”.

| Value | Description |
| --- | --- |
| "v2" | SupportProtocolVersion2 requests the “v2” support protocol version. Deprecated: this protocol version is no longer supported and the constant is retained for backwards compatibility only. |
| "v3" | SupportProtocolVersion3 requests the “v3” support protocol version. |

### ExtensionServiceSpec

(_Appears on:_[ExtensionService](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ExtensionService))

ExtensionServiceSpec defines the desired state of an ExtensionService resource.

| Field | Description |
| --- | --- |
| `services` _[[]ExtensionServiceTarget](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ExtensionServiceTarget)_ | Services specifies the set of Kubernetes Service resources that receive GRPC extension API requests. If no weights are specified for any of the entries in this array, traffic will be spread evenly across all the services. Otherwise, traffic is balanced proportionally to the Weight field in each entry. |
| `validation` _[UpstreamValidation](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.UpstreamValidation)_ | _(Optional)_ UpstreamValidation defines how to verify the backend service’s certificate |
| `protocol` _string_ | _(Optional)_ Protocol may be used to specify (or override) the protocol used to reach this Service. Values may be h2 or h2c. If omitted, protocol-selection falls back on Service annotations. |
| `loadBalancerPolicy` _[LoadBalancerPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.LoadBalancerPolicy)_ | _(Optional)_ The policy for load balancing GRPC service requests. Note that the `Cookie` and `RequestHash` load balancing strategies cannot be used here. |
| `timeoutPolicy` _[TimeoutPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.TimeoutPolicy)_ | _(Optional)_ The timeout policy for requests to the services. |
| `protocolVersion` _[ExtensionProtocolVersion](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ExtensionProtocolVersion)_ | _(Optional)_ This field sets the version of the GRPC protocol that Envoy uses to send requests to the extension service. Since Contour always uses the v3 Envoy API, this is currently fixed at “v3”. However, other protocol options will be available in future. |
| `circuitBreakerPolicy` _[CircuitBreakers](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.CircuitBreakers)_ | _(Optional)_ CircuitBreakerPolicy specifies the circuit breaker budget across the extension service. If defined this overrides the global circuit breaker budget. |

### ExtensionServiceStatus

(_Appears on:_[ExtensionService](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ExtensionService))

ExtensionServiceStatus defines the observed state of an ExtensionService resource.

| Field | Description |
| --- | --- |
| `conditions` _[[]DetailedCondition](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.DetailedCondition)_ | _(Optional)_ Conditions contains the current status of the ExtensionService resource. Contour will update a single condition, `Valid`, that is in normal-true polarity. Contour will not modify any other Conditions set in this block, in case some other controller wants to add a Condition. |

### ExtensionServiceTarget

(_Appears on:_[ExtensionServiceSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ExtensionServiceSpec))

ExtensionServiceTarget defines an Kubernetes Service to target with extension service traffic.

| Field | Description |
| --- | --- |
| `name` _string_ | Name is the name of Kubernetes service that will accept service traffic. |
| `port` _int_ | Port (defined as Integer) to proxy traffic to since a service can have multiple defined. |
| `weight` _uint32_ | _(Optional)_ Weight defines proportion of traffic to balance to the Kubernetes Service. |

### FeatureFlags (`[]string` alias)

(_Appears on:_[ContourConfigurationSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfigurationSpec))

FeatureFlags defines the set of feature flags to toggle new contour features.

### GatewayConfig

(_Appears on:_[ContourConfigurationSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfigurationSpec))

GatewayConfig holds the config for Gateway API controllers.

| Field | Description |
| --- | --- |
| `gatewayRef` _[NamespacedName](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.NamespacedName)_ | GatewayRef defines the specific Gateway that this Contour instance corresponds to. |

### HTTPProxyConfig

(_Appears on:_[ContourConfigurationSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfigurationSpec))

HTTPProxyConfig defines parameters on HTTPProxy.

| Field | Description |
| --- | --- |
| `disablePermitInsecure` _bool_ | _(Optional)_ DisablePermitInsecure disables the use of the permitInsecure field in HTTPProxy. Contour’s default is false. |
| `rootNamespaces` _[]string_ | _(Optional)_ Restrict Contour to searching these namespaces for root ingress routes. |
| `fallbackCertificate` _[NamespacedName](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.NamespacedName)_ | _(Optional)_ FallbackCertificate defines the namespace/name of the Kubernetes secret to use as fallback when a non-SNI request is received. |

### HTTPVersionType (`string` alias)

(_Appears on:_[EnvoyConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyConfig))

HTTPVersionType is the name of a supported HTTP version.

| Value | Description |
| --- | --- |
| "HTTP/1.1" | HTTPVersion1 is the name of the HTTP/1.1 version. |
| "HTTP/2" | HTTPVersion2 is the name of the HTTP/2 version. |

(_Appears on:_[PolicyConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.PolicyConfig))

| Field | Description |
| --- | --- |
| `set` _map[string]string_ | _(Optional)_ |
| `remove` _[]string_ | _(Optional)_ |

### HealthConfig

(_Appears on:_[ContourConfigurationSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfigurationSpec), [EnvoyConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyConfig))

HealthConfig defines the endpoints to enable health checks.

| Field | Description |
| --- | --- |
| `address` _string_ | _(Optional)_ Defines the health address interface. |
| `port` _int_ | _(Optional)_ Defines the health port. |

### IngressConfig

(_Appears on:_[ContourConfigurationSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfigurationSpec))

IngressConfig defines ingress specific config items.

| Field | Description |
| --- | --- |
| `classNames` _[]string_ | _(Optional)_ Ingress Class Names Contour should use. |
| `statusAddress` _string_ | _(Optional)_ Address to set in Ingress object status. |

### LogLevel (`string` alias)

(_Appears on:_[ContourSettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourSettings), [EnvoySettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoySettings))

LogLevel is the logging levels available.

| Value | Description |
| --- | --- |
| "critical" | CriticalLog sets the log level for Envoy to `critical`. |
| "debug" | DebugLog sets the log level for Contour/Envoy to `debug`. |
| "error" | ErrorLog sets the log level for Envoy to `error`. |
| "info" | InfoLog sets the log level for Contour/Envoy to `info`. |
| "off" | OffLog disable logging for Envoy. |
| "trace" | TraceLog sets the log level for Envoy to `trace`. |
| "warn" | WarnLog sets the log level for Envoy to `warn`. |

### MetricsConfig

(_Appears on:_[ContourConfigurationSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfigurationSpec), [EnvoyConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyConfig))

MetricsConfig defines the metrics endpoint.

| Field | Description |
| --- | --- |
| `address` _string_ | _(Optional)_ Defines the metrics address interface. |
| `port` _int_ | _(Optional)_ Defines the metrics port. |
| `tls` _[MetricsTLS](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.MetricsTLS)_ | _(Optional)_ TLS holds TLS file config details. Metrics and health endpoints cannot have same port number when metrics is served over HTTPS. |

### MetricsTLS

(_Appears on:_[MetricsConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.MetricsConfig))

TLS holds TLS file config details.

| Field | Description |
| --- | --- |
| `caFile` _string_ | _(Optional)_ CA filename. |
| `certFile` _string_ | _(Optional)_ Client certificate filename. |
| `keyFile` _string_ | _(Optional)_ Client key filename. |

### NamespacedName

(_Appears on:_[EnvoyConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyConfig), [GatewayConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.GatewayConfig), [HTTPProxyConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.HTTPProxyConfig), [RateLimitServiceConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.RateLimitServiceConfig), [TracingConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.TracingConfig))

NamespacedName defines the namespace/name of the Kubernetes resource referred from the config file. Used for Contour config YAML file parsing, otherwise we could use K8s types.NamespacedName.

| Field | Description |
| --- | --- |
| `name` _string_ |  |
| `namespace` _string_ |  |

### NetworkParameters

(_Appears on:_[EnvoyConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyConfig))

NetworkParameters hold various configurable network values.

| Field | Description |
| --- | --- |
| `numTrustedHops` _uint32_ | _(Optional)_ XffNumTrustedHops defines the number of additional ingress proxy hops from the right side of the x-forwarded-for HTTP header to trust when determining the origin client’s IP address. See [https://www.envoyproxy.io/docs/envoy/v1.17.0/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto?highlight=xff_num_trusted_hops](https://www.envoyproxy.io/docs/envoy/v1.17.0/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto?highlight=xff_num_trusted_hops) for more information. Contour’s default is 0. |
| `adminPort` _int_ | _(Optional)_ Configure the port used to access the Envoy Admin interface. If configured to port “0” then the admin interface is disabled. Contour’s default is 9001. |
| `stripTrailingHostDot` _bool_ | _(Optional)_ EnvoyStripTrailingHostDot defines if trailing dot of the host should be removed from host/authority header before any processing of request by HTTP filters or routing. This affects the upstream host header. Without setting this option to true, incoming requests with host example.com. will not match against route with domains match set to example.com. See [https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto?highlight=strip_trailing_host_dot](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto?highlight=strip_trailing_host_dot) for more information. Contour’s default is false. |

### NetworkPublishing

(_Appears on:_[EnvoySettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoySettings))

NetworkPublishing defines the schema for publishing to a network.

| Field | Description |
| --- | --- |
| `type` _[NetworkPublishingType](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.NetworkPublishingType)_ | _(Optional)_ NetworkPublishingType is the type of publishing strategy to use. Valid values are: *LoadBalancerService In this configuration, network endpoints for Envoy use container networking. A Kubernetes LoadBalancer Service is created to publish Envoy network endpoints. See: [https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer)* NodePortService Publishes Envoy network endpoints using a Kubernetes NodePort Service. In this configuration, Envoy network endpoints use container networking. A Kubernetes NodePort Service is created to publish the network endpoints. See: [https://kubernetes.io/docs/concepts/services-networking/service/#nodeport](https://kubernetes.io/docs/concepts/services-networking/service/#nodeport) NOTE: When provisioning an Envoy `NodePortService`, use Gateway Listeners’ port numbers to populate the Service’s node port values, there’s no way to auto-allocate them. See: [https://github.com/projectcontour/contour/issues/4499](https://github.com/projectcontour/contour/issues/4499) * ClusterIPService Publishes Envoy network endpoints using a Kubernetes ClusterIP Service. In this configuration, Envoy network endpoints use container networking. A Kubernetes ClusterIP Service is created to publish the network endpoints. See: [https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types) If unset, defaults to LoadBalancerService. |
| `externalTrafficPolicy` _[Kubernetes core/v1.ServiceExternalTrafficPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#serviceexternaltrafficpolicy-v1-core)_ | _(Optional)_ ExternalTrafficPolicy describes how nodes distribute service traffic they receive on one of the Service’s “externally-facing” addresses (NodePorts, ExternalIPs, and LoadBalancer IPs). If unset, defaults to “Local”. |
| `ipFamilyPolicy` _[Kubernetes core/v1.IPFamilyPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#ipfamilypolicy-v1-core)_ | _(Optional)_ IPFamilyPolicy represents the dual-stack-ness requested or required by this Service. If there is no value provided, then this field will be set to SingleStack. Services can be “SingleStack” (a single IP family), “PreferDualStack” (two IP families on dual-stack configured clusters or a single IP family on single-stack clusters), or “RequireDualStack” (two IP families on dual-stack configured clusters, otherwise fail). |
| `serviceAnnotations` _map[string]string_ | _(Optional)_ ServiceAnnotations is the annotations to add to the provisioned Envoy service. |

### NetworkPublishingType (`string` alias)

(_Appears on:_[NetworkPublishing](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.NetworkPublishing))

NetworkPublishingType is a way to publish network endpoints.

| Value | Description |
| --- | --- |
| "ClusterIPService" | ClusterIPServicePublishingType publishes a network endpoint using a Kubernetes ClusterIP Service. |
| "LoadBalancerService" | LoadBalancerServicePublishingType publishes a network endpoint using a Kubernetes LoadBalancer Service. |
| "NodePortService" | NodePortServicePublishingType publishes a network endpoint using a Kubernetes NodePort Service. |

### NodePlacement

(_Appears on:_[ContourSettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourSettings), [EnvoySettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoySettings))

NodePlacement describes node scheduling configuration for pods. If nodeSelector and tolerations are specified, the scheduler will use both to determine where to place the pod(s).

| Field | Description |
| --- | --- |
| `nodeSelector` _map[string]string_ | _(Optional)_ NodeSelector is the simplest recommended form of node selection constraint and specifies a map of key-value pairs. For the pod to be eligible to run on a node, the node must have each of the indicated key-value pairs as labels (it can have additional labels as well). If unset, the pod(s) will be scheduled to any available node. |
| `tolerations` _[[]Kubernetes core/v1.Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#toleration-v1-core)_ | _(Optional)_ Tolerations work with taints to ensure that pods are not scheduled onto inappropriate nodes. One or more taints are applied to a node; this marks that the node should not accept any pods that do not tolerate the taints. The default is an empty list. See [https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/) for additional details. |

### PolicyConfig

(_Appears on:_[ContourConfigurationSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfigurationSpec))

PolicyConfig holds default policy used if not explicitly set by the user

| Field | Description |
| --- | --- |
| `requestHeaders` _[HeadersPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.HeadersPolicy)_ | _(Optional)_ RequestHeadersPolicy defines the request headers set/removed on all routes |
| `responseHeaders` _[HeadersPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.HeadersPolicy)_ | _(Optional)_ ResponseHeadersPolicy defines the response headers set/removed on all routes |
| `applyToIngress` _bool_ | _(Optional)_ ApplyToIngress determines if the Policies will apply to ingress objects Contour’s default is false. |

### RateLimitServiceConfig

(_Appears on:_[ContourConfigurationSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfigurationSpec))

RateLimitServiceConfig defines properties of a global Rate Limit Service.

| Field | Description |
| --- | --- |
| `extensionService` _[NamespacedName](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.NamespacedName)_ | ExtensionService identifies the extension service defining the RLS. |
| `domain` _string_ | _(Optional)_ Domain is passed to the Rate Limit Service. |
| `failOpen` _bool_ | _(Optional)_ FailOpen defines whether to allow requests to proceed when the Rate Limit Service fails to respond with a valid rate limit decision within the timeout defined on the extension service. |
| `enableXRateLimitHeaders` _bool_ | _(Optional)_ EnableXRateLimitHeaders defines whether to include the X-RateLimit headers X-RateLimit-Limit, X-RateLimit-Remaining, and X-RateLimit-Reset (as defined by the IETF Internet-Draft linked below), on responses to clients when the Rate Limit Service is consulted for a request. ref. [https://tools.ietf.org/id/draft-polli-ratelimit-headers-03.html](https://tools.ietf.org/id/draft-polli-ratelimit-headers-03.html) |
| `enableResourceExhaustedCode` _bool_ | _(Optional)_ EnableResourceExhaustedCode enables translating error code 429 to grpc code RESOURCE_EXHAUSTED. When disabled it’s translated to UNAVAILABLE |
| `defaultGlobalRateLimitPolicy` _[GlobalRateLimitPolicy](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1.GlobalRateLimitPolicy)_ | _(Optional)_ DefaultGlobalRateLimitPolicy allows setting a default global rate limit policy for every HTTPProxy. HTTPProxy can overwrite this configuration. |

(_Appears on:_[EnvoyListenerConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyListenerConfig))

ServerHeaderTransformation defines the action to be applied to the Server header on the response path

| Value | Description |
| --- | --- |
| "append_if_absent" | If no Server header is present, set it to “envoy”. If a Server header is present, pass it through. |
| "overwrite" | Overwrite any Server header with “envoy”. This is the default value. |
| "pass_through" | Pass through the value of the Server header, and do not append a header if none is present. |

### SocketOptions

(_Appears on:_[EnvoyListenerConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyListenerConfig))

SocketOptions defines configurable socket options for Envoy listeners.

| Field | Description |
| --- | --- |
| `tos` _int32_ | _(Optional)_ Defines the value for IPv4 TOS field (including 6 bit DSCP field) for IP packets originating from Envoy listeners. Single value is applied to all listeners. If listeners are bound to IPv6-only addresses, setting this option will cause an error. |
| `trafficClass` _int32_ | _(Optional)_ Defines the value for IPv6 Traffic Class field (including 6 bit DSCP field) for IP packets originating from the Envoy listeners. Single value is applied to all listeners. If listeners are bound to IPv4-only addresses, setting this option will cause an error. |

### TLS

(_Appears on:_[XDSServerConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.XDSServerConfig))

TLS holds TLS file config details.

| Field | Description |
| --- | --- |
| `caFile` _string_ | _(Optional)_ CA filename. |
| `certFile` _string_ | _(Optional)_ Client certificate filename. |
| `keyFile` _string_ | _(Optional)_ Client key filename. |
| `insecure` _bool_ | _(Optional)_ Allow serving the xDS gRPC API without TLS. |

### TimeoutParameters

(_Appears on:_[EnvoyConfig](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoyConfig))

TimeoutParameters holds various configurable proxy timeout values.

| Field | Description |
| --- | --- |
| `requestTimeout` _string_ | _(Optional)_ RequestTimeout sets the client request timeout globally for Contour. Note that this is a timeout for the entire request, not an idle timeout. Omit or set to “infinity” to disable the timeout entirely. See [https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto#envoy-v3-api-field-extensions-filters-network-http-connection-manager-v3-httpconnectionmanager-request-timeout](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto#envoy-v3-api-field-extensions-filters-network-http-connection-manager-v3-httpconnectionmanager-request-timeout) for more information. |
| `connectionIdleTimeout` _string_ | _(Optional)_ ConnectionIdleTimeout defines how long the proxy should wait while there are no active requests (for HTTP/1.1) or streams (for HTTP/2) before terminating an HTTP connection. Set to “infinity” to disable the timeout entirely. See [https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/core/v3/protocol.proto#envoy-v3-api-field-config-core-v3-httpprotocoloptions-idle-timeout](https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/core/v3/protocol.proto#envoy-v3-api-field-config-core-v3-httpprotocoloptions-idle-timeout) for more information. |
| `streamIdleTimeout` _string_ | _(Optional)_ StreamIdleTimeout defines how long the proxy should wait while there is no request activity (for HTTP/1.1) or stream activity (for HTTP/2) before terminating the HTTP request or stream. Set to “infinity” to disable the timeout entirely. See [https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto#envoy-v3-api-field-extensions-filters-network-http-connection-manager-v3-httpconnectionmanager-stream-idle-timeout](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto#envoy-v3-api-field-extensions-filters-network-http-connection-manager-v3-httpconnectionmanager-stream-idle-timeout) for more information. |
| `maxConnectionDuration` _string_ | _(Optional)_ MaxConnectionDuration defines the maximum period of time after an HTTP connection has been established from the client to the proxy before it is closed by the proxy, regardless of whether there has been activity or not. Omit or set to “infinity” for no max duration. See [https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/core/v3/protocol.proto#envoy-v3-api-field-config-core-v3-httpprotocoloptions-max-connection-duration](https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/core/v3/protocol.proto#envoy-v3-api-field-config-core-v3-httpprotocoloptions-max-connection-duration) for more information. |
| `delayedCloseTimeout` _string_ | _(Optional)_ DelayedCloseTimeout defines how long envoy will wait, once connection close processing has been initiated, for the downstream peer to close the connection before Envoy closes the socket associated with the connection. Setting this timeout to ‘infinity’ will disable it, equivalent to setting it to ‘0’ in Envoy. Leaving it unset will result in the Envoy default value being used. See [https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto#envoy-v3-api-field-extensions-filters-network-http-connection-manager-v3-httpconnectionmanager-delayed-close-timeout](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto#envoy-v3-api-field-extensions-filters-network-http-connection-manager-v3-httpconnectionmanager-delayed-close-timeout) for more information. |
| `connectionShutdownGracePeriod` _string_ | _(Optional)_ ConnectionShutdownGracePeriod defines how long the proxy will wait between sending an initial GOAWAY frame and a second, final GOAWAY frame when terminating an HTTP/2 connection. During this grace period, the proxy will continue to respond to new streams. After the final GOAWAY frame has been sent, the proxy will refuse new streams. See [https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto#envoy-v3-api-field-extensions-filters-network-http-connection-manager-v3-httpconnectionmanager-drain-timeout](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto#envoy-v3-api-field-extensions-filters-network-http-connection-manager-v3-httpconnectionmanager-drain-timeout) for more information. |
| `connectTimeout` _string_ | _(Optional)_ ConnectTimeout defines how long the proxy should wait when establishing connection to upstream service. If not set, a default value of 2 seconds will be used. See [https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/cluster/v3/cluster.proto#envoy-v3-api-field-config-cluster-v3-cluster-connect-timeout](https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/cluster/v3/cluster.proto#envoy-v3-api-field-config-cluster-v3-cluster-connect-timeout) for more information. |

### TracingConfig

(_Appears on:_[ContourConfigurationSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfigurationSpec))

TracingConfig defines properties for exporting trace data to OpenTelemetry.

| Field | Description |
| --- | --- |
| `includePodDetail` _bool_ | _(Optional)_ IncludePodDetail defines a flag. If it is true, contour will add the pod name and namespace to the span of the trace. the default is true. Note: The Envoy pods MUST have the HOSTNAME and CONTOUR_NAMESPACE environment variables set for this to work properly. |
| `serviceName` _string_ | ServiceName defines the name for the service. contour’s default is contour. |
| `overallSampling` _string_ | _(Optional)_ OverallSampling defines the sampling rate of trace data. contour’s default is 100. |
| `maxPathTagLength` _uint32_ | _(Optional)_ MaxPathTagLength defines maximum length of the request path to extract and include in the HttpUrl tag. contour’s default is 256. |
| `customTags` _[[]CustomTag](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.CustomTag)_ | _(Optional)_ CustomTags defines a list of custom tags with unique tag name. |
| `extensionService` _[NamespacedName](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.NamespacedName)_ | ExtensionService identifies the extension service defining the otel-collector. |

### WorkloadType (`string` alias)

(_Appears on:_[EnvoySettings](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.EnvoySettings))

WorkloadType is the type of Kubernetes workload to use for a component.

### XDSServerConfig

(_Appears on:_[ContourConfigurationSpec](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.ContourConfigurationSpec))

XDSServerConfig holds the config for the Contour xDS server.

| Field | Description |
| --- | --- |
| `address` _string_ | _(Optional)_ Defines the xDS gRPC API address which Contour will serve. Contour’s default is “0.0.0.0”. |
| `port` _int_ | _(Optional)_ Defines the xDS gRPC API port which Contour will serve. Contour’s default is 8001. |
| `tls` _[TLS](https://projectcontour.io/docs/1.33/config/api/#projectcontour.io/v1alpha1.TLS)_ | _(Optional)_ TLS holds TLS file config details. Contour’s default is { caFile: “/certs/ca.crt”, certFile: “/certs/tls.cert”, keyFile: “/certs/tls.key”, insecure: false }. |

* * *

_Generated with `gen-crd-api-reference-docs`._
