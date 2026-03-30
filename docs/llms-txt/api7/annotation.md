# Source: https://docs.api7.ai/enterprise/3.8.x/reference/api7-ingress-controller/annotation.md

# Ingress Annotations

Annotations are key-value pairs that allow controllers to configure functionalities that are not available through standard Kubernetes resource fields. In API7 Ingress Controller, annotations are commonly used with Ingress resources to configure gateway behaviors, routing rules, upstream settings, plugins, and other features. Alternatively, you can use APISIX CRDs to configure these features for a better experience.

This document describes all available annotations and their uses.

## All Annotations[â](#all-annotations "Direct link to All Annotations")

| Annotation                                             |
| ------------------------------------------------------ |
| `kubernetes.io/ingress.class`                          |
| `k8s.apisix.apache.org/use-regex`                      |
| `k8s.apisix.apache.org/enable-websocket`               |
| `k8s.apisix.apache.org/plugin-config-name`             |
| `k8s.apisix.apache.org/upstream-scheme`                |
| `k8s.apisix.apache.org/upstream-retries`               |
| `k8s.apisix.apache.org/upstream-connect-timeout`       |
| `k8s.apisix.apache.org/upstream-read-timeout`          |
| `k8s.apisix.apache.org/upstream-send-timeout`          |
| `k8s.apisix.apache.org/enable-cors`                    |
| `k8s.apisix.apache.org/cors-allow-origin`              |
| `k8s.apisix.apache.org/cors-allow-headers`             |
| `k8s.apisix.apache.org/cors-allow-methods`             |
| `k8s.apisix.apache.org/enable-csrf`                    |
| `k8s.apisix.apache.org/csrf-key`                       |
| `k8s.apisix.apache.org/http-to-https`                  |
| `k8s.apisix.apache.org/http-redirect`                  |
| `k8s.apisix.apache.org/http-redirect-code`             |
| `k8s.apisix.apache.org/rewrite-target`                 |
| `k8s.apisix.apache.org/rewrite-target-regex`           |
| `k8s.apisix.apache.org/rewrite-target-regex-template`  |
| `k8s.apisix.apache.org/enable-response-rewrite`        |
| `k8s.apisix.apache.org/response-rewrite-status-code`   |
| `k8s.apisix.apache.org/response-rewrite-body`          |
| `k8s.apisix.apache.org/response-rewrite-body-base64`   |
| `k8s.apisix.apache.org/response-rewrite-add-header`    |
| `k8s.apisix.apache.org/response-rewrite-set-header`    |
| `k8s.apisix.apache.org/response-rewrite-remove-header` |
| `k8s.apisix.apache.org/auth-uri`                       |
| `k8s.apisix.apache.org/auth-ssl-verify`                |
| `k8s.apisix.apache.org/auth-request-headers`           |
| `k8s.apisix.apache.org/auth-upstream-headers`          |
| `k8s.apisix.apache.org/auth-client-headers`            |
| `k8s.apisix.apache.org/allowlist-source-range`         |
| `k8s.apisix.apache.org/blocklist-source-range`         |
| `k8s.apisix.apache.org/http-allow-methods`             |
| `k8s.apisix.apache.org/http-block-methods`             |
| `k8s.apisix.apache.org/auth-type`                      |
| `k8s.apisix.apache.org/svc-namespace`                  |

## Annotation Details[â](#annotation-details "Direct link to Annotation Details")

Note that annotation keys and values can only be strings.

### Ingress Class[â](#ingress-class "Direct link to Ingress Class")

The `kubernetes.io/ingress.class` annotation specifies which ingress controller should process a given Ingress resource. This is useful when multiple ingress controllers are deployed in the same cluster.

For example:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: httpbin
  annotations:
    kubernetes.io/ingress.class: "apisix"
spec:
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: httpbin
            port:
              number: 80
