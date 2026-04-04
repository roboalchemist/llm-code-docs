# Source: https://posthog.com/docs/feature-flags/local-evaluation/distributed-environments.md

# Local evaluation in distributed or stateless environments - Docs

When using [local evaluation](/docs/feature-flags/local-evaluation.md), the SDK fetches feature flag definitions and stores them in memory. This works well for single-instance applications, but in distributed or stateless environments (multiple servers, edge workers, lambdas), each instance fetches its own copy, wasting API calls and adding latency on cold starts.

An **external cache provider** lets you store flag definitions in shared storage (Redis, database, Cloudflare KV, etc.) so all instances can read from a single source.

This enables you to:

-   Share flag definitions across workers to reduce API calls
-   Coordinate fetching so only one worker polls at a time
-   Pre-cache definitions for ultra-low-latency flag evaluation

> **Note:** External cache providers are currently available in Node.js and Python SDKs only. This feature is experimental and may change in minor versions.

## When to use an external cache

| Scenario | Recommendation |
| --- | --- |
| Single server instance | SDK's built-in memory cache is sufficient |
| Multiple workers (same process) | SDK's built-in memory cache is sufficient |
| Multiple servers/containers | Use Redis or database caching with distributed locks |
| Edge workers (Cloudflare, Vercel Edge) | Use KV storage with split read/write pattern |

## Node.js

## Installation

Import the interface from the SDK:

typescript

PostHog AI

```typescript
import { FlagDefinitionCacheProvider, FlagDefinitionCacheData } from 'posthog-node/experimental'
```

## The interface

To create a custom cache, implement the `FlagDefinitionCacheProvider` interface:

typescript

PostHog AI

```typescript
interface FlagDefinitionCacheProvider {
  // Retrieve cached flag definitions
  getFlagDefinitions(): Promise<FlagDefinitionCacheData | undefined> | FlagDefinitionCacheData | undefined
  // Determine if this instance should fetch new definitions
  shouldFetchFlagDefinitions(): Promise<boolean> | boolean
  // Store definitions after a successful fetch
  onFlagDefinitionsReceived(data: FlagDefinitionCacheData): Promise<void> | void
  // Clean up resources on shutdown
  shutdown(): Promise<void> | void
}
```

When the SDK fetches flag definitions from the API, it passes a `FlagDefinitionCacheData` object to `onFlagDefinitionsReceived()` for you to store:

typescript

PostHog AI

```typescript
interface FlagDefinitionCacheData {
  flags: PostHogFeatureFlag[]               // Feature flag definitions
  groupTypeMapping: Record<string, string>  // Group type index to name mapping
  cohorts: Record<string, PropertyGroup>    // Cohort definitions for local evaluation
}
```

### Method details

| Method | Purpose | Return value |
| --- | --- | --- |
| getFlagDefinitions() | Retrieve cached definitions. Called when the poller refreshes. | Cached data, or undefined if cache is empty |
| shouldFetchFlagDefinitions() | Decide if this instance should fetch. Use for distributed coordination (e.g., locks). | true to fetch, false to skip |
| onFlagDefinitionsReceived(data) | Store definitions after a successful API fetch. | void |
| shutdown() | Release locks, close connections, clean up resources. | void |

> **Note:** All methods may throw errors. The SDK catches and logs them gracefully, ensuring cache provider errors never break flag evaluation.

## Using your cache provider

Pass your cache provider when initializing PostHog:

typescript

PostHog AI

```typescript
import { PostHog } from 'posthog-node'
const cache = new YourCacheProvider()
const posthog = new PostHog('<ph_project_token>', {
  personalApiKey: '<ph_personal_api_key>',
  enableLocalEvaluation: true,
  flagDefinitionCacheProvider: cache,
})
```

## Python

## Installation

Import the interface from the SDK:

Python

PostHog AI

```python
from posthog import FlagDefinitionCacheProvider, FlagDefinitionCacheData
```

## The interface

To create a custom cache, implement the `FlagDefinitionCacheProvider` protocol:

Python

PostHog AI

```python
class FlagDefinitionCacheProvider(Protocol):
    def get_flag_definitions(self) -> Optional[FlagDefinitionCacheData]:
        """Retrieve cached flag definitions."""
        ...
    def should_fetch_flag_definitions(self) -> bool:
        """Determine if this instance should fetch new definitions."""
        ...
    def on_flag_definitions_received(self, data: FlagDefinitionCacheData) -> None:
        """Store definitions after a successful fetch."""
        ...
    def shutdown(self) -> None:
        """Clean up resources on shutdown."""
        ...
```

When the SDK fetches flag definitions from the API, it passes a `FlagDefinitionCacheData` object to `on_flag_definitions_received()` for you to store:

Python

PostHog AI

```python
class FlagDefinitionCacheData(TypedDict):
    flags: List[Dict[str, Any]]           # Feature flag definitions
    group_type_mapping: Dict[str, str]    # Group type index to name mapping
    cohorts: Dict[str, Any]               # Cohort definitions for local evaluation
```

### Method details

| Method | Purpose | Return value |
| --- | --- | --- |
| get_flag_definitions() | Retrieve cached definitions. Called when the poller refreshes. | Cached data, or None if cache is empty |
| should_fetch_flag_definitions() | Decide if this instance should fetch. Use for distributed coordination (e.g., locks). | True to fetch, False to skip |
| on_flag_definitions_received(data) | Store definitions after a successful API fetch. | None |
| shutdown() | Release locks, close connections, clean up resources. | None |

> **Note:** All methods may throw errors. The SDK catches and logs them gracefully, ensuring cache provider errors never break flag evaluation.

## Using your cache provider

Pass your cache provider when initializing PostHog:

Python

PostHog AI

```python
from posthog import Posthog
cache = YourCacheProvider()
posthog = Posthog(
    '<ph_project_token>',
    personal_api_key='<ph_personal_api_key>',
    flag_definition_cache_provider=cache,
)
```

## Common patterns

### Shared caches with locking

When running multiple server instances with a shared cache like Redis, coordinate fetching so only one instance polls PostHog at a time.

The recommended pattern:

-   One instance owns the lock for its entire lifetime, not just during a single fetch
-   Refresh the lock TTL each polling cycle to maintain ownership
-   Release on shutdown, but only if you own the lock
-   Let locks expire if a process crashes, so another instance can take over

#### Redis example

A complete working example written in Python using Redis with distributed locking is available in the [posthog-python repository](https://github.com/PostHog/posthog-python/blob/master/examples/redis_flag_cache.py). It implements the locking pattern described above.

### Caches without locking

Some storage backends like Cloudflare KV don't support atomic locking operations. In these cases, use a split read/write pattern:

1.  A scheduled job (cron) periodically fetches flag definitions and writes to the cache
2.  Request handlers read from the cache and evaluate flags locally, with no API calls

This separates the concerns entirely. One process writes, all others read.

#### Cloudflare Workers example

A complete working example written in TypeScript is available in the [posthog-js repository](https://github.com/PostHog/posthog-js/tree/main/examples/example-cloudflare-kv-cache). It uses the split read/write pattern described above. The worker's scheduled job writes flag definitions to KV, and request handlers read from it.

This pattern is ideal for high-traffic edge applications where flag evaluation must be extremely fast and you can tolerate flag updates being slightly delayed.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better