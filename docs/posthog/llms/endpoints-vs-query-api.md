# Source: https://posthog.com/docs/endpoints/endpoints-vs-query-api.md

# Endpoints vs Query API - Docs

PostHog offers two ways to run queries programmatically: the [Query API](/docs/api/queries.md) and Endpoints. Here's how they differ and when to use each.

## Query API

The Query API is a free-form API that lets you run any query. While flexible, it has some drawbacks:

-   **Impossible to optimize** - Not knowing the query ahead of time makes it hard for us to help you get better performance.
-   **Harder to monitor** - Tracking query performance over time requires querying the `system.query_log` table manually.
-   **Future pricing** - We strongly discourage Query API usage and will eventually charge for it.

## Endpoints

Endpoints provide a more stable, purpose-built solution for production use cases:

-   **Isolated compute** - Materialized endpoints run on separate compute, avoiding the noisy neighbor problem and enabling better rate/concurrency limits.
-   **Easy monitoring** - The [**Usage** tab](/docs/endpoints/usage-analytics.md) shows performance metrics out of the box.
-   **Developer experience** - First-class features like [versioning](/docs/endpoints/versioning.md), [OpenAPI specs](/docs/endpoints/openapi-sdk-generation.md), and easy configuration.
-   **Cost and speed controls** - [Materialization](/docs/endpoints/materialization.md) and [caching](/docs/endpoints/caching.md) let you trade data freshness for performance.
-   **Abuse prevention** - Individual endpoints can be disabled if needed.

## When to use each

| Use case | Recommendation |
| --- | --- |
| Ad-hoc and explorative queries | Query API |
| Production application | Endpoints |
| Customer-facing analytics | Endpoints |
| High traffic | Endpoints |
| Data exports to a third-party (i.e. S3 or Snowflake) | [Batch exports](/docs/cdp/batch-exports.md) |

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better