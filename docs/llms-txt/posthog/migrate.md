# Source: https://posthog.com/docs/migrate.md

# Historical migrations overview - Docs

> Prior to starting a historical data migration, ensure you do the following:
>
> 1.  Create a project on our [US](https://us.posthog.com/signup) or [EU](https://eu.posthog.com/signup) Cloud.
> 2.  Sign up to a paid product analytics plan on [the billing page](https://us.posthog.com/organization/billing) (historic imports are free but this unlocks the necessary features).
> 3.  Set the `historical_migration` option to `true` when capturing events in the migration. This is automated if you are running a [managed migration](/docs/migrate/managed-migrations.md).

Historical migrations refer to ingesting and importing past data into PostHog for analysis. This includes:

-   Using [managed migrations](/docs/migrate/managed-migrations.md) for automated data import from Mixpanel, Amplitude or S3 buckets.

-   Migrating from a different tool or platform like [Google Analytics](/docs/migrate/google-analytics.md), [Heap](/docs/migrate/migrate-from-amplitude.md), [Plausible](/docs/migrate/plausible.md), or [LaunchDarkly](/docs/migrate/launchdarkly.md).

-   Migrating from a [self-hosted PostHog instance to PostHog Cloud](/docs/migrate/migrate-to-cloud.md).

-   Migrating from [one PostHog Cloud instance to another](/docs/migrate/migrate-to-cloud.md#between-cloud-instances-eg-us-cloud-to-eu-cloud), for example US -> EU.

-   Adding past data from a third-party source into PostHog.

> **What about exporting data from PostHog?** Use our [batch export feature](/docs/cdp/batch-exports.md) to export data from PostHog to external services like [S3](/docs/cdp/batch-exports/s3.md) or [BigQuery](/docs/cdp/batch-exports/bigquery.md).

## The basics of migrating data into PostHog

Start your migration by formatting your data correctly. There is no way to selectively delete event data in PostHog, so getting this right is critical. This means:

-   **Using the correct event names.** For example, to capture a pageview event in PostHog, you capture a `$pageview` event. This might be different than the "name" other services use.

-   **Including the `timestamp` field.** This ensures your events are ingested with the correct time in PostHog. It needs to be in the ISO 8601 format and dated at least 48 hours before the time of import.

-   **Use the correct `distinct_id`.** This is the unique identifier for your user in PostHog. Every event needs one. For example, `posthog-js` automatically generates a `uuidv7` value for anonymous users.

To capture events, you must use the PostHog Python SDK or the PostHog API `batch` endpoint with the `historical_migration` set to `true`. This ensures we handle this data correctly and you aren't charged standard ingestion fees for it.

Using our Python or Node SDKs, you can capture events like this:

PostHog AI

### Python

```python
from posthog import Posthog
from datetime import datetime
posthog = Posthog(
    '<ph_project_token>',
    host='https://us.i.posthog.com',
    debug=True,
    historical_migration=True
)
events = [
  {
    "event": "batched_event_name",
    "properties": {
      "distinct_id": "user_id",
      "timestamp": datetime.fromisoformat("2024-04-02T12:00:00")
    }
  },
  {
    "event": "batched_event_name",
    "properties": {
      "distinct_id": "used_id",
      "timestamp": datetime.fromisoformat("2024-04-02T12:00:00")
    }
  }
]
for event in events:
  posthog.capture(
    distinct_id=event["properties"]["distinct_id"],
    event=event["event"],
    properties=event["properties"],
    timestamp=event["properties"]["timestamp"],
  )
```

### Node.js

```javascript
import { PostHog } from 'posthog-node'
const client = new PostHog(
    '<ph_project_token>',
    {
      host: 'https://us.i.posthog.com',
      historicalMigration: true
    }
)
client.debug()
client.capture({
    event: "batched_event_name",
    distinctId: "user_id",
    properties: {},
    timestamp: "2024-04-03T12:00:00Z"
})
client.capture({
    event: "batched_event_name",
    distinctId: "user_id",
    properties: {},
    timestamp: "2024-04-03T13:00:00Z"
})
await client.shutdown()
```

An example `cURL` implementation using the `batch` API endpoint looks like this:

PostHog AI

### Terminal

```bash
curl -v -L --header "Content-Type: application/json" -d '{
  "api_key": "<ph_project_token>",
  "historical_migration": true,
  "batch": [
    {
      "event": "batched_event_name",
      "properties": {
        "distinct_id": "user_id"
      },
      "timestamp": "2024-04-03T12:00:00Z"
    },
    {
      "event": "batched_event_name",
      "properties": {
        "distinct_id": "user_id"
      },
      "timestamp": "2024-04-03T12:00:00Z"
    }
  ]
}' https://us.i.posthog.com/batch/
```

### Python

```python
# The Python SDK also support historical migrations
# See: /docs/libraries/python#historical-migrations
import requests
import json
url = "https://us.i.posthog.com/batch/"
headers = {
  "Content-Type": "application/json"
}
payload = {
  "api_key": "<ph_project_token>",
  "historical_migration": True,
  "batch": [
    {
      "event": "batched_event_name",
      "properties": {
        "distinct_id": "user_id",
      },
      "timestamp": "2024-04-03T12:00:00Z"
    },
    {
      "event": "batched_event_name",
      "properties": {
        "distinct_id": "user_id"
      },
      "timestamp": "2024-04-03T12:00:00Z"
    }
  ]
}
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.text)
```

> Need someone to do the migration for you? A PostHog [forward-deployed engineer](/services.md) can help!

## Best practices for migrations

-   We highly recommend testing at least a part of your migration on a test project before running it on your production project.

-   Separate exporting your data from your service from importing it into PostHog. Store it in a storage service like S3 or GCS in between to ensure exported data is complete.

-   Build resumability into your exports and imports, so you can just resume the process from the last successful point if any problems occur. For example, we use a cursor-based approach in our self-hosted migration tool.

-   To batch user updates, use the same request but with the `$identify` event. Same for groups and the `$group_identify` event.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better