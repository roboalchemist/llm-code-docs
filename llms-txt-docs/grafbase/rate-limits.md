# Source: https://grafbase.com/docs/gateway/configuration/rate-limits.md

# Rate Limits

The Grafbase Gateway offers ways to limit the number of requests per time window either globally or per subgraph. You can define the limit in memory per gateway instance or utilize a Redis backend to share the limit state with multiple gateway instances.

## Limits

Set global rate limits for all subgraphs:

```toml
[gateway.rate_limit.global]
limit = 100
duration = "10s"
```

- `limit`: Maximum number of requests allowed in the duration.
- `duration` ([duration](https://grafbase.com/docs/reference/gateway/configuration/durations.md)): Time window for the limit.

Subgraph-specific rate limits can also be set with the following:

```toml
# For the 'products' subgraph
[subgraphs.products.rate_limit]
limit = 100
duration = "10s"
```

## Storage

If you need to run multiple gateways and share the rate limit data with all of them, configure the gateway to use Redis as the rate limiter backend.

```toml
[gateway.rate_limit]
storage = "memory"
```

- `storage`: Rate limit storage backend. Supported values: `memory`, `redis`.

### In-memory

The default in-memory rate limiter uses the generic cell rate algorithm. It's a leaky bucket type scheduling algorithm. This method accurately limits sudden request bursts even before the current time window reaches its limit. It provides the fastest performance because the engine requires no network requests per GraphQL operation. When you restart the gateway with the in-memory rate limiter, the rate limit data starts empty.

### Redis

The Redis implementation uses an averaging fixed window rate limiting, which is different from the generic cell rate algorithm of the in-memory implementation. The Redis implementation generates two temporary keys to the database:

```
{key_prefix}:{subgraph:subgraph_name || global}:{current_time_bucket}
{key_prefix}:{subgraph:subgraph_name || global}:{previous_time_bucket}
```

The system fetches both values in a single Redis request, counts how far we are in the current time window, and calculates an averaged request count. The algorithm prevents spikes at the window border with an accuracy of a few percent.

Adding to the counter in the current time bucket happens off-thread, and the system deletes the buckets from the database after the time window ends.

The rate-limiting happens in a hot path, so the Redis server should be as close as possible to the gateway instances. Avoid using TLS for the counters to reduce the number of round trips to the Redis server.

```toml
[gateway.rate_limit.redis]
url = "redis://localhost:6379"
key_prefix = "my_gateway"
```

- `url`: Redis server URL.
- `key_prefix`: Prefix for the rate limit keys.

To connect using TLS, the Redis URL must start with `rediss://`. If the server CA certificate is not in the system certificates or if you want to use mTLS, define paths to these files in the TLS configuration.

```toml
[gateway.rate_limit.redis.tls]
cert = "/path/to/user.crt"
key = "/path/to/user.key"
ca = "/path/to/ca.crt"
```

- `cert`: Path to the client certificate.
- `key`: Path to the client key.
- `ca`: Path to the CA certificate.