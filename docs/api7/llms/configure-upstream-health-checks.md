# Source: https://docs.api7.ai/ingress-controller/configure-upstream-health-checks.md

# Configure Upstream Health Checks

Health checking is a mechanism that determines whether upstream services are healthy or unhealthy based on their responsiveness. With health checks enabled, the gateway will only forward requests to upstream services that are considered healthy and will not forward requests to services that are considered unhealthy.

There are two general approaches to health check:

* **Active checks**: the gateway proactively and periodically sends requests to upstream services and determines the health of those based on the responses to these requests.
* **Passive checks**: the gateway determines the health of upstream services based on how they respond to client requests, without proactively probing.

This guide will show you how to configure both active and passive health checks for your upstream services using the Ingress Controller.

known issue

If you are using the APISIX Ingress Controller RC5 with APISIX in standalone mode, there is currently an issue where the Control API does not return health check data. This issue does not occur when APISIX is running in traditional mode with etcd.

## Prerequisite[â](#prerequisite "Direct link to Prerequisite")

1. Complete [Set Up Ingress Controller and Gateway](https://docs.api7.ai/ingress-controller/set-up-ingress-controller-and-gateway.md).

## Start Example Upstream Services[â](#start-example-upstream-services "Direct link to Start Example Upstream Services")

Create a Kubernetes manifest file for the deployment of two NGINX instances as example upstream services:

nginx.yaml

```
apiVersion: apps/v1
kind: Deployment
metadata:
  namespace: aic
  name: nginx1
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx1
  template:
    metadata:
      labels:
        app: nginx1
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: nginx1
spec:
  selector:
    app: nginx1
  ports:
    - port: 8080
      targetPort: 80
---
apiVersion: apps/v1
kind: Deployment
metadata:
  namespace: aic
  name: nginx2
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx2
  template:
    metadata:
      labels:
        app: nginx2
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: nginx2
spec:
  selector:
    app: nginx2
  ports:
    - port: 8081
      targetPort: 80
```

Apply the configuration to your cluster:

```
kubectl apply -f nginx.yaml
```

Expose the NGINX service ports to your local machine by port forwarding:

```
kubectl port-forward svc/nginx1 8080:8080 &
kubectl port-forward svc/nginx2 8081:8081 &
```

Verify both NGINX instances are running:

```
for port in 8080 8081; do
  curl -s "http://127.0.0.1:$port" | grep -q "Welcome to nginx" &&
  echo "NGINX welcome page available on port $port."
done
```

You should see the following response:

```
NGINX welcome page available on port 8080.
NGINX welcome page available on port 8081.
```

## Enable Control API[â](#enable-control-api "Direct link to Enable Control API")

Upgrade your gateway to enable Control API.

* APISIX Gateway
* API7 Gateway

Export all values (including defaults):

```
helm get values -n aic apisix --all > values.yaml
```

In the values file, update the following section values as such:

values.yaml

```
apisix:
  enabled: true
control:
  enabled: true
```

Upgrade the release:

```
helm upgrade -n aic apisix apisix/apisix -f values.yaml
```

Port-forward the Control API port:

```
kubectl port-forward service/apisix-control 9090:9090 &
```

By default, the Control API is enabled on port `9090`:

values.yaml

```
control:
  enabled: true
  ip: 127.0.0.1
  port: 9090
```

Port-forward the Control API port:

```
kubectl port-forward pod/<api7-gateway-pod-name> 9090:9090 &
```

## Configure Active Health Checks[â](#configure-active-health-checks "Direct link to Configure Active Health Checks")

Active checks determine the health of upstream services by periodically sending requests, or probes, to the services and seeing how they respond.

In this section, you will find two examples to understand:

* How changes in upstream statuses can be detected by active checks.
* How the gateway forwards client requests to upstream services when all upstream statuses are unhealthy.

### Example: Status Change in Upstream Services[â](#example-status-change-in-upstream-services "Direct link to Example: Status Change in Upstream Services")

The following example demonstrates how the active health checks respond in situations where healthy upstream services have become: partially unavailable, all unavailable, and all recovered.

Create a route to the two services and configure active health checks that run every 2 seconds:

* Gateway API
* APISIX CRD

The Ingress Controller currently does not support using Gateway API to configure upstream health checks.

active-health-checks.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: nginx
spec:
  ingressClassName: apisix
  externalNodes:
  - type: Service
    name: nginx1
    port: 8080
  - type: Service
    name: nginx2
    port: 8081
  healthCheck:
    active:
      type: http
      httpPath: /
      healthy:
        interval: 2s
        successes: 1
      unhealthy:
        interval: 1s
        timeout: 3
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: example-hc-route
spec:
  ingressClassName: apisix
  http:
  - name: nginx-hc
    match:
      paths:
      - /
    upstreams:
    - name: nginx
```

â¶ `type`: the type of active health checks.

â· `httpPath`: the HTTP request path to actively probe.

â¸ `healthy.interval`: the time interval in seconds for periodically checking healthy nodes.

â¹ `healthy.successes`: the success count threshold for ruling if an upstream node is considered healthy.

âº `unhealthy.interval`: the time interval in seconds for periodically checking unhealthy nodes.

â» `unhealthy.timeout`: the timeout count threshold for ruling if an upstream node is considered unhealthy.

Apply the configuration to your cluster:

```
kubectl apply -f active-health-checks.yaml
```

### Verify[â](#verify "Direct link to Verify")

You will be verifying the above configurations to understand how the upstream health checks respond in different scenarios:

* when [all upstream services are healthy](#verify-both-upstream-services-are-healthy)
* when [only partial services are healthy](#verify-when-one-upstream-service-is-unavailable)
* when [none of the services is healthy](#verify-both-upstream-services-are-unavailable)
* when [all services are recovered](#verify-both-upstream-services-are-recovered)

Before proceeding, expose the gatewayâs service port to your local machine:

```
# replace with your gatewayâs service name
kubectl port-forward svc/<gateway-service-name> 9080:80 &
```

#### Verify Both Upstream Services Are Healthy[â](#verify-both-upstream-services-are-healthy "Direct link to Verify Both Upstream Services Are Healthy")

Send a request to the route to start health checks:

```
curl "http://127.0.0.1:9080/"
```

To see upstream health statuses, send a request to the health check endpoint in [Control API](https://docs.api7.ai/apisix/reference/control-api/.md):

```
curl "http://127.0.0.1:9090/v1/healthcheck"
```

You should see a response similar to the following:

```
[
  {
    "name": "/apisix/routes/example-hc-route",
    "type": "http",
    "nodes": [
      {
        "port": 80,
        "counter": {
          "http_failure": 0,
          "tcp_failure": 0,
          "timeout_failure": 0,
          "success": 0
        },
        "ip": "172.24.0.5",
        "status": "healthy"
      },
      {
        "port": 80,
        "counter": {
          "http_failure": 0,
          "tcp_failure": 0,
          "timeout_failure": 0,
          "success": 0
        },
        "ip": "172.24.0.4",
        "status": "healthy"
      }
    ]
  }
]
```

#### Verify When One Upstream Service Is Unavailable[â](#verify-when-one-upstream-service-is-unavailable "Direct link to Verify When One Upstream Service Is Unavailable")

Make one upstream service temporarily unavailable to verify if the gateway reports one of the upstream services unhealthy:

```
kubectl scale deployment nginx1 -n aic --replicas=0
```

Wait for a few seconds and send a request to the health check endpoint:

```
curl "http://127.0.0.1:9090/v1/healthcheck"
```

You should see a response similar to the following, showing one of the upstream nodes has 3 timeout failures and marked unhealthy:

```
[
  {
    "name": "/apisix/routes/example-hc-route",
    "type": "http",
    "nodes": [
      {
        "port": 80,
        "counter": {
          "http_failure": 0,
          "tcp_failure": 0,
          "timeout_failure": 0,
          "success": 0
        },
        "ip": "172.24.0.5",
        "status": "healthy"
      },
      {
        "port": 80,
        "counter": {
          "http_failure": 0,
          "tcp_failure": 0,
          "timeout_failure": 3,
          "success": 0
        },
        "ip": "172.24.0.4",
        "status": "unhealthy"
      }
    ]
  }
]
```

Send a request to the route to see if the gateway forwards the request to the other healthy node:

```
curl -i "http://127.0.0.1:9080/"
```

You should receive an `HTTP/1.1 200 OK` response.

#### Verify Both Upstream Services Are Unavailable[â](#verify-both-upstream-services-are-unavailable "Direct link to Verify Both Upstream Services Are Unavailable")

Make the other upstream service temporarily unavailable to verify if the gateway reports both upstream services unhealthy:

```
kubectl scale deployment nginx2 -n aic --replicas=0
```

Wait for a few seconds and send a request to the health check endpoint:

```
curl "http://127.0.0.1:9090/v1/healthcheck"
```

You should see a response similar to the following, showing both upstream nodes have 3 timeout failures and marked unhealthy:

```
[
  {
    "name": "/apisix/routes/example-hc-route",
    "type": "http",
    "nodes": [
      {
        "port": 80,
        "counter": {
          "http_failure": 0,
          "tcp_failure": 0,
          "timeout_failure": 3,
          "success": 0
        },
        "ip": "172.24.0.5",
        "status": "unhealthy"
      },
      {
        "port": 80,
        "counter": {
          "http_failure": 0,
          "tcp_failure": 0,
          "timeout_failure": 3,
          "success": 0
        },
        "ip": "172.24.0.4",
        "status": "unhealthy"
      }
    ]
  }
]
```

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/"
```

You should receive an `HTTP/1.1 502 Bad Gateway` response.

#### Verify Both Upstream Services Are Recovered[â](#verify-both-upstream-services-are-recovered "Direct link to Verify Both Upstream Services Are Recovered")

Make both services available again to verify if the gateway reports both upstream services healthy:

```
kubectl scale deployment -n aic nginx1 nginx2 --replicas=1
```

Wait for a few seconds and send a request to the health check endpoint:

```
curl "http://127.0.0.1:9090/v1/healthcheck"
```

You should see a response showing both upstream nodes are healthy, similar to [when both services are healthy at the start](#verify-both-upstream-services-are-healthy).

### Example: Forward Requests When Statuses Are Unhealthy[â](#example-forward-requests-when-statuses-are-unhealthy "Direct link to Example: Forward Requests When Statuses Are Unhealthy")

The following example demonstrates that the gateway would still forward client requests to upstream services even when all upstream health statuses are unhealthy.

Create a route to the two services and configure active health checks that run every 2 seconds:

* Gateway API
* APISIX CRD

The Ingress Controller currently does not support using Gateway API to configure upstream health checks.

active-health-checks.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: nginx
spec:
  ingressClassName: apisix
  externalNodes:
  - type: Service
    name: nginx1
    port: 8080
  - type: Service
    name: nginx2
    port: 8081
  healthCheck:
    active:
      type: http
      httpPath: /404
      healthy:
        interval: 2s
        successes: 1
      unhealthy:
        interval: 1s
        httpFailures: 2
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: example-hc-route
spec:
  ingressClassName: apisix
  http:
  - name: nginx-hc
    match:
      paths:
      - /
    upstreams:
    - name: nginx
```

â¶ `type`: the type of active health checks.

â· `httpPath`: the HTTP request path to actively probe. For the convenience of demonstration, this is set to `/404`, which is a path that does not exist in upstream services. Consequently, both services should always be considered unhealthy by the active health checks.

â¸ `unhealthy.httpFailures`: the HTTP failure count threshold for ruling if an upstream node is considered unhealthy.

Apply the configuration to your cluster:

```
kubectl apply -f active-health-checks.yaml
```

### Verify[â](#verify-1 "Direct link to Verify")

Expose the gatewayâs service port to your local machine:

```
# replace with your gatewayâs service name
kubectl port-forward svc/<gateway-service-name> 9080:80 &
```

Send a request to the route to start health checks:

```
curl -i "http://127.0.0.1:9080/"
```

You should receive an `HTTP/1.1 200 OK` response.

Send a request to the health check endpoint:

```
curl "http://127.0.0.1:9090/v1/healthcheck"
```

You should see a response similar to the following:

```
[
  {
    "name": "/apisix/routes/example-hc-route",
    "nodes": [
      {
        "counter": {
          "timeout_failure": 0,
          "http_failure": 2,
          "success": 0,
          "tcp_failure": 0
        },
        "port": 80,
        "ip": "172.25.0.5",
        "status": "unhealthy"
      },
      {
        "counter": {
          "timeout_failure": 0,
          "http_failure": 2,
          "success": 0,
          "tcp_failure": 0
        },
        "port": 80,
        "ip": "172.25.0.4",
        "status": "unhealthy"
      }
    ],
    "type": "http"
  }
]
```

Send a request to the route to see if the gateway still forwards the request:

```
curl -i "http://127.0.0.1:9080/"
```

You should receive an `HTTP/1.1 200 OK` response. This verifies that the gateway would still forward client requests to upstream services, despite both services being marked as unhealthy.

## Configure Passive Health Checks[â](#configure-passive-health-checks "Direct link to Configure Passive Health Checks")

To use passive health checks, it is required that you should also configure active health checks. When an upstream service becomes unhealthy, the active health check is in place to periodically check if the upstream service has recovered.

known issue

There is a known issue in the gateway where the passive health check data displayed through the Control API do not accurately reflect the actual health statuses, so your testing results may differ from the example shown. This issue is being actively resolved. However, the passive health check mechanism itself is functioning correctly and continues to route requests as intended.

### Example: Status Change in Upstream Services[â](#example-status-change-in-upstream-services-1 "Direct link to Example: Status Change in Upstream Services")

Create a route to the two services, and configure both active and passive health checks:

* Gateway API
* APISIX CRD

The Ingress Controller currently does not support using Gateway API to configure upstream health checks.

passive-health-checks.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: nginx
spec:
  ingressClassName: apisix
  externalNodes:
  - type: Service
    name: nginx1
    port: 8080
  - type: Service
    name: nginx2
    port: 8081
  healthCheck:
    active:
      type: http
      httpPath: /
      healthy:
        interval: 99999s
        successes: 1
      unhealthy:
        interval: 30s
    passive:
      healthy:
        httpCodes: [200,201,202,300,301,302]
        successes: 1
      unhealthy:
        httpCodes: [429,404,500,501,502,503,504,505]
        httpFailures: 3
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: example-hc-route
spec:
  ingressClassName: apisix
  http:
  - name: nginx-hc
    match:
      paths:
      - /404
    upstreams:
    - name: nginx
```

â¶ `active.healthy.interval`: the time interval in seconds for periodically checking healthy nodes.

â· `active.unhealthy.interval`: the time interval in seconds for periodically checking unhealthy nodes.

â¸ `passive.healthy.httpCodes`: the response HTTP status codes that are considered healthy.

â¹ `passive.unhealthy.httpCodes`: the response HTTP status codes that are considered unhealthy. The unhealthy responses are counted towards the `httpFailures`.

âº `passive.unhealthy.httpFailures`: the HTTP failure count threshold for ruling if an upstream node is considered unhealthy.

â» `paths`: the URI paths that the route matches. For the convenience of demonstration, this is set to `/404`, which is a path that does not exist in upstream services. Consequently, when a request is made, both upstream services should respond with a `404` status code.

Apply the configuration to your cluster:

```
kubectl apply -f passive-health-checks.yaml
```

### Verify[â](#verify-2 "Direct link to Verify")

Expose the gatewayâs service port to your local machine:

```
# replace with your gatewayâs service name
kubectl port-forward svc/<gateway-service-name> 9080:80 &
```

Send a request to the route to start health checks:

```
curl -i "http://127.0.0.1:9080/404"
```

You should see an `HTTP/1.1 404 Not Found` response.

Send a request to the health check endpoint:

```
curl "http://127.0.0.1:9090/v1/healthcheck"
```

You should see a response similar to the following:

```
[
  {
    "name": "/apisix/routes/example-hc-route",
    "nodes": [
      {
        "counter": {
          "timeout_failure": 0,
          "http_failure": 1,
          "success": 0,
          "tcp_failure": 0
        },
        "port": 80,
        "ip": "172.25.0.5",
        "status": "mostly_healthy"
      },
      {
        "counter": {
          "timeout_failure": 0,
          "http_failure": 0,
          "success": 0,
          "tcp_failure": 0
        },
        "port": 80,
        "ip": "172.25.0.4",
        "status": "healthy"
      }
    ],
    "type": "http"
  }
]
```

â¶ `http_failure` has a count of 1 due to the previous request with a 404 response.

â· `mostly_healthy` status means the current node status is healthy, but the gateway starts to receive unhealthy indications during health checks.

Generate consecutive requests to invoke `404` responses:

```
resp=$(seq 10 | xargs -I{} curl "http://127.0.0.1:9080/404" -o /dev/null -s -w "%{http_code}\n") && \
  count=$(echo "$resp" | grep "404" | wc -l) && \
  echo "Invoked $count responses with 404 status code."
```

Send a request to the health check endpoint:

```
curl "http://127.0.0.1:9090/v1/healthcheck"
```

You should see a response similar to the following:

```
[
  {
    "name": "/apisix/routes/example-hc-route",
    "nodes": [
      {
        "counter": {
          "timeout_failure": 0,
          "http_failure": 3,
          "success": 0,
          "tcp_failure": 0
        },
        "port": 80,
        "ip": "172.25.0.4",
        "status": "unhealthy"
      },
      {
        "counter": {
          "timeout_failure": 0,
          "http_failure": 4,
          "success": 0,
          "tcp_failure": 0
        },
        "port": 80,
        "ip": "172.25.0.5",
        "status": "unhealthy"
      }
    ],
    "type": "http"
  }
]
```

Wait at least 30 seconds for active checks to probe the upstream services at `/` and mark them as healthy. Then, send a request to the health check endpoint:

```
curl "http://127.0.0.1:9090/v1/healthcheck"
```

You should see a response similar to the following:

```
[
  {
    "name": "/apisix/routes/example-hc-route",
    "nodes": [
      {
        "counter": {
          "timeout_failure": 0,
          "http_failure": 0,
          "success": 1,
          "tcp_failure": 0
        },
        "port": 80,
        "ip": "172.25.0.4",
        "status": "healthy"
      },
      {
        "counter": {
          "timeout_failure": 0,
          "http_failure": 0,
          "success": 1,
          "tcp_failure": 0
        },
        "port": 80,
        "ip": "172.25.0.5",
        "status": "healthy"
      }
    ],
    "type": "http"
  }
]
```
