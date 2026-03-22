# Source: https://www.apollographql.com/docs/react/performance/performance.md

# Source: https://www.apollographql.com/docs/graphos/resources/saf/performance.md

# Source: https://www.apollographql.com/docs/graphos/routing/performance.md

# Source: https://www.apollographql.com/docs/graphos/connectors/performance.md

# Connectors Performance Overview

Apollo Connectors are designed with performance in mind, providing efficient ways to incorporate REST APIs directly into your graph through the GraphOS Router.

## Subgraph approach vs. direct integration

Before Connectors, integrating a REST API into your graph required spinning up a passthrough GraphQL API:

With Connectors, you eliminate the need for that additional service:

This architecture provides the following performance benefits:

* **Reduced network hops** with direct router-to-REST communication
* **Lower operational complexity** without additional services to deploy and maintain

## Router performance overhead

The GraphOS Router is optimized to handle Connector requests with minimal overhead:

* **Low latency processing** of REST API requests and responses
* **Parallel execution** of independent REST API requests when possible
* **Efficient response transformation** through declarative mapping language that executes directly in the router runtime

When comparing direct REST calls to Connector-based integration, the additional router processing adds only milliseconds of overhead while providing the significant benefits of GraphQL's declarative data fetching.

## Next steps

First, ensure that you're using [batch requests](https://www.apollographql.com/docs/graphos/connectors/requests/batching) whenever possible.

Additionally, the following configurations help prevent overwhelming backend services:

* [Request limits](https://www.apollographql.com/docs/graphos/connectors/security/request-limits) (this is also a security feature)
* [Traffic shaping](https://www.apollographql.com/docs/graphos/connectors/performance/traffic-shapping)
