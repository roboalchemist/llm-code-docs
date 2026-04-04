# Source: https://documentation.onesignal.com/docs/en/motherduck.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# MotherDuck

> Sync custom events from MotherDuck to OneSignal to trigger automated Journeys and personalized messaging campaigns based on user behavior.

export const PLATFORM_0 = "MotherDuck"

export const DATA_TYPE_0 = "table columns"

export const COLUMN_HEADER_0 = "MotherDuck Column"

export const PROPERTIES_DESCRIPTION_0 = "JSON object with event metadata"

## Overview

The OneSignal + MotherDuck integration enables automatic syncing of custom events from your MotherDuck databases to OneSignal to trigger automated messaging campaigns and Journeys based on user behavior.

MotherDuck is a DuckDB-in-the-cloud service that provides fast OLAP (Online Analytical Processing) capabilities with the simplicity of SQL.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### MotherDuck

* **MotherDuck account** with database access
* **Service token** for authentication
* **Database** containing event data
* **Tables or views** with structured event information

***

## Setup

<Steps>
  <Step title="Create MotherDuck service token">
    Generate an access token for OneSignal to connect to MotherDuck:

    1. Log in to the MotherDuck Web UI at `app.motherduck.com`
    2. Click your profile in the top-left corner
    3. Navigate to **Settings** > **General** > **Access Tokens**
    4. Click **Create Token**
    5. Set expiration date (or leave unlimited)
    6. Copy the generated service token
  </Step>

  <Step title="Prepare your event data">
    Ensure your MotherDuck database contains properly structured event tables:

    ```sql  theme={null}
    -- Example event table structure
    CREATE TABLE user_events (
        event_name VARCHAR,
        user_id VARCHAR,
        event_timestamp TIMESTAMP,
        event_properties JSON,
        session_id VARCHAR
    );
    ```
  </Step>

  <Step title="Connect to OneSignal">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    Select **MotherDuck** and provide:

    * **Service Token:** Token from Step 1
    * **Database Name:** Your MotherDuck database name
    * **Connection String:** `md:your_database_name`
  </Step>

  <Step title="Configure data sync">
    Select the tables or write custom SQL queries to define which event data to sync:

    ```sql  theme={null}
    SELECT
        event_name,
        user_id,
        event_timestamp,
        event_properties
    FROM user_events
    WHERE event_timestamp >= CURRENT_DATE - INTERVAL 7 DAYS
    ```
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

### Example Event Query

```sql  theme={null}
-- Optimized event query for OneSignal sync
SELECT
    event_name,
    user_id,
    event_timestamp,
    {
        'source': 'motherduck',
        'session_id': session_id,
        'device_type': device_type,
        'value': event_value
    }::JSON as event_properties
FROM analytics.user_events
WHERE event_timestamp >= CURRENT_TIMESTAMP - INTERVAL 1 DAY
ORDER BY event_timestamp DESC
```

***

## Processing Modes

### Table Mode

Sync entire tables directly from your MotherDuck database. OneSignal will automatically map columns to event fields.

### SQL Query Mode

Write custom DuckDB SQL queries to transform and filter your event data:

```sql  theme={null}
-- Advanced event aggregation
SELECT
    'daily_summary' as event_name,
    user_id,
    DATE_TRUNC('day', event_timestamp) as event_timestamp,
    {
        'total_events': COUNT(*),
        'unique_sessions': COUNT(DISTINCT session_id),
        'last_activity': MAX(event_timestamp)
    }::JSON as event_properties
FROM user_events
WHERE event_timestamp >= CURRENT_DATE - INTERVAL 7 DAYS
GROUP BY user_id, DATE_TRUNC('day', event_timestamp)
```

***

## Limitations

* Query complexity affects sync performance
* Large result sets may impact sync speed
* JSON parsing requires proper column typing

***

## FAQ

### How do I optimize query performance in MotherDuck?

Use DuckDB's columnar storage advantages by selecting only needed columns and applying filters early in your queries.

### Can I sync from multiple MotherDuck databases?

Yes, you can create separate integrations for each MotherDuck database in your account.

***

Built with [Mintlify](https://mintlify.com).
