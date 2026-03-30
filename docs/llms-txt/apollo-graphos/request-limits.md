# Source: https://www.apollographql.com/docs/graphos/routing/security/request-limits.md

# Source: https://www.apollographql.com/docs/graphos/connectors/security/request-limits.md

# Connectors Request Limit Configuration

You can configure the maximum number of REST API requests for each GraphQL operation in the router. This can help avoid overwhelming upstream services. For requests that exceed the limit, the router returns a `null` value in the GraphQL result for any fields with `@connect` directives. Additionally, the router returns a GraphQL error in the `errors` array of the response. Partial data may still be returned for portions of the operation that weren't affected by the limit.

## Example request limits configuration

You set request limits in the router config YAML:

```yaml title=router.yaml
connectors:
  max_requests_per_operation_per_source: 100
```

This configuration limits the number of requests made to each Connector source for a given GraphQL operation. If a Connector doesn't define a source, then this limit is applied at the Connector level.
The limit can also be configured for each individual Connector source:

```yaml title=router.yaml
connectors:
  sources:
    subgraph1.endpoint1:
      max_requests_per_operation: 50
```

Limits set on an individual source override the general `max_requests_per_operation_per_source` limit.

The limit can also be configured by setting the environment variable `APOLLO_CONNECTORS_MAX_REQUESTS_PER_OPERATION`.
Any configuration in the YAML file overrides the environment variable setting.
