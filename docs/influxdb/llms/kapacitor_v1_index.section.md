---
title: Kapacitor documentation
description: Kapacitor is an open source data processing framework that makes it easy to create alerts, run ETL jobs and detect anomalies.
url: https://docs.influxdata.com/kapacitor/v1/
product: Kapacitor
type: section
pages: 7
estimated_tokens: 2452
child_pages:
  - url: https://docs.influxdata.com/kapacitor/v1/working/
    title: Work with Kapacitor
  - url: https://docs.influxdata.com/kapacitor/v1/troubleshooting/
    title: Troubleshoot Kapacitor
  - url: https://docs.influxdata.com/kapacitor/v1/reference/
    title: Kapacitor reference
  - url: https://docs.influxdata.com/kapacitor/v1/guides/
    title: Guides
  - url: https://docs.influxdata.com/kapacitor/v1/introduction/
    title: Introducing Kapacitor
  - url: https://docs.influxdata.com/kapacitor/v1/administration/
    title: Administration
---

# Kapacitor documentation

Kapacitor is an open source data processing framework that makes it easy to create alerts, run ETL jobs and detect anomalies. Kapacitor is the final piece of the [TICK stack](https://influxdata.com/time-series-platform/).

## Key features

Here are some of the features that Kapacitor currently supports that make it a great choice for data processing.

-   Process both streaming data and batch data.
-   Query data from InfluxDB on a schedule, and receive data via the [line protocol](/influxdb/v2/reference/syntax/line-protocol/) and any other method InfluxDB supports.
-   Perform any transformation currently possible in [InfluxQL](/influxdb/v1/query_language/spec/).
-   Store transformed data back in InfluxDB.
-   Add custom user defined functions to detect anomalies.
-   Integrate with HipChat, OpsGenie, Alerta, Sensu, PagerDuty, Slack, and more.


---

## Work with Kapacitor

The documents in this section present the key features of the Kapacitor daemon (`kapacitord`) and the Kapacitor client (`kapacitor`).

-   [Kapacitor and Chronograf](/kapacitor/v1/working/kapa-and-chrono/) – presents how Kapacitor is integrated with the Chronograf graphical user interface application for managing tasks and alerts.
-   [Kapacitor API Reference documentation](/kapacitor/v1/working/api/) – presents the HTTP API and how to use it to update tasks and the Kapacitor configuration.
-   [Alerts - Overview](/kapacitor/v1/working/alerts/) – presents an overview of the Kapacitor alerting system.
-   [Alerts - Using topics](/kapacitor/v1/working/using_alert_topics/) – a walk-through on creating and using alert topics.
-   [Alerts - Event handler setup](/kapacitor/v1/working/event-handler-setup/) – presents setting up event handlers for HipChat and Telegraf, which can serve as a blueprint for other event handlers.
-   [Dynamic data scraping](/kapacitor/v1/working/scraping-and-discovery/) – introduces the discovery and scraping features, which allow metrics to be dynamically pulled into Kapacitor and then written to InfluxDB.


---

## Troubleshoot Kapacitor

## [Kapacitor frequently asked questions](/kapacitor/v1/troubleshooting/frequently-asked-questions/)

frequent sources of confusion or important things to know related to Kapacitor.


---

## Kapacitor reference

### [About the project](/kapacitor/v1/reference/about_the_project/)

View information about the Kapacitor project including release notes, licenses, and contribution guidelines.

### [TICKscript language reference](/kapacitor/v1/reference/tick/)

List of resources for working with TICKscript.

### [TICKscript nodes overview](/kapacitor/v1/reference/nodes/)

Overview of nodes in TICKscript.

### [Kapacitor event handlers](/kapacitor/v1/reference/event_handlers/)

Kapacitor event handlers provide ways to integrate Kapacitor alert messages with logging, specific URLs, and many third-party applications.

### [Kapacitor user types and permissions](/kapacitor/v1/reference/user-types-permissions/)

View Kapacitor user types and permissions available when using internal Kapacitor authorizations.

### [Kapacitor command line tools](/kapacitor/v1/reference/cli/)

…

### [Use the InfluxDB documentation MCP server](/kapacitor/v1/reference/mcp-server/)

Query Kapacitor documentation from your IDE using the InfluxDB documentation MCP server.


---

## Guides

These guides assume you’re familiar with the basics of defining, recording, replaying and enabling tasks within Kapacitor. See the [getting started](/kapacitor/v1/introduction/getting-started/) guide if you need a refresher.

## [Calculate rates across joined series + backfill](/kapacitor/v1/guides/join_backfill/)

Use a prepared data generator to calculate rates across joined series and backfill.

## [Custom anomaly detection using Kapacitor](/kapacitor/v1/guides/anomaly_detection/)

Detect anomalies in Kapacitor with user-defined functions (UDFs).

## [Handle Kapacitor alerts during scheduled downtime](/kapacitor/v1/guides/scheduled-downtime/)

Build Kapacitor TICKscripts that gracefully handle scheduled downtime without triggering unnecessary alerts.

## [Kapacitor as a Continuous Query engine](/kapacitor/v1/guides/continuous_queries/)

Use Kapacitor to downsample and process data at scheduled intervals.

## [Live leaderboard of game scores](/kapacitor/v1/guides/live_leaderboard/)

Tutorial on using Kapacitor stream processing and Chronograf to build a leaderboard for gamers to be able to see player scores in realtime. Historical data is also available for post-game analysis.

## [Load directory service](/kapacitor/v1/guides/load_directory/)

The load directory service enables file-based definitions of Kapacitor tasks, templates, and topic handlers that are loaded on startup or when a SIGHUP signal is sent to the process.

## [Reference TICKscripts](/kapacitor/v1/guides/reference_scripts/)

Example TICKscripts available in the Kapacitor repository.

## [Set up event handler](/kapacitor/v1/guides/event-handler-setup/)

Set up Kapacitor event handlers to send alerts and notifications to third-party endpoints.

## [Suppress Kapacitor alerts based on hierarchy](/kapacitor/v1/guides/hierarchical-alert-suppression/)

Kapacitor’s ‘.inhibit()’ allows you to create hierarchical alerting architectures by suppressing alerts with matching tags in a specified alert category.

## [Trigger alerts by comparing two measurements](/kapacitor/v1/guides/two-measurement-alert/)

Kapacitor allows you to create alerts triggered by comparisons between two or more measurements. This guide walks through how to join the measurements, trigger alerts, and create visualizations for the data comparison.

## [Write socket-based user-defined functions (UDFs)](/kapacitor/v1/guides/socket_udf/)

Learn how to write a simple socket-based UDF.


---

## Introducing Kapacitor

To get up and running with Kapacitor, complete the following tasks:

## Download Kapacitor

For information about downloading Kapacitor, visit the [InfluxData downloads page](https://www.influxdata.com/downloads/).

## [Install Kapacitor](/kapacitor/v1/introduction/installation/)

Install, start, and configure Kapacitor on your operating system of choice.

## [Get started with Kapacitor](/kapacitor/v1/introduction/getting-started/)

Get started with Kapacitor to process your time series data.

## [Docker Install](/kapacitor/v1/introduction/install-docker/)

Install Kapacitor with Docker.


---

## Administration

### [Upgrade to Kapacitor v1](/kapacitor/v1/administration/upgrading/)

Upgrade to the latest version of Kapacitor.

### [Configure Kapacitor](/kapacitor/v1/administration/configuration/)

Configure Kapacitor with configuration files options, environment variables, or the Kapacitor HTTP API.

### [Security](/kapacitor/v1/administration/security/)

Protect the data in your Kapacitor instance.

### [Set up authentication and authorization](/kapacitor/v1/administration/auth/)

An overview of TICK stack authentication and authorization, how to enable authentication in Kapacitor Enterprise, and how to manage users and privileges using the InfluxDB Meta API.

### [Manage Kapacitor subscriptions](/kapacitor/v1/administration/subscription-management/)

Kapacitor subscribes to InfluxDB and receives all data as it is written to InfluxDB. Learn how Kapacitor subscriptions work and how to configure and manage them.

