# Source: https://documentation.onesignal.com/docs/en/singlestore.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SingleStore

> Sync custom events from SingleStore to OneSignal to trigger automated Journeys and personalized messaging campaigns based on user behavior.

export const PLATFORM_0 = "SingleStore"

export const DATA_TYPE_0 = "event data"

export const COLUMN_HEADER_0 = "SingleStore Column"

export const PROPERTIES_DESCRIPTION_0 = "Event metadata as JSON"

## Overview

The OneSignal + SingleStore integration enables syncing of custom events from your SingleStore database to OneSignal to trigger automated messaging campaigns and Journeys based on user behavior.

SingleStore is a distributed SQL database designed for real-time analytics and high-performance applications.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### SingleStore

* **SingleStoreDB Cloud** or **SingleStoreDB v7.1+**
* **Database user** with appropriate permissions
* **Event tables** containing structured behavioral data
* **Network connectivity** from OneSignal to your SingleStore cluster

***

## Setup

<Steps>
  <Step title="Create dedicated user for OneSignal">
    Create a dedicated user account with a strong, unique password:

    ```sql  theme={null}
    -- Create census user with the ability to sign in with a password
    CREATE USER CENSUS IDENTIFIED BY '<strong-unique-password>';
    ```
  </Step>

  <Step title="Grant permissions to event data">
    Provide read-only access to schemas containing your event data:

    ```sql  theme={null}
    -- Grant read-only access to schema with event data
    GRANT SELECT ON analytics.* TO CENSUS;

    -- Repeat for additional schemas if needed
    GRANT SELECT ON events.* TO CENSUS;
    ```

    <Info>
      If you have multiple schemas containing event data, repeat the `GRANT SELECT` statement for each schema.
    </Info>
  </Step>

  <Step title="Connect to OneSignal">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    Select **SingleStore** and provide the following connection details:

    * **Host:** Your SingleStore cluster endpoint
    * **Port:** 3306 (default)
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
-- Example SingleStore event table
CREATE TABLE analytics.user_events (
    event_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(100) NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    event_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    event_data JSON,
    session_id VARCHAR(255),
    device_type VARCHAR(50)
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
WHERE event_timestamp >= DATE_SUB(NOW(), INTERVAL 7 DAY)
    AND JSON_EXTRACT_STRING(event_data, 'value') > '100'
ORDER BY event_timestamp DESC;
```

***

## Advanced Network Configuration

OneSignal can successfully connect to SingleStore instances that are using advanced networking controls including region constraints and IP address allow lists.

For more information about configuring network access, contact your SingleStore administrator or OneSignal support.

***

## Limitations

* Real-time analytics queries may impact cluster performance during high-traffic periods
* JSON operations should be optimized for distributed execution

***

## FAQ

### Can I connect to multiple SingleStore schemas?

Yes, you can grant the CENSUS user access to multiple schemas by running the `GRANT SELECT` statement for each schema containing event data.

### Does OneSignal support SingleStore Cloud?

Yes, OneSignal supports both SingleStoreDB Cloud and on-premises SingleStoreDB v7.1+ installations.

Built with [Mintlify](https://mintlify.com).
