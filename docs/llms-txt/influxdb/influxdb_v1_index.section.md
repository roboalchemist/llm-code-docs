---
title: InfluxDB OSS v1 documentation
description: Overview of documentation available for InfluxDB.
url: https://docs.influxdata.com/influxdb/v1/
product: InfluxDB OSS v1
type: section
pages: 13
estimated_tokens: 8556
child_pages:
  - url: https://docs.influxdata.com/influxdb/v1/write_protocols/
    title: Write protocols in InfluxDB
  - url: https://docs.influxdata.com/influxdb/v1/troubleshooting/
    title: Troubleshoot InfluxDB
  - url: https://docs.influxdata.com/influxdb/v1/tools/
    title: InfluxDB tools
  - url: https://docs.influxdata.com/influxdb/v1/supported_protocols/
    title: Supported protocols in InfluxDB
  - url: https://docs.influxdata.com/influxdb/v1/introduction/
    title: Learn about InfluxDB OSS 1.x
  - url: https://docs.influxdata.com/influxdb/v1/query_language/
    title: Influx Query Language (InfluxQL)
  - url: https://docs.influxdata.com/influxdb/v1/high_availability/
    title: High availability with InfluxDB
  - url: https://docs.influxdata.com/influxdb/v1/guides/
    title: InfluxDB guides
  - url: https://docs.influxdata.com/influxdb/v1/flux/
    title: Flux data scripting language
  - url: https://docs.influxdata.com/influxdb/v1/concepts/
    title: InfluxDB concepts
  - url: https://docs.influxdata.com/influxdb/v1/administration/
    title: Administer InfluxDB
  - url: https://docs.influxdata.com/influxdb/v1/about_the_project/
    title: About InfluxDB OSS
---

# InfluxDB OSS v1 documentation

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

