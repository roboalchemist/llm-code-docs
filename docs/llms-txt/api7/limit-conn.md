# Source: https://docs.api7.ai/hub/limit-conn.md

# limit-conn

The `limit-conn` plugin limits the rate of requests by the number of concurrent connections. Requests exceeding the threshold will be delayed or rejected based on the configuration, ensuring controlled resource usage and preventing overload.

## Local vs Redis Rate Limiting[â](#local-vs-redis-rate-limiting "Direct link to Local vs Redis Rate Limiting")

The `limit-conn` plugin supports two modes of rate limiting:

* **Local rate limiting**: Limits are enforced independently on each gateway instance. Each instance maintains its own counters, so the effective limit is roughly (limit Ã number of instances) when traffic is spread across instances. This is the default when no `policy` is set or when `policy` is `local`.
* **Redis-based rate limiting**: Limits are shared across all gateway instances through Redis. All instances share the same quota, so the configured limit applies to all gateway instances.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `limit-conn` in different scenarios.

### Apply Rate Limiting by Remote Address[â](#apply-rate-limiting-by-remote-address "Direct link to Apply Rate Limiting by Remote Address")

The following example demonstrates how to use `limit-conn` to rate limit requests by `remote_addr`, with example connection and burst thresholds.

Create a route with `limit-conn` plugin as such:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "limit-conn-route",
    "uri": "/get",
    "plugins": {
      "limit-conn": {
        "conn": 2,
        "burst": 1,
        "default_conn_delay": 0.1,
        "key_type": "var",
        "key": "remote_addr",
        "policy": "local",
        "rejected_code": 429
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
        name: limit-conn-route
        plugins:
          limit-conn:
            conn: 2
            burst: 1
            default_conn_delay: 0.1
            key_type: var
            key: remote_addr
            policy: local
            rejected_code: 429
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

limit-conn-ic.yaml

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
  name: limit-conn-plugin-config
spec:
  plugins:
    - name: limit-conn
      config:
        conn: 2
        burst: 1
        default_conn_delay: 0.1
        key_type: var
        key: remote_addr
        policy: local
        rejected_code: 429
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: limit-conn-route
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
            name: limit-conn-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

limit-conn-ic.yaml

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
  name: limit-conn-route
spec:
  ingressClassName: apisix
  http:
    - name: limit-conn-route
      match:
        paths:
          - /get
        methods:
          - GET
      upstreams:
        - name: httpbin-external-domain
      plugins:
        - name: limit-conn
          config:
            conn: 2
            burst: 1
            default_conn_delay: 0.1
            key_type: var
            key: remote_addr
            policy: local
            rejected_code: 429
```

Apply the configuration:

```
kubectl apply -f limit-conn-ic.yaml
```

â¶ `conn`: allow 2 concurrent requests.

â· `burst`: allow 1 excessive concurrent request.

â¸ `default_conn_delay`: Allow 0.1 second of processing latency for concurrent requests exceeding `conn + burst`.

â¹ `key_type`: set to `vars` to interpret `key` as a variable.

âº `key`: calculate rate limiting count by request's `remote_address`.

â» `policy`: use the local counter in memory.

â¼ `rejected_code`: set the rejection status code to `429`.

Send five concurrent requests to the route:

```
seq 1 5 | xargs -n1 -P5 bash -c 'curl -s -o /dev/null -w "Response: %{http_code}\n" "http://127.0.0.1:9080/get"'
```

You should see responses similar to the following, where excessive requests are rejected:

```
Response: 200
Response: 200
Response: 200
Response: 429
Response: 429
```

### Apply Rate Limiting by Remote Address and Consumer Name[â](#apply-rate-limiting-by-remote-address-and-consumer-name "Direct link to Apply Rate Limiting by Remote Address and Consumer Name")

The following example demonstrates how to use `limit-conn` to rate limit requests by a combination of variables, `remote_addr` and `consumer_name`.

* Admin API
* ADC
* Ingress Controller

Create consumer `john`:

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

Create a route with `key-auth` and `limit-conn` plugins:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "limit-conn-route",
    "uri": "/get",
    "plugins": {
      "key-auth": {},
      "limit-conn": {
        "conn": 2,
        "burst": 1,
        "default_conn_delay": 0.1,
        "rejected_code": 429,
        "policy": "local",
        "key_type": "var_combination",
        "key": "$remote_addr $consumer_name"
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
  - name: limit-conn-service
    routes:
      - name: limit-conn-route
        uris:
          - /get
        plugins:
          key-auth: {}
          limit-conn:
            conn: 2
            burst: 1
            default_conn_delay: 0.1
            rejected_code: 429
            policy: local
            key_type: var_combination
            key: "$remote_addr $consumer_name"
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

limit-conn-ic.yaml

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
  name: limit-conn-plugin-config
spec:
  plugins:
    - name: key-auth
      config:
        _meta:
          disable: false
    - name: limit-conn
      config:
        conn: 2
        burst: 1
        default_conn_delay: 0.1
        rejected_code: 429
        policy: local
        key_type: var_combination
        key: "$remote_addr $consumer_name"
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: limit-conn-route
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
            name: limit-conn-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

limit-conn-ic.yaml

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
  name: limit-conn-route
spec:
  ingressClassName: apisix
  http:
    - name: limit-conn-route
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
        - name: limit-conn
          config:
            conn: 2
            burst: 1
            default_conn_delay: 0.1
            rejected_code: 429
            policy: local
            key_type: var_combination
            key: "$remote_addr $consumer_name"
```

Apply the configuration:

```
kubectl apply -f limit-conn-ic.yaml
```

â¶ `key-auth`: enable key authentication on the route.

â· `key_type`: set to `var_combination` to interpret the `key` as a combination of variables.

â¸ `key`: set to `$remote_addr $consumer_name` to apply rate limiting quota by remote address and consumer.

Send five concurrent requests as the consumer `john`:

```
seq 1 5 | xargs -n1 -P5 bash -c 'curl -s -o /dev/null -w "Response: %{http_code}\n" "http://127.0.0.1:9080/get" -H "apikey: john-key"'
```

You should see responses similar to the following, where excessive requests are rejected:

```
Response: 200
Response: 200
Response: 200
Response: 429
Response: 429
```

Immediately send five concurrent requests as the consumer `jane`:

```
seq 1 5 | xargs -n1 -P5 bash -c 'curl -s -o /dev/null -w "Response: %{http_code}\n" "http://127.0.0.1:9080/get" -H "apikey: jane-key"'
```

You should also see responses similar to the following, where excessive requests are rejected:

```
Response: 200
Response: 200
Response: 200
Response: 429
Response: 429
```

In this case, the plugin rate limits by the combination of variables `remote_addr` and `consumer_name`, which means each consumer's quota is independent.

### Rate Limit WebSocket Connections[â](#rate-limit-websocket-connections "Direct link to Rate Limit WebSocket Connections")

The following example demonstrates how you can use the `limit-conn` plugin to limit the number of concurrent WebSocket connections.

Start a [sample upstream WebSocket server](https://hub.docker.com/r/jmalloc/echo-server):

* Docker
* Kubernetes

```
docker run -d \
  -p 8080:8080 \
  --name websocket-server \
  --network=apisix-quickstart-net \
  jmalloc/echo-server
```

Create a Kubernetes manifest file for the deployment of WebSocket server:

ws-deployment.yaml

```
apiVersion: apps/v1
kind: Deployment
metadata:
  namespace: aic
  name: websocket-server
spec:
  replicas: 1
  selector:
    matchLabels:
      app: websocket-server
  template:
    metadata:
      labels:
        app: websocket-server
    spec:
      containers:
      - name: echo-server
        image: jmalloc/echo-server
        ports:
        - containerPort: 8080
```

Create another Kubernetes manifest file for the WebSocket service:

ws-service.yaml

```
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: websocket-server
spec:
  selector:
    app: websocket-server
  ports:
  - protocol: TCP
    port: 8080
    targetPort: 8080
    appProtocol: kubernetes.io/ws
  type: ClusterIP
```

Gateway API and WebSocket

For Gateway API, WebSocket support is enabled through the Service's `appProtocol` field (`kubernetes.io/ws` or `kubernetes.io/wss`). Unlike ApisixRoute, there is no direct `websocket` field or annotation support in HTTPRoute. Ensure that your Service is configured with `appProtocol` if you are working with Gateway API resources.

See [Detect Upstream Protocol with appProtocol](https://docs.api7.ai/ingress-controller/detect-upstream-protocol-appprotocol.md) for more information.

The server has a WebSocket endpoint at `/.ws` that echoes back any message received.

Create a route to the server WebSocket endpoint and enable WebSocket for the route:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "ws-route",
  "uri": "/.ws",
  "plugins": {
    "limit-conn": {
      "conn": 2,
      "burst": 1,
      "default_conn_delay": 0.1,
      "key_type": "var",
      "key": "remote_addr",
      "rejected_code": 429,
      "policy": "local"
    }
  },
  "enable_websocket": true,
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "websocket-server:8080": 1
    }
  }
}'
```

â¶ Enable WebSocket for the route.

â· Replace with your WebSocket server address.

adc.yaml

```
services:
  - name: websocket-service
    routes:
      - name: ws-route
        uris:
          - /.ws
        enable_websocket: true
        plugins:
          limit-conn:
            conn: 2
            burst: 1
            default_conn_delay: 0.1
            key_type: var
            key: remote_addr
            rejected_code: 429
            policy: local
    upstream:
      type: roundrobin
      nodes:
        - host: websocket-server
          port: 8080
          weight: 1
```

â¶ Enable WebSocket for the route.

â· Replace with your WebSocket server address.

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

* Gateway API
* APISIX CRD

limit-conn-ic.yaml

```
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: limit-conn-plugin-config
spec:
  plugins:
    - name: limit-conn
      config:
        conn: 2
        burst: 1
        default_conn_delay: 0.1
        key_type: var
        key: remote_addr
        rejected_code: 429
        policy: local
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: ws-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /.ws
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: limit-conn-plugin-config
      backendRefs:
        - name: websocket-server
          port: 8080
```

limit-conn-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: ws-route
spec:
  ingressClassName: apisix
  http:
    - name: ws-route
      match:
        paths:
          - /.ws
        methods:
          - GET
      websocket: true
      backends:
        - serviceName: websocket-server
          servicePort: 8080
      plugins:
        - name: limit-conn
          config:
            conn: 2
            burst: 1
            default_conn_delay: 0.1
            key_type: var
            key: remote_addr
            rejected_code: 429
            policy: local
```

Apply the configuration:

```
kubectl apply -f limit-conn-ic.yaml
```

Install a WebSocket client, such as [websocat](https://github.com/vi/websocat), if you have not already. Establish connection with the WebSocket server through the route:

```
websocat "ws://127.0.0.1:9080/.ws"
```

Send a "hello" message in the terminal, you should see the WebSocket server echoes back the same message:

```
Request served by 1cd244052136
hello
hello
```

Open three more terminal sessions and run:

```
websocat "ws://127.0.0.1:9080/.ws"
```

You should see the last terminal session prints `429 Too Many Requests` when you try to establish a WebSocket connection with the server, due to the rate limiting effect.

### Share Quota Among APISIX Nodes with a Redis Server[â](#share-quota-among-apisix-nodes-with-a-redis-server "Direct link to Share Quota Among APISIX Nodes with a Redis Server")

The following example demonstrates the rate limiting of requests across multiple APISIX nodes with a Redis server, such that different APISIX nodes share the same rate limiting quota.

On each APISIX instance, create a route with the following configurations. Adjust the configuration details accordingly.

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "limit-conn-route",
    "uri": "/get",
    "plugins": {
      "limit-conn": {
        "conn": 1,
        "burst": 1,
        "default_conn_delay": 0.1,
        "rejected_code": 429,
        "key_type": "var",
        "key": "remote_addr",
        "policy": "redis",
        "redis_host": "192.168.xxx.xxx",
        "redis_port": 6379,
        "redis_password": "p@ssw0rd",
        "redis_database": 1
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
        name: limit-conn-route
        plugins:
          limit-conn:
            conn: 1
            burst: 1
            default_conn_delay: 0.1
            rejected_code: 429
            key_type: var
            key: remote_addr
            policy: redis
            redis_host: "192.168.xxx.xxx"
            redis_port: 6379
            redis_password: "p@ssw0rd"
            redis_database: 1
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

limit-conn-ic.yaml

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
  name: limit-conn-plugin-config
spec:
  plugins:
    - name: limit-conn
      config:
        conn: 1
        burst: 1
        default_conn_delay: 0.1
        rejected_code: 429
        key_type: var
        key: remote_addr
        policy: redis
        redis_host: "redis-service.aic.svc"
        redis_port: 6379
        redis_password: "p@ssw0rd"
        redis_database: 1
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: limit-conn-route
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
            name: limit-conn-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

limit-conn-ic.yaml

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
  name: limit-conn-route
spec:
  ingressClassName: apisix
  http:
    - name: limit-conn-route
      match:
        paths:
          - /get
        methods:
          - GET
      upstreams:
        - name: httpbin-external-domain
      plugins:
        - name: limit-conn
          config:
            conn: 1
            burst: 1
            default_conn_delay: 0.1
            rejected_code: 429
            key_type: var
            key: remote_addr
            policy: redis
            redis_host: "redis-service.aic.svc"
            redis_port: 6379
            redis_password: "p@ssw0rd"
            redis_database: 1
```

Apply the configuration:

```
kubectl apply -f limit-conn-ic.yaml
```

â¶ `policy`: set to `redis` to use a Redis instance for rate limiting.

â· `redis_host`: set to Redis instance IP address.

â¸ `redis_port`: set to Redis instance listening port.

â¹ `redis_password`: set to the password of the Redis instance, if any.

âº `redis_database`: set to the database number in the Redis instance.

Send five concurrent requests to the route:

```
seq 1 5 | xargs -n1 -P5 bash -c 'curl -s -o /dev/null -w "Response: %{http_code}\n" "http://127.0.0.1:9080/get"'
```

You should see responses similar to the following, where excessive requests are rejected:

```
Response: 200
Response: 200
Response: 429
Response: 429
Response: 429
```

This shows the two routes configured in different APISIX instances share the same quota.

### Share Quota Among APISIX Nodes with a Redis Cluster[â](#share-quota-among-apisix-nodes-with-a-redis-cluster "Direct link to Share Quota Among APISIX Nodes with a Redis Cluster")

You can also use a Redis cluster to apply the same quota across multiple APISIX nodes, such that different APISIX nodes share the same rate limiting quota.

Ensure that your Redis instances are running in [cluster mode](https://redis.io/docs/management/scaling/#create-and-use-a-redis-cluster). A minimum of two nodes are required for the `limit-conn` plugin configurations.

On each APISIX instance, create a route with the following configurations. Adjust the configuration details accordingly.

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "limit-conn-route",
    "uri": "/get",
    "plugins": {
      "limit-conn": {
        "conn": 1,
        "burst": 1,
        "default_conn_delay": 0.1,
        "rejected_code": 429,
        "key_type": "var",
        "key": "remote_addr",
        "policy": "redis-cluster",
        "redis_cluster_nodes": [
          "192.168.xxx.xxx:6379",
          "192.168.xxx.xxx:16379"
        ],
        "redis_password": "p@ssw0rd",
        "redis_cluster_name": "redis-cluster",
        "redis_cluster_ssl": true
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
        name: limit-conn-route
        plugins:
          limit-conn:
            conn: 1
            burst: 1
            default_conn_delay: 0.1
            rejected_code: 429
            key_type: var
            key: remote_addr
            policy: redis-cluster
            redis_cluster_nodes:
              - "192.168.xxx.xxx:6379"
              - "192.168.xxx.xxx:16379"
            redis_password: "p@ssw0rd"
            redis_cluster_name: "redis-cluster"
            redis_cluster_ssl: true
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

limit-conn-ic.yaml

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
  name: limit-conn-plugin-config
spec:
  plugins:
    - name: limit-conn
      config:
        conn: 1
        burst: 1
        default_conn_delay: 0.1
        rejected_code: 429
        key_type: var
        key: remote_addr
        policy: redis-cluster
        redis_cluster_nodes:
          - "redis-cluster-0.redis-cluster.aic.svc:6379"
          - "redis-cluster-1.redis-cluster.aic.svc:6379"
        redis_password: "p@ssw0rd"
        redis_cluster_name: "redis-cluster"
        redis_cluster_ssl: true
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: limit-conn-route
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
            name: limit-conn-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

limit-conn-ic.yaml

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
  name: limit-conn-route
spec:
  ingressClassName: apisix
  http:
    - name: limit-conn-route
      match:
        paths:
          - /get
        methods:
          - GET
      upstreams:
        - name: httpbin-external-domain
      plugins:
        - name: limit-conn
          config:
            conn: 1
            burst: 1
            default_conn_delay: 0.1
            rejected_code: 429
            key_type: var
            key: remote_addr
            policy: redis-cluster
            redis_cluster_nodes:
              - "redis-cluster-0.redis-cluster.aic.svc:6379"
              - "redis-cluster-1.redis-cluster.aic.svc:6379"
            redis_password: "p@ssw0rd"
            redis_cluster_name: "redis-cluster"
            redis_cluster_ssl: true
```

Apply the configuration:

```
kubectl apply -f limit-conn-ic.yaml
```

â¶ `policy`: set to `redis-cluster` to use a Redis cluster for rate limiting.

â· `redis_cluster_nodes`: set to Redis node addresses in the Redis cluster.

â¸ `redis_password`: set to the password of the Redis cluster, if any.

â¹ `redis_cluster_name`: set to the Redis cluster name.

â `redis_cluster_ssl`: enable SSL/TLS communication with Redis cluster.

Send five concurrent requests to the route:

```
seq 1 5 | xargs -n1 -P5 bash -c 'curl -s -o /dev/null -w "Response: %{http_code}\n" "http://127.0.0.1:9080/get"'
```

You should see responses similar to the following, where excessive requests are rejected:

```
Response: 200
Response: 200
Response: 429
Response: 429
Response: 429
```

This shows the two routes configured in different APISIX instances share the same quota.

### Rate Limit by Rules[â](#rate-limit-by-rules "Direct link to Rate Limit by Rules")

The following example demonstrates how you can configure `limit-conn` to apply different rate-limiting rules (available from API7 Enterprise 3.8.17) based on request attributes. In this example, rate limits are applied based on HTTP header values that represent the callerâs access tier.

Note that all rules are applied sequentially. If a configured key does not exist, the corresponding rule will be skipped.

tip

In addition to HTTP headers, you can also base rules on other [built-in variables](https://docs.api7.ai/enterprise/reference/built-in-variables.md) to implement more flexible and fine-grained rate-limiting strategies.

Create a route with the `limit-conn` plugin that applies different rate limits based on request headers, allowing requests to be rate limited per subscription (`X-Subscription-ID`) and enforcing a stricter limit for trial users (`X-Trial-ID`):

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "limit-conn-rules-route",
    "uri": "/get",
    "plugins": {
      "limit-conn": {
        "rejected_code": 429,
        "default_conn_delay": 0.1,
        "policy": "local",
        "rules": [
          {
            "key": "${http_x_subscription_id}",
            "conn": "${http_x_custom_conn ?? 5}",
            "burst": 1
          },
          {
            "key": "${http_x_trial_id}",
            "conn": 1,
            "burst": 1
          }
        ]
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
        name: limit-conn-rules-route
        plugins:
          limit-conn:
            rejected_code: 429
            default_conn_delay: 0.1
            policy: local
            rules:
              - key: "${http_x_subscription_id}"
                conn: "${http_x_custom_conn ?? 5}"
                burst: 1
              - key: "${http_x_trial_id}"
                conn: 1
                burst: 1
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

limit-conn-ic.yaml

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
  name: limit-conn-plugin-config
spec:
  plugins:
    - name: limit-conn
      config:
        rejected_code: 429
        default_conn_delay: 0.1
        policy: local
        rules:
          - key: "${http_x_subscription_id}"
            conn: "${http_x_custom_conn ?? 5}"
            burst: 1
          - key: "${http_x_trial_id}"
            conn: 1
            burst: 1
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: limit-conn-rules-route
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
            name: limit-conn-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

limit-conn-ic.yaml

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
  name: limit-conn-rules-route
spec:
  ingressClassName: apisix
  http:
    - name: limit-conn-rules-route
      match:
        paths:
          - /get
        methods:
          - GET
      upstreams:
        - name: httpbin-external-domain
      plugins:
        - name: limit-conn
          config:
            rejected_code: 429
            default_conn_delay: 0.1
            policy: local
            rules:
              - key: "${http_x_subscription_id}"
                conn: "${http_x_custom_conn ?? 5}"
                burst: 1
              - key: "${http_x_trial_id}"
                conn: 1
                burst: 1
```

Apply the configuration:

```
kubectl apply -f limit-conn-ic.yaml
```

â¶ Use the value of the `X-Subscription-ID` request header as the rate-limiting key.

â· Set the request connection dynamically based on the `X-Custom-Conn` header. If the header is not provided, a default concurrent connection count of 5 is applied.

â¸ Use the value of the `X-Trial-ID` request header as the rate-limiting key.

To verify rate limiting, send 7 concurrent requests to the route with the same subscription ID:

```
seq 1 7 | xargs -n1 -P7 bash -c 'curl -s -o /dev/null -w "Response: %{http_code}\n" "http://127.0.0.1:9080/get" -H "X-Subscription-ID: sub-123456789"'
```

You should see the following response, which shows that the default concurrent connection limit of 5 with a burst of 1 is applied when the `X-Custom-Conn` header is not provided:

```
Response: 429
Response: 200
Response: 200
Response: 200
Response: 200
Response: 200
Response: 200
```

Send 5 concurrent requests to the route with the same subscription ID and set the `X-Custom-Conn` header to 1:

```
seq 1 5 | xargs -n1 -P5 bash -c 'curl -s -o /dev/null -w "Response: %{http_code}\n" "http://127.0.0.1:9080/get" -H "X-Subscription-ID: sub-123456789" -H "X-Custom-Conn: 1"'
```

You should see the following response, which shows that the concurrent connection limit of 1 with a burst of 1 is applied:

```
Response: 429
Response: 429
Response: 429
Response: 200
Response: 200
```

Finally, generate 5 requests to the route with the trial ID header:

```
seq 1 5 | xargs -n1 -P5 bash -c 'curl -s -o /dev/null -w "Response: %{http_code}\n" "http://127.0.0.1:9080/get" -H "X-Trial-ID: trial-123456789"'
```

You should see the following response, which shows that the concurrent connection limit of 1 with a burst of 1 is applied:

```
Response: 429
Response: 429
Response: 429
Response: 200
Response: 200
```