```

### Response Rewrite[â](#response-rewrite "Direct link to Response Rewrite")

These annotations enable you to modify the response returned from the upstream service before it is sent to the client. They correspond to the functionality of the [`response-rewrite`](https://docs.api7.ai/hub/response-rewrite.md) plugin in APISIX.

| Annotation                                             | Description                                                                                                     |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `k8s.apisix.apache.org/enable-response-rewrite`        | Enables the response rewrite feature. Set to `true` to enable response rewriting for this resource.             |
| `k8s.apisix.apache.org/response-rewrite-status-code`   | Specifies a new HTTP status code for the response.                                                              |
| `k8s.apisix.apache.org/response-rewrite-body`          | Replaces the response body with the specified plain text content.                                               |
| `k8s.apisix.apache.org/response-rewrite-body-base64`   | Replaces the response body with Base64-encoded content.                                                         |
| `k8s.apisix.apache.org/response-rewrite-add-header`    | Adds new headers to the response. You can specify multiple headers as a comma-separated list.                   |
| `k8s.apisix.apache.org/response-rewrite-set-header`    | Sets or overrides existing headers in the response. You can specify multiple headers as a comma-separated list. |
| `k8s.apisix.apache.org/response-rewrite-remove-header` | Removes specified headers from the response. You can specify multiple headers as a comma-separated list.        |

For example:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: httpbin-response-rewrite
  annotations:
    k8s.apisix.apache.org/enable-response-rewrite: "true"
    k8s.apisix.apache.org/response-rewrite-status-code: "403"
    k8s.apisix.apache.org/response-rewrite-body: "Access denied"
    k8s.apisix.apache.org/response-rewrite-add-header: "X-Reason:Forbidden,X-Env:Test"
    k8s.apisix.apache.org/response-rewrite-remove-header: "header1,header2"
spec:
  ingressClassName: apisix
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: httpbin
            port:
              number: 80
```

### IP Restriction[â](#ip-restriction "Direct link to IP Restriction")

