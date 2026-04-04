# Source: https://docs.api7.ai/hub/proxy-cache.md

# proxy-cache

The `proxy-cache` plugin provides the capability to cache responses based on a cache key. The plugin supports both disk-based and memory-based caching options to cache for [GET](https://anything.org/learn/serving-over-http/#get-request), [POST](https://anything.org/learn/serving-over-http/#post-request), and [HEAD](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD) requests.

Responses can be conditionally cached based on request HTTP methods, response status codes, request header values, and more.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `proxy-cache` for different scenarios.

### Cache Data on Disk[â](#cache-data-on-disk "Direct link to Cache Data on Disk")

On-disk caching strategy offers the advantages of data persistency when system restarts and having larger storage capacity compared to in-memory cache. It is suitable for applications that prioritize durability and can tolerate slightly larger cache access latency.

The following example demonstrates how you can use `proxy-cache` plugin on a route to cache data on disk.

When using the on-disk caching strategy, the cache TTL is determined by value from the response header `Expires` or `Cache-Control`. If none of these headers is present or if APISIX returns `502 Bad Gateway` or `504 Gateway Timeout` due to unavailable upstreams, the cache TTL defaults to the value configured in the [configuration files](https://docs.api7.ai/hub/proxy-cache/configuration.md#static-configuration).

Create a route with the `proxy-cache` plugin to cache data on disk:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "proxy-cache-route",
    "uri": "/anything",
    "plugins": {
      "proxy-cache": {
        "cache_strategy": "disk"
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org": 1
      }
    }
  }'
```

adc.yaml

```
services:
  - name: proxy-cache-service
    routes:
      - name: proxy-cache-route
        uris:
          - /anything
        plugins:
          proxy-cache:
            cache_strategy: disk
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

* Gateway API
* APISIX CRD

proxy-cache-ic.yaml

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
  name: proxy-cache-plugin-config
spec:
  plugins:
    - name: proxy-cache
      config:
        cache_strategy: disk
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: proxy-cache-route
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
            name: proxy-cache-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

proxy-cache-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
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
  namespace: aic
  name: proxy-cache-route
spec:
  ingressClassName: apisix
  http:
    - name: proxy-cache-route
      match:
        paths:
          - /anything
      upstreams:
      - name: httpbin-external-domain
      plugins:
      - name: proxy-cache
        enable: true
        config:
          cache_strategy: disk
```

Apply the configuration to your cluster:

```
kubectl apply -f proxy-cache-ic.yaml
```

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should see an `HTTP/1.1 200 OK` response with the following header, showing the plugin is successfully enabled:

```
Apisix-Cache-Status: MISS
```

As there is no cache available before the first response, `Apisix-Cache-Status: MISS` is shown.

Send the same request again within the cache TTL window. You should see an `HTTP/1.1 200 OK` response with the following headers, showing the cache is hit:

```
Apisix-Cache-Status: HIT
```

Wait for the cache to expire after the TTL and send the same request again. You should see an `HTTP/1.1 200 OK` response with the following headers, showing the cache has expired:

```
Apisix-Cache-Status: EXPIRED
```

### Cache Data in Memory[â](#cache-data-in-memory "Direct link to Cache Data in Memory")

In-memory caching strategy offers the advantage of low-latency access to the cached data, as retrieving data from RAM is faster than retrieving data from disk storage. It also works well for storing temporary data that does not need to be persisted long-term, allowing for efficient caching of frequently changing data.

The following example demonstrates how you can use `proxy-cache` plugin on a route to cache data in memory.

Create a route with `proxy-cache` and configure it to use memory-based caching:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "proxy-cache-route",
    "uri": "/anything",
    "plugins": {
      "proxy-cache": {
        "cache_strategy": "memory",
        "cache_zone": "memory_cache",
        "cache_ttl": 10
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org": 1
      }
    }
  }'
```

adc.yaml

```
services:
  - name: proxy-cache-service
    routes:
      - name: proxy-cache-route
        uris:
          - /anything
        plugins:
          proxy-cache:
            cache_strategy: memory
            cache_zone: memory_cache
            cache_ttl: 10
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

* Gateway API
* APISIX CRD

proxy-cache-ic.yaml

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
  name: proxy-cache-plugin-config
spec:
  plugins:
    - name: proxy-cache
      config:
        cache_strategy: memory
        cache_zone: memory_cache
        cache_ttl: 10
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: proxy-cache-route
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
            name: proxy-cache-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

proxy-cache-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
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
  namespace: aic
  name: proxy-cache-route
spec:
  ingressClassName: apisix
  http:
    - name: proxy-cache-route
      match:
        paths:
          - /anything
      upstreams:
      - name: httpbin-external-domain
      plugins:
      - name: proxy-cache
        enable: true
        config:
          cache_strategy: memory
          cache_zone: memory_cache
          cache_ttl: 10
```

Apply the configuration to your cluster:

```
kubectl apply -f proxy-cache-ic.yaml
```

â¶ `cache_strategy`: set to `memory` for in-memory setting.

â· `cache_zone`: set to the name of an in-memory cache zone.

â¸ `cache_ttl`: set the time to live for the in-memory cache to 10 seconds.

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should see an `HTTP/1.1 200 OK` response with the following header, showing the plugin is successfully enabled:

```
Apisix-Cache-Status: MISS
```

As there is no cache available before the first response, `Apisix-Cache-Status: MISS` is shown.

Send the same request again within the cache TTL window. You should see an `HTTP/1.1 200 OK` response with the following headers, showing the cache is hit:

```
Apisix-Cache-Status: HIT
```

### Cache Responses Conditionally[â](#cache-responses-conditionally "Direct link to Cache Responses Conditionally")

The following example demonstrates how you can configure the `proxy-cache` plugin to conditionally cache responses.

Create a route with the `proxy-cache` plugin and configure the `no_cache` attribute:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "proxy-cache-route",
    "uri": "/anything",
    "plugins": {
      "proxy-cache": {
        "no_cache": ["$arg_no_cache", "$http_no_cache"]
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org": 1
      }
    }
  }'
