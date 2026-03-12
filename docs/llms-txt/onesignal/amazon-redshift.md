# Source: https://documentation.onesignal.com/docs/en/amazon-redshift.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Amazon Redshift

> Sync custom events from Amazon Redshift to OneSignal to trigger automated Journeys and personalized messaging campaigns based on user behavior.

export const PLATFORM_0 = "Amazon Redshift"

export const DATA_TYPE_0 = "columns"

export const COLUMN_HEADER_0 = "Redshift Column"

export const PROPERTIES_DESCRIPTION_0 = "JSON object with event details"

## Overview

The OneSignal + Amazon Redshift integration enables syncing of custom events from your Redshift data warehouse to OneSignal to trigger automated messaging campaigns and Journeys based on user behavior.

Amazon Redshift is a fully managed, petabyte-scale data warehouse service that makes it cost-effective to analyze large volumes of data using your existing business intelligence tools.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### Amazon Redshift

* **Redshift cluster** with network access
* **Database user** with appropriate permissions
* **Event tables** containing structured behavioral data
* **Network connectivity** from OneSignal to your Redshift cluster

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

  <Step title="Configure network access">
    Add OneSignal's IP addresses to your Redshift security groups. Redshift prevents external access by default.

    You can find OneSignal's IP addresses for your region in the integration settings. For more information, visit the AWS Redshift Help Center.
  </Step>

  <Step title="Connect to OneSignal">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    1. Select **Amazon Redshift** from the list
    2. Enter your connection details:
       * **Host:** Your Redshift cluster endpoint
       * **Port:** Usually 5439
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
-- Example Redshift event table
CREATE TABLE analytics.user_events (
    event_id BIGINT IDENTITY(1,1),
    event_name VARCHAR(100) NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    event_timestamp TIMESTAMP DEFAULT GETDATE(),
    event_data SUPER,
    session_id VARCHAR(255),
    created_at TIMESTAMP DEFAULT GETDATE()
)
DISTKEY(user_id)
SORTKEY(event_timestamp);
```

### SQL Query Mode

Write custom SQL queries to transform your event data:

```sql  theme={null}
-- Example: Recent high-value events
SELECT
    event_name,
    user_id,
    event_timestamp,
    event_data
FROM analytics.user_events
WHERE event_timestamp >= DATEADD(day, -7, GETDATE())
    AND JSON_EXTRACT_PATH_TEXT(event_data, 'value')::NUMERIC > 100
ORDER BY event_timestamp DESC;
```

***

## dbt Integration

If you're using dbt with Redshift, ensure OneSignal retains access after each dbt run:

### Option 1: Fine-grained Permissions

Add post-hooks in your dbt project to grant access after each model builds:

```sql  theme={null}
-- In your dbt model
{{ config(
    post_hook="GRANT SELECT ON {{ this }} TO CENSUS"
) }}
```

### Option 2: Default Privileges (Recommended)

Grant default permissions for your dbt production user:

```sql  theme={null}
-- Must be run by Redshift superuser
ALTER DEFAULT PRIVILEGES FOR USER "<your_dbt_run_user>"
IN SCHEMA "<your_dbt_target_schema>"
GRANT SELECT ON TABLES TO CENSUS;
```

***

## Advanced Network Configuration

### SSH Tunnel Setup

For Redshift clusters on private networks:

1. **Create SSH user**: Set up a dedicated user on your SSH host
2. **Configure tunnel**: Enable "Use SSH Tunnel" in OneSignal integration settings
3. **Install keypair**: Add OneSignal's public key to `~/.ssh/authorized_keys`
4. **Test connection**: Verify tunnel connectivity

### VPC Deployment

For Redshift within AWS VPC:

OneSignal uses the `UNLOAD` command for efficient bulk data extraction. VPC deployments require an **S3 VPC Endpoint** to allow Redshift to communicate with S3.

**Setup S3 VPC Endpoint:**

1. Navigate to VPC service in AWS Console
2. Create VPC Endpoint for S3 service
3. Associate with your Redshift subnet
4. Configure routing tables

***

## Performance Optimization

### Distribution and Sort Keys

Optimize your event tables for analytics workloads:

```sql  theme={null}
-- Distribute by user_id for user-centric queries
CREATE TABLE analytics.user_events (
    -- columns
)
DISTKEY(user_id)
SORTKEY(event_timestamp, event_name);
```

### Columnar Storage

Take advantage of Redshift's columnar storage for analytics:

* **Compression**: Redshift automatically compresses columns
* **Zone Maps**: Improve query performance with sorted data
* **Column-oriented**: Efficient for analytical queries on event data

***

## Limitations

* Multiple schemas require separate permission grants
* Views referencing cross-schema tables need additional permissions
* Complex stored procedure access may require additional setup
* VPC deployments require S3 VPC Endpoint configuration

***

## FAQ

### How does OneSignal handle large event datasets?

OneSignal uses Redshift's `UNLOAD` command for efficient bulk data extraction, which is optimized for large-scale analytics workloads.

### Can I use read-only mode?

Yes, you can skip the bookkeeping schema creation and use read-only mode if you prefer simpler setup and can't allow OneSignal to create tables.

### What about dbt compatibility?

OneSignal provides specific dbt integration patterns to ensure permissions are maintained after dbt runs. Use post-hooks or default privileges depending on your setup.

Built with [Mintlify](https://mintlify.com).
