# Source: https://documentation.onesignal.com/docs/en/trino.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Trino

> Sync custom events from Trino to OneSignal to trigger automated Journeys and personalized messaging campaigns based on user behavior.

export const PLATFORM_0 = "Trino"

export const DATA_TYPE_0 = "event data"

export const COLUMN_HEADER_0 = "Trino Column"

export const PROPERTIES_DESCRIPTION_0 = "Event metadata as JSON"

## Overview

The OneSignal + Trino integration enables syncing of custom events from your Trino cluster to OneSignal to trigger automated messaging campaigns and Journeys based on user behavior.

Trino is a distributed SQL query engine designed for running fast analytics queries against large datasets from multiple sources.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### Trino

* **Trino cluster** with network access
* **User credentials** with appropriate permissions
* **TLS connection** support (required by OneSignal)
* **Event data** accessible through Trino catalogs

***

## Setup

<Steps>
  <Step title="Configure Trino connection">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    Select **Trino** and provide the following connection details:

    * **Host:** Your Trino cluster hostname
    * **Username:** Your Trino username
    * **Password:** Your Trino password
    * **Port:** 443 (default) or your custom port

    <Info>
      OneSignal requires a TLS connection to Trino. If your instance doesn't run on port 443, specify your custom port.
    </Info>
  </Step>

  <Step title="Configure Advanced Sync Engine (Optional)">
    For enhanced performance, set up a dedicated CENSUS catalog:

    1. Create a catalog named `CENSUS` containing a schema named `CENSUS`
    2. Ensure your connector supports:
       * `CREATE TABLE` and `DROP TABLE` operations
       * Table writes (INSERT, DELETE, UPDATE)
       * `CREATE OR REPLACE TABLE` statement
    3. Grant full permissions on the `CENSUS.CENSUS` schema to your OneSignal user

    <Info>
      Tested configurations include MySQL, PostgreSQL, Snowflake, Iceberg, and Delta Lake connectors.
    </Info>
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
-- Example: Recent high-value events across catalogs
SELECT
    event_name,
    user_id,
    event_timestamp,
    CAST(event_properties AS JSON) as event_properties
FROM catalog.schema.user_events
WHERE event_timestamp >= current_timestamp - INTERVAL '7' DAY
    AND JSON_EXTRACT_SCALAR(event_properties, '$.value') > '100'
ORDER BY event_timestamp DESC;
```

### Cross-Catalog Event Queries

```sql  theme={null}
-- Example: Federated query across multiple data sources
SELECT
    'combined_activity' as event_name,
    u.user_id,
    current_timestamp as event_timestamp,
    JSON_FORMAT(JSON_OBJECT(
        'web_sessions', w.session_count,
        'mobile_events', m.event_count,
        'purchase_value', p.total_value
    )) as event_properties
FROM postgres_catalog.users.profiles u
LEFT JOIN web_catalog.analytics.sessions w ON u.user_id = w.user_id
LEFT JOIN mobile_catalog.events.activities m ON u.user_id = m.user_id
LEFT JOIN purchases_catalog.orders.summary p ON u.user_id = p.user_id
WHERE u.created_date >= current_date - INTERVAL '30' DAY;
```

***

## Sync Engine Options

### Basic Sync Engine

* Works with any Trino catalog and connector
* State tracking managed by OneSignal infrastructure
* Simpler setup with no additional requirements

### Advanced Sync Engine

* Enhanced performance with local state tracking
* Requires dedicated `CENSUS.CENSUS` catalog and schema
* Supports connectors with table write operations
* Recommended for high-volume event processing

***

## Supported Connectors

OneSignal's Advanced Sync Engine has been tested with:

* **MySQL connector** (read-write mode)
* **PostgreSQL connector** (read-write mode)
* **Snowflake connector** (read-write mode)
* **Iceberg connector** (with S3 and AWS Glue)
* **Delta Lake connector** (with AWS Glue and Starburst Galaxy catalogs)

***

## Limitations

* TLS connection required (OneSignal security requirement)
* Advanced Sync Engine requires `CREATE OR REPLACE TABLE` support (Trino October 2023+)
* Warehouse Writeback not yet supported (coming soon)
* Cannot provide custom table options in `WITH` clause

***

## FAQ

### Which Trino connectors work with OneSignal?

Any connector that supports read operations works with Basic Sync Engine. For Advanced Sync Engine, you need connectors that support table writes and `CREATE OR REPLACE TABLE`.

### Can I query multiple catalogs in a single sync?

Yes! Trino's federated query capabilities allow you to combine event data from multiple sources (PostgreSQL, MySQL, S3, etc.) in a single query.

### Do I need the Advanced Sync Engine?

No, Basic Sync Engine works well for most use cases. Use Advanced Sync Engine if you need enhanced performance and can set up the required `CENSUS.CENSUS` catalog.

Built with [Mintlify](https://mintlify.com).
