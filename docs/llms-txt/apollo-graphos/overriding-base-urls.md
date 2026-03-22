# Source: https://www.apollographql.com/docs/graphos/connectors/deployment/overriding-base-urls.md

# Overriding Base URLs

When deploying GraphQL services that use Apollo Connectors across different environments (dev, staging, production), you may need to point your Connectors to different REST API endpoints without changing your schema or subgraph code.

Overriding a source's `baseURL` configuration provides several key benefits:

* **Environment-specific deployments**: Connect to different API environments (dev, staging, production) using the same schema definition.
* **Simplified development workflow**: Developers can use local or mocked APIs during development while production uses real endpoints.
* **Security boundary separation**: Keep sensitive production API endpoints out of your schema code, where they might be committed to source control.

This deployment-focused approach allows you to maintain a consistent schema definition across environments while adjusting the actual service endpoints through configuration rather than code changes.

### Overriding `baseURL` for environment-specific API hosts

You can override the `baseURL` of a `@source` directive in your router configuration file.
For example, given this `@source` configuration in a schema:

```graphql title=schema.graphql
extend schema
  @source(
    name: "v1"
    http: { baseURL: "https://dev.api.example.com/v1/beta" }
  )
```

And by configuring `connectors.sources` in your router configuration like so:

```yaml title=router.yaml
connectors:
  sources:
    subgraph1.endpoint1:
      # These configurations apply to Connectors with the "endpoint1" source in the "subgraph1" subgraph
      override_url: "https://api.example.com/v1/beta"
```

You can override the `baseURL` for all `@connect` directives in the subgraph that reference the `endpoint1` source in the `subgraph1` subgraph.

If a `@connect` directive doesn't specify the `source` attribute, its URL can't be overridden.