These annotations control client access based on IP address ranges. They correspond to the functionality of the [`ip-restriction`](https://docs.api7.ai/hub/ip-restriction.md) plugin in APISIX.

| Annotation                                     | Description                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `k8s.apisix.apache.org/allowlist-source-range` | Comma-separated list of CIDR ranges that are allowed to access the resource. All other IPs are denied. |
| `k8s.apisix.apache.org/blocklist-source-range` | Comma-separated list of CIDR ranges that are blocked from accessing the resource.                      |

For example:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ip-restriction
  annotations:
    k8s.apisix.apache.org/allowlist-source-range: "10.0.0.0/24,192.168.1.0/24"
spec:
  ingressClassName: apisix
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: httpbin
            port:
              number: 80
```

### Forward Auth[â](#forward-auth "Direct link to Forward Auth")

These annotations configure an external authentication endpoint that validates incoming requests before they reach the backend service. They correspond to the functionality of the [`forward-auth`](https://docs.api7.ai/hub/forward-auth.md) plugin in APISIX.

| Annotation                                    | Description                                                                                                                   |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `k8s.apisix.apache.org/auth-uri`              | The URI of the external authentication server. Requests are forwarded to this URI for verification.                           |
| `k8s.apisix.apache.org/auth-ssl-verify`       | Enables or disables SSL certificate verification when communicating with the authentication server. Set to `true` or `false`. |
| `k8s.apisix.apache.org/auth-request-headers`  | Comma-separated list of request headers to forward to the authentication server.                                              |
| `k8s.apisix.apache.org/auth-upstream-headers` | Comma-separated list of headers from the auth response to forward to the upstream service.                                    |
| `k8s.apisix.apache.org/auth-client-headers`   | Comma-separated list of headers from the auth response to return to the client.                                               |

For example:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-forward-auth
  annotations:
    k8s.apisix.apache.org/auth-uri: "https://auth.example.com/verify"
    k8s.apisix.apache.org/auth-ssl-verify: "true"
    k8s.apisix.apache.org/auth-request-headers: "Authorization"
    k8s.apisix.apache.org/auth-upstream-headers: "X-User-ID,X-User-Role"
    k8s.apisix.apache.org/auth-client-headers: "X-Auth-Status"
spec:
  ingressClassName: apisix
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: httpbin
            port:
              number: 80
```

### RegEx Route Matching[â](#regex-route-matching "Direct link to RegEx Route Matching")

The `k8s.apisix.apache.org/use-regex` annotation allows an Ingress to define routes using regular expressions for advanced path matching. Set to `true` to interpret the `path` field as a RegEx pattern.

For example:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-regex
  annotations:
    k8s.apisix.apache.org/use-regex: "true"
spec:
  ingressClassName: apisix
  rules:
  - http:
      paths:
      - path: "/users/[0-9]+"
        pathType: ImplementationSpecific
        backend:
          service:
            name: user-service
            port:
              number: 80
```

### Authentication[â](#authentication "Direct link to Authentication")

The `k8s.apisix.apache.org/auth-type` annotation specifies the type of authentication to apply to an Ingress resource. Support `keyAuth` and `basicAuth`.

For example:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-key-auth
  annotations:
    k8s.apisix.apache.org/auth-type: "keyAuth"
spec:
  ingressClassName: apisix
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: httpbin
            port:
              number: 80
---
apiVersion: apisix.apache.org/v2
kind: ApisixConsumer
metadata:
  name: john
spec:
  ingressClassName: apisix
  authParameter:
    keyAuth:
      value:
        key: john-key
```

### Cross Namespace Service Access[â](#cross-namespace-service-access "Direct link to Cross Namespace Service Access")

The `k8s.apisix.apache.org/svc-namespace` annotation allows an Ingress to route traffic to a service located in a different namespace from the Ingress resource. By default, Ingresses can only reference Services within the same namespace.

For example:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: cross-namespace-ingress
  annotations:
    k8s.apisix.apache.org/svc-namespace: "other-namespace"
spec:
  ingressClassName: apisix
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: backend-service
            port:
              number: 80
```

### Proxy Rewrite[â](#proxy-rewrite "Direct link to Proxy Rewrite")

These annotations allow you to rewrite request paths before forwarding them to the upstream service. They correspond to the functionality of the [`proxy-rewrite`](https://docs.api7.ai/hub/proxy-rewrite.md) plugin in APISIX.

| Annotation                                            | Description                                                                                                                  |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `k8s.apisix.apache.org/rewrite-target`                | Rewrites the request path to the specified target path.                                                                      |
| `k8s.apisix.apache.org/rewrite-target-regex`          | Specifies a regular expression pattern to match in the original request path.                                                |
| `k8s.apisix.apache.org/rewrite-target-regex-template` | Template for rewriting the request path when using `rewrite-target-regex`. Supports capturing groups from the RegEx pattern. |

For example, the following configuration rewrites requests so that requests to `/api` are forwarded to `/new-path`:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-rewrite
  annotations:
    k8s.apisix.apache.org/rewrite-target: "/new-path"
spec:
  ingressClassName: apisix
  rules:
  - http:
      paths:
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: httpbin
            port:
              number: 80
```

For example, the following configuration rewrites requests so that requests to `/api/test` are forwarded to `/backend/test`:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-regex-rewrite
  annotations:
    k8s.apisix.apache.org/rewrite-target-regex: "^/api/(.*)"
    k8s.apisix.apache.org/rewrite-target-regex-template: "/backend/$1"
spec:
  ingressClassName: apisix
  rules:
  - http:
      paths:
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: httpbin
            port:
              number: 80
```

### Plugin Config[â](#plugin-config "Direct link to Plugin Config")

The `k8s.apisix.apache.org/plugin-config-name` annotation allows you to attach a predefined APISIX plugin configuration to an Ingress resource. It corresponds to a PluginConfig resource in APISIX, enabling reusable plugin settings across multiple routes or services.

For example:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-plugin-config
  annotations:
    k8s.apisix.apache.org/plugin-config-name: "rate-limit-config"
spec:
  ingressClassName: apisix
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: httpbin
            port:
              number: 80
---
apiVersion: apisix.apache.org/v2
kind: ApisixPluginConfig
metadata:
  name: rate-limit-config
spec:
  ingressClassName: apisix
  plugins:
  - name: limit-count
    enable: true
    config:
      count: 2
      time_window: 10
      rejected_code: 429
```

### CSRF[â](#csrf "Direct link to CSRF")

These annotations enable CSRF (Cross-Site Request Forgery) protection for an Ingress. They correspond to the [`csrf`](https://apisix.apache.org/docs/apisix/plugins/csrf/) plugin in APISIX.

| Annotation                          | Description                                                              |
| ----------------------------------- | ------------------------------------------------------------------------ |
| `k8s.apisix.apache.org/enable-csrf` | Enables or disables CSRF protection. Set to `true` to enable the plugin. |
| `k8s.apisix.apache.org/csrf-key`    | Specifies the secret key used to sign and validate CSRF tokens.          |

For example:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-csrf
  annotations:
    k8s.apisix.apache.org/enable-csrf: "true"
    k8s.apisix.apache.org/csrf-key: "my-secret-csrf-key"
spec:
  ingressClassName: apisix
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: httpbin
            port:
              number: 80
```

### Allow/Block HTTP Methods[â](#allowblock-http-methods "Direct link to Allow/Block HTTP Methods")

These annotations control which HTTP methods are allowed or blocked for an Ingress. If both allow and block methods are specified, only the allow list is effective.

| Annotation                                 | Description                                                                                                    |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| `k8s.apisix.apache.org/http-allow-methods` | Comma-separated list of HTTP methods that are explicitly allowed. Requests using other methods will be denied. |
| `k8s.apisix.apache.org/http-block-methods` | Comma-separated list of HTTP methods that are explicitly blocked. Requests using these methods will be denied. |

For example:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-http-methods
  annotations:
    k8s.apisix.apache.org/http-allow-methods: "GET,POST"
spec:
  ingressClassName: apisix
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: httpbin
            port:
              number: 80
```

### Enable Websocket[â](#enable-websocket "Direct link to Enable Websocket")

The `k8s.apisix.apache.org/enable-websocket` annotation enables WebSocket support for an Ingress when set to `true`.

For example:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-websocket
  annotations:
    k8s.apisix.apache.org/enable-websocket: "true"
spec:
  ingressClassName: apisix
  rules:
  - http:
      paths:
      - path: /ws
        pathType: Exact
        backend:
          service:
            name: websocket-service
            port:
              number: 8080
```

### Redirect[â](#redirect "Direct link to Redirect")

These annotations configure HTTP-to-HTTPS redirection or custom HTTP redirects for an Ingress. They correspond to the [`redirect`](https://apisix.apache.org/docs/apisix/plugins/redirect) plugin in APISIX.

| Annotation                                 | Description                                                     |
| ------------------------------------------ | --------------------------------------------------------------- |
| `k8s.apisix.apache.org/http-to-https`      | Set to `true` to automatically redirect HTTP requests to HTTPS. |
| `k8s.apisix.apache.org/http-redirect`      | Specifies a custom URL to redirect requests to.                 |
| `k8s.apisix.apache.org/http-redirect-code` | HTTP status code to use for the redirect.                       |

For example, the following configuration redirects HTTP requests to HTTPS with a 301 status code:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-https-redirect
  annotations:
    k8s.apisix.apache.org/http-to-https: "true"
spec:
  ingressClassName: apisix
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: httpbin
            port:
              number: 80
```

For example, the following configuration redirects HTTP requests to a new URI with a custom HTTP redirect status code:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-custom-redirect
  annotations:
    k8s.apisix.apache.org/http-redirect: "https://example.com/new-path"
    k8s.apisix.apache.org/http-redirect-code: "302"
spec:
  ingressClassName: apisix
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: httpbin
            port:
              number: 80
```

### CORS[â](#cors "Direct link to CORS")

These annotations configure Cross-Origin Resource Sharing (CORS) for an Ingress. They correspond to the [`cors`](https://docs.api7.ai/hub/cors.md) plugin in APISIX.

| Annotation                                 | Description                                                            |
| ------------------------------------------ | ---------------------------------------------------------------------- |
| `k8s.apisix.apache.org/enable-cors`        | Set to `true` to enable CORS.                                          |
| `k8s.apisix.apache.org/cors-allow-origin`  | Specifies the allowed origin(s), such as `*` or `https://example.com`. |
| `k8s.apisix.apache.org/cors-allow-headers` | Comma-separated list of allowed headers in cross-origin requests.      |
| `k8s.apisix.apache.org/cors-allow-methods` | Comma-separated list of allowed HTTP methods.                          |

For example:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-cors
  annotations:
    k8s.apisix.apache.org/enable-cors: "true"
    k8s.apisix.apache.org/cors-allow-origin: "https://example.com"
    k8s.apisix.apache.org/cors-allow-headers: "Content-Type,Authorization"
    k8s.apisix.apache.org/cors-allow-methods: "GET,POST,PUT"
spec:
  ingressClassName: apisix
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: httpbin
            port:
              number: 80
```

### Upstream[â](#upstream "Direct link to Upstream")

These annotations allow you to configure upstream behavior for an Ingress in APISIX, including scheme, retries, and timeouts. They correspond to the upstream settings in Apache APISIX.

| Annotation                                       | Description                                                                                                                            |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| `k8s.apisix.apache.org/upstream-scheme`          | Specifies the protocol used to communicate with the upstream service. Default is `http`. Support `http`, `https`, `grpc`, and `grpcs`. |
| `k8s.apisix.apache.org/upstream-retries`         | Number of retries for upstream requests in case of failure.                                                                            |
| `k8s.apisix.apache.org/upstream-connect-timeout` | Timeout for establishing a connection to the upstream service. Default is `60s`.                                                       |
| `k8s.apisix.apache.org/upstream-read-timeout`    | Timeout for reading a response from the upstream service. Default is `60s`.                                                            |
| `k8s.apisix.apache.org/upstream-send-timeout`    | Timeout for sending a request to the upstream service. Default is `60s`.                                                               |

For example:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-upstream
  annotations:
    k8s.apisix.apache.org/upstream-scheme: "https"
    k8s.apisix.apache.org/upstream-retries: "3"
    k8s.apisix.apache.org/upstream-connect-timeout: "5s"
    k8s.apisix.apache.org/upstream-read-timeout: "5s"
    k8s.apisix.apache.org/upstream-send-timeout: "5s"
spec:
  ingressClassName: apisix
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: httpbin
            port:
              number: 80
```
