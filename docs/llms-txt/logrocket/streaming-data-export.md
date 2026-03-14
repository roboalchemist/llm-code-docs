# Source: https://docs.logrocket.com/docs/streaming-data-export.md

# Streaming Data Export

Stream LogRocket data directly to your data warehouse

Streaming Data Export is purchasable as an add-on on top of your base contract.  Contact LogRocket Support if you are interested in learning more.

## What is Streaming Data Export?

LogRocket automatically exports session data to your cloud data warehouse (Snowflake, BigQuery, etc), allowing you to seamlessly integrate LogRocket data with other data sources across the business. This empowers analysts to quickly summarize and explore the LogRocket data, and its impact on overall business health, without the need for complex ETL pipelines or constant engineering support.

Streaming data export is simple to configure and offers a wide range of cloud data warehouse options. A single destination can be configured for each LogRocket organization.

Destination options include:

* Snowflake
* BigQuery
* Databricks
* RedShift
* Google Cloud Storage
* S3
* Postgres
* MySQL
* Athena
* Google Sheets

## What data is exported?

Once the export is enabled, a `logrocket_events` table will be created in your data warehouse with the schema described in our [Streaming Data Export Schema doc](https://docs.logrocket.com/docs/logrocket-events-table-schema). The data is exported once every hour and may include events related to sessions that have not yet ended. There is no limit on the amount of data that can be exported each hour.

The data exported is as follows:

* Session metadata, including browser version, device type, and location data when a session is started
* User information from [`LogRocket.identify()`](https://docs.logrocket.com/reference/identify) calls, including auto-generated identifiers for anonymous sessions
* Page navigation events
* Click events
* Mobile touch events
* Input events
* Custom events from [`LogRocket.track()`](https://docs.logrocket.com/reference/track) calls, including any properties
* JS errors
* Network response events, including URL, method, status, and duration (bodies aren't included)
* Redux action types (payloads aren't included)

## Setup

See the [Setup](https://docs.logrocket.com/docs/streaming-data-export-setup) docs to get started with Streaming Data Export.

## Usage

Data will be exported once the integration is enabled and appropriate destination is configured. The export is non-retroactive, so you will only see session data that occurred after all the proper configuration has been completed.