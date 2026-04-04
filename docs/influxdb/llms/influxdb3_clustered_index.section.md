---
title: InfluxDB Clustered documentation
description: InfluxDB Clustered is a highly available InfluxDB 3 cluster hosted and managed on your own infrastructure. The InfluxDB time series platform is designed to handle high write and query loads. Learn how to use and leverage InfluxDB Clustered for your specific time series use case.
url: https://docs.influxdata.com/influxdb3/clustered/
product: InfluxDB Clustered
type: section
pages: 10
estimated_tokens: 9128
child_pages:
  - url: https://docs.influxdata.com/influxdb3/clustered/write-data/
    title: Write data to InfluxDB Clustered
  - url: https://docs.influxdata.com/influxdb3/clustered/tags/
    title: Related to "Tags"
  - url: https://docs.influxdata.com/influxdb3/clustered/reference/
    title: InfluxDB Clustered reference documentation
  - url: https://docs.influxdata.com/influxdb3/clustered/query-data/
    title: Query data in InfluxDB Clustered
  - url: https://docs.influxdata.com/influxdb3/clustered/process-data/
    title: Process and visualize data stored in InfluxDB
  - url: https://docs.influxdata.com/influxdb3/clustered/install/
    title: Install InfluxDB Clustered
  - url: https://docs.influxdata.com/influxdb3/clustered/guides/
    title: InfluxDB guides
  - url: https://docs.influxdata.com/influxdb3/clustered/get-started/
    title: Get started with InfluxDB Clustered
  - url: https://docs.influxdata.com/influxdb3/clustered/admin/
    title: Administer InfluxDB Clustered
---

# InfluxDB Clustered documentation

InfluxDB Clustered is a highly available InfluxDB 3 cluster hosted and managed on your own infrastructure. The InfluxDB time series platform is designed to handle high write and query loads. Learn how to use and leverage InfluxDB Clustered for your specific time series use case.

