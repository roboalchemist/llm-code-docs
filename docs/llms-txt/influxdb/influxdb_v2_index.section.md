---
title: Get started with InfluxDB v2
description: InfluxDB OSS is an open source time series database designed to handle high write and query loads. Learn how to use and leverage InfluxDB in use cases such as monitoring metrics, IoT data, and events.
url: https://docs.influxdata.com/influxdb/v2/
product: InfluxDB OSS v2
type: section
pages: 13
estimated_tokens: 25708
child_pages:
  - url: https://docs.influxdata.com/influxdb/v2/write-data/
    title: Write data to InfluxDB
  - url: https://docs.influxdata.com/influxdb/v2/visualize-data/
    title: Visualize data with the InfluxDB UI
  - url: https://docs.influxdata.com/influxdb/v2/tools/
    title: InfluxDB tools and integrations
  - url: https://docs.influxdata.com/influxdb/v2/tags/
    title: Tags and related content
  - url: https://docs.influxdata.com/influxdb/v2/reference/
    title: InfluxDB reference
  - url: https://docs.influxdata.com/influxdb/v2/query-data/
    title: Query data in InfluxDB
  - url: https://docs.influxdata.com/influxdb/v2/process-data/
    title: Process data with InfluxDB tasks
  - url: https://docs.influxdata.com/influxdb/v2/monitor-alert/
    title: Monitor data and send alerts
  - url: https://docs.influxdata.com/influxdb/v2/install/
    title: Install InfluxDB OSS v2
  - url: https://docs.influxdata.com/influxdb/v2/get-started/
    title: Get started with InfluxDB
  - url: https://docs.influxdata.com/influxdb/v2/api-guide/
    title: Develop with the InfluxDB API
  - url: https://docs.influxdata.com/influxdb/v2/admin/
    title: Administer InfluxDB
---

---

## Write data to InfluxDB

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

1. Learn the [best practices](/influxdb/v2/write-data/best-practices/) for writing data.
2. Discover how to write data [without coding](/influxdb/v2/write-data/no-code/), by [loading data source in the UI](/influxdb/v2/write-data/no-code/load-data/), or using [developer tools](/influxdb/v2/write-data/developer-tools/).
3. Do any of the following:
   - [Troubleshoot the most common issues writing data](/influxdb/v2/write-data/troubleshoot/)
   - [Delete data you no longer need](/influxdb/v2/write-data/delete-data/)
   - [Query and explore data](/influxdb/v2/query-data/)
   - [Process data](/influxdb/v2/process-data/)
   - [Visualize data](/influxdb/v2/visualize-data/)
   - [Migrate data](/influxdb/cloud/write-data/migrate-data/)
   - [Monitor and alert](/influxdb/v2/monitor-alert/)

The following video discusses different ways to write data to InfluxDB:

### Related

