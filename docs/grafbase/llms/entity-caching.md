# Source: https://grafbase.com/docs/gateway/performance/entity-caching.md

# Entity Caching

Grafbase Gateway uses Entity Caching to cache requests to subgraphs. Enable entity caching globally in the [global entity cache config section](https://grafbase.com/docs/gateway/configuration/entity-cache.md). Every subgraph can define its own cache policies - learn more in the [per-subgraph entity cache config section](https://grafbase.com/docs/gateway/configuration/subgraph-configuration.md). The system protects user data by scoping cached data, and uses all headers to compute the scope.

Entity caching stores data in an in-memory cache by default. Configure Redis as your caching backend when you need to run and share cache across multiple gateways. Learn more about [configuring Redis for entity cache](https://grafbase.com/docs/gateway/configuration/entity-cache.md).

TLS with Redis increases response times, and each request requires at least one call to the Redis server. Place the Redis server as close as possible to the gateway instances and avoid using TLS for the counters.