# Source: https://www.apollographql.com/docs/graphos/routing/cloud/migrate-to-dedicated.md

# Migrate to Dedicated

Apollo is discontinuing Serverless and Dedicated plans, which use cloud routers. Serverless plans end on February 1, 2026, and serverless cloud routers are not available after February 15, 2026. Dedicated plans end on March 15, 2026, and dedicated cloud routers are not available after March 15, 2026.

If you're currently on a Serverless or Dedicated plan, migrate your graphs to use self-hosted routers. [See the migration guide](https://www.apollographql.com/docs/graphos/routing/cloud/migrate-to-self-hosted) for step-by-step instructions.

GraphOS supports [self-hosted and cloud graphs](https://www.apollographql.com/docs/graphos/graphs/#graph-types), each recommended for different use cases. You may want to migrate to a cloud graph in these scenarios:

* You have multiple GraphQL APIs you want to compose into a supergraph.
* You have one or more self-hosted GraphQL APIs and want to use GraphOS features beyond graph composition, for example, [`@defer` support](https://www.apollographql.com/docs/graphos/routing/operations/defer) or [metrics reporting](https://www.apollographql.com/docs/graphos/platform/insights/).
* You have a self-hosted supergraph and want to offload the management of your router service to Apollo while retaining or gaining access to premium router features like [subscription support](https://www.apollographql.com/docs/graphos/routing/operations/subscriptions/), [authentication](https://www.apollographql.com/docs/router/configuration/authn-jwt), and [more](https://www.apollographql.com/docs/router/enterprise-features). Your router service may be either the GraphOS Router or the `@apollo/gateway` package.

GraphOS offers two tiers of cloud routing: Serverless and Dedicated. This guide focuses on considerations when migrating to [Dedicated](https://www.apollographql.com/docs/graphos/routing/cloud/dedicated). Refer to [this router comparison](https://www.apollographql.com/docs/graphos/routing#router-comparison) to learn about the differences.

Dedicated cloud routers currently support all [premium router features](https://www.apollographql.com/docs/router/enterprise-features) except for [safelisting with persisted queries](https://www.apollographql.com/docs/graphos/routing/security/persisted-queries/), [automatic persisted queries](https://www.apollographql.com/docs/apollo-server/performance/apq/), and [offline licenses](https://www.apollographql.com/docs/graphos/routing/license/#offline-license). Support for both persisted queries features is on the roadmap.

## Migrating from `@apollo/gateway`

Cloud routers use the same [Apollo Router Core binary](https://github.com/apollographql/router) that you can self-host. Therefore, migrating from [`@apollo/gateway`](https://www.apollographql.com/docs/apollo-server/using-federation/api/apollo-gateway/) entails migrating to the Apollo Router Core. Refer to the [Gateway migration guide](https://www.apollographql.com/docs/graphos/reference/migration/from-gateway) for tips.

## Router customizations

The GraphOS Router supports a [few avenues for customization](https://www.apollographql.com/docs/router/customizations/overview):

* Custom router binaries
* Rhai scripting
* External coprocessing

As a managed service, cloud routers don't support running custom binaries. Cloud routers don't currently support Rhai scripts, though support is on the roadmap.
Therefore, you must migrate any customizations to [external coprocessors](https://www.apollographql.com/docs/graphos/routing/customization/coprocessor/) or built-in router features to use cloud routing.

Built-in router features that you may have previously supported with customizations include:

* [Authentication](https://www.apollographql.com/docs/router/configuration/authn-jwt)
* [Telemetry and monitoring](https://www.apollographql.com/docs/router/configuration/telemetry/overview)
* [Traffic shaping](https://www.apollographql.com/docs/router/configuration/traffic-shaping)

See the [router configuration documentation](https://www.apollographql.com/docs/graphos/routing) for a full list of features.

## Migration

Once your implementation is ready to run on the router, including customizations, you can follow the [Dedicated quickstart](https://www.apollographql.com/docs/graphos/routing/cloud/dedicated-quickstart) to get started.

## Pricing considerations

Cloud Dedicated pricing depends on throughput instead of operation volume. Refer to the [Throughput guide](https://www.apollographql.com/docs/graphos/routing/cloud/throughput-guide) to learn more.

When you no longer host your router, router-to-subgraph communication may be inter-region, inter-Availablity Zone (AZ), or egress traffic. Be aware of how your new network topology may affect your cloud costs.
