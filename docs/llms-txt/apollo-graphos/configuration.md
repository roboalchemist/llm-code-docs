# Source: https://www.apollographql.com/docs/apollo-operator/configuration.md

# Source: https://www.apollographql.com/docs/graphos/routing/cloud/configuration.md

# Source: https://www.apollographql.com/docs/graphos/routing/operations/subscriptions/configuration.md

# Source: https://www.apollographql.com/docs/graphos/connectors/deployment/configuration.md

# Runtime Configuration Overview

In this guide, you'll learn how to configure the GraphOS Router for Apollo Connectors by configuring `connectors` and other options in your router's configuration.

## Configuration

Configuring a self-hosted router for Connectors requires setting options in the router's YAML [configuration file](https://www.apollographql.com/docs/graphos/routing/configure-your-router#yaml-file-based-configuration).
When using Rover, you can call `rover dev` to start a router locally and use its `--router-config` option to pass your configuration file. For example:

```terminal
APOLLO_KEY=... \
APOLLO_GRAPH_REF=... \
APOLLO_ROVER_DEV_ROUTER_VERSION=2.0.0 \
rover dev --supergraph-config supergraph.yaml
--router-config router.yaml
```

Connectors configuration are nested under the `connectors` key.
Some configurations are applicable globally to all Connectors, some are applicable to specific Connector sources, and some can be configured for both.
For example, you can apply [request limits](https://www.apollographql.com/docs/graphos/connectors/deployment/configuration.md#request-limits) both globally across all Connectors and on specific Connector sources.

```yaml title=router.yaml
connectors:
  # This applies globally to all Connectors
  max_requests_per_operation_per_source: 100
  # This applies to Connectors with the "v1" source in the "example" subgraph
  sources:
    subgraph1.endpoint1:
      max_requests_per_operation: 50
```

To specify a source, you must include the subgraph name and source name, separated by a `.`—for example, `subgraph_name.connector_name`.

The example configurations on this page use the configuration format and names in the [General Availability release](https://www.apollographql.com/docs/graphos/schema-design/connectors/changelog#general-availability-of-apollo-connectors). If you are using a preview release, see the section on [migrating your configuration](https://www.apollographql.com/docs/graphos/schema-design/connectors/changelog#migrating-from-apollo-connectors-preview-releases).

To learn more about other router configurations, go to the [router configuration](https://www.apollographql.com/docs/graphos/reference/router/configuration) reference.

### Accessing router configuration in Connectors

You can pass configuration values—such as API keys or base paths—to your Connectors schema using the `$config` section in your [router configuration](https://www.apollographql.com/docs/graphos/routing/configure-your-router#yaml-file-based-configuration). This keeps sensitive or environment-specific values out of your schema.

Define values under `$config` for each source, then reference them in your schema with the [`$config` variable](https://www.apollographql.com/docs/graphos/schema-design/connectors/mapping#variables):

```yaml title=router.yaml
connectors:
  sources:
    subgraph1.endpoint1:
      $config:
        api_key: my-secret-key  # use ${env.API_KEY} in production
        base_path: v2
```

Reference these values in your schema using `{$config.<key>}` syntax.

```graphql title=schema.graphql
extend schema
  @source(
    name: "endpoint1"
    http: {
      baseURL: "https://api.example.com/{$config.base_path}"
      headers: [{ name: "Authorization", value: "Bearer {$config.api_key}" }]
    }
  )

type Query {
  products: [Product!]!
    @connect(
      source: "endpoint1"
      http: { GET: "/products" }
      selection: "id name"
    )
}
```

In this example, `{$config.api_key}` resolves to `"my-secret-key"` and `{$config.base_path}` resolves to `"v2"`, giving a base URL of `https://api.example.com/v2`. For secrets like API keys, use [environment variables](https://www.apollographql.com/docs/graphos/connectors/deployment/configuration.md#environment-variables) instead of inline values.

#### Nested values

Use nested YAML keys to organize related values. Dots in `$config` references act as path separators to traverse the YAML structure:

```yaml title=router.yaml
connectors:
  sources:
    subgraph1.endpoint1:
      $config:
        auth:
          token: my-token
```

In this example, `$config.auth.token` resolves to `"my-token"` by traversing the path `auth` → `token`.

Don't use dots in `$config` key names. For example, if you define `api.version: 2`, the reference `$config.api.version` doesn't match it. The router interprets dots as path separators and looks for a nested `api` key containing `version`. Use underscores (`api_version: 2`) or nested YAML keys instead.

#### Environment variables

Use `${env.VARIABLE_NAME}` syntax to inject environment variables into `$config` values. This is the recommended approach for secrets:

```yaml title=router.yaml
connectors:
  sources:
    subgraph1.endpoint1:
      $config:
        api_key: ${env.API_KEY}
```

## Next steps

* Explore all router configuration options in the [router configuration reference](https://www.apollographql.com/docs/graphos/routing/configuration)
* See the other pages in this section for Connectors-specific [security](https://www.apollographql.com/docs/graphos/connectors/security), [performance](https://www.apollographql.com/docs/graphos/connectors/performance), and [observability](https://www.apollographql.com/docs/graphos/connectors/observability) configurations
