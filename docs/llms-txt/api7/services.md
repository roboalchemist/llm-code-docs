# Source: https://docs.api7.ai/enterprise/key-concepts/services.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/key-concepts/services.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/key-concepts/services.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/key-concepts/services.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/key-concepts/services.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/key-concepts/services.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/key-concepts/services.md

# Source: https://docs.api7.ai/enterprise/3.8.x/key-concepts/services.md

# Source: https://docs.api7.ai/enterprise/3.7.x/key-concepts/services.md

# Source: https://docs.api7.ai/enterprise/3.6.x/key-concepts/services.md

# Source: https://docs.api7.ai/enterprise/3.5.x/key-concepts/services.md

# Source: https://docs.api7.ai/enterprise/3.4.x/key-concepts/services.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md

# Source: https://docs.api7.ai/apisix/key-concepts/services.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md

# Source: https://docs.api7.ai/apisix/key-concepts/services.md

# Services

In this document, you will learn the basic concept of *services* in APISIX and the advantages of using services.

Explore additional resources at the end for more information on related topics.

## Overview[â](#overview "Direct link to Overview")

A *service* object in APISIX is an abstraction of a backend application providing logically related functionalities. The relationship between a service and routes is usually one-to-many (1<!-- -->:N<!-- -->).

The following diagram illustrates an example of a service object used in architecting a data analytics (`da`) backend at Foodbar Company (a fictional company), where there are two routes with distinctive configurations - one for getting data ([HTTP GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)) and the other one for uploading data ([HTTP POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)):

<br />

![Services Diagram](https://static.api7.ai/uploads/2023/02/28/7Iudl0X8_services.svg)

<br />

<br />

Note that the [rate-limiting](https://docs.api7.ai/apisix/getting-started/rate-limiting.md) plugin `limit-count` is configured once on the service object, regulating incoming client requests from the two routes. Similarly, the upstream address is also configured only once on the [upstream](https://docs.api7.ai/apisix/key-concepts/upstreams.md) object. While plugins and upstreams can also be configured in routes individually (and repetitively) to serve the same purpose, it is advised against adopting this approach, as things quickly become hard to manage when the system grows. Using upstreams and services help reduce the risk of data anomalies and minimize operational costs.

For simplicity, the example above only pointed the traffic to one upstream node. You can add more upstream nodes, when needed, to [enable load balancing](https://docs.api7.ai/apisix/getting-started/load-balancing.md), maintaining a smooth operation and response for users and avoiding a single point of failure in the architecture.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Getting Started

  <!-- -->

  * [Configure Routes](https://docs.api7.ai/apisix/getting-started/configure-routes.md)
  * [Load Balancing](https://docs.api7.ai/apisix/getting-started/load-balancing.md)

* Key Concepts

  <!-- -->

  * [Routes](https://docs.api7.ai/apisix/key-concepts/routes.md)
  * [Upstreams](https://docs.api7.ai/apisix/key-concepts/upstreams.md)
  * [Plugins](https://docs.api7.ai/apisix/key-concepts/plugins.md)

* Admin API - [Service](https://docs.api7.ai/apisix/reference/admin-api/.md#tag/Service)
