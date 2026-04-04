# Source: https://grafbase.com/docs/gateway/configuration/entity-cache.md

# Global Entity Cache

Use the Grafbase Gateway entity caching to cache requests to subgraphs. Enable global caching in the `entity_caching` configuration section:

```toml
[entity_caching]
enabled = true
ttl = "60s"
storage = "memory"
```

- `enabled`: Enables or disables entity caching. Defaults to `false`.
- `ttl`: Time-to-live for cached entities. Defaults to `60s`.
- `storage`: Storage backend for entity caching. Supported values: `memory`, `redis`. Defaults to `memory`.

The system scopes cached data to prevent data leaks between users. The gateway uses all headers sent to the subgraph to compute the scope.

## Using Redis for Entity Caching

Entity caching stores data in an in-memory cache by default. To share cached data across multiple gateways, use Redis as the caching backend.

```toml
[entity_caching.redis]
url = "redis://localhost:6379"
key_prefix = "my_gateway"
```

- `url`: Redis endpoint URL. Use `redis://` for plain text protocol or `rediss://` for TLS connections. Defaults to `redis://localhost:6379`.
- `key_prefix`: String prefix for Redis cache keys. Defaults to `grafbase-cache`.

To use a TLS connection, start the Redis URL with `rediss://`. Add paths to these files in the TLS configuration if you don't have the server CA certificate in your system certificates or if you want to use mTLS.

```toml
[entity_caching.redis.tls]
cert = "/path/to/user.crt"
key = "/path/to/user.key"
ca = "/path/to/ca.crt"
```

- `cert`: The path to the mTLS user certificate file.
- `key`: The path to the mTLS user private key file. Must be defined together with the `cert`.
- `ca`: The path to the server CA certificate file.

Save files in PEM format. You don't need the `cert` and `key` unless your server uses mTLS. You don't need the `ca` if you've added the certificate to system certificate storage. The TLS library accepts only version 3 certificates and TLS version 1.3.