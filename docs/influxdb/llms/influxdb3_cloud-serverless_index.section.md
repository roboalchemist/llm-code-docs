---
title: InfluxDB Cloud Serverless documentation
description: InfluxDB Cloud Serverless is a hosted and managed version of InfluxDB 3, the time series platform designed to handle high write and query loads. Learn how to use and leverage InfluxDB Cloud Serverless in use cases such as monitoring metrics, IoT data, and events.
url: https://docs.influxdata.com/influxdb3/cloud-serverless/
product: InfluxDB Cloud Serverless
type: section
pages: 9
estimated_tokens: 11576
child_pages:
  - url: https://docs.influxdata.com/influxdb3/cloud-serverless/write-data/
    title: Write data to InfluxDB
  - url: https://docs.influxdata.com/influxdb3/cloud-serverless/sign-up/
    title: Sign up for InfluxDB Cloud Serverless
  - url: https://docs.influxdata.com/influxdb3/cloud-serverless/reference/
    title: InfluxDB Cloud Serverless reference documentation
  - url: https://docs.influxdata.com/influxdb3/cloud-serverless/query-data/
    title: Query data in InfluxDB Cloud
  - url: https://docs.influxdata.com/influxdb3/cloud-serverless/process-data/
    title: Process and visualize data stored in InfluxDB
  - url: https://docs.influxdata.com/influxdb3/cloud-serverless/guides/
    title: InfluxDB guides
  - url: https://docs.influxdata.com/influxdb3/cloud-serverless/get-started/
    title: Get started with InfluxDB Cloud Serverless
  - url: https://docs.influxdata.com/influxdb3/cloud-serverless/admin/
    title: Administer InfluxDB Cloud
---

# InfluxDB Cloud Serverless documentation

This InfluxDB Cloud documentation applies to all [organizations](/influxdb3/cloud-serverless/admin/organizations/) created through **cloud2.influxdata.com** on or after **January 31, 2023** that are powered by the InfluxDB 3 storage engine. If your organization was created before this date or through the Google Cloud Platform (GCP) or Azure marketplaces, see the [InfluxDB Cloud (TSM) documentation](/influxdb/cloud/).

