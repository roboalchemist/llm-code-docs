# Source: https://documentation.onesignal.com/docs/en/greenplum.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Greenplum

> Sync custom events from Greenplum to OneSignal to trigger automated Journeys and personalized messaging campaigns based on user behavior.

export const PLATFORM_0 = "Greenplum"

export const DATA_TYPE_0 = "table columns"

export const COLUMN_HEADER_0 = "Greenplum Column"

export const PROPERTIES_DESCRIPTION_0 = "JSON/JSONB object with event metadata"

## Overview

The OneSignal + Greenplum integration enables syncing of custom events from your Greenplum database to OneSignal to trigger automated messaging campaigns and Journeys based on user behavior.

Greenplum is a massively parallel processing (MPP) database built on PostgreSQL, designed for large-scale analytics workloads.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### Greenplum

* **Greenplum instance** with network access
* **Database user** with appropriate permissions
* **Event tables** containing structured behavioral data

***

## Sync Engines and Permissions

OneSignal reads data from tables and views in Greenplum and syncs it to trigger automated messaging campaigns. To limit the load on your database, OneSignal maintains state tracking tables that enable it to only sync data that has been modified since the last sync (incremental syncs). When configuring your Greenplum connection, you'll choose a Sync Engine that determines how state tracking is handled.

The **Basic Sync Engine** maintains state tracking tables on OneSignal-owned infrastructure and is simpler to configure, requiring read access only.

The **Advanced Sync Engine** delivers enhanced performance by maintaining state tracking tables in a dedicated schema within your own Greenplum instance.

## Setup

<Steps>
  <Step title="Create a Census user">
    Create a dedicated database user for OneSignal to use:

    ```sql  theme={null}
    -- Create CENSUS user and set password
    CREATE USER CENSUS WITH PASSWORD '<strong unique password>';
    ```
  </Step>

  <Step title="Choose your sync engine and configure permissions">
    **For Basic Sync Engine (Read-only access):**

    Grant read access to your event data schema. Replace `<your schema>` with your schema name:

    ```sql  theme={null}
    -- Let the census user read all existing tables in this schema
    GRANT SELECT ON ALL TABLES IN SCHEMA "<your schema>" TO CENSUS;

    -- Let the census user read any new tables added to this schema
    ALTER DEFAULT PRIVILEGES IN SCHEMA "<your schema>" GRANT SELECT ON TABLES TO CENSUS;

    -- Let the census user execute any existing functions in this schema
    GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA "<your schema>" TO CENSUS;

    -- Let the census user execute any new functions added to this schema
    ALTER DEFAULT PRIVILEGES IN SCHEMA "<your schema>" GRANT EXECUTE ON FUNCTIONS TO CENSUS;
    ```

    **For Advanced Sync Engine (Enhanced performance):**

    First complete the Basic Sync Engine steps above, then add:

    ```sql  theme={null}
    -- Create a private bookkeeping schema where Census can store sync state
    CREATE SCHEMA CENSUS;

    -- Give the census user full access to the bookkeeping schema
    GRANT ALL ON SCHEMA CENSUS TO CENSUS;

    -- Ensure the census user has access to any existing objects in the bookkeeping schema
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA CENSUS TO CENSUS;

    -- Let the census user see your data schema
    GRANT USAGE ON SCHEMA "<your schema>" TO CENSUS;
    ```
  </Step>

  <Step title="Connect to OneSignal">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    Select **Greenplum** and provide:

    * **Host:** Your Greenplum master host
    * **Port:** 5432 (or custom port)
    * **Database:** Your database name
    * **Username:** `CENSUS`
    * **Password:** Password from Step 1
    * **Sync Engine:** Choose Basic or Advanced based on Step 2
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

### Example Event Table Schema

```sql  theme={null}
-- Example Greenplum event table
CREATE TABLE analytics.user_events (
    event_id BIGSERIAL,
    event_name VARCHAR(100) NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    event_timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    event_properties JSONB,
    session_id VARCHAR(255),
    device_type VARCHAR(50)
);
```

***

## Processing Modes

### Table Mode

Sync entire tables or views directly from your Greenplum database. OneSignal will automatically map columns to event fields.

### SQL Query Mode

Write custom PostgreSQL-compatible queries to transform your event data:

```sql  theme={null}
-- Example: Recent high-value events
SELECT
    event_name,
    user_id,
    event_timestamp,
    event_properties
FROM analytics.user_events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
    AND (event_properties->>'value')::NUMERIC > 100
ORDER BY event_timestamp DESC;
```

### MPP Query Optimization

Take advantage of Greenplum's parallel processing by ensuring your event queries are optimized for distributed execution. Use appropriate distribution keys and avoid cross-segment data movement for better performance.

***

## Advanced Network Configuration

OneSignal can successfully connect to Greenplum instances that are using advanced networking controls including region constraints, IP address allow lists, or SSH Tunneling.

We recommend configuring your Greenplum instance to use TLS v1.2 or later for all connections.

## Limitations

* Large analytical queries may impact cluster performance
* JSON/JSONB operations should be optimized for distribution
* Cross-segment joins should be minimized for performance

***

## FAQ

### Which sync engine should I choose?

Use the **Basic Sync Engine** if you prefer simpler setup and read-only access. Choose the **Advanced Sync Engine** if you need enhanced performance and can allow OneSignal to create tables in your Greenplum instance.

### How do I optimize queries for Greenplum's MPP architecture?

Ensure queries utilize distribution keys effectively, avoid unnecessary data movement between segments, and leverage Greenplum's columnar storage for analytics.

### Can I use Greenplum's external tables for event data?

Yes, OneSignal can read from external tables that reference data in formats like Parquet or CSV stored in external systems.

***

Built with [Mintlify](https://mintlify.com).
