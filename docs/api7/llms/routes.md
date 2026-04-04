# Source: https://docs.api7.ai/enterprise/key-concepts/routes.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/key-concepts/routes.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/key-concepts/routes.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/key-concepts/routes.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/key-concepts/routes.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/key-concepts/routes.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/key-concepts/routes.md

# Source: https://docs.api7.ai/enterprise/3.8.x/key-concepts/routes.md

# Source: https://docs.api7.ai/enterprise/3.7.x/key-concepts/routes.md

# Source: https://docs.api7.ai/enterprise/3.6.x/key-concepts/routes.md

# Source: https://docs.api7.ai/enterprise/3.5.x/key-concepts/routes.md

# Source: https://docs.api7.ai/enterprise/3.4.x/key-concepts/routes.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/routes.md

# Source: https://docs.api7.ai/apisix/key-concepts/routes.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/routes.md

# Source: https://docs.api7.ai/apisix/key-concepts/routes.md

# Routes

In this document, you will learn the basic concept of routes in APISIX, different routing options APISIX offers, as well as drawbacks and solutions to repetitive route configurations.

Explore additional resources at the end of the document for more information on related topics.

## Overview[â](#overview "Direct link to Overview")

*Routes* define paths to upstream services. In APISIX, a route object is used to create a route when APISIX operates on the [application layer](https://en.wikipedia.org/wiki/Application_layer), as opposed to a [stream route](https://docs.api7.ai/apisix/key-concepts/stream-routes.md) object, which is used to create a route when APISIX functions as a stream proxy operating on the [transport layer](https://en.wikipedia.org/wiki/Transport_layer). Routes are responsible for matching client requests based on configured rules, loading and executing the corresponding plugins, and forwarding requests to the specified upstream endpoints.

A simple route can be set up with a path-matching URI and a corresponding upstream address. The diagram below shows an example of users sending two HTTP requests to the APISIX API gateway, which are forwarded accordingly per the configured rules in routes:

<br />

![Routes Diagram](https://static.api7.ai/uploads/2023/02/24/1yJwf7in_routes.svg)

<br />

<br />

Routes are often configured with plugins as well. For example, [configuring the rate-limit plugin in a route](https://docs.api7.ai/apisix/getting-started/rate-limiting.md) will enable rate-limiting effects.

## Router Options[â](#router-options "Direct link to Router Options")

APISIX offers three HTTP routing options:

1. `radixtree_host_uri` routes requests by hosts and URI paths, prioritizing hostnames over URI paths during matching. This is the default setting. It can be used to route north-south traffic between clients and servers.

2. `radixtree_uri` routes requests by hosts and URI paths, prioritizing URI paths over hostnames during matching. It can be used to route east-west traffic, such as between microservices.

3. `radixtree_uri_with_parameter` enhances `radixtree_uri` to support the use of parameter in path matching.

These routing options can be configured in `conf/config.yaml` under `apisix.router.http`. For more information, see [Router Options](https://docs.api7.ai/apisix/reference/router-options.md).

## Routes, Upstreams, and Services[â](#routes-upstreams-and-services "Direct link to Routes, Upstreams, and Services")

While routes are essential in defining the paths of traffic flows, there are drawbacks to repetitive route configurations (i.e. hard coding **the same upstream addresses or plugin names** for a group of routes). During updates, the repetitive field(s) of these routes will need to be traversed and updated one by one. Configurations like this increase a lot of maintenance costs as a result, especially in large-scale systems with many routes.

To address this issue, [Upstreams](https://docs.api7.ai/apisix/key-concepts/upstreams.md) and [Services](https://docs.api7.ai/apisix/key-concepts/services.md) were designed to abstract away repetitive information and reduce redundancies, following the [DRY principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).

## Additional Resource(s)[â](#additional-resources "Direct link to Additional Resource(s)")

* Getting Started - [Configure Routes](https://docs.api7.ai/apisix/getting-started/configure-routes.md)
* Key Concepts - [Stream Routes](https://docs.api7.ai/apisix/key-concepts/stream-routes.md)
* Admin API - [Route](https://docs.api7.ai/apisix/reference/admin-api/.md#tag/Route)
