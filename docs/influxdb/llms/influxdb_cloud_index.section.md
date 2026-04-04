---
title: Get started with InfluxDB Cloud
description: InfluxDB Cloud is a hosted and managed version of InfluxDB v2.0, the time series platform designed to handle high write and query loads. Learn how to use and leverage InfluxDB Cloud in use cases such as monitoring metrics, IoT data, and events.
url: https://docs.influxdata.com/influxdb/cloud/
product: InfluxDB Cloud (TSM)
type: section
pages: 16
estimated_tokens: 15127
child_pages:
  - url: https://docs.influxdata.com/influxdb/cloud/write-data/
    title: Write data to InfluxDB
  - url: https://docs.influxdata.com/influxdb/cloud/visualize-data/
    title: Visualize data with the InfluxDB UI
  - url: https://docs.influxdata.com/influxdb/cloud/upgrade/
    title: Upgrade to InfluxDB Cloud
  - url: https://docs.influxdata.com/influxdb/cloud/tools/
    title: InfluxDB tools and integrations
  - url: https://docs.influxdata.com/influxdb/cloud/tags/
    title: Tags and related content
  - url: https://docs.influxdata.com/influxdb/cloud/sign-up/
    title: Sign up for InfluxDB Cloud
  - url: https://docs.influxdata.com/influxdb/cloud/reference/
    title: InfluxDB reference
  - url: https://docs.influxdata.com/influxdb/cloud/query-data/
    title: Query data in InfluxDB
  - url: https://docs.influxdata.com/influxdb/cloud/process-data/
    title: Process data with InfluxDB tasks
  - url: https://docs.influxdata.com/influxdb/cloud/monitor-alert/
    title: Monitor data and send alerts
  - url: https://docs.influxdata.com/influxdb/cloud/migrate-regions/
    title: Migrate to an account in a new region
  - url: https://docs.influxdata.com/influxdb/cloud/get-started/
    title: Get started with InfluxDB Cloud
  - url: https://docs.influxdata.com/influxdb/cloud/api-guide/
    title: Develop with the InfluxDB API
  - url: https://docs.influxdata.com/influxdb/cloud/admin/
    title: Administer InfluxDB Cloud
  - url: https://docs.influxdata.com/influxdb/cloud/account-management/
    title: Manage your InfluxDB Cloud Account
---




---

## Write data to InfluxDB

