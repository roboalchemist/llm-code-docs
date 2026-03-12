# Source: https://documentation.onesignal.com/docs/en/azure-synapse.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure Synapse

> Sync custom events from Azure Synapse to OneSignal to trigger automated Journeys and personalized messaging campaigns based on user behavior.

export const PLATFORM_0 = "Azure Synapse"

export const DATA_TYPE_0 = "event data"

export const COLUMN_HEADER_0 = "Synapse Column"

export const PROPERTIES_DESCRIPTION_0 = "Event metadata as JSON string"

## Overview

The OneSignal + Azure Synapse integration enables syncing of custom events from your Azure Synapse Analytics workspace to OneSignal to trigger automated messaging campaigns and Journeys based on user behavior.

Azure Synapse Analytics is Microsoft's cloud-based analytics service that combines data integration, data warehousing, and analytics.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### Azure Synapse

* **Azure Synapse workspace** with SQL pool access
* **Database user** with appropriate permissions
* **Event tables** containing structured behavioral data
* **Firewall access** for the IP addresses provided by OneSignal in the Integration setup

***

## Setup

<Steps>
  <Step title="Create dedicated login for OneSignal">
    Create a dedicated login and user account with a strong, unique password:

    ```sql  theme={null}
    USE <your-database>;

    -- Create census login with the ability to sign in with a password
    CREATE LOGIN CENSUS WITH PASSWORD = '<strong-unique-password>';

    -- Create user for the login
    CREATE USER CENSUS FOR LOGIN CENSUS;

    -- Give the census user the ability to connect to database
    GRANT CONNECT TO CENSUS;
    ```

    <Info>
      Replace `<your-database>` with your actual database name containing event data.
    </Info>
  </Step>

  <Step title="Grant read permissions">
    Provide read-only access to your event data:

    ```sql  theme={null}
    -- Give the census user the ability to read all tables
    EXEC sp_addrolemember 'db_datareader', CENSUS;

    -- Grant census user ability to read schema and data
    -- Run this for each schema you intend OneSignal to access
    GRANT SELECT, VIEW DEFINITION ON SCHEMA::<your-schema> TO CENSUS;
    ```

    <Info>
      Replace `<your-schema>` with your actual schema name containing event data. Repeat this command for each schema you want OneSignal to access.
    </Info>
  </Step>

  <Step title="Configure firewall access">
    Configure Azure Synapse firewall to allow the IP addresses provided by OneSignal in the Integration setup.

    Use the Windows Azure Management Portal or run **sp\_set\_firewall\_rule** on the primary database:

    ```sql  theme={null}
    -- Example: Add firewall rule for OneSignal IP range
    EXEC sp_set_firewall_rule
        N'OneSignal Access',
        'ONESIGNAL_IP_START',
        'ONESIGNAL_IP_END';
    ```

    <Warning>
      Contact OneSignal support for the current IP address ranges for your region.
    </Warning>
  </Step>

  <Step title="Connect to OneSignal">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    Select **Azure Synapse** and provide the following connection details:

    * **Host:** Your Synapse SQL endpoint hostname
    * **Port:** 1433 (default)
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
-- Example Azure Synapse event table
CREATE TABLE analytics.user_events (
    event_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    event_name NVARCHAR(100) NOT NULL,
    user_id NVARCHAR(255) NOT NULL,
    event_timestamp DATETIME2 DEFAULT GETUTCDATE(),
    event_data NVARCHAR(MAX),
    session_id NVARCHAR(255),
    device_type NVARCHAR(50)
)
WITH (DISTRIBUTION = HASH(user_id), CLUSTERED COLUMNSTORE INDEX);
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

## Azure-Specific Features

### Distributed Architecture

* Events distributed by `user_id` for optimal query performance
* Clustered columnstore indexes for analytics workloads
* Massively parallel processing (MPP) for large-scale event data

### Integration with Azure Ecosystem

* Connect to Azure Data Factory for automated event pipelines
* Integrate with Azure Event Hubs for real-time event streaming
* Leverage Azure Active Directory for authentication

***

## Advanced Network Configuration

OneSignal can successfully connect to Azure Synapse instances that are using advanced networking controls including region constraints, IP address allow lists, or SSH Tunneling.

For more information about configuring network access, contact your Azure Synapse administrator or OneSignal support.

***

## Limitations

* Based on SQL Server JDBC driver connection protocol
* Requires explicit firewall rules for the IP addresses provided by OneSignal in the Integration setup
* Complex queries may impact SQL pool performance and costs
* JSON operations require careful indexing for optimal performance

***

## FAQ

### Can I connect to multiple Azure Synapse schemas?

Yes, you can grant the CENSUS user access to multiple schemas by running the `GRANT SELECT, VIEW DEFINITION ON SCHEMA::<schema>` statement for each schema containing event data.

### How do I configure firewall access for OneSignal?

Use the Azure Management Portal or `sp_set_firewall_rule` to add OneSignal's IP addresses. Contact OneSignal support for the current IP ranges.

### What's the difference between Azure Synapse and SQL Server integration?

Azure Synapse uses the same SQL Server JDBC driver but includes distributed architecture features and requires specific firewall configuration for cloud access.

Built with [Mintlify](https://mintlify.com).
