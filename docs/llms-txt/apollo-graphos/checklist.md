# Source: https://www.apollographql.com/docs/graphos/platform/production-readiness/checklist.md

# Production Readiness Checklist

We recommend that you read through this checklist and identify critical features for your team before your supergraph begins handling production traffic.

## GraphOS Studio

* Ensure that you've created multiple variants to represent the different environments where your supergraph runs (for example, production, staging, and development).
* [Protect your production variant](https://www.apollographql.com/docs/graphos/platform/graph-management/variants#protected-variants-enterprise-only) to avoid accidental changes while working in Studio.

## GraphOS Router

* Ensure that you've connected your router to your GraphOS supergraph and have enabled [GraphOS schema usage reporting](https://www.apollographql.com/docs/router/configuration/telemetry/apollo-telemetry).
* For security, [turn off introspection](https://www.apollographql.com/docs/router/configuration/overview/#introspection) for all production routers (by default the router disables introspection, but make sure you are not using `--dev` mode).
  * You can continue to view and fetch your GraphQL schemas from GraphOS and run operations from [GraphOS Studio Explorer](https://www.apollographql.com/docs/graphos/platform/explorer).
* Configure the [router traffic shaping](https://www.apollographql.com/docs/router/configuration/traffic-shaping) features:
  * Set request and subgraph level timeouts and rate limits
  * Deduplicate subgraph requests
  * Communicate with subgraphs using APQ
* Enable [operation limits](https://www.apollographql.com/docs/router/configuration/operation-limits) to block large and malicious requests
* Configure additional [tracing, metrics, and logging](https://www.apollographql.com/docs/router/configuration/telemetry/overview) through OpenTelemetry or Prometheus
* Enable the operation and query plan [distributed cache](https://www.apollographql.com/docs/router/configuration/distributed-caching)
* Optionally, enable any [other features](https://www.apollographql.com/docs/router/enterprise-features/) deemed critical for your deployment of GraphOS Router

## Subgraphs/servers

* For security, [turn off introspection](https://www.apollographql.com/docs/apollo-server/api/apollo-server/#introspection) for all production GraphQL subgraphs.
  * You can continue to view and fetch your GraphQL schemas from GraphOS and run operations from [GraphOS Studio Explorer](https://www.apollographql.com/docs/graphos/explorer).
* Ensure that you've integrated [`rover subgraph check`](https://www.apollographql.com/docs/rover/commands/subgraphs#subgraph-check) and [`rover subgraph publish`](https://www.apollographql.com/docs/rover/commands/subgraphs#subgraph-publish) into your CI/CD pipeline.
* If your subgraph servers are listed as [compatible with `FEDERATED TRACING`](https://www.apollographql.com/docs/graphos/federated-schemas/reference/compatible-subgraphs), ensure that you've enabled [federated traces](https://www.apollographql.com/docs/federation/metrics/), and that you can view operation metrics as expected in Apollo Studio.
  * Enable [fractional trace sampling via `fieldLevelInstrumentation`](https://www.apollographql.com/docs/graphos/platform/insights/field-usage/#fractional-sampling) to reduce performance hits due to tracing.
* Ensure that you've [load-tested your graph](https://www.apollographql.com/docs/graphos/platform/production-readiness/load-testing).
  * Test loads should be representative of your current traffic (both in terms of volume and in terms of the actual operations you execute in the test).
  * To investigate performance issues, use Apollo Studio to identify which operations are performing slowly.
    * Look at resolver execution times to identify slow areas of execution.
    * Whenever possible, avoid making multiple calls to data sources within a single resolver.
    * Understand [query plan execution](https://www.apollographql.com/docs/federation/query-plans) to help understand slow operations and optimize your supergraph to avoid them.
* Consider adding caching layers.
  * Apollo Server supports [automatic persisted queries (APQ)](https://www.apollographql.com/docs/apollo-server/performance/apq/) out of the box.
    * If using Apollo Server, ensure that you use a [distributed caching system](https://www.apollographql.com/docs/apollo-server/performance/cache-backends) for APQ in production to avoid cache inconsistency across server instances.
    * Optionally use the [`@cacheControl` directive](https://www.apollographql.com/docs/apollo-server/api/plugin/cache-control) to enable your CDN to cache APQ GET requests using the `Cache-Control` header.
  * Optionally add [full response caching](https://www.apollographql.com/docs/apollo-server/performance/caching/) to improve performance.

## Clients

* Ensure that your [clients identify themselves](https://www.apollographql.com/docs/graphos/metrics/client-awareness/) by name and version.
  * If you're using an Apollo Client library, you can add a client name and version to the constructor.
  * For example, the [React client uses the `name` and `version` attributes](https://www.apollographql.com/docs/react/api/core/ApolloClient#name) in the constructor options.
  * If you're using a third-party GraphQL client, set the `apollographql-client-name` and `apollographql-client-version` HTTP headers for each request to identify your client.
  * For an example of enforcing client identification in your gateway, see [Client ID enforcement](https://www.apollographql.com/docs/graphos/routing/observability/client-id-enforcement/).
* Consider adding caching layers.
  * Enable [Persisted Queries and/or Automatic Persisted Queries (APQ)](https://www.apollographql.com/docs/react/api/link/persisted-queries) support for request-size savings.
  * Enable and configure the client side [normalized cache](https://www.apollographql.com/docs/react/caching/overview)