To see which storage engine your organization is using, find the **InfluxDB Cloud powered by** link in your [InfluxDB Cloud organization homepage](https://cloud2.influxdata.com) version information. If your organization is using InfluxDB 3, you’ll see **InfluxDB Cloud Serverless** followed by the version number.

#### InfluxDB 3 and Flux

InfluxDB Cloud Serverless and other InfluxDB 3 products don’t support Flux. Although Flux might still work with InfluxDB Cloud Serverless, it isn’t officially supported or optimized for InfluxDB 3.

Flux is now in maintenance mode. For more information, see [The future of Flux](/flux/v0/future-of-flux).

InfluxDB Cloud Serverless is a hosted and managed version of InfluxDB backed by InfluxDB 3, the time series platform designed to handle high write and query loads. Learn how to use and leverage InfluxDB Cloud Serverless in use cases such as monitoring metrics, IoT data, and event monitoring.

[Get started with InfluxDB Cloud Serverless](/influxdb3/cloud-serverless/get-started/)

## InfluxDB 3

**InfluxDB 3** is InfluxDB’s next generation that unlocks series limitations present in the Time Structured Merge Tree (TSM) storage engine and allows infinite series cardinality without any impact on overall database performance. It also brings native **SQL support** and improved InfluxQL performance.

View the following video for more information about InfluxDB 3:

## How do you use InfluxDB 3?

All InfluxDB Cloud [accounts](/influxdb3/cloud-serverless/admin/accounts/) and [organizations](/influxdb3/cloud-serverless/admin/organizations/) created through [cloud2.influxdata.com](https://cloud2.influxdata.com) on or after **January 31, 2023** are powered by the InfluxDB 3.

To see which storage engine your organization is using, find the **InfluxDB Cloud powered by** link in your [InfluxDB Cloud organization homepage](https://cloud2.influxdata.com) version information. If your organization is using InfluxDB 3, you’ll see **InfluxDB Cloud Serverless** followed by the version number.


---

## Write data to InfluxDB

Write data to InfluxDB Cloud Serverless using the following tools and methods:

#### Choose the write endpoint for your workload

When bringing existing v1 write workloads, use the InfluxDB Cloud Serverless HTTP API [`/write` endpoint](/influxdb3/cloud-serverless/guides/api-compatibility/v1/). When creating new write workloads, use the HTTP API [`/api/v2/write` endpoint](/influxdb3/cloud-serverless/guides/api-compatibility/v2/).

### [Use Telegraf to write data](/influxdb3/cloud-serverless/write-data/use-telegraf/)

Use Telegraf to collect and write data to InfluxDB. Create Telegraf configurations in the InfluxDB UI or manually configure Telegraf.

### [Write CSV data to InfluxDB](/influxdb3/cloud-serverless/write-data/csv/)

Use the `influx CLI`, InfluxDB user interface, or Telegraf to write CSV data to InfluxDB.

### [Write line protocol data to InfluxDB Cloud Serverless](/influxdb3/cloud-serverless/write-data/line-protocol/)

Use Telegraf and API clients to write line protocol data to InfluxDB Cloud Serverless.

### [Best practices for writing data](/influxdb3/cloud-serverless/write-data/best-practices/)

Learn about the recommendations and best practices for writing data to InfluxDB.

### [Troubleshoot issues writing data](/influxdb3/cloud-serverless/write-data/troubleshoot/)

Troubleshoot issues writing data. Find response codes for failed writes. Discover how writes fail, from exceeding rate or payload limits, to syntax errors and schema conflicts.

### [Delete data](/influxdb3/cloud-serverless/write-data/delete-data/)

Use measurements, tags, and timestamp columns to avoid querying unwanted data.

### [Use the v1 write API](/influxdb3/cloud-serverless/write-data/api/v1-http/)

Use the InfluxDB v1 HTTP write API to write data stored in InfluxDB Cloud Serverless.

```sh
curl "https://cloud2.influxdata.com/write?db=DATABASE_NAME&rp=RETENTION_POLICY&precision=s" \
  --header "Authorization: Token API_TOKEN" \
  --header "Content-type: text/plain; charset=utf-8" \
  --data-binary 'home,room=kitchen temp=72 1463683075'
```

#### Related

-   [InfluxDB v1 API /write endpoint](/influxdb3/cloud-serverless/api/#tag/Write)
-   [Line protocol](/influxdb3/cloud-serverless/reference/syntax/line-protocol/)
-   [influx write](/influxdb3/cloud-serverless/reference/cli/influx/write/)


---

## Sign up for InfluxDB Cloud Serverless

InfluxDB Cloud Serverless is a fully managed and hosted version of InfluxDB 3, the time series platform purpose-built to collect and store time series data.

-   [Start for free](#start-for-free)
-   [Sign up](#sign-up)
-   [(Optional) Download, install, and use the influx CLI](#optional-download-install-and-use-the-influx-cli)
-   [Sign in](#sign-in)
-   [Get started working with data](#get-started-working-with-data)

## Start for free

Start using InfluxDB Cloud Serverless at no cost with the [Free Plan](/influxdb3/cloud-serverless/admin/accounts/pricing-plans/#free-plan). Use it as much and as long as you like within the plan’s rate-limits. [Limits](/influxdb3/cloud-serverless/admin/account/limits/) are designed to let you monitor 5-10 sensors, stacks or servers comfortably.

Users on the Free Plan are limited to one organization.

## Sign up

1. Choose one of the following:
    
    #### Subscribe through InfluxData
    
    To subscribe to an InfluxDB Cloud Serverless **Free Plan** through InfluxData, go to [InfluxDB Cloud](https://cloud2.influxdata.com/).
    
    -   To use social sign-on, click **Google** or **Microsoft**. Note that social sign-on does not support email aliases.
    -   Sign up with email by entering your name, email address, and password, and then click **Create Account**.
    
    If you originally signed up with email but want to enable social sign-on (SSO), log in through your SSO provider using the same email address you used to create your InfluxDB Cloud Serverless account.
    
    #### Subscribe through a cloud provider
    
    To subscribe to an InfluxDB Cloud Serverless **Usage-Based** plan and pay through your **Amazon Web Services (AWS)** account:
    
    1. Sign in to AWS, navigate to the [InfluxDB Cloud product on AWS Marketplace](https://aws.amazon.com/marketplace/pp/B08234JZPS/?href=_ptnr_web_docs_gettingstarted), and follow the prompts to subscribe.
    2. After you click **Set Up Your Account**, enter your credentials, and then click **Start Now**.
    
    All usage charges will be paid through the subscribed AWS account.
    
    Currently, we do **not support** using an existing InfluxDB Cloud account to sign up for an InfluxDB Cloud plan through the AWS Marketplace.
    
2. If you signed up with your email address, InfluxDB Cloud requires email verification to complete the sign up process. Verify your email address by opening the email sent to the address you provided and clicking **Verify Your Email**.
    
3. (If you subscribed through InfluxData) Choose your cloud provider.
    
4. Select a provider and region for your InfluxDB Cloud Serverless instance. The following are available:
    
    -   **Amazon Web Services (AWS)**
        -   US East (Virginia)
        -   EU Frankfurt
5. Enter your company name.
    
6. (If you subscribed through InfluxData) Review the terms of the agreement, and then select **I have viewed and agree to InfluxDB Cloud Services Subscription Agreement and InfluxData Global Data Processing Agreement**. For details on the agreements, see the [InfluxDB Cloud: Services Subscription Agreement](https://www.influxdata.com/legal/terms-of-use/) and the [InfluxData Global Data Processing Agreement](https://www.influxdata.com/legal/influxdata-global-data-processing-agreement/).
    
7. Click **Continue**, and then choose your plan:
    
    -   To upgrade to a Usage-Based plan, click **Upgrade Now**, set your limits (you may opt to receive an email when your usage exceeds the amount you enter in the **Limit ($1 minimum)** field). Next, enter your payment information and billing address, and then click **Upgrade**. A Ready To Rock confirmation appears; click **Start building your team**. Your plan will be upgraded and InfluxDB Cloud Serverless opens with a default organization and bucket (both created from your email address). To review your usage and billing details at any time, see how to [access billing details](/influxdb3/cloud-serverless/admin/billing/#access-billing-details).
    -   To keep the free plan, click **Keep**. InfluxDB Cloud Serverless opens with a default organization and bucket (both created from your email address). *To update organization and bucket names, see [Update an organization](/influxdb3/cloud-serverless/admin/organizations/update-org/) and [Update a bucket](/influxdb3/cloud-serverless/admin/buckets/update-bucket/#update-a-buckets-name-in-the-influxdb-ui).*
    -   To upgrade to an Annual plan, click **Contact Sales**, enter your information, and then click **Send**. Our team will contact you as soon as possible.

## (Optional) Download, install, and use the influx CLI

To use the `influx` CLI to manage and interact with your InfluxDB Cloud instance, complete the following steps:

<!-- Tabbed content: Select one of the following options -->

**macOS:**

#### Step 1: Download influx CLI for macOS

Click the following button to download and install `influx` CLI for macOS.

[influx CLI (macOS)](https://dl.influxdata.com/influxdb/releases/influxdb2-client-2.7.5-darwin-amd64.tar.gz)

#### Step 2: Unpackage the influx binary

**Note:** The commands below are examples. Adjust the file names, paths, and utilities to your own needs.

To unpackage the downloaded archive, **double click the archive file in Finder** or run the following command in a macOS command prompt application such **Terminal** or **[iTerm2](https://www.iterm2.com/)**:

```sh
# Unpackage contents to the current working directory
tar zxvf ~/Downloads/influxdb2-client-2.7.5-darwin-amd64.tar.gz
```

#### Step 3: (Optional) Place the binary in your $PATH

If you choose, you can place `influx` in your `$PATH` or you can prefix the executable with `./` to run in place. If the binary is on your $PATH, you can run `influx` from any directory. Otherwise, you must specify the location of the CLI (for example, `./influx`or `path/to/influx`).

**Note:** If you have the 1.x binary on your $PATH, moving the 2.0 binary to your $PATH will overwrite the 1.x binary because they have the same name.

```sh
# Copy the influx binary to your $PATH
sudo cp influxdb2-client-2.7.5-darwin-amd64/influx /usr/local/bin/
```

If you rename the binary, all references to `influx` in this documentation refer to the renamed binary.

#### Step 4: (macOS Catalina and newer) Authorize InfluxDB binaries

If running `influx` on macOS Catalina, you must manually authorize the `influx` binary in the **Security & Privacy** section of **System Preferences**.

#### Step 5: Set up a configuration profile

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

#### Step 6: Learn `influx` CLI commands

To see all available `influx` commands, type `influx -h` or check out [influx - InfluxDB command line interface](/influxdb/cloud/reference/cli/influx/).

**Linux:**

#### Step 1: Download influx CLI for Linux

Click one of the following buttons to download and install the `influx` CLI appropriate for your chipset.

[influx CLI (amd64)](https://dl.influxdata.com/influxdb/releases/influxdb2-client-2.7.5-linux-amd64.tar.gz) [influx CLI (arm)](https://dl.influxdata.com/influxdb/releases/influxdb2-client-2.7.5-linux-arm64.tar.gz)

#### Step 2: Unpackage the influx binary

**Note:** The commands below are examples. Adjust the file names, paths, and utilities to your own needs.

```sh
# Unpackage contents to the current working directory
tar xvfz influxdb2-client-2.7.5-linux-amd64.tar.gz
```

#### Step 3: (Optional) Place the binary in your $PATH

If you choose, you can place `influx` in your `$PATH` or you can prefix the executable with `./` to run in place. If the binary is on your $PATH, you can run `influx` from any directory. Otherwise, you must specify the location of the CLI (for example, `./influx`or `path/to/influx`).

**Note:** If you have the 1.x binary on your $PATH, moving the 2.0 binary to your $PATH will overwrite the 1.x binary because they have the same name.

```sh
# Copy the influx and influxd binary to your $PATH
sudo cp influxdb2-client-2.7.5-linux-amd64/influx /usr/local/bin/
```

If you rename the binary, all references to `influx` in this documentation refer to the renamed binary.

#### Step 4: Set up a configuration profile

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

#### Step 5: Learn `influx` CLI commands

To see all available `influx` commands, type `influx -h` or check out [influx - InfluxDB command line interface](/influxdb/cloud/reference/cli/influx/).

**Windows:**

#### Step 1: Download influx CLI for Windows

Click the following button to download and install `influx` CLI for Windows.

[influx CLI (Windows)](https://dl.influxdata.com/influxdb/releases/influxdb2-client-2.7.5-windows-amd64.zip)

#### Step 2: Expand the downloaded archive

Expand the downloaded archive into `C:\Program Files\InfluxData\influxdb`.

#### Step 3: Grant network access

When using the `influx` CLI for the first time, Windows Defender will appear with the following message: `Windows Defender Firewall has blocked some features of this app.`

1. Select **Private networks, such as my home or work network**.
2. Click **Allow access**.

#### Step 4: Learn `influx` CLI commands

To see all available `influx` commands, type `influx -h` or check out [influx - InfluxDB command line interface](/influxdb/cloud/reference/cli/influx/).

<!-- End tabbed content -->

## Sign in

Sign in to [InfluxDB Cloud Serverless](https://cloud2.influxdata.com) using your email address and password.

[Sign in to InfluxDB Cloud Serverless now](https://cloud2.influxdata.com)

## Get started working with data

To learn how to get started working with time series data, see [Get Started](/influxdb3/cloud-serverless/get-started).


---

## InfluxDB Cloud Serverless reference documentation

### [SQL reference documentation](/influxdb3/cloud-serverless/reference/sql/)

Learn the SQL syntax and structure used to query InfluxDB.

### [InfluxQL reference documentation](/influxdb3/cloud-serverless/reference/influxql/)

InfluxQL is an SQL-like query language for interacting with data in InfluxDB.

### [Command line tools](/influxdb3/cloud-serverless/reference/cli/)

InfluxDB provides command line tools designed to aid in managing and working with InfluxDB from the command line.

### [InfluxDB HTTP API](/influxdb3/cloud-serverless/reference/api/)

The InfluxDB HTTP API provides a programmatic interface for interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/write` or InfluxDB v1 endpoints.

### [API client libraries](/influxdb3/cloud-serverless/reference/client-libraries/)

InfluxDB client libraries are language-specific tools that integrate with InfluxDB APIs. View the list of available client libraries.

### [InfluxDB syntaxes](/influxdb3/cloud-serverless/reference/syntax/)

InfluxDB uses a handful of languages and syntaxes to perform tasks such as writing, querying, processing, and deleting data.

### [InfluxDB Cloud Serverless regions](/influxdb3/cloud-serverless/reference/regions/)

InfluxDB Cloud Serverless is available on multiple cloud providers and in multiple regions. Each region has a unique URL and API endpoint.

### [InfluxDB Cloud Serverless internals](/influxdb3/cloud-serverless/reference/internals/)

Learn about InfluxDB Cloud Serverless internal systems and mechanisms.

### [Policies and procedures](/influxdb3/cloud-serverless/reference/policies/)

InfluxData product policies and procedures.

### [Sample data](/influxdb3/cloud-serverless/reference/sample-data/)

Sample datasets are used throughout the the InfluxDB Cloud Serverless documentation to demonstrate functionality. Use the following sample datasets to replicate provided examples.

### [Glossary](/influxdb3/cloud-serverless/reference/glossary/)

Terms related to InfluxData products and platforms.

### [Use the InfluxDB documentation MCP server](/influxdb3/cloud-serverless/reference/mcp-server/)

Query InfluxDB Cloud Serverless documentation from your IDE using the InfluxDB documentation MCP server.


---

## Query data in InfluxDB Cloud

Learn to query data stored in InfluxDB.

#### Choose the query method for your workload

-   For new query workloads, use one of the many available [Flight clients](/influxdb3/cloud-serverless/tags/flight-client/) and SQL or InfluxQL.
-   [Use the HTTP API `/query` endpoint and InfluxQL](/influxdb3/cloud-serverless/query-data/execute-queries/v1-http/) when you bring existing v1 query workloads to InfluxDB Cloud Serverless.

### [Query data with SQL](/influxdb3/cloud-serverless/query-data/sql/)

Learn to query data stored in InfluxDB Cloud Serverless using SQL.

### [Query data with InfluxQL](/influxdb3/cloud-serverless/query-data/influxql/)

Learn to use InfluxQL to query data stored in InfluxDB Cloud Serverless.

### [Execute queries](/influxdb3/cloud-serverless/query-data/execute-queries/)

Use tools and libraries to query data stored in InfluxDB Cloud Serverless.

### [Troubleshoot and optimize queries](/influxdb3/cloud-serverless/query-data/troubleshoot-and-optimize/)

Troubleshoot errors and optimize performance for SQL and InfluxQL queries in InfluxDB. Use observability tools to view query execution and metrics.


---

## Process and visualize data stored in InfluxDB

Learn how to process, analyze, and visualize data stored in InfluxDB and perform tasks like modifying and storing modified data, applying advanced downsampling techniques, sending alerts, and more.

### [Downsample data stored in InfluxDB](/influxdb3/cloud-serverless/process-data/downsample/)

Learn about different methods for querying and downsampling time series data stored in InfluxDB.

### [Summarize query results and data distribution](/influxdb3/cloud-serverless/process-data/summarize/)

Query data stored in InfluxDB and use tools like pandas to summarize the results schema and distribution.

### [Use data analysis tools](/influxdb3/cloud-serverless/process-data/tools/)

Use popular data analysis tools to analyze time series data stored in an InfluxDB Cloud Serverless bucket.

### [Visualize data](/influxdb3/cloud-serverless/process-data/visualize/)

Use visualization tools like Grafana, Superset, and others to visualize time series data stored in InfluxDB.

### [Send alerts using data in InfluxDB](/influxdb3/cloud-serverless/process-data/send-alerts/)

Query, analyze, and send alerts using time series data stored in InfluxDB.


---

## InfluxDB guides

Learn how to integrate with and perform specific operations on data stored in InfluxDB Cloud Serverless.

### [Learn to use APIs for your workloads](/influxdb3/cloud-serverless/guides/api-compatibility/)

Choose the API and tools that fit your workload. Learn how to authenticate, write, and query using Telegraf, client libraries, and HTTP clients.

### [Migrate data to InfluxDB Cloud Serverless](/influxdb3/cloud-serverless/guides/migrate-data/)

Migrate data from InfluxDB powered by TSM (OSS, Enterprise, or Cloud) to InfluxDB Cloud Serverless.

### [Prototype your app on InfluxDB Cloud Serverless](/influxdb3/cloud-serverless/guides/prototype-evaluation/)

Utilize InfluxDB Cloud Serverless to prototype your production application and then move it to InfluxDB Cloud Dedicated. Learn about important differences between Cloud Serverless and Cloud Dedicated and best practices for building an application prototype on Cloud Serverless.


---

## Get started with InfluxDB Cloud Serverless

InfluxDB Cloud Serverless is the platform purpose-built to collect, store, process and visualize time series data. The InfluxDB 3.0 storage engine provides a number of benefits including nearly unlimited series cardinality, improved query performance, and interoperability with widely used data processing tools and platforms.

**Time series data** is a sequence of data points indexed in time order. Data points typically consist of successive measurements made from the same source and are used to track changes over time. Examples of time series data include:

-   Industrial sensor data
-   Server performance metrics
-   Heartbeats per minute
-   Electrical activity in the brain
-   Rainfall measurements
-   Stock prices

This multi-part tutorial walks you through writing time series data to InfluxDB Cloud Serverless, querying, and then visualizing that data.

## Key concepts before you get started

Before you get started using InfluxDB, it’s important to understand how time series data is organized and stored in InfluxDB and some key definitions that are used throughout this documentation.

-   [Data organization](#data-organization)
-   [Schema on write](#schema-on-write)
-   [Important definitions](#important-definitions)

### Data organization

The InfluxDB Cloud Serverless data model organizes time series data into buckets and measurements. A bucket can contain multiple measurements. Measurements contain multiple tags and fields.

-   **Bucket**: Named location where time series data is stored. A bucket can contain multiple *measurements*.
    -   **Measurement**: Logical grouping for time series data. All *points* in a given measurement should have the same *tags*. A measurement contains multiple *tags* and *fields*.
        -   **Tags**: Key-value pairs that provide metadata for each point–for example, something to identify the source or context of the data like host, location, station, etc. Tag values may be null.
        -   **Fields**: Key-value pairs with values that change over time–for example, temperature, pressure, stock price, etc. Field values may be null, but at least one field value is not null on any given row.
        -   **Timestamp**: Timestamp associated with the data. When stored on disk and queried, all data is ordered by time. A timestamp is never null.

### Schema on write

When using InfluxDB, you define your schema as you write your data. You don’t need to create measurements (equivalent to a relational table) or explicitly define the schema of the measurement. Measurement schemas are defined by the schema of data as it is written to the measurement.

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

The following table compares tools that you can use to interact with InfluxDB Cloud Serverless. This tutorial covers many of the recommended tools.

| Tool | Administration | Write | Query |
| --- | --- | --- | --- |
| Chronograf | - | - |  |
| influx CLI |  |  | - |
| influx3 data CLI* | - |  |  |
| influxctl CLI | - | - | - |
| InfluxDB HTTP API |  |  |  |
| InfluxDB user interface * |  | - |  |
| InfluxDB 3 client libraries* | - |  |  |
| InfluxDB v1 client libraries | - |  |  |
| InfluxDB v2 client libraries |  |  | - |
| Telegraf | - |  | - |
| Third-party tools |  |  |  |
| Flight SQL clients | - | - |  |
| Grafana | - | - |  |
| Superset | - | - |  |
| Tableau | - | - |  |

\* Covered in this tutorial

The `influxctl` admin CLI isn’t available for InfluxDB Cloud Serverless. It only works with InfluxDB Cloud Dedicated and InfluxDB Clustered.

### InfluxDB user interface

The InfluxDB user interface (UI) provides a web-based visual interface for interacting with and managing InfluxDB. To access the InfluxDB Cloud Serverless UI, [log into your InfluxDB Cloud account](https://cloud2.influxdata.com).

### `influx` CLI

The `influx` CLI lets you manage InfluxDB Cloud Serverless and write data from a command line. Querying InfluxDB Cloud Serverless isn’t supported.

For detailed CLI installation instructions, see the [`influx` CLI reference](/influxdb3/cloud-serverless/reference/cli/influx/).

### `influx3` data CLI

The [`influx3` data CLI](/influxdb3/cloud-serverless/get-started/query/?t=influx3+CLI#execute-an-sql-query) is a community-maintained tool that lets you write and query data in InfluxDB Cloud Serverless from a command line. It uses the HTTP API to write data and uses Flight gRPC to query data.

### InfluxDB HTTP API

The [InfluxDB HTTP API](/influxdb/v2/reference/api/) provides a simple way to let you manage InfluxDB Cloud Serverless and write and query data using HTTP(S) clients. Examples in this tutorial use cURL, but any HTTP(S) client will work.

The `/write` and `/query` v1-compatible endpoints work with the username/password authentication schemes and existing InfluxDB 1.x tools and code. The `/api/v2/write` v2-compatible endpoint works with existing InfluxDB 2.x tools and code.

### InfluxDB client libraries

InfluxDB client libraries are community-maintained, language-specific clients that interact with InfluxDB APIs.

[InfluxDB 3 client libraries](/influxdb3/cloud-serverless/reference/client-libraries/v3/) are the recommended client libraries for writing and querying data InfluxDB Cloud Serverless. They use the HTTP API to write data and use Flight gRPC to query data.

[InfluxDB v2 client libraries](/influxdb3/cloud-serverless/reference/client-libraries/v2/) can use `/api/v2` HTTP endpoints to manage resources such as buckets and API tokens, and write data in InfluxDB Cloud Serverless.

[InfluxDB v1 client libraries](/influxdb3/cloud-serverless/reference/client-libraries/v1/) can write data to InfluxDB Cloud Serverless.

## Authorization

**InfluxDB Cloud Serverless requires authentication** using [API tokens](/influxdb3/cloud-serverless/admin/tokens/). Each API token is associated with a user and a specific set of permissions for InfluxDB resources. You can use administration tools such as the InfluxDB UI, the `influx` CLI, or the InfluxDB HTTP API to create and manage API tokens.

[Set up InfluxDB](/influxdb3/cloud-serverless/get-started/setup/)


---

## Administer InfluxDB Cloud

The following articles provide information about managing your InfluxDB Cloud Serverless resources:

### [Manage API tokens](/influxdb3/cloud-serverless/admin/tokens/)

Manage API tokens in InfluxDB using the InfluxDB UI or the influx CLI.

### [Identify InfluxDB Cloud Serverless version](/influxdb3/cloud-serverless/admin/identify-version/)

Learn how to identify your InfluxDB Cloud Serverless instance through URL patterns, account settings, and HTTP headers.

### [Manage organizations](/influxdb3/cloud-serverless/admin/organizations/)

Manage organizations in InfluxDB using the InfluxDB UI or the influx CLI.

### [Manage your InfluxDB Cloud Serverless account](/influxdb3/cloud-serverless/admin/accounts/)

View and manage information related to your InfluxDB Cloud Serverless account such as pricing plans, data usage, account cancellation, etc.

### [Manage buckets](/influxdb3/cloud-serverless/admin/buckets/)

Manage buckets in InfluxDB Cloud Serverless using the InfluxDB UI, influx CLI, or InfluxDB HTTP API.

### [Manage billing](/influxdb3/cloud-serverless/admin/billing/)

Upgrade to the InfluxDB Cloud Serverless Usage-Based Plan and manage your billing information.

