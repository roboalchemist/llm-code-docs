# Source: https://grafbase.com/docs/gateway/security/rate-limiting.md

# Rate limiting

The Grafbase Gateway offers ways to limit the number of requests per time window either globally or per subgraph. You can define the limit in memory per gateway instance or utilize a Redis backend to share the limit state with multiple gateway instances. Read more on [global rate limit configuration](https://grafbase.com/docs/gateway/configuration/gateway.md) and [per-subgraph rate limit configuration](https://grafbase.com/docs/gateway/configuration/subgraph-configuration.md).

## Using In-memory Rate Limiting

The default in-memory rate limiter uses the [generic cell rate algorithm](https://en.wikipedia.org/wiki/Generic_cell_rate_algorithm), which is a leaky bucket type scheduling algorithm. This method accurately limits sudden request bursts even before the current time window reaches its limit. It provides the fastest performance because the engine requires no network requests per GraphQL operation. When you restart the gateway with the in-memory rate limiter, the rate limit data starts empty.

## Using Redis for Rate Limiting

If you need to run multiple gateways and share the rate limit data with all of them, configure the gateway to use Redis as the rate limiter backend. Read more on [configuring Redis for rate limiting](https://grafbase.com/docs/gateway/configuration/gateway.md).

The Redis implementation uses an averaging fixed window rate limiting, which is different from the generic cell rate algorithm of the in-memory implementation. The Redis implementation generates two temporary keys to the database:

- `{key_prefix}:{subgraph:subgraph_name || global}:{current_time_bucket}`
- `{key_prefix}:{subgraph:subgraph_name || global}:{previous_time_bucket}`

The system fetches both values in a single Redis request, counts how far we are in the current time window, and calculates an averaged request count. The algorithm prevents spikes at the window border with an accuracy of a few percent.

Adding to the counter in the current time bucket happens off-thread, and the system deletes the buckets from the database after the time window ends.

The rate-limiting happens in a hot path, so the Redis server should be as close as possible to the gateway instances. Avoid using TLS for the counters to reduce the number of round trips to the Redis server.