```

adc.yaml

```
services:
  - name: proxy-cache-service
    routes:
      - name: proxy-cache-route
        uris:
          - /anything
        plugins:
          proxy-cache:
            no_cache:
              - $arg_no_cache
              - $http_no_cache
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

* Gateway API
* APISIX CRD

proxy-cache-ic.yaml

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
  name: proxy-cache-plugin-config
spec:
  plugins:
    - name: proxy-cache
      config:
        no_cache:
          - $arg_no_cache
          - $http_no_cache
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: proxy-cache-route
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
            name: proxy-cache-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

proxy-cache-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
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
  namespace: aic
  name: proxy-cache-route
spec:
  ingressClassName: apisix
  http:
    - name: proxy-cache-route
      match:
        paths:
          - /anything
      upstreams:
      - name: httpbin-external-domain
      plugins:
      - name: proxy-cache
        enable: true
        config:
          no_cache:
            - $arg_no_cache
            - $http_no_cache
```

Apply the configuration to your cluster:

```
kubectl apply -f proxy-cache-ic.yaml
```

â¶ `no_cache`: If at least one of the values of the URL parameter `no_cache` and header `no_cache` is not empty and is not equal to `0`, the response will not be cached.

Send a few requests to the route with the URL parameter `no_cache` value indicating cache bypass:

```
curl -i "http://127.0.0.1:9080/anything?no_cache=1"
```

You should receive `HTTP/1.1 200 OK` responses for all requests and observe the following header every time:

```
Apisix-Cache-Status: EXPIRED
```

Send a few other requests to the route with the URL parameter `no_cache` value being zero:

```
curl -i "http://127.0.0.1:9080/anything?no_cache=0"
```

You should receive `HTTP/1.1 200 OK` responses for all requests and start seeing the cache being hit:

```
Apisix-Cache-Status: HIT
```

You can also specify the value in the `no_cache` header as such:

```
curl -i "http://127.0.0.1:9080/anything" -H "no_cache: 1"
```

The response should not be cached:

```
Apisix-Cache-Status: EXPIRED
```

### Retrieve Responses from Cache Conditionally[â](#retrieve-responses-from-cache-conditionally "Direct link to Retrieve Responses from Cache Conditionally")

The following example demonstrates how you can configure the `proxy-cache` plugin to conditionally retrieve responses from cache.

Create a route with the `proxy-cache` plugin and configure the `cache_bypass` attribute:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "proxy-cache-route",
    "uri": "/anything",
    "plugins": {
      "proxy-cache": {
        "cache_bypass": ["$arg_bypass", "$http_bypass"]
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org": 1
      }
    }
  }'
```

adc.yaml

