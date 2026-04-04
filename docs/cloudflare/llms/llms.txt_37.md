# Source: https://developers.cloudflare.com/analytics/llms.txt

# Analytics

Visualize the performance, security, and reliability data collected by Cloudflare products

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/analytics/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Analytics llms-full.txt](https://developers.cloudflare.com/analytics/llms-full.txt) for the complete Analytics documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Analytics](https://developers.cloudflare.com/analytics/index.md)

## Types of analytics

- [Types of analytics](https://developers.cloudflare.com/analytics/types-of-analytics/index.md)

## Understanding sampling in Cloudflare Analytics

- [Understanding sampling in Cloudflare Analytics](https://developers.cloudflare.com/analytics/sampling/index.md)

## Network analytics

- [Network analytics](https://developers.cloudflare.com/analytics/network-analytics/index.md)
- [Adjust the displayed data](https://developers.cloudflare.com/analytics/network-analytics/configure/displayed-data/index.md)
- [Share and export data](https://developers.cloudflare.com/analytics/network-analytics/configure/share-export/index.md)
- [Adjust the time range](https://developers.cloudflare.com/analytics/network-analytics/configure/time-range/index.md)
- [Get started](https://developers.cloudflare.com/analytics/network-analytics/get-started/index.md): Learn how to view and use data from Network Analytics.
- [Data collection](https://developers.cloudflare.com/analytics/network-analytics/reference/data-collection/index.md)
- [Concepts](https://developers.cloudflare.com/analytics/network-analytics/understand/concepts/index.md)
- [Main dashboard](https://developers.cloudflare.com/analytics/network-analytics/understand/main-dashboard/index.md)

## GraphQL Analytics API

- [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/index.md)
- [Error responses](https://developers.cloudflare.com/analytics/graphql-api/errors/index.md)
- [Confidence Intervals](https://developers.cloudflare.com/analytics/graphql-api/features/confidence-intervals/index.md)
- [Datasets (tables)](https://developers.cloudflare.com/analytics/graphql-api/features/data-sets/index.md)
- [Discovery](https://developers.cloudflare.com/analytics/graphql-api/features/discovery/index.md)
- [Introspection](https://developers.cloudflare.com/analytics/graphql-api/features/discovery/introspection/index.md)
- [Settings node](https://developers.cloudflare.com/analytics/graphql-api/features/discovery/settings/index.md)
- [Filtering](https://developers.cloudflare.com/analytics/graphql-api/features/filtering/index.md)
- [Nested Structures](https://developers.cloudflare.com/analytics/graphql-api/features/nested-structures/index.md)
- [Pagination](https://developers.cloudflare.com/analytics/graphql-api/features/pagination/index.md)
- [Sorting](https://developers.cloudflare.com/analytics/graphql-api/features/sorting/index.md)
- [Get started](https://developers.cloudflare.com/analytics/graphql-api/getting-started/index.md)
- [Authentication](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/index.md)
- [Authenticate with a Cloudflare API key](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/api-key-auth/index.md)
- [Configure an Analytics API token](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/api-token-auth/index.md)
- [Configure GraphQL client endpoint and HTTP headers](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/graphql-client-headers/index.md)
- [Compose a query in GraphiQL](https://developers.cloudflare.com/analytics/graphql-api/getting-started/compose-graphql-query/index.md): Learn how to use a GraphiQL client to compose and execute a GraphQL query. This guide covers setting up a query, selecting the dataset, and configuring parameters and fields.
- [Execute a GraphQL query with curl](https://developers.cloudflare.com/analytics/graphql-api/getting-started/execute-graphql-query/index.md)
- [Explore the GraphQL schema](https://developers.cloudflare.com/analytics/graphql-api/getting-started/explore-graphql-schema/index.md)
- [Querying basics](https://developers.cloudflare.com/analytics/graphql-api/getting-started/querying-basics/index.md): Learn the basics of querying with Cloudflare's GraphQL API. Understand query structure, schema, and how to fetch data using GraphQL queries.
- [Limits](https://developers.cloudflare.com/analytics/graphql-api/limits/index.md)
- [MCP server](https://developers.cloudflare.com/analytics/graphql-api/mcp-server/index.md)
- [Migration guides](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/index.md)
- [HTTP Requests by Colo Groups to HTTP Requests by Adaptive Groups](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/graphql-api-analytics/index.md)
- [Network Analytics v1 to Network Analytics v2](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/index.md)
- [Main differences](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/differences/index.md)
- [NAv2 node reference](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/index.md)
- [NAv1 to NAv2 schema map](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/schema-map/index.md)
- [Zone Analytics to GraphQL Analytics](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/zone-analytics/index.md)
- [Zone Analytics Colos Endpoint to GraphQL Analytics](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/zone-analytics-colos/index.md)
- [Sampling](https://developers.cloudflare.com/analytics/graphql-api/sampling/index.md)
- [Capture GraphQL queries with Chrome DevTools](https://developers.cloudflare.com/analytics/graphql-api/tutorials/capture-graphql-queries-from-dashboard/index.md)
- [Querying HTTP events by hostname with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/end-customer-analytics/index.md)
- [Querying Access login events with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-access-login-events/index.md)
- [Querying Email Routing events with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-email-routing/index.md)
- [Querying Firewall Events with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-firewall-events/index.md)
- [Querying Magic Transit endpoint health check results with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-magic-transit-endpoint-healthcheck-results/index.md)
- [Querying Magic Transit and Cloudflare WAN IPsec/GRE tunnel bandwidth analytics with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-magic-transit-tunnel-bandwidth-analytics/index.md)
- [Querying Magic Transit and Cloudflare WAN IPsec/GRE tunnel health check results with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-magic-transit-tunnel-healthcheck-results/index.md)
- [Querying Cloudflare Network Firewall Intrusion Detection System (IDS) samples with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-network-firewall-ids-samples/index.md)
- [Querying Cloudflare Network Firewall Samples with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-network-firewall-samples/index.md)
- [Querying Workers Metrics with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-workers-metrics/index.md)
- [Use GraphQL to create widgets](https://developers.cloudflare.com/analytics/graphql-api/tutorials/use-graphql-create-widgets/index.md)

## Workers Analytics Engine

- [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/index.md)
- [Get started](https://developers.cloudflare.com/analytics/analytics-engine/get-started/index.md)
- [Querying from Grafana](https://developers.cloudflare.com/analytics/analytics-engine/grafana/index.md)
- [Limits](https://developers.cloudflare.com/analytics/analytics-engine/limits/index.md)
- [Pricing](https://developers.cloudflare.com/analytics/analytics-engine/pricing/index.md): Workers Analytics Engine is priced based on two metrics âÂ data points written, and read queries.
- [Usage-based billing](https://developers.cloudflare.com/analytics/analytics-engine/recipes/usage-based-billing-for-your-saas-product/index.md): How to use Workers Analytics Engine to build usage-based billing into your SaaS product
- [Sampling with WAE](https://developers.cloudflare.com/analytics/analytics-engine/sampling/index.md): How data written to Workers Analytics Engine is automatically sampled at scale
- [SQL API](https://developers.cloudflare.com/analytics/analytics-engine/sql-api/index.md): The SQL API for Workers Analytics Engine
- [Aggregate functions](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/index.md)
- [Bit functions](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/bit-functions/index.md)
- [Conditional functions](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/conditional-functions/index.md)
- [Date and Time functions](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/date-time-functions/index.md)
- [Encoding functions](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/index.md)
- [Literals](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/literals/index.md)
- [Mathematical functions](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/mathematical-functions/index.md)
- [Operators](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/operators/index.md)
- [Statements](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/statements/index.md)
- [String functions](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/string-functions/index.md)
- [Type conversion functions](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/type-conversion-functions/index.md)
- [Querying from a Worker](https://developers.cloudflare.com/analytics/analytics-engine/worker-querying/index.md)

## Analytics integrations

- [Analytics integrations](https://developers.cloudflare.com/analytics/analytics-integrations/index.md)
- [Datadog](https://developers.cloudflare.com/analytics/analytics-integrations/datadog/index.md): This tutorial explains how to analyze Cloudflare metrics using the Cloudflare Integration tile for Datadog
- [Graylog](https://developers.cloudflare.com/analytics/analytics-integrations/graylog/index.md): This tutorial explains how to analyze Cloudflare Logs using Graylog. The Graylog integration is available on GitHub.
- [New Relic](https://developers.cloudflare.com/analytics/analytics-integrations/new-relic/index.md): This tutorial explains how to analyze Cloudflare metrics using the New Relic One Cloudflare Quickstart.
- [Sentinel](https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/index.md)
- [Splunk](https://developers.cloudflare.com/analytics/analytics-integrations/splunk/index.md): This tutorial explains how to analyze Cloudflare Logs using the Cloudflare App for Splunk.

## account-and-zone-analytics

- [Account analytics (beta)](https://developers.cloudflare.com/analytics/account-and-zone-analytics/account-analytics/index.md)
- [Cloudflare analytics with Workers](https://developers.cloudflare.com/analytics/account-and-zone-analytics/analytics-with-workers/index.md)
- [Status codes](https://developers.cloudflare.com/analytics/account-and-zone-analytics/status-codes/index.md)
- [Threat types](https://developers.cloudflare.com/analytics/account-and-zone-analytics/threat-types/index.md)
- [Total threats stopped](https://developers.cloudflare.com/analytics/account-and-zone-analytics/total-threats-stopped/index.md)
- [Zone Analytics](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/index.md)

## faq

- [About Cloudflare Analytics](https://developers.cloudflare.com/analytics/faq/about-analytics/index.md)
- [GraphQL API inconsistent results](https://developers.cloudflare.com/analytics/faq/graphql-api-inconsistent-results/index.md)
- [Other FAQs](https://developers.cloudflare.com/analytics/faq/other-faqs/index.md)
- [Workers Analytics Engine FAQs](https://developers.cloudflare.com/analytics/faq/wae-faqs/index.md)