To explore InfluxDB using existing data (*without writing your own data*), see how to [add sample data](/influxdb/cloud/query-data/execute-queries/query-sample-data/#add-sample).

1. Learn the [best practices](/influxdb/cloud/write-data/best-practices/) for writing data.
2. (Optional) Migrate a large amount of historical data, by [writing data in bulk](/influxdb/cloud/write-data/bulk-ingest-cloud/).
3. Discover how to write data [without coding](/influxdb/cloud/write-data/no-code), by [loading data source in the UI](/influxdb/cloud/write-data/no-code/load-data/), or using [developer tools](/influxdb/cloud/write-data/developer-tools).
4. Do any of the following:
   - [Troubleshoot the most common issues writing data](/influxdb/cloud/write-data/troubleshoot/)
   - [Delete data you no longer need](/influxdb/cloud/write-data/delete-data/)
   - [Query and explore data](/influxdb/cloud/query-data/)
   - [Process data](/influxdb/cloud/process-data/)
   - [Visualize data](/influxdb/cloud/visualize-data/)
   - [Monitor and alert](/influxdb/cloud/monitor-alert/)

The following video discusses different ways to write data to InfluxDB:

### Related

- [InfluxDB v1 API /write endpoint](/influxdb/cloud/api/#tag/Write)
- [Line protocol](/influxdb/cloud/reference/syntax/line-protocol/)
- [Annotated CSV](/influxdb/cloud/reference/syntax/annotated-csv/)
- [influx write](/influxdb/cloud/reference/cli/influx/write/)
- [How to Ingest Data in InfluxDB (Video)](/resources/videos/ingest-data/)

[write](/influxdb/cloud/tags/write/) [line protocol](/influxdb/cloud/tags/line-protocol/)

---

## Visualize data with the InfluxDB UI

The InfluxDB user interface (UI) provides tools for building custom dashboards to visualize your data. The following articles outline ways to customize and manage dashboards.

### [Explore metrics with InfluxDB](/influxdb/cloud/visualize-data/explore-metrics/)

Explore and visualize your data in InfluxDB’s Data Explorer. The InfluxDB user interface (UI) allows you to move seamlessly between using the Flux builder and manually editing the query.

### [Manage InfluxDB dashboards](/influxdb/cloud/visualize-data/dashboards/)

Create, edit, and manage custom dashboards in the InfluxDB user interface (UI).

### [Use and manage variables](/influxdb/cloud/visualize-data/variables/)

Dashboard variables allow you to alter specific components of cells’ queries without having to edit the queries, making it easy to interact with your dashboard cells and explore your data.

### [Manage labels in the InfluxDB UI](/influxdb/cloud/visualize-data/labels/)

Labels are a way to add visual metadata to dashboards, tasks, and other items in the InfluxDB UI. View and manage labels in the InfluxDB user interface.

### [Use annotations in dashboards](/influxdb/cloud/visualize-data/annotations/)

Add annotations to your InfluxDB dashboards to provide useful, contextual information about single points in time.

### [Visualization types](/influxdb/cloud/visualize-data/visualization-types/)

The InfluxDB UI provides multiple visualization types to visualize your data in a format that makes the most sense for your use case. Use the available customization options to customize each visualization.

[visualize](/influxdb/cloud/tags/visualize/)

---

## Upgrade to InfluxDB Cloud

Upgrade to InfluxDB Cloud from InfluxDB 1.x and 2.x:

### [Upgrade from InfluxDB 1.x to InfluxDB Cloud](/influxdb/cloud/upgrade/v1-to-cloud/)

To upgrade from InfluxDB 1.x to InfluxDB Cloud, migrate data, and then create database and retention policy (DBRP) mappings.

### [Upgrade from InfluxDB OSS 2.x to InfluxDB Cloud](/influxdb/cloud/upgrade/v2-to-cloud/)

To upgrade from Influx 2.x to InfluxDB Cloud, create a new InfluxDB Cloud account, migrate resources, time series data, and more.

---

## InfluxDB tools and integrations

### Flux VS Code extension no longer available

The `vsflux` extension is no longer available in the Visual Studio Marketplace. `vsflux` and the `flux-lsp` Flux Language Server Protocol plugin are no longer maintained. Their repositories have been archived and are no longer receiving updates.

### [Telegraf configurations](/influxdb/cloud/tools/telegraf-configs/)

InfluxDB Cloud lets you automatically generate Telegraf configurations or upload customized Telegraf configurations that collect metrics and write them to InfluxDB Cloud.

### [Notebooks](/influxdb/cloud/tools/notebooks/)

Use notebooks to build and annotate processes and data flows for time series data.

### [InfluxDB templates](/influxdb/cloud/tools/influxdb-templates/)

InfluxDB templates are prepackaged InfluxDB configurations that contain everything from dashboards and Telegraf configurations to notifications and alerts.

### [Install and use the influx CLI](/influxdb/cloud/tools/influx-cli/)

Use the `influx` command line interface to interact with and manage InfluxDB Cloud.

### [Use the Interactive Flux REPL](/influxdb/cloud/tools/flux-repl/)

Use the Flux REPL (Read–Eval–Print Loop) to execute Flux scripts and interact with InfluxDB and other data sources.

### [Use the InfluxQL shell](/influxdb/cloud/tools/influxql-shell/)

Use the InfluxQL interactive shell to execute InfluxQL queries and interact with InfluxDB.

### [Use the Flux LSP with Vim](/influxdb/cloud/tools/flux-vim-lsp/)

Use the Flux LSP with Vim to add auto-completion, syntax checking, and other language-specific features to your editor.

### [Use Grafana with InfluxDB Cloud](/influxdb/cloud/tools/grafana/)

Use [Grafana](https://grafana.com/) to visualize data from your **InfluxDB Cloud** instance.

### [Use Chronograf with InfluxDB Cloud](/influxdb/cloud/tools/chronograf/)

Chronograf is a data visualization and dashboarding tool designed to visualize data in InfluxDB 1.x. It is part of the [TICKstack](/platform/) that provides an InfluxQL data explorer, Kapacitor integrations, and more. Continue to use Chronograf with **InfluxDB Cloud** and **InfluxDB OSS 2.0** and the [1.x compatibility API](/influxdb/v2/reference/api/influxdb-1x/).

### [Use Kapacitor with InfluxDB Cloud](/influxdb/cloud/tools/kapacitor/)

[Kapacitor](/kapacitor/) is a data processing framework that makes it easy to create alerts, run ETL (Extract, Transform and Load) jobs and detect anomalies. Use Kapacitor with **InfluxDB Cloud**.

### [Use Postman with the InfluxDB API](/influxdb/cloud/tools/postman/)

Use [Postman](https://www.postman.com/), a popular tool for exploring APIs, to interact with the [InfluxDB API](/influxdb/cloud/api-guide/).

### [Use ThingWorx with InfluxDB Cloud](/influxdb/cloud/tools/thingworx/)

Connect [ThingWorx](https://www.ptc.com/en/products/thingworx) with your **InfluxDB Cloud** instance.

### [Use the InfluxDB documentation MCP server](/influxdb/cloud/tools/mcp-server/)

Query InfluxDB Cloud (TSM) documentation from your IDE using the InfluxDB documentation MCP server.

---

## Tags and related content

- [aggregates](aggregates) (2)
- [ai](ai) (1)
- [alert](alert) (5)
- [alerts](alerts) (1)
- [annotations](annotations) (1)
- [api](api) (8)
- [api guides](api-guides) (1)
- [authentication](authentication) (3)
- [authorization](authorization) (7)
- [backup](backup) (1)
- [backups](backups) (1)
- [best practices](best-practices) (7)
- [bucket schemas](bucket-schemas) (1)
- [bucket-schema](bucket-schema) (2)
- [buckets](buckets) (5)
- [check](check) (1)
- [checks](checks) (3)
- [cli](cli) (6)
- [client libraries](client-libraries) (7)
- [conditionals](conditionals) (1)
- [config](config) (1)
- [counters](counters) (1)
- [csv](csv) (2)
- [cumulative sum](cumulative-sum) (1)
- [custom](custom) (2)
- [dashboards](dashboards) (5)
- [dbrp](dbrp) (6)
- [delete](delete) (3)
- [design principles](design-principles) (1)
- [email](email) (1)
- [endpoints](endpoints) (2)
- [errors](errors) (1)
- [exists](exists) (1)
- [explicit bucket schemas](explicit-bucket-schemas) (1)
- [fill](fill) (1)
- [flux](flux) (17)
- [functions](functions) (2)
- [get-started](get-started) (4)
- [glossary](glossary) (1)
- [go](go) (1)
- [grafana](grafana) (1)
- [group](group) (1)
- [health](health) (1)
- [histogram](histogram) (1)
- [iiot](iiot) (1)
- [increase](increase) (1)
- [influx](influx) (1)
- [influxql](influxql) (6)
- [infrastructure](infrastructure) (1)
- [install](install) (1)
- [internals](internals) (3)
- [javascript](javascript) (5)
- [join](join) (1)
- [key concepts](key-concepts) (4)
- [labels](labels) (2)
- [limit](limit) (1)
- [line protocol](line-protocol) (3)
- [llm](llm) (1)
- [logs](logs) (1)
- [manually](manually) (1)
- [math](math) (1)
- [mcp](mcp) (1)
- [median](median) (1)
- [monitor](monitor) (10)
- [moving average](moving-average) (1)
- [mqtt](mqtt) (1)
- [networking](networking) (1)
- [networks](networks) (1)
- [nodejs](nodejs) (3)
- [notebooks](notebooks) (3)
- [notification](notification) (1)
- [notifications](notifications) (4)
- [organizations](organizations) (2)
- [percentile](percentile) (1)
- [persistence provider](persistence-provider) (1)
- [ping](ping) (1)
- [plugin](plugin) (1)
- [prometheus](prometheus) (2)
- [ptc](ptc) (1)
- [python](python) (2)
- [quantile](quantile) (1)
- [queries](queries) (5)
- [query](query) (28)
- [rate](rate) (1)
- [regex](regex) (1)
- [replication](replication) (10)
- [restore](restore) (1)
- [scalar](scalar) (1)
- [schema](schema) (3)
- [scripts](scripts) (1)
- [secrets](secrets) (10)
- [security](security) (9)
- [select](select) (1)
- [sort](sort) (1)
- [sql](sql) (1)
- [states](states) (1)
- [syntax](syntax) (6)
- [tasks](tasks) (8)
- [telegraf](telegraf) (3)
- [templates](templates) (15)
- [thingworx](thingworx) (1)
- [tokens](tokens) (1)
- [tools](tools) (1)
- [transform](transform) (1)
- [users](users) (1)
- [variables](variables) (8)
- [visualize](visualize) (1)
- [where](where) (1)
- [write](write) (28)

---

## Sign up for InfluxDB Cloud

InfluxDB Cloud (TSM) is a fully managed and hosted version of InfluxDB 2.x, designed to collect, store, process, and visualize metrics and events.

### New InfluxDB Cloud signups use InfluxDB 3

New InfluxDB Cloud signups are for [InfluxDB Cloud Serverless, powered by the InfluxDB 3 storage engine](/influxdata/cloud-serverless/).

If you are looking to use InfluxDB v2 (TSM), consider self-hosting [InfluxDB OSS v2](/influxdata/v2/).

InfluxDB Cloud (TSM) is API-compatible and functionally compatible with InfluxDB OSS v2.

The primary differences between InfluxDB OSS v2 and InfluxDB Cloud are:

- [InfluxDB scrapers](/influxdb/v2/write-data/no-code/scrape-data/) that collect data from specified targets are not available in InfluxDB Cloud.
- InfluxDB Cloud instances are currently limited to a single organization.
- [Start for free](#start-for-free)
- [Sign up](#sign-up)
- [(Optional) Download, install, and use the influx CLI](#optional-download-install-and-use-the-influx-cli)
- [Sign in](#sign-in)
- [Get started working with data](#get-started-working-with-data)

### Other deployment options

- **InfluxDB OSS v2 (single-node, self-hosted)**: Available for on-premises setups.
- **InfluxDB Cloud Serverless**: Managed, multi-tenant InfluxDB Cloud 3 instance.
- **InfluxDB Cloud Dedicated**: Managed, single-tenant InfluxDB Cloud 3 cluster.

## Sign up

### New InfluxDB Cloud signups use InfluxDB 3

New InfluxDB Cloud signups are for [InfluxDB Cloud Serverless, powered by the InfluxDB 3 storage engine](/influxdata/cloud-serverless/).

If you are looking to use InfluxDB v2 (TSM), consider self-hosting [InfluxDB OSS v2](/influxdata/v2/).

## (Optional) Download, install, and use the influx CLI

To use the `influx` CLI to manage and interact with your InfluxDB Cloud instance, complete the following steps:

<!-- Tabbed content: Select one of the following options -->

**macOS:**

### Step 1: Download influx CLI for macOS

Click the following button to download and install `influx` CLI for macOS.

[influx CLI (macOS)](https://dl.influxdata.com/influxdb/releases/influxdb2-client-2.7.5-darwin-amd64.tar.gz)

### Step 2: Unpackage the influx binary

**Note:** The commands below are examples. Adjust the file names, paths, and utilities to your own needs.

To unpackage the downloaded archive, **double click the archive file in Finder** or run the following command in a macOS command prompt application such **Terminal** or **[iTerm2](https://www.iterm2.com/)**:

```sh
# Unpackage contents to the current working directory
tar zxvf ~/Downloads/influxdb2-client-2.7.5-darwin-amd64.tar.gz
```

### Step 3: (Optional) Place the binary in your $PATH

If you choose, you can place `influx` in your `$PATH` or you can prefix the executable with `./` to run in place. If the binary is on your $PATH, you can run `influx` from any directory. Otherwise, you must specify the location of the CLI (for example, `./influx`or `path/to/influx`).

**Note:** If you have the 1.x binary on your $PATH, moving the 2.0 binary to your $PATH will overwrite the 1.x binary because they have the same name.

```sh
# Copy the influx binary to your $PATH
sudo cp influxdb2-client-2.7.5-darwin-amd64/influx /usr/local/bin/
```

If you rename the binary, all references to `influx` in this documentation refer to the renamed binary.

### Step 4: (macOS Catalina only) Authorize InfluxDB binaries

If running `influx` on macOS Catalina, you must manually authorize the `influx` binary in the **Security & Privacy** section of **System Preferences**.

### Step 5: Set up a configuration profile

To avoid having to pass your InfluxDB [API token](/influxdb/cloud/admin/tokens/) with each `influx` command, set up a configuration profile that stores your credentials.

In a terminal, run the following command:

```sh
# Set up a configuration profile
influx config create -n default \
  -u https://cloud2.influxdata.com \
  -o example-org \
  -t mySuP3rS3cr3tT0keN \
  -a
```

This configures a new profile named `default` and makes the profile active so your `influx` CLI commands run against this instance. For more detail, see [influx config](/influxdb/cloud/reference/cli/influx/config/).

### Step 6: Learn `influx` CLI commands

To see all available `influx` commands, type `influx -h` or check out [influx - InfluxDB command line interface](/influxdb/cloud/reference/cli/influx/).

**Linux:**

### Step 1: Download influx CLI for Linux

Click one of the following buttons to download and install the `influx` CLI appropriate for your chipset.

[influx CLI (amd64)](https://dl.influxdata.com/influxdb/releases/influxdb2-client-2.7.5-linux-amd64.tar.gz) [influx CLI (arm)](https://dl.influxdata.com/influxdb/releases/influxdb2-client-2.7.5-linux-arm64.tar.gz)

### Step 2: Unpackage the influx binary

**Note:** The commands below are examples. Adjust the file names, paths, and utilities to your own needs.

```sh
# Unpackage contents to the current working directory
tar xvfz influxdb2-client-2.7.5-linux-amd64.tar.gz
```

### Step 3: (Optional) Place the binary in your $PATH

If you choose, you can place `influx` in your `$PATH` or you can prefix the executable with `./` to run in place. If the binary is on your $PATH, you can run `influx` from any directory. Otherwise, you must specify the location of the CLI (for example, `./influx`or `path/to/influx`).

**Note:** If you have the 1.x binary on your $PATH, moving the 2.0 binary to your $PATH will overwrite the 1.x binary because they have the same name.

```sh
# Copy the influx and influxd binary to your $PATH
sudo cp influxdb2-client-2.7.5-linux-amd64/influx /usr/local/bin/
```

If you rename the binary, all references to `influx` in this documentation refer to the renamed binary.

### Step 4: Set up a configuration profile

To avoid having to pass your InfluxDB [API token](/influxdb/cloud/admin/tokens/) with each `influx` command, set up a configuration profile that stores your credentials.

In a terminal, run the following command:

```sh
# Set up a configuration profile
influx config create -n default \
  -u https://cloud2.influxdata.com \
  -o example-org \
  -t mySuP3rS3cr3tT0keN \
  -a
```

This configures a new profile named `default` and makes the profile active so your `influx` CLI commands run against this instance. For more detail, see [influx config](/influxdb/cloud/reference/cli/influx/config/).

### Step 5: Learn `influx` CLI commands

To see all available `influx` commands, type `influx -h` or check out [influx - InfluxDB command line interface](/influxdb/cloud/reference/cli/influx/).

**Windows:**

### Step 1: Download influx CLI for Windows

Click the following button to download and install `influx` CLI for Windows.

[influx CLI (Windows)](https://dl.influxdata.com/influxdb/releases/influxdb2-client-2.7.5-windows-amd64.zip)

### Step 2: Expand the downloaded archive

Expand the downloaded archive into `C:\Program Files\InfluxData\influxdb`.

### Step 3: Grant network access

When using the `influx` CLI for the first time, Windows Defender will appear with the following message: `Windows Defender Firewall has blocked some features of this app.`

1. Select **Private networks, such as my home or work network**.
2. Click **Allow access**.

### Step 4: Learn `influx` CLI commands

To see all available `influx` commands, type `influx -h` or check out [influx - InfluxDB command line interface](/influxdb/cloud/reference/cli/influx/).

<!-- End tabbed content -->

## Sign in

Sign in to [InfluxDB Cloud](https://cloud2.influxdata.com) using your email address and password.

[Sign in to InfluxDB Cloud now](https://cloud2.influxdata.com)

## Get started working with data

To learn how to get started working with time series data, see [Get Started](/influxdb/cloud/get-started).

[get-started](/influxdb/cloud/tags/get-started/) [install](/influxdb/cloud/tags/install/) [cli](/influxdb/cloud/tags/cli/)

---

## InfluxDB reference

### [Release notes](/influxdb/cloud/reference/release-notes/)

Find important information about what’s included in new versions of InfluxData products.

### [InfluxDB key concepts](/influxdb/cloud/reference/key-concepts/)

Concepts related to InfluxDB.

### [InfluxDB HTTP API](/influxdb/cloud/reference/api/)

The InfluxDB HTTP API provides a programmatic interface for interactions with InfluxDB, such as writing and querying data, and managing resources within an InfluxDB instance. Access the InfluxDB API using the `/api/v2/` endpoint.

### [Command line tools](/influxdb/cloud/reference/cli/)

InfluxDB provides command line tools designed to aid in managing and working with InfluxDB from the command line.

### [InfluxDB syntaxes](/influxdb/cloud/reference/syntax/)

InfluxDB uses a handful of languages and syntaxes to perform tasks such as writing, querying, processing, and deleting data.

### [InfluxDB Cloud regions](/influxdb/cloud/reference/regions/)

InfluxDB Cloud is available on multiple cloud providers and in multiple regions. Each region has a unique InfluxDB Cloud URL and API endpoint.

### [InfluxDB Cloud internals](/influxdb/cloud/reference/internals/)

```html
    <h3 id="influxdb-cloud-data-durability"><a href="/influxdb/cloud/reference/internals/durability/" target="">InfluxDB Cloud data durability</a></h3>

    <p>InfluxDB Cloud ensures the durability of all stored data by replicating data across multiple availability zones in a cloud region, automatically creating backups, and verifying that replicated data is consistent and readable.</p>




    <h3 id="influxdb-cloud-security"><a href="/influxdb/cloud/reference/internals/security/" target="">InfluxDB Cloud security</a></h3>

    <p>InfluxDB Cloud is built on industry-standard security practices and principles.</p>




    <h3 id="influxdb-cloud-system-buckets"><a href="/influxdb/cloud/reference/internals/system-buckets/" target="">InfluxDB Cloud system buckets</a></h3>

    <p>InfluxDB system buckets contain time series data used by and generated from the InfluxDB monitoring and alerting system and the task engine.</p>

```

### [Sample data](/influxdb/cloud/reference/sample-data/)

Use sample data to familiarize yourself with time series data and InfluxDB. InfluxData provides many sample time series datasets to use with InfluxDB and InfluxDB Cloud.

### [Prometheus metric parsing formats](/influxdb/cloud/reference/prometheus-metrics/)

When scraping [Prometheus-formatted metrics](https://prometheus.io/docs/concepts/data_model/) and writing them to InfluxDB Cloud, metrics are parsed and stored in InfluxDB in different formats.

### [Frequently asked questions](/influxdb/cloud/reference/faq/)

Find answers to common questions related to InfluxDB OSS.

### [Policies and procedures](/influxdb/cloud/reference/policies/)

InfluxData product policies and procedures.

### [Glossary](/influxdb/cloud/reference/glossary/)

Terms related to InfluxData products and platforms.

### [InfluxDB Cloud (TSM) service notices](/influxdb/cloud/reference/service-notices/)

Important service notices related to the InfluxDB Cloud (TSM) platform.

---

## Query data in InfluxDB

Learn to query data stored in InfluxDB using Flux and tools such as the InfluxDB user interface and the ‘influx’ command line interface.

### [Get started with Flux](/influxdb/cloud/query-data/get-started/)

Get started with Flux, InfluxData’s functional data scripting language. This step-by-step guide through the basics of writing a Flux query.

### [Query data with Flux](/influxdb/cloud/query-data/flux/)

Guides that walk through both common and complex queries and use cases for Flux.

### [Query data with InfluxQL](/influxdb/cloud/query-data/influxql/)

Use the [InfluxDB 1.x `/query` compatibility endpoint](/influxdb/cloud/reference/api/influxdb-1x/query) to query data in InfluxDB Cloud and InfluxDB OSS 2.4 with **InfluxQL**.

### [Execute queries](/influxdb/cloud/query-data/execute-queries/)

There are multiple ways to query data from InfluxDB including the InfluxDB UI, CLI, and API.

### [Common queries](/influxdb/cloud/query-data/common-queries/)

This collection of articles walks through common use cases for Flux queries.

### [Optimize Flux queries](/influxdb/cloud/query-data/optimize-queries/)

Optimize your Flux queries to reduce their memory and compute (CPU) requirements.

### [Use parameterized Flux queries](/influxdb/cloud/query-data/parameterized-queries/)

Use parameterized queries to re-use Flux queries and dynamically populate variables and prevent injection attacks.

[query](/influxdb/cloud/tags/query/) [flux](/influxdb/cloud/tags/flux/)

---

## Process data with InfluxDB tasks

Process and analyze your data with tasks in the InfluxDB **task engine**. Use tasks (scheduled Flux queries) to input a data stream and then analyze, modify, and act on the data accordingly.

Discover how to create and manage tasks using the InfluxDB user interface (UI) and the `influx` command line interface (CLI). Find examples of data downsampling, anomaly detection *(Coming)*, alerting *(Coming)*, and other common tasks.

Tasks replace InfluxDB v1.x continuous queries.

### [Get started with tasks](/influxdb/cloud/process-data/get-started/)

Learn the basics of writing an InfluxDB task that processes data, and then performs an action, such as storing the modified data in a new bucket or sending an alert.

### [Manage tasks](/influxdb/cloud/process-data/manage-tasks/)

InfluxDB provides options for creating, reading, updating, and deleting tasks using the `influx` CLI, the InfluxDB UI, and the InfluxDB API.

### [Common data processing tasks](/influxdb/cloud/process-data/common-tasks/)

InfluxDB Tasks process data on specified schedules. This collection of articles walks through common use cases for InfluxDB tasks.

### [Task configuration options](/influxdb/cloud/process-data/task-options/)

Task options define specific information about a task such as its name, the schedule on which it runs, execution delays, and others.

### Related

- [Tasks & InfluxDB](/resources/videos/influxdb-tasks/)

[tasks](/influxdb/cloud/tags/tasks/)

---

## Monitor data and send alerts

Monitor your time series data and send alerts by creating checks, notification rules, and notification endpoints. Or use [community templates to monitor](/influxdb/cloud/monitor-alert/templates/) supported environments.

## Overview

1. A [check](/influxdb/cloud/reference/glossary/#check) in InfluxDB queries data and assigns a status with a `_level` based on specific conditions.
2. InfluxDB stores the output of a check in the `statuses` measurement in the `_monitoring` system bucket.
3. [Notification rules](/influxdb/cloud/reference/glossary/#notification-rule) check data in the `statuses` measurement and, based on conditions set in the notification rule, send a message to a [notification endpoint](/influxdb/cloud/reference/glossary/#notification-endpoint).
4. InfluxDB stores notifications in the `notifications` measurement in the `_monitoring` system bucket.

## Create an alert

To get started, do the following:

1. [Create checks](/influxdb/cloud/monitor-alert/checks/create/) to monitor data and assign a status.
2. [Add notification endpoints](/influxdb/cloud/monitor-alert/notification-endpoints/create/) to send notifications to third parties.
3. [Create notification rules](/influxdb/cloud/monitor-alert/notification-rules/create) to check statuses and send notifications to your notifications endpoints.

## Manage your monitoring and alerting pipeline

### [Manage checks](/influxdb/cloud/monitor-alert/checks/)

Checks in InfluxDB query data and apply a status or level to each data point based on specified conditions.

### [Manage notification endpoints](/influxdb/cloud/monitor-alert/notification-endpoints/)

Create, read, update, and delete endpoints in the InfluxDB UI.

### [Manage notification rules](/influxdb/cloud/monitor-alert/notification-rules/)

Manage notification rules in InfluxDB.

### [Monitor with templates](/influxdb/cloud/monitor-alert/templates/)

Use community templates to monitor data in many supported environments. Monitor infrastructure, networking, IoT, software, security, TICK stack, and more.

### [Send alert email](/influxdb/cloud/monitor-alert/send-email/)

Send an alert email.

### [Create custom checks](/influxdb/cloud/monitor-alert/custom-checks/)

Create custom checks with a Flux task.

[monitor](/influxdb/cloud/tags/monitor/) [alert](/influxdb/cloud/tags/alert/) [checks](/influxdb/cloud/tags/checks/) [notification](/influxdb/cloud/tags/notification/) [endpoints](/influxdb/cloud/tags/endpoints/)

---

## Migrate to an account in a new region

The following guide provides instructions on migrating data and resources from an existing InfluxDB Cloud account to a new InfluxDB account in another InfluxDB Cloud region.

## Create a new account in a new region

InfluxDB organizations are bound to a specific cloud provider and region. [Create a new InfluxDB Cloud account](/influxdb/cloud/sign-up/) in the region you want to migrate to.

## Migrate Data

If you want to migrate data from your current InfluxDB Cloud account to your new destination InfluxDB Cloud account, there is documentation available that walks through the migration. The specific process varies depending on whether your destination account is powered by our current database engine, [Time-Structured Merge Tree (TSM)](/influxdb/v2/reference/internals/storage-engine/#time-structured-merge-tree-tsm) or [our new database engine, InfluxDB 3](/blog/announcing-general-availability-new-database-engine/).

To benefit from the InfluxDB 3 storage engine's unlimited cardinality and support for SQL, migrate your data to InfluxDB Cloud Serverless.

- [Migrate data TSM to Serverless](/influxdb3/cloud-serverless/write-data/migrate-data/migrate-tsm-to-serverless/)
- [Migrate data from TSM to TSM](/influxdb/cloud/write-data/migrate-data/migrate-cloud-to-cloud/).

To see which storage engine your organization uses, find the **InfluxDB Cloud powered by** link in your [InfluxDB Cloud organization homepage](https://cloud2.influxdata.com) version information. If your organization is using TSM, you’ll see **TSM** followed by the version number. If Serverless, you’ll see **InfluxDB Cloud Serverless** followed by the version number.

### Dual write into both organizations

Depending on the duration of your retention policy for storing data it may be easier to temporarily dual write into both the source and destination accounts for an overlapping period until the destination account holds all desired data.

## Migrate Resources

Resources include, but are not limited to the following:

- buckets
- dashboards
- notification rules
- tasks
- labels
- variables

If you have resources that you want to migrate to your destination account (rather than recreating these resources in the destination account) you can do the following:

1. [Download and install the 2.x `influx` CLI](/influxdb/cloud/tools/influx-cli/).

2. [Set up InfluxDB connection configurations](/influxdb/cloud/tools/influx-cli/#provide-required-authentication-credentials) for both your **source** and **destination** InfluxDB Cloud accounts. Use the [`influx config create` command](/influxdb/cloud/reference/cli/influx/config/create/) and provide the following for each connection:

   - Connection configuration name
   - [InfluxDB Cloud region URL](/influxdb/cloud/reference/regions/)
   - [InfluxDB organization name](/influxdb/cloud/admin/organizations/)
   - [InfluxDB API token](/influxdb/cloud/admin/tokens/)

   ```sh
   # Create your source connection configuration and set it to active
   $ influx config create \
     --config-name source \
     --host-url https://cloud2.influxdata.com \
     --org <your-source-org> \
     --token <your-source-auth-token> \
     --active

   # Create your destination connection configuration
   $ influx config create \
     --config-name destination \
     --host-url https://cloud2.influxdata.com \
     --org <your-destination-org> \
     --token <your-destination-auth-token>
   ```

3. Use the [`influx export all` command](/influxdb/cloud/reference/cli/influx/export/all/#export-all-resources-in-an-organization-as-a-template) to export all resources from your **source account** to an [InfluxDB template](/influxdb/cloud/tools/influxdb-templates/use/).

   ```sh
   influx export all
   ```

4. Use the [`influx config` command](/influxdb/cloud/reference/cli/influx/config/) to switch to your **destination** connection configuration. Provide the name of the configuration to switch to:

   ```sh
   influx config destination
   ```

5. Use [`influx template apply` command](/influxdb/cloud/reference/cli/influx/apply/#apply-a-template-from-a-file) to apply the exported InfluxDB template created in the previous step to your destination account:

   ```sh
   influx apply --file path/to/template.json
   ```

---

## Get started with InfluxDB Cloud

InfluxDB Cloud is the platform purpose-built to collect, store, process and visualize time series data. **Time series data** is a sequence of data points indexed in time order. Data points typically consist of successive measurements made from the same source and are used to track changes over time. Examples of time series data include:

- Industrial sensor data
- Server performance metrics
- Heartbeats per minute
- Electrical activity in the brain
- Rainfall measurements
- Stock prices

This multi-part tutorial walks you through writing time series data to InfluxDB Cloud, querying that data, processing and alerting on the data, and then visualizing the data.

## Key concepts before you get started

Before you get started using InfluxDB, it’s important to understand how time series data is organized and stored in InfluxDB and some key definitions that are used throughout this documentation.

### Data organization

The InfluxDB data model organizes time series data into buckets and measurements. A bucket can contain multiple measurements. Measurements contain multiple tags and fields.

- **Bucket**: Named location where time series data is stored. A bucket can contain multiple *measurements*.
  - **Measurement**: Logical grouping for time series data. All *points* in a given measurement should have the same *tags*. A measurement contains multiple *tags* and *fields*.
    - **Tags**: Key-value pairs with values that differ, but do not change often. Tags are meant for storing metadata for each point–for example, something to identify the source of the data like host, location, station, etc.
    - **Fields**: Key-value pairs with values that change over time–for example: temperature, pressure, stock price, etc.
    - **Timestamp**: Timestamp associated with the data. When stored on disk and queried, all data is ordered by time.

*For detailed information and examples of the InfluxDB data model, see [Data elements](/influxdb/cloud/reference/key-concepts/data-elements/).*

### Important definitions

The following are important definitions to understand when using InfluxDB:

- **Point**: Single data record identified by its *measurement, tag keys, tag values, field key, and timestamp*.
- **Series**: A group of points with the same *measurement, tag keys and values, and field key*.

#### Example InfluxDB query results

| _time | _measurement | city | country | _field | _value |
| --- | --- | --- | --- | --- | --- |
| 2022-01-01T12:00:00Z | weather | London | UK | temperature | 12.0 |
| 2022-02-01T12:00:00Z | weather | London | UK | temperature | 12.1 |
| 2022-03-01T12:00:00Z | weather | London | UK | temperature | 11.5 |
| 2022-04-01T12:00:00Z | weather | London | UK | temperature | 5.9 |

| _time | _measurement | city | country | _field | _value |
| --- | --- | --- | --- | --- | --- |
| 2022-01-01T12:00:00Z | weather | Cologne | DE | temperature | 13.2 |
| 2022-02-01T12:00:00Z | weather | Cologne | DE | temperature | 11.5 |
| 2022-03-01T12:00:00Z | weather | Cologne | DE | temperature | 10.2 |
| 2022-04-01T12:00:00Z | weather | Cologne | DE | temperature | 7.9 |

| _time | _measurement | city | country | _field | _value |
| --- | --- | --- | --- | --- | --- |
| 2022-01-01T12:00:00Z | weather | London | UK | humidity | 88.4 |
| 2022-02-01T12:00:00Z | weather | London | UK | humidity | 94.0 |
| 2022-03-01T12:00:00Z | weather | London | UK | humidity | 82.1 |
| 2022-04-01T12:00:00Z | weather | London | UK | humidity | 87.6 |

| _time | _measurement | city | country | _field | _value |
| --- | --- | --- | --- | --- | --- |
| 2022-01-01T12:00:00Z | weather | Cologne | DE | humidity | 88.5 |
| 2022-02-01T12:00:00Z | weather | Cologne | DE | humidity | 87.8 |
| 2022-03-01T12:00:00Z | weather | Cologne | DE | humidity | 76.4 |
| 2022-04-01T12:00:00Z | weather | Cologne | DE | humidity | 93.3 |

## Tools to use

Throughout this tutorial, there are multiple tools you can use to interact with InfluxDB Cloud. Examples are provided for each of the following:

- [InfluxDB user interface (UI)](#influxdb-user-interface-ui)
- [`influx` CLI](#influx-cli)
- [InfluxDB HTTP API](#influxdb-http-api)

### InfluxDB user interface (UI)

The InfluxDB UI provides a web-based visual interface for interacting with and managing InfluxDB.

To access the InfluxDB Cloud UI, [log into your InfluxDB Cloud account](https://cloud2.influxdata.com).

### `influx` CLI

The `influx` CLI lets you interact with and manage InfluxDB Cloud from a command line.

For detailed CLI installation instructions, see [Use the influx CLI](/influxdb/cloud/tools/influx-cli/).

### InfluxDB HTTP API

The [InfluxDB API](/influxdb/cloud/reference/api/) provides a simple way to interact with the InfluxDB Cloud using HTTP(S) clients. Examples in this tutorial use cURL, but any HTTP(S) client will work.

### InfluxDB client libraries

[InfluxDB client libraries](/influxdb/cloud/api-guide/client-libraries/) are language-specific clients that interact with the InfluxDB HTTP API. Examples for client libraries are not provided in this tutorial, but these can be used to perform all the actions outlined in this tutorial.

## Authorization

**InfluxDB Cloud requires authentication** using [API tokens](/influxdb/cloud/admin/tokens/). Each API token is associated with a user and a specific set of permissions for InfluxDB resources.

[Set up InfluxDB](/influxdb/cloud/get-started/setup/)

![InfluxDB University](/svgs/influxdbu-full-white.svg)

### InfluxDB Essentials

Learn how to write, query, and visualize data in InfluxDB in this **free** InfluxDB University course.

[Take the course](https://university.influxdata.com/courses/influxdb-essentials-tutorial/)

[get-started](/influxdb/cloud/tags/get-started/)

---

## Develop with the InfluxDB API

The InfluxDB v2 API provides a programmatic interface for interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.

### InfluxDB client libraries

InfluxDB client libraries are language-specific packages that integrate with the InfluxDB v2 API. For information about supported client libraries, see [InfluxDB client libraries](/influxdb/cloud/api-guide/client-libraries/).

### InfluxDB Cloud API documentation

[InfluxDB Cloud API documentation](/influxdb/cloud/api/)

### InfluxDB v1 compatibility API documentation

The InfluxDB v2 API includes [InfluxDB 1.x compatibility endpoints](/influxdb/cloud/reference/api/influxdb-1x/) that work with InfluxDB 1.x client libraries and third-party integrations like [Grafana](https://grafana.com) and others.

[View full v1 compatibility API documentation](/influxdb/cloud/api/v1-compatibility/)

![InfluxDB University](/svgs/influxdbu-full-white.svg)

### Building IoT Apps with InfluxDB

Learn the basics of how to build an IoT application with InfluxDB with this **free** InfluxDB University course.

[Take the course](https://university.influxdata.com/courses/building-iot-apps-with-influxdb-tutorial/)

[api](/influxdb/cloud/tags/api/)

---

## Administer InfluxDB Cloud

Use the InfluxDB API, user interface (UI), and CLIs to perform administrative tasks in InfluxDB Cloud (TSM).

### [Identify InfluxDB Cloud (TSM) version](/influxdb/cloud/admin/identify-version/)

Learn how to identify your InfluxDB Cloud (TSM) instance through URL patterns, account settings, and HTTP headers.

### [Manage organizations](/influxdb/cloud/admin/organizations/)

Manage organizations in InfluxDB using the InfluxDB UI or the influx CLI.

### [Manage API tokens](/influxdb/cloud/admin/tokens/)

Manage API tokens in InfluxDB using the InfluxDB UI or the influx CLI.

### [Manage buckets](/influxdb/cloud/admin/buckets/)

Manage buckets in InfluxDB using the InfluxDB UI or the influx CLI.

### [Manage secrets](/influxdb/cloud/admin/secrets/)

Manage and use secrets in InfluxDB Cloud.

---

## Manage your InfluxDB Cloud Account

### [InfluxDB Cloud plans](/influxdb/cloud/account-management/pricing-plans/)

InfluxDB Cloud provides two pricing plans to fit your needs – the Free Plan and the Usage-based Plan.

### [Manage billing](/influxdb/cloud/account-management/billing/)

Upgrade to the InfluxDB Cloud Usage-Based Plan and manage your billing information.

### [View data usage](/influxdb/cloud/account-management/data-usage/)

View your InfluxDB Cloud data usage and rate limit notifications.

### [Change your password](/influxdb/cloud/account-management/change-password/)

To update your InfluxDB Cloud password, click the **Forgot Password** link on the [InfluxDB Cloud login page](https://cloud2.influxdata.com/login). Passwords must be at least 8 characters in length, and must not contain common words, personal information, or previous passwords.

### [Switch InfluxDB Cloud accounts](/influxdb/cloud/account-management/switch-account/)

Switch from one InfluxDB Cloud account to another and set a default account.

### [Switch InfluxDB Cloud organizations](/influxdb/cloud/account-management/switch-org/)

Switch from one InfluxDB Cloud organization to another.

### [Cancel your InfluxDB Cloud subscription](/influxdb/cloud/account-management/offboarding/)

Cancel your InfluxDB Cloud account at any time by stopping all read and write requests, and backing up data.

### [Limits and adjustable quotas](/influxdb/cloud/account-management/limits/)

InfluxDB Cloud has adjustable service quotas and global (non-adjustable) system limits.
