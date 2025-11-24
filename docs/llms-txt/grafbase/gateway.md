# Source: https://grafbase.com/docs/gateway/configuration/gateway.md

# Gateway

Set gateway server settings in this section:

```toml
[gateway]
timeout = "30s"
subgraph_timeout = "4s"
```

- `timeout` ([duration](https://grafbase.com/docs/gateway/configuration/durations.md)): Timeout for slow requests and responses. Default: `30s`.
- `subgraph_timeout` ([duration](https://grafbase.com/docs/gateway/configuration/durations.md)): A global timeout for all subgraph requests. A subgraph [can override](https://grafbase.com/docs/gateway/configuration/subgraph-configuration.md) this setting.

## Query Batching

Configure query batching in the Grafbase Gateway. When you use a large batch of queries, you risk causing a denial of service attack on your subgraph service or gateway.

```toml
[gateway.batching]
enabled = true
limit = 5
```

- `enabled`: Enables query batching. Defaults to `false`.
- `limit`: The maximum number of queries in a batch. If not set, the gateway does not limit the number of queries in a batch.

## Retries

Use retry configuration to specify how to handle subgraph request failures. A subgraph request can fail when the service times out, returns an error code, or reaches its rate limit.

```toml
[gateway.retry]
enabled = true
min_per_second = 10
ttl = "1s"
retry_percent = 0.1
retry_mutations = false
```

The gateway uses budget logic for retries. A successful subgraph request adds to the budget, while a failing request uses budget capacity.

- `enabled`: Enables retries for the given subgraph. Defaults to `false`.
- `min_per_second`: How many retries are available per second, at a minimum. Defaults to `10`.
- `ttl` ([duration](https://grafbase.com/docs/gateway/configuration/durations.md)): Each successful request to the subgraph adds to the retry budget. This setting controls how long the budget remembers successful requests. Defaults to `10s`.
- `retry_percent`: The fraction of the successful requests budget that can be used for retries. Defaults to `0.2`.
- `retry_mutations`: Whether mutations should be retried at all. Enable this setting only if mutations are idempotent. Defaults to `false`.

When you enable subgraph retries, the gateway executes them with an exponential backoff. The gateway performs the first retry after 100 milliseconds, the second after 200 milliseconds, the third after 400 milliseconds, and so on. The engine adds jitter to the times to prevent the thundering herd problem where too many requests reach the subgraph simultaneously. The gateway applies a jitter multiplier between 0.0 to 2.0 to the retry backoff.