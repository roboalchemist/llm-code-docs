# Source: https://docs.api7.ai/enterprise/best-practices/upstream-ha.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/best-practice/upstream-ha.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/best-practice/upstream-ha.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/best-practice/upstream-ha.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/best-practice/upstream-ha.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/best-practice/upstream-ha.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/best-practice/upstream-ha.md

# Source: https://docs.api7.ai/enterprise/3.8.x/best-practices/upstream-ha.md

# Source: https://docs.api7.ai/enterprise/3.7.x/best-practices/upstream-ha.md

# Source: https://docs.api7.ai/enterprise/3.6.x/best-practices/upstream-ha.md

# Source: https://docs.api7.ai/enterprise/3.5.x/best-practices/upstream-ha.md

# Source: https://docs.api7.ai/enterprise/3.4.x/best-practices/upstream-ha.md

# Source: https://docs.api7.ai/enterprise/3.3.x/best-practices/upstream-ha.md

# Ensure Upstream High Availability

When API7 Gateway sends the API requests to the [upstreams](https://docs.api7.ai/enterprise/3.3.x/key-concepts/upstreams.md), there can be availability and reliability concerns if those upstream systems fail. This guide covers strategies for the high availability of your upstream dependencies.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. [Have a running API on the gateway group](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md).

## Add Multiple Upstream Nodes[â](#add-multiple-upstream-nodes "Direct link to Add Multiple Upstream Nodes")

Using multiple upstream nodes protects against single-node failure. Modifications made to upstream nodes in a gateway group will not affect the same service version published to other gateway groups.

* Dashboard
* Ingress Controller

1. Select **Published Services** of your gateway group from the side navigation bar, then click the service you want to modify, for example, `httpbin` with version `1.0.0`.
2. Under the published service, select **Upstreams** from the side navigation bar.
3. Click **Nodes** > **Add Node**.
4. From the dialog box, do the following:

* In the **Host** and **Port** fields, enter another API Endpoint.
* In the **Weight** field, enter `100`, the same as the first node.
* Click **Add**.

Create a Kubernetes manifest file to configure a route pointing to multiple upstream services using the ApisixRoute custom resource:

multiple-upstream-nodes.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  name: multiple-upstream-nodes
  # namespace: api7    # replace with your namespace
spec:
  http:
    - name: multiple-upstream-nodes
      match:
        paths:
          - /*
      backends:
        - serviceName: upstream1
          servicePort: 80
        - serviceName: upstream2
          servicePort: 80
```

Apply the configuration to your cluster:

```
kubectl apply -f multiple-upstream-nodes.yaml
```

## Modify Load Balancing Type[â](#modify-load-balancing-type "Direct link to Modify Load Balancing Type")

Load balancing distributes network requests across multiple nodes. It is crucial for systems handling high traffic volumes, improving performance, scalability, and reliability.

API7 Gateway supports a variety of load-balancing algorithms:

* Weighted Round Robin (WRR)
* Consistent Hash
* Exponentially Weighted Moving Average (EWMA)
* Least Connection

By default, API7 Gateway supports the WRR algorithm. This algorithm distributes incoming requests over a set of nodes based on their weight in a cyclical pattern.

* Dashboard
* Ingress Controller

1. Select **Published Services** of your gateway group from the side navigation bar, then click the service you want to modify, for example, `httpbin` with version `1.0.0`.
2. Under the published service, select **Upstreams** from the side navigation bar.
3. In the **Upstream Configuration** field, click **Edit**.
4. From the dialog box, edit **Load Balancing Type** to `Least Connection`.
5. Click **Save**.

loadbalancer.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  name: httpbin        # correspond to service name
  # namespace: api7    # replace with your namespace
spec:
  loadbalancer:
    type: least_conn
```

Apply the configuration to your cluster:

```
kubectl apply -f loadbalancer.yaml
```

## Enable Health Checks[â](#enable-health-checks "Direct link to Enable Health Checks")

Health checking is a mechanism that determines whether upstream nodes are healthy or unhealthy based on their responsiveness. With health checks enabled, API7 Enterprise Edition will only forward requests to upstream nodes that are considered healthy, and not forward requests to the nodes that are considered unhealthy.

There are two general approaches to health checks:

* Active health checks: determines the health of an upstream node by actively probing the node.
* Active health checks: determine the health of an upstream node by actively probing the node.

info

Make sure your API backend has already implemented the endpoints for health checks before enabling them.

* Dashboard
* Ingress Controller

1. Select **Published Services** of your gateway group from the side navigation bar, then click the service you want to modify, for example, `httpbin` with version `1.0.0`.
2. Under the published service, select **Upstreams** from the side navigation bar.
3. In the **Health Check** field, click **Enable**.
4. From the dialog box, do the following:

* In the **Probe Scheme** field, choose `HTTP`.
* In the **HTTP Probe Path** field, enter `/health`.
* Use the default value for the rest of the fields.
* Click **Enable**.

Create a Kubernetes manifest file for an upstream, where health check is enabled:

upstream-healthcheck.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  name: httpbin        # correspond to service name
  # namespace: api7    # replace with your namespace
spec:
  healthCheck:
    passive:
      unhealthy:
        httpCodes:
          - 429
          - 404
          - 500
          - 501
          - 502
          - 503
          - 504
          - 505
        httpFailures: 5
    active:
      type: http
      httpPath: /health
      timeout: 3
      healthy:
        successes: 2
        interval: 1s
        httpCodes:
          - 200
          - 302
```

Apply the configuration to your cluster:

```
kubectl apply -f upstream-healthcheck.yaml
```

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts

  <!-- -->

  * [Services](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md)
  * [Upstreams](https://docs.api7.ai/enterprise/3.3.x/key-concepts/upstreams.md)
