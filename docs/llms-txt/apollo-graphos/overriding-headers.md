# Source: https://www.apollographql.com/docs/graphos/connectors/deployment/overriding-headers.md

# Overriding Headers

When integrating REST APIs through Apollo Connectors, you can [set HTTP headers in your schemas](https://www.apollographql.com/docs/graphos/connectors/requests#headers).
For cross-environment deployments and security configurations, you may need to override these headers without modifying other aspects of your schema.
Header overrides in your router configuration provide this flexibility.

### Header propagation

Connectors support the router's [header propagation features](https://www.apollographql.com/docs/graphos/routing/header-propagation) to propagate, insert, and rename headers.

You can configure header propagation for all connectors or a specific connector source.

* To configure all connectors, set headers configurations on `headers.connector.all`.
* To configure a specific connector source, set headers configurations on `headers.connector.sources.X` where `X` is your `subgraph_name.source_name`.
* If you configure both, specific connector source configurations override configurations set on `tls.connector.all`.

The example configuration below inserts an `x-inserted-header` and propagates an `x-client-header` for all connectors and overrides the configuration for the `endpoint1` source on the `subgraph1` subgraph.

If header rules in your router configuration conflict with headers set in `@connect` or `@source`, the router configuration takes precedence.

```yaml title=router.yaml
headers:
  connector:
    # Set header configurations for all connectors
    all:
      request:
        - insert:
            name: "x-inserted-header"
            value: "hello world!"
        - propagate:
            named: "x-awesome-header"
    # Override global setting for specific sources
    sources:
      subgraph1.endpoint1:
        request:
          - insert:
              name: "x-inserted-header"
              value: "hello world 2!"
          - propagate:
              named: "x-client-header"
```