- [Use Telegraf to write data](/influxdb/v2/write-data/no-code/use-telegraf/)
- [InfluxDB v1 API /write endpoint](/influxdb/v2/api/#tag/Write)
- [Line protocol](/influxdb/v2/reference/syntax/line-protocol/)
- [Annotated CSV](/influxdb/v2/reference/syntax/annotated-csv/)
- [influx write](/influxdb/v2/reference/cli/influx/write/)
- [Migrate data to InfluxDB](/influxdb/v2/write-data/migrate-data/)
- [How to Ingest Data in InfluxDB (Video)](/resources/videos/ingest-data/)

[write](/influxdb/v2/tags/write/) [line protocol](/influxdb/v2/tags/line-protocol/)

---

## Visualize data with the InfluxDB UI

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

The InfluxDB user interface (UI) provides tools for building custom dashboards to visualize your data. The following articles outline ways to customize and manage dashboards.

The InfluxDB UI is packaged with InfluxDB and runs as part of the InfluxDB server. To access the UI, start the [`influxd` service](/influxdb/v2/reference/cli/influxd/) and visit [http://localhost:8086](http://localhost:8086) in your web browser.

### [Manage InfluxDB dashboards](/influxdb/v2/visualize-data/dashboards/)

Create, edit, and manage custom dashboards in the InfluxDB user interface (UI).

### [Use and manage variables](/influxdb/v2/visualize-data/variables/)

Dashboard variables allow you to alter specific components of cells’ queries without having to edit the queries, making it easy to interact with your dashboard cells and explore your data.

### [Manage labels in the InfluxDB UI](/influxdb/v2/visualize-data/labels/)

Labels are a way to add visual metadata to dashboards, tasks, and other items in the InfluxDB UI. View and manage labels in the InfluxDB user interface.

### [Use annotations in dashboards](/influxdb/v2/visualize-data/annotations/)

Add annotations to your InfluxDB dashboards to provide useful, contextual information about single points in time.

### [Visualization types](/influxdb/v2/visualize-data/visualization-types/)

The InfluxDB UI provides multiple visualization types to visualize your data in a format that makes the most sense for your use case. Use the available customization options to customize each visualization.

[visualize](/influxdb/v2/tags/visualize/)

---

## InfluxDB tools and integrations

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

### Flux VS Code extension no longer available

The `vsflux` extension is no longer available in the Visual Studio Marketplace. `vsflux` and the `flux-lsp` Flux Language Server Protocol plugin are no longer maintained. Their repositories have been archived and are no longer receiving updates.

### [Telegraf configurations](/influxdb/v2/tools/telegraf-configs/)

InfluxDB OSS lets you automatically generate Telegraf configurations or upload custom Telegraf configurations that collect metrics and write them to InfluxDB OSS.

### [Notebooks](/influxdb/v2/tools/notebooks/)

Use notebooks to build and annotate processes and data flows for time series data.

### [InfluxDB templates](/influxdb/v2/tools/influxdb-templates/)

InfluxDB templates are prepackaged InfluxDB configurations that contain everything from dashboards and Telegraf configurations to notifications and alerts.

### [Install and use the influx CLI](/influxdb/v2/tools/influx-cli/)

Use the `influx` and `influxd` command line interfaces to interact with and manage InfluxDB.

### [Use the Interactive Flux REPL](/influxdb/v2/tools/flux-repl/)

Use the Flux REPL (Read–Eval–Print Loop) to execute Flux scripts and interact with InfluxDB and other data sources.

### [Use the InfluxQL shell](/influxdb/v2/tools/influxql-shell/)

Use the InfluxQL interactive shell to execute InfluxQL queries and interact with InfluxDB.

### [Use the Flux LSP with Vim](/influxdb/v2/tools/flux-vim-lsp/)

Use the Flux LSP with Vim to add auto-completion, syntax checking, and other language-specific features to your editor.

### [Use Grafana with InfluxDB OSS](/influxdb/v2/tools/grafana/)

Use [Grafana](https://grafana.com/) to visualize data from your **InfluxDB** instance.

### [Use Chronograf with InfluxDB OSS](/influxdb/v2/tools/chronograf/)

Chronograf is a data visualization and dashboarding tool designed to visualize data in InfluxDB 1.x. It is part of the [TICKstack](/platform/) that provides an InfluxQL data explorer, Kapacitor integrations, and more. Continue to use Chronograf with **InfluxDB Cloud** and **InfluxDB OSS 2.x** and the [1.x compatibility API](/influxdb/v2/reference/api/influxdb-1x/).

### [Use Kapacitor with InfluxDB OSS](/influxdb/v2/tools/kapacitor/)

[Kapacitor](/kapacitor/) is a data processing framework that makes it easy to create alerts, run ETL (Extract, Transform and Load) jobs and detect anomalies. Use Kapacitor with **InfluxDB OSS 2.x**.

### [Downsample data with Quix Streams](/influxdb/v2/tools/downsample-data-quix/)

Use Quix Streams to create Python service that downsamples data stored in InfluxDB.

### [Use Postman with the InfluxDB API](/influxdb/v2/tools/postman/)

Use [Postman](https://www.postman.com/), a popular tool for exploring APIs, to interact with the [InfluxDB API](/influxdb/v2/api-guide/).

### [Use the InfluxDB documentation MCP server](/influxdb/v2/tools/mcp-server/)

Query InfluxDB documentation from your IDE using the InfluxDB documentation MCP server.

---

## Tags and related content

- [aggregates](aggregates) (2)
- [ai](ai) (1)
- [alert](alert) (5)
- [alerts](alerts) (1)
- [annotations](annotations) (1)
- [api](api) (6)
- [authentication](authentication) (6)
- [authorization](authorization) (7)
- [backup](backup) (2)
- [best practices](best-practices) (2)
- [bucket-schema](bucket-schema) (1)
- [buckets](buckets) (4)
- [cardinality](cardinality) (3)
- [check](check) (1)
- [checks](checks) (3)
- [cli](cli) (8)
- [client libraries](client-libraries) (8)
- [conditionals](conditionals) (1)
- [config](config) (2)
- [counters](counters) (1)
- [cpu](cpu) (1)
- [csv](csv) (2)
- [cumulative sum](cumulative-sum) (1)
- [custom](custom) (2)
- [dashboards](dashboards) (5)
- [dbrp](dbrp) (6)
- [delete](delete) (3)
- [design principles](design-principles) (1)
- [development](development) (1)
- [email](email) (1)
- [endpoints](endpoints) (2)
- [errors](errors) (1)
- [exists](exists) (1)
- [export](export) (1)
- [fill](fill) (1)
- [flux](flux) (17)
- [functions](functions) (2)
- [get-started](get-started) (3)
- [glossary](glossary) (1)
- [go](go) (1)
- [grafana](grafana) (1)
- [group](group) (1)
- [hardening](hardening) (1)
- [health](health) (1)
- [histogram](histogram) (1)
- [https](https) (1)
- [increase](increase) (1)
- [influx](influx) (1)
- [influxd](influxd) (3)
- [influxql](influxql) (6)
- [infrastructure](infrastructure) (1)
- [inspect](inspect) (15)
- [install](install) (2)
- [internals](internals) (8)
- [javascript](javascript) (6)
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
- [members](members) (2)
- [memory](memory) (1)
- [metrics](metrics) (1)
- [monitor](monitor) (9)
- [moving average](moving-average) (1)
- [mqtt](mqtt) (1)
- [networking](networking) (1)
- [networks](networks) (1)
- [nodejs](nodejs) (1)
- [notebooks](notebooks) (7)
- [notification](notification) (1)
- [notifications](notifications) (4)
- [organizations](organizations) (3)
- [percentile](percentile) (1)
- [performance](performance) (1)
- [ping](ping) (1)
- [plugin](plugin) (1)
- [prometheus](prometheus) (5)
- [python](python) (2)
- [quantile](quantile) (1)
- [queries](queries) (5)
- [query](query) (27)
- [rate](rate) (1)
- [regex](regex) (1)
- [replication](replication) (10)
- [restore](restore) (3)
- [scalar](scalar) (1)
- [schema](schema) (2)
- [scraper](scraper) (5)
- [scripts](scripts) (1)
- [secrets](secrets) (11)
- [security](security) (12)
- [select](select) (1)
- [shards](shards) (2)
- [sort](sort) (1)
- [sql](sql) (1)
- [ssl](ssl) (1)
- [states](states) (1)
- [storage](storage) (9)
- [syntax](syntax) (6)
- [tasks](tasks) (10)
- [telegraf](telegraf) (3)
- [templates](templates) (13)
- [tls](tls) (1)
- [tokens](tokens) (1)
- [tools](tools) (1)
- [transform](transform) (1)
- [tsi](tsi) (3)
- [tsm](tsm) (4)
- [upgrade](upgrade) (1)
- [usage](usage) (1)
- [users](users) (2)
- [variables](variables) (8)
- [visualize](visualize) (1)
- [wal](wal) (2)
- [where](where) (1)
- [write](write) (22)

---

## InfluxDB reference

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

### [Release notes](/influxdb/v2/reference/release-notes/)

Find important information about what’s included in new versions of InfluxData products.

### [InfluxDB key concepts](/influxdb/v2/reference/key-concepts/)

Concepts related to InfluxDB.

### [InfluxDB configuration options](/influxdb/v2/reference/config-options/)

Customize your InfluxDB configuration by using [`influxd`](/influxdb/v2/reference/cli/influxd/) configuration flags, setting environment variables, or defining configuration options in a configuration file.

### [InfluxDB HTTP API](/influxdb/v2/reference/api/)

The InfluxDB HTTP API provides a programmatic interface for interactions with InfluxDB, such as writing and querying data, and managing resources within an InfluxDB instance. Access the InfluxDB API using the `/api/v2/` or InfluxDB v1 endpoints.

### [Command line tools](/influxdb/v2/reference/cli/)

InfluxDB provides command line tools designed to aid in managing and working with InfluxDB from the command line.

### [InfluxDB syntaxes](/influxdb/v2/reference/syntax/)

InfluxDB uses a handful of languages and syntaxes to perform tasks such as writing, querying, processing, and deleting data.

### [InfluxDB OSS URLs](/influxdb/v2/reference/urls/)

InfluxDB OSS is accessed at `localhost:8086` by default, but you can also customize your InfluxDB host and port.

### [InfluxDB internals](/influxdb/v2/reference/internals/)

```html
<h3 id="influxdb-storage-engine"><a href="/influxdb/v2/reference/internals/storage-engine/" target="">InfluxDB storage engine</a></h3>

<p>An overview of the InfluxDB storage engine architecture.</p>

<h3 id="influxdb-file-system-layout"><a href="/influxdb/v2/reference/internals/file-system-layout/" target="">InfluxDB file system layout</a></h3>

<p>The InfluxDB file system layout depends on the operating system, package manager, or containerization platform used to install InfluxDB.</p>

<h3 id="data-retention-in-influxdb"><a href="/influxdb/v2/reference/internals/data-retention/" target="">Data retention in InfluxDB</a></h3>

<p>The InfluxDB retention service checks for and removes data with timestamps beyond the defined retention period of the bucket the data is stored in.</p>

<h3 id="influxdb-runtime"><a href="/influxdb/v2/reference/internals/runtime/" target="">InfluxDB runtime</a></h3>

<p>Learn how to collect Go runtime profiling and tracing information to help with InfluxDB performance analysis and debugging.</p>
```

### [Sample data](/influxdb/v2/reference/sample-data/)

Use sample data to familiarize yourself with time series data and InfluxDB. InfluxData provides many sample time series datasets to use with InfluxDB and InfluxDB Cloud.

### [Prometheus metric parsing formats](/influxdb/v2/reference/prometheus-metrics/)

When scraping [Prometheus-formatted metrics](https://prometheus.io/docs/concepts/data_model/) and writing them to InfluxDB, metrics are parsed and stored in InfluxDB in different formats.

### [Usage telemetry](/influxdb/v2/reference/telemetry/)

InfluxData collects information, or *telemetry data*, about the usage of InfluxDB to help improve the product. Learn what data InfluxDB collects and sends to InfluxData, how it’s used, and how you can opt out.

### [Frequently asked questions](/influxdb/v2/reference/faq/)

Find answers to common questions related to InfluxDB OSS.

### [Glossary](/influxdb/v2/reference/glossary/)

Terms related to InfluxData products and platforms.

### [Contribute to InfluxDB OSS](/influxdb/v2/reference/contributing/)

Find important information about what’s included in new versions of InfluxData products.

---

## Query data in InfluxDB

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

Learn to query data stored in InfluxDB using Flux and tools such as the InfluxDB user interface and the ‘influx’ command line interface.

### [Get started with Flux and InfluxDB](/influxdb/v2/query-data/get-started/)

Get started with Flux, the functional data scripting language, and learn the basics of writing a Flux query that queries InfluxDB.

### [Query data with Flux](/influxdb/v2/query-data/flux/)

Guides that walk through both common and complex queries and use cases for Flux.

### [Query data with InfluxQL](/influxdb/v2/query-data/influxql/)

Use the InfluxDB v1 `/query` compatibility endpoint to query data in InfluxDB v2 using InfluxQL.

### [Execute queries](/influxdb/v2/query-data/execute-queries/)

There are multiple ways to query data from InfluxDB including the InfluxDB UI, CLI, and API.

### [Common queries](/influxdb/v2/query-data/common-queries/)

This collection of articles walks through common use cases for Flux queries.

### [Optimize Flux queries](/influxdb/v2/query-data/optimize-queries/)

Optimize your Flux queries to reduce their memory and compute (CPU) requirements.

![InfluxDB University](/svgs/influxdbu-full-white.svg)

### InfluxDB Essentials

Learn how to write, query, and visualize data in InfluxDB in this **free** InfluxDB University course.

[Take the course](https://university.influxdata.com/courses/influxdb-essentials-tutorial/)

[query](/influxdb/v2/tags/query/) [flux](/influxdb/v2/tags/flux/)

---

## Process data with InfluxDB tasks

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

Process and analyze your data with tasks in the InfluxDB **task engine**. Use tasks (scheduled Flux queries) to input a data stream and then analyze, modify, and act on the data accordingly.

Discover how to create and manage tasks using the InfluxDB user interface (UI) the `influx` command line interface (CLI), and the InfluxDB `/api/v2` API. Find examples of data downsampling and other common tasks.

Tasks replace InfluxDB v1.x continuous queries.

### [Get started with tasks](/influxdb/v2/process-data/get-started/)

Learn the basics of writing an InfluxDB task that processes data, and then performs an action, such as storing the modified data in a new bucket or sending an alert.

### [Manage tasks](/influxdb/v2/process-data/manage-tasks/)

InfluxDB provides options for creating, reading, updating, and deleting tasks using the `influx` CLI, the InfluxDB UI, and the InfluxDB API.

### [Common data processing tasks](/influxdb/v2/process-data/common-tasks/)

InfluxDB Tasks process data on specified schedules. This collection of articles walks through common use cases for InfluxDB tasks.

### [Task configuration options](/influxdb/v2/process-data/task-options/)

Task options define specific information about a task such as its name, the schedule on which it runs, execution delays, and others.

### Related

- [Tasks & InfluxDB](/resources/videos/influxdb-tasks/)

[tasks](/influxdb/v2/tags/tasks/)

---

## Monitor data and send alerts

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

Monitor your time series data and send alerts by creating checks, notification rules, and notification endpoints. Or use [community templates to monitor](/influxdb/v2/monitor-alert/templates/) supported environments.

## Overview

1. A [check](/influxdb/v2/reference/glossary/#check) in InfluxDB queries data and assigns a status with a `_level` based on specific conditions.
2. InfluxDB stores the output of a check in the `statuses` measurement in the `_monitoring` system bucket.
3. [Notification rules](/influxdb/v2/reference/glossary/#notification-rule) check data in the `statuses` measurement and, based on conditions set in the notification rule, send a message to a [notification endpoint](/influxdb/v2/reference/glossary/#notification-endpoint).
4. InfluxDB stores notifications in the `notifications` measurement in the `_monitoring` system bucket.

## Create an alert

To get started, do the following:

1. [Create checks](/influxdb/v2/monitor-alert/checks/create/) to monitor data and assign a status.
2. [Add notification endpoints](/influxdb/v2/monitor-alert/notification-endpoints/create/) to send notifications to third parties.
3. [Create notification rules](/influxdb/v2/monitor-alert/notification-rules/create) to check statuses and send notifications to your notifications endpoints.

## Manage your monitoring and alerting pipeline

### [Manage checks](/influxdb/v2/monitor-alert/checks/)

Checks in InfluxDB query data and apply a status or level to each data point based on specified conditions.

### [Manage notification endpoints](/influxdb/v2/monitor-alert/notification-endpoints/)

Create, read, update, and delete endpoints in the InfluxDB UI.

### [Manage notification rules](/influxdb/v2/monitor-alert/notification-rules/)

Manage notification rules in InfluxDB.

### [Monitor with templates](/influxdb/v2/monitor-alert/templates/)

Use community templates to monitor data in many supported environments. Monitor infrastructure, networking, IoT, software, security, TICK stack, and more.

### [Send alert email](/influxdb/v2/monitor-alert/send-email/)

Send an alert email.

### [Create custom checks](/influxdb/v2/monitor-alert/custom-checks/)

Create custom checks with a Flux task.

[monitor](/influxdb/v2/tags/monitor/) [alert](/influxdb/v2/tags/alert/) [checks](/influxdb/v2/tags/checks/) [notification](/influxdb/v2/tags/notification/) [endpoints](/influxdb/v2/tags/endpoints/)

---

## Install InfluxDB OSS v2

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

The InfluxDB v2 time series platform is purpose-built to collect, store, process and visualize metrics and events.

- [Download and install InfluxDB v2](#download-and-install-influxdb-v2)
- [Start InfluxDB](#start-influxdb)
- [Download, install, and configure the `influx` CLI](#download-install-and-configure-the-influx-cli)

## Download and install InfluxDB v2

Recommended:: Before you open and install packages and downloaded files, use SHA checksum verification and GPG signature verification to ensure the files are intact and authentic.

InfluxDB installation instructions for some OS versions include steps to verify downloaded files before you install them.

For more information about SHA and GPG verifications, see the following:

[](#choose-the-influxdata-key-pair-for-your-os-version)

Choose the InfluxData key-pair for your OS version

*Before running the installation steps, substitute the InfluxData key-pair compatible with your OS version:*

For newer releases (for example, Ubuntu 20.04 LTS and newer, Debian Buster and newer) that support subkey verification:

- GPG key file: [`influxdata-archive.key`](https://repos.influxdata.com/influxdata-archive.key)
- Primary key fingerprint: `24C975CBA61A024EE1B631787C3D57159FC2F927`

For older versions (for example, CentOS/RHEL 7, Ubuntu 18.04 LTS, or Debian Stretch) that don’t support subkeys for verification:

- GPG key file: [`influxdata-archive_compat.key`](https://repos.influxdata.com/influxdata-archive_compat.key)
- Signing key fingerprint: `9D539D90D3328DC7D6C8D3B9D8FF8E1F7DF8B07E`

[](#verify-download-integrity-using-sha-256)

Verify download integrity using SHA-256

For each released binary, InfluxData publishes the SHA checksum that you can use to verify that the downloaded file is intact and hasn’t been corrupted.

To use the SHA checksum to verify the downloaded file, do the following:

1. In the [downloads page](https://www.influxdata.com/downloads), select the **Version** and **Platform** for your download, and then copy the **SHA256:** checksum value.

2. Compute the SHA checksum of the downloaded file and compare it to the published checksum–for example, enter the following command in your terminal:

```bash
# Use 2 spaces to separate the checksum from the filename
echo "8d7872013cad3524fb728ca8483d0adc30125ad1af262ab826dcf5d1801159cf  influxdb2-2.8.0_linux_amd64.tar.gz" \
| sha256sum --check -
```

Replace the following:

- `8d7872013cad3524fb728ca8483d0adc30125ad1af262ab826dcf5d1801159cf`: the **SHA256:** checksum value that you copied from the downloads page

If the checksums match, the output is the following; otherwise, an error message.

```text
influxdb2-2.8.0_linux_amd64.tar.gz: OK
```

[](#verify-file-integrity-and-authenticity-using-gpg)

Verify file integrity and authenticity using GPG

InfluxData uses [GPG (GnuPG)](https://www.gnupg.org/software/) to sign released software and provides public key and encrypted private key (`.key` file) pairs that you can use to verify the integrity of packages and binaries from the InfluxData repository.

Most operating systems include `gpg` by default. *If `gpg` isn’t available on your system, see [GnuPG download](https://gnupg.org/download/) and install instructions.*

The following steps guide you through using GPG to verify InfluxDB binary releases:

1. [Choose the InfluxData key-pair for your OS version](#choose-the-influxdata-key-pair-for-your-os-version).

2. Download and import the InfluxData public key.

    `gpg --import` outputs to stderr. The following example shows how to import the key, redirect the output to stdout, and then check for the expected key name:

```sh
curl --silent --location https://repos.influxdata.com/influxdata-archive.key \
 | gpg --import - 2>&1 \
 | grep 'InfluxData Package Signing Key <support@influxdata.com>'
```

Replace the following:

- `https://repos.influxdata.com/influxdata-archive.key`: the InfluxData private key file compatible with your OS version

If successful, the output is the following:

```text
gpg: key 7C3D57159FC2F927: public key "InfluxData Package Signing Key <support@influxdata.com>" imported
```

3. Download the signature file for the release by appending `.asc` to the download URL, and then use `gpg` to verify the download signature–for example, enter the following in your terminal:

    ```sh
    curl --silent --location \
    https://download.influxdata.com/influxdb/releases/v2.8.0/influxdb2-2.8.0_darwin_amd64.tar.gz.asc \
    | gpg --verify - ~/Downloads/influxdb2-2.8.0_darwin_amd64.tar.gz \
    2>&1 | grep 'InfluxData Package Signing Key <support@influxdata.com>'
    ```

   - `curl --silent --location`: Follows any server redirects and fetches the signature file silently (without progress meter).
   - `gpg --verify -`: Reads the signature from stdin and uses it to verify the the downloaded `influxdbv2` binary.

    If successful, the output is the following:

    ```text
    gpg: Good signature from "InfluxData Package Signing Key <support@influxdata.com>" [unknown]
    ```

*For security, InfluxData periodically rotates keys and publishes the new key pairs.*

The following instructions include steps for downloading, verifying, and installing InfluxDB:

<!-- Tabbed content: Select one of the following options -->

**macOS:**

To install InfluxDB, do one of the following:

- [Install using Homebrew](#install-using-homebrew)
- [Manually download and install for macOS](#manually-download-and-install-for-macos)

We recommend using [Homebrew](https://brew.sh/) to install InfluxDB v2 on macOS.

### InfluxDB and the influx CLI are separate packages

The InfluxDB server ([`influxd`](/influxdb/v2/reference/cli/influxd/)) and the [`influx` CLI](/influxdb/v2/reference/cli/influx/) are packaged and versioned separately.

*You’ll install the `influx CLI` in a [later step](#download-install-and-configure-the-influx-cli).*

### Install using Homebrew

```sh
brew update
brew install influxdb
```

### Manually download and install for macOS

1. In your browser or your terminal, download the InfluxDB package.

    [InfluxDB v2 (macOS)](https://download.influxdata.com/influxdb/releases/v2.8.0/influxdb2-2.8.0_darwin_amd64.tar.gz)

    ```sh
    # Download using cURL
    curl --location -O \
    "https://download.influxdata.com/influxdb/releases/v2.8.0/influxdb2-2.8.0_darwin_amd64.tar.gz"
    ```

2. Recommended:: Verify the integrity of the download–for example, enter the following command in your terminal:

```sh
# Use 2 spaces to separate the checksum from the filename
echo "224926fd77736a364cf28128f18927dda00385f0b6872a108477246a1252ae1b  influxdb2-2.8.0_darwin_amd64.tar.gz" \
| shasum --algorithm 256 --quiet --check -
```

Replace the following:

- `224926fd77736a364cf28128f18927dda00385f0b6872a108477246a1252ae1b`: the SHA checksum from the [downloads page](https://www.influxdata.com/downloads/#telegraf)

3. Unpackage the InfluxDB binary.

    Do one of the following:

   - In **Finder**, double-click the downloaded package file.
   - In your terminal (for example, **Terminal** or **[iTerm2](https://www.iterm2.com/)**), use `tar` to unpackage the file–for example, enter the following command to extract it into the current directory:

    ```sh
    # Unpackage contents to the current working directory
    tar zxvf ./influxdb2-2.8.0_darwin_amd64.tar.gz
    ```

4. Optional: Place the `influxd` binary in your `$PATH`–for example, copy the binary to `/usr/local/bin`:

    ```sh
    # (Optional) Copy the influxd binary to your $PATH
    sudo cp influxdb2-2.8.0/influxd /usr/local/bin/
    ```

    With the `influxd` binary in your `$PATH` (`/usr/local/bin`), you can enter `influxd` in your terminal to start the server.

    If you choose not to move the `influxd` binary into your `$PATH`, enter the path to the binary to start the server–for example:

    ```sh
    ./influxdb2-2.8.0/influxd
    ```

[](#recommended--set-appropriate-directory-permissions)

Recommended – Set appropriate directory permissions

To prevent unwanted access to data, set the permissions on the influxdb `data-dir` to not be world readable. If installing on a server, set a umask of `0027` to properly permission all newly created files–for example, enter the following command in your terminal:

```bash
chmod 0750 ~/.influxdbv2
```

Both InfluxDB 1.x and 2.x have associated `influxd` and `influx` binaries. If InfluxDB 1.x binaries are already in your `$PATH`, run the v2 binaries in place or rename them before putting them in your `$PATH`. If you rename the binaries, all references to `influxd` and `influx` in this documentation refer to your renamed binaries.

**Linux:**

To install InfluxDB on Linux, do one of the following:

- [Install InfluxDB as a service with systemd](#install-influxdb-as-a-service-with-systemd)
- [Manually download and install the influxd binary](#manually-download-and-install-the-influxd-binary)

### InfluxDB and the influx CLI are separate packages

The InfluxDB server ([`influxd`](/influxdb/v2/reference/cli/influxd/)) and the [`influx` CLI](/influxdb/v2/reference/cli/influx/) are packaged and versioned separately.

*You’ll install the `influx CLI` in a [later step](#download-install-and-configure-the-influx-cli).*

### Install InfluxDB as a service with systemd

1. [Choose the InfluxData key-pair for your OS version](#choose-the-influxdata-key-pair-for-your-os-version).

2. Run the command for your OS version to install the InfluxData key, add the InfluxData repository, and install `influxdb`.

    *Before running the command, replace the fingerprint and key filename with the key-pair from the preceding step.*

    ```bash
    # Ubuntu and Debian
    # Add the InfluxData key to verify downloads and add the repository
    curl --silent --location -O https://repos.influxdata.com/influxdata-archive.key
    gpg --show-keys --with-fingerprint --with-colons ./influxdata-archive.key 2>&1 \
    | grep -q '^fpr:\+24C975CBA61A024EE1B631787C3D57159FC2F927:$' \
    && cat influxdata-archive.key \
    | gpg --dearmor \
    | sudo tee /etc/apt/keyrings/influxdata-archive.gpg > /dev/null \
    && echo 'deb [signed-by=/etc/apt/keyrings/influxdata-archive.gpg] https://repos.influxdata.com/debian stable main' \
    | sudo tee /etc/apt/sources.list.d/influxdata.list
    # Install influxdb
    sudo apt-get update && sudo apt-get install influxdb2
    ```

    ```bash
    # RedHat and CentOS
    # Add the InfluxData key to verify downloads
    curl --silent --location -O https://repos.influxdata.com/influxdata-archive.key
    gpg --show-keys --with-fingerprint --with-colons ./influxdata-archive.key 2>&1 \
    | grep -q '^fpr:\+24C975CBA61A024EE1B631787C3D57159FC2F927:$' \
    && cat influxdata-archive.key \
    | gpg --dearmor \
    | tee /etc/pki/rpm-gpg/RPM-GPG-KEY-influxdata > /dev/null

    # Add the InfluxData repository to the repository list.
    cat <<EOF | tee /etc/yum.repos.d/influxdata.repo
    [influxdata]
    name = InfluxData Repository - Stable
    baseurl = https://repos.influxdata.com/stable/\${basearch}/main
    enabled = 1
    gpgcheck = 1
    gpgkey = file:///etc/pki/rpm-gpg/RPM-GPG-KEY-influxdata
    EOF

    # Install influxdb
    sudo yum install influxdb2
    ```

3. Start the InfluxDB service:

    ```bash
    sudo service influxdb start
    ```

    Installing the InfluxDB package creates a service file at `/lib/systemd/system/influxdb.service` to start InfluxDB as a background service on startup.

4. To verify that the service is running correctly, restart your system and then enter the following command in your terminal:

    ```bash
    sudo service influxdb status
    ```

    If successful, the output is the following:

    ```text
    ● influxdb.service - InfluxDB is an open-source, distributed, time series database
       Loaded: loaded (/lib/systemd/system/influxdb.service; enabled; vendor preset: enable>
       Active: active (running)
    ```

For information about where InfluxDB stores data on disk when running as a service, see [File system layout](/influxdb/v2/reference/internals/file-system-layout/?t=Linux#installed-as-a-package).

### Pass configuration options to the service

You can use systemd to customize [InfluxDB configuration options](/influxdb/v2/reference/config-options/#configuration-options) and pass them to the InfluxDB service.

1. Edit the `/etc/default/influxdb2` service configuration file to assign configuration directives to `influxd` command line flags–for example, add one or more `<ENV_VARIABLE_NAME>=<COMMAND_LINE_FLAG>` lines like the following:

   ```sh
   ARG1="--http-bind-address :8087"
   ARG2="--storage-wal-fsync-delay=15m"
   ```

2. Edit the `/lib/systemd/system/influxdb.service` file to pass the variables to the `ExecStart` value:

   ```sh
   ExecStart=/usr/bin/influxd $ARG1 $ARG2
   ```

### Manually download and install the influxd binary

*If necessary, adjust the example file paths and utilities for your system.*

1. In your browser or your terminal, download the InfluxDB binary for your system architecture (AMD64 or ARM).

   [InfluxDB v2 (amd64)](https://download.influxdata.com/influxdb/releases/v2.8.0/influxdb2-2.8.0_linux_amd64.tar.gz) [InfluxDB v2 (arm)](https://download.influxdata.com/influxdb/releases/v2.8.0/influxdb2-2.8.0_linux_arm64.tar.gz)

   ```sh
   # Use curl to download the amd64 binary.
   curl --location -O \
   https://download.influxdata.com/influxdb/releases/v2.8.0/influxdb2-2.8.0_linux_amd64.tar.gz
   ```

   ```sh
   # Use curl to download the arm64 binary.
   curl --location -O \
   https://download.influxdata.com/influxdb/releases/v2.8.0/influxdb2-2.8.0_linux_arm64.tar.gz
   ```

2. [Choose the InfluxData key-pair for your OS version](#choose-the-influxdata-key-pair-for-your-os-version).

3. Recommended:: Verify the authenticity of the downloaded binary–for example, enter the following command in your terminal.

   *Before running the command for your system, replace `https://repos.influxdata.com/influxdata-archive.key` with the key URL from the preceding step.*

    ```bash
    # amd64
    # Download and import the key
    curl --silent --location https://repos.influxdata.com/influxdata-archive.key \
    | gpg --import - 2>&1 \
    | grep 'InfluxData Package Signing Key <support@influxdata.com>' \
    &&
    # Download and verify the binary's signature file
    curl --silent --location "https://download.influxdata.com/influxdb/releases/v2.8.0/influxdb2-2.8.0_linux_amd64.tar.gz.asc" \
    | gpg --verify - influxdb2-2.8.0_linux_amd64.tar.gz \
    2>&1 | grep 'InfluxData Package Signing Key <support@influxdata.com>'
    ```

    ```bash
    # arm64
    # Download and import the key
    curl --silent --location https://repos.influxdata.com/influxdata-archive.key \
    | gpg --import - 2>&1 \
    | grep 'InfluxData Package Signing Key <support@influxdata.com>' \
    &&
    # Download and verify the binary's signature file
    curl --silent --location "https://download.influxdata.com/influxdb/releases/v2.8.0/influxdb2-2.8.0_linux_arm64.tar.gz.asc" \
    | gpg --verify - influxdb2-2.8.0_linux_arm64.tar.gz \
    2>&1 | grep 'InfluxData Package Signing Key <support@influxdata.com>'
    ```

   If successful, the output is similar to the following:

   ```text
   gpg: Good signature from "InfluxData Package Signing Key <support@influxdata.com>" [unknown]
   ```

4. Extract the downloaded binary–for example, enter the following command for your system:

   ```bash
   # amd64
   tar xvzf ./influxdb2-2.8.0_linux_amd64.tar.gz
   ```

   ```bash
   # arm64
   tar xvzf ./influxdb2-2.8.0_linux_arm64.tar.gz
   ```

5. Optional: Place the extracted `influxd` executable binary in your system `$PATH`.

   ```bash
   # amd64
   sudo cp ./influxdb2-2.8.0/usr/bin/influxd /usr/local/bin/
   ```

   ```bash
   # arm64
   sudo cp ./influxdb2-2.8.0/usr/bin/influxd /usr/local/bin/
   ```

   If you choose to not move the `influxd` binary into your `$PATH`, enter the path to the binary to start the server–for example:

   ```bash
   ./influxdb2-2.8.0/usr/bin/influxd
   ```

[](#recommended--set-appropriate-directory-permissions)

Recommended – Set appropriate directory permissions

To prevent unwanted access to data, set the permissions on the influxdb `data-dir` to not be world readable. If installing on a server, we recommend setting a umask of `0027` to properly permission all newly created files. To set umask, use a UMask directive in a systemd unit file or run Influxdb as a specific user that has the umask properly set–for example, enter the following command in your terminal:

```sh
chmod 0750 ~/.influxdbv2
```

**Windows:**

### System requirements

- Windows 10
- 64-bit AMD architecture
- [Powershell](https://docs.microsoft.com/powershell/) or [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/)

### Command line examples

Use **Powershell** or **WSL** to execute `influx` and `influxd` commands. The command line examples in this documentation use `influx` and `influxd` as if installed on the system `PATH`. If these binaries are not installed on your `PATH`, replace `influx` and `influxd` in the provided examples with `./influx` and `./influxd` respectively.

### InfluxDB and the influx CLI are separate packages

The InfluxDB server ([`influxd`](/influxdb/v2/reference/cli/influxd/)) and the [`influx` CLI](/influxdb/v2/reference/cli/influx/) are packaged and versioned separately.

*You'll install the `influx CLI` in a [later step](#download-install-and-configure-the-influx-cli).*

[InfluxDB v2 (Windows)](https://download.influxdata.com/influxdb/releases/v2.8.0/influxdb2-2.8.0-windows_amd64.zip)

Expand the downloaded archive into `C:\Program Files\InfluxData\` and rename the files if desired.

```powershell
Expand-Archive .\influxdb2-2.8.0-windows_amd64.zip -DestinationPath 'C:\Program Files\InfluxData\'
mv 'C:\Program Files\InfluxData\influxdb2-2.8.0-windows-amd64' 'C:\Program Files\InfluxData\influxdb'
```

[](#recommended--set-appropriate-directory-permissions)

Recommended – Set appropriate directory permissions

To prevent unwanted access to data, we recommend setting the permissions on the influxdb `data-dir` to not be world readable–for example: enter the following commands in your terminal:

```powershell
$acl = Get-Acl "C:\Users\<username>\.influxdbv2"
$accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule("everyone","Read","Deny")
$acl.SetAccessRule($accessRule)
$acl | Set-Acl "C:\Users\<username>\.influxdbv2"
```

**Docker:**

### Install and set up InfluxDB in a container

The following steps show how to use the [Docker CLI](https://docs.docker.com/reference/cli/docker/) to set up and run InfluxDB. but you can also [use Docker Compose](/influxdb/v2/install/use-docker-compose).

*The following guide uses Docker mounted [volumes](https://docs.docker.com/storage/volumes/) to persist InfluxDB configuration and data. Persisting your data to a file system outside the container ensures that your data isn't deleted if you delete the container.*

1. Install [Docker Desktop](https://www.docker.com/get-started/) for your system.

2. Start a Docker container from the [`influxdb` Docker Hub image](https://hub.docker.com/_/influxdb)–for example, in your terminal, enter the `docker run influxdb:2` command with command line flags for initial setup options and file system mounts.

*If you don't specify InfluxDB initial setup options, you can [set up manually](/influxdb/v2/get-started/setup/) later using the UI or CLI in a running container.*

```bash
docker run \
 --name influxdb2 \
 --publish 8086:8086 \
 --mount type=volume,source=influxdb2-data,target=/var/lib/influxdb2 \
 --mount type=volume,source=influxdb2-config,target=/etc/influxdb2 \
 --env DOCKER_INFLUXDB_INIT_MODE=setup \
 --env DOCKER_INFLUXDB_INIT_USERNAME=ADMIN_USERNAME \
 --env DOCKER_INFLUXDB_INIT_PASSWORD=ADMIN_PASSWORD \
 --env DOCKER_INFLUXDB_INIT_ORG=ORG_NAME \
 --env DOCKER_INFLUXDB_INIT_BUCKET=BUCKET_NAME \
 influxdb:2
```

The command passes the following arguments:

- `--publish 8086:8086`: Exposes the InfluxDB [UI](/influxdb/v2/get-started/#influxdb-user-interface-ui) and [HTTP API](/influxdb/v2/reference/api/) on the host's `8086` port.

- `--mount type=volume,source=influxdb2-data,target=/var/lib/influxdb2`: Creates a volume named `influxdb2-data` mapped to the [InfluxDB data directory](/influxdb/v2/reference/internals/file-system-layout/?t=docker#file-system-layout) to persist data outside the container.

- `--mount type=volume,source=influxdb2-config,target=/etc/influxdb2`: Creates a volume named `influxdb2-config` mapped to the [InfluxDB configuration directory](/influxdb/v2/reference/internals/file-system-layout/?t=docker#file-system-layout) to make configurations available outside the container.

- `--env DOCKER_INFLUXDB_INIT_MODE=setup`: Environment variable that invokes the automated setup of the initial organization, user, bucket, and token when creating the container.

- `--env DOCKER_INFLUXDB_INIT_<SETUP_OPTION>`: Environment variables for initial setup options–replace the following with your own values:

  - `ADMIN_USERNAME`: The username for the initial [user](/influxdb/v2/admin/users/)–an admin user with an API [Operator token](/influxdb/v2/admin/tokens/#operator-token).
  - `ADMIN_PASSWORD`: The password for the initial [user](/influxdb/v2/admin/users/).
  - `ORG_NAME`: The name for the initial [organization](/influxdb/v2/admin/organizations/).
  - `BUCKET_NAME`: The name for the initial [bucket](/influxdb/v2/admin/buckets/).

If successful, the command starts InfluxDB initialized with the user, organization, bucket, and *[Operator token](/influxdb/v2/admin/tokens/#operator-token)*, and logs to stdout.

You can view the Operator token in the `/etc/influxdb2/influx-configs` file and use it to authorize [creating an All Access token](#examples). For more information, see [API token types](/influxdb/v2/admin/tokens/#api-token-types).

*To run the InfluxDB container in [detached mode](https://docs.docker.com/engine/reference/run/#detached-vs-foreground), include the `--detach` flag in the `docker run` command.*

For more InfluxDB configuration options, see the [`influxdb` Docker Hub image](https://hub.docker.com/_/influxdb) documentation.

### Run InfluxDB CLI commands in a container

When you start a container using the `influxdb` Docker Hub image, it also installs the [`influx` CLI](/influxdb/v2/tools/influx-cli/) in the container. With InfluxDB setup and running in the container, you can use the Docker CLI [`docker exec`](https://docs.docker.com/reference/cli/docker/container/exec/) command to interact with the `influx` and `influxd` CLIs inside the container.

#### Syntax

```bash
docker exec -it <CONTAINER_NAME> <CLI_NAME> <COMMAND>`
```

#### Examples

```bash
# Create an All Access token
docker exec -it influxdb2 influx auth create \
  --all-access \
  --token OPERATOR_TOKEN
```

```bash
# List CLI configurations
docker exec -it influxdb2 influx config ls
```

```bash
# View the server configuration
docker exec -it influxdb2 influx server-config
# Inspect server details
docker exec -it influxdb2 influxd inspect -d
```

### Manage files in mounted volumes

To copy files, such as the InfluxDB server `config.yml` file, between your local file system and a volume, use the [`docker container cp` command](https://docs.docker.com/reference/cli/docker/container/cp/).

**Kubernetes:**

### Install InfluxDB in a Kubernetes cluster

The instructions below use **minikube** or **kind**, but the steps should be similar in any Kubernetes cluster. InfluxData also makes [Helm charts](https://github.com/influxdata/helm-charts) available.

1. Install [minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/) or [kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation).

2. Start a local cluster:

   ```bash
   # with minikube
   minikube start
   ```

   ```bash
   # with kind
   kind create cluster
   ```

3. Apply the [sample InfluxDB configuration](https://github.com/influxdata/docs-v2/blob/master/static/downloads/influxdb-k8-minikube.yaml) by running:

   ```bash
   kubectl apply -f https://raw.githubusercontent.com/influxdata/docs-v2/master/static/downloads/influxdb-k8-minikube.yaml
   ```

   This creates an `influxdb` Namespace, Service, and StatefulSet. A PersistentVolumeClaim is also created to store data written to InfluxDB.

   **Important**: always inspect YAML manifests before running `kubectl apply -f <url>`!

4. Ensure the Pod is running:

   ```bash
   kubectl get pods -n influxdb
   ```

5. Ensure the Service is available:

   ```bash
   kubectl describe service -n influxdb influxdb
   ```

   You should see an IP address after `Endpoints` in the command's output.

6. Forward port 8086 from inside the cluster to localhost:

   ```bash
   kubectl port-forward -n influxdb service/influxdb 8086:8086
   ```

**Raspberry Pi:**

### Requirements

To run InfluxDB on Raspberry Pi, you need:

- a Raspberry Pi 4+ or 400
- a 64-bit operating system. Recommended:: a [64-bit version of Ubuntu](https://ubuntu.com/download/raspberry-pi) of Ubuntu Desktop or Ubuntu Server compatible with 64-bit Raspberry Pi.

### Install Linux binaries

Follow the [Linux installation instructions](/influxdb/v2/install/?t=Linux#install-linux) to install InfluxDB on a Raspberry Pi.

### Monitor your Raspberry Pi

Use the [InfluxDB Raspberry Pi template](/influxdb/cloud/monitor-alert/templates/infrastructure/raspberry-pi/) to easily configure collecting and visualizing system metrics for the Raspberry Pi.

### Monitor 32-bit Raspberry Pi systems

If you have a 32-bit Raspberry Pi, [use Telegraf](/telegraf/v1/) to collect and send data to:

- [InfluxDB OSS](/influxdb/v2/), running on a 64-bit system
- InfluxDB Cloud with a [**Free Tier**](/influxdb/cloud/account-management/pricing-plans/#free-plan) account
- InfluxDB Cloud with a paid [**Usage-Based**](/influxdb/cloud/account-management/pricing-plans/#usage-based-plan) account with relaxed resource restrictions.

<!-- End tabbed content -->

## Start InfluxDB

If it isn't already running, follow the instructions to start InfluxDB on your system:

<!-- Tabbed content: Select one of the following options -->

**macOS:**

To start InfluxDB, run the `influxd` daemon:

```bash
influxd
```

### (macOS Catalina and newer) Authorize the influxd binary

macOS requires downloaded binaries to be signed by registered Apple developers. Currently, when you first attempt to run `influxd`, macOS will prevent it from running.

To manually authorize the `influxd` binary, follow the instructions for your macOS version to allow downloaded applications.

#### Run InfluxDB on macOS Ventura

1. Follow the preceding instructions to attempt to start `influxd`.
2. Open **System Settings** and click **Privacy & Security**.
3. Under the **Security** heading, there is a message about "influxd" being blocked, click **Allow Anyway**.
4. When prompted, enter your password to allow the setting.
5. Close **System Settings**.
6. Attempt to start `influxd`.
7. A prompt appears with the message *"macOS cannot verify the developer of "influxd"…""*. Click **Open**.

#### Run InfluxDB on macOS Catalina

1. Attempt to start `influxd`.
2. Open **System Preferences** and click **Security & Privacy**.
3. Under the **General** tab, there is a message about `influxd` being blocked. Click **Open Anyway**.

We are in the process of updating the build process to ensure released binaries are signed by InfluxData.

### "too many open files" errors

After running `influxd`, you might see an error in the log output like the following:

```text
too many open files
```

To resolve this error, follow the [recommended steps](https://unix.stackexchange.com/a/221988/471569) to increase file and process limits for your operating system version then restart `influxd`.

**Linux:**

If InfluxDB was installed as a systemd service, systemd manages the `influxd` daemon and no further action is required. If the binary was manually downloaded and added to the system `$PATH`, start the `influxd` daemon with the following command:

```bash
influxd
```

**Windows:**

In **Powershell**, navigate into `C:\Program Files\InfluxData\influxdb` and start InfluxDB by running the `influxd` daemon:

```powershell
cd -Path 'C:\Program Files\InfluxData\influxdb'
./influxd
```

#### Grant network access

When starting InfluxDB for the first time, **Windows Defender** appears with the following message:

> Windows Defender Firewall has blocked some features of this app.

1. Select **Private networks, such as my home or work network**.
2. Click **Allow access**.

**Docker:**

To use the Docker CLI to start an existing container, enter the following command:

```bash
docker start influxdb2
```

Replace `influxdb2` with the name of your container.

To start a new container, follow instructions to [install and set up InfluxDB in a container](?t=docker#install-and-set-up-influxdb-in-a-container).

**Kubernetes:**

To start InfluxDB using Kubernetes, follow instructions to [install InfluxDB in a Kubernetes cluster](?t=kubernetes#download-and-install-influxdb-v2).

<!-- End tabbed content -->

If successful, you can view the InfluxDB UI at [http://localhost:8086](http://localhost:8086).

InfluxDB starts with default settings, including the following:

- `http-bind-address=:8086`: Uses port `8086` (TCP) for InfluxDB UI and HTTP API client-server communication.
- `reporting-disabled=false`: Sends InfluxDB telemetry information back to InfluxData.

To override default settings, specify [configuration options](/influxdb/v2/reference/config-options) when starting InfluxDB–for example:

[](#configure-the-port-or-address)

Configure the port or address

By default, the InfluxDB UI and HTTP API use port `8086`.

To specify a different port or address, override the [`http-bind-address` option](/influxdb/v2/reference/config-options/#http-bind-address) when starting `influxd`–for example:

<!-- Tabbed content: Select one of the following options -->

**Linux:**

```bash
influxd --http-bind-address
```

**Windows Powershell:**

```powershell
./influxd --http-bind-address
```

<!-- End tabbed content -->

[](#opt-out-of-telemetry-reporting)

Opt-out of telemetry reporting

By default, InfluxDB sends telemetry data back to InfluxData. The [InfluxData telemetry](https://www.influxdata.com/telemetry) page provides information about what data is collected and how it is used.

To opt-out of sending telemetry data back to InfluxData, specify the [`reporting-disabled` option](/influxdb/v2/reference/config-options/#reporting-disabled) when starting `influxd`–for example:

<!-- Tabbed content: Select one of the following options -->

**Linux:**

```bash
influxd --reporting-disabled
```

**Windows Powershell:**

```powershell
./influxd --reporting-disabled
```

<!-- End tabbed content -->

For information about InfluxDB v2 default settings and how to override them, see [InfluxDB configuration options](/influxdb/v2/reference/config-options/).

With InfluxDB installed and initialized, [get started](/influxdb/v2/get-started/) writing and querying data.

## Download, install, and configure the `influx` CLI

Recommended:: Install the `influx` CLI, which provides a simple way to interact with InfluxDB from a command line. For detailed installation and setup instructions, see [Use the influx CLI](/influxdb/v2/tools/influx-cli/).

### InfluxDB and the influx CLI are separate packages

The InfluxDB server ([`influxd`](/influxdb/v2/reference/cli/influxd/)) and the [`influx` CLI](/influxdb/v2/reference/cli/influx/) are packaged and versioned separately. Some install methods (for example, the InfluxDB Docker Hub image) include both.

### Related

- [influx auth](/influxdb/v2/reference/cli/influx/auth/)
- [influx config](/influxdb/v2/reference/cli/influx/config/)
- [influx - InfluxDB command line interface](/influxdb/v2/reference/cli/influx/)
- [Manage API tokens](/influxdb/v2/admin/tokens/)

[install](/influxdb/v2/tags/install/)

---

## Get started with InfluxDB

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

InfluxDB 2.8 is the platform purpose-built to collect, store, process and visualize time series data. **Time series data** is a sequence of data points indexed in time order. Data points typically consist of successive measurements made from the same source and are used to track changes over time. Examples of time series data include:

- Industrial sensor data
- Server performance metrics
- Heartbeats per minute
- Electrical activity in the brain
- Rainfall measurements
- Stock prices

This multi-part tutorial walks you through writing time series data to InfluxDB 2.8, querying that data, processing and alerting on the data, and then visualizing the data.

## Key concepts before you get started

Before you get started using InfluxDB, it’s important to understand how time series data is organized and stored in InfluxDB and some key definitions that are used throughout this documentation.

### Data organization

The InfluxDB data model organizes time series data into buckets and measurements. A bucket can contain multiple measurements. Measurements contain multiple tags and fields.

- **Bucket**: Named location where time series data is stored. A bucket can contain multiple *measurements*.
  - **Measurement**: Logical grouping for time series data. All *points* in a given measurement should have the same *tags*. A measurement contains multiple *tags* and *fields*.
    - **Tags**: Key-value pairs with values that differ, but do not change often. Tags are meant for storing metadata for each point–for example, something to identify the source of the data like host, location, station, etc.
    - **Fields**: Key-value pairs with values that change over time–for example: temperature, pressure, stock price, etc.
    - **Timestamp**: Timestamp associated with the data. When stored on disk and queried, all data is ordered by time.

*For detailed information and examples of the InfluxDB data model, see [Data elements](/influxdb/v2/reference/key-concepts/data-elements/).*

### Important definitions

The following are important definitions to understand when using InfluxDB:

- **Point**: Single data record identified by its *measurement, tag keys, tag values, field key, and timestamp*.
- **Series**: A group of points with the same *measurement, tag keys, and tag values*.

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

## Tools to use

Throughout this tutorial, there are multiple tools you can use to interact with InfluxDB 2.8. Examples are provided for each of the following:

- [InfluxDB user interface (UI)](#influxdb-user-interface-ui)
- [`influx` CLI](#influx-cli)
- [InfluxDB HTTP API](#influxdb-http-api)

### InfluxDB user interface (UI)

The InfluxDB UI provides a web-based visual interface for interacting with and managing InfluxDB. The UI is packaged with InfluxDB and runs as part of the InfluxDB service. To access the UI, with InfluxDB running, visit [localhost:8086](http://localhost:8086) in your browser.

### `influx` CLI

The `influx` CLI lets you interact with and manage InfluxDB 2.8 from a command line. The CLI is packaged separately from InfluxDB and must be downloaded and installed separately.

For detailed CLI installation instructions, see [Use the influx CLI](/influxdb/v2/tools/influx-cli/).

### InfluxDB HTTP API

The [InfluxDB API](/influxdb/v2/reference/api/) provides a simple way to interact with the InfluxDB 2.8 using HTTP(S) clients. Examples in this tutorial use cURL, but any HTTP(S) client will work.

### InfluxDB client libraries

[InfluxDB client libraries](/influxdb/v2/api-guide/client-libraries/) are language-specific clients that interact with the InfluxDB HTTP API. Examples for client libraries are not provided in this tutorial, but these can be used to perform all the actions outlined in this tutorial.

## Authorization

**InfluxDB 2.8 requires authentication** using [API tokens](/influxdb/v2/admin/tokens/). Each API token is associated with a user and a specific set of permissions for InfluxDB resources.

[Set up InfluxDB](/influxdb/v2/get-started/setup/)

![InfluxDB University](/svgs/influxdbu-full-white.svg)

### InfluxDB Essentials

Learn how to write, query, and visualize data in InfluxDB in this **free** InfluxDB University course.

[Take the course](https://university.influxdata.com/courses/influxdb-essentials-tutorial/)

[get-started](/influxdb/v2/tags/get-started/)

---

## Develop with the InfluxDB API

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

The InfluxDB v2 API provides a programmatic interface for interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.

## Developer guides

- [API Quick Start](/influxdb/v2/api-guide/api_intro/)

## InfluxDB client libraries

InfluxDB client libraries are language-specific packages that integrate with the InfluxDB v2 API. For tutorials and information about client libraries, see [InfluxDB client libraries](/influxdb/v2/api-guide/client-libraries/).

## InfluxDB v2 API documentation

[InfluxDB OSS 2.8 API documentation](/influxdb/v2/api/)

### View InfluxDB API documentation locally

InfluxDB API documentation is built into the `influxd` service and represents the API specific to the current version of InfluxDB. To view the API documentation locally, [start InfluxDB](/influxdb/v2/get-started/#start-influxdb) and visit the `/docs` endpoint in a browser ([localhost:8086/docs](http://localhost:8086/docs)).

## InfluxDB v1 compatibility API documentation

The InfluxDB v2 API includes [InfluxDB v1 compatibility endpoints and authentication](/influxdb/v2/api-guide/influxdb-1x/) that work with InfluxDB 1.x client libraries and third-party integrations like [Grafana](https://grafana.com) and others.

[View full v1 compatibility API documentation](/influxdb/v2/api/v2/#tag/Compatibility-endpoints)

[api](/influxdb/v2/tags/api/)

---

## Administer InfluxDB

This page documents an earlier version of InfluxDB OSS. [InfluxDB 3 Core](/influxdb3/core/) is the latest stable version.

Use the InfluxDB API, user interface (UI), and CLIs to perform administrative tasks in InfluxDB.

### [Identify InfluxDB OSS v2 version](/influxdb/v2/admin/identify-version/)

Learn how to identify your InfluxDB OSS v2 version using command-line tools, the UI, and HTTP endpoints.

### [Manage organizations](/influxdb/v2/admin/organizations/)

Manage organizations in InfluxDB using the InfluxDB UI or the influx CLI.

### [Manage API tokens](/influxdb/v2/admin/tokens/)

Manage API tokens in InfluxDB using the InfluxDB UI or the influx CLI.

### [Manage buckets](/influxdb/v2/admin/buckets/)

Manage buckets in InfluxDB using the InfluxDB UI or the influx CLI.

### [Manage users](/influxdb/v2/admin/users/)

Manage users in InfluxDB using the InfluxDB UI or the influx CLI.

### [Manage security and authorization](/influxdb/v2/admin/security/)

Security, access control, and sensitive secret handling are incredibly important when handling any sort of sensitive data. This section provides information about managing the security of your InfluxDB instance.

### [Manage secrets](/influxdb/v2/admin/secrets/)

Manage, use, and store secrets in InfluxDB.

### [Back up and restore data](/influxdb/v2/admin/backup-restore/)

InfluxDB provides tools that let you back up and restore data and metadata stored in InfluxDB.

### [Manage InfluxDB internal systems](/influxdb/v2/admin/internals/)

Manage the internal systems of InfluxDB such as the Time Series Index (TSI), the time-structured merge tree (TSM) storage engine, and the write-ahead log (WAL).

### [Manage InfluxDB logs](/influxdb/v2/admin/logs/)

Learn how to configure, manage, and process your InfluxDB logs.

