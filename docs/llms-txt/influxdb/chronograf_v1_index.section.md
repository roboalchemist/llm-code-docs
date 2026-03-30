---
title: Chronograf documentation
description: Chronograf is InfluxData’s open source web application. Use Chronograf with the other components of the TICK stack to visualize your monitoring data and easily create alerting and automation rules.
url: https://docs.influxdata.com/chronograf/v1/
product: Chronograf
type: section
pages: 7
estimated_tokens: 4299
child_pages:
  - url: https://docs.influxdata.com/chronograf/v1/troubleshooting/
    title: Troubleshoot Chronograf
  - url: https://docs.influxdata.com/chronograf/v1/tools/
    title: Chronograf Tools
  - url: https://docs.influxdata.com/chronograf/v1/introduction/
    title: Introduction to Chronograf
  - url: https://docs.influxdata.com/chronograf/v1/guides/
    title: Guides for Chronograf
  - url: https://docs.influxdata.com/chronograf/v1/administration/
    title: Administering Chronograf
  - url: https://docs.influxdata.com/chronograf/v1/about_the_project/
    title: About the Chronograf project
---

# Chronograf documentation

Chronograf is InfluxData’s open source web application. Use Chronograf with the other components of the [TICK stack](https://www.influxdata.com/products/) to visualize your monitoring data and easily create alerting and automation rules.

## Key features

### Infrastructure monitoring

-   View all hosts and their statuses in your infrastructure
-   View the configured applications on each host
-   Monitor your applications with Chronograf’s [pre-created dashboards](/chronograf/v1/guides/using-precreated-dashboards/)

### Alert management

Chronograf offers a UI for [Kapacitor](https://github.com/influxdata/kapacitor), InfluxData’s data processing framework for creating alerts, running ETL jobs, and detecting anomalies in your data.

-   Generate threshold, relative, and deadman alerts on your data
-   Easily enable and disable existing alert rules
-   View all active alerts on an alert dashboard
-   Send alerts to the supported event handlers, including Slack, PagerDuty, HipChat, and [more](/chronograf/v1/guides/configuring-alert-endpoints/)

### Data visualization

-   Monitor your application data with Chronograf’s [pre-created dashboards](/chronograf/v1/guides/using-precreated-dashboards/)
-   Create your own customized dashboards complete with various graph types and [template variables](/chronograf/v1/guides/dashboard-template-variables/)
-   Investigate your data with Chronograf’s data explorer and query templates

### Database management

-   Create and delete databases and retention policies
-   View currently-running queries and stop inefficient queries from overloading your system
-   Create, delete, and assign permissions to users (Chronograf supports [InfluxDB OSS](/influxdb/v1/administration/authentication_and_authorization/#authorization) and InfluxDB Enterprise user management)

### Query management

-   View a list of databases, queries and their status
-   Kill a query
-   Download a list of queries in your instance to a CSV file

### Multi-organization and multi-user support

**Note:** To use this feature, OAuth 2.0 authentication must be configured. Once configured, the Chronograf Admin tab on the Admin menu is visible. For details, see [Managing Chronograf security](/chronograf/v1/administration/managing-security/).

-   Create organizations and assign users to those organizations
-   Restrict access to administrative functions
-   Allow users to set up and maintain unique dashboards for their organizations


---

## Troubleshoot Chronograf

Follow the link below to access Chronograf’s FAQ.

## [Chronograf frequently asked questions (FAQs)](/chronograf/v1/troubleshooting/frequently-asked-questions/)

Common issues with Chronograf


---

## Chronograf Tools

Chronograf provides command line tools designed to aid in managing and working with Chronograf from the command line. The following command line interfaces (CLIs) are available:

## [Use the InfluxDB documentation MCP server](/chronograf/v1/tools/mcp-server/)

Query Chronograf documentation from your IDE using the InfluxDB documentation MCP server.

## [chronoctl](/chronograf/v1/tools/chronoctl/)

The `chronoctl` command line interface (CLI) includes commands to interact with an instance of Chronograf’s data store.

## [chronograf - Chronograf server](/chronograf/v1/tools/chronograf/)

The `chronograf` daemon starts and manages all the processes associated with the Chronograf server and includes options that manage many aspects of Chronograf security.


---

## Introduction to Chronograf

Follow the links below to get acquainted with Chronograf:

### [Download Chronograf](/chronograf/v1/introduction/downloading/)

Download the latest Chronograf release at the [InfluxData download page](https://www.influxdata.com/downloads/). Click **Are you interested in InfluxDB 1.x Open Source?** to expand the 1.x options. Scroll to the **Chronograf** section and select your desired Chronograf version and operating system. Execute the provided download commands.

### [Get started with Chronograf](/chronograf/v1/introduction/getting-started/)

Overview of data visualization, alerting, and infrastructure monitoring features available in Chronograf.

### [Install Chronograf](/chronograf/v1/introduction/installation/)

Download and install Chronograf.


---

## Guides for Chronograf

Follow the links below to explore Chronograf’s features.

### [Write data to InfluxDB](/chronograf/v1/guides/write-to-influxdb/)

Use Chronograf to write data to InfluxDB. Upload line protocol into the UI, use the InfluxQL `INTO` clause, or use the Flux `to()` function to write data back to InfluxDB.

### [Advanced Kapacitor usage](/chronograf/v1/guides/advanced-kapacitor/)

Use Kapacitor with Chronograf to manage alert history, TICKscripts, and Flux tasks.

### [Analyze logs with Chronograf](/chronograf/v1/guides/analyzing-logs/)

Analyze log information using Chronograf.

### [Clone dashboards and cells](/chronograf/v1/guides/cloning-in-ui/)

Clone a dashboard or a cell and use the copy as a starting point to create new dashboard or cells.

### [Configure Chronograf alert endpoints](/chronograf/v1/guides/configuring-alert-endpoints/)

Send alert messages with Chronograf alert endpoints.

### [Create Chronograf alert rules](/chronograf/v1/guides/create-alert-rules/)

Trigger alerts by building Kapacitor alert rules in the Chronograf user interface (UI).

### [Create Chronograf dashboards](/chronograf/v1/guides/create-a-dashboard/)

Visualize your data with custom Chronograf dashboards.

### [Explore data in Chronograf](/chronograf/v1/guides/querying-data/)

Query and visualize data in the Data Explorer.

### [Monitor InfluxDB Enterprise clusters](/chronograf/v1/guides/monitoring-influxenterprise-clusters/)

Use Chronograf dashboards with an InfluxDB OSS server to measure and monitor InfluxDB Enterprise clusters.

### [Use annotations in Chronograf views](/chronograf/v1/guides/annotations/)

Add contextual information to Chronograf dashboards with annotations.

### [Use dashboard template variables](/chronograf/v1/guides/dashboard-template-variables/)

Chronograf dashboard template variables let you update cell queries without editing queries, making it easy to interact with your dashboard cells and explore your data.

### [Use pre-created dashboards in Chronograf](/chronograf/v1/guides/using-precreated-dashboards/)

Display metrics for popular third-party applications with preconfigured dashboards in Chronograf.

### [View Chronograf dashboards in presentation mode](/chronograf/v1/guides/presentation-mode/)

View dashboards in full screen using presentation mode.

### [Visualization types in Chronograf](/chronograf/v1/guides/visualization-types/)

Chronograf’s dashboard views support the following visualization types, which can be selected in the **Visualization Type** selection view of the [Data Explorer](/chronograf/v1/guides/querying-data).

[Visualization Type selector](/img/chronograf/1-6-viz-types-selector.png)

Each of the available visualization types and available user controls are described below.

-   [Line Graph](#line-graph)
-   [Stacked Graph](#stacked-graph)
-   [Step-Plot Graph](#step-plot-graph)
-   [Single Stat](#single-stat)
-   [Line Graph + Single Stat](#line-graph-single-stat)
-   [Bar Graph](#bar-graph)
-   [Gauge](#gauge)
-   [Table](#table)
-   [Note](#note)

For information on adding and displaying annotations in graph views, see [Adding annotations to Chronograf views](/chronograf/v1/guides/annotations/).


---

## Administering Chronograf

Follow the links below for more information.

### [Chronograf configuration options](/chronograf/v1/administration/config-options/)

Options available in the Chronograf configuration file and environment variables.

### [Configure Chronograf](/chronograf/v1/administration/configuration/)

Configure Chronograf, including security, multiple users, and multiple organizations.

### [Connecting Chronograf to InfluxDB Enterprise clusters](/chronograf/v1/administration/chrono-on-clusters/)

Work with InfluxDB Enterprise clusters through the Chronograf UI.

### [Create a Chronograf HA configuration](/chronograf/v1/administration/create-high-availability/)

Create a Chronograf high-availability (HA) cluster using etcd.

### [Create InfluxDB and Kapacitor connections](/chronograf/v1/administration/creating-connections/)

Create and manage InfluxDB and Kapacitor connections in the UI.

### [Import and export Chronograf dashboards](/chronograf/v1/administration/import-export-dashboards/)

Share dashboard JSON files between Chronograf instances, or add dashboards as resources to include in a deployment.

### [Manage Chronograf organizations](/chronograf/v1/administration/managing-organizations/)

Create, configure, map, and remove organizations in Chronograf.

### [Manage Chronograf security](/chronograf/v1/administration/managing-security/)

Manage Chronograf security with OAuth 2.0 providers.

### [Manage Chronograf users](/chronograf/v1/administration/managing-chronograf-users/)

Manage users and roles, including SuperAdmin permission and organization-bound users.

### [Manage InfluxDB users in Chronograf](/chronograf/v1/administration/managing-influxdb-users/)

Enable authentication and manage InfluxDB OSS and InfluxDB Enterprise users in Chronograf.

### [Manage queries in Chronograf](/chronograf/v1/administration/managing-queries/)

Manage queries using the Queries page in Chronograf.

### [Migrate to a Chronograf HA configuration](/chronograf/v1/administration/migrate-to-high-availability/)

Migrate a Chronograf single instance configuration using BoltDB to a Chronograf high-availability (HA) cluster configuration using etcd.

### [Prebuilt dashboards in Chronograf](/chronograf/v1/administration/prebuilt-dashboards/)

Import prebuilt dashboards into Chronograf based on Telegraf plugins.

### [Restore a Chronograf database](/chronograf/v1/administration/restoring-chronograf-db/)

If you’re rolling back to a previous version of Chronograf, restore your internal database.

### [Upgrade Chronograf](/chronograf/v1/administration/upgrading/)

Upgrade to the latest version of Chronograf.


---

## About the Chronograf project

Chronograf is the user interface component of the [InfluxData time series platform](https://www.influxdata.com/time-series-platform/). It makes the monitoring and alerting for your infrastructure easy to setup and maintain. It is simple to use and includes templates and libraries to allow you to rapidly build dashboards with realtime visualizations of your data.

Follow the links below for more information.

### [Chronograf release notes](/chronograf/v1/about_the_project/release-notes/)

Important changes and what’s new in each version of Chronograf.

### [Contribute to Chronograf](/chronograf/v1/about_the_project/contributing/)

Contribute to the Chronograf project.

### [InfluxData Contributor License Agreement (CLA)](/chronograf/v1/about_the_project/cla/)

Before contributing to the Chronograf project, submit the InfluxData Contributor License Agreement.

### [Open source license for Chronograf](/chronograf/v1/about_the_project/licenses/)

Find the open source license for Chronograf.

Chronograf is released under the GNU Affero General Public License. This Free Software Foundation license is fairly new, and differs from the more widely known and understood GPL.

Our goal with using AGPL is to preserve the concept of copyleft with Chronograf. With traditional GPL, copyleft was associated with the concept of distribution of software. The problem is that nowadays, distribution of software is rare: things tend to run in the cloud. AGPL fixes this “loophole” in GPL by saying that if you use the software over a network, you are bound by the copyleft. Other than that, the license is virtually the same as GPL v3.

To say this another way: if you modify the core source code of Chronograf, the goal is that you have to contribute those modifications back to the community.

Note however that it is NOT required that your dashboards and alerts created by using Chronograf be published. The copyleft applies only to the source code of Chronograf itself.

If this explanation isn’t good enough for you and your use case, we dual license Chronograf under our [standard commercial license](https://www.influxdata.com/legal/slsa/).

[Contact sales for more information](https://www.influxdata.com/contact-sales/).

## Third Party Software

InfluxData products contain third party software, which means the copyrighted, patented, or otherwise legally protected software of third parties that is incorporated in InfluxData products.

Third party suppliers make no representation nor warranty with respect to such third party software or any portion thereof. Third party suppliers assume no liability for any claim that might arise with respect to such third party software, nor for a customer’s use of or inability to use the third party software.

The [list of third party software components, including references to associated license and other materials](https://github.com/influxdata/chronograf/blob/master/LICENSE_OF_DEPENDENCIES.md), is maintained on a version by version basis.

