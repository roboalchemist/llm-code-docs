# Source: https://docs.api7.ai/enterprise/key-concepts/stream-routes.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/key-concepts/stream-routes.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/key-concepts/stream-routes.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/key-concepts/stream-routes.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/key-concepts/stream-routes.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/key-concepts/stream-routes.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/key-concepts/stream-routes.md

# Source: https://docs.api7.ai/enterprise/3.8.x/key-concepts/stream-routes.md

# Source: https://docs.api7.ai/enterprise/3.7.x/key-concepts/stream-routes.md

# Source: https://docs.api7.ai/enterprise/3.6.x/key-concepts/stream-routes.md

# Source: https://docs.api7.ai/enterprise/3.5.x/key-concepts/stream-routes.md

# Source: https://docs.api7.ai/enterprise/3.4.x/key-concepts/stream-routes.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/stream-routes.md

# Source: https://docs.api7.ai/apisix/key-concepts/stream-routes.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/stream-routes.md

# Source: https://docs.api7.ai/apisix/key-concepts/stream-routes.md

# Stream Routes

In this document, you will learn the basic concept of stream routes in APISIX and why you may need them.

Explore additional resources at the end of the document for more information on related topics.

## Overview[â](#overview "Direct link to Overview")

In APISIX, a *stream route* object is used to create a route when APISIX functions as a stream proxy, operating on the [transport layer](https://en.wikipedia.org/wiki/Transport_layer) for TCP and UDP connections. This is analogous to the concept of routes in cases where APISIX functions as an [application-layer](https://en.wikipedia.org/wiki/Application_layer) proxy.

The following diagram illustrates the concept of a stream route object. In this example, APISIX functions as a stream proxy for a [MySQL](https://www.mysql.com) server that uses TCP protocol for communication. APISIX is deployed at IP address `192.168.1.10` and configured to listen for TCP connections on port `9500`:

![APISIX and MySQL Server with one stream route restricting on client IP address](https://static.api7.ai/uploads/2023/04/28/NxlpM4Yf_stream_routes.svg)

<br />

The `client_addr` field in the stream route filters on the client IP, ensuring that only requests originating from the specified IP address are allowed to pass through this route to the upstream MySQL server. While both clients have used the correct credentials to connect to the MySQL server, only the client with IP address whitelisted in `client_addr` is permitted to establish a connection.

In addition to the `client_addr` field, there are other fields such as `server_addr` and `server_port` that can be configured to filter incoming requests before rejecting or forwarding them to upstream services. To learn more about these fields and other configuration options, please refer to the Admin API reference for stream routes (coming soon).

For detailed instructions on how to configure APISIX as a stream proxy, see the [Proxy Transport Layer (L4) Traffic](https://docs.api7.ai/apisix/how-to-guide/traffic-management/proxy-transport-layer-l4-traffic.md) how-to guide.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Getting Started - [Configure Routes](https://docs.api7.ai/apisix/getting-started/configure-routes.md)
* Key Concepts - [Routes](https://docs.api7.ai/apisix/key-concepts/routes.md)
* Admin API - [Stream Route](https://docs.api7.ai/apisix/reference/admin-api/.md#tag/Stream-Route)
