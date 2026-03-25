# Source: https://documentation.onesignal.com/docs/en/materialize.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Materialize

> Sync custom events from Materialize to OneSignal to trigger automated Journeys and personalized messaging campaigns based on real-time user behavior.

export const PLATFORM_0 = "Materialize"

export const DATA_TYPE_0 = "view or table columns"

export const COLUMN_HEADER_0 = "Materialize Column"

export const PROPERTIES_DESCRIPTION_0 = "JSON object with event metadata"

## Overview

The OneSignal + Materialize integration enables automatic syncing of custom events from your Materialize streaming database to OneSignal to trigger automated messaging campaigns and Journeys based on real-time user behavior.

Materialize is a PostgreSQL-compatible streaming database that maintains incrementally updated views of your data, enabling real-time analytics and event processing.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### Materialize

* **Materialize account** with console access
* **App Password** for external tool authentication
* **Materialized views** or tables containing event data
* **Event data** accessible in your Materialize database

***

## Setup

<Steps>
  <Step title="Get Materialize connection details">
    Sign in to the Materialize console and navigate to the **Connect** page to find your connection details.
  </Step>

  <Step title="Create App Password">
    In the Materialize console, create a new **App Password** for OneSignal to use for authentication.
  </Step>

  <Step title="Connect to OneSignal">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    Select **Materialize** and provide:

    * **Host:** Your Materialize host name (found under **External Tools** in the Materialize console Connect page)
    * **Username:** Your email address (used to sign in to Materialize)
    * **Password:** The App Password created in Step 2
    * **Database:** Database name (optional, defaults to `materialize`)
  </Step>

  <Step title="Test connection">
    Click **Test** to verify the connection is working correctly.
  </Step>
</Steps>

***

### Event data mapping

Map your {PLATFORM_0} {DATA_TYPE_0} to OneSignal's custom events format:

| OneSignal Field | {COLUMN_HEADER_0} | Description                | Required |
| --------------- | ----------------- | -------------------------- | -------- |
| `name`          | `event_name`      | Event identifier           | Yes      |
| `external_id`   | `user_id`         | User identifier            | Yes      |
| `timestamp`     | `event_timestamp` | When event occurred        | No       |
| `properties`    | `event_data`      | {PROPERTIES_DESCRIPTION_0} | No       |

### Example Real-time Event View

```sql  theme={null}
-- Real-time materialized view for recent events
CREATE MATERIALIZED VIEW analytics.recent_user_events AS
SELECT
    event_name,
    user_id,
    event_timestamp,
    event_properties,
    session_id,
    device_type
FROM raw_events.stream
WHERE event_timestamp >= NOW() - INTERVAL '1 day';
```

***

## Processing Modes

### Materialized Views (Recommended)

Leverage Materialize's real-time processing by syncing from materialized views that automatically update as new data arrives:

```sql  theme={null}
-- High-value events materialized view
CREATE MATERIALIZED VIEW analytics.high_value_events AS
SELECT
    event_name,
    user_id,
    event_timestamp,
    event_properties || jsonb_build_object(
        'source', 'materialize',
        'value_tier', 'high'
    ) as event_properties
FROM raw_events.stream
WHERE (event_properties->>'value')::numeric > 100;
```

### SQL Query Mode

Write custom PostgreSQL-compatible queries to transform your event data:

```sql  theme={null}
-- Real-time user activity summary
SELECT
    'activity_summary' as event_name,
    user_id,
    NOW() as event_timestamp,
    jsonb_build_object(
        'events_last_hour', COUNT(*),
        'unique_sessions', COUNT(DISTINCT session_id),
        'total_value', SUM((event_properties->>'value')::numeric),
        'last_seen', MAX(event_timestamp)
    ) as event_properties
FROM analytics.recent_user_events
WHERE event_timestamp >= NOW() - INTERVAL '1 hour'
GROUP BY user_id
HAVING COUNT(*) >= 5;
```

### Real-time Stream Processing

```sql  theme={null}
-- Progressive profiling view
CREATE MATERIALIZED VIEW analytics.user_progression AS
SELECT
    user_id,
    COUNT(*) as total_events,
    COUNT(DISTINCT event_name) as unique_event_types,
    MAX(event_timestamp) as last_activity,
    CASE
        WHEN COUNT(*) >= 50 THEN 'power_user'
        WHEN COUNT(*) >= 20 THEN 'active_user'
        WHEN COUNT(*) >= 5 THEN 'engaged_user'
        ELSE 'new_user'
    END as user_segment
FROM raw_events.stream
GROUP BY user_id;
```

***

## Limitations

* Materialize only supports the Basic Sync Engine
* Real-time queries may consume more compute resources
* Complex joins across large datasets should be optimized
* Materialized views require ongoing cluster resources

***

## FAQ

### How do I optimize real-time performance in Materialize?

Use indexes on frequently queried columns and consider partitioning large event datasets by time ranges for better performance.

### Can I sync from both tables and materialized views?

Yes, OneSignal can read from both static tables and real-time materialized views in Materialize.

### How does real-time syncing work?

Materialize maintains incrementally updated views, so OneSignal will always read the latest state of your data without additional processing overhead.

***

Built with [Mintlify](https://mintlify.com).
