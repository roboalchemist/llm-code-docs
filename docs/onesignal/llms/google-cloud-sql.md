# Source: https://documentation.onesignal.com/docs/en/google-cloud-sql.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Cloud SQL

> Sync custom events from Google Cloud SQL to OneSignal to trigger automated Journeys and personalized messaging campaigns based on user behavior.

export const PLATFORM_0 = "Google Cloud SQL"

export const DATA_TYPE_0 = "event table fields"

export const COLUMN_HEADER_0 = "Cloud SQL Field"

export const PROPERTIES_DESCRIPTION_0 = "Event metadata as JSON object"

## Overview

The OneSignal + Google Cloud SQL integration enables automatic syncing of custom events from your Cloud SQL database to OneSignal. This allows you to trigger automated Journeys and personalized messaging campaigns based on user behavioral data stored in your managed PostgreSQL database.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### Google Cloud SQL

* **Cloud SQL for PostgreSQL** instance (version 11 or higher recommended)
* **Database access** with read permissions for event tables
* **Network connectivity** from OneSignal to your Cloud SQL instance
* **Cloud SQL Auth proxy** for secure connections (recommended)

***

## Setup

<Steps>
  <Step title="Configure Cloud SQL database access">
    Create a dedicated user for OneSignal with read-only access to event tables:

    ```sql  theme={null}
    -- Create OneSignal user
    CREATE USER onesignal_reader WITH PASSWORD 'strong_unique_password';

    -- Grant schema access
    GRANT USAGE ON SCHEMA event_data TO onesignal_reader;

    -- Grant table access
    GRANT SELECT ON ALL TABLES IN SCHEMA event_data TO onesignal_reader;

    -- Grant access to future tables
    ALTER DEFAULT PRIVILEGES IN SCHEMA event_data
    GRANT SELECT ON TABLES TO onesignal_reader;
    ```
  </Step>

  <Step title="Configure network access">
    Ensure OneSignal can connect to your Cloud SQL instance:

    **Option 1: Authorized Networks (Public IP)**

    * In Google Cloud Console, go to **SQL > Instances**
    * Select your instance → **Connections** → **Networking**
    * Add the IP addresses provided by OneSignal in the Integration setup to **Authorized networks**

    **Option 2: Private IP (Recommended)**

    * Configure your Cloud SQL instance with a private IP
    * Use Cloud SQL Auth Proxy for secure connections
    * Ensure proper VPC peering or firewall rules

    **Option 3: Cloud SQL Auth Proxy**

    * Download and configure the Cloud SQL Auth Proxy
    * Use service account authentication
    * Connect through secure proxy tunnel
  </Step>

  <Step title="Set up Cloud SQL Auth Proxy (recommended)">
    For enhanced security, use Cloud SQL Auth Proxy:

    ```bash  theme={null}
    # Download Cloud SQL Auth Proxy
    curl -o cloud_sql_proxy https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64

    # Make executable
    chmod +x cloud_sql_proxy

    # Run proxy (replace with your instance connection name)
    ./cloud_sql_proxy -instances=PROJECT:REGION:INSTANCE=tcp:5432
    ```

    Create a service account with Cloud SQL Client role:

    ```bash  theme={null}
    gcloud iam service-accounts create onesignal-cloudsql
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="serviceAccount:onesignal-cloudsql@PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/cloudsql.client"
    ```
  </Step>

  <Step title="Add integration in OneSignal">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    Select **Google Cloud SQL** and provide:

    * **Instance Connection Name**: `PROJECT_ID:REGION:INSTANCE_ID`
    * **Database Name**: Your event database name
    * **Username**: `onesignal_reader`
    * **Password**: The password created in Step 1
    * **SSL Mode**: `require` (recommended for security)
    * **Connection Type**: Choose between Direct, Auth Proxy, or Private IP
  </Step>

  <Step title="Configure event data queries">
    Define the SQL query to retrieve event data from your Cloud SQL database:

    ```sql  theme={null}
    SELECT
        event_name,
        user_id,
        created_at as event_timestamp,
        properties as event_payload
    FROM event_data.user_events
    WHERE created_at >= CURRENT_TIMESTAMP - INTERVAL '1 hour'
    ORDER BY created_at DESC
    ```

    Ensure your event tables include:

    * Event name/type (String)
    * User identifier (String)
    * Event timestamp (Timestamp)
    * Event properties (JSON/JSONB)
  </Step>

  <Step title="Test the connection">
    Click **Test Connection** to verify OneSignal can connect to your Cloud SQL instance and execute the event query successfully.
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

### Connection Pooling

Optimize database connections for high-volume event syncing:

```sql  theme={null}
-- Check current connection limits
SELECT * FROM pg_stat_activity WHERE datname = 'your_database';

-- Optimize for OneSignal connections
ALTER SYSTEM SET max_connections = 200;
ALTER SYSTEM SET shared_preload_libraries = 'pg_stat_statements';
```

### Query Optimization

Improve event query performance:

```sql  theme={null}
-- Create index on timestamp for efficient filtering
CREATE INDEX idx_events_created_at ON user_events(created_at);

-- Create composite index for user-based queries
CREATE INDEX idx_events_user_time ON user_events(user_id, created_at);

-- Analyze query performance
EXPLAIN ANALYZE
SELECT event_name, user_id, created_at, properties
FROM user_events
WHERE created_at >= NOW() - INTERVAL '1 hour';
```

### JSON Data Handling

If using JSONB for event properties, optimize JSON queries:

```sql  theme={null}
-- Create GIN index for JSON properties
CREATE INDEX idx_events_properties ON user_events USING GIN(properties);

-- Query specific JSON properties
SELECT
    event_name,
    user_id,
    properties->>'purchase_amount' as amount,
    properties->>'product_id' as product
FROM user_events
WHERE properties->>'event_type' = 'purchase';
```

<Warning>
  Monitor your Cloud SQL instance's performance when OneSignal queries event data. Consider using read replicas for analytics workloads to avoid impacting production performance.
</Warning>

***

## FAQ

### How often does OneSignal sync events from Cloud SQL?

OneSignal syncs event data based on your configured schedule, with a minimum interval of 15 minutes.

### Can I use Cloud SQL read replicas for event syncing?

Yes, using read replicas is recommended to isolate analytics queries from your production database workload.

### What happens if my Cloud SQL instance is temporarily unavailable?

OneSignal will retry connections with exponential backoff. Event syncing will resume automatically once your instance is accessible again.

Built with [Mintlify](https://mintlify.com).
