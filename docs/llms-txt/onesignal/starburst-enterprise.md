# Source: https://documentation.onesignal.com/docs/en/starburst-enterprise.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Starburst Enterprise

> Sync custom events from Starburst Enterprise to OneSignal to trigger automated Journeys and personalized messaging campaigns based on user behavior.

export const PLATFORM_0 = "Starburst Enterprise"

export const DATA_TYPE_0 = "event data"

export const COLUMN_HEADER_0 = "Starburst Column"

export const PROPERTIES_DESCRIPTION_0 = "Event metadata as JSON"

## Overview

The OneSignal + Starburst Enterprise integration enables syncing of custom events from your Starburst Enterprise cluster to OneSignal to trigger automated messaging campaigns and Journeys based on user behavior.

Starburst Enterprise is a commercial distribution of Trino designed for enterprise analytics and data lake querying across multiple sources.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### Starburst Enterprise

* **Starburst Enterprise cluster** with network access
* **User credentials** with appropriate permissions
* **TLS connection** support (required by OneSignal)
* **Event data** accessible through Starburst catalogs

***

## Setup

<Steps>
  <Step title="Get JDBC connection details">
    Follow Starburst's documentation to get your JDBC URL for your desired cluster.

    **Example JDBC URL:**

    ```
    jdbc:trino://census-example-cluster.trino.galaxy.starburst.io:[email protected]/accountadmin
    ```

    **Extract hostname for OneSignal:**

    ```
    census-example-cluster.trino.galaxy.starburst.io
    ```

    <Info>
      OneSignal uses JDBC to connect to Starburst Enterprise. You only need the hostname portion of the JDBC URL.
    </Info>
  </Step>

  <Step title="Configure Starburst Enterprise connection">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    Select **Starburst Enterprise** and provide the following connection details:

    * **Host:** Your Starburst cluster hostname (from Step 1)
    * **Username:** Your Starburst username
    * **Password:** Your Starburst password
    * **Port:** 443 (default) or your custom port
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
      Tested configurations include MySQL, PostgreSQL, Snowflake, Iceberg, and Starburst Delta Lake connectors.
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

### Enterprise Data Lake Queries

```sql  theme={null}
-- Example: Federated query across enterprise data sources
SELECT
    'enterprise_activity' as event_name,
    u.user_id,
    current_timestamp as event_timestamp,
    JSON_FORMAT(JSON_OBJECT(
        'crm_interactions', c.interaction_count,
        'warehouse_orders', w.order_count,
        'lake_analytics', l.score_value
    )) as event_properties
FROM salesforce_catalog.users.accounts u
LEFT JOIN crm_catalog.interactions.summary c ON u.user_id = c.user_id
LEFT JOIN warehouse_catalog.orders.summary w ON u.user_id = w.user_id
LEFT JOIN datalake_catalog.analytics.scores l ON u.user_id = l.user_id
WHERE u.created_date >= current_date - INTERVAL '30' DAY;
```

***

## Sync Engine Options

### Basic Sync Engine

* Works with any Starburst catalog and connector
* State tracking managed by OneSignal infrastructure
* Simpler setup with no additional requirements

### Advanced Sync Engine

* Enhanced performance with local state tracking
* Requires dedicated `CENSUS.CENSUS` catalog and schema
* Supports connectors with table write operations
* Recommended for high-volume enterprise event processing

***

## Supported Connectors

OneSignal's Advanced Sync Engine has been tested with:

* **MySQL connector** (read-write mode)
* **PostgreSQL connector** (read-write mode)
* **Snowflake connector** (read-write mode)
* **Iceberg connector** (with S3 and AWS Glue)
* **Starburst Delta Lake connector** (with AWS Glue catalogs)

***

## Enterprise Features

### Multi-Source Federation

* Query across enterprise data sources in a single sync
* Combine CRM, warehouse, and data lake event data
* Unified customer event profiles from disparate systems

### Security & Compliance

* Enterprise-grade authentication and authorization
* Row-level security and column masking support
* Audit logging for data access tracking

***

## Limitations

* TLS connection required (OneSignal security requirement)
* Advanced Sync Engine requires `CREATE OR REPLACE TABLE` support
* Warehouse Writeback not yet supported (coming soon)
* Cannot provide custom table options in `WITH` clause

***

## FAQ

### How do I get my Starburst Enterprise hostname?

Follow Starburst's documentation to get your JDBC URL, then extract just the hostname portion (without `jdbc:trino://` prefix) for use in OneSignal.

### Can I query multiple enterprise data sources?

Yes! Starburst Enterprise's federated query capabilities allow you to combine event data from multiple enterprise sources (Salesforce, SAP, Oracle, etc.) in a single query.

### Which Starburst release supports the Advanced Sync Engine?

Check your Starburst Enterprise release notes for `CREATE OR REPLACE TABLE` support, which is required for Advanced Sync Engine functionality.

Built with [Mintlify](https://mintlify.com).
