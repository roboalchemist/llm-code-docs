---
title: InfluxDB Enterprise v1 documentation
description: Documentation for InfluxDB Enterprise v1, which adds clustering, high availability, fine-grained authorization, and more to InfluxDB OSS.
url: https://docs.influxdata.com/enterprise_influxdb/v1/
product: InfluxDB Enterprise v1
type: section
pages: 13
estimated_tokens: 8168
child_pages:
  - url: https://docs.influxdata.com/enterprise_influxdb/v1/write_protocols/
    title: Write protocols in InfluxDB
  - url: https://docs.influxdata.com/enterprise_influxdb/v1/troubleshooting/
    title: Troubleshoot InfluxDB Enterprise v1
  - url: https://docs.influxdata.com/enterprise_influxdb/v1/tools/
    title: InfluxDB Enterprise v1 tools
  - url: https://docs.influxdata.com/enterprise_influxdb/v1/supported_protocols/
    title: Supported protocols in InfluxDB
  - url: https://docs.influxdata.com/enterprise_influxdb/v1/query_language/
    title: Influx Query Language (InfluxQL)
  - url: https://docs.influxdata.com/enterprise_influxdb/v1/introduction/
    title: Introducing InfluxDB Enterprise v1
  - url: https://docs.influxdata.com/enterprise_influxdb/v1/guides/
    title: InfluxDB Enterprise v1 guides
  - url: https://docs.influxdata.com/enterprise_influxdb/v1/flux/
    title: Flux data scripting language
  - url: https://docs.influxdata.com/enterprise_influxdb/v1/features/
    title: InfluxDB Enterprise v1 features
  - url: https://docs.influxdata.com/enterprise_influxdb/v1/concepts/
    title: InfluxDB Enterprise v1 concepts
  - url: https://docs.influxdata.com/enterprise_influxdb/v1/administration/
    title: Administer InfluxDB Enterprise v1
  - url: https://docs.influxdata.com/enterprise_influxdb/v1/about-the-project/
    title: About the project
---

# InfluxDB Enterprise v1 documentation

InfluxDB Enterprise provides a time series database designed to handle high write and query loads and offers highly scalable clusters on your infrastructure with a management UI. Use for DevOps monitoring, IoT sensor data, and real-time analytics.

#### InfluxDB Cloud 1 users

**InfluxDB Cloud 1** (InfluxCloud 1.x) is based on InfluxDB Enterprise v1. This is the correct documentation.

