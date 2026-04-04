# Source: https://www.apollographql.com/docs/graphos/routing/performance/traffic-shaping.md

# Source: https://www.apollographql.com/docs/graphos/connectors/performance/traffic-shaping.md

# Connectors Traffic Shaping Configuration

Connectors support the router's [traffic shaping features](https://www.apollographql.com/docs/graphos/routing/performance/traffic-shaping) to improve the performance and reliability of traffic between clients and the router and between the router and Connector sources. Connectors support all traffic shaping features, except [query deduplication](https://www.apollographql.com/docs/graphos/routing/performance/traffic-shaping#query-deduplication).

You can configure traffic shaping for all Connectors or a specific Connector source.

* To configure all Connectors, set traffic shaping configurations on `traffic_shaping.connector.all`.
* To configure a specific Connector source, set traffic shaping configurations on `traffic_shaping.connector.sources.X` where `X` is your `subgraph_name.source_name`.
* If you configure both, specific Connector source configurations override configurations set on `traffic_shaping.connector.all`.

## Example traffic shaping configuration

The example configuration below sets a [rate limit](https://www.apollographql.com/docs/graphos/routing/performance/traffic-shaping#rate-limiting) and [timeout](https://www.apollographql.com/docs/graphos/routing/performance/traffic-shaping#timeouts) for all Connectors and overrides the configuration for the `endpoint1` source on the `subgraph1` subgraph. It also sets [HTTP/2](https://www.apollographql.com/docs/graphos/routing/performance/traffic-shaping#http2) protocol for all subgraph connections.

```yaml title=router.yaml
traffic_shaping:
  connector:
    # Set traffic shaping configurations for all Connectors
    all:
      global_rate_limit:
        capacity: 50
        interval: 1s
      timeout: 5s
      experimental_http2: http2only
    # Override global setting for specific sources
    sources:
      subgraph1.endpoint1:
        global_rate_limit:
          capacity: 20
          interval: 1s
        timeout: 1s
```
