# Source: https://docs.api7.ai/enterprise/key-concepts/upstreams.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/key-concepts/upstreams.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/key-concepts/upstreams.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/key-concepts/upstreams.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/key-concepts/upstreams.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/key-concepts/upstreams.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/key-concepts/upstreams.md

# Source: https://docs.api7.ai/enterprise/3.8.x/key-concepts/upstreams.md

# Source: https://docs.api7.ai/enterprise/3.7.x/key-concepts/upstreams.md

# Source: https://docs.api7.ai/enterprise/3.6.x/key-concepts/upstreams.md

# Source: https://docs.api7.ai/enterprise/3.5.x/key-concepts/upstreams.md

# Source: https://docs.api7.ai/enterprise/3.4.x/key-concepts/upstreams.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/upstreams.md

# Source: https://docs.api7.ai/apisix/key-concepts/upstreams.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/upstreams.md

# Source: https://docs.api7.ai/apisix/key-concepts/upstreams.md

# Upstreams

In this document, you will learn the basic concept of an upstream object in APISIX and why you would want to use it. You will be introduced to a few relevant features, including load balancing, service discovery, and upstream health checking.

Explore additional resources at the end for more information on related topics.

## Overview[â](#overview "Direct link to Overview")

An *upstream* object in APISIX is a logical abstraction of a set containing one or more upstream addresses. It is required in [routes](https://docs.api7.ai/apisix/key-concepts/routes.md) or [services](https://docs.api7.ai/apisix/key-concepts/services.md) to specify **where** requests flow to and **how** they are distributed.

There are different ways to configure upstream addresses, one of which is to explicitly configure them in every route/service. Here is an example of such a configuration in routes, where the same upstream address is repeated across three different routes:

<br />

![Upstreams Diagram showing three routes with different plugins and the same hard-coded upstream address](https://static.api7.ai/uploads/2023/02/24/6gZ6zw2R_upstream-before.svg)

<br />

<br />

This approach, however, leads to data redundancies and poses a risk for update anomalies (i.e. inconsistent data resulting from a partial update).

A better approach is to extract the repetitive upstream configurations into a separate upstream object and embed its `upstream_id` into routes/services, such as the following:

<br />

![Upstreams Diagram showing three routes with different plugins pointing to the same upstream object with the desired upstream address](https://static.api7.ai/uploads/2023/02/24/vPjoKWdE_upstream-after.svg)

<br />

As you can probably see, large-scale systems with many routes/services would benefit significantly from configuring identical groups of upstream addresses in upstream objects, reducing redundant information and operational costs.

## Load Balancing[â](#load-balancing "Direct link to Load Balancing")

An important configuration option in upstreams is the [load balancing](https://docs.api7.ai/apisix/getting-started/load-balancing.md) algorithm.

APISIX offers four load-balancing algorithm options to choose from:

* `roundrobin` - weighted round robin
* `chash` - consistent hashing
* `ewma` - exponentially weighted moving average
* `least_conn` - least connections

You can also build your own load balancing algorithm by adding the source file under `apisix/balancer` and importing it with `require("apisix.balancer.your_balancer_name")`, where needed.

To learn more about how you can configure load balancing in APISIX, see the [load balancing tutorial](https://docs.api7.ai/apisix/getting-started/load-balancing.md) and [Admin API reference](https://docs.api7.ai/apisix/reference/admin-api/.md#tag/Upstream/paths/~1apisix~1admin~1upstreams~1%7Bid%7D/put).

## Service Discovery[â](#service-discovery "Direct link to Service Discovery")

While it is straightforward to figure upstream addresses statically, in microservice-based architectures, upstream addresses are often dynamically assigned and therefore changed during autoscaling, failures, and updates. Static configurations are less than ideal in this case.

Service discovery comes to the rescue. It describes the process of automatically detecting the available upstream services, keeping their addresses in a database (called a service registry) for others to reference. That way, an API gateway can always fetch the latest list of upstream addresses through the registry, ensuring all requests are forwarded to healthy upstream nodes.

APISIX supports integrations with many service registries, such as Consul, Eureka, Nacos, Kubernetes service discovery, and more.

For more details about how to integrate with third-party service registries, such as HashiCorp Consul, please see the [how-to guide](https://docs.api7.ai/apisix/how-to-guide/service-discovery/consul-integration.md).

## Upstream Health Checking[â](#upstream-health-checking "Direct link to Upstream Health Checking")

APISIX provides active and passive health checking options to probe if upstream nodes are online (a.k.a. healthy). Unhealthy upstream nodes will be ignored until they recover and are deemed healthy again.

Upstream health checking can be configured in the `checks` parameter in an upstream object.

For more details about how to configure active and passive upstream health check, please see the [how-to guide](https://docs.api7.ai/apisix/how-to-guide/traffic-management/health-check.md).

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Getting Started - [Load Balancing](https://docs.api7.ai/apisix/getting-started/load-balancing.md)
* [Configure Upstream Health Checks](https://docs.api7.ai/apisix/how-to-guide/traffic-management/health-check.md)
* [Integrate with HashiCorp Consul for Service Discovery](https://docs.api7.ai/apisix/how-to-guide/service-discovery/consul-integration.md)
* Admin API - [Upstream](https://docs.api7.ai/apisix/reference/admin-api/.md#tag/Upstream)