InfluxDB is a [time series database](https://www.influxdata.com/time-series-database/) designed to handle high write and query loads. InfluxDB OSS v1 is purpose-built to handle any use case involving large amounts of timestamped data and is an integral component of the [TICK stack](https://influxdata.com/time-series-platform/).

Common use cases include:

- Infrastructure and DevOps monitoring
- Application metrics and performance monitoring
- IoT sensor data collection
- Real-time analytics
- Events handling

## InfluxDB Cloud 1 users

**InfluxDB Cloud 1** (InfluxCloud 1.x) is based on InfluxDB Enterprise v1. Use the [Enterprise v1 documentation](/enterprise_influxdb/v1/) instead.

- **InfluxDB Cloud 1 Support**: [help.influxcloud.net](https://help.influxcloud.net)
- **Migrate**: Consider [migrating to InfluxDB 3](/platform/#migration-to-influxdb-3) (Enterprise, Cloud Serverless, or Cloud Dedicated) with v1 API compatibility

## Key features

InfluxDB v1.12 supports the following features for working with time series data.

- Custom high performance datastore written specifically for time series data. The TSM engine allows for high ingest speed and data compression
- Written entirely in Go. It compiles into a single binary with no external dependencies.
- Simple, high performing write and query HTTP APIs.
- Plugins support for other data ingestion protocols such as Graphite, collectd, and OpenTSDB.
- Expressive SQL-like query language tailored to easily query aggregated data.
- Tags allow series to be indexed for fast and efficient queries.
- Retention policies efficiently auto-expire stale data.
- Continuous queries automatically compute aggregate data to make frequent queries more efficient.

InfluxDB OSS v1 runs on a single node. If you require high availability to eliminate a single point of failure, consider [InfluxDB 3 Enterprise](/influxdb3/enterprise/), InfluxDB's next generation that supports multi-node clustering, allows infinite series cardinality without impact on overall database performance, and brings native SQL support and improved InfluxQL performance.

---

## Write protocols in InfluxDB

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

The InfluxDB line protocol is a text based format for writing points to InfluxDB databases.

## [InfluxDB line protocol reference](/influxdb/v1/write_protocols/line_protocol_reference/)

InfluxDB line protocol is a text-based format for writing points to InfluxDB.

## [InfluxDB line protocol tutorial](/influxdb/v1/write_protocols/line_protocol_tutorial/)

Tutorial for using InfluxDB line protocol.

---

## Troubleshoot InfluxDB

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

## [InfluxDB error messages](/influxdb/v1/troubleshooting/errors/)

Covers InfluxDB error messages, their descriptions, and common resolutions.

## [InfluxDB frequently asked questions](/influxdb/v1/troubleshooting/frequently-asked-questions/)

Common issues with InfluxDB OSS.

## [InfluxQL query management](/influxdb/v1/troubleshooting/query_management/)

Show, kill, and manage queries in InfluxQL.

## [systemd permission errors](/influxdb/v1/troubleshooting/systemd/)

Troubleshoot errors with InfluxDB and systemd permissions

---

## InfluxDB tools

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

### Flux VS Code extension no longer available

The `vsflux` extension is no longer available in the Visual Studio Marketplace. `vsflux` and the `flux-lsp` Flux Language Server Protocol plugin are no longer maintained. Their repositories have been archived and are no longer receiving updates.

This section covers the available tools for interacting with InfluxDB.

## `influx` command line interface (CLI)

The [InfluxDB command line interface (`influx`)](/influxdb/v1/tools/influx-cli/) includes commands to manage many aspects of InfluxDB, including databases, organizations, users, and tasks.

## `influxd` command

The [`influxd` command](/influxdb/v1/tools/influxd) starts and runs all the processes necessary for InfluxDB to function.

## InfluxDB API client libraries

The list of [client libraries](/influxdb/v1/tools/api_client_libraries/) for interacting with the InfluxDB API.

## Influx Inspect disk shard utility

[Influx Inspect](/influxdb/v1/tools/influx_inspect/) is a tool designed to view detailed information about on disk shards, as well as export data from a shard to line protocol that can be inserted back into the database.

## InfluxDB inch tool

Use the [InfluxDB `inch` tool](/influxdb/v1/tools/inch/) to test InfluxDB performance. Adjust metrics such as the batch size, tag values, and concurrent write streams to test how ingesting different tag cardinalities and metrics affects performance.

## Graphs and dashboards

Use [Chronograf](/chronograf/v1/) or [Grafana](https://grafana.com/docs/grafana/latest/features/datasources/influxdb/) dashboards to visualize your time series data.

> **Tip:** Use template variables in your dashboards to filter meta query results by a specified period of time (see example below).

### Filter meta query results using template variables

The example below shows how to filter hosts retrieving data in the past hour.

#### Example

```sh
# Create a retention policy.
CREATE RETENTION POLICY "lookup" ON "prod" DURATION 1d REPLICATION 1

# Create a continuous query that groups by the tags you want to use in your template variables.
CREATE CONTINUOUS QUERY "lookupquery" ON "prod" BEGIN SELECT mean(value) as value INTO "your.system"."host_info" FROM "cpuload"
WHERE time > now() - 1h GROUP BY time(1h), host, team, status, location END;

# In your Grafana or Chronograf templates, include your tag values.
SHOW TAG VALUES FROM "your.system"."host_info" WITH KEY = “host”
```

> **Note:** In Chronograf, you can also filter meta query results for a specified time range by [creating a `custom meta query` template variable](/chronograf/v1/guides/dashboard-template-variables/#create-custom-template-variables) and adding a time range filter.

## Flux tools

### vsflux and Flux-LSP no longer maintained

The `vsflux` Flux VS Code extension and the `flux-lsp` language server plugin for Vim are no longer maintained. Their repositories have been archived and are no longer receiving updates. `vsflux` is no longer available in the Visual Studio Marketplace.

---

## Supported protocols in InfluxDB

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

InfluxData supports the following protocols for interacting with InfluxDB:

### [CollectD protocol support in InfluxDB](/influxdb/v1/supported_protocols/collectd/)

The collectd input allows InfluxDB to accept data transmitted in collectd native format.

### [Graphite protocol support in InfluxDB](/influxdb/v1/supported_protocols/graphite/)

Use the Graphite plugin to write data to InfluxDB using the Graphite protocol.

### [OpenTSDB protocol support in InfluxDB](/influxdb/v1/supported_protocols/opentsdb/)

Use the OpenTSDB plugin to write data to InfluxDB using the OpenTSDB protocol.

### [Prometheus endpoints support in InfluxDB](/influxdb/v1/supported_protocols/prometheus/)

Read and write Prometheus data in InfluxDB.

### [UDP protocol support in InfluxDB](/influxdb/v1/supported_protocols/udp/)

Overview of support for UDP protocol in InfluxDB.

---

## Learn about InfluxDB OSS 1.x

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

To get up and running with InfluxDB OSS v1.12, complete the following:

## [Download InfluxDB OSS v1](/influxdb/v1/introduction/download/)

Download the latest InfluxDB open source (OSS) release at the [InfluxData Downloads page](https://www.influxdata.com/downloads/).

1. Scroll to the bottom of the [downloads page](https://www.influxdata.com/downloads/) and click **2** to navigate to the second page of products.
2. Under **InfluxDB OSS 1.x**, select:
   - your **Platform** (operating system) and
   - the **Version** of InfluxDB you want to download.
3. Run the provided commands to download and install InfluxDB.

## [Get started with InfluxDB OSS v1](/influxdb/v1/introduction/get-started/)

Get started with InfluxDB OSS v1.12. Learn how to create databases, write data, and query your time series data.

## [Install and run InfluxDB using Docker](/influxdb/v1/introduction/install/docker/)

Install and run InfluxDB OSS v1.12 using Docker. Configure and operate InfluxDB in a Docker container.

## [Install InfluxDB OSS v1](/influxdb/v1/introduction/install/)

Install, start, and configure InfluxDB OSS v1.12.

---

## Influx Query Language (InfluxQL)

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

This section introduces InfluxQL, the InfluxDB SQL-like query language for working with data in InfluxDB databases.

## InfluxQL Reference

The [reference documentation for InfluxQL](/influxdb/v1/query_language/spec/).

## InfluxQL tutorial

The first seven documents in this section provide a tutorial-style introduction to InfluxQL. Feel free to download the dataset provided in [Sample Data](/influxdb/v1/query_language/data_download/) and follow along with the documentation.

### Data exploration

[Data exploration](/influxdb/v1/query_language/explore-data/) covers the query language basics for InfluxQL, including the [`SELECT` statement](/influxdb/v1/query_language/explore-data/#the-basic-select-statement), [`GROUP BY` clauses](/influxdb/v1/query_language/explore-data/#the-group-by-clause), [`INTO` clauses](/influxdb/v1/query_language/explore-data/#the-into-clause), and more. See Data Exploration to learn about [time syntax](/influxdb/v1/query_language/explore-data/#time-syntax) and [regular expressions](/influxdb/v1/query_language/explore-data/#regular-expressions) in queries.

### Schema exploration

[Schema exploration](/influxdb/v1/query_language/explore-schema/) covers queries that are useful for viewing and exploring your [schema](/influxdb/v1/concepts/glossary/#schema). See Schema Exploration for syntax explanations and examples of InfluxQL's `SHOW` queries.

### Database management

[Database management](/influxdb/v1/query_language/manage-database/) covers InfluxQL for managing [databases](/influxdb/v1/concepts/glossary/#database) and [retention policies](/influxdb/v1/concepts/glossary/#retention-policy-rp) in InfluxDB. See Database Management for creating and dropping databases and retention policies as well as deleting and dropping data.

### InfluxQL functions

Covers all [InfluxQL functions](/influxdb/v1/query_language/functions/).

### InfluxQL Continuous Queries

[InfluxQL Continuous Queries](/influxdb/v1/query_language/continuous_queries/) covers the [basic syntax](/influxdb/v1/query_language/continuous_queries/#basic-syntax) , [advanced syntax](/influxdb/v1/query_language/continuous_queries/#advanced-syntax) , and [common use cases](/influxdb/v1/query_language/continuous_queries/#continuous-query-use-cases) for [Continuous Queries](/influxdb/v1/concepts/glossary/#continuous-query-cq). This page also describes how to [`SHOW`](/influxdb/v1/query_language/continuous_queries/#listing-continuous-queries) and [`DROP`](/influxdb/v1/query_language/continuous_queries/#deleting-continuous-queries) Continuous Queries.

### InfluxQL mathematical operators

[InfluxQL mathematical operators](/influxdb/v1/query_language/math_operators/) covers the use of mathematical operators in InfluxQL.

### Authentication and authorization

[Authentication and authorization](/influxdb/v1/administration/authentication_and_authorization/) covers how to [set up authentication](/influxdb/v1/administration/authentication_and_authorization/#set-up-authentication) and how to [authenticate requests](/influxdb/v1/administration/authentication_and_authorization/#authenticate-requests) in InfluxDB. This page also describes the different [user types](/influxdb/v1/administration/authentication_and_authorization/#user-types-and-privileges) and the InfluxQL for [managing database users](/influxdb/v1/administration/authentication_and_authorization/#user-management-commands).

## InfluxQL reference

The [reference documentation for InfluxQL](/influxdb/v1/query_language/spec/).

---

## High availability with InfluxDB

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

InfluxDB OSS 1.12 does **not** support clustering. For high availability or horizontal scaling of InfluxDB, use the commercial clustered offering, [InfluxDB Enterprise](/enterprise_influxdb/v1/).

- For information about creating an InfluxDB Enterprise cluster, see [Install an InfluxDB Enterprise cluster](/enterprise_influxdb/v1/introduction/installation/).
- To learn more about high availability clustering, see [Clustering in InfluxDB Enterprise](/enterprise_influxdb/v1/concepts/clustering/).

## Related

- [Install an InfluxDB Enterprise v1 cluster](/enterprise_influxdb/v1/introduction/installation/)
- [Clustering in InfluxDB Enterprise v1](/enterprise_influxdb/v1/concepts/clustering/)

---

## InfluxDB guides

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

- [Calculate percentages in a query](/influxdb/v1/guides/calculate_percentages/)
- [Downsample and retain data](/influxdb/v1/guides/downsample_and_retain/)
- [Hardware sizing guidelines](/influxdb/v1/guides/hardware_sizing/)
- [Migrate from InfluxDB OSS to InfluxDB Enterprise](/influxdb/v1/guides/migrate-to-enterprise/)
- [Query data with the InfluxDB API](/influxdb/v1/guides/query_data/)
- [Write data with the InfluxDB API](/influxdb/v1/guides/write_data/)

---

## Flux data scripting language

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

Flux is a functional data scripting language designed for querying, analyzing, and acting on time series data. It takes the power of [InfluxQL](/influxdb/v1/query_language/spec/) and the functionality of [TICKscript](/kapacitor/v1/reference/tick/introduction/) and combines them into a single, unified syntax.

> Flux is production-ready and included with [InfluxDB v1.8+](/influxdb/v1/).

## Flux design principles

Flux is designed to be usable, readable, flexible, composable, testable, contributable, and shareable. Its syntax is largely inspired by [2018’s most popular scripting language](https://insights.stackoverflow.com/survey/2018#technology), JavaScript, and takes a functional approach to data exploration and processing.

The following example illustrates pulling data from a bucket (similar to an InfluxQL database) for the last five minutes, filtering that data by the `cpu` measurement and the `cpu=cpu-total` tag, windowing the data in 1 minute intervals, and calculating the average of each window:

```js
from(bucket:"telegraf/autogen")
  |> range(start:-1h)
  |> filter(fn:(r) =>
    r._measurement == "cpu" and
    r.cpu == "cpu-total"
  )
  |> aggregateWindow(every: 1m, fn: mean)
```

### [Query data with Flux](/influxdb/v1/flux/guides/)

Guides that walk through both common and complex queries and use cases for Flux.

### [Enable Flux](/influxdb/v1/flux/installation/)

Instructions for enabling Flux in your InfluxDB configuration.

### [Flux vs InfluxQL](/influxdb/v1/flux/flux-vs-influxql/)

Flux is an alternative to [InfluxQL](/influxdb/v1/query_language/) and other SQL-like query languages for querying and analyzing data. Flux uses functional language patterns making it incredibly powerful, flexible, and able to overcome many of the limitations of InfluxQL. This article outlines many of the tasks possible with Flux but not InfluxQL and provides information about Flux and InfluxQL parity.

- [Possible with Flux](#possible-with-flux)
- [InfluxQL and Flux parity](#influxql-and-flux-parity)

## Possible with Flux

- [Joins](#joins)
- [Math across measurements](#math-across-measurements)
- [Sort by tags](#sort-by-tags)
- [Group by any column](#group-by-any-column)
- [Window by calendar months and years](#window-by-calendar-months-and-years)
- [Work with multiple data sources](#work-with-multiple-data-sources)
- [DatePart-like queries](#datepart-like-queries)
- [Pivot](#pivot)
- [Histograms](#histograms)
- [Covariance](#covariance)
- [Cast booleans to integers](#cast-booleans-to-integers)
- [String manipulation and data shaping](#string-manipulation-and-data-shaping)
- [Work with geo-temporal data](#work-with-geo-temporal-data)

### Joins

InfluxQL has never supported joins. They can be accomplished using [TICKscript](/kapacitor/v1/reference/tick/introduction/), but even TICKscript’s join capabilities are limited. Flux’s [`join()` function](/flux/v0/stdlib/universe/join/) allows you to join data **from any bucket, any measurement, and on any columns** as long as each data set includes the columns on which they are to be joined. This opens the door for really powerful and useful operations.

### [Get started with Flux](/influxdb/v1/flux/get-started/)

Get started with Flux, InfluxData's new functional data scripting language. This step-by-step guide will walk you through the basics and get you on your way.

---

## InfluxDB concepts

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

Understanding the following concepts will help you get the most out of InfluxDB.

## [InfluxDB file system layout](/influxdb/v1/concepts/file-system-layout/)

The InfluxDB file system layout depends on the operating system, package manager, or containerization platform used to install InfluxDB.

## [Compare InfluxDB to SQL databases](/influxdb/v1/concepts/crosswalk/)

Differences between InfluxDB and SQL databases.

## [In-memory indexing and the Time-Structured Merge Tree (TSM)](/influxdb/v1/concepts/storage_engine/)

InfluxDB storage engine, in-memory indexing, and the Time-Structured Merge Tree (TSM) in InfluxDB OSS.

## [InfluxDB design insights and tradeoffs](/influxdb/v1/concepts/insights_tradeoffs/)

Optimizing for time series use case entails some tradeoffs, primarily to increase performance at the cost of functionality.

## [InfluxDB glossary](/influxdb/v1/concepts/glossary/)

Terms related to InfluxDB OSS.

## [InfluxDB key concepts](/influxdb/v1/concepts/key_concepts/)

Covers key concepts to learn about InfluxDB.

## [InfluxDB schema design and data layout](/influxdb/v1/concepts/schema_and_data_layout/)

Improve InfluxDB schema design and data layout to reduce high cardinality and make your data more performant.

## [Time Series Index (TSI) details](/influxdb/v1/concepts/tsi-details/)

Enable and understand the Time Series Index (TSI).

## [Time Series Index (TSI) overview](/influxdb/v1/concepts/time-series-index/)

The Time Series Index (TSI) storage engine supports high cardinality in time series data.

---

## Administer InfluxDB

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

The administration documentation contains all the information needed to administer a working InfluxDB installation.

## [Identify InfluxDB OSS v1 version](/influxdb/v1/administration/identify-version/)

Learn how to identify your InfluxDB OSS v1 version using command-line tools, HTTP endpoints, and other methods.

## [Authentication and authorization in InfluxDB](/influxdb/v1/administration/authentication_and_authorization/)

Set up and manage authentication and authorization in InfluxDB OSS.

## [Back up and restore data](/influxdb/v1/administration/backup_and_restore/)

To prevent unexpected data loss, back up and restore InfluxDB OSS instances.

## [Compact a series file offline](/influxdb/v1/administration/compact-series-file/)

Use the `influx_inspect buildtsi -compact-series-file` command to compact your series file and reduce its size on disk.

## [Configure InfluxDB OSS](/influxdb/v1/administration/config/)

Learn about InfluxDB OSS configuration settings and environment variables.

## [Enable HTTPS with InfluxDB](/influxdb/v1/administration/https_setup/)

Enable HTTPS and Transport Security Layer (TLS) secure communication between clients and your InfluxDB servers.

## [InfluxDB ports](/influxdb/v1/administration/ports/)

Enabled and disabled ports in InfluxDB.

## [Log and trace with InfluxDB](/influxdb/v1/administration/logs/)

Structured logging, access logging, tracing, and logging locations in InfluxDB.

## [Manage InfluxDB security](/influxdb/v1/administration/security/)

Protect the data in your InfluxDB OSS instance.

## [Manage subscriptions in InfluxDB](/influxdb/v1/administration/subscription-management/)

Manage subscriptions, which copy all written data to a local or remote endpoint, in InfluxDB OSS.

## [Monitor InfluxDB servers](/influxdb/v1/administration/server_monitoring/)

Troubleshoot and monitor InfluxDB OSS.

## [Rebuild the TSI index](/influxdb/v1/administration/rebuild-tsi-index/)

Use the `influxd_inspect buildtsi` command to rebuild your InfluxDB TSI index.

## [Stability and compatibility](/influxdb/v1/administration/stability_and_compatibility/)

API and storage engine compatibility and stability in InfluxDB OSS.

## [Upgrade to InfluxDB 1.11.x](/influxdb/v1/administration/upgrading/)

Upgrade to the latest version of InfluxDB.

## Downgrade

To revert to a prior version, complete the same steps as when [Upgrading to InfluxDB 1.11.x](/influxdb/v1/administration/upgrading/), replacing 1.11.x with the version you want to downgrade to. After downloading the release, migrating your configuration settings, and enabling TSI or TSM, make sure to [rebuild your index](/influxdb/v1/administration/rebuild-tsi-index).

> **Note:** Some versions of InfluxDB may have breaking changes that impact your ability to upgrade and downgrade. For example, you cannot downgrade from InfluxDB 1.3 or later to an earlier version. Please review the applicable version of release notes to check for compatibility issues between releases.

---

## About InfluxDB OSS

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

## [Contribute to InfluxDB OSS](/influxdb/v1/about_the_project/contributing/)

Contribute to the InfluxDB OSS project.

## [InfluxData Contributor License Agreement (CLA)](/influxdb/v1/about_the_project/cla/)

Before contributing to the InfluxDB OSS project, you must complete and sign the [InfluxData Contributor License Agreement (CLA)](https://www.influxdata.com/legal/cla/), available on the InfluxData website.

## [InfluxDB v1 release notes](/influxdb/v1/about_the_project/release-notes/)

Important features, fixes, and updates in each version of InfluxDB OSS v1.

## [Open source license for InfluxDB](/influxdb/v1/about_the_project/licenses/)

The [open source license for InfluxDB](https://github.com/influxdata/influxdb/blob/master/LICENSE) is available in the GitHub repository.

## [Third party software](/influxdb/v1/about_the_project/third-party/)

InfluxData products contain third party software, which means the copyrighted, patented, or otherwise legally protected software of third parties that is incorporated in InfluxData products.

Third party suppliers make no representation nor warranty with respect to such third party software or any portion thereof. Third party suppliers assume no liability for any claim that might arise with respect to such third party software, nor for a customer's use of or inability to use the third party software.
