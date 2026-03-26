# Source: https://docs.api7.ai/apisix/how-to-guide/traffic-management/health-check.md

# Configure Upstream Health Checks

Health checking is a mechanism that determines whether upstream services are healthy or unhealthy based on their responsiveness. With health checks enabled, APISIX will only forward requests to upstream services that are considered healthy and will not forward requests to services that are considered unhealthy.

There are two general approaches to health check:

* **Active checks**: APISIX proactively and periodically sends requests to upstream services and determines the health of those based on the responses to these requests.
* **Passive checks**: APISIX determines the health of upstream services based on how they respond to client requests, without proactively probing.

This guide will show you how to configure both active and passive health checks for your upstream services.

note

If you are using the APISIX Ingress Controller RC5 with APISIX in standalone mode, there is currently an issue where the Control API does not return health check data. This issue does not occur when APISIX is running in traditional mode with etcd.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Start Sample Upstream Services[â](#start-sample-upstream-services "Direct link to Start Sample Upstream Services")

Start two NGINX instances as sample upstream services in the same Docker network as APISIX:

```
DOCKER_NETWORK=apisix-quickstart-net
docker run -d -p 8080:80 --network=${DOCKER_NETWORK} --name nginx1 nginx
docker run -d -p 8081:80 --network=${DOCKER_NETWORK} --name nginx2 nginx
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

## Configure Active Health Checks[â](#configure-active-health-checks "Direct link to Configure Active Health Checks")

Active checks determine the health of upstream services by periodically sending requests, or probes, to the services and seeing how they respond.

In this section, you will find two examples with verification steps, to understand:

* how changes in upstream statuses can be detected by active checks
* how APISIX forwards client requests to upstream services when all upstream statuses are unhealthy

### Example: Status Change in Upstream Services[â](#example-status-change-in-upstream-services "Direct link to Example: Status Change in Upstream Services")

The following example demonstrates how APISIX active health checks respond in situations where healthy upstream services have become: partially unavailable, all unavailable, and all recovered.

Create a route to the two services and configure active health checks that run every 2 seconds:

* Admin API
* ADC

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "example-hc-route",
  "uri":"/",
  "upstream": {
    "type":"roundrobin",
    "nodes": {
      "nginx1:80": 1,
      "nginx2:80": 1
    },
    "checks": {
      "active": {
        "type": "http",
        "http_path": "/",
        "healthy": {
          "interval": 2,
          "successes": 1
        },
        "unhealthy": {
          "interval": 1,
          "timeouts": 3
        }
      }
    }
  }
}'
```

â¶ `type`: the type of active health checks.

â· `http_path`: the HTTP request path to actively probe.

â¸ `healthy.interval`: the time interval in seconds for periodically checking healthy nodes.

â¹ `healthy.successes`: the success count threshold for ruling if an upstream node is considered healthy.

âº `unhealthy.interval`: the time interval in seconds for periodically checking unhealthy nodes.

â» `unhealthy.timeouts`: the timeout count threshold for ruling if an upstream node is considered unhealthy.

adc.yaml

```
services:
  - name: Nginx Service
    routes:
      - uris:
          - /
        name: example-hc-route
    upstream:
      type: roundrobin
      nodes:
        - host: nginx1
          port: 80
          weight: 1
        - host: nginx2
          port: 80
          weight: 1
      checks:
        active:
          type: http
          http_path: /
          healthy:
            interval: 2
            successes: 1
          unhealthy:
            interval: 1
            timeouts: 3
```

â¶ `type`: the type of active health checks.

â· `http_path`: the HTTP request path to actively probe.

â¸ `healthy.interval`: the time interval in seconds for periodically checking healthy nodes.

â¹ `healthy.successes`: the success count threshold for ruling if an upstream node is considered healthy.

âº `unhealthy.interval`: the time interval in seconds for periodically checking unhealthy nodes.

â» `unhealthy.timeouts`: the timeout count threshold for ruling if an upstream node is considered unhealthy.

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

### Verify[â](#verify "Direct link to Verify")

You will be verifying the above configurations to understand how APISIX upstream health checks respond in different scenarios:

* when [all upstream services are healthy](#verify-both-upstream-services-are-healthy)
* when [only partial services are healthy](#verify-when-one-upstream-service-is-unavailable)
* when [none of the services is healthy](#verify-both-upstream-services-are-unavailable)
* when [all services are recovered](#verify-both-upstream-services-are-recovered)

If you started APISIX in Docker with [Getting Started quickstart](https://docs.api7.ai/apisix/getting-started/.md#get-apisix), Control API port `9090` is already mapped (`-p 9090:9090`).

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

Make one upstream service temporarily unavailable to verify if APISIX reports one of the upstream services unhealthy:

```
docker container stop nginx1
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

Send a request to the route to see if APISIX forwards the request to the other healthy node:

```
curl -i "http://127.0.0.1:9080/"
```

You should receive an `HTTP/1.1 200 OK` response.

#### Verify Both Upstream Services Are Unavailable[â](#verify-both-upstream-services-are-unavailable "Direct link to Verify Both Upstream Services Are Unavailable")

Make the other upstream service temporarily unavailable to verify if APISIX reports both upstream services unhealthy:

```
docker container stop nginx2
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

Make both services available again to verify if APISIX reports both upstream services healthy:

```
docker container start nginx1 nginx2
```

Wait for a few seconds and send a request to the health check endpoint:

```
curl "http://127.0.0.1:9090/v1/healthcheck"
```

You should see a response showing both upstream nodes are healthy, similar to [when both services are healthy at the start](#verify-both-upstream-services-are-healthy).

### Example: Forward Requests When Statuses Are Unhealthy[â](#example-forward-requests-when-statuses-are-unhealthy "Direct link to Example: Forward Requests When Statuses Are Unhealthy")

The following example demonstrates that APISIX would still forward client requests to upstream services even when all upstream health statuses are unhealthy.

Create a route to the two services and configure active health checks that run every 2 seconds:

* Admin API
* ADC

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "example-hc-route",
  "uri":"/",
  "upstream": {
    "type":"roundrobin",
    "nodes": {
      "nginx1:80": 1,
      "nginx2:80": 1
    },
    "checks": {
      "active": {
        "type": "http",
        "http_path": "/404",
        "healthy": {
          "interval": 2,
          "successes": 1
        },
        "unhealthy": {
          "interval": 1,
          "http_failures": 2
        }
      }
    }
  }
}'
```

â¶ `type`: the type of active health checks.

â· `http_path`: the HTTP request path to actively probe. For the convenience of demonstration, this is set to `/404`, which is a path that does not exist in upstream services. Consequently, both services should always be considered unhealthy by the active health checks.

â¸ `unhealthy.http_failures`: the HTTP failure count threshold for ruling if an upstream node is considered unhealthy.

adc.yaml

```
services:
  - name: Nginx Service
    routes:
      - uris:
          - /
        name: example-hc-route
    upstream:
      type: roundrobin
      nodes:
        - host: nginx1
          port: 80
          weight: 1
        - host: nginx2
          port: 80
          weight: 1
      checks:
        active:
          type: http
          http_path: /404
          healthy:
            interval: 2
            successes: 1
          unhealthy:
            interval: 1
            http_failures: 3
```

â¶ `type`: the type of active health checks.

â· `http_path`: the HTTP request path to actively probe. For the convenience of demonstration, this is set to `/404`, which is a path that does not exist in upstream services. Consequently, both services should always be considered unhealthy by the active health checks.

â¸ `unhealthy.http_failures`: the HTTP failure count threshold for ruling if an upstream node is considered unhealthy.

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

### Verify[â](#verify-1 "Direct link to Verify")

If you started APISIX in Docker with [Getting Started quickstart](https://docs.api7.ai/apisix/getting-started/.md#get-apisix), Control API port `9090` is already mapped (`-p 9090:9090`).

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

Send a request to the route to see if APISIX still forwards the request:

```
curl -i "http://127.0.0.1:9080/"
```

You should receive an `HTTP/1.1 200 OK` response. This verifies that APISIX would still forward client requests to upstream services, despite both services being marked as unhealthy.

## Configure Passive Health Checks[â](#configure-passive-health-checks "Direct link to Configure Passive Health Checks")

APISIX requires the use of active health checks with passive health checks. When an upstream service becomes unhealthy, the active health check is in place to periodically check if the upstream service has recovered.

note

There is a known issue where the health check data displayed through the Control API does not accurately reflect the actual health statuses, so your testing results may differ from the example shown. The issue is being actively resolved. However, the passive health check mechanism itself is functioning correctly and continues to route requests as expected.

### Example: Status Change in Upstream Services[â](#example-status-change-in-upstream-services-1 "Direct link to Example: Status Change in Upstream Services")

Create a route to the two services, and configure both active and passive health checks:

* Admin API
* ADC

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "example-hc-route",
  "uri": "/404",
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "nginx1:80": 1,
      "nginx2:80": 1
    },
    "checks": {
      "active": {
        "type": "http",
        "http_path": "/",
        "healthy": {
          "interval": 99999,
          "successes": 1
        },
        "unhealthy": {
          "interval": 30
        }
      },
      "passive": {
        "healthy": {
          "http_statuses": [200,201,202,300,301,302],
          "successes": 1
        },
        "unhealthy": {
          "http_statuses": [429,404,500,501,502,503,504,505],
          "http_failures": 3
        }
      }
    }
  }
}'
```

â¶ `uri`: the URI path that the route matches. For the convenience of demonstration, this is set to `/404`, which is a path that does not exist in upstream services. Consequently, when a request is made, both upstream services should respond with a `404` status code.

â· `active.healthy.interval`: the time interval in seconds for periodically checking healthy nodes.

â¸ `active.unhealthy.interval`: the time interval in seconds for periodically checking unhealthy nodes.

â¹ `passive.healthy.http_statuses`: the response HTTP status codes that are considered healthy.

âº `passive.unhealthy.http_statuses`: the response HTTP status codes that are considered unhealthy. The unhealthy responses are counted towards the `http_failures`.

â» `passive.unhealthy.http_failures`: the HTTP failure count threshold for ruling if an upstream node is considered unhealthy.

adc.yaml

```
services:
  - name: Nginx Service
    routes:
      - uris:
          - /404
        name: example-hc-route
    upstream:
      type: roundrobin
      nodes:
        - host: nginx1
          port: 80
          weight: 1
        - host: nginx2
          port: 80
          weight: 1
      checks:
        active:
          type: http
          http_path: /
          healthy:
            interval: 99999
            successes: 1
          unhealthy:
            interval: 30
        passive:
          healthy:
            http_statuses:
              - 200
              - 201
              - 202
              - 300
              - 301
              - 302
            successes: 1
          unhealthy:
            http_statuses:
              - 429
              - 404
              - 500
              - 501
              - 502
              - 503
              - 504
              - 505
            http_failures: 3
```

â¶ `uris`: the URI paths that the route matches. For the convenience of demonstration, this is set to `/404`, which is a path that does not exist in upstream services. Consequently, when a request is made, both upstream services should respond with a `404` status code.

â· `active.healthy.interval`: the time interval in seconds for periodically checking healthy nodes.

â¸ `active.unhealthy.interval`: the time interval in seconds for periodically checking unhealthy nodes.

â¹ `passive.healthy.http_statuses`: the response HTTP status codes that are considered healthy.

âº `passive.unhealthy.http_statuses`: the response HTTP status codes that are considered unhealthy. The unhealthy responses are counted towards the `http_failures`.

â» `passive.unhealthy.http_failures`: the HTTP failure count threshold for ruling if an upstream node is considered unhealthy.

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

### Verify[â](#verify-2 "Direct link to Verify")

If you started APISIX in Docker with [Getting Started quickstart](https://docs.api7.ai/apisix/getting-started/.md#get-apisix), Control API port `9090` is already mapped (`-p 9090:9090`).

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

â· `mostly_healthy` status means the current node status is healthy, but APISIX starts to receive unhealthy indications during health checks.

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

## Disable All Health Checks[â](#disable-all-health-checks "Direct link to Disable All Health Checks")

You can disable all upstream health checks globally. This is useful in scenarios such as emergency maintenance, where health checks might interfere with routing or fallback behavior.

To disable all health checks, update your [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample) as follows:

conf/config.yaml

```
apisix:
  disable_upstream_healthcheck: true
```

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for configuration changes to take effect:

```
docker exec apisix-quickstart apisix reload
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned how to configure active and passive health checks for upstream services in APISIX. To learn more about the available configuration options for upstream health checks, see [Admin API, Upstream](https://docs.api7.ai/apisix/reference/admin-api/.md#tag/Upstream/paths/~1apisix~1admin~1upstreams/post) for reference.

APISIX also offers an `api-breaker` plugin, which implements circuit breaker functionality based on the health of upstream services and helps improve application resilience. See the `api-breaker` plugin doc for more details (coming soon).
