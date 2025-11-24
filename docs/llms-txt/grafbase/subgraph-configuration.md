# Source: https://grafbase.com/docs/gateway/configuration/subgraph-configuration.md

# Subgraph Configuration

Define settings per subgraph to add to or override global settings.

```toml
[subgraphs.products]
url = "https://example.com/graphql"
websocket_url = "https://example.com/"
subscriptions_protocol = "websocket"
timeout = "4s"
```

- `url`: Set the GraphQL endpoint for the subgraph to override the schema endpoint.
- `websocket_url`: Specifies the WebSocket URL that a subgraph uses when it differs from the GraphQL endpoint.
- `subscriptions_protocol` (optional, either "websocket" or "server_sent_events"): The protocol used by the gateway to communicate with the subgraph for subscriptions. If this option is not set, the gateway will default to websockets if `websocket_url` is defined, and server-sent events otherwise.
- `timeout`: The timeout for the subgraph.

## Entity Cache

Configure different settings per subgraph:

```toml
[subgraphs.products.entity_caching]
enabled = true
ttl = "60s"
```

- `enabled`: Enables or disables entity caching for the subgraph. Default value is the global setting.
- `ttl`: Sets the time-to-live for the cache. Default value is the global setting.

Read more on [global entity cache](https://grafbase.com/docs/gateway/configuration/entity-cache.md).

## Header Rules

Define header rules per subgraph. They execute after the global rules.

```toml
[[subgraphs.products.headers]]
rule = "forward"
name = "content-type"
```

For more information about available options, see [global header rules](https://grafbase.com/docs/gateway/configuration/headers.md).

## Rate Limit

Define custom rate limits for each subgraph and let the gateway check them before it sends requests. For more information, see [rate limiting](https://grafbase.com/docs/gateway/security/rate-limiting.md). You can hot-reload the subgraph rate limit and duration settings.

```toml
[subgraphs.products.rate_limit]
limit = 100
duration = "10s"
```

For more information about available options, see [global rate limit configuration](https://grafbase.com/docs/gateway/configuration/gateway.md).

## Retries

You can override the retry budget for the specific subgraph.

```toml
[subgraphs.products.retry]
enabled = true
min_per_second = 10
ttl = "1s"
retry_percent = 0.1
retry_mutations = false
```

For more information about available options, see [global retries configuration](https://grafbase.com/docs/gateway/configuration/gateway.md).

## Mutual TLS (mTLS)

Enable mutual TLS (mTLS) authentication for a specific subgraph:

```toml
[subgraphs.products.mtls]
root.certificate = "/path/to/ca.pem"
root.is_bundle = false
identity = "/path/to/ca.pem"
allow_invalid_certs = false
```

- `root.certificate`: Path to either a root CA certificate or a certificate bundle
- `root.is_bundle`: Specify `true` when using a certificate bundle
- `identity`: Client identity file containing both PEM certificate and key in a single file (PKCS#8 format)
- `allow_invalid_certs`: Only enable in development environments to bypass certificate validation

For subgraphs using self-signed certificates, you'll need to set the root certificate. The identity file must contain both the client certificate and key in the same file. The client key can be in RSA, SEC1 Elliptic Curve, or PKCS#8 format.

When using a self-signed certificate for your subgraph server, ensure the hostname appears in the Subject Alternative Name (SAN) section of the certificate. This is important because the gateway's HTTP client uses rustls for TLS connections, which disregards the Common Name (CN) when SANs are missing.

For a practical example, see our [certificate generation script](https://github.com/grafbase/grafbase/tree/main/crates/integration-tests/data/mtls-subgraph/generate-certs.sh) used in integration tests.