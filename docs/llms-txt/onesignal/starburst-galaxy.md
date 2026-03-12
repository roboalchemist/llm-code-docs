# Source: https://documentation.onesignal.com/docs/en/starburst-galaxy.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Starburst Galaxy

> Sync custom events from Starburst Galaxy to OneSignal to trigger automated Journeys and personalized messaging campaigns based on user behavior.

export const PLATFORM_0 = "Starburst Galaxy"

export const DATA_TYPE_0 = "event data"

export const COLUMN_HEADER_0 = "Galaxy Column"

export const PROPERTIES_DESCRIPTION_0 = "Event metadata as JSON"

## Overview

The OneSignal + Starburst Galaxy integration enables syncing of custom events from your Starburst Galaxy cluster to OneSignal to trigger automated messaging campaigns and Journeys based on user behavior.

Starburst Galaxy is a fully managed cloud analytics platform based on Trino, designed for fast SQL queries across cloud data lakes and warehouses.

***

## Requirements

* Access to [Event Streams](/docs/en/event-streams) for outbound message events (Plan limitations and overages apply)
* Access to [Custom Events](/docs/en/custom-events) for inbound event syncing (Plan limitations and overages apply)
* [Updated Account Plan](https://onesignal.com/pricing) (not available on free apps)

### Starburst Galaxy

* **Starburst Galaxy cluster** with network access
* **User credentials** with appropriate permissions
* **TLS connection** support (built-in for Galaxy)
* **Event data** accessible through Galaxy catalogs

***

## Setup

<Steps>
  <Step title="Get Galaxy JDBC connection details">
    In your Starburst Galaxy console, navigate to your cluster's connection details.

    **Example JDBC URL:**

    ```
    jdbc:trino://census-example-cluster.trino.galaxy.starburst.io:[email protected]/accountadmin
    ```

    **Extract hostname for OneSignal:**

    ```
    census-example-cluster.trino.galaxy.starburst.io
    ```

    <Info>
      OneSignal uses JDBC to connect to Starburst Galaxy. You only need the hostname portion from Galaxy's JDBC URL.
    </Info>
  </Step>

  <Step title="Configure Starburst Galaxy connection">
    In OneSignal, go to **Data > Integrations** and click **Add Integration**.

    Select **Starburst Galaxy** and provide the following connection details:

    * **Host:** Your Galaxy cluster hostname (from Step 1)
    * **Username:** Your Galaxy username
    * **Password:** Your Galaxy password
    * **Port:** 443 (default for Galaxy)
  </Step>

  <Step title="Configure Advanced Sync Engine (Optional)">
    For enhanced performance, set up a dedicated CENSUS catalog in Galaxy:

    1. Create a catalog named `CENSUS` containing a schema named `CENSUS`
    2. Ensure your connector supports:
       * `CREATE TABLE` and `DROP TABLE` operations
       * Table writes (INSERT, DELETE, UPDATE)
       * `CREATE OR REPLACE TABLE` statement
    3. Grant full permissions on the `CENSUS.CENSUS` schema to your OneSignal user

    <Info>
      Tested configurations include MySQL, PostgreSQL, Snowflake, Iceberg, and Starburst Galaxy catalogs.
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
-- Example: Recent high-value events across Galaxy catalogs
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

### Cloud Data Lake Queries

```sql  theme={null}
-- Example: Federated query across cloud data sources
SELECT
    'cloud_activity' as event_name,
    u.user_id,
    current_timestamp as event_timestamp,
    JSON_FORMAT(JSON_OBJECT(
        's3_interactions', s.interaction_count,
        'snowflake_orders', sf.order_count,
        'bigquery_analytics', bq.score_value
    )) as event_properties
FROM s3_catalog.users.profiles u
LEFT JOIN s3_catalog.interactions.summary s ON u.user_id = s.user_id
LEFT JOIN snowflake_catalog.orders.summary sf ON u.user_id = sf.user_id
LEFT JOIN bigquery_catalog.analytics.scores bq ON u.user_id = bq.user_id
WHERE u.created_date >= current_date - INTERVAL '30' DAY;
```

***

## Sync Engine Options

### Basic Sync Engine

* Works with any Galaxy catalog and connector
* State tracking managed by OneSignal infrastructure
* Simpler setup with no additional requirements

### Advanced Sync Engine

* Enhanced performance with local state tracking
* Requires dedicated `CENSUS.CENSUS` catalog and schema
* Supports connectors with table write operations
* Recommended for high-volume cloud event processing

***

## Supported Connectors

OneSignal's Advanced Sync Engine has been tested with:

* **MySQL connector** (read-write mode)
* **PostgreSQL connector** (read-write mode)
* **Snowflake connector** (read-write mode)
* **Iceberg connector** (with S3 and AWS Glue)
* **Starburst Galaxy catalog** (native Galaxy storage)

***

## Cloud Platform Features

### Multi-Cloud Federation

* Query across AWS, Azure, and GCP data sources
* Combine S3, Snowflake, BigQuery, and Azure data
* Unified event analytics across cloud providers

### Managed Infrastructure

* Fully managed Trino clusters with auto-scaling
* Built-in security and compliance features
* No infrastructure management required

### Galaxy-Native Catalogs

* High-performance native Galaxy storage
* Seamless integration with Galaxy ecosystem
* Optimized for cloud analytics workloads

***

## Limitations

* TLS connection required (built-in for Galaxy)
* Advanced Sync Engine requires `CREATE OR REPLACE TABLE` support
* Warehouse Writeback not yet supported (coming soon)
* Cannot provide custom table options in `WITH` clause

***

## FAQ

### How do I get my Galaxy cluster hostname?

In your Starburst Galaxy console, go to your cluster's connection details and copy the JDBC URL. Extract just the hostname portion (without `jdbc:trino://` prefix) for use in OneSignal.

### Can I query multiple cloud data sources?

Yes! Starburst Galaxy's federated query capabilities allow you to combine event data from multiple cloud sources (S3, Snowflake, BigQuery, etc.) in a single query.

### Does Galaxy support auto-scaling for OneSignal workloads?

Yes, Starburst Galaxy automatically scales clusters based on query load, ensuring optimal performance for your OneSignal event processing without manual intervention.

Built with [Mintlify](https://mintlify.com).
