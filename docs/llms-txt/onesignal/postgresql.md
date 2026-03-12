# Source: https://documentation.onesignal.com/docs/en/postgresql.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# PostgreSQL

> Sync custom events from PostgreSQL to OneSignal to trigger automated Journeys and personalized messaging campaigns based on user behavior.

export const PLATFORM_0 = "PostgreSQL"

export const DATA_TYPE_0 = "columns"

export const COLUMN_HEADER_0 = "PostgreSQL Column"

export const PROPERTIES_DESCRIPTION_0 = "JSON object with event details"

## Overview

The OneSignal + PostgreSQL integration enables syncing of custom events from your PostgreSQL database to OneSignal to trigger automated messaging campaigns and Journeys based on user behavior.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### PostgreSQL

* **PostgreSQL 9.6+** or compatible database
* **Database user** with appropriate permissions
* **Network access** from OneSignal to your PostgreSQL instance
* **Event tables** containing structured behavioral data

<Warning>
  We **strongly recommend against** connecting OneSignal to a production PostgreSQL database. Event sync queries are analytical in nature and may impact production performance. Use with databases set up for analytic workloads only.
</Warning>

***

## Setup

<Steps>
  <Step title="Create dedicated user for OneSignal">
    Create a dedicated user account with appropriate permissions:

    ```sql  theme={null}
    -- Create OneSignal user with strong password
    CREATE USER CENSUS WITH PASSWORD '<strong-unique-password>';

    -- Create private bookkeeping schema for sync state (skip if read-only mode)
    CREATE SCHEMA CENSUS;

    -- Grant full access to bookkeeping schema (skip if read-only mode)
    GRANT ALL ON SCHEMA CENSUS TO CENSUS;

    -- Ensure access to existing objects in bookkeeping schema (skip if read-only mode)
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA CENSUS TO CENSUS;
    ```
  </Step>

  <Step title="Grant permissions to event data">
    Provide read access to schemas containing your event data:

    ```sql  theme={null}
    -- Grant schema access (repeat for each schema with event data)
    GRANT USAGE ON SCHEMA "<your_schema>" TO CENSUS;

    -- Grant read access to existing tables
    GRANT SELECT ON ALL TABLES IN SCHEMA "<your_schema>" TO CENSUS;

    -- Grant read access to future tables
    ALTER DEFAULT PRIVILEGES IN SCHEMA "<your_schema>" GRANT SELECT ON TABLES TO CENSUS;

    -- Grant execute permissions on functions
    GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA "<your_schema>" TO CENSUS;
    ALTER DEFAULT PRIVILEGES IN SCHEMA "<your_schema>" GRANT EXECUTE ON FUNCTIONS TO CENSUS;
    ```
  </Step>

  <Step title="Connect to OneSignal">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    1. Select **PostgreSQL** from the list
    2. Enter your connection details:
       * **Host:** Your PostgreSQL server hostname
       * **Port:** Usually 5432
       * **Database:** Your database name
       * **Username:** `CENSUS`
       * **Password:** The password you created
    3. Test the connection
    4. Configure which tables contain your event data
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
-- Example PostgreSQL event table
CREATE TABLE analytics.user_events (
    event_id SERIAL PRIMARY KEY,
    event_name VARCHAR(100) NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    event_timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    event_data JSONB,
    session_id VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### SQL Query Mode

Write custom SQL queries to transform your event data:

```sql  theme={null}
-- Example: Recent purchase events
SELECT
    event_name,
    user_id,
    event_timestamp,
    event_data
FROM analytics.user_events
WHERE event_timestamp >= NOW() - INTERVAL '7 days'
    AND event_name = 'purchase'
ORDER BY event_timestamp DESC;
```

***

## Advanced Network Configuration

OneSignal can connect to PostgreSQL instances using advanced networking controls:

* **IP Allow Lists**: Add OneSignal's IP addresses to your firewall and `pg_hba.conf`
* **SSH Tunneling**: Connect through a bastion host for private networks
* **VPC Configuration**: Direct connection within cloud environments
* **TLS Encryption**: Secure connections using SSL/TLS

### SSH Tunnel Setup

For PostgreSQL instances on private networks:

1. **Create SSH user**: Set up a dedicated user on your SSH host
2. **Configure tunnel**: Enable "Use SSH Tunnel" in OneSignal integration settings
3. **Install keypair**: Add OneSignal's public key to `~/.ssh/authorized_keys`
4. **Test connection**: Verify tunnel connectivity

***

## Notes

* **Multiple Schemas**: Repeat permission grants for each schema containing event data
* **Views with Cross-Schema References**: May require additional read permissions in older PostgreSQL versions
* **Azure PostgreSQL**: Use `username@hostname` format for Azure instances
* **AWS RDS**: Use standard `username` format
* **Performance**: Consider using read replicas for large-scale event processing

***

## Limitations

* Avoid connecting to production databases due to analytical query overhead
* Complex cross-schema queries may require additional permissions
* Connection pooling recommended for high-frequency event processing

***

## FAQ

### Should I use read-only mode?

Use **read-only mode** if you prefer simpler setup and can't allow OneSignal to create tables. Use **full mode** for better performance with large event datasets.

### How do I handle multiple event schemas?

Repeat the permission grant commands for each schema containing event data. OneSignal can read from multiple schemas within a single connection.

Built with [Mintlify](https://mintlify.com).
