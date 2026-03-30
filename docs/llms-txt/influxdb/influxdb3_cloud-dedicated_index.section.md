---
title: InfluxDB Cloud Dedicated documentation
description: InfluxDB Cloud Dedicated is a hosted and managed InfluxDB Cloud cluster dedicated to a single tenant. The InfluxDB time series platform is designed to handle high write and query loads. Learn how to use and leverage InfluxDB Cloud Dedicated for your specific time series use case.
url: https://docs.influxdata.com/influxdb3/cloud-dedicated/
product: InfluxDB Cloud Dedicated
type: section
pages: 8
estimated_tokens: 7771
child_pages:
  - url: https://docs.influxdata.com/influxdb3/cloud-dedicated/write-data/
    title: Write data to InfluxDB Cloud Dedicated
  - url: https://docs.influxdata.com/influxdb3/cloud-dedicated/reference/
    title: InfluxDB Cloud Dedicated reference documentation
  - url: https://docs.influxdata.com/influxdb3/cloud-dedicated/query-data/
    title: Query data in InfluxDB Cloud Dedicated
  - url: https://docs.influxdata.com/influxdb3/cloud-dedicated/process-data/
    title: Process and visualize data stored in InfluxDB
  - url: https://docs.influxdata.com/influxdb3/cloud-dedicated/guides/
    title: InfluxDB guides
  - url: https://docs.influxdata.com/influxdb3/cloud-dedicated/get-started/
    title: Get started with InfluxDB Cloud Dedicated
  - url: https://docs.influxdata.com/influxdb3/cloud-dedicated/admin/
    title: Administer InfluxDB Cloud Dedicated
---

# InfluxDB Cloud Dedicated documentation

InfluxDB Cloud Dedicated is a hosted and managed InfluxDB Cloud cluster dedicated to a single tenant. The InfluxDB time series platform is designed to handle high write and query loads. Learn how to use and leverage InfluxDB Cloud Dedicated for your specific time series use case.

