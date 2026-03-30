# Source: https://documentation.onesignal.com/docs/en/mysql.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# MySQL

> Sync custom events from MySQL to OneSignal to trigger automated Journeys and personalized messaging campaigns based on user behavior.

export const PLATFORM_0 = "MySQL"

export const DATA_TYPE_0 = "event data"

export const COLUMN_HEADER_0 = "MySQL Column"

export const PROPERTIES_DESCRIPTION_0 = "Event properties as JSON"

## Overview

The OneSignal + MySQL integration enables syncing of custom events from your MySQL database to OneSignal to trigger automated messaging campaigns and Journeys based on user behavior.

MySQL is a widely-used open-source relational database management system, ideal for storing structured event data that can power personalized messaging campaigns.

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### MySQL

* **MySQL Community 5.7** or later, or recent versions of **MariaDB**
* **Event tables** containing structured behavioral data
* **Network connectivity** from OneSignal to your MySQL instance
* **TLS v1.2** or greater supported

***

## Setup

<Steps>
  <Step title="Create dedicated user for OneSignal">
    Create a dedicated user account with read-only permissions:

    ```sql  theme={null}
    -- Create census user with ability to sign in with a password
    CREATE USER CENSUS IDENTIFIED BY '<strong, unique password>';

    -- Grant read-only access to your event schema
    GRANT SELECT ON <your_schema>.* TO CENSUS;
    ```

    <Info>
      If you have multiple schemas that contain event data, repeat the `GRANT SELECT` statement for each schema.
    </Info>
  </Step>

  <Step title="Configure OneSignal connection">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    Select **MySQL** and provide your connection details:

    * **Host:** Your MySQL server hostname
    * **Port:** MySQL port (typically 3306)
    * **Database:** Database name containing your event tables
    * **Username:** `CENSUS`
    * **Password:** The password you created above
  </Step>

  <Step title="Test connection">
    Click **Test Connection** to verify OneSignal can successfully connect to your MySQL database and access your event tables.
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
CREATE TABLE user_events (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(100) NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    event_data JSON,
    session_id VARCHAR(255),
    device_type VARCHAR(50)
);
```

### Table Mode

Select your event table directly and OneSignal will sync all rows as individual events.

### SQL Query Mode

Write custom SQL queries to transform your event data:

```sql  theme={null}
-- Example: Recent high-value events
SELECT
    event_name,
    user_id,
    created_at as timestamp,
    event_data as payload
FROM user_events
WHERE created_at >= DATE_SUB(NOW(), INTERVAL 7 DAY)
    AND JSON_EXTRACT(event_data, '$.value') > 100
ORDER BY created_at DESC;
```

***

## Advanced Network Configuration

OneSignal can successfully connect to MySQL instances using advanced networking controls including region constraints, IP address allow lists, or SSH Tunneling.

OneSignal supports MySQL with TLS versions 1.2 and greater for secure connections.

***

## FAQ

### Which MySQL versions are supported?

OneSignal supports MySQL Community 5.7 or later, as well as recent versions of MariaDB.

### Can I connect to MySQL in a private network?

Yes, OneSignal supports SSH tunneling and IP allow lists for connecting to MySQL instances in private networks or behind firewalls.

***

Built with [Mintlify](https://mintlify.com).
