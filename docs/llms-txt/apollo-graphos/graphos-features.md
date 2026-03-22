# Source: https://www.apollographql.com/docs/graphos/routing/graphos-features.md

# Licensed GraphOS Router Features

This page lists the additional features of GraphOS Router that are enabled via integration with a licensed GraphOS plan.

> Refer to the [pricing page](https://www.apollographql.com/pricing) to compare GraphOS Router features across plan types.

## GraphOS Router licensed features

* Real-time updates via [GraphQL subscriptions](https://www.apollographql.com/docs/graphos/routing/operations/subscriptions)
* Improved performance with [query batching](https://www.apollographql.com/docs/graphos/routing/performance/query-batching)
* Authentication of inbound requests via [JSON Web Token (JWT)](https://www.apollographql.com/docs/graphos/routing/security/jwt)
* [Authorization of specific fields and types](https://www.apollographql.com/docs/graphos/routing/security/authorization) through the [`@requiresScopes`](https://www.apollographql.com/docs/graphos/routing/security/authorization#requiresscopes), [`@authenticated`](https://www.apollographql.com/docs/graphos/routing/security/authorization#authenticated), and [`@policy`](https://www.apollographql.com/docs/graphos/routing/security/authorization#policy) directives
* Redis-backed [distributed caching of query plans](https://www.apollographql.com/docs/graphos/routing/query-planning/caching#distributed-caching-with-redis) and [automatic persisted queries](https://www.apollographql.com/docs/graphos/routing/operations/apq#distributed-caching-with-redis)
* Redis-backed [response caching](https://www.apollographql.com/docs/graphos/routing/performance/caching/response-caching/overview) (preview)
* Custom request handling in any language via [external coprocessing](https://www.apollographql.com/docs/graphos/routing/customization/coprocessor)
* Mitigation of potentially malicious requests via [request limits](https://www.apollographql.com/docs/graphos/routing/security/request-limits), [demand control](https://www.apollographql.com/docs/graphos/routing/security/demand-control), and [safelisting](https://www.apollographql.com/docs/graphos/routing/security/persisted-queries)
* Custom instrumentation and telemetry, including [custom attributes for spans](https://www.apollographql.com/docs/graphos/reference/router/telemetry/instrumentation/spans#attributes).
* An [offline license](https://www.apollographql.com/docs/graphos/routing/license/#offline-license) that enables running the router with GraphOS features when disconnected from the internet.

## Enabling licensed plan features

To enable licensed plan features in a router:

* You must run GraphOS Router v1.12 or later. [Download the latest version.](https://www.apollographql.com/docs/graphos/reference/router/self-hosted-install#1-download-and-extract-the-router-binary)
  * Certain features might require a later router version. See a particular feature's documentation for details.
* Your router instances must connect to GraphOS with a **graph API key** and **graph ref** associated with your organization.
  * You connect your router to GraphOS by setting [these environment variables](https://www.apollographql.com/docs/graphos/reference/router/configuration#environment-variables) when starting the router.

> Learn more about the [GraphOS plan license](https://www.apollographql.com/docs/graphos/routing/license).