[Run an InfluxDB Cloud Dedicated proof of concept (PoC)](https://www.influxdata.com/contact-sales-cloud-dedicated/)  
[Get started with InfluxDB Cloud Dedicated](/influxdb3/cloud-dedicated/get-started/)

## InfluxDB 3

**InfluxDB 3** is InfluxDB’s next generation that unlocks series limitations present in the Time Structured Merge Tree (TSM) storage engine and allows infinite series cardinality without any impact on overall database performance. It also brings native **SQL support** and improved InfluxQL performance.

View the following video for more information about InfluxDB 3:


---

## Write data to InfluxDB Cloud Dedicated

Write data to InfluxDB Cloud Dedicated using the following tools and methods:

#### Choose the write endpoint for your workload

When bringing existing v1 write workloads, use the InfluxDB Cloud Dedicated HTTP API [`/write` endpoint](/influxdb3/cloud-dedicated/guides/api-compatibility/v1/). When creating new write workloads, use the HTTP API [`/api/v2/write` endpoint](/influxdb3/cloud-dedicated/guides/api-compatibility/v2/).

### [Use Telegraf to write data](/influxdb3/cloud-dedicated/write-data/use-telegraf/)

Use Telegraf to collect and write data to InfluxDB. Create Telegraf configurations in the InfluxDB UI or manually configure Telegraf.

### [Write line protocol data to InfluxDB Cloud Dedicated](/influxdb3/cloud-dedicated/write-data/line-protocol/)

Use Telegraf and API clients to write line protocol data to InfluxDB Cloud Dedicated.

### [Write CSV data to InfluxDB Cloud Dedicated](/influxdb3/cloud-dedicated/write-data/csv/)

Use Telegraf or the HTTP API to write CSV data to InfluxDB Cloud Dedicated.

### [Best practices for writing data](/influxdb3/cloud-dedicated/write-data/best-practices/)

Learn about the recommendations and best practices for writing data to InfluxDB Cloud Dedicated.

### [Troubleshoot issues writing data](/influxdb3/cloud-dedicated/write-data/troubleshoot/)

Troubleshoot issues writing data. Find response codes for failed writes. Discover how writes fail, from exceeding rate or payload limits, to syntax errors and schema conflicts.


---

## InfluxDB Cloud Dedicated reference documentation

### [Release notes related to InfluxDB Cloud Dedicated](/influxdb3/cloud-dedicated/reference/release-notes/)

View release notes and updates for products and tools related to InfluxDB Cloud Dedicated.

### [SQL reference documentation](/influxdb3/cloud-dedicated/reference/sql/)

Learn the SQL syntax and structure used to query InfluxDB.

### [InfluxQL reference documentation](/influxdb3/cloud-dedicated/reference/influxql/)

InfluxQL is an SQL-like query language for interacting with data in InfluxDB.

### [Command line tools](/influxdb3/cloud-dedicated/reference/cli/)

InfluxDB provides command line tools designed to manage and work with your InfluxDB Cloud Dedicated cluster from the command line.

### [InfluxDB HTTP API](/influxdb3/cloud-dedicated/reference/api/)

The InfluxDB HTTP API provides a programmatic interface for interactions with InfluxDB, such as writing and querying data, and managing an InfluxDB cluster. Access the InfluxDB API using the `/api/v2/write`, InfluxDB v1, or Management API endpoints for InfluxDB Cloud Dedicated.

### [Other InfluxDB syntaxes](/influxdb3/cloud-dedicated/reference/syntax/)

InfluxDB uses a handful of languages and syntaxes to perform tasks such as writing, querying, and processing data.

### [API client libraries](/influxdb3/cloud-dedicated/reference/client-libraries/)

InfluxDB client libraries are language-specific tools that integrate with InfluxDB APIs. View the list of available client libraries.

### [InfluxDB internals](/influxdb3/cloud-dedicated/reference/internals/)

Learn about internal systems and implementation details of InfluxDB Cloud Dedicated.

### [Naming restrictions and conventions](/influxdb3/cloud-dedicated/reference/naming-restrictions/)

Learn about naming restrictions and conventions for databases, tables, tags, fields, and other identifiers in InfluxDB Cloud Dedicated.

### [Policies and procedures](/influxdb3/cloud-dedicated/reference/policies/)

InfluxData product policies and procedures.

### [Glossary](/influxdb3/cloud-dedicated/reference/glossary/)

Terms related to InfluxData products and platforms.

### [Sample data](/influxdb3/cloud-dedicated/reference/sample-data/)

Sample datasets are used throughout the the InfluxDB Cloud Dedicated documentation to demonstrate functionality. Use the following sample datasets to replicate provided examples.


---

## Query data in InfluxDB Cloud Dedicated

Learn to query data stored in InfluxDB.

#### Choose the query method for your workload

-   For new query workloads, use one of the many available [Flight clients](/influxdb3/cloud-dedicated/tags/flight-client/) and SQL or InfluxQL.
-   [Use the HTTP API `/query` endpoint and InfluxQL](/influxdb3/cloud-dedicated/query-data/execute-queries/influxdb-v1-api/) when you bring existing v1 query workloads to InfluxDB Cloud Dedicated.

### [Execute queries](/influxdb3/cloud-dedicated/query-data/execute-queries/)

Use tools and libraries to query data stored in InfluxDB Cloud Dedicated.

### [Query data with SQL](/influxdb3/cloud-dedicated/query-data/sql/)

Learn to query data stored in InfluxDB Cloud using SQL.

### [Query data with InfluxQL](/influxdb3/cloud-dedicated/query-data/influxql/)

Learn to use InfluxQL to query data stored in InfluxDB Cloud Dedicated.

### [Troubleshoot and optimize queries](/influxdb3/cloud-dedicated/query-data/troubleshoot-and-optimize/)

Troubleshoot errors and optimize performance for SQL and InfluxQL queries in InfluxDB. Use observability tools to view query execution and metrics.


---

## Process and visualize data stored in InfluxDB

Learn how to process, analyze, and visualize data stored in InfluxDB and perform tasks like modifying and storing modified data, applying advanced downsampling techniques, sending alerts, and more.

### [Downsample data stored in InfluxDB](/influxdb3/cloud-dedicated/process-data/downsample/)

Learn about different methods for querying and downsampling time series data stored in InfluxDB.

### [Summarize query results and data distribution](/influxdb3/cloud-dedicated/process-data/summarize/)

Query data stored in InfluxDB and use tools like pandas to summarize the results schema and distribution.

### [Use data analysis tools](/influxdb3/cloud-dedicated/process-data/tools/)

Use popular data analysis tools to analyze time series data stored in an InfluxDB database.

### [Visualize data](/influxdb3/cloud-dedicated/process-data/visualize/)

Use visualization tools like Grafana, Superset, and others to visualize time series data stored in InfluxDB.

### [Send alerts using data in InfluxDB](/influxdb3/cloud-dedicated/process-data/send-alerts/)

Query, analyze, and send alerts using time series data stored in InfluxDB.


---

## InfluxDB guides

Learn how to integrate with and perform specific operations on data stored in InfluxDB Cloud Dedicated.

### [Learn to use APIs for your workloads](/influxdb3/cloud-dedicated/guides/api-compatibility/)

Choose the API and tools that fit your workload. Learn how to authenticate, write, and query using Telegraf, client libraries, and HTTP clients.

### [Migrate data to InfluxDB Cloud Dedicated](/influxdb3/cloud-dedicated/guides/migrate-data/)

Migrate data from InfluxDB powered by TSM (OSS, Enterprise, or Cloud) to InfluxDB Cloud Dedicated.

### [Prototype your app on InfluxDB Cloud Serverless](/influxdb3/cloud-dedicated/guides/prototype-evaluation/)

Utilize InfluxDB Cloud Serverless to prototype your production application and then move it to InfluxDB Cloud Dedicated. Learn about important differences between Cloud Serverless and Cloud Dedicated and best practices for building an application prototype on Cloud Serverless.


---

## Get started with InfluxDB Cloud Dedicated

InfluxDB is the platform purpose-built to collect, store, and query time series data. InfluxDB Cloud Dedicated is powered by the InfluxDB 3 storage engine, that provides nearly unlimited series cardinality, improved query performance, and interoperability with widely used data processing tools and platforms.

[Run an InfluxDB Cloud Dedicated proof of concept (PoC)](https://www.influxdata.com/contact-sales-cloud-dedicated/)

**Time series data** is a sequence of data points indexed in time order. Data points typically consist of successive measurements made from the same source and are used to track changes over time. Examples of time series data include:

-   Industrial sensor data
-   Server performance metrics
-   Heartbeats per minute
-   Electrical activity in the brain
-   Rainfall measurements
-   Stock prices

This multi-part tutorial walks you through writing time series data to InfluxDB Cloud Dedicated, querying, and then visualizing that data.

## Key concepts before you get started

Before you get started using InfluxDB, it’s important to understand how time series data is organized and stored in InfluxDB and some key definitions that are used throughout this documentation.

-   [Data organization](#data-organization)
-   [Schema on write](#schema-on-write)
-   [Important definitions](#important-definitions)

### Data organization

The InfluxDB Cloud Dedicated data model organizes time series data into databases and tables.

A database can contain multiple tables. Tables contain multiple tags and fields.

-   **Database**: A named location where time series data is stored in *tables*. *Database* is synonymous with *bucket* in InfluxDB Cloud Serverless and InfluxDB TSM.
    -   **Table**: A logical grouping for time series data. All *points* in a given table should have the same *tags*. A table contains *tags* and *fields*. *Table* is synonymous with *measurement* in InfluxDB Cloud Serverless and InfluxDB TSM.
        -   **Tags**: Key-value pairs that provide metadata for each point–for example, something to identify the source or context of the data like host, location, station, etc. Tag values may be null.
        -   **Fields**: Key-value pairs with values that change over time–for example, temperature, pressure, stock price, etc. Field values may be null, but at least one field value is not null on any given row.
        -   **Timestamp**: Timestamp associated with the data. When stored on disk and queried, all data is ordered by time. A timestamp is never null.

#### What about buckets and measurements?

If coming from InfluxDB Cloud Serverless or InfluxDB powered by the TSM storage engine, you’re likely familiar with the concepts *bucket* and *measurement*. *Bucket* in TSM or InfluxDB Cloud Serverless is synonymous with *database* in InfluxDB Cloud Dedicated. *Measurement* in TSM or InfluxDB Cloud Serverless is synonymous with *table* in InfluxDB Cloud Dedicated.

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

The following table compares tools that you can use to interact with InfluxDB Cloud Dedicated. This tutorial covers many of the recommended tools.

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

Avoid using the `influx` CLI with InfluxDB Cloud Dedicated. While it may coincidentally work, it isn’t supported.

### `influxctl` CLI

The [`influxctl` command line interface (CLI)](/influxdb3/cloud-dedicated/reference/cli/influxctl/) writes, queries, and performs administrative tasks, such as managing databases and authorization tokens in a cluster.

### `influx3` data CLI

The [`influx3` data CLI](/influxdb3/cloud-dedicated/get-started/query/?t=influx3+CLI#execute-an-sql-query) is a community-maintained tool that lets you write and query data in InfluxDB Cloud Dedicated from a command line. It uses the HTTP API to write data and uses Flight gRPC to query data.

### InfluxDB HTTP API

The [InfluxDB HTTP API](/influxdb/v2/reference/api/) provides a simple way to let you manage InfluxDB Cloud Dedicated and write and query data using HTTP(S) clients. Examples in this tutorial use cURL, but any HTTP(S) client will work.

The `/write` and `/query` v1-compatible endpoints work with the username/password authentication schemes and existing InfluxDB 1.x tools and code. The `/api/v2/write` v2-compatible endpoint works with existing InfluxDB 2.x tools and code.

### InfluxDB client libraries

InfluxDB client libraries are community-maintained, language-specific clients that interact with InfluxDB APIs.

[InfluxDB 3 client libraries](/influxdb3/cloud-dedicated/reference/client-libraries/v3/) are the recommended client libraries for writing and querying data InfluxDB Cloud Dedicated. They use the HTTP API to write data and use InfluxDB’s Flight gRPC API to query data.

[InfluxDB v2 client libraries](/influxdb3/cloud-dedicated/reference/client-libraries/v2/) can use `/api/v2` HTTP endpoints to manage resources such as buckets and API tokens, and write data in InfluxDB Cloud Dedicated.

[InfluxDB v1 client libraries](/influxdb3/cloud-dedicated/reference/client-libraries/v1/) can write data to InfluxDB Cloud Dedicated.

## Authorization

**InfluxDB Cloud Dedicated requires authentication** using one of the following [token](/influxdb3/cloud-dedicated/admin/tokens/) types:

-   **Database token**: A token that grants read and write access to InfluxDB databases.
    
-   **Management token**: [Auth0 authentication token](/influxdb3/cloud-dedicated/reference/internals/security/#access-authentication-and-authorization) generated by the `influxctl` CLI and used to administer your InfluxDB cluster. Management tokens authorize a user to perform tasks related to:
    
    -   Account management
    -   Database management
    -   Database token management
    -   Pricing

By default, management tokens are

-   short-lived
-   issued for a specific user
-   issued by an OAuth2 identity provider
-   managed by `influxctl` and don’t require management by users

However, for automation purposes, an `influxctl` user can [manually create a long-lived management token](/influxdb3/cloud-dedicated/admin/tokens/management/#create-a-management-token) for use with the [Management API for Cloud Dedicated](/influxdb3/cloud-dedicated/api/management). Manually-created management tokens authenticate directly with your InfluxDB cluster and don’t require human interaction with your identity provider.

[Set up InfluxDB](/influxdb3/cloud-dedicated/get-started/setup/)


---

## Administer InfluxDB Cloud Dedicated

The following articles provide information about managing your InfluxDB Cloud Dedicated resources:

### [Identify InfluxDB Cloud Dedicated version](/influxdb3/cloud-dedicated/admin/identify-version/)

Learn how to identify your InfluxDB Cloud Dedicated cluster through URL patterns, account settings, and HTTP headers.

### [View account information](/influxdb3/cloud-dedicated/admin/account/)

Use the Admin UI for InfluxDB Cloud Dedicated to view information for your Cloud Dedicated account. Your InfluxDB Cloud Dedicated account is a collection of InfluxDB Cloud Dedicated clusters and associated resources.

### [Manage clusters](/influxdb3/cloud-dedicated/admin/clusters/)

Manage InfluxDB Cloud Dedicated clusters. An InfluxDB Cloud Dedicated cluster is a collection of InfluxDB servers dedicated to the workload of a single customer and associated with an InfluxDB account.

### [Manage databases](/influxdb3/cloud-dedicated/admin/databases/)

Manage databases in your InfluxDB Cloud Dedicated cluster. A database is a named location where time series data is stored. Each InfluxDB database has a retention period, which defines the maximum age of data stored in the database.

### [Manage tables](/influxdb3/cloud-dedicated/admin/tables/)

Manage tables in your InfluxDB Cloud Dedicated cluster. A table is a collection of related data stored in table format. In previous versions of InfluxDB, tables were known as “measurements.”

### [Manage tokens](/influxdb3/cloud-dedicated/admin/tokens/)

Manage database tokens in your InfluxDB Cloud Dedicated cluster. Database tokens grant read and write permissions to one or more databases and allow for actions like writing and querying data.

### [Manage users](/influxdb3/cloud-dedicated/admin/users/)

Manage users and access to resources in your InfluxDB Cloud Dedicated cluster. Use the Admin UI for self-service user management or contact support for advanced operations

### [Manage data partitioning](/influxdb3/cloud-dedicated/admin/custom-partitions/)

Customize your partitioning strategy to optimize query performance for your specific schema and workload.

### [Monitor your cluster](/influxdb3/cloud-dedicated/admin/monitor-your-cluster/)

Use the Admin UI or Grafana operational dashboards to monitor your InfluxDB Cloud Dedicated cluster.

### [Query system data](/influxdb3/cloud-dedicated/admin/query-system-data/)

Query system tables in your InfluxDB Cloud Dedicated cluster to see data related to queries, tables, partitions, and compaction in your cluster.

### [Enable autoscaling](/influxdb3/cloud-dedicated/admin/autoscaling/)

Learn how autoscaling works in InfluxDB Cloud Dedicated and how to enable and configure autoscaling limits for your clusters.

### [Set up and use single sign-on (SSO)](/influxdb3/cloud-dedicated/admin/sso/)

Set up and use single sign-on (SSO) to authenicate access to your InfluxDB Cluster.

### [Use the InfluxDB 3 MCP server](/influxdb3/cloud-dedicated/admin/mcp-server/)

Use the **InfluxDB MCP server** to interact with and manage InfluxDB Cloud Dedicated using natural language with LLM agents to query and analyze data, manage databases and more. Query InfluxDB Cloud Dedicated documentation from your IDE using the InfluxDB documentation MCP server.

