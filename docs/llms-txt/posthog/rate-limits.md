# Source: https://posthog.com/docs/endpoints/rate-limits.md

# Rate limits - Docs

Endpoints can provide better rate limits than other APIs depending on how they're configured.

## Direct execution

Endpoints running with direct execution (no materialization) have the same rate limits as the standard [API rate limits](/docs/api.md#rate-limiting).

## Materialized endpoints

Materialized endpoints have higher limits because their execution goes through a different compute path:

-   **Burst**: 1,200 requests/minute
-   **Sustained**: 12,000 requests/hour
-   **Concurrency**: 10 concurrent requests

## Need higher limits?

If you need higher rate and concurrency limits, [materialize your endpoints](/docs/endpoints/materialization.md). If that's still not enough, [talk to us](/talk-to-a-human.md).

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better