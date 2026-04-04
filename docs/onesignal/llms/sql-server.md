# Source: https://documentation.onesignal.com/docs/en/sql-server.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SQL Server

> Sync custom events from Microsoft SQL Server to OneSignal to trigger automated Journeys and personalized messaging campaigns based on user behavior.

export const PLATFORM_0 = "SQL Server"

export const DATA_TYPE_0 = "event data"

export const COLUMN_HEADER_0 = "SQL Server Column"

export const PROPERTIES_DESCRIPTION_0 = "Event metadata as JSON string"

## Overview

The OneSignal + SQL Server integration enables syncing of custom events from your Microsoft SQL Server database to OneSignal to trigger automated messaging campaigns and Journeys based on user behavior.

SQL Server is Microsoft's relational database management system designed for enterprise applications and data warehousing.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### SQL Server

* **SQL Server instance** with network access
* **Database user** with appropriate permissions
* **Event tables** containing structured behavioral data
* **Network connectivity** from OneSignal to your SQL Server instance

***

## Setup

<Steps>
  <Step title="Create dedicated user for OneSignal">
    Create a dedicated user account with a strong, unique password:

    ```sql  theme={null}
    -- Create census user with the ability to sign in with a password
    CREATE USER CENSUS WITH PASSWORD = '<strong-unique-password>';

    -- Give the census user the ability to connect to database
    GRANT CONNECT TO CENSUS;
    ```

    <Info>
      All SQL Server commands will run within the database that is specified when running the script.
    </Info>
  </Step>

  <Step title="Grant read permissions">
    Provide read-only access to your event data:

    ```sql  theme={null}
    -- Give the census user the ability to read tables within the database
    EXEC sp_addrolemember 'db_datareader', CENSUS;

    -- Grant census user ability to read data from within a schema
    -- Run this for each schema you intend OneSignal to access
    GRANT SELECT, VIEW DEFINITION ON SCHEMA::<your-schema> TO CENSUS;
    ```

    <Info>
      Replace `<your-schema>` with your actual schema name containing event data. Repeat this command for each schema you want OneSignal to access.
    </Info>
  </Step>

  <Step title="Configure Advanced Sync Engine (Optional)">
    For enhanced performance, create a bookkeeping schema for OneSignal's sync state:

    ```sql  theme={null}
    -- Create a private bookkeeping schema where Census can store sync state
    CREATE SCHEMA CENSUS AUTHORIZATION CENSUS;

    -- Give the census user full access to the bookkeeping schema
    GRANT ALTER, DELETE, EXECUTE, INSERT, REFERENCES, SELECT,
              UPDATE, VIEW DEFINITION ON SCHEMA::CENSUS TO CENSUS;

    -- Give the census user the ability to create tables within the database
    GRANT CREATE TABLE TO CENSUS;
    ```

    <Warning>
      Skip this step if using Basic Sync Engine or read-only mode.
    </Warning>
  </Step>

  <Step title="Connect to OneSignal">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    Select **SQL Server** and provide the following connection details:

    * **Host:** Your SQL Server instance hostname or IP address
    * **Port:** 1433 (default) or your custom port
    * **Database:** Your database name
    * **Username:** `CENSUS`
    * **Password:** The password from Step 1
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
-- Example SQL Server event table
CREATE TABLE analytics.user_events (
    event_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    event_name NVARCHAR(100) NOT NULL,
    user_id NVARCHAR(255) NOT NULL,
    event_timestamp DATETIME2 DEFAULT GETUTCDATE(),
    event_data NVARCHAR(MAX),
    session_id NVARCHAR(255),
    device_type NVARCHAR(50)
);
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
WHERE event_timestamp >= DATEADD(day, -7, GETUTCDATE())
    AND JSON_VALUE(event_data, '$.value') > 100
ORDER BY event_timestamp DESC;
```

***

## Advanced Network Configuration

OneSignal can successfully connect to SQL Server instances that are using advanced networking controls including region constraints, IP address allow lists, or SSH Tunneling.

For more information about configuring network access, contact your SQL Server administrator or OneSignal support.

***

## Sync Engine Options

### Basic Sync Engine

* Read-only access to your event data
* State tracking managed by OneSignal infrastructure
* Simpler setup with minimal permissions

### Advanced Sync Engine

* Enhanced performance with local state tracking
* Requires additional permissions to create tables
* Recommended for high-volume event processing

***

## Limitations

* Complex queries may impact database performance during high-traffic periods
* JSON operations require SQL Server 2016 or later for optimal performance
* All permissions are granted at the database level specified during setup

***

## FAQ

### Can I connect to multiple SQL Server schemas?

Yes, you can grant the CENSUS user access to multiple schemas by running the `GRANT SELECT, VIEW DEFINITION ON SCHEMA::<schema>` statement for each schema containing event data.

### Which SQL Server versions are supported?

OneSignal supports modern SQL Server versions. For JSON operations in event queries, SQL Server 2016 or later is recommended.

### Do I need to use the Advanced Sync Engine?

No, the Basic Sync Engine works well for most use cases. Use Advanced Sync Engine if you need enhanced performance and can allow OneSignal to create tables in your SQL Server instance.

Built with [Mintlify](https://mintlify.com).
