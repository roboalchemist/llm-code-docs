# Source: https://docs.api7.ai/hub/limit-req.md

# limit-req

The `limit-req` plugin uses the [leaky bucket](https://en.wikipedia.org/wiki/Leaky_bucket) algorithm to rate limit the number of the requests and allow for throttling.

## Local vs Redis Rate Limiting[â](#local-vs-redis-rate-limiting "Direct link to Local vs Redis Rate Limiting")

The `limit-req` plugin supports two modes of rate limiting:

* **Local rate limiting**: Limits are enforced independently on each gateway instance. Each instance maintains its own counters, so the effective limit is roughly (limit Ã number of instances) when traffic is spread across instances. This is the default when no `policy` is set or when `policy` is `local`.
* **Redis-based rate limiting**: Limits are shared across all gateway instances through Redis. All instances share the same quota, so the configured limit applies to all gateway instances.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `limit-req` in different scenarios.

### Apply Rate Limiting by Remote Address[â](#apply-rate-limiting-by-remote-address "Direct link to Apply Rate Limiting by Remote Address")

The following example demonstrates the rate limiting of HTTP requests by a single variable, `remote_addr`.

Create a route with `limit-req` plugin that allows for 1 QPS per remote address:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '
  {
    "id": "limit-req-route",
    "uri": "/get",
    "plugins": {
      "limit-req": {
        "rate": 1,
        "burst": 0,
        "key": "remote_addr",
        "key_type": "var",
        "rejected_code": 429,
        "policy": "local",
        "nodelay": true
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

adc.yaml

```
services:
  - name: httpbin
    routes:
      - uris:
          - /get
        name: limit-req-route
        plugins:
          limit-req:
            rate: 1
            burst: 0
            key: remote_addr
            key_type: var
            rejected_code: 429
            policy: local
            nodelay: true
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

limit-req-ic.yaml

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
  name: limit-req-plugin-config
spec:
  plugins:
    - name: limit-req
      config:
        rate: 1
        burst: 0
        key: remote_addr
        key_type: var
        rejected_code: 429
        policy: local
        nodelay: true
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: limit-req-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /get
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: limit-req-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

limit-req-ic.yaml

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
  name: limit-req-route
spec:
  ingressClassName: apisix
  http:
    - name: limit-req-route
      match:
        paths:
          - /get
        methods:
          - GET
      upstreams:
        - name: httpbin-external-domain
      plugins:
        - name: limit-req
          config:
            rate: 1
            burst: 0
            key: remote_addr
            key_type: var
            rejected_code: 429
            policy: local
            nodelay: true
```

Apply the configuration:

```
kubectl apply -f limit-req-ic.yaml
```

â¶ `rate`: limit the QPS to 1.

â· `key`: set to `remote_addr` to apply rate limiting quota by remote address and consumer.

â¸ `key_type`: set to `var` to interpret the `key` as a variable.

Send a request to verify:

```
curl -i "http://127.0.0.1:9080/get"
```

You should see an `HTTP/1.1 200 OK` response.

The request has consumed all the quota allowed for the time window. If you send the request again within the same second, you should receive an `HTTP/1.1 429 Too Many Requests` response, indicating the request surpasses the quota threshold.

### Implement API Throttling[â](#implement-api-throttling "Direct link to Implement API Throttling")

The following example demonstrates how to configure `burst` to allow overrun of the rate limiting threshold by the configured value and achieve request throttling. You will also see a comparison against when throttling is not implemented.

Create a route with `limit-req` plugin that allows for 1 QPS per remote address, with a `burst` of 1:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "limit-req-route",
    "uri": "/get",
    "plugins": {
      "limit-req": {
        "rate": 1,
        "burst": 1,
        "key": "remote_addr",
        "rejected_code": 429,
        "policy": "local"
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

adc.yaml

```
services:
  - name: httpbin
    routes:
      - uris:
          - /get
        name: limit-req-route
        plugins:
          limit-req:
            rate: 1
            burst: 1
            key: remote_addr
            rejected_code: 429
            policy: local
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

limit-req-ic.yaml

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
  name: limit-req-plugin-config
spec:
  plugins:
    - name: limit-req
      config:
        rate: 1
        burst: 1
        key: remote_addr
        rejected_code: 429
        policy: local
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: limit-req-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /get
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: limit-req-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

limit-req-ic.yaml

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
  name: limit-req-route
spec:
  ingressClassName: apisix
  http:
    - name: limit-req-route
      match:
        paths:
          - /get
        methods:
          - GET
      upstreams:
        - name: httpbin-external-domain
      plugins:
        - name: limit-req
          config:
            rate: 1
            burst: 1
            key: remote_addr
            rejected_code: 429
            policy: local
```

Apply the configuration:

```
kubectl apply -f limit-req-ic.yaml
```

â¶ `burst`: allow for 1 request exceeding the `rate` to be delayed for processing.

Generate three requests to the route:

```
resp=$(seq 3 | xargs -I{} curl -i "http://127.0.0.1:9080/get" -o /dev/null -s -w "%{http_code}\n") && \
  count_200=$(echo "$resp" | grep "200" | wc -l) && \
  count_429=$(echo "$resp" | grep "429" | wc -l) && \
  echo "200 responses: $count_200 ; 429 responses: $count_429"
```

You are likely to see that all three requests are successful:

```
200 responses: 3 ; 429 responses: 0
```

To see the effect without `burst`, update `burst` to 0 or set `nodelay` to `true` as follows:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes/limit-req-route" -X PATCH \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "plugins": {
      "limit-req": {
        "nodelay": true
      }
    }
  }'
```

Update the ADC YAML with `nodelay: true`:

adc.yaml

```
services:
  - name: httpbin
    routes:
      - uris:
          - /get
        name: limit-req-route
        plugins:
          limit-req:
            rate: 1
            burst: 1  # alternatively, set burst to 0
            key: remote_addr
            rejected_code: 429
            policy: local
            nodelay: true
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

Synchronize the configuration with updated plugin settings:

```
adc sync -f adc.yaml
```

Update the manifest file as such:

* Gateway API
* APISIX CRD

limit-req-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: limit-req-plugin-config
spec:
  plugins:
    - name: limit-req
      config:
        rate: 1
        burst: 1  # alternatively, set burst to 0
        key: remote_addr
        rejected_code: 429
        policy: local
        nodelay: true
```

limit-req-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: limit-req-route
spec:
  ingressClassName: apisix
  http:
    - name: limit-req-route
      match:
        paths:
          - /get
        methods:
          - GET
      upstreams:
        - name: httpbin-external-domain
      plugins:
        - name: limit-req
          config:
            rate: 1
            burst: 1  # alternatively, set burst to 0
            key: remote_addr
            rejected_code: 429
            policy: local
            nodelay: true
```

Apply the updated configuration:

```
kubectl apply -f limit-req-ic.yaml
```

Generate three requests to the route again:

```
resp=$(seq 3 | xargs -I{} curl -i "http://127.0.0.1:9080/get" -o /dev/null -s -w "%{http_code}\n") && \
  count_200=$(echo "$resp" | grep "200" | wc -l) && \
  count_429=$(echo "$resp" | grep "429" | wc -l) && \
  echo "200 responses: $count_200 ; 429 responses: $count_429"
```

You should see a response similar to the following, showing requests surpassing the rate have been rejected:

```
200 responses: 1 ; 429 responses: 2
```

### Apply Rate Limiting by Remote Address and Consumer Name[â](#apply-rate-limiting-by-remote-address-and-consumer-name "Direct link to Apply Rate Limiting by Remote Address and Consumer Name")

The following example demonstrates the rate limiting of requests by a combination of variables, `remote_addr` and `consumer_name`.

* Admin API
* ADC
* Ingress Controller

Create a consumer `john`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "john"
  }'
```

Create `key-auth` credential for the consumer:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/john/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-john-key-auth",
    "plugins": {
      "key-auth": {
        "key": "john-key"
      }
    }
  }'
```

Create a second consumer `jane`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "jane"
  }'
```

Create `key-auth` credential for the consumer:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/jane/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-jane-key-auth",
    "plugins": {
      "key-auth": {
        "key": "jane-key"
      }
    }
  }'
```

Create a route with `key-auth` and `limit-req` plugins:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "limit-req-route",
    "uri": "/get",
    "plugins": {
      "key-auth": {},
      "limit-req": {
        "rate": 1,
        "burst": 0,
        "key": "$remote_addr $consumer_name",
        "key_type": "var_combination",
        "rejected_code": 429,
        "policy": "local"
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

Create two consumers and a route that enables rate limiting by consumers:

adc.yaml

```
consumers:
  - username: john
    credentials:
      - name: key-auth
        type: key-auth
        config:
          key: john-key
  - username: jane
    credentials:
      - name: key-auth
        type: key-auth
        config:
          key: jane-key
services:
  - name: limit-req-service
    routes:
      - name: limit-req-route
        uris:
          - /get
        plugins:
          key-auth: {}
          limit-req:
            rate: 1
            burst: 0
            key: "$remote_addr $consumer_name"
            key_type: var_combination
            rejected_code: 429
            policy: local
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

Create two consumers and a route that enables rate limiting by consumers:

* Gateway API
* APISIX CRD

limit-req-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: Consumer
metadata:
  namespace: aic
  name: john
spec:
  gatewayRef:
    name: apisix
  credentials:
    - type: key-auth
      name: primary-key
      config:
        key: john-key
---
apiVersion: apisix.apache.org/v1alpha1
kind: Consumer
metadata:
  namespace: aic
  name: jane
spec:
  gatewayRef:
    name: apisix
  credentials:
    - type: key-auth
      name: primary-key
      config:
        key: jane-key
---
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
  name: limit-req-plugin-config
spec:
  plugins:
    - name: key-auth
      config:
        _meta:
          disable: false
    - name: limit-req
      config:
        rate: 1
        burst: 0
        key: "$remote_addr $consumer_name"
        key_type: var_combination
        rejected_code: 429
        policy: local
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: limit-req-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /get
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: limit-req-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

limit-req-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixConsumer
metadata:
  namespace: aic
  name: john
spec:
  ingressClassName: apisix
  authParameter:
    keyAuth:
      value:
        key: john-key
---
apiVersion: apisix.apache.org/v2
kind: ApisixConsumer
metadata:
  namespace: aic
  name: jane
spec:
  ingressClassName: apisix
  authParameter:
    keyAuth:
      value:
        key: jane-key
---
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
  name: limit-req-route
spec:
  ingressClassName: apisix
  http:
    - name: limit-req-route
      match:
        paths:
          - /get
        methods:
          - GET
      upstreams:
        - name: httpbin-external-domain
      plugins:
        - name: key-auth
          config:
            _meta:
              disable: false
        - name: limit-req
          config:
            rate: 1
            burst: 0
            key: "$remote_addr $consumer_name"
            key_type: var_combination
            rejected_code: 429
            policy: local
```

tip

The ApisixConsumer CRD does not support configuring plugins on consumers. If you need to apply rate limiting per consumer, consider using [Gateway API Consumer](https://api7.ai/docs/ingress-controller/latest/crd/crd-go-client) which supports plugins on consumers.

Apply the configuration:

```
kubectl apply -f limit-req-ic.yaml
```

â¶ `key-auth`: enable key authentication on the route.

â· `key`: set to `$remote_addr $consumer_name` to apply rate limiting quota by remote address and consumer.

â¸ `key_type`: set to `var_combination` to interpret the `key` as a combination of variables.

Send two requests simultaneously, each for one consumer:

```
curl -i "http://127.0.0.1:9080/get" -H 'apikey: jane-key' & \
curl -i "http://127.0.0.1:9080/get" -H 'apikey: john-key' &
```

You should receive `HTTP/1.1 200 OK` for both requests, indicating the request has not exceeded the threshold for each consumer.

If you send more requests as either consumer within the same second, you should receive an `HTTP/1.1 429 Too Many Requests` response.

This verifies the plugin rate limits by the combination of variables, `remote_addr` and `consumer_name`.
