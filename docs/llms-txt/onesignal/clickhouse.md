# Source: https://documentation.onesignal.com/docs/en/clickhouse.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ClickHouse

> Sync custom events from ClickHouse to OneSignal to trigger automated Journeys and personalized messaging campaigns based on user behavior.

export const PLATFORM_0 = "ClickHouse"

export const DATA_TYPE_0 = "event table columns"

export const COLUMN_HEADER_0 = "ClickHouse Column"

export const PROPERTIES_DESCRIPTION_0 = "JSON column or multiple columns"

## Overview

The OneSignal + ClickHouse integration enables automatic syncing of custom events from your ClickHouse analytics database to OneSignal. This allows you to trigger automated Journeys and personalized messaging campaigns based on user behavioral data stored in your high-performance columnar database.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### ClickHouse

* **ClickHouse server** (self-hosted or cloud)
* **Database credentials** with read access to event tables
* **Event data tables** containing behavioral data with proper schema

***

## Setup

<Steps>
  <Step title="Create ClickHouse user for OneSignal">
    Create a dedicated user account for OneSignal with read-only access to your event tables:

    ```sql  theme={null}
    CREATE USER onesignal_reader IDENTIFIED BY 'strong_password';
    GRANT SELECT ON event_database.* TO onesignal_reader;
    ```
  </Step>

  <Step title="Configure network access">
    Ensure OneSignal can connect to your ClickHouse instance:

    * **Self-hosted**: Allow connections from OneSignal's IP addresses
    * **ClickHouse Cloud**: Add OneSignal IPs to your allowlist
    * **Port**: Default ClickHouse port is 8123 (HTTP) or 9000 (native)
  </Step>

  <Step title="Add integration in OneSignal">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    Select **ClickHouse** and provide:

    * **Host**: Your ClickHouse server hostname or IP
    * **Port**: ClickHouse port (default: 8123 for HTTP, 9000 for native)
    * **Database**: Database name containing event tables
    * **Username**: `onesignal_reader` (or your chosen username)
    * **Password**: Password for the ClickHouse user
    * **Protocol**: HTTP or Native (HTTP recommended for simplicity)
  </Step>

  <Step title="Configure event data source">
    Specify the ClickHouse table containing your event data:

    * **Table**: Table name containing event records (e.g., `user_events`)
    * **Event Query**: Optional SQL query to filter or transform event data

    Your event table should contain columns for:

    * Event name/type (String)
    * User identifier (String)
    * Event timestamp (DateTime)
    * Additional event properties (JSON or individual columns)
  </Step>

  <Step title="Test the connection">
    Click **Test Connection** to verify OneSignal can access your ClickHouse database and read event data.
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

***

## Advanced Configuration

### Custom SQL Queries

Use custom SQL to filter or transform event data before syncing to OneSignal:

```sql  theme={null}
SELECT
  event_name,
  user_id,
  toDateTime(event_timestamp) as timestamp,
  toJSONString(
    map(
      'product_id', product_id,
      'purchase_amount', purchase_amount,
      'category', category
    )
  ) as payload
FROM user_events
WHERE event_timestamp >= now() - INTERVAL 7 DAY
  AND event_name IN ('purchase', 'signup', 'upgrade')
ORDER BY event_timestamp DESC
```

### Performance Optimization

ClickHouse is optimized for analytical queries. Consider:

* **Partitioning**: Use date-based partitioning on event timestamp
* **Indexing**: Create appropriate indexes on user\_id and event\_name
* **Materialized Views**: Pre-aggregate event data for faster querying

<Warning>
  ClickHouse is optimized for append-only workloads. Ensure your event data follows this pattern for best performance.
</Warning>

***

## FAQ

### How often does OneSignal sync events from ClickHouse?

OneSignal syncs event data based on your configured schedule, with a minimum interval of 15 minutes.

### Can I sync events from multiple ClickHouse tables?

Yes, you can create multiple integrations for different tables or use UNION queries to combine data from multiple tables.

Built with [Mintlify](https://mintlify.com).
