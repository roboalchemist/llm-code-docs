# Source: https://grafbase.com/docs/gateway/configuration/operation-caching.md

# Operation Caching

The Grafbase Gateway maintains cached operation plans for unique operations to speed up consecutive requests with the same operation.

```toml
[operation_caching]
enabled = true
limit = 1000
warm_on_reload = false
warming_percent = 100
```

- `enabled`: Enables operation caching. Defaults to `true`.
- `limit`: The maximum number of operation plans to cache. Defaults to `1000`.
- `warm_on_reload`: If set to true, operations cached in memory will be
   re-planned and stored in the cache prior to a schema reload.
- `warming_percent`: The percentage of the cache that should be warmed, if
  `warm_on_reload` is set.  Defaults to 100.

## Using Redis for Operation Caching

Operation caching stores data in an in-memory cache by default. To share cached data across multiple gateways, use Redis as the caching backend.  Note that calling redis may be slower than replanning many operations, so be sure to test latency with your expected workload before enabling this.

```toml
[operation_caching.redis]
url = "redis://localhost:6379"
key_prefix = "my_gateway"
```

- `url`: Redis endpoint URL. Use `redis://` for plain text protocol or `rediss://` for TLS connections. Defaults to `redis://localhost:6379`.
- `key_prefix`: String prefix for Redis cache keys. Defaults to `grafbase-operation-cache`.

To use a TLS connection, start the Redis URL with `rediss://`. Add paths to these files in the TLS configuration if you don't have the server CA certificate in your system certificates or if you want to use mTLS.

```toml
[operation_caching.redis.tls]
cert = "/path/to/user.crt"
key = "/path/to/user.key"
ca = "/path/to/ca.crt"
```

- `cert`: The path to the mTLS user certificate file.
- `key`: The path to the mTLS user private key file. Must be defined together with the `cert`.
- `ca`: The path to the server CA certificate file.

Save files in PEM format. You don't need the `cert` and `key` unless your server uses mTLS. You don't need the `ca` if you've added the certificate to system certificate storage. The TLS library accepts only version 3 certificates and TLS version 1.3.