-   **InfluxDB Cloud 1 Support**: [help.influxcloud.net](https://help.influxcloud.net)
-   **Migrate**: Consider [migrating to InfluxDB 3](/platform/#migration-to-influxdb-3) (Enterprise, Cloud Serverless, or Cloud Dedicated) with v1 API compatibility

## Key features

-   High performance datastore written specifically for time series data. High ingest speed and data compression.
-   Provides high availability across your cluster and eliminates a single point of failure.
-   Written entirely in Go. Compiles into a single binary with no external dependencies.
-   Simple, high performing write and query HTTP APIs.
-   Plugin support for other data ingestion protocols such as Graphite, collectd, and OpenTSDB.
-   Expressive SQL-like query language tailored to easily query aggregated data.
-   Continuous queries automatically compute aggregate data to make frequent queries more efficient.
-   Tags let you index series for fast and efficient queries.
-   Retention policies efficiently auto-expire stale data.

## Next steps

-   [Install and deploy](/enterprise_influxdb/v1/introduction/installation/)
-   Review key [concepts](/enterprise_influxdb/v1/concepts/)
-   [Get started](/enterprise_influxdb/v1/introduction/getting-started/)


---

## Write protocols in InfluxDB

The InfluxDB line protocol is a text based format for writing points to InfluxDB databases.

## [InfluxDB line protocol reference](/enterprise_influxdb/v1/write_protocols/line_protocol_reference/)

InfluxDB line protocol is a text-based format for writing points to InfluxDB.

## [InfluxDB line protocol tutorial](/enterprise_influxdb/v1/write_protocols/line_protocol_tutorial/)

Tutorial for using InfluxDB line protocol.


---

## Troubleshoot InfluxDB Enterprise v1

## [InfluxDB Enterprise v1 frequently asked questions](/enterprise_influxdb/v1/troubleshooting/frequently-asked-questions/)

Common issues with InfluxDB Enterprise.

## [InfluxDB error messages](/enterprise_influxdb/v1/troubleshooting/errors/)

Covers InfluxDB error messages, their descriptions, and common resolutions.

## [Manage queries](/enterprise_influxdb/v1/troubleshooting/query_management/)

Manage query execution within InfluxDB.

## [Report issues](/enterprise_influxdb/v1/troubleshooting/reporting-issues/)

Contact support to report issues with InfluxDB Enterprise.

## [systemd permission errors](/enterprise_influxdb/v1/troubleshooting/systemd/)

Troubleshoot errors with InfluxDB and systemd permissions


---

## InfluxDB Enterprise v1 tools

#### Flux VS Code extension no longer available

The `vsflux` extension is no longer available in the Visual Studio Marketplace. `vsflux` and the `flux-lsp` Flux Language Server Protocol plugin are no longer maintained. Their repositories have been archived and are no longer receiving updates.

Use the following tools to work with InfluxDB Enterprise:

### [Use the InfluxDB documentation MCP server](/enterprise_influxdb/v1/tools/mcp-server/)

Query InfluxDB Enterprise v1 documentation from your IDE using the InfluxDB documentation MCP server.

### [influx - InfluxDB command line interface](/enterprise_influxdb/v1/tools/influx-cli/)

The `influx` command line interface (CLI) provides an interactive shell for the HTTP API associated with `influxd`. It includes commands for writing and querying data, and managing many aspects of InfluxDB, including databases, organizations, and users.

## Usage

```
influx [flags]
```

## Flags

| Flag | Description |
| --- | --- |
| -version | Display the version and exit |
| -url-prefix | Path to add to the URL after the host and port. Specifies a custom endpoint to connect to. |
| -host | HTTP address of InfluxDB (default: http://localhost:8086) |
| -port | Port to connect to |
| -socket | Unix socket to connect to |
| -database | Database to connect to the server |
| -password | Password to connect to the server. Leaving blank will prompt for password (--password ''). |
| -username | Username to connect to the server |
| -ssl | Use https for requests |
| -unsafessl | Set this when connecting to the cluster using https |
| -execute | Execute command and quit |
| -format | Specify the format of the server responses: json, csv, or column |
| -precision | Specify the format of the timestamp: rfc3339, h, m, s, ms, u or ns |
| -consistency | Set write consistency level: any, one, quorum, or all |
| -pretty | Turns on pretty print for JSON format |
| -import | Import a previous database export from file |
| -pps | Points per second the import will allow. The default is 0 and will not throttle importing. |
| -path | Path to file to import |
| -compressed | Set to true if the import file is compressed |

```
<div class="children-links">
	
		
		
		
		 <h3 id="use-influx---influxdb-command-line-interface"><a href="/enterprise_influxdb/v1/tools/influx-cli/use-influx-cli/" target="">Use influx - InfluxDB command line interface</a></h3>
		
		<p>InfluxDB&rsquo;s command line interface (<code>influx</code>) is an interactive shell for the HTTP API.</p>

```

### [Influx Inspect disk utility](/enterprise_influxdb/v1/tools/influx_inspect/)

Use the `influx_inspect` commands to manage InfluxDB disks and shards.

### [influxd - InfluxDB daemon](/enterprise_influxdb/v1/tools/influxd/)

The influxd daemon starts and runs all the processes necessary for InfluxDB to function.

### [influxd-ctl CLI](/enterprise_influxdb/v1/tools/influxd-ctl/)

Use the `influxd-ctl` CLI to manage your InfluxDB Enterprise v1 cluster.

### [InfluxDB API reference](/enterprise_influxdb/v1/tools/api/)

Use the InfluxDB API endpoints to run queries, write data, check server status, and troubleshoot by tracking HTTP client requests, collecting server statistics, and using Go “pprof” profiles.

### [InfluxDB client libraries](/enterprise_influxdb/v1/tools/api_client_libraries/)

InfluxDB client libraries includes support for Arduino, C#, C++, Go, Java, JavaScript, PHP, Python, and Ruby.

### [InfluxDB inch tool](/enterprise_influxdb/v1/tools/inch/)

Use the InfluxDB inch tool to test InfluxDB performance. Adjust the number of points and tag values to test ingesting different tag cardinalities.

### [Use Grafana with InfluxDB Enterprise v1](/enterprise_influxdb/v1/tools/grafana/)

Configure Grafana to query and visualize data from InfluxDB Enterprise v1.

## InfluxDB open source tools

Tools built for InfluxDB OSS v1.8+ also work with InfluxDB v1 Enterprise. For more information, see [InfluxDB tools](/enterprise_influxdb/v1/tools/).


---

## Supported protocols in InfluxDB

InfluxData supports the following protocols for interacting with InfluxDB:

### [CollectD protocol support in InfluxDB](/enterprise_influxdb/v1/supported_protocols/collectd/)

The collectd input allows InfluxDB to accept data transmitted in collectd native format.

### [Graphite protocol support in InfluxDB](/enterprise_influxdb/v1/supported_protocols/graphite/)

Use the Graphite plugin to write data to InfluxDB using the Graphite protocol.

### [OpenTSDB protocol support in InfluxDB](/enterprise_influxdb/v1/supported_protocols/opentsdb/)

Use the OpenTSDB plugin to write data to InfluxDB using the OpenTSDB protocol.

### [Prometheus endpoints support in InfluxDB](/enterprise_influxdb/v1/supported_protocols/prometheus/)

Read and write Prometheus data in InfluxDB.

### [UDP protocol support in InfluxDB](/enterprise_influxdb/v1/supported_protocols/udp/)

Overview of support for UDP protocol in InfluxDB.


---

## Influx Query Language (InfluxQL)

This section introduces InfluxQL, the InfluxDB SQL-like query language for working with data in InfluxDB databases.

## InfluxQL tutorial

The first seven documents in this section provide a tutorial-style introduction to InfluxQL. Feel free to download the dataset provided in [Sample Data](/enterprise_influxdb/v1/query_language/data_download/) and follow along with the documentation.

#### Data exploration

[Data exploration](/enterprise_influxdb/v1/query_language/explore-data/) covers the query language basics for InfluxQL, including the [`SELECT` statement](/enterprise_influxdb/v1/query_language/explore-data/#the-basic-select-statement), [`GROUP BY` clauses](/enterprise_influxdb/v1/query_language/explore-data/#the-group-by-clause), [`INTO` clauses](/enterprise_influxdb/v1/query_language/explore-data/#the-into-clause), and more. See Data Exploration to learn about [time syntax](/enterprise_influxdb/v1/query_language/explore-data/#time-syntax) and [regular expressions](/enterprise_influxdb/v1/query_language/explore-data/#regular-expressions) in queries.

#### Schema exploration

[Schema exploration](/enterprise_influxdb/v1/query_language/explore-schema/) covers queries that are useful for viewing and exploring your [schema](/enterprise_influxdb/v1/concepts/glossary/#schema). See Schema Exploration for syntax explanations and examples of InfluxQL’s `SHOW` queries.

#### Database management

[Database management](/enterprise_influxdb/v1/query_language/manage-database/) covers InfluxQL for managing [databases](/enterprise_influxdb/v1/concepts/glossary/#database) and [retention policies](/enterprise_influxdb/v1/concepts/glossary/#retention-policy-rp) in InfluxDB. See Database Management for creating and dropping databases and retention policies as well as deleting and dropping data.

#### InfluxQL functions

Covers all [InfluxQL functions](/enterprise_influxdb/v1/query_language/functions/).

#### InfluxQL Continuous Queries

[InfluxQL Continuous Queries](/enterprise_influxdb/v1/query_language/continuous_queries/) covers the [basic syntax](/enterprise_influxdb/v1/query_language/continuous_queries/#basic-syntax) , [advanced syntax](/enterprise_influxdb/v1/query_language/continuous_queries/#advanced-syntax) , and [common use cases](/enterprise_influxdb/v1/query_language/continuous_queries/#continuous-query-use-cases) for [Continuous Queries](/enterprise_influxdb/v1/concepts/glossary/#continuous-query-cq). This page also describes how to [`SHOW`](/enterprise_influxdb/v1/query_language/continuous_queries/#listing-continuous-queries) and [`DROP`](/enterprise_influxdb/v1/query_language/continuous_queries/#deleting-continuous-queries) Continuous Queries.

#### InfluxQL mathematical operators

[InfluxQL mathematical operators](/enterprise_influxdb/v1/query_language/math_operators/) covers the use of mathematical operators in InfluxQL.

#### Authentication and authorization

[Authentication and authorization](/enterprise_influxdb/v1/administration/authentication_and_authorization/) covers how to [set up authentication](/enterprise_influxdb/v1/administration/authentication_and_authorization/#set-up-authentication) and how to [authenticate requests](/enterprise_influxdb/v1/administration/authentication_and_authorization/#authenticate-requests) in InfluxDB. This page also describes the different [user types](/enterprise_influxdb/v1/administration/authentication_and_authorization/#user-types-and-privileges) and the InfluxQL for [managing database users](/enterprise_influxdb/v1/administration/authentication_and_authorization/#user-management-commands).

## InfluxQL reference

The [reference documentation for InfluxQL](/enterprise_influxdb/v1/query_language/spec/).


---

## Introducing InfluxDB Enterprise v1

### [Getting started with InfluxDB Enterprise v1](/enterprise_influxdb/v1/introduction/getting-started/)

Set up your cluster as a data source in Chronograf.

### [InfluxDB Enterprise v1 downloads](/enterprise_influxdb/v1/introduction/download/)

Download InfluxDB Enterprise v1.

### [Install an InfluxDB Enterprise v1 cluster](/enterprise_influxdb/v1/introduction/installation/)

Install InfluxDB Enterprise in your own on-premise environment.

### [Installation requirements](/enterprise_influxdb/v1/introduction/installation_requirements/)

Requirements for installing and deploying InfluxDB Enterprise.


---

## InfluxDB Enterprise v1 guides

## [Authenticate requests to InfluxDB Enterprise v1](/enterprise_influxdb/v1/guides/authenticate/)

Calculate percentages using basic math operators available in InfluxQL or Flux. This guide walks through use cases and examples of calculating percentages from two values in a single query.

## [Calculate percentages in a query](/enterprise_influxdb/v1/guides/calculate_percentages/)

Calculate percentages using basic math operators available in InfluxQL or Flux. This guide walks through use-cases and examples of calculating percentages from two values in a single query.

## [Downsample and retain data](/enterprise_influxdb/v1/guides/downsample_and_retain/)

Downsample data to keep high precision while preserving storage.

## [Hardware sizing guidelines](/enterprise_influxdb/v1/guides/hardware_sizing/)

Review configuration and hardware guidelines for InfluxDB OSS (open source) and InfluxDB Enterprise v1.

## [Migrate InfluxDB OSS instances to InfluxDB Enterprise v1 clusters](/enterprise_influxdb/v1/guides/migration/)

Migrate a running instance of InfluxDB open source (OSS) to an InfluxDB Enterprise v1 cluster.

## [Query data with the InfluxDB API](/enterprise_influxdb/v1/guides/query_data/)

Query data with Flux and InfluxQL in the InfluxDB API.

## [Write data with the InfluxDB API](/enterprise_influxdb/v1/guides/write_data/)

Use the command line interface (CLI) to write data into InfluxDB with the API.


---

## Flux data scripting language

Flux is a functional data scripting language designed for querying, analyzing, and acting on time series data. Its takes the power of [InfluxQL](/enterprise_influxdb/v1/query_language/spec/) and the functionality of [TICKscript](/kapacitor/v1/reference/tick/introduction/) and combines them into a single, unified syntax.

> Flux v0.65 is production-ready and included with \*\*InfluxDB v1 Enterprise. The InfluxDB v1.8+ implementation of Flux is read-only and does not support writing data back to InfluxDB.

## Flux design principles

Flux is designed to be usable, readable, flexible, composable, testable, contributable, and shareable. Its syntax is largely inspired by [2018’s most popular scripting language](https://insights.stackoverflow.com/survey/2018#technology), JavaScript, and takes a functional approach to data exploration and processing.

The following example illustrates pulling data from a bucket (similar to an InfluxQL database) for the last five minutes, filtering that data by the `cpu` measurement and the `cpu=cpu-total` tag, windowing the data in 1 minute intervals, and calculating the average of each window:

```js
from(bucket: "telegraf/autogen")
    |> range(start: -1h)
    |> filter(fn: (r) => r._measurement == "cpu" and r.cpu == "cpu-total")
    |> aggregateWindow(every: 1m, fn: mean)
```

### [Execute Flux queries](/enterprise_influxdb/v1/flux/execute-queries/)

Use the InfluxDB CLI, API, and the Chronograf Data Explorer to execute Flux queries.

### [Query data with Flux](/enterprise_influxdb/v1/flux/guides/)

Guides that walk through both common and complex queries and use cases for Flux.

### [Optimize Flux queries](/enterprise_influxdb/v1/flux/optimize-queries/)

Optimize your Flux queries to reduce their memory and compute (CPU) requirements.

### [Enable Flux](/enterprise_influxdb/v1/flux/installation/)

Instructions for enabling Flux in your InfluxDB configuration.

### [Flux vs InfluxQL](/enterprise_influxdb/v1/flux/flux-vs-influxql/)

Flux is an alternative to [InfluxQL](/enterprise_influxdb/v1/query_language/) and other SQL-like query languages for querying and analyzing data. Flux uses functional language patterns making it incredibly powerful, flexible, and able to overcome many of the limitations of InfluxQL. This article outlines many of the tasks possible with Flux but not InfluxQL and provides information about Flux and InfluxQL parity.

-   [Possible with Flux](#possible-with-flux)
-   [InfluxQL and Flux parity](#influxql-and-flux-parity)

## Possible with Flux

-   [Joins](#joins)
-   [Math across measurements](#math-across-measurements)
-   [Sort by tags](#sort-by-tags)
-   [Group by any column](#group-by-any-column)
-   [Window by calendar months and years](#window-by-calendar-months-and-years)
-   [Work with multiple data sources](#work-with-multiple-data-sources)
-   [DatePart-like queries](#datepart-like-queries)
-   [Pivot](#pivot)
-   [Histograms](#histograms)
-   [Covariance](#covariance)
-   [Cast booleans to integers](#cast-booleans-to-integers)
-   [String manipulation and data shaping](#string-manipulation-and-data-shaping)
-   [Work with geo-temporal data](#work-with-geo-temporal-data)

### Joins

InfluxQL has never supported joins. They can be accomplished using [TICKscript](/kapacitor/v1/reference/tick/introduction/), but even TICKscript’s join capabilities are limited. Flux’s [`join()` function](/flux/v0/stdlib/universe/join/) lets you to join data **from any bucket, any measurement, and on any columns** as long as each data set includes the columns on which they are to be joined. This opens the door for really powerful and useful operations.

### [Get started with Flux](/enterprise_influxdb/v1/flux/get-started/)

Get started with Flux, InfluxData’s new functional data scripting language. This step-by-step guide will walk you through the basics and get you on your way.


---

## InfluxDB Enterprise v1 features

InfluxDB Enterprise has additional capabilities that enhance [availability](#clustering), [scalability](#clustering), and [security](#security), and provide [eventual consistency](#eventual-consistency).

## Clustering

InfluxDB Enterprise runs on a network of independent servers, a *cluster*, to provide fault tolerance, availability, and horizontal scalability of the database.

While many InfluxDB Enterprise features are available when run with a single meta node and a single data node, this configuration does not take advantage of the clustering capability or ensure high availability.

Nodes can be added to an existing cluster to improve database performance for querying and writing data. Certain configurations (e.g., 3 meta and 2 data node) provide high-availability assurances while making certain tradeoffs in query performance when compared to a single node.

Further increasing the number of nodes can improve performance in both respects. For example, a cluster with 4 data nodes and a [replication factor](/enterprise_influxdb/v1/concepts/glossary/#replication-factor) of 2 can support a higher volume of write traffic than a single node could. It can also support a higher *query* workload, as the data is replicated in two locations. Performance of the queries may be on par with a single node in cases where the query can be answered directly by the node which receives the query.

For more information on clustering, see [Clustering in InfluxDB Enterprise](/enterprise_influxdb/v1/concepts/clustering/).

## Security

Enterprise authorization uses an expanded set of [*16 user permissions and roles*](/enterprise_influxdb/v1/features/users/). (InfluxDB OSS only has `READ` and `WRITE` permissions.) Administrators can give users permission to read and write to databases, create and remove databases, rebalance a cluster, and manage particular resources.

Organizations can automate managing permissions with the [InfluxDB Enterprise Meta API](/enterprise_influxdb/v1/administration/manage/security/authentication_and_authorization-api/).

[Fine-grained authorization](/enterprise_influxdb/v1/guides/fine-grained-authorization/) for particular data is also available.

InfluxDB Enterprise can also use [LDAP for managing authentication](/enterprise_influxdb/v1/administration/manage/security/ldap/).

For FIPS compliance, InfluxDB Enterprise password hashing algorithms are configurable.

Kapacitor OSS can also delegate its LDAP and security setup to InfluxDB Enterprise. For details, see [“Set up InfluxDB Enterprise authorizations”](/kapacitor/v1/administration/auth/influxdb-enterprise-auth/).

## Eventual consistency

### Hinted handoff

Hinted handoff (HH) is how InfluxDB Enterprise deals with data node outages while writes are happening. HH is essentially a durable disk based queue.

For more information, see [“Hinted handoff”](/enterprise_influxdb/v1/concepts/clustering/#hinted-handoff).

### Anti-entropy

Anti-entropy is an optional service to eliminate edge cases related to cluster consistency.

For more information, see [“Use Anti-Entropy service in InfluxDB Enterprise”](/enterprise_influxdb/v1/administration/anti-entropy/).

### [InfluxDB Enterprise v1 cluster features](/enterprise_influxdb/v1/features/clustering-features/)

Overview of features related to InfluxDB Enterprise v1 clustering.


---

## InfluxDB Enterprise v1 concepts

-   [InfluxDB file system layout](/enterprise_influxdb/v1/concepts/file-system-layout/)
-   [Clustering in InfluxDB Enterprise v1](/enterprise_influxdb/v1/concepts/clustering/)
-   [Compare InfluxDB to SQL databases](/enterprise_influxdb/v1/concepts/crosswalk/)
-   [Glossary](/enterprise_influxdb/v1/concepts/glossary/)
-   [In-memory indexing and the Time-Structured Merge Tree (TSM)](/enterprise_influxdb/v1/concepts/storage_engine/)
-   [InfluxDB design insights and tradeoffs](/enterprise_influxdb/v1/concepts/insights_tradeoffs/)
-   [InfluxDB Enterprise v1 startup process](/enterprise_influxdb/v1/concepts/influxdb-enterprise-startup/)
-   [InfluxDB key concepts](/enterprise_influxdb/v1/concepts/key_concepts/)
-   [InfluxDB schema design and data layout](/enterprise_influxdb/v1/concepts/schema_and_data_layout/)
-   [Time Series Index (TSI) details](/enterprise_influxdb/v1/concepts/tsi-details/)
-   [Time Series Index (TSI) overview](/enterprise_influxdb/v1/concepts/time-series-index/)


---

## Administer InfluxDB Enterprise v1

### [Identify InfluxDB Enterprise v1 version](/enterprise_influxdb/v1/administration/identify-version/)

Learn how to identify your InfluxDB Enterprise v1 version using command-line tools, HTTP endpoints, and other methods.

### [Back up and restore](/enterprise_influxdb/v1/administration/backup-and-restore/)

Back up and restore InfluxDB Enterprise v1 clusters to prevent data loss.

### [Configure](/enterprise_influxdb/v1/administration/configure/)

Configure cluster and node settings in InfluxDB Enterprise.

### [Manage](/enterprise_influxdb/v1/administration/manage/)

Manage security, clusters, and subscriptions in InfluxDB enterprise.

### [Monitor InfluxDB Enterprise v1](/enterprise_influxdb/v1/administration/monitor/)

Monitor InfluxDB Enterprise with InfluxDB Cloud or OSS.

### [Renew or update a license key or file](/enterprise_influxdb/v1/administration/renew-license/)

Renew or update a license key or file for your InfluxDB Enterprise v1 cluster.

### [Stability and compatibility](/enterprise_influxdb/v1/administration/stability_and_compatibility/)

API and storage engine compatibility and stability in InfluxDB OSS.

### [Upgrade InfluxDB Enterprise v1 clusters](/enterprise_influxdb/v1/administration/upgrading/)

Upgrade to the latest version of InfluxDB Enterprise.


---

## About the project

## [InfluxDB Enterprise v1 release notes](/enterprise_influxdb/v1/about-the-project/release-notes/)

Important changes and what’s new in each version InfluxDB Enterprise v1.

## [Third party software](/enterprise_influxdb/v1/about-the-project/third-party/)

InfluxData products contain third-party software that is copyrighted, patented, or otherwise legally protected software of third parties incorporated in InfluxData products.

## Commercial license

InfluxDB Enterprise is available with a commercial license. [Contact sales for more information](https://www.influxdata.com/contact-sales/).