[Run an InfluxDB Clustered proof of concept (PoC)](https://www.influxdata.com/contact-sales-influxdb-clustered/)  
[Get started with InfluxDB Clustered](/influxdb3/clustered/get-started/)

## InfluxDB 3

**InfluxDB 3** is InfluxDB’s next generation that unlocks series limitations present in the Time Structured Merge Tree (TSM) storage engine and allows infinite series cardinality without any impact on overall database performance. It also brings with it native **SQL support** and improved InfluxQL performance.

View the following video for more information about InfluxDB 3:


---

## Write data to InfluxDB Clustered

Write data to InfluxDB Clustered using the following tools and methods:

#### Choose the write endpoint for your workload

When bringing existing v1 write workloads, use the InfluxDB Clustered HTTP API [`/write` endpoint](/influxdb3/clustered/guides/api-compatibility/v1/). When creating new write workloads, use the HTTP API [`/api/v2/write` endpoint](/influxdb3/clustered/guides/api-compatibility/v2/).

### [Use Telegraf to write data](/influxdb3/clustered/write-data/use-telegraf/)

Use Telegraf to collect and write data to InfluxDB. Create Telegraf configurations in the InfluxDB UI or manually configure Telegraf.

### [Write line protocol data to InfluxDB Clustered](/influxdb3/clustered/write-data/line-protocol/)

Use Telegraf and API clients to write line protocol data to InfluxDB Clustered.

### [Write CSV data to InfluxDB Clustered](/influxdb3/clustered/write-data/csv/)

Use Telegraf or the HTTP API to write CSV data to InfluxDB Clustered.

### [Best practices for writing data](/influxdb3/clustered/write-data/best-practices/)

Learn about the recommendations and best practices for writing data to InfluxDB Clustered.

### [Troubleshoot issues writing data](/influxdb3/clustered/write-data/troubleshoot/)

Troubleshoot issues writing data. Find response codes for failed writes. Discover how writes fail, from exceeding rate or payload limits, to syntax errors and schema conflicts.

[write](/influxdb3/clustered/tags/write/) [line protocol](/influxdb3/clustered/tags/line-protocol/)


---

## Related to "Tags"

### [AI](/influxdb3/clustered/tags/ai/)

### [Analysis](/influxdb3/clustered/tags/analysis/)

### [Api](/influxdb3/clustered/tags/api/)

### [Arrow](/influxdb3/clustered/tags/arrow/)

### [Backup](/influxdb3/clustered/tags/backup/)

### [Backups](/influxdb3/clustered/tags/backups/)

### [C#](/influxdb3/clustered/tags/c%23/)

### [Cli](/influxdb3/clustered/tags/cli/)

### [Client Libraries](/influxdb3/clustered/tags/client-libraries/)

### [Databases](/influxdb3/clustered/tags/databases/)

### [Developer Tools](/influxdb3/clustered/tags/developer-tools/)

### [Errors](/influxdb3/clustered/tags/errors/)

### [Flight](/influxdb3/clustered/tags/flight/)

### [Flight API](/influxdb3/clustered/tags/flight-api/)

### [Flight Client](/influxdb3/clustered/tags/flight-client/)

### [Flight RPC](/influxdb3/clustered/tags/flight-rpc/)

### [Flight SQL](/influxdb3/clustered/tags/flight-sql/)

### [Flightsql](/influxdb3/clustered/tags/flightsql/)

### [Get-Started](/influxdb3/clustered/tags/get-started/)

### [Glossary](/influxdb3/clustered/tags/glossary/)

### [Go](/influxdb3/clustered/tags/go/)

### [Grafana](/influxdb3/clustered/tags/grafana/)

### [GRPC](/influxdb3/clustered/tags/grpc/)

### [Influxctl](/influxdb3/clustered/tags/influxctl/)

### [InfluxQL](/influxdb3/clustered/tags/influxql/)

### [Internals](/influxdb3/clustered/tags/internals/)

### [Java](/influxdb3/clustered/tags/java/)

### [JavaScript](/influxdb3/clustered/tags/javascript/)

### [Kubernetes](/influxdb3/clustered/tags/kubernetes/)

### [Licensing](/influxdb3/clustered/tags/licensing/)

### [Line Protocol](/influxdb3/clustered/tags/line-protocol/)

### [LLM](/influxdb3/clustered/tags/llm/)

### [MCP](/influxdb3/clustered/tags/mcp/)

### [NodeJS](/influxdb3/clustered/tags/nodejs/)

### [Observability](/influxdb3/clustered/tags/observability/)

### [Pandas](/influxdb3/clustered/tags/pandas/)

### [Partial Writes](/influxdb3/clustered/tags/partial-writes/)

### [Performance](/influxdb3/clustered/tags/performance/)

### [Powerbi](/influxdb3/clustered/tags/powerbi/)

### [Pyarrow](/influxdb3/clustered/tags/pyarrow/)

### [Python](/influxdb3/clustered/tags/python/)

### [Query](/influxdb3/clustered/tags/query/)

### [Regular Expressions](/influxdb3/clustered/tags/regular-expressions/)

### [Restore](/influxdb3/clustered/tags/restore/)

### [Scale](/influxdb3/clustered/tags/scale/)

### [Schema](/influxdb3/clustered/tags/schema/)

### [Security](/influxdb3/clustered/tags/security/)

### [SQL](/influxdb3/clustered/tags/sql/)

### [Storage](/influxdb3/clustered/tags/storage/)

### [Superset](/influxdb3/clustered/tags/superset/)

### [Syntax](/influxdb3/clustered/tags/syntax/)

### [Tableau](/influxdb3/clustered/tags/tableau/)

### [Tables](/influxdb3/clustered/tags/tables/)

### [Telegraf](/influxdb3/clustered/tags/telegraf/)

### [Tokens](/influxdb3/clustered/tags/tokens/)

### [Tools](/influxdb3/clustered/tags/tools/)

### [Upgrade](/influxdb3/clustered/tags/upgrade/)

### [Visualization](/influxdb3/clustered/tags/visualization/)

### [Window Functions](/influxdb3/clustered/tags/window-functions/)

### [Write](/influxdb3/clustered/tags/write/)


---

## InfluxDB Clustered reference documentation

### [Release notes related to InfluxDB Clustered](/influxdb3/clustered/reference/release-notes/)

View release notes and updates for products and tools related to InfluxDB Clustered.

### [SQL reference documentation](/influxdb3/clustered/reference/sql/)

Learn the SQL syntax and structure used to query InfluxDB.

### [InfluxQL reference documentation](/influxdb3/clustered/reference/influxql/)

InfluxQL is an SQL-like query language for interacting with data in InfluxDB.

### [Naming restrictions and conventions](/influxdb3/clustered/reference/naming-restrictions/)

Learn about naming restrictions and conventions for databases, tables, tags, fields, and other identifiers in InfluxDB Clustered.

### [Command line tools](/influxdb3/clustered/reference/cli/)

InfluxDB provides command line tools designed to manage and work with your InfluxDB cluster from the command line.

### [API client libraries](/influxdb3/clustered/reference/client-libraries/)

InfluxDB client libraries are language-specific tools that integrate with InfluxDB APIs. View the list of available client libraries.

### [InfluxDB HTTP API](/influxdb3/clustered/reference/api/)

The InfluxDB HTTP API provides a programmatic interface for interactions with InfluxDB, such as writing and querying data. Access the InfluxDB API using the `/api/v2/write` or InfluxDB v1 endpoints.

### [InfluxDB internals](/influxdb3/clustered/reference/internals/)

Learn about internal systems and implementation details of InfluxDB Clustered.

### [Other InfluxDB syntaxes](/influxdb3/clustered/reference/syntax/)

InfluxDB uses a handful of languages and syntaxes to perform tasks such as writing, querying, and processing data.

### [Glossary](/influxdb3/clustered/reference/glossary/)

Terms related to InfluxData products and platforms.

### [Sample data](/influxdb3/clustered/reference/sample-data/)

Sample datasets are used throughout the the InfluxDB Clustered documentation to demonstrate functionality. Use the following sample datasets to replicate provided examples.

### [Use the InfluxDB documentation MCP server](/influxdb3/clustered/reference/mcp-server/)

Query InfluxDB Clustered documentation from your IDE using the InfluxDB documentation MCP server.


---

## Query data in InfluxDB Clustered

Learn to query data stored in InfluxDB.

#### Choose the query method for your workload

-   For new query workloads, use one of the many available [Flight clients](/influxdb3/clustered/tags/flight-client/) and SQL or InfluxQL.
-   [Use the HTTP API `/query` endpoint and InfluxQL](/influxdb3/clustered/query-data/execute-queries/influxdb-v1-api/) when you bring existing v1 query workloads to InfluxDB Clustered.

### [Execute queries](/influxdb3/clustered/query-data/execute-queries/)

Use tools and libraries to query data stored in an InfluxDB cluster.

### [Query data with SQL](/influxdb3/clustered/query-data/sql/)

Learn to query data stored in InfluxDB Clustered using SQL.

### [Query data with InfluxQL](/influxdb3/clustered/query-data/influxql/)

Learn to use InfluxQL to query data stored in InfluxDB Clustered.

### [Troubleshoot and optimize queries](/influxdb3/clustered/query-data/troubleshoot-and-optimize/)

Troubleshoot errors and optimize performance for SQL and InfluxQL queries in InfluxDB. Use observability tools to view query execution and metrics.

[query](/influxdb3/clustered/tags/query/)


---

## Process and visualize data stored in InfluxDB

Learn how to process, analyze, and visualize data stored in InfluxDB and perform tasks like modifying and storing modified data, applying advanced downsampling techniques, sending alerts, and more.

### [Downsample data stored in InfluxDB](/influxdb3/clustered/process-data/downsample/)

Learn about different methods for querying and downsampling time series data stored in InfluxDB.

### [Summarize query results and data distribution](/influxdb3/clustered/process-data/summarize/)

Query data stored in InfluxDB and use tools like pandas to summarize the results schema and distribution.

### [Use data analysis tools](/influxdb3/clustered/process-data/tools/)

Use popular data analysis tools to analyze time series data stored in an InfluxDB database.

### [Visualize data](/influxdb3/clustered/process-data/visualize/)

Use visualization tools like Grafana, Superset, and others to visualize time series data stored in InfluxDB.

### [Send alerts using data in InfluxDB](/influxdb3/clustered/process-data/send-alerts/)

Query, analyze, and send alerts using time series data stored in InfluxDB.


---

## Install InfluxDB Clustered

InfluxDB Clustered is deployed and managed using Kubernetes. This installation guide walks you through the following four installation phases and the goal of each phase. This process helps you set up and run your cluster and ensure it performs well with your expected production workload.

1. **[Set up your cluster](/influxdb3/clustered/install/set-up-cluster/)**: Get a basic InfluxDB cluster up and running with as few external dependencies as possible and confirm you can write and query data.
2. **[Customize your cluster](/influxdb3/clustered/install/customize-cluster/)**: Review and customize the available configuration options specific to your workload.
3. **[Optimize your cluster](/influxdb3/clustered/install/optimize-cluster/)**: Scale and load test your InfluxDB cluster to confirm that it will satisfy your scalability and performance needs. Work with InfluxData to review your schema and determine how best to organize your data and develop queries representative of your workload to ensure queries meet performance requirements.
4. **[Secure your cluster](/influxdb3/clustered/install/secure-cluster/)**: Integrate InfluxDB with your identity provider to manage access to your cluster. Install TLS certificates and enable TLS access. Prepare your cluster for production use.

## InfluxDB Clustered license

InfluxDB Clustered is a commercial product offered by InfluxData, the creators of InfluxDB. Please contact InfluxData Sales to obtain a license *before* installing InfluxDB Clustered.

[Contact InfluxData Sales](https://www.influxdata.com/contact-sales-influxdb-clustered/)

## Setup, configure, and deploy InfluxDB Clustered

#### Deploying in air-gapped environments

To deploy InfluxDB Clustered in an air-gapped environment (without internet access), use one of the following approaches:

-   **Recommended**: Directly use `kubit local apply`
-   Helm (includes the kubit operator)
-   Directly use the kubit operator

For more information, see [Choose the right deployment tool for your environment](/influxdb3/clustered/install/set-up-cluster/configure-cluster/#choose-the-right-deployment-tool-for-your-environment)

1. [Set up your InfluxDB cluster](/influxdb3/clustered/install/set-up-cluster/)
2. [Customize your InfluxDB cluster](/influxdb3/clustered/install/customize-cluster/)
3. [Optimize your InfluxDB cluster](/influxdb3/clustered/install/optimize-cluster/)
4. [Secure your InfluxDB cluster](/influxdb3/clustered/install/secure-cluster/)

[Set up prerequisites](/influxdb3/clustered/install/set-up-cluster/prerequisites/)


---

## InfluxDB guides

Learn how to integrate with and perform specific operations on data stored in InfluxDB Clustered.

### [Learn to use APIs for your workloads](/influxdb3/clustered/guides/api-compatibility/)

Choose the API and tools that fit your workload. Learn how to authenticate, write, and query using Telegraf, client libraries, and HTTP clients.

### [Migrate data to InfluxDB Clustered](/influxdb3/clustered/guides/migrate-data/)

Migrate data from InfluxDB powered by TSM (OSS, Enterprise, or Cloud) to InfluxDB Clustered.


---

## Get started with InfluxDB Clustered

InfluxDB is the platform purpose-built to collect, store, and query time series data. InfluxDB Clustered is powered by the InfluxDB 3 storage engine, that provides nearly unlimited series cardinality, improved query performance, and interoperability with widely used data processing tools and platforms.

**Time series data** is a sequence of data points indexed in time order. Data points typically consist of successive measurements made from the same source and are used to track changes over time. Examples of time series data include:

-   Industrial sensor data
-   Server performance metrics
-   Heartbeats per minute
-   Electrical activity in the brain
-   Rainfall measurements
-   Stock prices

This multi-part tutorial walks you through writing time series data to your InfluxDB cluster, querying, and then visualizing that data.

## Key concepts before you get started

Before you get started using InfluxDB, it’s important to understand how time series data is organized and stored in InfluxDB and some key definitions that are used throughout this documentation.

-   [Data organization](#data-organization)
-   [Schema on write](#schema-on-write)
-   [Important definitions](#important-definitions)

### Data organization

The InfluxDB Clustered data model organizes time series data into databases and tables.

A database can contain multiple tables. Tables contain multiple tags and fields.

-   **Database**: A named location where time series data is stored in *tables*. *Database* is synonymous with *bucket* in InfluxDB Cloud Serverless and InfluxDB TSM.
    -   **Table**: A logical grouping for time series data. All *points* in a given table should have the same *tags*. A table contains *tags* and *fields*. *Table* is synonymous with *measurement* in InfluxDB Cloud Serverless and InfluxDB TSM.
        -   **Tags**: Key-value pairs that provide metadata for each point–for example, something to identify the source or context of the data like host, location, station, etc. Tag values may be null.
        -   **Fields**: Key-value pairs with values that change over time–for example, temperature, pressure, stock price, etc. Field values may be null, but at least one field value is not null on any given row.
        -   **Timestamp**: Timestamp associated with the data. When stored on disk and queried, all data is ordered by time. A timestamp is never null.

#### What about buckets and measurements?

If coming from InfluxDB Cloud Serverless or InfluxDB powered by the TSM storage engine, you’re likely familiar with the concepts *bucket* and *measurement*. *Bucket* in TSM or InfluxDB Cloud Serverless is synonymous with *database* in InfluxDB Clustered. *Measurement* in TSM or InfluxDB Cloud Serverless is synonymous with *table* in InfluxDB Clustered.

### Schema on write

As you write data to InfluxDB, the data defines the table schema. You don’t need to create tables or explicitly define the table schema.

### Important definitions

The following definitions are important to understand when using InfluxDB:

-   **Point**: Single data record identified by its *measurement, tag keys, tag values, field key, and timestamp*.
-   **Series**: A group of points with the same *measurement, tag keys and values, and field key*.
-   **Primary key**: Columns used to uniquely identify each row in a table. Rows are uniquely identified by their *timestamp and tag set*. A row’s primary key *tag set* does not include tags with null values.

##### Example InfluxDB query results

name: weather

| time | city | country | temperature | humidity |
| --- | --- | --- | --- | --- |
| 2022-01-01T12:00:00Z | London | UK | 12.0 | 88.4 |
| 2022-01-01T12:00:00Z | Cologne | DE | 13.2 | 88.5 |
| 2022-02-01T12:00:00Z | London | UK | 12.1 | 94.0 |
| 2022-02-01T12:00:00Z | Cologne | DE | 11.5 | 87.8 |
| 2022-03-01T12:00:00Z | London | UK | 11.5 | 82.1 |
| 2022-03-01T12:00:00Z | Cologne | DE | 10.2 | 76.4 |
| 2022-04-01T12:00:00Z | London | UK | 5.9 | 87.6 |
| 2022-04-01T12:00:00Z | Cologne | DE | 7.9 | 93.3 |

## Tools to use

The following table compares tools that you can use to interact with InfluxDB Clustered. This tutorial covers many of the recommended tools.

| Tool | Administration | Write | Query |
| --- | --- | --- | --- |
| Chronograf | - | - |  |
| influx CLI | - | - | - |
| influxctl CLI* |  |  |  |
| influx3 data CLI* | - |  |  |
| InfluxDB HTTP API* | - |  |  |
| InfluxDB user interface | - | - | - |
| InfluxDB 3 client libraries* | - |  |  |
| InfluxDB v2 client libraries | - |  | - |
| InfluxDB v1 client libraries | - |  |  |
| Telegraf* | - |  | - |
| Third-party tools |  |  |  |
| Flight SQL clients | - | - |  |
| Grafana | - | - |  |
| Superset | - | - |  |
| Tableau | - | - |  |

\* Covered in this tutorial

Avoid using the `influx` CLI with InfluxDB Clustered. While it may coincidentally work, it isn’t supported.

### `influxctl` admin CLI

The [`influxctl` command line interface (CLI)](/influxdb3/clustered/reference/cli/influxctl/) writes, queries, and performs administrative tasks, such as managing databases and authorization tokens in a cluster.

### `influx3` data CLI

The [`influx3` data CLI](/influxdb3/clustered/get-started/query/?t=influx3+CLI#execute-an-sql-query) is a community-maintained tool that lets you write and query data in InfluxDB Clustered from a command line. It uses the HTTP API to write data and uses Flight gRPC to query data.

### InfluxDB HTTP API

The [InfluxDB HTTP API](/influxdb/v2/reference/api/) provides a simple way to let you manage InfluxDB Clustered and write and query data using HTTP(S) clients. Examples in this tutorial use cURL, but any HTTP(S) client will work.

The `/write` and `/query` v1-compatible endpoints work with the username/password authentication schemes and existing InfluxDB 1.x tools and code. The `/api/v2/write` v2-compatible endpoint works with existing InfluxDB 2.x tools and code.

### InfluxDB client libraries

InfluxDB client libraries are community-maintained, language-specific clients that interact with InfluxDB APIs.

[InfluxDB 3 client libraries](/influxdb3/clustered/reference/client-libraries/v3/) are the recommended client libraries for writing and querying data InfluxDB Clustered. They use the HTTP API to write data and use InfluxDB’s Flight gRPC API to query data.

[InfluxDB v2 client libraries](/influxdb3/clustered/reference/client-libraries/v2/) can use `/api/v2` HTTP endpoints to manage resources such as buckets and API tokens, and write data in InfluxDB Clustered.

[InfluxDB v1 client libraries](/influxdb3/clustered/reference/client-libraries/v1/) can write data to InfluxDB Clustered.

## Authorization

**InfluxDB Clustered requires authentication** using one of the following [token](/influxdb3/clustered/admin/tokens/) types:

-   **Database token**: A token that grants read and write access to InfluxDB databases.
    
-   **Management token**: A short-lived (1 hour) [Auth0 token](#) used to administer your InfluxDB cluster. These are generated by the `influxctl` CLI and do not require any direct management. Management tokens authorize a user to perform tasks related to:
    
    -   Account management
    -   Database management
    -   Database token management
    -   Pricing

[Set up InfluxDB](/influxdb3/clustered/get-started/setup/)

[get-started](/influxdb3/clustered/tags/get-started/)


---

## Administer InfluxDB Clustered

The following articles provide information about managing your InfluxDB Clustered resources:

### [Identify InfluxDB Clustered version](/influxdb3/clustered/admin/identify-version/)

Learn how to identify your InfluxDB Clustered version using influxctl CLI and other methods.

### [Manage your InfluxDB Clustered license](/influxdb3/clustered/admin/licensing/)

Install and manage your InfluxDB Clustered license to authorize the use of the InfluxDB Clustered software.

### [Manage users in your InfluxDB cluster](/influxdb3/clustered/admin/users/)

Manage users with administrative access to your InfluxDB cluster through your identity provider and your InfluxDB `AppInstance` resource.

### [Manage databases](/influxdb3/clustered/admin/databases/)

Manage databases in your InfluxDB cluster. A database is a named location where time series data is stored. Each InfluxDB database has a retention period, which defines the maximum age of data stored in the database.

### [Manage tables](/influxdb3/clustered/admin/tables/)

Manage tables in your InfluxDB cluster. A table is a collection of related data stored in table format. In previous versions of InfluxDB, tables were known as “measurements.”

### [Manage tokens](/influxdb3/clustered/admin/tokens/)

Manage database tokens in your InfluxDB cluster. Database tokens grant read and write permissions to one or more databases and allow for actions like writing and querying data.

### [Manage data partitioning](/influxdb3/clustered/admin/custom-partitions/)

Customize your partitioning strategy to optimize query performance for your specific schema and workload.

### [Back up and restore your cluster](/influxdb3/clustered/admin/backup-restore/)

Use InfluxDB Clustered Catalog snapshots to keep necessary data in object storage and restore to a recovery point in case of emergency.

### [Query system data](/influxdb3/clustered/admin/query-system-data/)

Query system tables in your InfluxDB cluster to see data related to queries, tables, partitions, and compaction in your cluster.

### [Upgrade InfluxDB Clustered](/influxdb3/clustered/admin/upgrade/)

Use Kubernetes to upgrade your InfluxDB Clustered version.

### [Scale your InfluxDB cluster](/influxdb3/clustered/admin/scale-cluster/)

InfluxDB Clustered lets you scale individual components of your cluster both vertically and horizontally to match your specific workload.

### [Manage environment variables in your InfluxDB Cluster](/influxdb3/clustered/admin/env-vars/)

Use environment variables to define settings for individual components in your InfluxDB cluster.

### [Bypass your identity provider](/influxdb3/clustered/admin/bypass-identity-provider/)

InfluxDB clustered generates a valid access token (known as the *admin token*) that can be used in development and testing environments in lieu of configuring and using an OAuth2 identity provider.