```
services:
  - name: proxy-cache-service
    routes:
      - name: proxy-cache-route
        uris:
          - /anything
        plugins:
          proxy-cache:
            cache_bypass:
              - $arg_bypass
              - $http_bypass
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

* Gateway API
* APISIX CRD

proxy-cache-ic.yaml

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
  name: proxy-cache-plugin-config
spec:
  plugins:
    - name: proxy-cache
      config:
        cache_bypass:
          - $arg_bypass
          - $http_bypass
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: proxy-cache-route
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
            name: proxy-cache-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

proxy-cache-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
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
  namespace: aic
  name: proxy-cache-route
spec:
  ingressClassName: apisix
  http:
    - name: proxy-cache-route
      match:
        paths:
          - /anything
      upstreams:
      - name: httpbin-external-domain
      plugins:
      - name: proxy-cache
        enable: true
        config:
          cache_bypass:
            - $arg_bypass
            - $http_bypass
```

Apply the configuration to your cluster:

```
kubectl apply -f proxy-cache-ic.yaml
```

â¶ `cache_bypass`: If at least one of the values of the URL parameter `bypass` and header `bypass` is not empty and is not equal to `0`, the response will not be retrieved from the cache.

Send a request to the route with the URL parameter `bypass` value indicating cache bypass:

```
curl -i "http://127.0.0.1:9080/anything?bypass=1"
```

You should see an `HTTP/1.1 200 OK` response with the following header:

```
Apisix-Cache-Status: BYPASS
```

Send another request to the route with the URL parameter `bypass` value being zero:

```
curl -i "http://127.0.0.1:9080/anything?bypass=0"
```

You should see an `HTTP/1.1 200 OK` response with the following header:

```
Apisix-Cache-Status: MISS
```

You can also specify the value in the `bypass` header as such:

```
curl -i "http://127.0.0.1:9080/anything" -H "bypass: 1"
```

The cache should be bypassed:

```
Apisix-Cache-Status: BYPASS
```

### Cache for 502 and 504 Error Response Code[â](#cache-for-502-and-504-error-response-code "Direct link to Cache for 502 and 504 Error Response Code")

When the upstream services return server errors in the 500 range, `proxy-cache` plugin will cache the responses if and only if the returned status is `502 Bad Gateway` or `504 Gateway Timeout`.

The following example demonstrates the behavior of `proxy-cache` plugin when the upstream service returns `504 Gateway Timeout`.

Create a route with the `proxy-cache` plugin and configure a dummy upstream service:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "proxy-cache-route",
    "uri": "/timeout",
    "plugins": {
      "proxy-cache": { }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "12.34.56.78": 1
      }
    }
  }'
```

adc.yaml

```
services:
  - name: proxy-cache-service
    routes:
      - name: proxy-cache-route
        uris:
          - /timeout
        plugins:
          proxy-cache: {}
    upstream:
      type: roundrobin
      nodes:
        - host: 12.34.56.78
          port: 80
          weight: 1
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

* Gateway API
* APISIX CRD

proxy-cache-ic.yaml

```
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: dummy-upstream
spec:
  type: ExternalName
  externalName: dummy.example.com
---
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: proxy-cache-plugin-config
spec:
  plugins:
    - name: proxy-cache
      config:
        _meta:
          disable: false
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: proxy-cache-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /timeout
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: proxy-cache-plugin-config
      backendRefs:
        - name: dummy-upstream
          port: 80
```

proxy-cache-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: dummy-upstream
spec:
  ingressClassName: apisix
  externalNodes:
  - type: Domain
    name: dummy.example.com
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: proxy-cache-route
spec:
  ingressClassName: apisix
  http:
    - name: proxy-cache-route
      match:
        paths:
          - /timeout
      upstreams:
      - name: dummy-upstream
      plugins:
      - name: proxy-cache
        enable: true
```

Apply the configuration to your cluster:

```
kubectl apply -f proxy-cache-ic.yaml
```

Generate a few requests to the route:

```
seq 4 | xargs -I{} curl -I "http://127.0.0.1:9080/timeout"
```

You should see a response similar to the following:

```
HTTP/1.1 504 Gateway Time-out
...
Apisix-Cache-Status: MISS

HTTP/1.1 504 Gateway Time-out
...
Apisix-Cache-Status: HIT

HTTP/1.1 504 Gateway Time-out
...
Apisix-Cache-Status: HIT

HTTP/1.1 504 Gateway Time-out
...
Apisix-Cache-Status: HIT
```

However, if the upstream services returns `503 Service Temporarily Unavailable`, the response will not be cached.
