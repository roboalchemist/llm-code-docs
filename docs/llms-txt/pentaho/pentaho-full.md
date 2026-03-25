# Pentaho Documentation

The Pentaho Platform changes how your business discovers and manages data, ensuring seamless scalability across all data types and volumes. Simplify data observability with a unified business glossary and advanced metadata management to enhance trust and quality. Embrace a smarter way to handle your data, making it easier to search, validate, and derive insights that are tailored to your unique business needs.

<table data-card-size="large" data-view="cards"><thead><tr><th align="center"></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td align="center">Pentaho Data Integration</td><td><a href="https://docs.pentaho.com/pdia-data-integration">https://docs.pentaho.com/pdia-data-integration</a></td><td><a href="https://2703045236-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F3IlYoST8ikFrLrfNDjT1%2Fuploads%2FFGkdViCshtGcoA4AfXhX%2FKayak.jpg?alt=media&#x26;token=11fb9162-7101-4eaf-bbd4-e26ceca8da27">Kayak.jpg</a></td></tr><tr><td align="center">Pentaho Business Analytics</td><td><a href="https://docs.pentaho.com/pba">https://docs.pentaho.com/pba</a></td><td><a href="https://2703045236-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F3IlYoST8ikFrLrfNDjT1%2Fuploads%2F99KpQlgB34V2KpR4eBmY%2FTennis.jpg?alt=media&#x26;token=bcde7ecd-ce84-4874-b673-3910a9db50da">Tennis.jpg</a></td></tr><tr><td align="center">Pentaho Data Catalog</td><td><a href="https://docs.pentaho.com/pdc-whats-new">https://docs.pentaho.com/pdc-whats-new</a></td><td><a href="https://2703045236-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F3IlYoST8ikFrLrfNDjT1%2Fuploads%2FjuFZdaczxc38dnnZlU80%2FMBike.jpg?alt=media&#x26;token=9fd5b1a5-32d8-41b7-8d70-3d239909ecb2">MBike.jpg</a></td></tr><tr><td align="center">Pentaho Data Optimizer</td><td><a href="https://docs.pentaho.com/pdc-10.2-data-optimizer">https://docs.pentaho.com/pdc-10.2-data-optimizer</a></td><td><a href="https://2703045236-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F3IlYoST8ikFrLrfNDjT1%2Fuploads%2F6Sx7U7lw4fZaVwwGxVU6%2FSurf.jpg?alt=media&#x26;token=f516f4cd-1425-4490-894f-df71f0ac6346">Surf.jpg</a></td></tr></tbody></table>


# Pentaho Data Integration and Analytics


# Pentaho Data Catalog


# What's new in Pentaho 10.2

Version 10.2 of Pentaho Data Integration and Analytics Enterprise Edition delivers enhancements across Pentaho Data Integration (PDI) and Pentaho Business Analytics (PBA) that includes both usability improvements and performance across several components.

Along with these features and enhancements, Pentaho 10.2 is a Long Term Support (LTS) release. LTS refers to a widely adopted release that provides stability and flexibility for customers to upgrade when best suited. This type of release is for customers who have rigid environments and cannot frequently upgrade.

The key features in this release are:

## Java 17 support

Use Pentaho now built on Oracle Java 17 and Open JDK Java 17. The following Java 17 support benefits are key to Pentaho:

* Oracle Java 17 is available under a new license that permits free production use.
* Java 17 has several performance improvements over Java 11.

See [Java virtual machine](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia000/components-reference/java-virtual-machine) for details.

## License manager enhancements

Enhance your license manager interactions with the following capabilities:

* Re-introduced support for offline license files. If you are in an air-gapped environment, you can deploy licenses without the need for any license server. Additional audit costs may apply. Please contact your Pentaho representative for your license management options. You can still use Hitachi Vantara maintained cloud License Servers or install Local License Servers with no additional audit costs.
* Separate entitlements for development or production usage. You can track and control usage across these two types of scenarios within your environment.
* Separate PDI client (ETL authoring) entitlements. You can track and control the use of PDI within your environment independently from other Pentaho components. These entitlements are instance-based as opposed to other Pentaho components, which are core-based.
* The borrow-time (how often licenses are validated) has now been increased to reduce the number of license validation calls made by Pentaho components to further minimize resource utilization due to license validation.
* Enhancements to enable OEMs to self-manage entitlements to their customers.

See [Acquire and install enterprise licenses](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia002/manage-the-pentaho-system/manage-pentaho-licenses/acquire-and-install-enterprise-licenses) for instructions on using the license manager.

## New charts available for Analyzer reports

In your Analyzer reports, visualize progress or status of a specific metric or goal with the new Gauge E-chart or show a comparison of multiple categories across several variables with the new Radar E-chart. See [Gauge chart](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia004/pentaho-analyzer/creating-analyzer-reports/visualizations-for-analyzer/gauge-chart) and [Radar chart](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia004/pentaho-analyzer/creating-analyzer-reports/visualizations-for-analyzer/radar-chart) for details.

## CBC support for AES Encryption

Choose between the existing (default) Electronic Code Book (ECB) or the new Cipher Block Chaining (CBC) implementation of the Pentaho Advanced Encryption Standard (AES) security protocol. See [AES security](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia002/secure-the-pentaho-system/user-security/advanced-security-providers/aes-security) for details.

## Scheduling Improvements

Improve your scheduling experience with the following enhancements:

* **Parameter information**

  A new **Parameter** column added to the schedule management listings in Pentaho User Console (PUC) and Pentaho Data Integration (PDI). See [PUC Schedules](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia004/pentaho-user-console/about-pentaho-user-console-perspectives/schedules) and [Scheduler perspective in the PDI client](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia003/scheduler-perspective-in-the-pdi-client) for details.
* **Schedule Power User role**

  A new role designed for a user who mostly executes schedules. See [Manage Users and Roles in PUC](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia004/pentaho-user-console/about-pentaho-user-console-perspectives/administration/manage-users-and-roles-in-puc) for details.
* **VFS-based scheduling updates**

  Virtual File System (VFS) connections added to PUC **Browse File** perspective, VFS access based on roles, and specification of a VFS root folder path. See [Set up a VFS location for schedule outputs](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia004/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/set-up-a-vfs-location-for-schedule-outputs) for details.
* **E-mail address updates**

  External LDAP and JDBC support added for syncing and improved search functionality for e-mail addresses. See [Importing and updating email addresses used for scheduling from data sources](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia002/manage-the-pentaho-system/manage-the-pentaho-server/importing-and-updating-email-addresses-used-for-scheduling-from-data-sources) and [Create an email group](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia004/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/schedule-reports/set-up-emails-for-scheduled-reports/create-an-email-group) for details.
* **Report date**

  New reporting date added to scheduled email attachment filename. See [Schedule a report](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia004/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/schedule-reports/schedule-a-report) for details

## Support for UNC Paths (SMB)

Connect to your Server Message Block (SMB) files through VFS in both PUC and PDI. See [Set up a VFS location for schedule outputs](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia004/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/set-up-a-vfs-location-for-schedule-outputs) for PUC details and [Connecting to Virtual File Systems](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia003/data-integration-perspective-in-the-pdi-client/connecting-to-virtual-file-systems) for PDI details.

## AWS Athena available as a data source

Access Amazon Web Service (AWS) Athena as a data source in both PUC and PDI. See [AWS Athena](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia001/jdbc-drivers-reference/aws-athena) for details and [Define data connections](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia001/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections) for instructions on adding a database connection.

## Support for Apache Vanilla Hadoop

Directly connect to plain Hadoop clusters (commonly known as Apache Vanilla Hadoop clusters) through the new Apache Vanilla Hadoop driver. See [Using the Apache Vanilla Hadoop driver](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia003/advanced-pentaho-data-integration-topics/connecting-to-a-hadoop-cluster-with-the-pdi-client/using-the-apache-vanilla-hadoop-driver) for details.

## Data formatting in PDI logging output

Specify the date used in PDI logging with the **Pattern** parameter in the `log4j2.xml` file. See [Set up the log](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia002/optimize-the-pentaho-system/performance-monitoring/pdi-logging/set-up-the-log-file) file for details.

## PDI transformation steps enhancement

The following PDI transformation steps have been modified for this release:

* **Microsoft Excel Writer**

  This step has been improved to include functionality from the Microsoft Excel Output step, which is now deprecated in favor of the Microsoft Excel Writer step. See [Microsoft Excel Writer](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia003/pdi-transformation-steps/microsoft-excel-writer) for details on this enhanced step.
* **Cassandra Input and Output moved to the Marketplace**

  These steps were moved to the Marketplace to relieve a vulnerability to the PDI core. Contact [Pentaho Support](https://support.pentaho.com/) for details.

## Improved Excel export performance from Pentaho Report Designer

Improve output performance with support of Excel XLSX export. See [Microsoft Excel report takes a long time to generate](https://docs.hitachivantara.com/r/en-us/pentaho-data-integration-and-analytics/10.2.x/mk-95pdia008/report-designer-and-reporting-engine-issues/microsoft-excel-report-takes-a-long-time-to-generate) for details.


# Pentaho EE Marketplace Plugins

The plug-ins listed on this page are available from the [Support Portal](https://support.pentaho.com/home) home page.

## Pentaho 10.0.2

You can use the Salesforce bulk operation step plug-in for bulk operations on Salesforce objects. This step can significantly increase performance of Salesforce operations.

With the Bulk load into Databricks job entry, you can load large amounts of data from files in your cloud accounts into Databricks tables.

## Pentaho 10.0.1

You can use the new Google Analytics v4 plug-in to generate reports and populate your data warehouse.

A new Hitachi Data Connector for SAP and Business Warehouse plug-in is available. This new plug-in is the ideal Pentaho Data Integration plug-in to use SAP data in your data integration work flows. It enables the querying and extraction of complex and nested SAP structures. The plug-in supports both full and incremental (delta) load scenarios and bi-directional (read from and write to SAP) transfers. In addition, it integrates with SAP security allowing you to manage access within your existing setup. For more information, ask your customer support representative.

## Pentaho 10.0

The Elasticsearch REST Bulk Insert step now supports Elasticsearch version 8 and has been made available as a Pentaho EE Marketplace plug-in.

## Pentaho 9.5

For the Pentaho EE 9.5 GA release, two new plugins were released as part of the Pentaho EE Marketplace Plugin release with new features to improve your data management operations. The plugins are available from the [Support Portal](https://support.pentaho.com/home) home page. Sign into the portal using the Pentaho support username and password provided in your Pentaho Welcome Packet. The plugins are:

* A hierarchical data plugin that adds five new steps for working with hierarchical data.
* A Kafka streaming plugin that enhances the Kafka consumer and producer steps and adds a **Kafka Offset** job with the ability to reset the offset.

## Hierarchical data type steps

Pentaho has added an hierarchical data type, and has five new steps for processing structured, complex, and nested data types. This new data type is supported in steps in previous releases of Pentaho that can handle hierarchical data. These five new steps consist of the following:

* **Hierarchical JSON Input**

  This step accepts a JSON file or JSONL from a previous step or a file location and converts it into a hierarchical object.
* **Hierarchical JSON Output**

  This step accepts hierarchical data from a previous step and converts it into a JSON formatted string. 
* **Extract to Rows**

  This step parses hierarchical data from input steps.
* **Modify values from a single row**

  This step modifies the hierarchical data using incoming columns or create hierarchical data output to another step.
* **Modify values from grouped rows**

  This step builds complex hierarchical data or group data based on a field.

The last three steps are used within the transformation flow for interacting with the hierarchical data type structure in-place, without needing to flatten the data to a row structure.​

## Kafka Improvements

A new job entry called Kafka Offset has been added to enable you to change the offset of a topic partition. This Job entry has fields to connect to a Kafka broker or cluster in the **Setup** and **Options** tabs.

The following improvements have been made to the Kafka Consumer and Kafka Producer steps:

* Encryption is supported for connection parameters.
* SSL and Kerberos (SASL) connectivity have been certified.
* You can now use variables from Kettle properties, PDI environment variables. and parameter variables in the Kafka properties settings on the **Options** tab.
* The Kafka client library has been upgraded to 3.4.0.
* Logging has been improved to make debugging easier.
* Improved the Kafka consumer step to consume messages until the time stamp set using the **Offset Settings** tab in the Kafka Offset job.
* An offset rebalancer has been added to correctly commit offsets if a rebalance occurs when a new consumer is added or an existing consumer removed from the consumer group.


# What's new in Pentaho 9.3

The Pentaho 9.3 Enterprise Edition delivers a variety of features and enhancements, including the Java upgrade to version 11, Docker container deployment, and component upgrades. Pentaho 9.3 also continues to enhance the Pentaho business analytics experience.

Along with these features and enhancements, Pentaho 9.3 is a Long Term Support (LTS) release. LTS refers to a widely adopted release that provides stability and flexibility for customers to upgrade when best suited. Such a release is for customers who have rigid environments and cannot frequently upgrade.

## Java 11

With Oracle's support of Java 8 ending, Pentaho 9.3 is built on the latest release of Java, version 11. See the **Components reference** in the **Try Pentaho Data Integration and Analytics** document for more information.

## Docker container deployment

You can now create and deploy Docker containers of Pentaho products with a command line tool. For example, you can use your Pentaho Server, based on your licensed Pentaho software installation, to create a standardized Docker container with data integration, business analytics, and Carte server components. See the **Install Pentaho Data Integration and Analytics** document for more information.

## MongoDB improvements

You can now use MongoDB Atlas string format to connect Pentaho to MongoDB. With this type of string, you no longer need to specify all your cluster members in the connection. Also, you can now continue processing aggregation pipeline data when it exceeds the standard 100MB RAM allocation. See the MongoDB Input anf MongoDB Output steps in the **Pentaho Data Integration** document for more information.

## Component upgrades

Pentaho 9.3 contains many upgraded components, including Snowflake, ElasticSearch, IBM MQ, Postgres, Oracle, SQL Server, Windows Server, MacOS 11 Big Sur, and Ubuntu. See the **Components reference** in the **Try Pentaho Data Integration and Analytics** document for more information.

## Security improvements

Log4j has been upgraded to version 2.17.1 to improve logging and address Log4j security issues. See [Hitachi Vantara Lumada and Pentaho Support Portal](https://support.pentaho.com/hc/en-us) for more information.

## Reduced Pentaho installation download size and improved startup time

The download size of the Pentaho installation is reduced by almost half, leading to a smaller footprint and quicker download time. Pentaho's start time is also significantly improved now that only your specific drivers are loaded at startup instead of the entire set. See the **Install Pentaho Data Integration and Analytics** document for instructions on downloading and adding your specific drivers.

## Analyzer enhancements

Pentaho 9.3 includes the following Analyzer improvements:

* **Query performance inprovement**

  Improved Analyzer's caching of queries to increase performance.
* **Improved handling of daylight savings when scheduling reports**

  The new **Ignore daylight saving adjustment** option permits your report to run at least once every 24 hours, regardless of daylight saving. See **Schedule a report** in the **Pentaho Business Analytics** document for more information.
* **Enable or disable report options at the server level**

  The new **Show Empty Rows where the Measure cells is blank** property improves performance by avoiding cross-joins. See **Control empty rows in reports** in the **Pentaho Business Analytics** document for more information.
* **Select parameter values when scheduling reports**

  You can now add parameters values when scheduling an Analyzer report from Pentaho User Console and set default values at the time a report is scheduled to run. See **Add query parameters to Analyzer reports** in the **Pentaho Business Analytics** document for more information.
* **Drill up or down a dimension**

  You have new options for drilling up or down a dimension. See **Working with Analyzer fields** in the **Pentaho Business Analytics** document for more information.
* **Export an Analyzer report as a JSON file through a URL**

  You can now export an Analyzer report as a JSON file from a Pentaho repository through a URL, which can be useful when you want to export reports from a different scheduler. See **Export an Analyzer report through a URL** in the **Pentaho Business Analytics** document for more information.


# What's New in 11.0

Release 11 of Pentaho Data Integration & Analytics includes several major updates that improve the user experience in both Data Integration and Business Analytics. It also introduces new performance- and security-related features, as well as simplified deployment and upgrades.

Release 11 is a Long Term Supported (LTS) release. For details about the support period and the service pack and update release schedule, see the[ Pentaho Support Lifecycle page](https://support.pentaho.com/hc/en-us/articles/205789159-Pentaho-Product-Lifecycle-Overview).

The **key features and enhancements introduced** in this release are:

1. [<mark style="color:blue;">**Pipeline Designer**</mark>](#pipeline-designer)
2. [<mark style="color:blue;">**Project Lifecycle Management**</mark>](#project-lifecycle-management)
3. [<mark style="color:blue;">**New Pentaho User Console**</mark>](#new-pentaho-user-console) <mark style="color:blue;">**(Preview)**</mark>
4. [<mark style="color:blue;">**New Data Modeling Workflow (replacing Schema Workbench and Data Source Wizard)**</mark>](#new-data-modeling-workflow)
5. [<mark style="color:blue;">**Out-of-the-box support for OIDC / OAuth 2.0**</mark>](#out-of-the-box-support-for-oidc-oauth-2.0)
6. [<mark style="color:blue;">**Granular Permissions in Pentaho / BA Server**</mark>](#granular-permissions-for-pentaho-ba-server)
7. [<mark style="color:blue;">**Docker Simplification**</mark>](#docker-simplification)
8. [<mark style="color:blue;">**Java 21 Support & Tomcat 10**</mark>](#java-21-support-tomcat-10)
9. [<mark style="color:blue;">**Plugin Manager**</mark>](#plugin-manager)
10. [<mark style="color:blue;">**Karaf/OSGi removal and Big Data plugins**</mark>](#karaf-osgi-removal-and-big-data-plugins)
11. [<mark style="color:blue;">**OTEL-based observability**</mark>](#otel-based-observability)

The following sections describe each of these features and enhancements.

## Pipeline Designer

Release 11 introduces a browser-based user experience (UX) that you can use to author ETL pipelines. This experience enables you to build PDI transformations and jobs in a web browser without the need to deploy Spoon.

<figure><img src="https://2804294592-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyzYIVXc5NujjLFFhw5Jm%2Fuploads%2FT7qwBRJmSw1J2dkMntsY%2Fimage.png?alt=media&#x26;token=e0d86cad-bcd1-40c3-b937-8950f82dc700" alt=""><figcaption></figcaption></figure>

Conceptually, it is similar to the Spoon interface that users know and rely on. However, the UI is built on a modern UI framework. This interface also maintains compatibility with existing transformations and jobs that you developed by using Spoon.

For more information, see [Pipeline Designer](https://docs.pentaho.com/pba/11.0-pba/pipeline-designer).

## Project Lifecycle Management

In PDI versions prior to Release 11, there was no defined structure for organizing transformations, jobs, and associated configuration. This lack of structure made it challenging for ETL developers and DevOps teams to keep pipeline development work organized and made collaboration and migration across environments difficult.

In addition, there were differences in how configuration references were resolved, resulting in behavior that might appear to be inconsistent.

<figure><img src="https://2804294592-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyzYIVXc5NujjLFFhw5Jm%2Fuploads%2Fj9bWqemlvUzaV4Nmz88m%2Fimage.png?alt=media&#x26;token=e1e7e58f-70ea-4086-94ea-7a6a70c86332" alt=""><figcaption></figcaption></figure>

Project Lifecycle Management introduces several features to address these gaps. For more information, see [Configuring ETL with Projects](https://docs.pentaho.com/pdia-data-integration/pdia-11.0-data-integration/organizing-etl-with-projects#manageability).

## New Pentaho User Console (Preview)

With Release 11, Pentaho introduces a completely revamped user experience (UX) for Pentaho User Console (PUC). This UX aligns with the broader Pentaho platform UX and serves as the entry point for most PDI and PBA users. The new UX presents a more modern and convenient interface and addresses several pain points associated with the existing PUC in 10.2 and earlier.

<figure><img src="https://2804294592-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyzYIVXc5NujjLFFhw5Jm%2Fuploads%2FUyUxCG5t0P9X4ealemYT%2Fimage.png?alt=media&#x26;token=f148a13e-3285-46b7-92cf-bfe33e187bd8" alt=""><figcaption></figcaption></figure>

The existing PUC will continue to be available until all existing functionality has been moved to the new UX. For more information, see [Introducing Modern PUC](https://docs.pentaho.com/pba/11.0-pba/pentaho-user-console/modern-design).

## New Data Modeling Workflow

Release 11 introduces a new tool for building and managing Mondrian data models. Customers have typically used Schema Workbench or Data Source Wizard to build, edit, and deploy Mondrian models. Pentaho now includes a web-based tool, Semantic Model Editor (SME), that enables you to build and manage Mondrian models in an easy-to-use, modern UX.

Both novice and advanced users can use SME to work with Mondrian data models. SME provides a significantly better experience for users of PBA and especially Analyzer. In addition, SME supports all existing Mondrian models and provides advanced capabilities that were not available in either Schema Workbench or Data Source Wizard.

<figure><img src="https://2804294592-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyzYIVXc5NujjLFFhw5Jm%2Fuploads%2FbvAaOXY6vTCT8cYvhpLG%2Fimage.png?alt=media&#x26;token=bf0cdd57-08df-4c7a-8c4a-c2e468dea084" alt=""><figcaption></figcaption></figure>

For more information, see [Semantic Model Editor](https://docs.pentaho.com/pba/11.0-pba/semantic-model-editor).

## Out-of-the-box support for OIDC / OAuth 2.0

Release 11 supports OAuth 2.0/OIDC authentication for Pentaho Server, enabling single sign-on (SSO) integration with identity providers such as Google, Okta, and Azure. It supports any OIDC-compliant identity provider (IdP). This support greatly simplifies SSO configuration in Pentaho.

<figure><img src="https://2804294592-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyzYIVXc5NujjLFFhw5Jm%2Fuploads%2FsmMHck3iMCiWXWr3j3jn%2Fimage.png?alt=media&#x26;token=c66d9337-1950-429e-8847-cc93b64d3850" alt=""><figcaption></figcaption></figure>

For more information, see [OIDC/OAuth](https://docs.pentaho.com/pdia-admin/readme/security-pages-moved/user-security-legacy-pages/advanced-security-providers#oidc-oauth-2-0).

## Granular Permissions for Pentaho / BA Server

Release 11 introduces more granular and flexible access control across the platform to address several long-standing challenges, such as:

1. Permissions were not sufficiently fine-grained. For example, the "Read Content" permission allows a user to see any content from any plugin (unless file or folder permissions prevent it).
2. Permissions were not structured in a way that could prevent or provide access to individual plugins.
3. Permissions were not sufficiently fine-grained for data sources or other assets.
4. Execute permissions were very broad.

<figure><img src="https://2804294592-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyzYIVXc5NujjLFFhw5Jm%2Fuploads%2FrTbSN2et5tUaVD8nVzls%2Fimage.png?alt=media&#x26;token=cad4f374-af6b-42d9-8ee9-c9dbd89d865e" alt=""><figcaption></figcaption></figure>

Release 11 addresses these issues in Pentaho Server. Together with OAuth 2.0/OIDC support, Pentaho now has a more robust authentication and authorization model.

For more information, see [Granular Permissions for Pentaho](https://docs.pentaho.com/pba/11.0-pba/semantic-model-editor/sharing-a-semantic-model/permissions-for-semantic-models).

## Docker Simplification

Release 11 significantly simplifies Docker-based Pentaho deployments. First, Pentaho introduces optimized, prebuilt images for on-premises deployments (plain Docker and Kubernetes \[K8s]), EKS, AKS, and GKE. These images have standardized installation paths and variables. In addition, enhanced entrypoint scripts support runtime configuration overrides (configuration files and licenses), allowing flexible customization by injecting files at startup.

For more information, see [Docker Deployment](https://docs.pentaho.com/install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-server).

## Java 21 Support & Tomcat 10

Java 21 is supported in Release 11. This support allows customers to operate Pentaho with an Oracle JVM without associated licensing costs. Customers can continue to use OpenJDK or other supported JVMs (see the list of supported JVMs in the documentation).

Pentaho Server in Release 11 comes with Tomcat 10, addressing several vulnerabilities and other defects associated with Tomcat 9.

For more information about supported JVM and Tomcat versions, see [Components Reference](https://docs.pentaho.com/install/pdia-11.0-installation/components-reference).

## Plugin Manager

Release 11 introduces a Plugin Manager that enables administrators to manage both PDI and PBA plugins. Going forward, Pentaho will release new functionality as plugins where possible. Having a plugin manager to identify, deploy, and manage plugins conveniently is therefore key to managing Pentaho deployments.

<figure><img src="https://2804294592-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyzYIVXc5NujjLFFhw5Jm%2Fuploads%2Fy5CzkfB31Zn3EuPPsUdn%2Fimage.png?alt=media&#x26;token=8e60d853-c28e-4501-a22d-b5781bc80f17" alt=""><figcaption></figcaption></figure>

For more information, see [Plugin Manager](https://docs.pentaho.com/pba/11.0-pba/pentaho-user-console/modern-design/plugin-manager).

## Karaf / OSGi Removal and Big Data Plugins

With Release 11, Karaf and OSGi are completely removed from PDI. Big data components are now available as plugins. There is no separate PDI deployment with big data add-ons. Big data components are treated the same as any other PDI plugin and can be deployed in the same manner.

This change significantly reduces the size of both the PDI client and Pentaho Server deployments by more than 1 GB.

For more information, see [Plugin Manager](https://docs.pentaho.com/pba/11.0-pba/pentaho-user-console/modern-design/plugin-manager).

## OTEL-based Observability

[OTEL](https://opentelemetry.io/docs/languages/java/) is an open standard for applications to communicate telemetry data, such as traces, metrics, and logs. There is a broad ecosystem of tools that can consume OTEL data, including Datadog, Splunk, Elastic, Amazon CloudWatch, and Azure Monitor.

With the OTEL plugin, you can monitor every Pentaho ETL process with the following:

* Logs that are consolidated in a single place and represented hierarchically
* Traces to view task timing, execution hierarchy, and variables during execution
* Metrics to track data flow trends at specified points of interest

For more information, see [Plugin Manager](https://docs.pentaho.com/pba/11.0-pba/pentaho-user-console/modern-design/plugin-manager).

## Other Enhancements

Release 11 also introduces several other enhancements and defect fixes. These are documented in the release notes.


# Release Notes 11.0

Welcome to the release notes for Pentaho Data Integration & Analytics 11.0. This is a Long Term Supported (LTS) release. LTS releases are stable releases with a longer support lifecycle. See the Support Lifecycle page to review the support terms for an LTS release.

The last LTS release, 10.2, was released in August 2024. This document covers the incremental enhancements from 10.2 to 11.0.

## What's New?

The **key features and enhancements introduced** in this release are:

1. <mark style="color:blue;">**Pipeline Designer**</mark>
2. <mark style="color:blue;">**Project Lifecycle Management**</mark>
3. <mark style="color:blue;">**New Pentaho User Console (Preview)**</mark>
4. <mark style="color:blue;">**New Data Modeling Workflow (replacing Schema Workbench and Data Source Wizard)**</mark>
5. <mark style="color:blue;">**OOB Support for OIDC / OAuth 2.0**</mark>
6. <mark style="color:blue;">**Granular Permissions in Pentaho / BA Server**</mark>
7. <mark style="color:blue;">**Java 21 Support & Tomcat 10**</mark>
8. <mark style="color:blue;">**Plugin Manager**</mark>
9. <mark style="color:blue;">**Karaf / OSGi removal and Big Data plugins**</mark>
10. <mark style="color:blue;">**OTEL-based observability**</mark>
11. <mark style="color:blue;">**Docker Simplification**</mark>

For an overview of the new features, see [What's New in 11.0](https://docs.pentaho.com/whats-new/readme).

## Bug Fixes

The following issues have been addressed in 11.0.

### Pentaho Data Integration Issues

The following issues in Pentaho Data Integration have been addressed.

<table data-full-width="true"><thead><tr><th>Issue ID</th><th>Description</th></tr></thead><tbody><tr><td>PDI-20592</td><td>Spoon throws an OutOfMemoryError when running jobs in parallel</td></tr><tr><td>PDI-20300</td><td>Bug - Carte Object ID is not captured in the channel logs table when execution is done through the <code>executeJob</code> API</td></tr><tr><td>PDI-20282</td><td>Failure to abort the main job even after the subjobs fail with an error.</td></tr><tr><td>PDI-20251</td><td>PDI data services - Missing Log4j-related libraries</td></tr><tr><td>PDI-20188</td><td>NullPointerException when saving a job/transformation to a file-based repository in Pentaho 10.2 and 10.1</td></tr><tr><td>PDI-20187</td><td>AWS v2 metadata check causes failure to start</td></tr><tr><td>PDI-20199</td><td>Spoon runs out of memory while running a job</td></tr><tr><td>PDI-19731</td><td>Separator is not working as expected in Text File Input and Text File Output.</td></tr><tr><td>PDI-20540</td><td>Avro Input step does not handle expected null fields</td></tr><tr><td>PDI-20404</td><td>Splash screen text capitalization</td></tr><tr><td>PDI-20194</td><td>Variable replacement in PVFS implementation is not working as expected</td></tr><tr><td>PDI-20319</td><td>Unable to read nested fields from a JSON file and throws "cannot find any data" with path error. (.js vs .json)</td></tr><tr><td>PDI-20160</td><td>Cannot extract files from an SFTP server when multiple copies of a job that uses the SFTP step are called</td></tr><tr><td>PDI-20105</td><td>MapReduce execution does not wait for KAR file installation before launching the mapper KTR</td></tr><tr><td>PDI-20220</td><td>Pan cannot run KTRs with PVFS URLs when the associated VFS connection config contains a variable</td></tr><tr><td>PDI-20159</td><td>REST API step - When processing an API URL, the space value is not rendered correctly</td></tr><tr><td>PDI-20589</td><td>Mail step in transformation fails when no auth is used</td></tr><tr><td>PDI-20546</td><td>[Transformation] Bulk load into Snowflake UI issue</td></tr><tr><td>PDI-20419</td><td>Bulk load into Amazon Redshift throws error: S3ServiceException: The AWS Access Key ID you provided does not exist in our records</td></tr><tr><td>PDI-20406</td><td>Too many transitive dependencies in the Excel and core plugins cause errors</td></tr><tr><td>PDI-20325</td><td>[Excel Input] Throws higher override value with IOUtils.SetByteArrayMaxOverride() exception</td></tr><tr><td>PDI-20295</td><td>10.2.x: Microsoft Excel Writer step is unable to write incoming rows to an MS Excel file.</td></tr><tr><td>PDI-20283</td><td>Excel Writer step fails to write XLS with java.lang.NoClassDefFoundError: com/zaxxer/sparsebits/SparseBitSet when "Shift existing cells down" is enabled</td></tr><tr><td>PDI-20189</td><td>Step (or job) names are unchanged to Japanese characters in PDI.</td></tr><tr><td>PDI-20601</td><td>/opt/pentaho/data-integration/logs is not writable as a mounted volume</td></tr><tr><td>PDI-20568</td><td>Cannot copy files using the job's Copy Files step from S3 bucket to S3 bucket</td></tr><tr><td>PDI-20563</td><td>Job Status API fails when multiple instances of the same job exist</td></tr><tr><td>PDI-20569</td><td>Error when attempting to copy a folder using S3 VFS (MinIO)</td></tr><tr><td>PDI-20548</td><td>When backing up with "import-export.sh", the value of the "add file name to result filenames" tag in the backed up job file changes from "Y" to "N".</td></tr><tr><td>PDI-20514</td><td>Using variables in S3 connection parameters: only the "region" variable is not retained after reopening the connection dialog</td></tr><tr><td>PDI-20495</td><td>Variable is not retained in "Timeout" field of "Get a file with FTP" step</td></tr><tr><td>PDI-20494</td><td>Variable is not retained when set in "Wait" column of "Check DB connections" entry</td></tr><tr><td>PDI-20485</td><td>"Put a file with FTP" PDI step "timeout" field does not store a variable from environment variables.</td></tr><tr><td>PDI-20484</td><td>"FTP Delete" PDI job entry step "timeout" field does not store a variable from environment variables.</td></tr><tr><td>PDI-20482</td><td>"Block this step until steps finish" PDI step Copy nr field does not store a variable from environment variables.</td></tr><tr><td>PDI-20455</td><td>NullPointerException encountered when trying to copy files using a VFS connection, combining TGZ notation and PVFS</td></tr><tr><td>PDI-20435</td><td>PDI fails to start when located in a folder with spaces in the path</td></tr><tr><td>PDI-20410</td><td>Performance degradation when using more than one Table Input on a transformation</td></tr><tr><td>PDI-20403</td><td>NullPointerException in Python Executor step during JSON parsing</td></tr><tr><td>PDI-20395</td><td>Error with Pentaho Reporting Output in PDI if a Groovy scripted datasource is used in the report: Caused by: org.apache.bsf.BSFException: unable to load language: groovy</td></tr><tr><td>PDI-20387</td><td>Azure ADLS2 VFS Block Blob fails when writing large files (> block size)</td></tr><tr><td>PDI-20377</td><td>As an ETL developer, I would expect Spoon to select data types that do not cause data corruption.</td></tr><tr><td>PDI-20372</td><td>Performance drag when comparing Pentaho PDI 9.3, 10.2.0.2 to Pentaho PDI 6.1</td></tr><tr><td>PDI-20371</td><td>As an ETL developer, I would expect the 'Discover metadata from a Text File' step to produce field sizes on integers that match the fields.</td></tr><tr><td>PDI-20370</td><td>Poor performance copying files from S3 to S3 using PVFS and MultiPartUpload</td></tr><tr><td>PDI-20369</td><td>As an ETL developer, I would expect the 'Discover metadata from a Text File' step to produce field sizes on strings.</td></tr><tr><td>PDI-20364</td><td>PDI (Kitchen) sporadically runtime error: 'Central Log Store is not initialized'</td></tr><tr><td>PDI-20342</td><td>Reporting Output step fails to create DataCacheFactory resulting in performance regression</td></tr><tr><td>PDI-20334</td><td>Transformation with Metadata Injection step and "Optional target file" field set causes deadlock, leading to server hang</td></tr><tr><td>PDI-20322</td><td>Disable gather performance metrics when scheduling jobs/KTRs from Spoon's schedule perspective</td></tr><tr><td>PDI-20311</td><td>Using "Run SSH commands" step to connect to destination with "OpenSSH_8.9p1 Ubuntu-3ubuntu0.10, OpenSSL 3.0.2 15 Mar 2022": fails</td></tr><tr><td>PDI-20301</td><td>UnsupportedEncodingException occurred while using Load file content in memory</td></tr><tr><td>PDI-20292</td><td>Record count is not accurately determined in the Text File Input step when multiple input files are used.</td></tr><tr><td>PDI-20262</td><td>Uploaded PDI job/transformation in PDI and saved in repository has a file size of 0 on the Properties screen</td></tr><tr><td>PDI-20219</td><td>Charts do not function in DET in 9.3.0.8</td></tr><tr><td>PDI-20206</td><td>Spoon PDI client: user unable to connect to repository if password has special characters and server is configured to use LDAP</td></tr><tr><td>PDI-20195</td><td>Inconsistent variable names recently created</td></tr><tr><td>PDI-20190</td><td>Issues with encoding when reading files with charset different from UTF-8</td></tr><tr><td>PDI-20183</td><td>Clustered Mapping (sub-transformation) step run on a Carte cluster causes the job to hang in a Running state if the next step is not clustered</td></tr><tr><td>PDI-20171</td><td>Modified JavaScript Value step in PDI 9.3.0.8 fails to terminate when setting variables</td></tr><tr><td>PDI-20154</td><td>Spoon crashes with NullPointerException when connected with Power User role</td></tr><tr><td>PDI-20135</td><td>HTTP Post step does not process configured file paths correctly</td></tr><tr><td>PDI-20106</td><td>Memory leak when accessing jobs and transformations concurrently on repository</td></tr><tr><td>PDI-20035</td><td>When the underlying MDI template steps are removed, errors persist.</td></tr><tr><td>PDI-20030</td><td>Move Files job entry does not move large files from S3 bucket to S3 bucket, and is missing the partSize logic</td></tr><tr><td>PDI-19926</td><td>Put a file with FTP: an error doesn't occur when local directory permissions are changed.</td></tr><tr><td>PDI-19803</td><td>Loss of functionality present in the PDI 'SFTP Put' step due to outdated jsch-0.1.54.jar</td></tr><tr><td>PDI-19550</td><td>The Carte jobStatus API was changed to always require a name parameter, even when a valid ID is provided</td></tr><tr><td>PDI-17941</td><td>Data Validator - Read allowed values from another step - Loses values</td></tr><tr><td>PDI-17634</td><td>Carte Server configured for SSL cannot be stopped from the command line</td></tr><tr><td>PDI-17311</td><td>Currency sign replaced by currency symbol (Â¤) specified in Regex Evaluation step errors out.</td></tr><tr><td>PDI-17310</td><td>Currency sign replaced by currency symbol (Â¤) specified in Generate Rows step errors out.</td></tr><tr><td>PDI-20172</td><td>Carte and Pentaho Server notify multiple TransFinished events when transformation fails or aborts</td></tr><tr><td>PDI-20161</td><td>Memory leak issues encountered on Pentaho 9.3.0.8 SP.</td></tr></tbody></table>

### Pentaho Business Analytics

The following issues have been addressed in the BA platform and Analyzer, Interactive Reporting, Report Designer, and Aggregation Designer components.

<table data-full-width="true"><thead><tr><th width="163">Issue ID</th><th width="694">Description</th></tr></thead><tbody><tr><td>BISERVER-15447</td><td>Bug - Schedule is displayed with server's timezone instead of browser's timezone, and it will not be triggered on time if the schedule is set up using browser's local timezone</td></tr><tr><td>BISERVER-15401</td><td>Post-upgrade task URL is still pointing to old documentation link.</td></tr><tr><td>BISERVER-15378</td><td>PUC - Help > hitachivantara.com... should be Help > pentaho.com...</td></tr><tr><td>BISERVER-15303</td><td>Run Once scheduler jobs do not terminate after running once.</td></tr><tr><td>BISERVER-15305</td><td>Cannot schedule blockout jobs in PUC; they get created as normal scheduled jobs</td></tr><tr><td>PPP-5768</td><td>Start time for monthly jobs is incorrect</td></tr><tr><td>BISERVER-15291</td><td>Wrong table used on migrate_old_quartz_data scripts</td></tr><tr><td>BISERVER-15279</td><td>Upgrade from 10.2.0.2 to 10.2.0.3 breaks due to large pentaho-mapreduce-libraries.zip file.</td></tr><tr><td>BISERVER-15277</td><td>Start/end date reflected in PUC does not consider the time zone when the scheduler is created from PDI</td></tr><tr><td>BISERVER-15180</td><td>Bug - Duplicate parameters are added to parameter dialog when clicking Tab to leave parameter's textbox</td></tr><tr><td>BISERVER-15216</td><td>Run Once - Next button disabled by default on Scheduler Page Two in PUC</td></tr><tr><td>BISERVER-15176</td><td>User-defined internal variables are crossing between schedules</td></tr><tr><td>BISERVER-15174</td><td>StringIndexOutOfBoundsException displaying schedules when using migration script</td></tr><tr><td>PPP-5469</td><td>The upgrade utility is ignoring the BACKUP_ROOT_PATH variable</td></tr><tr><td>PPP-5466</td><td>Upgrade utility does not detect /tmp correctly</td></tr><tr><td>PPP-5380</td><td>License screen for marketplace images shows no licenses.</td></tr><tr><td>BISERVER-15124</td><td>Enabling the RepositoryCleanerSystemListener on 10.2 causes server to not start.</td></tr><tr><td>BISERVER-15051</td><td>Bug - Scheduler showing internal variable usage from other jobs and cannot be cleared.</td></tr><tr><td>BISERVER-14374</td><td>Schedule is displayed with server's timezone instead of browser's timezone, and it will not be triggered on time if the schedule is set up using browser's local timezone</td></tr><tr><td>PRD-6184</td><td>HTML streaming format fails to generate report</td></tr><tr><td>PMD-1128</td><td>In macOS Ventura, unable to use PME</td></tr><tr><td>BISERVER-15168</td><td>Restored schedules from previous versions are missing on latest scheduler-plugin</td></tr><tr><td>BISERVER-15167</td><td>Schedules are lost during backup-restore procedure even when restore is successful on same version of Pentaho Server</td></tr><tr><td>ANALYZER-4150</td><td>Format MDX expression cannot be applied to measures on Analyzer UI</td></tr><tr><td>BISERVER-15148</td><td>Fresh installation of 10.2.0.0 and 10.2.0.1 will give scheduling errors</td></tr><tr><td>ANALYZER-4137</td><td>Reintroduce ability to delete filter and column when clicking OK on the alert that appears when deleting column from report that also has Top 10 numeric filter based on it</td></tr><tr><td>BISERVER-15406</td><td>PUC Administration - Operation permission revert fails – server ignores latest change and sends empty array</td></tr><tr><td>BISERVER-15407</td><td>CanUpload, CanDownload, and UploadDownloadAndScheduleKjbFunctionalTest automation tests failing with permissions errors</td></tr><tr><td>ANALYZER-4177</td><td>Column resizing in Analyzer reports inconsistent due to trash can hover zone interfering</td></tr><tr><td>PPP-5748</td><td>Intermittent redirect to CDF JS script instead of login or home page</td></tr><tr><td>PPP-5722</td><td>Logging in after session timeout redirects to RequireJS config file</td></tr><tr><td>PIR-1547</td><td>Control Type Selector for PIR Prompt Definition not displayed in Sapphire and Crystal themes</td></tr><tr><td>ANALYZER-4155</td><td>Subtotals not being displayed in Analyzer reports migrated from v9.3.0.0 to v10.1 and up.</td></tr><tr><td>BISERVER-15190</td><td>FileService throws NPE on no access, not found, or a depth of 0</td></tr><tr><td>PPP-5388</td><td>PUC - License Manager dialog shows accessibility outline border for hidden button</td></tr><tr><td>PPP-5238</td><td>Error when path ends with forward slash</td></tr><tr><td>BISERVER-15097</td><td>Random redirection to .js or .json files instead of Pentaho Home</td></tr><tr><td>BAD-1992</td><td>BIG DATA VFS [GCS] - Parquet/ORC IO throws an error when running or executing preview data functionality</td></tr><tr><td>BAD-1972</td><td>[Bigdata-EMR] EMR cluster is shut down on Amazon Hive Executor step failure when using existing cluster option.</td></tr><tr><td>BAD-1971</td><td>Amazon Job Executor and Hive Job Executor step do not work due to a change in Amazon API requirement</td></tr><tr><td>PPP-5904</td><td>Licensing exception because en_ZA locale is not found when trying to use a LLS server</td></tr><tr><td>PPP-5706</td><td>Spoon 10.2.0.3 crashes when using an expired offline license</td></tr><tr><td>PPP-5673</td><td>Local License Server is showing used counts of 1040 PDI cores on one client and 48 PDI cores on another client even though both servers only have 8 CPU cores</td></tr><tr><td>PPP-5609</td><td>Licensing - Regression - PUC - Offline mode - License page not displaying</td></tr><tr><td>PPP-5611</td><td>Licensing - Regression - PUC/PDI - Allows incorrect URL/Activation ID to corrupt an existing validated license</td></tr><tr><td>PPP-5598</td><td>Existence of unnecessary license libraries is causing an issue with some Mondrian features</td></tr><tr><td>BISERVER-15218</td><td>IMPORT/EXPORT UTILITY - the listing for emails and groups does not display in logs</td></tr><tr><td>PPP-5557</td><td>Re-evaluate the host ID implementation to ensure it remains consistent across machine restarts</td></tr><tr><td>PIR-1542</td><td>Unable to export PIR report data (HTML, CSV, PDF, Excel, Text) in PUC</td></tr><tr><td>PPP-5463</td><td>The Local License Server requires /tmp to allow executions</td></tr><tr><td>BISERVER-15169</td><td>There is no useful information that can aid debugging import-export utility</td></tr><tr><td>PPP-5378</td><td>.elmLicInfo.plt file gets corrupted by switching License Server providers and causes downtime</td></tr><tr><td>PPP-5283</td><td>Expired Offline Trial License File (.bin) does not show any information about expiration dates</td></tr><tr><td>PPP-5264</td><td>Licensing - Offline license files show trial expiry even though the trial duration has not been exceeded</td></tr><tr><td>PIR-1513</td><td>Database query is not cancelled when clicking Cancel during the run/build of an Interactive Report</td></tr><tr><td>BAD-1942</td><td>[Bigdata|CDP71SecureJ11] YARN job fails when executing Start a PDI Cluster on YARN "locally" leaving PDI Client Archive field blank.</td></tr><tr><td>BISERVER-15275</td><td>Jobs and transformations are hidden by default when using PUC upload facility</td></tr><tr><td>BISERVER-15420</td><td>Errors occur due to missing Java opens on Pentaho Executable installer</td></tr><tr><td>BISERVER-15271</td><td>NoClassDefFoundError: com/zaxxer/sparsebits/SparseBitSet error when executing a transformation with Microsoft Excel Writer step using .xls format and "shift existing cells down" setting on Pentaho Server.</td></tr><tr><td>BISERVER-15247</td><td>Files written to Local VFS are locked at the OS level</td></tr><tr><td>BISERVER-15191</td><td>[Bigdata] PMR job fails with ApacheVanilla shim.</td></tr><tr><td>BISERVER-15184</td><td>[Bigdata] Parquet Input step fails to read files from Azure Cloud Storage (ADLSGen2)</td></tr><tr><td>BAD-1961</td><td>[Bigdata] Pentaho MapReduce job to read/write from Cloud Storage (S3) fails with emr700 shim</td></tr><tr><td>PRD-6169</td><td>Cannot preview or export large MS Excel files with PRD and the latest POI</td></tr><tr><td>ANALYZER-4144</td><td>Large table reports cannot be exported to MS Excel based on changes to POI</td></tr><tr><td>BAD-1955</td><td>[Bigdata] ORC input/output steps fail when connected to EMR cluster</td></tr><tr><td>BISERVER-15128</td><td>Excel reports generated using newer Apache POI library leave larger files on Tomcat's temp directory</td></tr><tr><td>PIR-1529</td><td>PIR Save/Open fails when a calculated field exists</td></tr><tr><td>PIR-1528</td><td>FATAL ERROR when using calculated fields (with > or &#x3C; and no space between field and operator) in Pentaho v10.1 Interactive Reports</td></tr><tr><td>BISERVER-15414</td><td>Pentaho Server does not start if the server folder path has spaces in the name</td></tr><tr><td>PIR-1568</td><td>PIR 10.2.0.6 – Firefox: Reports with pipe symbol “|” in the saved file name are not editable</td></tr><tr><td>BISERVER-15379</td><td>Older and newer AWS JARs exist together after applying SP 10.2.0.3.</td></tr><tr><td>BISERVER-15374</td><td>Inconsistent JAR deployment between incremental and direct SP 10.2.0.5 installation.</td></tr><tr><td>PRD-6224</td><td>Report Designer: Numeric format not applied to Excel and PDF exports.</td></tr><tr><td>PMD-1134</td><td>Unable to start Metadata Editor OSGi version; startup gets stuck.</td></tr><tr><td>BISERVER-15349</td><td>Simple trigger schedules display “undefined” after upgrade to 10.2.0.2 and above</td></tr><tr><td>BISERVER-15341</td><td>Cannot use "-" dash character on username when security is Jackrabbit</td></tr><tr><td>BISERVER-15339</td><td>10.2.0.4 introduced regression in Karaf that breaks SAML plugin</td></tr><tr><td>BISERVER-15302</td><td>Tooltips do not work for 'Browse files' when browser page is reloaded in 10.2</td></tr><tr><td>BISERVER-15276</td><td>Schedules created via Spoon are missing after restoring the Pentaho Repository using import-export utility.</td></tr><tr><td>ANALYZER-4174</td><td>PDF export of line (and similar) graph shows inaccurate time horizon on X axis</td></tr><tr><td>PRD-6195</td><td>Change the error message that is displayed after applying the fix on PRD-6182</td></tr><tr><td>BISERVER-15257</td><td>Pentaho import issue with special characters in filenames</td></tr><tr><td>PPP-5648</td><td>Import-export does not import all schedules correctly</td></tr><tr><td>PIR-1550</td><td>Fix Interactive Reporting plugin unit test (handleMissingFields)</td></tr><tr><td>PRD-6186</td><td>PRD query editor resets back to the default value of disable_distinct after making changes</td></tr><tr><td>ANALYZER-4166</td><td>HTTP Status 400 - Bad Request error with Filter link when using German, French and Japanese language in Pentaho 10.2</td></tr><tr><td>BAD-1967</td><td>[Bigdata] Parquet and ORC Input Output steps fail to read/write from S3 when running jobs using kitchen.sh</td></tr><tr><td>PRD-6182</td><td>PRD query editor does not correctly parse complex conditions and throws a NullPointerException</td></tr><tr><td>BISERVER-15219</td><td>Default HyperSQL (HSQLDB) in-memory DB start script with error</td></tr><tr><td>BISERVER-15211</td><td>PIR in Edit mode gets frozen after pressing Esc after selecting "Select ..." in the General tab of Template Selector dialog</td></tr><tr><td>BISERVER-15243</td><td>Unable to log in with new non-admin user with a password that includes all special characters on the keyboard Ã‡-[~!@#$%^&#x26;*(){}|.,]-=_+|;'"?&#x3C;>~`:</td></tr><tr><td>PPP-5546</td><td>Ops Mart: Generate_DIM_DATE transformation hardcoded to generate dates for about 20 years starting on 20050101</td></tr><tr><td>PRD-6179</td><td>PRD - Unable to connect to MongoDB in Pentaho Report Designer v10.x due to missing pentaho-mongo-utils.jar</td></tr><tr><td>PRD-6177</td><td>With Java 17, the property settings in "Edit Chart" within Report Designer are no longer editable.</td></tr><tr><td>BISERVER-15179</td><td>Revision required for Details section of New Schedule dialog on Scheduler plugin</td></tr><tr><td>BISERVER-15178</td><td>appendDateFormat attribute is treated as parameter or variable under Scheduler perspective</td></tr><tr><td>BISERVER-15173</td><td>StringIndexOutOfBoundsException displaying schedules with many variables on them</td></tr><tr><td>PRD-6173</td><td>RowLimit while exporting Excel for PRD report does not work in PUC</td></tr><tr><td>BISERVER-15161</td><td>Schedule a Report - Trigger Execute Now - Last run column is not updated</td></tr><tr><td>PIR-1538</td><td>Manage Data Sources - Delete a field from a datasource present in a saved PIR report (column and group) - Only one message appears</td></tr><tr><td>BISERVER-15156</td><td>Multiple report executions result when using Execute Now on daily recurrence</td></tr><tr><td>BISERVER-15155</td><td>File size in KB is calculated through division by 1000 instead of 1024</td></tr><tr><td>ANALYZER-4149</td><td>Percentage measure displayed incorrectly on the Trend Line in Pentaho v10.2</td></tr><tr><td>BISERVER-15147</td><td>Shell Job entry step invoking Perl script fails</td></tr><tr><td>BISERVER-15145</td><td>Prevent the creation of usernames with leading/trailing whitespaces</td></tr><tr><td>BISERVER-15144</td><td>Invalid database connection is saved and used despite "Cancel"</td></tr><tr><td>BISERVER-15139</td><td>"Files" text box displays an ellipsis (...) when the file name is very long</td></tr><tr><td>BISERVER-15135</td><td>Username with prefix or suffix blank spaces on login page triggers UsernameNotFoundException, but session is created</td></tr><tr><td>ANALYZER-4145</td><td>Multiselect feature for Analyzer report filter no longer requires holding CTRL key</td></tr><tr><td>ANALYZER-4143</td><td>Analyzer reports are re-executed when saving and editing, creating performance issues</td></tr><tr><td>BISERVER-15125</td><td>Sparkl (App Builder) plugin not available for Pentaho 9.3 or 10.2</td></tr><tr><td>BISERVER-15101</td><td>Schedule a Report - Execute Now after report is run for the first time and in the next minute - Reports are generated twice</td></tr><tr><td>PPP-5127</td><td>Turn autoDeploy from true to false in Tomcat's server.xml due to security concerns</td></tr><tr><td>BISERVER-15098</td><td>PUC: folders don't update the Last Modified date</td></tr><tr><td>PAD-179</td><td>ODBC access type does not work and should be removed from connection dialogs</td></tr><tr><td>PSW-282</td><td>ODBC access type does not work and should be removed from connection dialogs</td></tr><tr><td>PMD-1119</td><td>ODBC access type does not work and should be removed from connection dialogs</td></tr><tr><td>PRD-6162</td><td>ODBC access type does not work and should be removed from connection dialogs</td></tr><tr><td>PDB-2096</td><td>View Mode wrong tooltip text</td></tr><tr><td>PIR-1524</td><td>Load PIR in blank without error message, InteractiveAdhocReportUtils.ERROR_0002 - Unable to load report query</td></tr><tr><td>BISERVER-14919</td><td>PRPT any report using formula calculation fails when running Pentaho 9.4 in a docker container or server using UTC timezone</td></tr><tr><td>PRD-6138</td><td>Bar codes not displayed in Excel or HTML (single-page) report output for newly created reports</td></tr><tr><td>BISERVER-13909</td><td>Uploaded PDI Job/Transformation has file size of 0 on the Properties screen</td></tr><tr><td>MONDRIAN-2752</td><td>UserDefinedFunction scripting capability broken due to removal of Nashorn scripting engine from JDK</td></tr><tr><td>MONDRIAN-2751</td><td>MemberFormatter scripting capability broken due to removal of Nashorn scripting engine from JDK</td></tr><tr><td>MONDRIAN-2750</td><td>PropertyFormatter scripting capability broken due to removal of Nashorn scripting engine from JDK</td></tr><tr><td>MONDRIAN-2749</td><td>CellFormatter scripting capability broken due to removal of Nashorn scripting engine from JDK</td></tr><tr><td>MONDRIAN-2646</td><td>Mondrian does not cache empty children requests - generates numerous queries</td></tr><tr><td>PRD-6156</td><td>Strange behavior of parameter text box with parameterized query</td></tr><tr><td>PDB-2103</td><td>Prompts are not in sequence</td></tr><tr><td>BISERVER-14394</td><td>PUC - XML parsing error: no root element found - Firefox</td></tr><tr><td>BISERVER-14274</td><td>Schedule: error in console for more than 25 schedules</td></tr></tbody></table>

## Security Issues Addressed

The following vulnerabilities have been addressed in 11.0. Several vulnerabilities are already addressed in 10.2 service packs. These fixes are also included in 11.0 but not listed here. Review the relevant service pack notes for details.

<table><thead><tr><th width="170.9791259765625">CVE ID</th><th>Details</th></tr></thead><tbody><tr><td>CVE-2020-17521</td><td>https://nvd.nist.gov/vuln/detail/CVE-2020-17521</td></tr><tr><td>CVE-2025-55752</td><td>https://nvd.nist.gov/vuln/detail/CVE-2025-55752</td></tr><tr><td>CVE-2025-30065</td><td>https://nvd.nist.gov/vuln/detail/CVE-2025-30065</td></tr><tr><td>CVE-2025-41248</td><td>https://nvd.nist.gov/vuln/detail/CVE-2025-41248</td></tr><tr><td>CVE-2025-41249</td><td>https://nvd.nist.gov/vuln/detail/CVE-2025-41249</td></tr><tr><td>CVE-2025-22228</td><td>https://nvd.nist.gov/vuln/detail/CVE-2025-22228</td></tr><tr><td>CVE-2025-27820</td><td>https://nvd.nist.gov/vuln/detail/CVE-2025-27820</td></tr><tr><td>CVE-2015-6420</td><td>https://nvd.nist.gov/vuln/detail/CVE-2015-6420</td></tr><tr><td>CVE-2015-1832</td><td>https://nvd.nist.gov/vuln/detail/CVE-2015-1832</td></tr><tr><td>CVE-2009-4611</td><td>https://nvd.nist.gov/vuln/detail/CVE-2009-4611</td></tr><tr><td>CVE-2025-46762</td><td>https://nvd.nist.gov/vuln/detail/CVE-2025-46762</td></tr><tr><td>CVE-2021-33813</td><td>https://nvd.nist.gov/vuln/detail/CVE-2021-33813</td></tr><tr><td>CVE-2025-52099</td><td>https://nvd.nist.gov/vuln/detail/CVE-2025-52099</td></tr><tr><td>CVE-2025-9230</td><td>https://nvd.nist.gov/vuln/detail/CVE-2025-9230</td></tr><tr><td>CVE-2024-6162</td><td>https://nvd.nist.gov/vuln/detail/CVE-2024-6162</td></tr><tr><td>CVE-2025-35036</td><td>https://nvd.nist.gov/vuln/detail/CVE-2025-35036</td></tr><tr><td>CVE-2023-5072</td><td>https://nvd.nist.gov/vuln/detail/CVE-2023-5072</td></tr><tr><td>CVE-2024-1635</td><td>https://nvd.nist.gov/vuln/detail/CVE-2024-1635</td></tr><tr><td>CVE-2024-7885</td><td>https://nvd.nist.gov/vuln/detail/CVE-2024-7885</td></tr><tr><td>CVE-2023-4639</td><td>https://nvd.nist.gov/vuln/detail/CVE-2023-4639</td></tr><tr><td>CVE-2023-5685</td><td>https://nvd.nist.gov/vuln/detail/CVE-2023-5685</td></tr><tr><td>CVE-2023-1973</td><td>https://nvd.nist.gov/vuln/detail/CVE-2023-1973</td></tr><tr><td>CVE-2024-47554</td><td>https://nvd.nist.gov/vuln/detail/CVE-2024-47554</td></tr><tr><td>CVE-2024-5971</td><td>https://nvd.nist.gov/vuln/detail/CVE-2024-5971</td></tr><tr><td>CVE-2024-57699</td><td>https://nvd.nist.gov/vuln/detail/CVE-2024-57699</td></tr><tr><td>CVE-2025-6297</td><td>https://nvd.nist.gov/vuln/detail/CVE-2025-6297</td></tr><tr><td>CVE-2023-31484</td><td>https://nvd.nist.gov/vuln/detail/CVE-2023-31484</td></tr><tr><td>CVE-2023-45853</td><td>https://nvd.nist.gov/vuln/detail/CVE-2023-45853</td></tr><tr><td>CVE-2025-6020</td><td>https://nvd.nist.gov/vuln/detail/CVE-2025-6020</td></tr><tr><td>CVE-2024-4741</td><td>https://nvd.nist.gov/vuln/detail/CVE-2024-4741</td></tr><tr><td>CVE-2024-56406</td><td>https://nvd.nist.gov/vuln/detail/CVE-2024-56406</td></tr></tbody></table>


# Try Pentaho Data Integration and Analytics

Learn how to install an evaluation version of Pentaho Data Integration and Analytics, then get started with basic concepts, walk-throughs, and workflows.

Pentaho Data Integration and Analytics is a platform for access and analytics. It supports flat files, relational databases, Hadoop, NoSQL, and cloud sources. Use it to integrate, transform, visualize, and analyze data. Use the APIs to extend reports, queries, and transformations.

## Install the 30-day trial of Pentaho Data Integration and Analytics

The Pentaho Installation Wizard is a streamlined way to install, learn about, and evaluate the Pentaho Suite. With this 30-day trial, you can install and test Pentaho Business Analytics (BA) and Data Integration (DI).

To get started fast after installation, follow the [Pentaho Data Integration (PDI) tutorial](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/pdi-transformation-tutorial).

If you have issues with the 30-day trial, contact the [Pentaho Trial Experts](mailto:trialexperts.pentaho@hitachivantara.com).

{% hint style="warning" %}
**Important**: Moving to development or production is not supported for installations completed with the Pentaho Installation Wizard.
{% endhint %}

With the Pentaho Installation Wizard you can choose one of two install types:

* **Default**: Select **Keep it simple. Give me everything.**
* **Custom**: Select **Let me decide for myself.**

### Process overview

Installation instructions are the same for Windows, Linux, and macOS.

Complete these tasks in order:

1. [Download the trial software](#download-the-trial-software)
2. [Start the Pentaho Installation Wizard](#start-the-pentaho-installation-wizard)
3. Choose a [default installation](#default-installation) or [custom installation](#custom-installation).
4. [Verify installation](#verify-installation)
5. [Getting started tutorial](#getting-started-tutorial)

| Explore Considerations        |                                                                                                                                                                                                 |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| You Supply                    | A computer that meets Pentaho's [operating system and hardware requirements](https://docs.pentaho.com/pdia-try-pdia/components-reference).                                                      |
| We Supply                     | <ul><li>Installation Package</li><li>Oracle JRE</li><li>Repository Platform (PostgreSQL)</li><li>Repository Platform JDBC Driver (PostgreSQL)</li><li>Web Application Server (Tomcat)</li></ul> |
| Technologies Used             | <ul><li>Tomcat web application server</li><li>PostgreSQL database to house the Pentaho Repository</li></ul>                                                                                     |
| Expertise                     | <ul><li>Basic computer knowledge.</li></ul>                                                                                                                                                     |
| Approximate Installation Time | 30 minutes                                                                                                                                                                                      |

### Download the trial software

To download the software, complete these steps.

1. Make sure you are logged in to the computer where you want to install the software.

   You should use an account that can install software.

   * On Windows, this is typically an account with administrator privileges.
   * On Linux, this is also an account with administrator privileges.
2. Navigate to the [Pentaho trial download](https://www.hitachivantara.com/en-us/products/data-management-analytics/pentaho/download-pentaho.html) website.
3. Click **Start Your 30-Day Trial**.

   The **Submission Agreement** form appears.
4. Fill in the requested information and click **Submit**.

   The **Getting Started with**   \
   **Pentaho Data Integration & Analytics** page opens.
5. In the **On-Prem** section, click **Download** for your operating system.
6. When prompted, choose a directory for the installer and wait for the download to finish.
7. If you are using Linux, make sure you can execute the file.

   Open a terminal, go to the directory where you downloaded the file, then run:

   ```
   chmod a+x ./pentaho-business-analytics-10.3.0-x64.bin
   ```

### Start the Pentaho Installation Wizard

To start the installation wizard, complete the following steps.

{% hint style="info" %}
**Note:** Launch the installation wizard from a locally mounted hard drive only. Network-mounted drives (for example NFS) are not supported.
{% endhint %}

Do one of the following.

* **Windows**: Open File Explorer, go to the installer, then double-click `pentaho-business-analytics-10.3.0-x64.exe`.
* **macOS**: Unpack `pentaho-business-analytics-10.3.0-x64.app.tar.gz`, then double-click `pentaho-business-analytics-10.3.0-x64.app`.
* **Linux (graphics)**: Open a terminal, go to the installer, then run:

  ```
  ./pentaho-business-analytics-10.3.0-x64.bin
  ```
* **Linux (no graphics)**: Open a terminal, go to the installer, then run one of these:
  * GTK text mode:

    ```
    ./pentaho-business-analytics-10.3.0-x64.bin --mode text
    ```
  * OpenMotif X mode:

    ```
    ./pentaho-business-analytics-10.3.0-x64.bin --mode xwindow
    ```

### Default installation

If you want to install every component and some sample data, complete the following steps. If you want a custom install, see [Custom installation](#custom-installation).

{% hint style="warning" %}
**Important:** You cannot install into a directory that already exists. On Linux, do not install under `/opt/`. It can cause permissions problems.
{% endhint %}

1. After you start the wizard, the splash screen appears, then the **Pentaho Business Analytics installation is ready!** window. Click **Next**.

   ![Install is ready. Click Next](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-609ad99a0695960ffaedf97fb3d8664bacecbf1e%2Fpdi_install_ready_screen_w532.png?alt=media)
2. Read the license agreement. Select **Accept**, then click **Next**.
3. In **Installation folder**, accept the default directory or enter a different path, then click **Next**.

   ![Choose Pentaho installation directory](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-c918e37d17233d7bb5667d29dee2e73a5ee07436%2Fpdi_install_choose_install_directory_w532.png?alt=media)
4. You are prompted to add a PostgreSQL password. Enter and confirm the password for the `postgres` user.

   <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p><strong>Important:</strong> Do not use these characters in the password: <code>' " &#x26; &#x3C; > \</code></p></div>
5. Click **Next**.
6. In the **What do you want to install?** window, select **Keep it simple. Give me everything**, then click **Next.**&#x20;
7. If the **Sample Database** window appears, enter a port number, then click **Next**.

   This prompt appears only if the default ports are not available.
8. In the **Pentaho License Information** window, leave the box empty and click **Next**. A 30-day license is installed for the trial.
9. In **We're Set. Let's install!** window, click **Next**. Installation begins and takes about 30 minutes to complete.
10. When installation is complete, select **Pentaho Data Integration** to launch Spoon.

    ![Select Pentaho Data Integration](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-03ce14c87150597334ccdf4aa251fc670eb3d68a%2Fpdi_install_launch_chooser_w532.png?alt=media)
11. Click **Finish**.

    After PDI starts, you will see the **Welcome!** window.

    ![Welcome to Pentaho Data Integration](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-6944eb3e4405bf79bd1505edf4356dd482f20657%2Fpdi_install_welcome_to_pdi_landing_page_w532.png?alt=media)

    To get started quickly after installation, follow the [Pentaho Data Integration (PDI) tutorial](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/pdi-transformation-tutorial).

If you have trouble with the installation wizard, see the [Administer Pentaho Data Integration and Analytics](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/iFWuQjAZNxh1EoQbRnsT/) document.

### Custom installation

If you want to choose which components to install and whether to install sample data, complete the following steps. If you want the default install, see [Default installation](#default-installation).

{% hint style="warning" %}
**Note:** You cannot install into a directory that already exists. On Linux, do not install under `/opt/`. It can cause permissions problems.
{% endhint %}

1. After you start the wizard, the splash screen appears, then the **Pentaho Business Analytics installation is ready!** window. Click **Next**.

   ![Install is ready. Click Next](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-609ad99a0695960ffaedf97fb3d8664bacecbf1e%2Fpdi_install_ready_screen_w532.png?alt=media)
2. Read the license agreement. Select **Accept**, then click **Next**.
3. In **Installation folder**, accept the default directory or enter a different path, then click **Next**.

   ![Choose Pentaho installation directory](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-c918e37d17233d7bb5667d29dee2e73a5ee07436%2Fpdi_install_choose_install_directory_w532.png?alt=media)
4. You are prompted to add a PostgreSQL password. Enter and confirm the password for the `postgres` user.

   <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p><strong>Important:</strong> Do not use these characters in the password: <code>' " &#x26; &#x3C; > \</code></p></div>
5. Click **Next**.&#x20;
6. If the **Sample Database** window appears, enter a port number, then click **Next**.

   This prompt appears only if the default ports are not available.
7. In the **What do you want to install?** window, select **Let me decide for myself**, then click **Next**.&#x20;
8. Select the components you want to install, then click **Next**.
9. Select whether to include sample content, then click **Next**.
10. If the **Sample Database** window appears, enter a port number, then click **Next**.
11. In the **Pentaho License Information** window, leave the box empty and click **Next**. A 30-day license is installed for the trial.
12. In **We're Set. Let's install!** window, click **Next**. Installation begins and takes about 30 minutes to complete.
13. When installation is complete, select the components you want to launch and click **Finish**.

If you have trouble with the installer, see the [Administer Pentaho Data Integration and Analytics](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/iFWuQjAZNxh1EoQbRnsT/) document.

### Verify installation

To verify the installation, review the directory structure and the installation summary file.

1. Open a file explorer or command line tool.
2. Navigate to the install directory and compare it to the structure below.

   ```
   pentaho/
   pentaho/design-tools/
   pentaho/design-tools/aggregation-designer/
   pentaho/design-tools/data-integration/
   pentaho/design-tools/metadata-editor/
   pentaho/design-tools/report-designer/
   pentaho/design-tools/schema-workbench/
   pentaho/documentation/
   pentaho/java/
   pentaho/jdbc-distribution/
   pentaho/license-installer/
   pentaho/licenses/pentaho/monetdb/
   pentaho/postgresql/
   pentaho/scripts/
   pentaho/server/
   ```
3. Open `installation-summary.txt`. Make sure it lists the design tools and plugins you installed.
4. Review the file locations below.

   | File                       | Description                                                                                      |
   | -------------------------- | ------------------------------------------------------------------------------------------------ |
   | `ctlscript.sh`             | Starts, stops, restarts, and shows the status of Pentaho services. Available on Linux and macOS. |
   | `installation-summary.txt` | Contains the information from the summary screen at the end of the installation process.         |
   | `uninstall`                | A script that removes Pentaho Business Analytics.                                                |

   | Tool/Plugin              | Location                                                                                |
   | ------------------------ | --------------------------------------------------------------------------------------- |
   | Pentaho Server           | `pentaho/server/pentaho-server/`                                                        |
   | Report Designer          | `pentaho/design-tools/report-designer/`                                                 |
   | Schema Workbench         | `pentaho/design-tools/schema-workbench/`                                                |
   | Data Integration (Spoon) | `pentaho/design-tools/data-integration/`                                                |
   | Metadata Editor          | `pentaho/design-tools/metadata-editor/`                                                 |
   | Aggregation Designer     | `pentaho/design-tools/aggregation-designer/`                                            |
   | Dashboard Designer       | `pentaho/server/pentaho-server/pentaho-solutions/system/dashboards/`                    |
   | Analyzer                 | `pentaho/server/pentaho-server/pentaho-solutions/system/analyzer/`                      |
   | Interactive Reports      | `pentaho/server/pentaho-server/pentaho-solutions/system/pentaho-interactive-reporting/` |
   | License Installer        | `pentaho/license-installer/`                                                            |

   | Log                                                 | Location                                     |
   | --------------------------------------------------- | -------------------------------------------- |
   | Pentaho Server Logs for BA configuration            | `pentaho/server/pentaho-server/logs/`        |
   | Tomcat Logs for Pentaho Server for BA configuration | `pentaho/server/pentaho-server/tomcat/logs/` |

   For macOS, copy the JDBC `.jar` into the location listed for Report Designer.

   | JDBC Driver                         | Location                                             |
   | ----------------------------------- | ---------------------------------------------------- |
   | Pentaho Server for BA configuration | `pentaho/server/pentaho-server/tomcat/lib/`          |
   | Report Designer                     | `pentaho/design-tools/report-designer/lib/jdbc/`     |
   | Schema Workbench                    | `pentaho/design-tools/schema-workbench/drivers/`     |
   | Aggregation Designer                | `pentaho/design-tools/aggregation-designer/drivers/` |
   | Metadata Editor                     | `pentaho/design-tools/metadata-editor/libext/JDBC/`  |
   | PDI client (Spoon)                  | `pentaho/design-tools/data-integration/lib/`         |

   | Port Number | Description                                   |
   | ----------- | --------------------------------------------- |
   | 5432        | PostgreSQL Server                             |
   | 8080        | Pentaho Server Tomcat Web Server Startup Port |
   | 8012        | Pentaho Server Shutdown Port                  |
   | 9001        | HSQL Server Port                              |
   | 9092        | Embedded H2 Database                          |

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> Your port numbers might differ. If you installed using the installation wizard, check <code>installation-summary.txt</code> for the actual ports.</p></div>

### Getting started tutorial

To get started quickly after installation, follow the [Pentaho Data Integration (PDI) tutorial](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/pdi-transformation-tutorial).

## Start and stop the PDI client on Windows

If you installed PDI on Windows using the installation wizard, start Spoon from: **Start** > **All Programs** > **Pentaho Enterprise Edition** > **Design Tools** > **Data Integration**.

## Start and stop the Pentaho Server for configuration on Windows

When you ran the installation wizard on Windows, the Pentaho Server deployed in an included Apache Tomcat application server. Manage Pentaho and Tomcat from: **Start** > **All Programs** > **Pentaho Enterprise Edition** > **Server Management**.

Use one of these menu items:

* **Start Pentaho Server**
* **Stop Pentaho Server**

The installer also registered services for:

* **Pentaho Server**
* **Data Integration**
* **Pentaho Repository**

You can start and stop these services from **Control Panel** > **Administrative Tools** > **Services**.

## Start and stop the Pentaho Server for configuration on Linux

When you ran the installation wizard on Linux, the Pentaho Server deployed in an included Apache Tomcat application server. Use `/pentaho/ctlscript.sh` to start and stop services.

Common arguments:

* `start`
* `stop`
* `restart`
* `status`
* `help`

Common services:

* `pentahoserver`
* `postgresql`

Examples:

```
./ctlscript.sh start pentahoserver
./ctlscript.sh status pentahoserver
./ctlscript.sh status postgresql
./ctlscript.sh help
```

## Adjust Java VM memory limits for an installation on Windows

Windows users might see out-of-memory errors. Increase the Java VM memory allocation to fix them.

{% hint style="info" %}
**Note:** These steps apply when you installed with the installation wizard.
{% endhint %}

1. Stop the Pentaho Server. See [Start and stop the Pentaho Server for configuration on Windows](#start-and-stop-the-pentaho-server-for-configuration-on-windows).
2. Double-click `pentahoserverw.exe` in `server\pentaho-server\tomcat\bin` to open **Pentaho Server Properties**.

   You might need to select **Run as Administrator**.
3. Select the **Java** tab.

   ![Windows Properties dialog box](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-2a1f41d402a763f44322846527b4cf79417c916a%2FWindows%20properties%20dialog%20box.png?alt=media)
4. Set:
   * **Initial memory pool**: `6144` MB
   * **Maximum memory pool**: `8192` MB
5. Start the Pentaho Server. See [Start and stop the Pentaho Server for configuration on Windows](#start-and-stop-the-pentaho-server-for-configuration-on-windows).

If the JVM refuses to start, you might need to add RAM, stop memory-intensive services, or lower the maximum memory limit.

## Adjust Java VM memory limits for a graphical installation on Linux

These steps apply when you installed using the installation wizard, your computer can display graphics, and you are running Linux.

1. Stop the server. See [Start and stop the Pentaho Server for configuration on Linux](#start-and-stop-the-pentaho-server-for-configuration-on-linux).
2. Go to `pentaho-server/tomcat/scripts`.
3. Edit `ctl.sh`.
4. Locate the line under `start tomcat`, which looks like this:

   ```
   export JAVA_OPTS="... -Xms128m -Xmx768m -XX:MaxPermSize=256m ..."
   ```
5. Set the memory to a minimum of `4096` MB and a maximum of `6144` MB, based on available system memory.
6. Start the server. See [Start and stop the Pentaho Server for configuration on Linux](#start-and-stop-the-pentaho-server-for-configuration-on-linux).

If the JVM refuses to start, add RAM, stop memory-intensive services, or lower the maximum memory limit.

## Increase Pentaho Server memory limit for installations on Windows

If you installed the Pentaho Server on Windows using the installation wizard, you can increase the server memory limits by editing the Tomcat Java settings.

{% hint style="info" %}
**Notes:**

* For Linux, see [Increase Pentaho Server memory limit for installations on Linux](#increase-pentaho-server-memory-limit-for-installations-on-linux).
* For a custom install, see **Configure and start the Pentaho Server after manual installation** in the **Install Pentaho Data Integration and Analytics** document.
  {% endhint %}

1. Stop the Pentaho Server if it is running. See [Start and stop the Pentaho Server for configuration on Windows](#start-and-stop-the-pentaho-server-for-configuration-on-windows).
2. Type `services.msc` into the Windows Search box.
3. Find the Pentaho Server entry and note the **service name**.

   It should be `pentahoserver`.
4. In `C:\pentaho\server\pentaho-server\tomcat\bin\`, rename `tomcat8w.exe` to match the service name.

   Example: `pentahoserverw.exe`.
5. Double-click the renamed file to open the **Properties** window.

   You might need to select **Run as Administrator**.
6. Select the **Java** tab.
7. Set:
   * Minimum: `4096` MB
   * Maximum: `6144` MB
8. Start the Pentaho Server. See [Start and stop the Pentaho Server for configuration on Windows](#start-and-stop-the-pentaho-server-for-configuration-on-windows).

If the JVM refuses to start with increased limits, add RAM, stop memory-intensive services, or reduce the maximum memory limit.

See also: [Increase the PDI client memory limit](#increase-the-pdi-client-memory-limit).

## Increase Pentaho Server memory limit for installations on Linux

If you installed PDI on Linux using the installation wizard, you can increase memory limits by editing a variable in a Pentaho-supplied script.

{% hint style="info" %}
**Note:**

* For Windows, see [Increase Pentaho Server memory limit for installations on Windows](#increase-pentaho-server-memory-limit-for-installations-on-windows).
* For a custom install, see **Configure and start the Pentaho Server after manual installation** in the **Install Pentaho Data Integration and Analytics** document.
  {% endhint %}

1. Stop the server. See [Start and stop the Pentaho Server for configuration on Linux](#start-and-stop-the-pentaho-server-for-configuration-on-linux).
2. Go to `pentaho-server/tomcat/scripts`.
3. Edit `ctl.sh`.
4. Locate the line under `start tomcat`, which looks like this:

   ```java
   export JAVA_OPTS="-Dpentaho.installed.licenses.file=/opt/pentaho/.installedLicenses.xml -Xms128m -Xmx768m -XX:MaxPermSize=256m -Dsun.rmi.dgc.client.gcInterval=3600000 -Dsun.rmi.dgc.server.gcInterval=3600000"
   ```
5. Set the memory to a minimum of `4096` MB and a maximum of `6144` MB, based on available system memory.
6. Start the server. See [Start and stop the Pentaho Server for configuration on Linux](#start-and-stop-the-pentaho-server-for-configuration-on-linux).

See also: [Increase the PDI client memory limit](#increase-the-pdi-client-memory-limit).

## Increase the PDI client memory limit

As a best practice, increase PDI's memory limit so Spoon can perform memory-intensive tasks. You must increase the memory limit for both the Pentaho Server and the PDI client.

{% hint style="info" %}
**Note:** Instead of modifying the PDI client startup script, you can set the environment variable `PENTAHO_DI_JAVA_OPTIONS` to `-Xmx2g -XX:MaxPermSize=256m` on your client.
{% endhint %}

## Uninstalling the Pentaho Suite after evaluation

To uninstall the Pentaho Suite after evaluation:

1. Go to the `pentaho` directory and run the uninstall file.
2. Follow the Uninstall Wizard.
3. When prompted, choose whether to delete the data files.
4. Restart your computer.

Before you install a production version of Pentaho, uninstall the evaluation version first.

## Tutorials

Review these tutorials to start using PDI, reporting tools, and dashboards.

If you are new to PDI, start with [Getting Started with PDI](https://docs.pentaho.com/pdia-try-pdia/getting-started-with-pdi).

Within this tutorial, you can also view:

* [PDI Transformation Tutorial](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/pdi-transformation-tutorial)
* [PDI Job Tutorial](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/pdi-job-tutorial)
* [Getting started with PDI and Hadoop](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/getting-started-with-pdi-and-hadoop)

The [Getting Started with Analyzer, Interactive Reports, and Dashboard Designer](https://docs.pentaho.com/pdia-try-pdia/getting-started-with-analyzer-interactive-reports-and-dashboard-designer) tutorial covers product features, best practices, and troubleshooting.

Within that tutorial, you can also view:

* [About Pentaho business analytics tools](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/about-pentaho-business-analytics-tools)
* [Get started with Pentaho Reporting tools](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/get-started-with-pentaho-reporting-tools)
* [Quick tour of the Pentaho User Console](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/quick-tour-of-the-pentaho-user-console-puc)
* [Get started with Interactive Reports](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/get-started-with-interactive-reports)
* [Get started with Analyzer Reports](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/get-started-with-analyzer-reports)
* [Get started with Dashboard Designer](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/get-started-with-dashboard-designer)
* [Next steps](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/next-steps-analyzer-reports-dashboard)

The [Getting started with Report Designer](https://docs.pentaho.com/pdia-try-pdia/getting-started-with-report-designer) tutorial includes step-by-step report creation instructions.

Within that tutorial, you can also view:

* [About Pentaho Report Designer](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/report-designer-merged-pages/about-pentaho-report-designer)
* [Create a report with Report Designer](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/report-designer-merged-pages/create-a-report-with-report-designer)

## Remove sample data from the Pentaho Server

By default, you have access to a sample data source and example content. When you are ready to move to development or production, remove the sample content.

To remove sample data and content:

1. Stop the Pentaho Server.
2. Delete `samples.zip` from `/pentaho-server/pentaho-solutions/system/default-content`.

   If you performed a manual WAR build and deployment, the path is `/pentaho-server/pentaho-solutions/system`.
3. Edit `/pentaho/WEB-INF/web.xml` inside the deployed `pentaho.war`.

   For archive installs, the path is usually `/pentaho-server/tomcat/webapps/pentaho/WEB-INF/web.xml`.
4. Remove the `hsqldb-databases` section:

   ```xml
   <!-- [BEGIN HSQLDB DATABASES] -->
       <context-param>
           <param-name>hsqldb-databases</param-name>
           <param-value>sampledata@../../data/hsqldb/sampledata</param-value>
       </context-param>
   <!-- [END HSQLDB DATABASES] -->
   ```
5. Remove the `hsqldb-starter` section:

   ```xml
   <!-- [BEGIN HSQLDB STARTER] --> 
   <listener> 
   <listener-class>org.pentaho.platform.web.http.context.HsqldbStartupListener</listener-class> 
   </listener> 
   <!-- [END HSQLDB STARTER] -->
   ```
6. Remove the `SystemStatusFilter`.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> This filter shows status messages useful only for development and testing.</p></div>

   ```xml
   <filter>
       <filter-name>SystemStatusFilter</filter-name>
       <filter-class>com.pentaho.ui.servlet.SystemStatusFilter</filter-class>
       <init-param>
           <param-name>initFailurePage</param-name>
           <param-value>InitFailure</param-value>
           <description>This page is displayed if the PentahoSystem fails to properly initialize.</description>
       </init-param>
   </filter>
   ```
7. Remove the filter mapping:

   ```xml
   <filter-mapping>
       <filter-name>SystemStatusFilter</filter-name>
       <url-pattern>/*</url-pattern>
   </filter-mapping>
   ```
8. Save and close `web.xml`.
9. Delete the `/pentaho-server/data/` directory.
10. Restart the Pentaho Server, then sign in to the Pentaho User Console as an administrator.

    On **Browse Files**, delete the sample folders under **Public**.

## Data Integration and Analytics components and tools

Pentaho Data Integration and Analytics includes web-based components and design tools. What you use depends on your workflow and environment.

### Data Integration and Analytics web-based components

Use the Pentaho web-based components to share business intelligence solutions by analyzing data, creating reports, and building dashboards.

These components include:

* **Pentaho User Console (PUC)**

  A design environment for accessing Analyzer, Interactive Reports, and Dashboard Designer. PUC also offers administration features for configuring your Pentaho Server.
* **Analyzer**

  Visualize data to make informed decisions. Create charts and visualizations, filter data, and configure drill-down links.
* **Interactive Reports**

  Create simple and on-demand operational reports without relying on IT.
* **Dashboard Designer**

  Create dashboards from templates, themes, and content. Combine Interactive Reports, Analyzer, and more.
* **CTools**

  A community-driven framework for creating dashboards with web technologies.

### Data Integration and Analytics design tools

Use Pentaho design tools to model, transform, and store data.

These tools include:

* **Pentaho Data Integration (PDI)**

  An ETL engine for capturing data, cleansing it, and storing it in a usable format.
* **Report Designer**

  Create pixel-perfect reports from virtually any data source.
* **Aggregation Designer**

  Create aggregate tables for OLAP cubes to improve performance.
* **Metadata Editor**

  Build metadata domains and models. Map physical database structures into a business model.
* **Schema Workbench**

  Create and edit Mondrian models.

### Evaluate Pentaho Data Integration and Analytics

Before you set up and use Pentaho Data Integration and Analytics in production, evaluate it:

1. [Install the 30-day trial of Pentaho Data Integration and Analytics](#install-the-30-day-trial-of-pentaho-data-integration-and-analytics)
2. [Learn about Analyzer, Interactive Reports, and Dashboard Designer](https://docs.pentaho.com/pdia-try-pdia/getting-started-with-analyzer-interactive-reports-and-dashboard-designer)
3. [Learn about Report Designer](https://docs.pentaho.com/pdia-try-pdia/getting-started-with-report-designer)
4. [Learn about Pentaho Data Integration and the PDI client](https://docs.pentaho.com/pdia-try-pdia/getting-started-with-pdi)
5. [Learn about Pentaho, big data, and Hadoop](https://docs.pentaho.com/pdia-try-pdia/pentaho-big-data-and-hadoop)
6. [Understand common workflows](https://docs.pentaho.com/pdia-try-pdia/about-pentaho-workflows)

### Data Integration and Analytics supported technologies

Reference material for supported components and JDBC drivers:

* [Components Reference](https://docs.pentaho.com/pdia-try-pdia/components-reference)
* [JDBC drivers reference](https://docs.pentaho.com/pdia-try-pdia/jdbc-drivers-reference)


# Getting Started with Analyzer, Interactive Reports, and Dashboard Designer

This guide covers core Pentaho Business Analytics workflows in one place.

Jump to:

* [About Pentaho business analytics tools](#about-pentaho-business-analytics-tools)
* [Quick tour of the Pentaho User Console](#quick-tour-of-the-pentaho-user-console)
* [Get started with Analyzer Reports](#get-started-with-analyzer-reports)
* [Get started with Interactive Reports](#get-started-with-interactive-reports)
* [Get started with Pentaho Reporting tools](#get-started-with-pentaho-reporting-tools)
* [Get started with Dashboard Designer](#get-started-with-dashboard-designer)
* [Next steps](#next-steps)

### About Pentaho business analytics tools

The topics found in this section give you an overview of the reports and dashboards you create with the User Console, to help you become familiar with the look and feel of the console.

The Pentaho User Console is a web-based design environment where you can analyze data, create interactive reports, dashboard reports, and build integrated dashboards to share business intelligence solutions with others in your organization and on the internet. In addition to its design features, the User Console offers a wide variety of system administration features for configuring the Pentaho Server, maintaining the Pentaho licenses, setting up security, managing report scheduling, and tailoring system performance to meet your requirements.

#### Prerequisites

Before you work with the User Console, install the Pentaho software and configure the Pentaho Server.

See [Install the 30-day trial of Pentaho Data Integration and Analytics](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/pentaho-evaluation).

#### Expertise

You do not need special skills to use the design environment.

To use system administration features, you should understand your data sources, system configuration, and security providers.

#### Tools

In the User Console, you can access the Pentaho Repository on the server and these tools:

* Analyzer
* Interactive Reports
* Dashboard Designer
* Data Source Wizard
* Data Source Model Editor

#### Sign-in credentials

Some tasks require that you [sign in to the User Console](#log-in-to-the-pentaho-user-console) with an evaluator username and password.

### Quick tour of the Pentaho User Console

If you use file management tools or any web browser, you should feel right at home with the Pentaho User Console (PUC). To familiarize yourself with the different features and options of the User Console, take a quick tour.

{% hint style="info" %}
The features and options you see depend on your role and permissions.

See the **Pentaho Business Analytics** documentation for full details.
{% endhint %}

Jump to a section:

* [Log in](#log-in-to-the-pentaho-user-console)
* [Home](#home)
* [Opened](#opened)
  * [Use Pentaho tools](#use-pentaho-tools)
* [Browse Files](#browse-files)
* [Schedules](#schedules)
* [Administration](#administration)

#### Log in to the Pentaho User Console

Follow these steps to log in to the User Console.

1. Launch a web browser.
2. Enter the URL for the Pentaho Server.

   Your IT administrator can provide the URL.
3. On the Welcome page, enter your username and password.
4. Select **Log in**.

   You can also use **Log in as an evaluator** if enabled.

![Welcome page](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-683e2620184cc5f3f8ad2ac76d6e3ca676346f71%2FPUC_Welcome_page.png?alt=media)

#### Home

After you log in, you land on the Home perspective. Use it to start most tasks.

![Home perspective](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-7c10750739d5f2f08a52dd26165a4c8af4a077c3%2FPUC_Home_page.png?alt=media)

| Item | Name                    | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | User menu               | Shows the name of the user currently logged in to the User Console. To log out or change your password, click the arrow next to your username.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 2    | **Home**                | <p>Indicates the Home perspective, which you can use to explore learning resources, create reports, dashboards and data sources, open recent files, view Help documentation, and access other User Console perspectives. Click <strong>Home</strong> and use the drop-down menu to navigate to the different perspectives:</p><ul><li>Home - Shows the Home perspective. See the <strong>Pentaho Business Analytics</strong> documentation for more information.</li><li><a href="#opened">Opened</a> - Shows your open files.</li><li><a href="#browse-files">Browse Files</a> - Helps you access, view, and manage the files and folders you need.</li><li><a href="#schedules">Schedules</a> - Shows your active scheduled reports, any block out times, and allows you to create, edit, and maintain report schedules.</li><li><a href="#administration">Administration</a> - Allows you to perform user setup, mail server configuration, revise Pentaho Server authentication settings, and view the available Pentaho licenses.</li></ul> |
| 3    | **Getting Started**     | <p>Shows resources to help you get familiar with Pentaho. Click the tabs in this section for videos, and report and dashboard examples.- The <strong>Welcome</strong> tab contains an introductory video about Pentaho products. Click the play icon to view the video.</p><ul><li>The <strong>Samples</strong> tab contains sample reports and dashboards that you can use to get familiar with the features and functionality of the User Console. Click <strong>Explore</strong> to view the samples.</li><li>The <strong>Tutorials</strong> tab contains tutorial videos that provide a visual tour of the User Console, reports, and dashboards. Click <strong>Watch the Video</strong> to view the tutorial.</li></ul>                                                                                                                                                                                                                                                                                                                     |
| 4    | **Browse Files**        | Opens the Browse Files perspective, where you can locate your files and folders, manage files, and schedule reports. Any file that you open appears in a new tab on the Opened perspective.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 5    | **Create New**          | Allows you to create new reports, dashboards, and data sources, if your user role has permissions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 6    | **Manage Data Sources** | Allows you to manage existing, and add new, data sources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 7    | **Documentation**       | Opens the [Pentaho documentation](https://docs.hitachivantara.com/) in a new window or tab.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 8    | **Recents**             | Shows a list of your most recently opened files. Click the star next to the file name to add it to Favorites.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 9    | **Favorites**           | Shows a list of your favorite files for quick access. To add a file for future access, use **Recents**, or select **Add to Favorites** in Browse Files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

#### Opened

The Opened perspective contains your open files. It appears after you open a file from **Recents**, **Favorites**, or the **Browse Files** perspective.

Select **Home** > **Opened**.

The icons and options you see depend on the file type you select. See the **Pentaho Business Analytics** documentation for more information.

![Opened perspective](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-b67c339b9762cd17f2816c9af55e2d4117cdb1ff%2FPUC_Opened.png?alt=media)

**Use Pentaho tools**

Your download includes sample reports and dashboards. It also includes the Steel Wheels sample database.

* [Interactive Reports](#get-started-with-interactive-reports) helps you create operational, tabular reports.
* [Analyzer Reports](#get-started-with-analyzer-reports) helps you explore data visually with filtering and drill-down.
* [Dashboard Designer](#get-started-with-dashboard-designer) helps you combine multiple visuals into one dashboard.

#### Browse Files

The Browse Files perspective helps you organize, find, and manage files. Your files can be local, stored in the repository, or accessed through a virtual file system (VFS) connection.

Select **Home** > **Browse Files**.

You can use this view for file management and actions like sharing and scheduling. See the **Pentaho Business Analytics** documentation for more information.

![Browse Files perspective](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-8e5cbac2ea2583eba5f11d82eb081ffde910e64a%2FPUC_Browse_Files.png?alt=media)

#### Schedules

The Schedules perspective shows your active scheduled reports.

Select **Home** > **Schedules**.

You can view recurrence patterns, last run time, next run time, and status. You can also edit schedules and create blockout times. See the **Pentaho Business Analytics** documentation for more information.

![Schedules perspective](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-d5523307297d5680b61f61567a17302dd25f03eb%2FPUC_Schedules.png?alt=media)

#### Administration

The Administration perspective is for users with the **Administer Security** permission.

Select **Home** > **Administration**.

If you do not have admin privileges, you do not see **Administration**.

Options include:

* **Users & Roles**
* **Authentication**
* **Mail Server**
* **Licenses**
* **VFS Connections**
* **Settings**
* **Email Groups**

See the **Pentaho Business Analytics** documentation for more information.

![Administration perspective](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-b75ca2af8f796898af27294875a32732ef3a5331%2FPUC_Admininstration.png?alt=media)

### Get started with Analyzer Reports

Analyzer Reports is an analytical visualization tool. It helps you filter and drill into data from Pentaho analysis data sources.

Use Analyzer when you need quick, interactive analysis. You can sort, filter, pivot, and add chart visualizations.

#### View an Analyzer report sample

This section highlights popular Analyzer capabilities. It uses the sample report **European Sales** in the **Getting Started** widget.

1. In the **Getting Started** widget on the Home page, click the **Samples** tab.
2. In the scrolling panel, scroll down and click **European Sales**, then click **Explore**.

   ![European Sales (Geo Map)](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-07ef77577a0251a4fae19fafeb532b4d5a17d576%2FssGetStartedWidgetEuroSalesGeoSample.png?alt=media)

   A new browser window opens. Click the **Samples** tab to see the report.

#### Tour the Analyzer panels

You can open an editable version of **European Sales** in Analyzer from the **Browse Files** page.

1. From the User Console Home page, click **Browse Files**.
2. In the **Browsing** pane, expand `Public`, then expand **Steel Wheels**.
3. In the center pane, double-click **European Sales**.

   ![Opened page, Analysis report](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-ef22b7e630bbbba31fdfe12527acfda3dcf1ee70%2FssgetstartedwidgetAnalyzerPanel.png?alt=media)

   The **Opened** page appears with the Analyzer report.
4. On the toolbar, click **Add More Fields** and **Rearrange Fields**.

   The **Available Fields** and **Layout** panels expand.

**Panel and toolbar basics**

* **Opened page**
  * Quick-access buttons for **Analysis Report**, **Interactive Report**, and **Dashboard**.
  * Tabs across the page for opened reports and files.
* **Available Fields** and **Layout**
  * Drag levels and measures into a report.
  * The canvas updates as you build the layout.
  * Remove a field by dragging it off the **Layout** panel.
* **Report canvas**
  * Dynamic view of your report as you build it.
  * Shown fields depend on the selected chart type.
* **Analyzer toolbar and filters**
  * Undo/redo, show or hide panels, and change settings.
  * Use the **Filters** panel to view, edit, and delete filters.

#### Create your first Analyzer report

These steps use the **Steel Wheels** sample data.

1. From the User Console Home page, click **Create New**, then select **Analysis Report**.
2. In **Select Data Source**, select **SteelWheels:SteelWheelsSales**, then click **OK**.

   A blank Analyzer report appears.
3. Build a basic pivot table:

   * Drag **Territory** to **Rows**.
   * Drag **Years** to **Columns**.
   * Drag **Sales** to **Measures**.

   ![Pivot table, Analysis Report](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-5ce42c84ad63c34082d8ebe3e19dbcf68d84203d%2FssGettingStartedAnalyzerScreen1.png?alt=media)
4. Add subtotals:

   1. Drag **Line** above **Territory** in the **Layout** column.
   2. Right-click the **Line** header, then select **Show Subtotals**.

   ![Show Subtotals, Analysis Report](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-5bf868d737da1765ec7c73892706940806e3f513%2FssGettingStartedAnalyzerScreen2.png?alt=media)
5. Add conditional formatting:
   * Right-click the first **Sales** column.
   * Select **Conditional Formatting** > **Data Bar - Green**.
6. Add a user-defined measure:

   1. Right-click the same **Sales** column.
   2. Select **User Defined Measure** > **% of Rank, Running Sum**.
   3. Select **% of Sales**, then click **Next**.

   ![Measure field creation](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-486f8c13837fbb4521a53ac0af5f848c60fe74c2%2FssGettingStartedAnalyzerDialog1.png?alt=media)
7. Refine the measure:

   * Select **Each Line Column/Row Subtotal (Subtotal is 100%)**, then click **Done**.

   ![Measure field refinement](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-e8bc66767aa22d403a919310a847a83468d0f147%2FssGettingStartedAnalyzerDialog2.png?alt=media)
8. Add a filter:

   1. Click **Show Filters** to expand the filters canvas.
   2. Drag **Territory** from **Available Fields** to the filter canvas.

   The **Filter on Territory** dialog box appears.
9. In **Filter on Territory**, select **APAC**, then click the right arrow to move it to the selected list.
10. Enable **Parameter Name**.
11. In **Parameter Name**, type `region`, then click **OK**.

![Filter on Territory dialog box](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-04c72be63f6496d0e6f2c3763e05caacefbea0f3%2FssGettingStartedAnalyzerDialog3.png?alt=media)

The report updates and shows APAC sales data. 12. Resize columns as needed for readability.

![Sales data, Analysis report](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-51768e5e0849ded0c7db6276f0c0e39013dac3af%2FssGettingStartedAnalyzerScreen3.png?alt=media) 13. Save the report:

1. Click **Save As**.
2. Save the report as `Territory - Sales` in your user folder.

You have created a simple Analyzer report from scratch. For deeper Analyzer workflows, see [About Pentaho business analytics tools](#about-pentaho-business-analytics-tools).

### Get started with Interactive Reports

Interactive Reports is a web-based design interface which is used to create both simple and on-demand operational reports without depending on IT or report developers. Use Interactive Reports if you want to create a quick report that answers an immediate business question, looks professional, and provides significant control over formatting elements such as fonts, column width or sorting, background colors, and more.

Jump to:

* [View an Interactive report sample](#view-an-interactive-report-sample)
* [Tour the Interactive panels](#tour-the-interactive-panels)
* [Create your first Interactive report](#create-your-first-interactive-report)

#### View an Interactive report sample

This section highlights some popular Interactive Reports capabilities that are available, using the sample report called Vendor Sales Report, located in the **Getting Started** widget.

1. In the **Getting Started** widget on the Home page, click the **Samples** tab.

   ![Home page](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-ab458750968240ded31b3ccf7b6248bc2b88f1ef%2FPIR_Tutorial_01_Tab_Samples_Select_Vendor_Sales_w596.png?alt=media)
2. Click **Vendor Sales** from the scrolling panel on the right.
3. Click **Explore** in the **Samples** pane.

   A new window opens showing the Vendor Sales sample report.

   ![Vendor Sales Report](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-615fa8bc29056259d23a1896904542c1233f7a0e%2FPIR_Tutorial_02_Tab_Samples_Select_Vendor_Sales_Report_Open_w555.png?alt=media)

#### Tour the Interactive panels

By going to the Browse Files page in the User Console, you can also view an editable version of the Vendor Sales report.

1. Switch to the Browse Files page in the User Console.
2. In the **Folders** pane, click to expand the **Public** folder, then click to highlight the `Steel Wheels` folder.
3. In the **Files** pane, click **Vendor Sales**, then click **Edit** in **File Actions**.

   The Opened page appears with the interactive report and toolbars active.

   ![Opened page](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-98ca399a4612e36559ce7bbfe92943020bd50689%2FPIR_Tutorial_03_Vendor_Sales_Edit_Report_Hitachi_Red_Numbers_w555.png?alt=media)

Key areas on the page:

1. **Opened page**\
   Provides quick access buttons across the top to create and save a new **Analysis Report**, **Interactive Report**, and **Dashboard**. Opened reports and files show as a series of tabs across the page.
2. **Data**, **Formatting**, and **General** panels\
   Use the **Data** panel to drag information into a column or a row on the report. Your report updates as you drag items onto the report canvas. Use **Find** to search for a specific field. Delete a field by dragging it from the layout area to the trash can that appears in the lower right corner of the report canvas.

   Use the **Formatting** panel to change font size and type.

   Use the **General** panel to set preferences, select a paper size for printing, and select templates for your report.
3. **Report canvas**\
   Shows a dynamic view of your report as you build it. The look of your report changes as you use the **Data**, **Formatting**, and **General** panels.
4. **Interactive toolbar and filters**\
   Use the toolbar to undo and redo actions, hide lists of fields, add or hide filters, disable auto-refresh, adjust settings, change the report view, and limit the number of rows queried. Use the **Filters** panel to view, edit, and delete filters for the active report.

#### Create your first Interactive report

The instructions below guide you through the creation of your first Interactive report using the Steel Wheels sample data.

1. From the Home page, click **Create New**, then choose **Interactive Report**.

   ![Home page, Interactive Report](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-0b7c1024cca2129b33ab85e42d2f96d3ed406115%2FPIR_Tutorial_04_Home_Create_Interactive_Report_w565.png?alt=media)
2. Choose the **Inventory** data source from the **Select Data Source** dialog box. Click **OK**.

   ![Select Data Source dialog box](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-652cb3b7a25e5c2ced683f20ec52958af35d2007%2FPIR_Tutorial_05_Select_Data_Source_w365.png?alt=media)
3. Click **Get Started** on the dialog box that appears.

   A blank Interactive report canvas appears.
4. Click and drag the **Product Code** element onto the report canvas until a highlighted vertical line appears. Drop it onto the report canvas.

   ![Click and drag item to canvas](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-6a89473abc32594fd7f05cd584102c7abe5884eb%2FPIR_Tutorial_06_Drag_Product_Code_w555.png?alt=media)
5. Continue dragging and dropping these fields onto the canvas: **Product Name**, **Product Vendor**, **Quantity in Stock**, **MSRP**, and **Buy Price**.

   ![Report fields](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-1091d498d0201ca83747dd6634050eff2eefd36f%2FPIR_Tutorial_07_Drag_Fields_Canvas_w562.png?alt=media)

   The data from the chosen fields appears on the report canvas and populates with the information from the server.

   **Note:** You can change the order of the columns by clicking the column headings and dragging them left or right. If you want to delete a column, drag the column title to the trash can.
6. Rename your report by double-clicking **Untitled** in the report canvas and typing a name in the field that appears. `In Stock Report` is used in this example.

   ![Renaming the report](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-4889d0928f75fd5ee1613cd40d80370864c521f6%2FPIR_Tutorial_08_Rename_report_w311.png?alt=media)
7. After you have arranged your columns, apply a filter to the data. Click the **Filter** icon in the toolbar. After the **Filter** pane expands, drag the **Product Code** field onto the filter workspace.

   ![Applying a filter](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-0938602e32f96ffae23eb2eea1c01885f9348341%2FPIR_Tutorial_09_Drag_Product_Code_into_Filters_w580.png?alt=media)
8. In the **Filter on** dialog box, click **Select from a list**.

   ![Selecting filter values](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-3c7b00925b4b63eb8e10db061d706973524ea915%2FPIR_Tutorial_10_Filter_on_Product_Code_Dialog_w530.png?alt=media)
9. Choose items from the filter list using one of these methods. Click the arrows to move your selected filters on or off the filter list.
   * To choose more than one item, hold down Ctrl and click the items. Then click the top arrow to move them to the right panel.
   * To choose a range, hold down Shift. Then click the first and last item.
   * To choose a single item, click it. Then click the top arrow to move it to the right panel.
10. Click **OK**, then click **Save As** on the toolbar.
    1. In the **Save As** dialog box, save your report using the title you used in Step 6. `In Stock Report` is used in this example.
    2. Choose your user folder as the location. Remember the folder and report title. You use the report in a later tutorial. Click **Save**.
11. If you want to export the report, click the **Export** icon on the toolbar and choose a format from the dropdown list.

    ![Report export selection](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-8fcfbded60db6626a176bfc66add5afcd0c983da%2FPIR_Tutorial_11_Export_w580.png?alt=media)

    The report exports in the selected format. You can print a paper copy from the export.

    ![Exported report example](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-2d8796e0967273cd4e028405a3b884341bd623d2%2FPIR_Tutorial_12_HTML_Report_w550.png?alt=media)

You have successfully created a simple Interactive report from scratch. See **Pentaho Business Analytics** for details on how to work with more complex interactive reports.

### Get started with Pentaho Reporting tools

After you define the data sources for your Pentaho Server, you are ready to begin working with the Pentaho User Console to create your first reports. Each section below uses sample data sources that are included with the installation.

Use these sections in order:

* [Quick tour of the Pentaho User Console](#quick-tour-of-the-pentaho-user-console)
* [Get started with Interactive Reports](#get-started-with-interactive-reports)
* [Get started with Analyzer Reports](#get-started-with-analyzer-reports)
* [Get started with Dashboard Designer](#get-started-with-dashboard-designer)
* [Next steps](#next-steps)

### Get started with Dashboard Designer

Dashboard Designer lets you build dashboards with minimal training. A dashboard combines several reports in one view. Use it to monitor multiple reports at once, keep quick links to pages you use often, and view charts while you work.

In this topic:

* [View a dashboard sample](#view-a-dashboard-sample)
* [Tour the Dashboard panels](#tour-the-dashboard-panels)
* [Create your first dashboard](#create-your-first-dashboard)

#### View a dashboard sample

This section highlights popular Dashboard Designer capabilities, using the sample dashboard **Sales Performance (Dashboard)** in the **Getting Started** widget.

1. In the **Getting Started** widget on the Home page, click the **Samples** tab.
2. Scroll down to **Sales Performance (Dashboard)**.
3. Click **Explore** to open a new browser window, then click the **Samples** tab.
4. Scroll right in the horizontal list at the bottom.
5. Click **Sales Performance (Dashboard)**.

![Dashboard sample](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-ba47b1cc29009b8b0cb345d53cda2eaa2b699065%2FssDashboardSampleNew.png?alt=media)

#### Tour the Dashboard panels

You can open the editable version of **Sales Performance (Dashboard)** in Dashboard Designer from **Browse Files**.

1. In the **Folders** pane, expand `Public`, then select `Steel Wheels`.
2. In the center pane, double-click **Sales Performance (Dashboard)**.
3. After the dashboard opens, in **File Actions**, click **Edit**.

![Dashboard example](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-f0a3aee1fe810d298093853260cbc3d7e9f7d8d5%2FssDashboardSampleEditPanels.png?alt=media)

| Item | Name                           | Function                                                                                                                                                                                                           |
| ---- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | **Opened** page                | Provides quick access buttons across the top to create and save a new **Analysis Report**, **Interactive Report**, and **Dashboard**. Opened reports and files show as a series of tabs across the page.           |
| 2    | Prompts panel                  | The prompts panel gives you a way to add filters to the individual parts of your dashboard.                                                                                                                        |
| 3    | **Browse** and **Files** panel | Locate your files using the **Browse** and **Files** panels, and add them to dashboards.                                                                                                                           |
| 4    | Dashboard canvas               | Shows a dynamic view of your dashboard as you work to build it. The look of your dashboard refreshes as you add content from the **Browse** and **Files** panels, and work with the prompts or **Objects** panels. |
| 5    | **Objects** panel              | Refine the look of your dashboard with the **Objects** panel by choosing a dashboard template or changing the titles for each object in the dashboard.                                                             |

#### Create your first dashboard

1. From the User Console Home page, click **Create New**, then select **Dashboard**.
2. In the **Edit** pane, click the **Templates** tab, then select **2 over 1**.
3. In the **Edit** pane, click the **Properties** tab, then enter `My Dashboard` in **Page Title**.

   This is the title for your dashboard page.

   ![Properties tab, Dashboard](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-37cfc658332b92fa18006128f8aeb523e5c211bc%2FssGettingStartedDashboardScreen1.png?alt=media)
4. Click the **Themes** tab, then select a theme.

   The new theme applies immediately.
5. In the **Browse** pane, open the folder you used earlier.
6. From the **Files** pane, drag `Territory - Sales` onto the top-left dashboard panel.

   ![Drag and drop into dashboard](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-c12e21c7d9d29c94cf7046af44efcb76a4e0741f%2FssGettingStartedDashboardScreen2.png?alt=media)
7. In the **Edit** pane, enter `Territory - Sales` in **Title**, then click **Apply**.

   The panel populates with the **Territory - Sales** report.
8. Locate your Interactive report in the **Browse** pane.
9. Drag `In Stock Report` onto the top-right dashboard panel.
10. In the **Edit** pane, enter `In Stock Report` in **Title**, then click **Apply**.

    The panel populates with the **In Stock Report**.
11. Drag any report from `Public/Steel Wheels` into the bottom dashboard panel.
12. Enter a title for the bottom panel, then click **Apply**.
13. In the toolbar, click **Save As**.
14. Save the dashboard as `My Dashboard`, then click **Save**.
15. Close the dashboard (click **X** on its tab).
16. Go to **Browse Files**, then double-click `My Dashboard` in the **Files** pane.

![Created dashboard](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-810f8c294ed3edc061304288a2919e1c57977a1d%2FssGettingStartedDashboardScreen3.png?alt=media)

You created a simple dashboard. See **Pentaho Business Analytics** for details on complex dashboards.

### Next steps

After you have finished working through the walk-through tutorials, you are ready to learn more about Pentaho reporting with the following documents:

* **Pentaho Business Analytics**
* **Pentaho Report Designer**


# Getting started with Report Designer

Use this topic to create and refine a sample report in Report Designer.

You use Pentaho’s sample database in these steps. Sample data is installed by default with Report Designer.

### In this topic

* [About Pentaho Report Designer](#about-pentaho-report-designer)
* [Create a report with Report Designer](#create-a-report-with-report-designer)
* [Design your report](#design-your-report)
* [Refine your report](#refine-your-report)
* [Row banding, data formatting, and alignment](#row-banding-data-formatting-and-alignment)
* [Add a chart to your report](#add-a-chart-to-your-report)
* [Add parameters to your report](#add-parameters-to-your-report)
* [Publish your report](#publish-your-report)

### About Pentaho Report Designer

Pentaho Report Designer is a report creation tool. You can use it standalone or as part of the Pentaho Business Analytics suite.

It helps you build detailed reports from prepared data. You can connect to most data sources.

### Create a report with Report Designer

Perform the steps below to create a report using Report Designer.

1. Start Report Designer. Go to **Start** > **Programs** > **Pentaho Enterprise Edition** > **Design Tools** > **Report Designer**.

   The Report Designer home page appears.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To change the zoom level, drag the percentage in the upper-left corner. Double-click it to reset to 100%.</p></div>
2. Click **New Report** in the Welcome dialog box.

   The design workspace appears.
3. In the right pane, click the **Data** tab.
4. Right-click **Data Sets** and select **JDBC**.

   You can also click the yellow database icon.
5. Under **Connections**, select **SampleData (Hypersonic)**.
6. Next to **Available Queries**, click the plus sign to add queries.

   ![JDBC Data Source dialog box](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-d1b71a60a45872623318eae4c21443ed12525d93%2FssPRDJDBCDataSource.png?alt=media)

   Query 1 appears under **Available Queries**.
7. Click the edit icon (![Edit](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-155f015433752130f7340b11ca96303843194c36%2Fedit.png?alt=media)).

   The SQL Query Designer window opens.
8. Select **PUBLIC** in the **schema filter** menu. Double-click **ORDERFACT** so the table appears in the workspace.

   ![SQL Query Designer](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-9af15ced36e9b4649dee2049f32cb76e14071cd3%2FssPRDSQLQueryDesigner%20-%20SchemaFilter.png?alt=media)
9. In the SQL Query Designer workspace, right-click **ORDERFACT** and select **deselect all**.

   ![Clear all, SQL Query Designer](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-d6c90f5ce3d3daf14f1245dffecec90b249b5d09%2FssPRDSQLQueryDesigner%20-%20DeselectAll.png?alt=media)
10. Select the **ORDERNUMBER**, **QUANTITYORDERED**, **PRICEEACH**, and **ORDERDATE** fields.

    ![Orderfact fields](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-1a3668091f81d8b4993261a5f04d8b49a4e6fe83%2FssPRDSQLQueryDesigner%20-%20ORDERFACTFields.png?alt=media)
11. Double-click **PRODUCTS** so the table also appears in the workspace.

    Notice the line joining the **ORDERFACT** and **PRODUCTS** tables.
12. Clear all **PRODUCTS** fields. Then select **PRODUCTNAME** and **PRODUCTLINE**.

    ![Products table](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-dfdfc6cbdcc770069b9a78245a0f4dc0c0f8e19d%2FssPRDSQLQueryDesigner%20-%20PRODUCTSTable.png?alt=media)
13. Click the **Syntax** tab to view the SQL statement.

    Notice that **PRODUCTCODE** joins the tables.

    ![Syntax tab](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-b0407375a7ef9d0ee3c8d72ee5adab1f2d89b389%2FssPRDSQLQueryDesigner_-_SyntaxTab.png?alt=media)
14. Click **OK** to return to the JDBC Data Source dialog box.

    The SQL statement appears under **Query**.
15. Click **OK** in the JDBC Data Source dialog box.

    ![Query 1 fields](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-18a9f13c177be7630d806abd6826de28f394a737%2FssPRDDataTabShowingQuery1.png?alt=media)

    The fields now appear under **Query 1**.

Next: [Design your report](#design-your-report).

### Design your report

This exercise walks you through designing your report layout.

1. Under **View**, select **Element Alignment Hints** and **Snap to Elements**.

   These options help align elements.
2. Under **Query 1**, drag **ORDERNUMBER** into the **Details** band.
3. Add **ORDERDATE**, **PRODUCTNAME**, **QUANTITYORDERED**, and **PRICEEACH** to the **Details** band.

   Do not overlap fields.
4. Resize **PRODUCTNAME** larger. Resize **QUANTITYORDERED** smaller.

   ![Resizing](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-ef7dbe13d8c74d2d78eaa1723da9e37d871050ab%2Frd_13.png?alt=media)
5. Click **Preview** (![Preview](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-501ad0aec8b3fa954777888b04e2d17b735c10ce%2Fpreview_eye.png?alt=media)).

   ![Report preview](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-2a431a25ca123bb2f7ec505355acab4e5189550a%2FssPRDInitialReportDesign.png?alt=media)
6. Click **Edit** (![Edit](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-155f015433752130f7340b11ca96303843194c36%2Fedit.png?alt=media)) to return to the workspace.

Next: [Refine your report](#refine-your-report).

### Refine your report

You created a report in the previous exercise. Now add labels, headers, and row banding.

1. Drag a label (![Label](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-f952ae1a87a67130c08d8d6e5df5c2a409833d04%2Frd_35.png?alt=media)) to the **Page Header** band.

   The **Structure** tab updates.

   ![Structure tab](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-03721f7235725c36663164292add6ca4e6ad0eeb%2Frd_15.png?alt=media)
2. Click inside the label and type `Order Report`.
3. Select the label text. Set the font size to 18. Apply bold.

   ![Font resizing](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-5165a7f7928326eca83f5f7bee7843205045fe06%2Frd_16.png?alt=media)
4. With the label selected, set a font color.

   The page header appears on every page.
5. Create column headers. Click **Details Header** under the **Structure** tab.

   The **Style** and **Attributes** tabs appear.
6. Under **common** in **Attributes**, set **hide-on-canvas** to **False**.

   The **Details Header** band appears.
7. Click the **Select Objects** icon (![Select objects](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-75d16c81c01f61ce83aebfef6cf3d9ea0578702a%2Fselect_objects_icon.png?alt=media)).
8. Select all column objects in the **Details** pane.

   ![Selected objects](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-003a0d129a45ba7019aa51b6b43795badd424b69%2Fselect_objects.png?alt=media)
9. Press Ctrl+C to copy. Press Ctrl+V to paste into the **Details Header** pane.
10. Select **Format** > **Morph** > **label**.

    The objects change to labels.
11. Type the header labels: `Order No.`, `Order Date`, `Product Name`, `Quan.`, and `Price Each`.
12. Click **Preview** (![Preview](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-501ad0aec8b3fa954777888b04e2d17b735c10ce%2Fpreview_eye.png?alt=media)).

    ![Report example](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-688d663e1122f8b16d656853748ff3d7b4c2d197%2FssPRDReportWithHeadingLabels.png?alt=media)
13. Select **Format** > **Row Banding**.
14. In the Row Banding dialog box, select **Yellow** for **Visible Color**. Click **OK**.
15. Click **Preview**.

    ![Report with row banding](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-4201c67cb9c92ebe1721386fe571bc6fd13523ac%2FssPRDReportWithRowBanding.png?alt=media)
16. Select **File** > **Save**. Save to `.../report-designer/samples`. Use `Orders` as the file name.

Next: [Row banding, data formatting, and alignment](#row-banding-data-formatting-and-alignment).

### Row banding, data formatting, and alignment

#### Row banding

Create a row band element to control which fields show banding. You can name the row band element anything.

In this example, the row band element is named **row-band-element**.

![Row Banding dialog box](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-aa798a428b075c114bfb6e372b783e9fa4ebc66f%2FssPrdRowBand.png?alt=media)

After you create the element, select the fields to band. In **Attributes**, type `row-band-element` in the **name** field.

![Name field, Attributes](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-0afa73f11ea2a7dde92d3d4ce84cde0105c4e40b%2FssPrdAllColumnsSelected.png?alt=media)

#### Data formatting

Report Designer uses default formats for dates and numbers. You can change formats under **Attributes**.

Select a field. Then select a value for **format**.

In this example, **Order Date** uses `MM-dd-yy`.

![Format field, Attributes](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-6e8c48dcfb730211d7738bb2bc6cf66b9484efcb%2FssPrdDataFormat.png?alt=media)

Preview the report to confirm the results.

![Order Date formatting applied](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-11377ab81449d287a4a5689807471bf06360f431%2FssPrdOrderDateClean.png?alt=media)

{% hint style="info" %}
You can also type a custom format string. Use the JavaScript date and number format syntax.
{% endhint %}

#### Alignment

To align multiple objects, select them first. Then choose an alignment option under **Format**.

To multi-select, press Shift and click each object. You can also use **Select Objects** (![Select Objects](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-75d16c81c01f61ce83aebfef6cf3d9ea0578702a%2Fselect_objects_icon.png?alt=media)) and drag to select.

![Alignment selection, Format menu](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-c48a77edb7a039f2077e95f2d4be57479d171f07%2FssPrdAlignHeaders.png?alt=media)

Next: [Add a chart to your report](#add-a-chart-to-your-report).

### Add a chart to your report

In this exercise, you add a chart to your report.

1. Select **File** > **Open**. Open the report you saved earlier.
2. In the **Palette**, drag a Chart icon (![Chart](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-38ee5d74b5834c1c460abd2aed454513dc9fac8c%2Frd_chart.png?alt=media)) into the **Report Footer** band.
3. Resize and center the chart.

   ![Chart resizing handles](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-5152344111a904ce3c66e136031d958befbb9146%2Frd_24.png?alt=media)
4. Double-click the sample chart.
5. Select the **pie chart** icon.

   Chart properties are listed on the left. Data properties are listed on the right.
6. Under **Title**, set **chart-title** to `Product Pie Chart`.
7. Under **Common** in **Primary DataSource**, set **value-column**. Click the ellipsis to open the Select Field dialog box.
8. Select **QUANTITYORDERED** and click **OK**.
9. Under **Series**, click the ellipsis next to **series-by-field**.

   The Edit Array dialog box opens.
10. Click the **Add** icon (![Add](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-5fda46e3255983f47487ad27f06e7f8a20ee00ad%2Fadd.png?alt=media)).
11. Select **PRODUCTLINE** and click **OK**.
12. Click **OK** to close the Edit Chart dialog box.
13. Click **Preview** (![Preview](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-501ad0aec8b3fa954777888b04e2d17b735c10ce%2Fpreview_eye.png?alt=media)).
14. Scroll to the last page.

    ![Displayed report](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-0abdff8b62ff222c4923cb44cabc9ab80c9999c1%2Frd_27.png?alt=media)
15. Save your report.

{% hint style="info" %}
To use a bar or line chart, change the chart type. Add **series-by-value** entries for `SALES` and `COST`.
{% endhint %}

Next: [Add parameters to your report](#add-parameters-to-your-report).

### Add parameters to your report

Now make your report interactive by setting parameters. Users get prompted for values when they run the report.

1. In Report Designer, open your Orders report.
2. Select **Data** > **Add Parameter**.

   You can also select **Master Report Parameter** (![Master report parameter](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-cc7624a3679de5abfb1daa93eed0f47f90e041eb%2Frd_add_parameter.png?alt=media)) under the **Data** tab.

   The Add Parameter dialog box appears.
3. In **Name**, enter `enter_prodline`.
4. In **Label**, enter `Select Line`.
5. For **Display Type**, select **Drop Down**.
6. Under **DataSources**, select **JDBC (SampleData (Hypersonic)**. Click the **Edit** icon (![Edit](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-155f015433752130f7340b11ca96303843194c36%2Fedit.png?alt=media)).

   The JDBC Data Source dialog box appears.
7. Under **Connections**, select **SampleData (Memory)**.
8. Next to **Available Queries**, click **Add** (![Add](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-5fda46e3255983f47487ad27f06e7f8a20ee00ad%2Fadd.png?alt=media)).

   Query 2 is added.
9. In **Query Name**, enter `prodlineList`.
10. In **Query**, enter the following SQL:

    ```sql
    SELECT DISTINCT
         "PRODUCTS"."PRODUCTLINE"
    FROM
         "PRODUCTS"
    ```

    You can also build the query in SQL Query Designer.
11. Click **OK** to close the Data Source dialog box.
12. In the Add Parameter dialog box, under **DataSources**, select **prodlineList**.
13. For **Value Type**, select **String**.
14. Optional: Set a default value, such as `Motorcycles`.

    ![Add Parameter dialog box](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-d8b51d365198804d3db91167781b4243703f8294%2FssPRDAddParameter.png?alt=media)
15. Click **OK** to close the Add Parameter dialog box.
16. Map the parameter back to Query 1. Under **Data**, double-click **Query 1**.
17. Click the **Edit** icon (![Edit](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-155f015433752130f7340b11ca96303843194c36%2Fedit.png?alt=media)) to open SQL Query Designer. Right-click **PRODUCTLINE** and select **add where condition**.
18. In the condition editor, enter `${enter_prodline}`. Click **OK**.

    ![Condition.edit dialog box](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-95cd10972f49d0c02ebf3211a7f9601ca6e840b4%2Frd_condition_edit.png?alt=media)
19. Click **OK** to close SQL Query Designer.
20. Click **OK** to close the Data Source dialog box.
21. Click **Preview**.

    ![Product line menu](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-07962c842428094e839a87810bf5d8005ff2b1b2%2FssPRDProductLineParameterInReport.png?alt=media)
22. Save and close the report.

Next: [Publish your report](#publish-your-report).

### Publish your report

Now publish the report to a Pentaho server.

1. In Report Designer, open the report you created.
2. Select **File** > **Publish**.

   You can also select **Publishes the report on a Pentaho server** (![Publish](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-39fd703669f0982b5f50c4b42c17c35e20f5d300%2Frd_publish.png?alt=media)).
3. In the Login dialog box, confirm the server URL is `http://localhost:8080/pentaho/`.

   ![Login dialog box](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-1b90efe4ae3bad75b38eb8ff08bc12e26e29de8b%2FssPRDServerLogin.png?alt=media)
4. Click **OK**.

   The Publish to Server dialog box appears.
5. Enter a report title and description.
6. Under **Location**, save to `...public/Steel Wheels`.
7. Set **Output Type** to **html** and click **OK**.

   A success message appears.
8. Click **Yes** to open the User Console and view the report.

   To view it later, go to `http://localhost:8080/pentaho/`. Then browse to the `Reporting Examples` directory.
9. Log in as `Admin`.

   The default password is `password`.
10. Select a product line parameter value. Keep the default **Output Type**.

Your report is now available to users.


# Getting Started with PDI

If you are new to Pentaho Data Integration, start here.

Use these tutorials to build your first transformations and jobs in Spoon.

### In this topic

* [Pentaho Data Integration (PDI) tutorial](#pentaho-data-integration-pdi-tutorial)
* [PDI job tutorial](#pdi-job-tutorial)
* [Getting started with PDI and Hadoop](#getting-started-with-pdi-and-hadoop)

### Pentaho Data Integration (PDI) tutorial

The following tutorial is intended for users who are new to the Pentaho suite or who are evaluating Pentaho as a data integration and business analysis solution. The tutorial consists of six basic steps, demonstrating how to build a data integration transformation and a job using the features and tools provided by Pentaho Data Integration (PDI).

The Data Integration perspective of PDI allows you to create two basic file types: transformations and jobs. Transformations describe the data flows for ETL such as reading from a source, transforming data and loading it into a target location. Jobs coordinate ETL activities such as defining the flow and dependencies for what order transformations should be run, or prepare for execution by checking conditions such as, "Is my source file available?" or "Does a table exist in my database?"

The aim of this tutorial is to walk you through the basic concepts and processes involved in building a transformation with PDI in a typical business scenario. In this scenario, you are loading a flat file (CSV) of sales data into a database to generate mailing lists. Several of the customer records are missing postal codes that must be resolved before loading into the database. In the preview feature of PDI, you will use a combination of steps to cleanse, format, standardize, and categorize the sample data. The six basic steps are:

1. Step 1: Extract and load data
2. Step 2: Filter for missing codes
3. Step 3: Resolve missing data
4. Step 4: Clean the data
5. Step 5: Run the transformation
6. Step 6: Orchestrate with jobs

#### Prerequisites

To complete this tutorial, you need the following items:

* An installed version of the [Pentaho 30-day trial](https://www.hitachivantara.com/en-us/products/data-management-analytics/pentaho-platform/pentaho-data-integration/pentaho-trial-download.html).

#### Step 1: Extract and load data

In Step 1, you will retrieve data from a CSV flat file and use the Text File Input step to connect to a repository, view the file schema, and retrieve the data contents.

**Create a new transformation**

Follow these steps to create a new transformation.

If you want to insert a variable into a field that accepts variables, you can put your cursor in the fields and press **CTRL+Spacebar** to see a list of variables to insert. Fields that accept variables have a blue diamond.

1. Select **File** > **New** > **Transformation** in the upper-left corner of the PDI window.

   ![](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-2b2a8afe8c01bfdff955fc6c660fb69cf4e54917%2FDesign%20list%20with%20metatdata%20discovery.png?alt=media)
2. Under the **Design** tab, expand the **Input** node, then select and drag a Text File Input step onto the canvas.
3. Double-click the Text File input step. In the Text file input window, you can set the properties of the step.

   ![Text File Input File tab](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-7dcb73e05215aedada34b2cddb2af13df065de3a%2Fpdi_tutorial_text_file_input_step_w532.png?alt=media)
4. In the **Step Name** field, type `Read Sales Data`.

   The Text file input step is now renamed to Read Sales Data.
5. Click **Browse** to locate the `sales_data.csv` source file in the `...\design-tools\data-integration\samples\transformations\files` folder. The **Browse** button appears in the upper-right side of the window near the **File or Directory** field.
6. Change **File type** to `*.csv`. Select `sales_data.csv`, then click **OK**​.

   The path to the source file appears in the **File or directory** field.
7. Click **Add**.

   The path to the file appears under **Selected Files**.

**View the content in the sample file**

Follow these steps to look at the contents of the sample file.

1. Click the **Content** tab, then set the **Format** field to **Unix**​.
2. Click the **File** tab again and click the **Show file content** in the lower section of the window.
3. The Number of lines (0-all lines) window appears. Click **OK** to accept the default.
4. The Content of first file window shows the file. Examine the file to see how that input file is delimited, what enclosure character is used, and whether or not a header row is present.

   In the sample, the input file is comma delimited, using the enclosure character of a quotation mark ("). It contains a single header row containing field names.
5. Click the **Close** button to close the window.

**Edit and save the transformation**

Follow these steps to provide information about the data's content.

1. Click the **Content** tab. Use the fields under the **Content** tab to define how your data is formatted.
2. Verify that the **Separator** is set to comma (,) and that the **Enclosure** is set to quotation mark ("). Select **Header** and enter `1` in the **Number of header lines** field.

   ![Text File Input Content tab](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-3d044838f0a501a3bff891adeb4ff4451f4f6241%2Fpdi_tutorial_Text_File_Input_content_tab_w532.png?alt=media)
3. Click the **Fields** tab and click **Get Fields** to retrieve the input fields from your source file. When the Number of lines to sample window appears, enter `0` in the field, then click **OK**.
4. If the Scan Result window displays, click **Close** to close the window.

   ![Text File Input Fields tab](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-e7f38a3758b4da24d24d7c7c6b2e00799900af93%2Fpdi_tutorial_Text_File_Input_scan_results_w532.png?alt=media)
5. To verify that the data is read correctly, click the **Content** tab, then click **Preview Rows**.
6. In the Enter the number of rows you would like to preview window, click **OK** to accept the default.

   The Examine preview data window appears.
7. Review the data. Do you notice any missing, incomplete, or variations of the data?
   * `STATE & POSTALCODE` both contain `<null>`
   * `COUNTRY` contains both `USA` and `United States`.
8. Click **OK** to save the information that you entered in the step.
9. Enter a name for the transformation and provide additional properties using the Transformation Properties window. There are multiple ways to open the Transformation Properties window.
   * Right-click any empty space on the canvas and select **Properties**.
   * Double-click any empty space on the canvas to select **Properties**.
   * Enter the CTRL-T keyboard combination.
10. In the **Transformation Name** field, enter `Getting Started Transformation`.

    Below the name, the filename is empty.
11. Click **OK** to close the Transformation Properties window.
12. To save the transformation, select **File** > **Save**.

    When saving your transformation for the first time, you are prompted for a file location and name of your choice. The file extension `.ktr` is the usual file extension for transformations.

**Load data into a relational database**

Now you are ready to take all the records that are exiting the Filter Rows step (added in Step 2) where the **POSTALCODE** was not null (the **true** condition) and load them into a database table. You will use the Table Output step and a hop from the Text File Input step to direct the data stream into a database table. This section of the tutorial uses a pre-existing database established during the Pentaho installation, which is started along with the server.

**Create the Table Output step**

Follow these instructions to create the Table Output step.

1. Under the **Design** tab, expand the contents of the **Output** node.
2. Click and drag a Table Output step into your transformation.
3. Create a hop between the Read Sales Data and Table Output steps. To create the hop:
   1. Press the SHIFT key.
   2. Click the Read Sales Data (Text File Input) step and drag the mouse to draw a line to the Table Output step.
   3. Release the SHIFT key.
   4. Click the Table Output step.
4. Double-click the Table Output step to open its **Edit properties** dialog box.
5. Rename your Table Output step to Write to Database.

**Create a connection to the database**

Follow these steps to create a connection to the database.

1. Click **New** next to the **Connection** field. You must create a connection to the database.

   The Database Connection window appears.
2. Provide the settings for connecting to the database.

   | Field               | Setting                                                                              |
   | ------------------- | ------------------------------------------------------------------------------------ |
   | **Connection Name** | Sample Data                                                                          |
   | **Connection Type** | Hypersonic                                                                           |
   | **Host Name**       | localhost                                                                            |
   | **Database Name**   | sampledata                                                                           |
   | **Port Number**     | 9001                                                                                 |
   | **User Name**       | pentaho\_admin                                                                       |
   | **Password**        | password (If `password` does not work, please check with your system administrator.) |
3. Click **Test** to verify your entries are correct. A success message appears. Click **OK**.

   **Note:** If you get an error when testing your connection, ensure that you have provided the correct settings information as described in the table and that the sample database is running. Depending on your platform, see [Start and stop the Pentaho Server for configuration on Windows](https://github.com/pentaho/documentation/blob/main/PDIA/11.0/Get%20Started/Pentaho%20evaluation/Start%20and%20stop%20the%20Pentaho%20Server%20for%20configuration%20on%20Windows=GUID-2DF3CCF0-39D7-4BC4-8129-AE3C6A3FBD60=1=en=.md) or [Start and stop the Pentaho Server for configuration on Linux](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages-do-not-use/install-trial-legacy-child-pages/start-and-stop-the-pentaho-server-for-configuration-on-linux).
4. Click **OK** to exit the Database Connections window.

**Define the Data Definition Language (DDL)**

DDLs are the SQL commands that define the different structures in a database such as `CREATE TABLE`. Fortunately, Pentaho can help you create the necessary DDL.

1. Enter `SALES_DATA` in the **Target Table** text field.
2. This table does not exist in the target database, so Pentaho can generate the DDL to create the table and execute it. In this scenario, the DDL is based on the stream of data coming from the previous step, which is the Read Sales Data step.
3. In the Table Output window, select the **Truncate Table** property.

   ![Table Output step Truncate table field](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-bbf4ec48bbf8594dffc1d93b8b8acef29c2b849c%2Fpdi_tutorial_table_output_truncate_table_property_532.png?alt=media)
4. Click the **SQL** button in the bottom of the Table output dialog box to generate the DDL for creating your target table.
5. The Simple SQL editor window appears with the SQL statements needed to create the table.

   ![Simple SQL editor](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-7e278b742b5d6a35af4ddf0197609dcf0613cc11%2Fpdi_tutorial_simple_sql_editor_w395.png?alt=media)
6. Click **Execute** to execute the SQL statement.

   The Results of the SQL statements window appears.
7. Examine the results, then click **OK** to close the Results of the SQL statements window.
8. Click **Close** in the Simple SQL editor window
9. Click **OK** to close the Table output window.
10. Save your transformation.

#### Step 2: Filter for missing codes

After completing Step 1: Extract and load data, you are ready to add a transformation component to your data pipeline. The source file contains several records that are missing postal codes. This section of the tutorial filters out those records that have missing postal codes, where the POSTALCODE is not null (the true condition), and ensures that only complete records are loaded into the database table.

**Preview the rows read by the input step**

Follow these steps to preview the rows read by the input step.

1. Right-click the Read Sales Data step and select **Preview**.

   ![Transformation Menu showing how to access Preview](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-093ee170a56a7addec5c96f105454723e81f15a4%2Fpdi_tutorial_new_transformation_how_to_access_preview_w499.png?alt=media)
2. Specify the number of rows to preview. Optionally, you can configure breakpoints which pause execution based on a defined condition, such as a field having a specific value or exceeding a threshold.
3. Click the **Quick Launch** button. Preview the data and notice that several of the input rows are missing values for the **POSTALCODE** field.

   ![Preview showing missing postalcode fields](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-e780416b1a3ef58c7b7cb9ce383e9dff046eac95%2Fpdi_tutorial_new_transformation_preview_with_missing_postal_codes_w532.png?alt=media)
4. Click **Stop** on the preview window to end the preview.

**Separate the records with missing postal codes**

Follow these instructions to use the Filter Rows transformation step to separate out those records missing postal codes. These records are resolved later in the tutorial.

1. Add a Filter Rows step to your transformation. Under the **Design** tab, select **Flow** > **Filter Rows**.
2. Insert your Filter Rows step between your Read Sales Data step and your Write to Database step.

   1. Right-click and delete the hop between the Read Sales Data step and Write to Database steps.
   2. Create a hop between the Read Sales Data step and the Filter Rows step. Create a hop by clicking the step, and then hold the SHIFT key down and click-and-drag to draw a line to the next step.
   3. Create a hop between the Filter Rows step and Write to Database step.
   4. In the dialog box that appears, select **Result is TRUE.**

   ![Hop dialog set to Result is True](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-1b5bbf3de80233c6470290e9aa25c65831a1e747%2Fpdi_tutorial_new_transformation_filter_results_is_true_w522.png?alt=media)
3. Double-click the Filter Rows step. The Filter Rows window appears.
4. In the **Step Name** field, enter `Filter Missing Zips`.
5. Click in **The condition** field to open the Fields window. The available conditions appear.
6. In the **Fields** window select **POSTALCODE** and click **OK**.
7. Click the comparison operator field, which is set to **=** by default. The Functions window appears.
8. Select **IS NOT NULL** from the list of functions, and then click **OK**​ to close the Functions window.

   ![Filter rows is set postalcode is not null](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-cf03b6964a3e2b63e8fd75ac7050a2eaf5c7c3fe%2Fpdi_tutorial_new_transformation_filter_rows_is_null_w532.png?alt=media)
9. Click **OK** to exit the Filter Rows window.

   **Note:** You will return to this step later to configure the **Send true data to step** and **Send false data to step** settings after adding their target steps to your transformation.
10. Save your transformation.

#### Step 3: Resolve missing data

After completing Step 2: Filter for missing codes, you are ready to resolve the missing postal codes. In this section, you will learn how to use a second text file containing a list of cities, states, and postal codes, to look up the postal codes for those records in which the fields are missing, which is the false branch of your Filter rows step.

First, you will use a Text file input step to read from the source file. Then, you will use a Stream lookup step to bring the resolved postal codes into the stream. Lastly, you will use the Select values step to rename fields on the stream, remove unnecessary fields, and more.

**Retrieve data from your lookup file**

Follow these steps to retrieve data from your lookup file.

1. Add a new Text File Input step to your transformation.

   This step retrieves the records from your lookup file. Do not add a hop yet.

   ![Add Text File Input step to canvas](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-859c25f009bd5760018f4f78493f7af4743c1af3%2Fpdi_tutorial_add_text_file_input_step_to_canvas_w391.png?alt=media)
2. Open the Text File Input step window, then enter `Read Postal Codes` in the **Step name** property.
3. Click **Browse** to navigate to the `Zipssortedbycitystate.csv` source file located in the directory `...\design-tools\data-integration\samples\transformations\files`.
4. Change **File type** to `*.csv`, select `Zipsortedbycitrystate.csv`, and click **OK**.

   The path to the source file appears in the **File or directory** field.
5. Click **Add**.

   The path to the file appears under **Selected files**.

**View the contents of the sample file**

Follow these steps to view the contents of the sample file.

1. Click the **Content** tab, then set the **Format** field to **Unix**​.
2. Click the **File** tab again and click the **Show file content** near the bottom of the window.
3. The Number of lines(0=all lines) window appears. Click the **OK**button to accept the default.
4. The **Content of first file** window shows the file. Examine the file to see how that input file is delimited, what enclosure character is used, and whether a header row is present. In the example, the input file is comma (,) delimited and the enclosure character is the quotation mark ("). A single header row contains field names.
5. Click **Close** to close the window.

**Edit and save the transformation**

Follow these steps to edit and save your transformation.

1. In the **Content** tab, change the **Separator** character to a comma (,) and confirm that the **Enclosure** setting is a quotation mark ("). Verify that the **Header** option is selected.
2. Under the **Fields** tab, click **Get Fields** to retrieve the data from your CSV file.
3. The Number of lines to sample window appears. Enter `0` in the field, then click **OK.**

   ![Results from Get Fields in the Fields tab](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-156081d05838b488762dbc18fbb967cb4ac94477%2Fpdi_tutorial_retrieve_fields_w532.png?alt=media)
4. If the Scan Result window displays, click **Close** to close it.
5. Click **Preview rows** to verify that your entries are correct.
   1. When prompted to enter the preview size, click **OK**.
   2. Review the information in the window, then click **Close**.
6. Click **OK** to exit the Text File input window.
7. Save the transformation.

**Resolve missing zip code information**

Follow these steps to resolve the missing postal code information.

1. Add a Stream Lookup step to your transformation by clicking the **Design** tab, expanding the **Lookup** folder, then selecting **Stream Lookup**.
2. Draw a hop from the Filter Missing Zips to the Stream lookup step. In the dialog box that appears, select **Result is FALSE**.
3. Create a hop from the Read Postal Codes step to the Stream lookup step.

   ![Add a hop from Read Postal Codes to Stream Lookup](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-d123518de033472219109e298137fee0714c7069%2Fpdi_tutorial_add_hop_from_read_postal_codes_to_steam_lookup_w372.png?alt=media)
4. Double-click the Stream lookup step to open the Stream Value Lookup window.
5. Rename Stream Lookup to Lookup Missing Zips.
6. From the Lookup step drop-down box, select **Read Postal Codes** as the lookup step. Perform the following:
   1. In the **key(s) to look up the value(s)** table, define the **CITY** and **STATE** fields .
   2. In **row #1**, open the drop-down menu in the **Field** column and select **CITY**.
   3. Click in the **LookupField** column and select **CITY**.
   4. In **row #2**, open the drop-down menu in the **Field** column and select **STATE**.
   5. Click in the **LookupField** column and select **STATE**.

      ![Stream value lookup example](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-566dab0ca0abadc797c3ea4c1faee737b6f4f34b%2Fpdi_tutorial_lookup_state_w532.png?alt=media)
7. Click **Get Lookup Fields** to pull the three fields from the Read Postal Code step.
8. **POSTALCODE** is the only field you want to retrieve. To delete the **CITY** and **STATE** lines, right-click in the line and select **Delete Selected Lines**.
9. In the **New Name** field, change the name **POSTALCODE** to **ZIP\_RESOLVED** and verify that **Type** is set to **String**.
10. Select **Use sorted list (i.s.o. hashtable)**.

    ![Value lookup example](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-3e94f028e77815c72a691acd2f11e787b228bc63%2Fpdi_tutorial_use_sorted_list_w532.png?alt=media)
11. Click **OK** to close the Stream Value Lookup edit properties dialog box.​​
12. Save your transformation.

**Preview your transformation**

Follow these steps to preview your transformation.

1. To preview the data, select and right-click the Lookup Missing Zips step. From the menu that appears, select **Preview**.
2. In the Transformation debug dialog window, click **Quick Launch** to preview the data flowing through this step.
3. In the Examine preview data window that appears, note that the new field, **ZIP\_RESOLVED**, has been added to the stream containing your resolved postal codes.

   ![Examine ZIP\_RESOLVED field](broken-reference)
4. Click **Close** to close the window.
5. If the Select the preview step window appears, click **Close**.

The execution results near the bottom of the PDI window show updated metrics in the **Step Metrics** tab.

**Apply formatting to your transformation**

Follow these steps to clean up the field layout on your lookup stream so that it matches the format and layout of the other stream going to the Write to Database step.

1. Add a Select Values step to your transformation by expanding the **Transform** folder and clicking Select Values.
2. Create a hop from the Lookup Missing Zips to the Select Values step.

   ![Add hop from Lookup Missing Zips to Select Values](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-74f97aed4729d8d76a1886ad045ddd9c1d5595a4%2Fpdi_tutorial_add_hop_from_lookup_missing_zips_to_select_values_w466.png?alt=media)
3. Double-click the Select Values step to open its properties dialog box.
4. Rename the Select Values step to Prepare Field Layout.
5. Click **Get fields to select** to retrieve all fields and begin modifying the stream layout.
6. In the **Fields** list, find the **#** column and click the number for the **ZIP\_RESOLVED** field.

   Use CTRL+UP (Windows/Linux) or COMMAND+UP (macOS) to move **ZIP\_RESOLVED** just below the **POSTALCODE** field, which is the one that still contains null values.

   ![Move ZIP\_RESOLVED field under POSTALCODES field](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-08456645bd9a2a2664a986c4241e7b2ee96ae1b6%2Fpdi_tutorial_mov_zip_resolved_fields_under_postal_codes_field_w532.png?alt=media)
7. Select the old **POSTALCODE** field in the list (line 20), right-click in the line, and select **Delete Selected Lines**
8. The original **POSTALCODE** field was formatted as a 9-character string. You must modify your new field to match the form. Click the **Meta-Data** tab.
9. In the first row of the **Fields to alter table the meta-data for** section, click in the **Fieldname** column and select **ZIP\_RESOLVED**. Perform the following steps:
   1. Enter `POSTALCODE` in the **Rename to** column.
   2. Select **String** in the **Type** column and enter `9` in the **Length** column.

      ![POSTALCODE String type and length](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-bb60cad84959554e60f3912950667cab74be81db%2Fpdi_tutorial_postal_code_string_and_length_w532.png?alt=media)
   3. Click **OK** to exit the **edit properties** dialog box.
10. Draw a hop from the Prepare Field Layout (Select values) step to the Write to Database (Table output) step.
11. When prompted, select the **Main output of the step** option.
12. Save your transformation.

    ![Renaming fields workflow example](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-20b8a5eb7bef00edf14857e375ddeb6d0a61fd4c%2Fpdi_tutorial_save_transformation_w532.png?alt=media)

#### Step 4: Clean the data

After completing Step 3: Resolve missing data, you can further cleanse and categorize the data into buckets before loading it into a relational database. In this section, you will cleanse the `COUNTRY` field data by mapping `United States` to `USA` using the Value mapper step. Cleaning the data ensures there is only one version of `USA`.

In addition, you will learn how to use buckets for categorizing the `SALES` data into small, medium, and large categories using the Number range step. You will learn how to insert these cleaning and categorizing functions into your transformation just prior to the Write to Database step on the canvas.

**Add a Value mapper step to the transformation**

Follow these steps to add the Value mapper step to the transformation.

1. Delete both hops connected to the Write to Database step. For each hop, right-click and select **Delete**.
2. Create some extra space on the canvas. Drag the Write to Database step toward the right side of your canvas.

   ![Add space on canvas for Value mapper step](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-a2d7f9799a6ad39b29926b4aa5dcf46d5a75ecea%2Fpdi_tutorial_add_space_on_canvas_for_value_mapper_step_w532_001.png?alt=media)
3. Add the Value mapper step to your transformation by expanding the **Transform** folder and choosing **Value mapper**.
4. Create a hop between the Filter Missing Zips and Value mapper steps. In the dialog box that appears, select **Result is TRUE**.
5. Create a hop between the Prepare Field Layout and Value mapper steps. When prompted, select the **Main output of the step** option.

   ![Add Value mapper step to the canvas](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-c32e0e1552a581cbbbfc9b7f8a691005032ca507%2Fpdi_tutorial_add_value_mapper_step_to_canvas_w532_002.png?alt=media)

**Set the properties in the Value Mapper step**

Follow these steps to set the properties in the Value mapper step.

1. Double-click the Value mapper step to open its properties dialog box.
2. Click in the **Fieldname to use** field and select **COUNTRY**.
3. In the **Field Values** table, define the `United States` and `USA` field values.
   1. In row #1, click the field in the **Source value** column and enter `United States`
   2. Then, click the field in the **Target value** column and enter `USA`

      ![Set values for fields in the Value mapper step](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-2a10691c56f86b064acb287d8dbeffb425f81222%2Fpdi_tutorial_set_properties_in_value_mapper_step_w532_003.png?alt=media)
4. Click **OK**.
5. Save your transformation.

**Apply ranges**

Follow these steps to apply ranges to your transformation.

1. Add a Number range step to your transformation by expanding the **Transform** folder and selecting **Number range**.
2. Create a hop between the **Value mapper** and **Number range** steps.
3. Create a hop between the Number range and Write to Database (which was built using Table output) steps. When prompted, select the **Main output of the step** option.

   ![Add Number range step to the canvas](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-1f76478db2fd4f7dd9ddb8c3d0b9767f5e11f9c4%2Fpdi_tutorial_add_number_range_step_to_canvas_w532_004.png?alt=media)
4. Double-click the Number range step to open its **properties** dialog box.
5. Click in the **Input field** and select **SALES** from the list.
6. In the **Output field** enter `DEALSIZE`.
7. In the **Ranges (min <=x< max)** table, define the **Lower Bound** and **Upper Bound** field ranges along with the bucket **Value**.
   1. In row #1, click the field in the **Upper Bound** column and enter `3000.0`. Then, click the field in the **Value** column and enter `Small`.
   2. In row #2, click the field in the **Lower Bound** column and enter `3000.0`. Then, click the field in the **Upper Bound** column and enter `7000.0`. Click the field in the **Value** column and enter `Medium`.
   3. In row #3, click the field in the **Lower Bound** column and enter `7000.0`. Then, click the field in the **Value** column and enter `Large`.

      ![Set ranges in Number Range step](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-d5f484d9a0fa34538ced8412ad7a8b85bcd8e4ab%2Fpdi_tutorial_set_ranges_in_number_range_step_w532_005.png?alt=media)
8. Click **OK**.

**Execute the SQL statement**

Your database table does not yet contain the field `DEALSIZE`. Perform these steps to execute the SQL statement.

1. Double-click the Write to Database step to open its properties dialog box.
2. Click the **SQL** button at the bottom of the window to generate the new DDL for editing your original target table. Note that the Write to Database step was built using Table output.
   1. The **Simple SQL editor** window appears with the SQL statements needed to `alter` the table.

      ![Simple SQL editor to generate the DDL](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-e79f63e267d4a35d3835f29184d3a18a8785162b%2Fpdi_tutorial_simple_sql_editor_to_generate_ddl_w455_006.png?alt=media)
   2. Click **Execute** to execute the SQL statement.
   3. The Results of the SQL statements window appears. Examine the results, then click **OK** to close the window.
   4. Click **Close** in the Simple SQL editor window to close it.
   5. Click **OK** to close the Write to Database window. Note that the Write to Database step was built using Table output
3. Save your transformation.

#### Step 5: Run the transformation

Pentaho Data Integration provides a number of deployment options. The **Running a Transformation** section in the **Pentaho Data Integration** document explains these and other options available for execution. In this section of the tutorial, you create a transformation using the **Local** run option.

1. In the PDI client window, select **Action** > **Run**.

   The Run Options window appears.
2. Keep the default **Pentaho local** option for this exercise.

   It uses the native Pentaho engine and runs the transformation on your local machine. See the **Pentaho Data Integration** document if you are interested in setting up configurations that use another engine.
3. Click **Run**.

   The transformation executes.

   ![Transformation runs without errors](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-a9eb59d912a8c7a9e2bb4592cf9372ef3fef269c%2Fpdi_tutorial_transformation_ran_good_w552.png?alt=media)

After the transformation runs, the **Execution Results** panel opens below the canvas.

**Viewing the execution results**

Use the tabs in the **Execution Results** section of the window to view how the transformation executed, pinpoint errors, and monitor performance.

* **Step Metrics**

  Provides statistics for each step in your transformation including how many records were read, written, or caused an error, as well as processing speed (rows per second) and more. This tab also indicates whether an error occurred in a transformation step.

  This tutorial introduces no intentional transformation errors, so the transformation should run correctly. If a mistake does occur, you can view the steps that caused the transformation to fail highlighted in red. In the example below, the Lookup Missing Zips step caused an error.

  ![Error message display](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-845e491680e7ccbc8d7397d0e78bed87db04eece%2Fpdi_tutorial_transformation_ran_with_errors_w532.png?alt=media)
* **Logging**

  Shows the logging details for the most recent execution of the transformation. It also allows you to drill deeper to determine where errors occur. Error lines are highlighted in red. In the example below, the **Lookup Missing Zips** step caused an error because it attempted to look up values on a field called **POSTALCODE2** which did not exist in the lookup stream.

  ![Transformation logging display](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-9b168628910e2d5daa4b15ada360973c64f1ed73%2Fpdi_tutorial_transformation_logging_display_w532.png?alt=media)
* **Execution History**

  Provides access to the step metrics and log information from previous executions of the transformation. This feature works only if you have configured your transformation to log to a database through the **Logging** tab of the Transformation Settings dialog box.
* **Performance Graph**

  Analyzes the performance of steps based on a variety of metrics including how many records were read, written, or caused an error, as well as processing speed (rows per second) and more. Like the execution history, this feature requires you to configure your transformation to log to a database through the **Logging** tab found in the Transformation Settings dialog box.
* **Metrics tab**

  Shows a Gantt chart after the transformation or job runs. This information includes how long it takes to connect to a database, the time spent executing a SQL query, or the load time of a transformation.

  ![Step metrics tab](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-de2390bd39457804598553cd27afa48acd0e52de%2Fpdi_tutorial_transformation_metrics_tab_w532.png?alt=media)
* **Preview Data**

  Shows a preview of the data.

#### Step 6: Orchestrate with jobs

Jobs are used to coordinate ETL activities such as:

* Defining the flow and dependencies that control the linear order for the transformations to run.
* Preparing for execution by checking conditions such as, "Is my source file available?" or "Does a table exist?"
* Performing bulk load database operations.
* Assisting file management, such as posting or retrieving files using FTP, copying files, and deleting files.
* Sending success or failure notifications through email.

For this part of the tutorial, imagine that an external system is responsible for placing your `sales_data.csv` input in its source location every Saturday night at 9 p.m. You want to create a job that will verify that the file has arrived and then run the transformation to load the records into the database. In a subsequent exercise, you will schedule the job to run every Sunday morning at 9 a.m.

The following steps assume that you have built a Getting Started transformation as described in Step 1: Extract and load data of the tutorial.

1. Go to **File** > **New** > **Job**.

   ![PDI job window](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-191884ec46461d9ebaeef5f08f1d4dcbbc9f5728%2Fpdi_tutorial_screen_job_new_job_canvas_w552.png?alt=media)
2. Expand the **General** folder and drag a Start job entry onto the canvas.

   The **Start** job entry defines where the execution will begin.

   **Note:** Jobs run in a sequential order of steps and transformations can run in a parallel order of steps.
3. Expand the **Conditions** folder and add a File Exists job entry.
4. Draw a hop from the Start job entry to the File Exists job entry.

   ![Draw hop from Start to File exists](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-65f7466f6cc1e6dde485b8ee18917430c730bdc0%2Fpdi_tutorial_screen_job_draw_hop_w221.png?alt=media)
5. Double-click the File Exists job entry to open its properties dialog box. Click **Browse** and set the filter near the bottom of the window to **All Files**. Select the `sales_data.csv` from the following directory: `...\design-tools\data-integration\samples\transformations\files`.
6. Click **OK** to exit the Open File window.
7. Click **OK** to exit the Check if a file exists window.
8. Expand the **General** folder and add a Transformation job entry.
9. Draw a hop between the File Exists and the Transformation job entries.
10. Double-click the Transformation job entry to open its properties dialog box.
11. Click **Browse** to open the **Select repository object** window. Browse to and select the **Getting Started** transformation.
12. Click **OK** to close the Transformation window.
13. Save your job as **Sample Job**.
14. Click **Run** icon in the toolbar. When the Run Options window appears, select **Local** environment type and click **Run**. The **Execution Results** panel should open showing you the job metrics and log information for the job execution.

    ![Job sample](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-e138ad954c6675e8c2ceefcff122c9042d266e20%2Fpdi_tutorial_screen_job_sample_job_w552.png?alt=media)

### PDI job tutorial

This is a shorter, standalone version of the job exercise.

Jobs are used to coordinate ETL activities such as:

* Defining the flow and dependencies for what order transformations should be run.
* Preparing for execution by checking conditions such as, "Is my source file available?" or "Does a table exist?"
* Performing bulk load database operations.
* File management such as posting or retrieving files using FTP, copying files and deleting files.
* Sending success or failure notifications through email.

For this exercise, imagine that an external system is responsible for placing your `sales_data.csv` input in its source location every Saturday night at 9 p.m. You want to create a job that will check to see that the file has arrived and run your transformation to load the records into the database. In a subsequent exercise, you will schedule the job to be run every Sunday morning at 9 a.m.

To complete this exercise, you must have completed the exercises in the [Pentaho Data Integration (PDI) tutorial](#pentaho-data-integration-pdi-tutorial).

1. Go to **File** > **New** > **Job**.

   ![PDI Job Window](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-fe869e2bd6f8244f9d0606d6a5abac92fddc56fe%2FPDI_Job_Tutorial_PDI_Job_Window.png?alt=media)
2. Expand the **General** folder and drag a Start job entry onto the graphical workspace.

   The **Start** job entry defines where the execution will begin.
3. Expand the **Conditions** folder and add a File Exists job entry.
4. Draw a hop from the Start job entry to the File Exists job entry.
5. Double-click the File Exists job entry to open its Edit Properties dialog box. Click **Browse** and set the filter near the bottom of the window to **All Files**. Select the `sales_data.csv` from the following location: `...\design-tools\data-integration\samples\transformations\files`.
6. Click **OK** to exit from the Open File window.
7. Click **OK** to exit from the Check if a file exists window.
8. In Spoon, expand the **General** folder and add a Transformation job entry.
9. Draw a hop between the File Exists and the Transformation job entries.
10. Double-click the Transformation job entry to open its edit Properties dialog box.
11. Click **Browse** to open the **Select repository object** window. Browse to and select the transformation you created in the [Pentaho Data Integration (PDI) tutorial](#pentaho-data-integration-pdi-tutorial).
12. Expand the repository tree to find your sample transformation. Select it and click **OK**.

    ![Select repository object window](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-fa489220686f9ffd06b9bdfc7dd113b2069eb6bf%2FPDI_Job_Tutorial_Select_repository_object_window.png?alt=media)
13. Save your job as Sample Job.
14. Click **Run** icon in the toolbar. When the Run Options window appears, choose **Local** environment type and click **Run**. The **Execution Results** panel should open showing you the job metrics and log information for the job execution.

    ![Job Sample](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-225ec0b5f2c087ef881f79d64b6b74e2c8e75b1a%2FPDI_Job_Tutorial_Sample_Job.png?alt=media)

### Getting started with PDI and Hadoop

Pentaho provides a complete big data analytics solution that supports the entire big data analytics process. From big data aggregation, preparation, and integration, to interactive visualization, analysis, and prediction, Pentaho allows you to harvest the meaningful patterns buried in big data stores. Analyzing your big data sets gives you the ability to identify new revenue sources, develop loyal and profitable customer relationships, and run your organization more efficiently and cost effectively.

### Next steps

The tutorials above are designed to quickly demonstrate basic PDI features.

For more detailed information about PDI features and functions, see the following topics in the **Pentaho Data Integration** document:

* **Learn about the PDI Client**
* **Use Pentaho Repositories in PDI**
* **Schedule Perspective in the PDI Client**


# Pentaho, big data, and Hadoop

The term big data applies to very large, complex, or dynamic datasets that need to be stored and managed over a long time. To derive benefits from big data, you need the ability to access, process, and analyze data as it is being created. However, the size and structure of big data makes it very inefficient to maintain and process it using traditional relational databases.

Big data solutions re-engineer the components of traditional databases, such as data storage, retrieval, query, processing, and massively scale them.

### In this topic

* [Big data overview](#big-data-overview)
* [About Hadoop](#about-hadoop)
* [Big data resources](#big-data-resources)

### Big data overview

Pentaho increases speed-of-thought analysis against even the largest of big data stores by focusing on the features that deliver performance.

* Instant access: Pentaho provides visual tools to make it easy to define the sets of data that are important to you for interactive analysis. These data sets and associated analytics can be easily shared with others, and as new business questions arise, new views of data can be defined for interactive analysis.
* High performance platform: Pentaho is built on a modern, lightweight, high performance platform. This platform fully leverages 64-bit, multi-core processors and large memory spaces to efficiently leverage the power of contemporary hardware.
* Extreme-scale, in-memory caching: Pentaho is unique in leveraging external data grid technologies, such as Infinispan and Memcached to load vast amounts of data into memory so that it is instantly available for speed-of-thought analysis.
* Federated data integration: Data can be extracted from multiple sources, including big data and traditional data stores, integrated together and then flowed directly into reports, without needing an enterprise data warehouse or data mart.

### About Hadoop

The Apache Hadoop software library is a framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. It is designed to scale up from single servers to thousands of machines, each offering local computation and storage. Rather than rely on hardware to deliver high-availability, the library itself is designed to detect and handle failures at the application layer, so delivering a highly-available service on top of a cluster of computers, each of which may be prone to failures.

A Hadoop platform consists of a Hadoop kernel, a [MapReduce](http://wiki.apache.org/hadoop/MapReduce) model, a distributed file system, and often a number of related projects—such as [Apache Hive](http://hive.apache.org/), [Apache HBase](http://hbase.apache.org/), and others.

A Hadoop Distributed File System, commonly referred to as HDFS, is a Java-based, distributed, scalable, and portable file system for the Hadoop framework.

### Big data resources

The following resources may help in understanding big data architecture and components:

* [Pentaho Big Data Analytics Center](http://www.pentahobigdata.com/resources)
* [Apache Hadoop project](http://hadoop.apache.org/) -- A project that contains libraries that allows for the distributed processing of large data sets across clusters of computers using simple programming models. There are several modules, including the [Hadoop Distributed File System (HDFS)](http://wiki.apache.org/hadoop/HDFS), which is a distributed file system that provides high-throughput access to application data and [Hadoop MapReduce](http://wiki.apache.org/hadoop/MapReduce), which is a key algorithm to distribute work around a cluster.
* [Avro](http://avro.apache.org/)—A data serialization system
* [HBase](http://hbase.apache.org/)—A scalable, distributed database that supports structured data storage for large tables
* [Hive](http://hive.apache.org/)—A data warehouse infrastructure that provides data summarization and on-demand querying
* [ZooKeeper](http://zookeeper.apache.org/)—A high-performance coordination service for distributed applications
* [MongoDB](http://www.mongodb.org/)— A NoSQL open source document-oriented database system developed and supported by 10gen
* [Splunk](http://www.splunk.com/) - A data collection, visualization and indexing engine for operational intelligence that is developed by Splunk, Inc.
* [CouchDB](http://couchdb.apache.org/)—A NoSQL open source document-oriented database system developed and supported by Apache
* [Sqoop](http://sqoop.apache.org/)—Software for transferring data between relational databases and Hadoop
* [Oozie](http://oozie.apache.org/)—A workflow scheduler system to manage Hadoop jobs


# About Pentaho workflows

The route that you take with Pentaho depends on your expertise, business needs, and data. It also depends on what you want to analyze and report. During an evaluation, you might use both tracks.

All of the products are integrated to work smoothly together, regardless of which track you ultimately choose. We provide specific details within the workflow discussions, however, here are the high-level use cases for each track.

* Business Analytics (BA) Track: Great for analysis and reporting. Meant primarily for business users and does not require special skills to successfully use the components involved. This track enables anyone to build Pentaho solutions without using programming or having deep understanding of data structures.
* Data Integration (DI) Track: Meant for data design professionals and requires a working knowledge of data structures and modeling, as well as extract, transform, and load (ETL) processes. With this track, you can directly manipulate data from multiple sources, making it scalable and efficient for enterprise-wide analysis and reporting.

Each track has three workflows: one for Evaluation, one for Development, and one for Production.

* Evaluate and Learn: If you used the trial download on the Pentaho website and want to get a hands-on feel for the components that are best for your implementation, follow the Evaluation Workflow.
* Develop Pentaho Solutions: After you have figured out which components are best for you and how to use them, the Develop Workflow is the process you use to build, change, and test Pentaho solutions until they meet your production requirements.
* Go Live for Production: When your solution is working just right, the Go Live Workflow shows how to move your solution from development to production.

### In this topic

* [Prepare for the evaluation](#prepare-for-the-evaluation)
* [Pentaho Data Integration workflows](#pentaho-data-integration-workflows)
* [Pentaho Business Analytics workflow](#pentaho-business-analytics-workflow)

### Prepare for the evaluation

This table guides you through the differences between the Business Analytics and Data Integration tracks. It also helps you decide which track to follow for evaluation. You may choose to follow one track, then the other, while you are exploring the software.

| Explore Considerations                                                                                                                        | Choose Options                                                                                                                                                                |                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Business Analytics Evaluation](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/evaluate-and-learn-pentaho-business-analytics) | [Data Integration Evaluation](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/evaluate-and-learn-pentaho-data-integration-pdi)                                 |                                                                                                                                                                                       |
| Expertise                                                                                                                                     | <ul><li>No special skills required</li><li>Knowledge of business requirements and what reports and analysis should show</li></ul>                                             | <ul><li>Knowledge of business requirements</li><li>Understanding of data structures and modeling</li><li>Knowledge of extract, transform, and load (ETL) processes</li></ul>          |
| Data Set Description                                                                                                                          | <ul><li>Single source of data</li><li>Data from multiple sources that have been transformed and joined into a single data mart or warehouse</li><li>Small data sets</li></ul> | <ul><li>Multiple sources of data</li><li>Data you want to transform and join in one or more data marts or warehouses</li><li>Large to enormously vast data sets</li></ul>             |
| Reporting Options                                                                                                                             | Offers a wide variety of visualization and reporting options.                                                                                                                 | Offers more limited but focused reporting options that help you visualize and analyze data. BA tools can be used to generate reports based on DI-processed data.                      |
| Data Storage Types                                                                                                                            | <ul><li>Relational databases</li><li>CSV data sources</li><li>SQL queries</li></ul>                                                                                           | <ul><li>Relational databases</li><li>NoSQL or Hadoop databases</li><li>Big data of any types</li><li>Data from a web service</li></ul>                                                |
| Recommendation                                                                                                                                | Best used by business analysts, managers, report designers, individual business units within an organization or enterprise                                                    | Best used by data scientists, data modelers, data integration and ETL developers, individual business units within an organization or enterprise, and enterprise-wide implementations |

Now that you have an idea of which track you want to follow for evaluation, choose an evaluation method. This decision table explains the different options for evaluation so you can pick the option that works best for you.

| Explore Considerations                            | Choose Options                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Hosted Demo](http://www.pentaho.com/hosted-demo) | [Custom Prototype](http://www.pentaho.com/helpmeout)                                                                                                                                                                                                                                                                                                                                                     | [Trial Download](http://www.pentaho.com/download)                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                           |
| Track                                             | Business Analytics                                                                                                                                                                                                                                                                                                                                                                                       | Business Analytics or Data Integration                                                                                                                                                                                                                                                                                                     | Business Analytics or Data Integration                                                                                                                                                                                                                                                                                                                                                    |
| Summary                                           | A cloud-based, hands-on, interactive exploration of Business Analytics reports, analysis, visualizations, and dashboards. Here you can see how easy and fun it can be to use Pentaho.                                                                                                                                                                                                                    | Work with Pentaho analysts and data integration specialists to plan and build a complimentary custom prototype that illustrates what Pentaho can do with your data. A representative will guide you through the entire process.                                                                                                            | Using our trial software, tutorials, and documentation, install and configure your own work environment. Then, build a prototype to get a complete Pentaho experience from installation and administration, through creating your first data models and build reports, analysis, dashboards, and data integration ETL transformations.                                                    |
| Data Source                                       | Pentaho sample data in CSV format                                                                                                                                                                                                                                                                                                                                                                        | Your sample data, including a range of typical data characteristics in CSV format.                                                                                                                                                                                                                                                         | Your sample data, including a range of typical data characteristics in the format that you commonly use                                                                                                                                                                                                                                                                                   |
| Hardware/Software Requirements                    | Web browser                                                                                                                                                                                                                                                                                                                                                                                              | Varies, depending on your requirements.                                                                                                                                                                                                                                                                                                    | One computer that meets the server requirements stated in the [Components Reference](https://docs.pentaho.com/pdia-try-pdia/components-reference).                                                                                                                                                                                                                                        |
| Recommendation                                    | <p>Any evaluator who wants an overview of Business Analytics features.</p><ul><li>Recommended for business analysts and report designers.</li></ul><p>We recommend that you try out the <a href="http://www.pentaho.com/resources/events/20121109-analytics-accelerator-program/">Custom Prototype</a> or <a href="http://www.pentaho.com/download">Trial Download</a> after you do the hosted demo.</p> | <p>All evaluators, particularly any big data or Data Integration evaluators.</p><ul><li>Recommended for evaluators who want to <a href="http://www.pentaho.com/accelerator-program">explore Business Analytics and Data Integration features</a> using a subset of their own data.</li><li>Limited to first-time customers only.</li></ul> | <p>Any evaluator who wants to independently work with Business Analytics, Data Integration tools, and big data. - Recommended for evaluators who want to explore Business Analytics and Data Integration features using their own data.</p><ul><li><a href="http://www.pentaho.com/service/technical-support">Technical support</a> is available to help if you have questions.</li></ul> |

### Pentaho Data Integration workflows

Pentaho Data Integration is a robust extract, transform, and load (ETL) tool that you can use to integrate, manipulate, and visualize your data. You can use PDI to import, transform, and export data from multiple data sources, including flat files, relational databases, Hadoop, NoSQL databases, analytic databases, social media streams, and operational stores. You can also use PDI to clean and enrich the data, move data between databases, and to visualize your data.

#### In this topic

* [Evaluate and learn PDI](#evaluate-and-learn-pdi)
* [Develop your PDI solution](#develop-your-pdi-solution)
* [Go Live for production - DI](#go-live-for-production---di)
* [Commonly used PDI steps and entries](#commonly-used-pdi-steps-and-entries)

#### Evaluate and learn PDI

As you explore Pentaho Data Integration (PDI), you will be introduced to the major components, watch videos, work through hands-on examples, and read about the different features.

Review the documentation and contact Pentaho [sales support](https://www.pentaho.com/services) if you have questions.

**PDI basics**

This section familiarizes you with PDI and introduces you to basic terminology and concepts. Then, you learn how to start and configure Spoon and take a spin through the interface.

* Get a basic understanding of what PDI does.
* View a video that explains how PDI fits into the [Business Analytics Platform](http://www.youtube.com/watch?v=hCMtrLCsBuE).
* Read about Pentaho Data Integration architecture in the **Pentaho Data Integration** document.

**Get acquainted with the PDI client**

Spoon is the PDI design tool. In this section you will set up Spoon, take a tour of the Spoon interface, and learn about the different Spoon perspectives.

* Check out the [hardware and software requirements](https://docs.pentaho.com/pdia-try-pdia/components-reference) for PDI.
* [Download trial version](http://www.pentaho.com/download) of the Pentaho Suite and install the software. (The platform includes PDI.)
* Learn how to install PDI only. See [Custom installation](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages-do-not-use/install-trial-legacy-child-pages/custom-installation) for details.
* Configure the Pentaho Server. Depending on your platform, see [Increase Pentaho Server memory limit for installations on Linux](https://github.com/pentaho/documentation/blob/main/PDIA/11.0/Get%20Started/Pentaho%20evaluation/Increase%20Pentaho%20Server%20memory%20limit%20for%20installations%20on%20Linux=GUID-EBDD031B-404B-4E8C-B48E-75AC258CDF52=3=en=.md) or [Increase Pentaho Server memory limit for installations on Windows](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages-do-not-use/install-trial-legacy-child-pages/increase-pentaho-server-memory-limit-for-installations-on-windows) for details.
* Start the Pentaho Server. Depending on your platform, see [Start and stop the Pentaho Server for configuration on Linux](https://github.com/pentaho/documentation/blob/main/PDIA/11.0/Get%20Started/Pentaho%20evaluation/Start%20and%20stop%20the%20Pentaho%20Server%20for%20configuration%20on%20Linux=GUID-2AF5899D-DD81-4F5E-B884-BA998F6DBC2A=1=en=.md) or [Start and stop the Pentaho Server for configuration on Windows](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages-do-not-use/install-trial-legacy-child-pages/start-and-stop-the-pentaho-server-for-configuration-on-windows) for details.
* Access the PDI client. See the **Pentaho Data Integration** document for details.
* Tour the PDI client perspectives. See the **Pentaho Data Integration** document for details.
* Read about terminology and basic concepts in the **Pentaho Data Integration** document.

**Build transformations and jobs**

Now that your environment is set up and you are familiar with the PDI client, you are ready to build transformations and jobs. Trying the following task may be helpful.

* Create a connection to the Pentaho Repository.
* Work through the exercise on [Creating a Transformation](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/pdi-transformation-tutorial) that involves a flat file. Click through the links at the bottom of the page to complete the exercise.
* Create a job to execute the transformation.
* Schedule a job to execute the transformation at a later time.
* Review [commonly used steps and job entries](#commonly-used-pdi-steps-and-entries).

**Explore Big Data and Streamlined Data Refinery**

In this section, you will learn how to use transformation steps to connect to a variety of big data sources, including Hadoop, NoSQL, and analytical databases such as MongoDB. You can then try working through the detailed, step-by-step tutorials, and peruse the out-of-the-box steps that Spoon provides. Learn how to work with Streamlined Data Refinery. Then, you will have an opportunity to move beyond the basics and learn how to edit transformations and metadata models.

* Watch one of our [Big Data Videos](http://www.youtube.com/watch?v=vOMOFPMnXgk).
* Learn how to work with Streamlined Data Refinery. See **Pentaho Data Integration** for details.
* Learn how to auto model using the Build Model. See **Pentaho Data Integration** for details. job entry and how this feature intersects with Analyzer.
* Find out what big data steps are available out-of-the-box. See [Commonly used PDI steps and entries](#commonly-used-pdi-steps-and-entries) for details.
* Find out which Hadoop distributions are available and how to configure them. See [Pentaho, big data, and Hadoop](https://docs.pentaho.com/pdia-try-pdia/pentaho-big-data-and-hadoop) for details.

  **Note:** You should already have a cluster set up to perform this task.
* Edit transformations and metadata models. See **Pentaho Data Integration** for details.
* Watch a video about how to use PDI to [blend Big Data](http://www.youtube.com/watch?v=JyypUdwySrQ).

**About Kitchen, Pan, and Carte**

Kitchen, Pan, and Carte are command line tools for executing transformations and jobs modeled in the PDI client.

* Use Pan and Kitchen command line tools to work with transformations and jobs
* Use Carte clusters to:
  * Run transformations and jobs on a Carte cluster.
  * Schedule jobs to run on a remote Carte server.
  * Start or stop Carte from the command line interface or a URL.
  * Run transformations and jobs from the repository on the Carte server

See the **Pentaho Data Integration** document for details on Kitchen, Pan, and Carte.

**Learn more**

Now that you have completed an initial evaluation of PDI, dig a little deeper. Find out how to:

* Use newer steps and entries, like Spark Submit. See the **Pentaho Data Integration** document for details.
* Read about how to turn a transformation into a data service. See the **Pentaho Data Integration** document for details.
* Use the ETL Metadata Injection step. See the **Pentaho Data Integration** document for details.
* Check out our **What's New** document.
* Create other Data Integration solutions. See the **Pentaho Data Integration** document for details.
* Administer PDI. See the administration documentation for details.
* Integrate with different security protocols, like Pentaho security, LDAP, MSAD, and Kerberos. See the administration documentation for details.
* Check out our developer center section in the administration documentation.

#### Develop your PDI solution

This workflow helps you to set up and configure the DI development and test environments, then build, test, and tune your Pentaho DI solution prototype. This process is similar to the trial download evaluation experience, except that you will be completely configuring the Pentaho Server for data integration and working with your own ETL developers.

If you need extra help, Pentaho [professional services](https://www.pentaho.com/services) is available. The end result is to learn DI implementation best practices and deploy your DI solution to a production server. Most development and testing for DI occurs in Spoon.

Before you begin developing your DI solution, we recommend that you attend Pentaho [training classes](http://www.pentaho.com/service/training) to learn how to install and configure the Pentaho Server, as well as how to develop data models.

This section is grouped into parts that will guide you during the development of your DI solution. These parts are iterative and you might bounce between them during development. For example, as you tune a job, you might find that although you have built a solution that produces the right results, it takes a long time to run. You might need to rebuild and test a transformation to improve efficiency, and then retest it.

**Design DI solution**

Design helps you think critically about the problem you want to solve and possible solutions. Consider these questions as you gather your requirements and design the solution.

* **Output**

  What does the overall solution look like? What questions are posing and how do you want the answers formatted?
* **Data Sources**

  What type(s) of data sources are you querying? Where are they located? How much data do you need to process? Are you using big data? Are you using relational or non-relational data sources? Will you have a target data source? If so, where are they located?
* **Content/Processing**

  What data quality issues do you have? How is the input data mapped to the output data? Where do you want to process the content, in PDI or in the data source? What hardware will you include in your development environment? Will you need one or more quality assurance test environments or production environments?

Also, consider templates or standards, naming conventions, and other requirements of your end users if you have them. Consider how you will back up your data as well.

**Set up a development environment**

Setting up the environment includes installing and configuring PDI on development computers, configuring clustering if needed, and connecting to data sources. If you have one or more quality assurance environments, you will need to set those up also.

| Task                                    | Do This                                                                                                                                                                                                                                                               | Objective                                                                                                                                            |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Verify System Requirements              | <p>Consult the following references to verify requirements:- <a href="components-reference">Components Reference</a></p><ul><li><a href="https://help.hitachivantara.com/Documentation/Pentaho/9.3/Setup/JDBC_drivers_reference">JDBC Drivers Reference</a></li></ul> | <ul><li>Acquire one or more servers that meet the requirements.</li><li>Obtain the correct drivers for your system.</li></ul>                        |
| Obtain Software and Install PDI         | <p>See the <strong>Install Pentaho Data Integration and Analytics</strong> document for following instructions:- Installing PDI</p><ul><li>Starting the Pentaho Server</li><li>Starting the PDI client (also known as Spoon)</li></ul>                                | <ul><li>Get the software from your Sales Support representative.</li><li>Install the software.</li><li>Start the Pentaho Server and Spoon.</li></ul> |
| Install licenses for the Pentaho Server | See the **Administer Pentaho Data Integration and Analytics** document for instructions on installing licenses.                                                                                                                                                       | <ul><li>Add all acquired Pentaho licenses.</li></ul>                                                                                                 |
| Connect to the Pentaho Repository       | See the **Pentaho Data Integration** for instructions on connecting to the Pentaho Repository.                                                                                                                                                                        | <ul><li>Connect to the Pentaho Repository.</li></ul>                                                                                                 |
| Apply Advanced Security (if needed)     | See the **Administer Pentaho Data Integration and Analytics** document for details on Advanced Security.                                                                                                                                                              | <ul><li>Determine whether you need to apply Advanced Security.</li></ul>                                                                             |

**Build and test solution**

During this step, you develop transformations, jobs, and models, then test what you have developed. You will tune the transformations, jobs, and models for optimal performance.

Development occurs in the PDI client design tool. The PDI client's streamlined design tightly couples the build and test activities so that you can easily perform them iteratively. The PDI client has perspectives to help you perform ETL and visualize data. The PDI client also provides a scheduling perspective that can be used to automate testing. Testing encompasses verifying the quality of transformations and jobs, reviewing visualizations, and debugging issues. One common method of testing is to include steps in a transformation or job that calculates hash totals, checksums, record counts, and so forth to determine whether data is being properly processed. You can also visualize your data in analyzer and report designer and review the results as you develop. This can not only help you find errors and issues with processing but can help you get a jump on user acceptance testing if you show these reports to your customers or business analysts to get early feedback.

One basic question is how you can determine the number of transformations and jobs needed, as well as the order in which they should be executed. A good rule of thumb is to create one transformation for each combination of source system and target tables. You can often identify combinations in your mapping documents. Once you have identified the number of transformations that you need, you can use the same process to determine that number of jobs that you need. When considering the order of execution for transformations and jobs, consider how referential integrity is enforced. Run target table transformations that have no dependencies first, then run transformations that depend on those tables, and so forth.

| Task                                     | Do This                                                                                                                    | Objective                                                                                                                                                                                         |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Understand the Basics                    | <ul><li>Read the overview of the PDI client process in the <strong>Pentaho Data Integration</strong> document.</li></ul>   | <ul><li>Review information about the process and perspectives.</li></ul>                                                                                                                          |
| Review most often used steps and entries | <ul><li>Review <a href="#commonly-used-pdi-steps-and-entries">commonly-used steps and entries</a>.</li></ul>               | <ul><li>Review available transformations and determine how you can use them for your solution.</li><li>Review job step references to identify which steps can be used in your solution.</li></ul> |
| Create and Run Transformations           | <ul><li>Create and run a transformation. See the <strong>Pentaho Data Integration</strong> document for details.</li></ul> | <ul><li>Identify the transformations needed for your job and implement them.</li><li>Save transformation.</li><li>Run transformations locally.</li></ul>                                          |
| Create and Run a Job                     | <ul><li>Create and run a job. See the <strong>Pentaho Data Integration</strong> document for details.</li></ul>            | <ul><li>Create a job.</li><li>Arrange transformations in a job so that they execute logically.</li><li>Run a job.</li></ul>                                                                       |

**Tune solution**

Fine tune transformations and jobs to optimize performance. This involves using various tools such as the DI Operation and Audit Mart to determine where bottlenecks or other performance issues occur, and addressing them.

| Task                                                                                 | Do This                                                                                                                                                                                                                                                                                             | Objective                                                                                                                     |
| ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Review the Performance Tuning Checklist and Make Changes to Transformations and Jobs | <ul><li>Review tuning tips. See the <strong>Administer Pentaho Data Integration and Analytics</strong> document for tuning tips.</li></ul>                                                                                                                                                          | <ul><li>Get familiar with things that you can do to optimize performance.</li><li>Apply tuning tips as needed.</li></ul>      |
| Consider other performance tuning options                                            | <ul><li>Read about transactional databases. See the <strong>Pentaho Data Integration</strong> document for details on transactional databases.</li><li>Read about using logs. See the <strong>Administer Pentaho Data Integration and Analytics</strong> document for details on logging.</li></ul> | <ul><li>Learn how to apply transactional databases.</li><li>Learn how to use logs to tune transformations and jobs.</li></ul> |

**Next steps**

These resources will be helpful to you as you prepare to Go Live for Production:

* Prepare to [Go Live for Production - DI](#go-live-for-production---di).
* [Support Portal](https://support.pentaho.com/hc/en-us): check with Support for service packs.

#### Go Live for production - DI

Go Live is the process by which you migrate a prototype to production. This process is divided into four parts:

* Setting up the production environment
* Deploying the solution
* Tuning the solution
* Scheduling the runs

**Set up production environment**

Setting up the environment includes installing the software on production computers, configuring clustering, and connecting to data sources. To set up the environment, install and configure the Pentaho Server, Spoon, and any plugins required. Then set up data sources and clusters.

| Task                                           | Do This                                                                                                                                                                                                                                                                                                                                                                                       | Objective                                                                                                                                                                          |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Verify system requirements                     | <ul><li>Consult the <a href="components-reference">Components Reference</a>.</li><li>Consult the <a href="https://help.hitachivantara.com/Documentation/Pentaho/9.3/Setup/JDBC_drivers_reference">JDBC Drivers Reference</a>.</li></ul>                                                                                                                                                       | <ul><li>Acquire one or more servers that meet the requirements.</li><li>Obtain the correct drivers for your system.</li></ul>                                                      |
| Obtain software and install the Pentaho Server | <ul><li>Download the Pentaho software.</li><li>Start the Pentaho Server. See <strong>Install Pentaho Data Integration and Analytics</strong> for details.</li><li>Start the PDI client. See <strong>Pentaho Data Integration</strong> for details.</li><li>Install the licenses (if necessary). See <strong>Administer Pentaho Data Integration and Analytics</strong> for details.</li></ul> | <ul><li>Get the software from your Sales Support representative.</li><li>Install the software.</li></ul>                                                                           |
| Change the Server Fully Qualified URL          | <ul><li>Change the ports and URLs. See <strong>Administer Pentaho Data Integration and Analytics</strong> for details.</li></ul>                                                                                                                                                                                                                                                              | <ul><li>Change the server's URL so that you do not have a conflict.</li></ul>                                                                                                      |
| Connect to the Pentaho Repository              | <ul><li>Create a connection to the Pentaho Repository. See <strong>Pentaho Data Integration</strong> for details.</li></ul>                                                                                                                                                                                                                                                                   | <ul><li>Connect to the Pentaho Repository.</li></ul>                                                                                                                               |
| Set up clusters                                | <ul><li>Optional: Set up clusters. See <strong>Pentaho Data Integration</strong> for details.</li></ul>                                                                                                                                                                                                                                                                                       | <ul><li>Become familiar with clustering.</li><li>Set up clusters, if they are needed in your environment.</li></ul>                                                                |
| Copy configuration files                       | Copy `shared.xml`, `repositories.xml`, `kettle.properties`, and JAR files from the development environment to the production environment.                                                                                                                                                                                                                                                     | <ul><li>System is set up and ready for production.</li></ul>                                                                                                                       |
| Logging and monitoring your server             | <ul><li>Review logging and monitoring operations. See <strong>Pentaho Data Integration</strong> for details.</li><li>Enable logging. See <strong>Administer Pentaho Data Integration and Analytics</strong> for details.</li><li>Monitor PDI and SNMP traps. See <strong>Administer Pentaho Data Integration and Analytics</strong> for details.</li></ul>                                    | <ul><li><p>Learn about the different ways to log and monitor Pentaho Server operations:</p><ul><li>Log through Spoon and Carte</li><li>Use SNMP traps with PDI</li></ul></li></ul> |

**Deploy solution**

Export solutions from the Pentaho Repository that is in the development or test environments, to the Pentaho Repository that is in the production environment.

| Task                                 | Do This                                                                                                                                                                 | Objective                                                                                                                                     |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Export and Import Pentaho Repository | <ul><li>See <strong>Export and Import Pentaho Repository Content</strong> in the <strong>Administer Pentaho Data Integration and Analytics</strong> document.</li></ul> | <ul><li>Export Pentaho Repository content from test environment</li><li>Import Pentaho Repository content to production environment</li></ul> |

**Tune solution**

Fine tune transformations and jobs to optimize performance. This involves using various tools such as the DI Operations and Audit Marts to determine where bottlenecks or other performance issues occur, and attempting to address them.

| Task                                                                                 | Do This                                                                                                                                                                                                                                                                                               | Objective                                                                                                                     |
| ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Review the Performance Tuning Checklist and Make Changes to Transformations and Jobs | <ul><li>Consult the tuning tips. See the <strong>Administer Pentaho Data Integration and Analytics</strong> document for tuning tips.</li></ul>                                                                                                                                                       | <ul><li>Get familiar with things that you can do to optimize performance.</li><li>Apply tuning tips as needed.</li></ul>      |
| Consider other performance tuning options                                            | <ul><li>Learn about transactional databases. See the <strong>Pentaho Data Integration</strong> document for details on transactional databases.</li><li>Learn about using logs. See the <strong>Administer Pentaho Data Integration and Analytics</strong> document for details on logging.</li></ul> | <ul><li>Learn how to apply transactional databases.</li><li>Learn how to use logs to tune transformations and jobs.</li></ul> |

**Schedule runs**

Use the PDI client, Pan, or Kitchen to schedule executions of transformations and jobs.

| Task                                           | Do This                                                                                                                                                                                                                             | Objective                                                                   |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Schedule Transformations and Jobs From Spoon   | <ul><li>Schedule transformations and jobs. See the <strong>Pentaho Data Integration</strong> document for details.</li></ul>                                                                                                        | <ul><li>Schedule transformations and jobs</li></ul>                         |
| Command Line Scripting Through Pan and Kitchen | <ul><li>Learn about Pan's options. See the <strong>Pentaho Data Integration</strong> document for details.</li><li>Learn about Kitchen's options. See the <strong>Pentaho Data Integration</strong> document for details.</li></ul> | <ul><li>Use Pan and Kitchen to schedule transformations and jobs.</li></ul> |

**Next steps**

These resources will be helpful to you after your production server is live.

* Fine-tune Pentaho systems: Provides guidance on how to maintain and fine-tune your Pentaho Server. See the **Administer Pentaho Data Integration and Analytics** document for details.
* Pentaho [Training and Education](https://www.hitachivantara.com/en-us/services/training-certification.html)
* [Support Portal](https://support.pentaho.com/hc/en-us): Check with support for service packs.

#### Commonly used PDI steps and entries

Although there are over 330 transformation steps and job entries, some steps and entries are used more often than others. If you are creating a transformation and job, but do not know where to begin, this list might be helpful to you.

**Top ten transformation steps**

PDI transformation steps are documented in Pentaho Data Integration.

* Text File Input
* Table Input
* Microsoft Excel Input
* Text File Output
* Table Output
* Microsoft Excel writer
* Select Values
* Filter Rows
* Group By
* Stream Lookup

**Other commonly used transformation steps**

PDI transformation steps are documented in Documentation

* INPUT: Generate Rows, Data Grid, Get Data from XML, CSV File Input, Fixed File Input
* OUTPUT: XML Output
* TRANSFORM: Split Fields, Calculator, Add Constants, Add Sequence, Replacing Strings, Split Fields, Sort Rows, String Operations, Strings Cut
* SCRIPTING: User Defined Java Class, Modified Java Script Value, User Defined Java Expression
* FLOW: Abort, Append Streams, Block this step until steps finish, Blocking Step, Detect Empty Stream, Dummy, ETL Metadata Injection, Filter Rows, Identify Last Row in a Stream, Java Filter, Job Executor, Prioritize Streams, Single Threader, Switch/Case, Transformation Executor
* LOOKUP
* JOINS: Join Rows, Merge Join
* JOB: Get Variables, Set Variables

**Commonly used job entries**

PDI job entries are documented in documentation.

* GENERAL: Start, Job, Transformation, Success
* UTILITY: Abort
* MAIL: Mail
* FILE MANAGEMENT: Add filenames to result, Compare folders, Convert file between Windows and Unix, Copy Files, Create a folder, Create file, Delete file, Delete filenames from result, Delete files, Delete folders, File Compare, HTTP, Move Files, Process result filenames, Unzip file, Wait for file, Write to file, Zip file
* UTILITIES: Write to log

### Pentaho Business Analytics workflow

Pentaho Business Analytics is a combined business analytics and data integration platform that allows business users, data scientists, and IT administrators to easily access, explore, and visualize their data. Pentaho empowers business users to make information-driven decisions that positively impact their organization’s performance, data scientists to use a full-spectrum of tools to create robust data models, and IT to rapidly deliver a secure, scalable, flexible, and easy to manage business analytics platform for the broadest set of users.

#### Workflow stages

Use these sections to move from evaluation to production:

* [Evaluate and learn Pentaho Business Analytics](#evaluate-and-learn-pentaho-business-analytics)
* [Develop your BA environment](#develop-your-ba-environment)
* [Go live for production - BA](#go-live-for-production---ba)

#### Evaluate and learn Pentaho Business Analytics

As you explore Pentaho Business Analytics, you will be introduced to the major components, watch videos, work through hands-on examples, and learn about the different features.

Go at your own pace. Feel free to dig into the documentation or to contact Pentaho [sales support](https://www.pentaho.com/services) if you have questions.

Use the sections below to get familiar with Business Analytics:

* [Tour the User Console and create your first reports](#tour-the-user-console-and-create-your-first-reports)
* [Explore and learn data source basics](#explore-and-learn-data-source-basics)
* [Learn about Report Designer](#learn-about-report-designer)
* [Discover more about Pentaho Business Analytics](#discover-more-about-pentaho-business-analytics)
* [Next steps](#next-steps-evaluation)

**Tour the User Console and create your first reports**

The User Console is a web-based design environment where you can analyze data, create interactive reports, dashboard reports, and build integrated dashboards to share business intelligence solutions with others in your organization and on the internet. In addition to its design features, the User Console offers a wide variety of system administration features for configuring the Pentaho Server, managing Pentaho licenses, setting up security, managing report scheduling, and tailoring system performance to meet your requirements.

If you have installed the trial download on your laptop or desktop machine, you are ready to get started exploring. If you have the software installed on a server, and want to use your machine to point to it, see [Develop your BA environment](#develop-your-ba-environment) for details.

| Lesson                                   | Do This                                                                                                                                                                                       | Notes                                                                                                                                               |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tour the User Console                    | [Quick tour of the Pentaho User Console](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/quick-tour-of-the-pentaho-user-console-puc)                                           | <ul><li>Understand the features of the User Console</li><li>View the sample reports on the Samples tab of the Getting Started section</li></ul>     |
| Create Your First Reports and Dashboards | [Getting Started with Analyzer, Interactive Reports, and Dashboard Designer](https://docs.pentaho.com/pdia-try-pdia/getting-started-with-analyzer-interactive-reports-and-dashboard-designer) | <ul><li>Created and saved an Interactive Report</li><li>Created and saved an Analysis Report</li><li>Created and saved a custom Dashboard</li></ul> |
| Schedule Your Report                     | <ul><li>Learn about scheduling reports. See the <strong>Pentaho Business Analytics</strong> document for details.</li></ul>                                                                   | <ul><li>Scheduled a report to run and email automatically.</li><li>Received your report through email after the schedule runs.</li></ul>            |

**Explore and learn data source basics**

If you have already worked with the Steel Wheels sample data and want to learn how to create your own data sources and data models with Pentaho, use the Data Source Wizard. The Data Source Wizard helps you define a data source that contains the data you want to use and guides you through the creation of your evaluation data model for use in creating reports.

After you define a data source, you can make it available to other evaluators so they can create reports and analysis by simply picking the data source from the data source list. Any number of reports can be created using a single data source.

| Lesson                                | Do This                                                                                                                                            | Notes                                                                                                                                                                                                                                                                      |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create Your First Data Source         | <ul><li>Create a Data Source</li><li>Tour the Data Source Wizard</li></ul><p>See <strong>Pentaho Business Analytics</strong> for instructions.</p> | <ul><li>Understand how the Pentaho Server and Data Source Wizard work together to create usable data sources and data models.</li><li>Explore the Data Source Wizard interface.</li><li>Learn the basics of creating a data source using the Data Source Wizard.</li></ul> |
| Choose Data Source Types              | <ul><li>Choose a data source type</li></ul><p>See <strong>Pentaho Business Analytics</strong> for instructions.</p>                                | <ul><li>Learn about the different data source types supported by the Data Source Wizard.</li></ul><p>We recommend using a CSV data source for evaluation.</p>                                                                                                              |
| Create Your First CSV Data Source     | <ul><li>Create a CSV data source</li></ul><p>See <strong>Pentaho Business Analytics</strong> for instructions.</p>                                 | <ul><li>Import a CSV data file using the Data Source Wizard.</li><li>Create the CSV data source.</li></ul><p>We recommend creating a report using this new CSV data source, then refining the data model with the Data Source Model Editor as needed.</p>                  |
| Refine Your Data Source Model         | <ul><li>Edit multidimensional data source models.</li></ul><p>See <strong>Pentaho Business Analytics</strong> for instructions.</p>                | (Optional) Edit your evaluation data source model using the Data Source Model Editor.                                                                                                                                                                                      |
| Inline Model Editing                  | <ul><li>Read <strong>Working with Analyzer measures</strong> in the <strong>Pentaho Business Analytics</strong> document.</li></ul>                | <ul><li>Learn how to edit your data models while working in Analyzer.</li></ul>                                                                                                                                                                                            |
| Learn about Streamlined Data Refinery | <ul><li>Learn how to work with Streamlined Data Refinery</li></ul><p>See <strong>Pentaho Data Integration</strong> for instructions.</p>           | <ul><li>Learn how Streamlined Data Refinery works.</li></ul>                                                                                                                                                                                                               |

**Learn about Report Designer**

Pentaho Report Designer is a report creation tool that you can use by itself, or as part of the Pentaho Suite. It allows professionals to create print-quality reports based on data from virtually any type of data source.

These resources in the **Pentaho Report Designer** document will help you get familiar with the Report Designer interface, and guide you through the creation and publishing of a print-quality report.

| Lesson                                | Section in document                                                       | Notes                                                                                                                            |
| ------------------------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Explore the Report Designer Interface | <ul><li><strong>Explore Report Designer</strong></li></ul>                | <ul><li>Tour the Report Designer interface before you begin building reports.</li></ul>                                          |
| Report Designer Workflow Overview     | <ul><li><strong>Learn about Report Designer workflow</strong></li></ul>   | <ul><li>Look over the workflow concepts for Report Designer.</li></ul>                                                           |
| Create Your First Report              | <ul><li><strong>Create your first print-quality report</strong></li></ul> | <ul><li>Create a report.</li><li>Add a chart and parameters to your report.</li><li>View and then publish your report.</li></ul> |
| Refine the Look of Your Report        | <ul><li><strong>Design print-quality reports</strong></li></ul>           | <ul><li>Explore more advanced features of Report Designer, beginning with report elements.</li></ul>                             |
| Add a PDI Data Source                 | <ul><li><strong>Add a PDI data source</strong></li></ul>                  | <ul><li>Add a PDI data source and use it to create a report in Report Designer.</li></ul>                                        |

**Discover more about Pentaho Business Analytics**

* The Pentaho Analyzer, Interactive Reports, and Dashboard Designer plugins provide in-depth details about creating eye-catching business intelligence deliverables for your user community. See the **Pentaho Business Analytics** document for details.
* If you are a system administrator, check out the **Install Pentaho Data Integration and Analytics** document. Both have details on configuring and administering your Pentaho Server using the User Console, as well as a section on the variety of things you can do to maintain your server manually.

**Next steps (evaluation)**

* Contact [Pentaho](https://www.pentaho.com/helpmeout) to learn more about how Business Analytics can be tailored to meet your business needs.
* Continue with [Develop your BA environment](#develop-your-ba-environment).

#### Develop your BA environment

This workflow outlines how to set up a Pentaho Server for BA development. It also covers how to build, refine, and test BA content.

This workflow is similar to the Trial Download Evaluation experience. The difference is you configure the server fully. You also work with your own report designers and data scientists. You can also engage Pentaho [professional services](https://www.hitachivantara.com/en-us/services/big-data-analytics-services.html).

Before you start, consider Pentaho [training classes](https://www.hitachivantara.com/en-us/services/training-certification.html). Training helps you install and configure the server. Training also helps you build data models and BA applications.

**Set up your Pentaho Server**

Use this checklist to verify requirements. Then install and configure the Pentaho Server and BA design tools.

**Verify system requirements**

* Review required components in [Components Reference](https://docs.pentaho.com/pdia-try-pdia/components-reference).
* Review required drivers in [JDBC drivers reference](https://docs.pentaho.com/pdia-try-pdia/jdbc-drivers-reference).
* Acquire one or more servers that meet requirements.
* Obtain the correct drivers for your system.

**Obtain software and install the Pentaho Server**

* Download the Pentaho software from your Sales Support representative.
* Install the software using [Install the 30-day trial of Pentaho Data Integration and Analytics](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/pentaho-evaluation).
* Sign in using [Quick tour of the Pentaho User Console](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/quick-tour-of-the-pentaho-user-console-puc).
* Tour **Administration**.
* Change the default administrator password.

**Change the Pentaho Server fully qualified URL**

* Follow **Administer Pentaho Data Integration and Analytics** instructions to change the server URL.
* If multiple machines point to one server, confirm all clients use the new URL.

**Configure the Pentaho Server**

* Manage licenses. See **Administer Pentaho Data Integration and Analytics**.
* Configure server data connections. See **Install Pentaho Data Integration and Analytics**.
* Configure email for scheduled reports. See **Pentaho Business Analytics**.
* Review schedule management. See **Pentaho Business Analytics**.

**Configure BA design tools**

Do this only on a development system. Do not configure design tools on your production server.

* Configure design tools and utilities. See **Install Pentaho Data Integration and Analytics**.
* Configure each tool’s data connections. See **Install Pentaho Data Integration and Analytics**.

**Import data sources and data models**

Create data sources and models that support agile BA development.

**Choose data source types**

* Choose a data source type. See **Pentaho Business Analytics**.
* Review relational versus multidimensional models.

**Create data sources and models**

* Tour the Data Source Wizard. See **Pentaho Business Analytics**.
* Learn how the server and wizard produce usable sources and models.

**Create database table data sources**

* Create a database table source. See **Pentaho Business Analytics**.
* Create initial data sources and preliminary models.

**Learn about Mondrian schemas**

* Create and modify Mondrian schemas. See **Pentaho Schema Workbench**.
* Add a Mondrian data source.
* Adapt the schema for Analyzer.
* Refine the schema in Schema Workbench.

**Create reports and further refine data models**

Work with data scientists and business analysts at this stage. This improves the quality of models and reports.

As you prepare to move to production, use data sources from:

* Pentaho Schema Workbench
* Pentaho Metadata Editor

**Create Analyzer reports, Interactive reports, and dashboards**

* Follow **Pentaho Business Analytics** instructions.
* Create Interactive and Analyzer reports.
* Create a dashboard.
* Verify results match what you need.
* If needed, refine models with your data team.

**Create a report with Report Designer (optional)**

* Follow **Pentaho Report Designer** instructions.

**Refine your data source model**

* Edit multidimensional models. See **Pentaho Business Analytics**.
* Refine Mondrian schemas. See **Pentaho Schema Workbench**.
* Refine relational models. See **Pentaho Metadata Editor**.
* Recreate reports to validate changes.
* Repeat until results meet requirements.

**Test environment quality**

If you do quality assurance testing, upload content to the Pentaho Repository. Then download it to the QA server. See **Administer Pentaho Data Integration and Analytics** for details.

Some organizations also run user acceptance testing after QA.

**Next steps (development)**

* Investigate security. See **Administer Pentaho Data Integration and Analytics**.
* Plan scheduling for production. See **Pentaho Business Analytics**.
* Decide what content to promote to production. See **Administer Pentaho Data Integration and Analytics**.
* Check the [Support Portal](https://support.pentaho.com/hc/en-us) for service packs.
* Prepare to [Go live for production - BA](#go-live-for-production---ba).

#### Go live for production - BA

This section explains how to move Pentaho content and server settings between servers.

This process usually uses two or three servers with identical configurations:

* BA content development
* Testing and QA (optional)
* Production

We recommend working with Pentaho [professional services](https://www.pentaho.com/services) during production deployment.

**Prepare for going live**

This section has two parts:

* A checklist for setting up a Pentaho Server
* Prerequisites to complete before you go live

If your production server is already set up, start with the prerequisites.

**Pentaho Server setup checklist**

| Task                                           | Do this                                                                                                                                                                                                                                                                                                        | Notes                                                                                                                                                                                                                                                              |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Verify system requirements                     | <p>Consult:<br>- <a href="components-reference">Components Reference</a><br>- <a href="jdbc-drivers-reference">JDBC drivers reference</a></p>                                                                                                                                                                  | <p>- Acquire one or more servers that meet requirements.<br>- Obtain the correct drivers.</p>                                                                                                                                                                      |
| Obtain software and install the Pentaho Server | <p>- Install Pentaho Suite. See <strong>Install Pentaho Data Integration and Analytics</strong>.<br>- Download and install the latest service pack. See <strong>Administer Pentaho Data Integration and Analytics</strong>.<br>- Access the User Console. See <strong>Pentaho Business Analytics</strong>.</p> | <p>- Install the software.<br>- Install the latest service pack.<br>- Access the User Console, review <strong>Administration</strong>, and change the default administrator password.<br><br>If needed, change the fully qualified URL for the Pentaho Server.</p> |
| Change the server fully qualified URL          | Change the Pentaho Server fully qualified URL if needed. See **Administer Pentaho Data Integration and Analytics**.                                                                                                                                                                                            | If many machines point to one server, change the URL and verify connectivity.                                                                                                                                                                                      |
| Configure the server                           | <p>- Manage licenses. See <strong>Administer Pentaho Data Integration and Analytics</strong>.<br>- Specify data connections. See <strong>Install Pentaho Data Integration and Analytics</strong>.<br>- Set up email for scheduled reports. See <strong>Pentaho Business Analytics</strong>.</p>                | <p>- Set up data connections.<br>- Configure email through <strong>Administration</strong>.</p>                                                                                                                                                                    |

**Prerequisites before you go live**

| Task                        | Do this                                                                                                                                                                                                                                                                                                  | Notes                                                                                                                                           |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Compare configuration files | <p>- Compare server configuration files.<br>- Verify and increase memory settings. See <strong>Administer Pentaho Data Integration and Analytics</strong>.</p>                                                                                                                                           | <p>- Identify configuration differences.<br>- Commit a unified properties file to version control.<br>- Increase memory settings as needed.</p> |
| Verify data sources         | <p>- Specify data connections. See <strong>Install Pentaho Data Integration and Analytics</strong>.<br>- Define JNDI connections. See <strong>Install Pentaho Data Integration and Analytics</strong>.</p>                                                                                               | <p>- Confirm data sources can be promoted.<br>- Establish JNDI sources as replacements if needed.</p>                                           |
| Define security             | <p>- Define Pentaho Server security. See <strong>Administer Pentaho Data Integration and Analytics</strong>.<br>- Manage users and roles. See <strong>Pentaho Business Analytics</strong>.<br>- Implement advanced security. See <strong>Administer Pentaho Data Integration and Analytics</strong>.</p> | <p>- Implement security.<br>- Define users, roles, and permissions.</p>                                                                         |
| Upload content              | Upload and download from the Pentaho Repository. See **Administer Pentaho Data Integration and Analytics**.                                                                                                                                                                                              | - Upload files and folders.                                                                                                                     |

**Compare configuration files**

The most important server configuration settings are stored in the `/server/pentaho-server/pentaho-solutions/system/` directory.

Some core settings are also inside the Pentaho WAR archive deployed to your application server. These settings should not change after initial setup.

{% hint style="warning" %}
Do not change the names of content files, data sources, solution directories, or other file names during promotion.

Set names during solution development. Keep names consistent through promotion.

Renaming can cause issues that you will not detect immediately. This can break QA and production content.
{% endhint %}

To ensure you selected all server configuration files, compare these directories in full:

* `/pentaho-solutions/system/`
* `/WEB-INF/` inside your deployed `pentaho.war`
* `/META-INF/` inside your deployed `pentaho.war`

{% hint style="info" %}
Plugin directories for Analyzer, Dashboard Designer, Interactive Reports, and Community Dashboard Framework include binaries.

Binary differences usually indicate version differences. Focus on XML and properties files.

If you customized plugins, promote those changes too.
{% endhint %}

**Move content to production server**

This checklist summarizes best practices to promote Pentaho Server settings, data sources, and content.

Before you promote from development to production, complete the preparation and prerequisite tasks earlier in this page.

| Task                                | Do this                                                                       | Notes                                                                                                                                               |
| ----------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Download content                    | - Upload and download from the Pentaho Repository.                            | <p>- Move all desired content to production.<br>- See <strong>Administer Pentaho Data Integration and Analytics</strong> for details.</p>           |
| Set up schedules and blockout times | <p>- Manage schedules.<br>- Prevent scheduling by setting blockout times.</p> | <p>- Set up production schedules.<br>- Set up blockout times for maintenance.<br>- See <strong>Pentaho Business Analytics</strong> for details.</p> |

**Next steps (production)**

These resources are helpful after your production server is live:

* See **Administer Pentaho Data Integration and Analytics** for guidance on maintenance and tuning.
* Pentaho [Training and Education](https://www.hitachivantara.com/en-us/services/training-certification.html)
* [Support Portal](https://support.pentaho.com/hc/en-us) for service packs


# Components reference

Pentaho aims to accommodate diverse computing environments. This list provides details about the environment components and versions we support. Where applicable, versions are listed as certified or supported:

* **Certified**

  The version has been tested and validated for compatibility with Pentaho.
* **Supported**

  Support is available for listed non-certified versions.

If you have questions about your particular computing environment, contact [Pentaho Support](https://support.pentaho.com/).

### Server operating system

The Pentaho Server is hardware-independent and runs on server-class computers.

Your server-class computer must comply with the specifications for minimum hardware and required operating systems:

| Hardware                                                                                                                                                                                                                                         | Certified Operating System - 64 bit                                                                            | Supported Operating System - 64 bit                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| <p><strong>Processor</strong></p><p>Intel EM64T or AMD64 Dual-Core or later</p><p></p><p><strong>RAM</strong></p><p>8 GB with 4 GB dedicated to Pentaho servers</p><p></p><p><strong>Disk Space</strong></p><p>20 GB free after installation</p> | <ul><li>Microsoft Windows 2025 Server</li><li>Red Hat Enterprise 9\*</li><li>Ubuntu Server 22.04 LTS</li></ul> | <p></p><ul><li>Microsoft Windows 2022 Server</li><li>Red Hat Enterprise 8\*</li></ul> |

\*Pentaho Data Integration and Analytics is supported on any Linux distribution binary-compatible with RHEL 9 and Ubuntu Server 22, including in virtualized and cloud environments. If you have any questions, contact [Pentaho Support](https://support.pentaho.com/).

{% hint style="info" %}
**Note:** Mac servers are not supported as an operating system.
{% endhint %}

### Container deployment

Supported technology for deploying Pentaho in containers.

<table><thead><tr><th width="164.99993896484375">Technology</th><th>Certified</th></tr></thead><tbody><tr><td>Docker</td><td>27.5.1</td></tr></tbody></table>

{% hint style="info" %}
**Note:** Kubernetes environments that use this Docker version are also supported.
{% endhint %}

You can also deploy pre-configured Docker images of specific Pentaho products in your AWS environments. See [Docker container deployment of Pentaho Server](https://app.gitbook.com/s/qfaQ2p0JAZrP8b3cpM9a/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-server) and [Docker container deployment of Carte, Pan, and Kitchen](https://app.gitbook.com/s/qfaQ2p0JAZrP8b3cpM9a/pentaho-installation-overview-cp/docker-container-deployment-of-carte-pan-and-kitchen) for details.

### Workstation operating system

These Pentaho design tools are hardware-independent and run on client-class computers that comply with these specifications for minimum hardware and required operation systems.

* Pentaho Aggregation Designer
* Pentaho Data Integration
* Pentaho Metadata Editor
* Pentaho Report Designer
* Pentaho Schema Workbench

| Hardware - 64 bit                                                                                                                                                                                                                                                                                                                                                                                                                       | Certified Operating System - 64 bit                                                            | Supported Operating System - 64 bit |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------- |
| <p><strong>Processors</strong></p><ul><li>Apple Macintosh Dual-Core</li><li>Apple Mac M1, M2, and M3 chipset</li><li>Intel EM64T or AMD64 Dual-Core or later</li></ul><p></p><p><strong>RAM</strong></p><p>2 GB RAM for most of the design tools, PDI requires 2 GB dedicated</p><p></p><p><strong>Disk Space</strong></p><p>2 GB free after installation</p><p></p><p><strong>Minimum Screen Size</strong></p><p>1280 x 960 pixels</p> | <ul><li>Ubuntu Desktop 22.04</li><li>Microsoft Windows 11</li><li>macOS 15 (Sequioa)</li></ul> | <ul><li>macOS 14 (Sonoma)</li></ul> |

{% hint style="info" %}
**Note:** Ubuntu Linux requires \`libwebkitgtk-1.0\`. See **Install Pentaho Data Integration and Analytics** for more information.
{% endhint %}

#### Embedded software <a href="#embedded-software" id="embedded-software"></a>

When embedding Pentaho software into other applications, the computing environment should comply with these specifications for minimum hardware and required operation systems.

* Embedded Pentaho Reporting
* Embedded Pentaho Analysis
* Embedded Pentaho Data Integration

{% hint style="info" %}
**Note:** Pentaho Data Integration and Analytics is officially certified to run on the Red Hat Enterprise and Ubuntu Linux distributions. It is compatible with any binary-compatible Linux distribution that meets the necessary software and hardware requirements, including in virtualized and cloud environments. If you have any questions, contact [Pentaho Support](https://support.pentaho.com/). The following specifications comply with minimum hardware and required operating systems for embedding Pentaho reporting, analysis, and data integration:
{% endhint %}

| Hardware—64 bit                                                                                                                                                                                                                                             | Certified Operating System—64 bit                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| <ul><li><strong>Processors</strong></li></ul><p>Intel EM64T or AMD64 Dual-Core</p><ul><li><strong>RAM</strong></li></ul><p>8 GB with 4 GB dedicated to Pentaho servers</p><ul><li><strong>Disk Space</strong></li></ul><p>20 GB free after installation</p> | <ul><li>Microsoft Windows 2022 Server</li><li>Red Hat Enterprise 9</li><li>Ubuntu Server 22.04 LTS</li></ul> |

### Application servers

The server to which you deploy Pentaho software must run the following application server:

* Tomcat 10.1.48 (Certified)

### Solution database repositories

Pentaho software stores processing artifacts in these database repositories:

<table><thead><tr><th width="165.99993896484375">Repository</th><th width="131">Certified</th><th width="280.00006103515625">Supported</th></tr></thead><tbody><tr><td>PostgreSQL</td><td>16</td><td>15</td></tr><tr><td>MySQL</td><td>8.4</td><td></td></tr><tr><td>Oracle</td><td>23c &#x26; 23ai</td><td></td></tr><tr><td>MS SQL Server</td><td>2022</td><td>2019 (including patched versions)</td></tr><tr><td>Maria DB</td><td>11.4</td><td></td></tr></tbody></table>

\* The default installed solution database.

#### Apache Hadoop vendors <a href="#apache-hadoop-vendors" id="apache-hadoop-vendors"></a>

Pentaho software has certified or supported data sources from these Hadoop Vendors.

| Vendor                                     | Driver Version |
| ------------------------------------------ | -------------- |
| Amazon EMR                                 | 7.7.0          |
| Cloudera Data Platform (CDP) Private Cloud | 7.1.x, 7.3.1   |

#### Data Sources: Pentaho Tools

This table summarizes which data sources are compatible with the main Pentaho tools.

<table><thead><tr><th width="372">Pentaho Software</th><th>Data Source</th></tr></thead><tbody><tr><td>Pentaho Reporting</td><td><ul><li>JDBC 3/4<sup>1</sup></li><li>ODBC</li><li>OLAP4J</li><li>XML</li><li>Pentaho Analysis</li><li>Pentaho Data Integration</li><li>Pentaho Metadata</li><li>Scriptable</li><li>Snowflake</li></ul></td></tr><tr><td>Pentaho Server, Action Sequences</td><td><ul><li>Relational (JDBC)</li><li>Hibernate</li><li>Javascript</li><li>Metadata (MQL)</li><li>Mondrian (MDX)</li><li>XML (XQuery)</li><li>Security User/Role List Provider</li><li>Snowflake</li><li>Data Integration Steps (PDI)</li><li>Other Action Sequences</li><li>Web Services</li><li>XMLA</li></ul></td></tr><tr><td>Pentaho Data Integration</td><td><ul><li>JDBC 3/4<sup>1</sup></li><li>OLAP4J</li><li>Salesforce</li><li>Snowflake</li><li>XML</li><li>CSV</li><li>Microsoft Excel</li></ul></td></tr></tbody></table>

<sup>1</sup> Use a JDBC 3.x or 4.x compliant driver that is compatible with SQL-92 standards when communicating with relational data sources. For a list of drivers to use with relational JDBC databases, see the [JDBC drivers reference](https://docs.pentaho.com/pdia-try-pdia/jdbc-drivers-reference).

### Big Data Sources: General

Pentaho software supports the following Big Data sources. Check this list if you are evaluating Pentaho or checking for general compatibility with a specific vendor.

| Data Source                                              | Certified | Supported |
| -------------------------------------------------------- | --------- | --------- |
| Amazon EMR (via Hive)                                    | 7.7.0     |           |
| Cassandra (Datastax)                                     | 6.8       |           |
| Cloudera Data Platform (CDP) on premises (private cloud) | 7.1.9     |           |
| Google BigQuery (Simba)                                  | 1.6.2     | 1.2.25    |
| MongoDB                                                  | 7.0       |           |
| Vertica<sup>\*</sup>                                     | 24        |           |

<sup>\*</sup> Deprecated beginning in version 11.0.

### Big Data Sources: Details

This table shows the Big Data sources that are compatible with specific Pentaho tools.

<table data-full-width="false"><thead><tr><th width="126">Data Source</th><th width="115">Versions</th><th width="107.00006103515625">Analyzer</th><th width="108">PIR/PDD</th><th width="116.0001220703125">Pentaho Reporting</th><th width="85">DSW</th><th width="156">PDIServer/Client</th><th width="95.00006103515625">PRD</th><th width="69.99993896484375">PSW</th><th>PME</th></tr></thead><tbody><tr><td>Amazon EMR</td><td>7.7.0<sup>1</sup> (Certified)</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Cassandra (Datastax)</td><td>6.8 (Certified)</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Cloudera Data Platform (CDP) Private Cloud</td><td>7.1.9 (for job execution)</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Cloudera Data Platform (CDP) Private Cloud</td><td><a href="#support-statement-for-analyzer-on-impala">via Impala</a> (as data source)</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Cloudera Data Platform (CDP) Private Cloud</td><td>via Hive3<sup>2</sup> (as data source)</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td><a href="#google-bigquery">Google BigQuery</a></td><td>1.5.4.1008<sup>3</sup></td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>MongoDB</td><td>7</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Vertica<sup>4</sup></td><td>11</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></tbody></table>

<sup>1</sup> EMR clusters (version 7.x and later) built with JDK 17 exclude the `commons-lang-2.6.jar` library from their standard Hadoop library directories (`$HADOOP_HOME/lib`). To use the EMR driver for EMR 7.x, obtain the `commons-lang-2.6.jar` file from a trusted source, such as the official Maven repository ([Maven Repository: commons-lang » commons-lang » 2.6](https://mvnrepository.com/artifact/commons-lang/commons-lang/2.6)). Then manually copy the downloaded JAR file to the `$HADOOP_HOME/lib` or `$HADOOP_MAPRED_HOME/lib` directory on each node within the EMR cluster to ensure that all worker nodes have access to the library.

<sup>2</sup> Hive3 as a data source for CDP also supports Hive LLAP, and Hive3 on Tez.

<sup>3</sup> The Simba driver required for Google BigQuery is the JDBC 4.2-compatible version, which you can download from <https://storage.googleapis.com/simba-bq-release/jdbc/SimbaJDBCDriverforGoogleBigQuery42_1.2.2.1004.zip>.

<sup>4</sup> Deprecated beginning in version 11.0.

{% hint style="info" %}
**Note:** A generic Apache Hadoop driver is included in the Pentaho distribution for version 11.0. Other supported drivers can be downloaded from the [Support Portal](https://support.pentaho.com/hc/en-us).
{% endhint %}

### SQL Dialect-Specific

Pentaho software generates dialect-specific SQL when communicating with these data sources. Certified indicates the SQL dialect has been tested for compatibility with Pentaho.

| Pentaho Software         | Data Source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pentaho Analyzer         | <p>Certified</p><ul><li>Amazon Redshift</li><li>Azure SQL</li><li>Impala</li><li>MySQL</li><li>Microsoft SQL Server</li><li>Oracle</li><li>PostgreSQL</li><li>Snowflake</li></ul><p>Supported</p><ul><li>Access</li><li>Firebird</li><li>Hsqldb</li><li>IBM DB2</li><li>IBM MQ 9.2</li><li>Informix</li><li>Ingres<sup>1</sup></li><li>Interbase<sup>1</sup></li><li>Neoview<sup>1</sup></li><li>SqlStream</li><li>Sybase<sup>1</sup></li><li>Vectorwise<sup>1</sup></li><li>Vertica<sup>1</sup></li><li>Other SQL-89 compliant<sup>2</sup></li></ul>                                                                                                                                                                         |
| Pentaho Metadata         | <p>Certified</p><ul><li>Azure SQL</li><li>Hive 2</li><li>Impala</li><li>MySQL</li><li>PostgreSQL</li></ul><p>Supported</p><ul><li>Amazon Redshift</li><li>ASSQL</li><li>Firebird</li><li>H2</li><li>Hypersonic</li><li>IBM DB2</li><li>IBM MQ 9.2</li><li>Ingres<sup>1</sup></li><li>Interbase<sup>1</sup></li><li>MS Access</li><li>MS SQL Server (JTDS Driver)</li><li>MS SQL Server (Microsoft Driver)</li><li>Snowflake</li><li>Sybase<sup>1</sup></li><li>Vertica<sup>1</sup></li><li>Other SQL-92 compliant<sup>2</sup></li></ul>                                                                                                                                                                                       |
| Pentaho Data Integration | <p>Certified</p><ul><li>Amazon Redshift</li><li>Azure SQL</li><li>Hive<sup>1</sup></li><li>Hive 2</li><li>Impala</li><li>MS SQL Server (JTDS Driver)</li><li>MS SQL Server (Microsoft Driver)</li><li>MySQL</li><li>Oracle</li><li>PostgreSQL</li><li>Snowflake</li><li>Vertica<sup>1</sup></li></ul><p>Supported</p><ul><li>AS/400</li><li>InfiniDB<sup>1</sup></li><li>Exasol 4</li><li>Firebird SQL</li><li>H2</li><li>Hypersonic</li><li>IBM DB2</li><li>IBM MQ 9.2</li><li>Informix</li><li>Ingres<sup>1</sup></li><li>Ingres VectorWise<sup>1</sup></li><li>MaxDB (SAP DB)</li><li>Neoview<sup>1</sup></li><li>Oracle RDB</li><li>SQLite</li><li>UniVerse database</li><li>Other SQL-92 compliant<sup>2</sup></li></ul> |

<sup>1</sup> Deprecated beginning in version 11.0.

<sup>2</sup> If your data source is not in this list and is compatible with SQL-92, Pentaho software uses a generic SQL dialect.

### Security

Pentaho software integrates with these third-party security authentication systems:

* CAS 7 (Certified)
* Integrated Windows Authentication with Internet Information Services 10 (Certified)
* Spring 6.2.12 (Certified)

### Java virtual machine

Pentaho software requirements for Java Runtime Environment (JRE).

| Pentaho Software     | Certified                                                  | Supported                                                  |
| -------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| All Pentaho software | <ul><li>Oracle Java 21</li><li>Oracle OpenJDK 21</li></ul> | <ul><li>Oracle Java 17</li><li>Oracle OpenJDK 17</li></ul> |

{% hint style="info" %}
**Note:** The PDI client requires at least Java 11.x to run on Windows 11.
{% endhint %}

### Web browsers

Pentaho supports major versions of web browsers that are publicly available six weeks before the finalization of a Pentaho release.

| Certified Browsers                                                                                                                          | Supported Browsers                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p></p><ul><li>Apple Safari 26.1 (On macOS only)</li><li>Google Chrome 142</li><li>Microsoft Edge 142</li><li>Mozilla Firefox 144</li></ul> | <p></p><ul><li>Apple Safari 26.1 and later (On macOS only)</li><li>Google Chrome 142 and later</li><li>Microsoft Edge 142 and later</li><li>Mozilla Firefox 144 and later</li></ul> |

### Support Statement for Analyzer on Impala

These are the minimum requirements for Analyzer to work with Impala:

* Pentaho 7.1 or later
* Impala 1.3.x or later
* Recommend using Parquet compressed file format for tables in Impala
* Make sure that the JDBC driver is dropped into the Pentaho Server and Schema Workbench directories. See the **Install Pentaho Data Integration and Analytics** document for details.
* Turn off connection pooling in Pentaho Server.
* In Mondrian schemas, divide dimension tables with high cardinality into several levels

**Note:** As with any data source, the performance of Pentaho Analyzer on Impala will be dependent upon the data shape, Impala’s configuration, and the types of queries. See the best practice, "Pentaho Analyzer with Impala as a Data Source" located at: [https://support.pentaho.com/hc/en-us/articles/208652846](https://support.pentaho.com/hc/en-us/articles/360002913871-Big-Data-and-Pentaho) or download the [PDF](https://support.pentaho.com/hc/en-us/article_attachments/360012191711/Pentaho_Analyzer_and_Impala_Data_Source_Settings_and_Recommendations.pdf).

There are some compiled Mondrian automated test suite results for Analyzer on Impala with OEM Simba, as well as the community Apache Hive driver:

* [Analyzer on Impala with OEM Simba](http://wiki.pentaho.com/display/analysis/PA_CR_PA-3.7.0.0-752_impalad-1.3.0_simba-2.5.2)
* [Analyzer on Impala with community Apache Hive driver](http://wiki.pentaho.com/display/analysis/PA_CR_PA-3.7.0.0-752_impalad-1.3.0)

### Google BigQuery

You can use Google BigQuery as a data source with the Pentaho User Console or with the PDI client.

Before you begin, you must have a Google account and must create service account credentials in the form of a key file in JSON format to connect to Google BigQuery. To create service account credentials, see the [Google Cloud Storage Authentication documentation](https://cloud.google.com/storage/docs/authentication).

Additionally, you must set permissions for your BigQuery and Google Cloud accounts. To configure your service account authentication, see the [Google Service Account documentation](https://www.simba.com/products/BigQuery/doc/v1/JDBC_InstallGuide/content/jdbc/bq/authenticating/serviceaccount.htm).

Perform the following steps to create a JDBC connection to a Google BigQuery data source from the User Console or PDI client.

1. Stop the Pentaho Server.
2. Download the ZIP file containing the Simba version 1.5.4.1008 JDBC 4.2 driver for Google BigQuery from <https://storage.googleapis.com/simba-bq-release/jdbc/SimbaJDBCDriverforGoogleBigQuery42_1.2.2.1004.zip>.
3. Navigate to the `server/pentaho-server/tomcat/webapps/pentaho/WEB-INF/lib` directory for the User Console or the `design-tools/data-integration/lib` directory for the PDI client and delete any files associated with previous versions of Google BigQuery.

   Visually verify each file to ensure the older version is deleted.
4. Extract the following files to the `server/pentaho-server/tomcat/webapps/pentaho/WEB-INF/lib` folder for the User Console or the `design-tools/data-integration/lib` directory for the PDI client.
   * `animal-sniffer-annotations-1.14.jar`
   * `api-common-1.7.0.jar`
   * `avro-1.9.0.jar`
   * `checker-compat-qual-2.5.2.jar`
   * `error_prone_annotations-2.1.3.jar`
   * `gax-1.42.0.jar`
   * `gax-grpc-1.42.0.jar`
   * `google-api-client-1.28.0.jar`
   * `google-api-services-bigquery-v2-rev426-1.25.0.jar`
   * `google-auth-library-credentials-0.15.0.jar`
   * `google-auth-library-oauth2-http-0.13.0.jar`
   * `GoogleBigQueryJDBC42.jar`
   * `google-cloud-bigquerystorage-0.85.0-alpha.jar`
   * `google-cloud-core-1.67.0.jar`
   * `google-cloud-core-grpc-1.67.0.jar`
   * `google-http-client-1.29.0.jar`
   * `google-http-client-apache-2.0.0.jar`
   * `google-http-client-jackson2-1.28.0.jar`
   * `google-oauth-client-1.28.0.jar`
   * `grpc-alts-1.18.0.jar`
   * `grpc-auth-1.18.0.jar`
   * `grpc-context-1.18.0.jar`
   * `grpc-core-1.18.0.jar`
   * `grpc-google-cloud-bigquerystorage-v1beta1-0.50.0.jar`
   * `grpc-grpclb-1.18.0.jar`
   * `grpc-netty-shaded-1.18.0.jar`
   * `grpc-protobuf-1.18.0.jar`
   * `grpc-protobuf-lite-1.18.0.jar`
   * `grpc-stub-1.18.0.jar`
   * `gson-2.7.jar`
   * `j2objc-annotations-1.1.jar`
   * `javax.annotation-api-1.3.2.jar`
   * `jsr305-3.0.2.jar`
   * `opencensus-api-0.18.0.jar`
   * `opencensus-contrib-grpc-metrics-0.18.0.jar`
   * `opencensus-contrib-http-util-0.18.0.jar`
   * `protobuf-java-3.7.0.jar`
   * `protobuf-java-util-3.7.0.jar`
   * `proto-google-cloud-bigquerystorage-v1beta1-0.50.0.jar`
   * `proto-google-common-protos-1.15.0.jar`
   * `proto-google-iam-v1-0.12.0.jar`
   * `threetenbp-1.3.3.jar`**Note:** The Google BigQuery connection name does not display in the User Console Database Connection dialog box until you copy these files.
5. Restart the Pentaho Server.
6. Log on to the User Console or the PDI client, then open the Database Connection dialog box.

   See the **Install Pentaho Data Integration and Analytics** document for more information on the Database Connection dialog box.
7. In the Database Connection dialog box, select **General**, then select **Google BigQuery** as the **Database Type**.
8. In the **Settings** area, enter the information for your Google BigQuery account.
   * The **Host Name** is the URL to Google's BigQuery web services API. For example, <https://www.googleapis.com/bigquery/v2>
   * The **Project ID** in the PDI client and the **Database name** in the User Console are identical.
   * The **Port Number** is `443`.
9. Click **Options**, then add the following parameters and values.

   | Parameter                 | Value                                                                                                                  |
   | ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
   | **OAuthType**             | `0` (Zero)                                                                                                             |
   | **OAuthServiceAcctEmail** | Specify your service account email address.                                                                            |
   | **OAuthPvtKeyPath**       | Specify the path to your private key credential file.                                                                  |
   | **Timeout**               | Specify the amount of time, in seconds, before the server closes the connection. The recommended value is 120 seconds. |
10. Click **Test** to verify that you can connect to your data.


# JDBC drivers reference

{% hint style="warning" %}
This reference will be removed from the product.\
For JDBC driver questions, contact your database vendor or the [Support Portal](https://support.pentaho.com).
{% endhint %}

This reference can change.\
Report issues using the [Support Portal](https://support.pentaho.com).

## JDBC driver download links

| Database                                  | Vendor                              | URL                                                                              |
| ----------------------------------------- | ----------------------------------- | -------------------------------------------------------------------------------- |
| Amazon Redshift                           | Amazon                              | <http://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html> |
| AWS Aurora                                | Amazon                              | Aurora is MySQL- and PostgreSQL-compatible. Use the MySQL or PostgreSQL driver.  |
| AWS Athena                                | Amazon Web Services                 | <https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver.html>               |
| Caché<sup>1</sup>                         | InterSystems                        | <http://www.cachemonitor.de/intersystems-documentation/cache-jdbc-driver>        |
| CUBRID                                    | CUBRID                              | <http://www.cubrid.org/?mid=downloads&item=jdbc_driver>                          |
| Daffodil DB                               | Daffodil Software                   | <http://sourceforge.net/projects/daffodildb/>                                    |
| DB2 AS/400                                | IBM                                 | <https://www-03.ibm.com/systems/power/software/i/toolbox/downloads.html>         |
| DB2 Universal Database                    | IBM                                 | <http://www-01.ibm.com/support/docview.wss?uid=swg21363866>                      |
| Firebird                                  | Firebird Foundation                 | <http://www.firebirdsql.org/en/jdbc-driver/>                                     |
| FrontBase                                 | FrontBase                           | <http://www.frontbase.com/cgi-bin/WebObjects/FBWebSite>                          |
| Google BigQuery                           | Google BigQuery                     | <https://cloud.google.com/bigquery>                                              |
| Greenplum                                 | EMC2                                | <http://jdbc.postgresql.org/download.html>                                       |
| H2 Database                               | H2                                  | [http://www.h2database.com](http://www.h2database.com/)                          |
| Hive<sup>1</sup>                          | Apache                              | <http://hive.apache.org/>                                                        |
| Hive2                                     | Apache                              | <http://hive.apache.org/>                                                        |
| HSQLDB                                    | HyperSQL                            | <http://sourceforge.net/projects/hsqldb/>                                        |
| Impala                                    | Cloudera                            | <https://www.cloudera.com/documentation.html>                                    |
| Informix                                  | IBM                                 | <https://www-01.ibm.com/software/data/informix/>                                 |
| Ingres<sup>1</sup>                        | Actian                              | <http://esd.actian.com/product/drivers/JDBC/java>                                |
| InterBase<sup>1</sup>                     | Embarcadero                         | [http://edn.embarcadero.com](http://edn.embarcadero.com/)                        |
| jTDS Free MS SQL Sybase<sup>1</sup>       | jTDS                                | <http://jtds.sourceforge.net/>                                                   |
| MariaDB                                   | MariaDB                             | <https://downloads.mariadb.org/connector-java/>                                  |
| MaxDB                                     | SAP                                 | [http://maxdb.sap.com](http://maxdb.sap.com/)                                    |
| Mckoi SQL Database                        | Mckoi SQL Database                  | <http://www.mckoi.com/originalmckoisql/index.html>                               |
| Mimer                                     | Mimer Information Technology        | [http://www.mimer.com](http://www.mimer.com/)                                    |
| MySQL                                     | Oracle                              | <https://dev.mysql.com/downloads/connector/j/>                                   |
| Neoview<sup>1</sup>                       | HP                                  | Contact your local HP representative for information on this product.            |
| Netezza                                   | IBM                                 | [http://www.netezza.com](http://www.netezza.com/)                                |
| OpenBase SQL                              | OpenBase International              | <http://www.openbase.com/index.php/products/downloads>                           |
| Oracle                                    | Oracle                              | <http://www.oracle.com/technetwork/database/features/jdbc/index.html>            |
| Pervasive                                 | Pervasive                           | <http://www.pervasivedb.com/download/Pages/PDBDownloads.aspx>                    |
| PostgreSQL                                | PostgreSQL Global Development Group | <http://jdbc.postgresql.org/>                                                    |
| SAP ASE (formerly Sybase ASE)<sup>1</sup> | SAP                                 | <https://support.sap.com/swdc>                                                   |
| SAP DB                                    | SAP MaxDB                           | <https://support.sap.com/software.html>                                          |
| SAP HANA                                  | SAP                                 | <http://help.sap.com/hana>                                                       |
| SAP SQL Anywhere                          | SAP                                 | <https://support.sap.com/software.html>                                          |
| SmallSQL                                  | SmallSQL                            | <http://www.smallsql.de/download.html>                                           |
| Snowflake                                 | Snowflake                           | <https://repo1.maven.org/maven2/net/snowflake/snowflake-jdbc>                    |
| SQLite                                    | Xerial                              | <http://www.xerial.org/trac/Xerial/wiki/SQLiteJDBC>                              |
| SQL Server                                | Microsoft                           | <http://msdn.microsoft.com/en-us/sqlserver/aa937724.aspx>                        |
| Teradata                                  | Teradata                            | <http://downloads.teradata.com/download/connectivity/jdbc-driver>                |
| Vertica<sup>1</sup>                       | HP                                  | [http://www.vertica.com](http://www.vertica.com/)                                |

<sup>1</sup> Deprecated beginning in version 11.0.

## Driver details by database

### Amazon Redshift

| Vendor Name                                                                                                                                                                          | Details                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                            |                                                                                                           |
| Amazon Web Services                                                                                                                                                                  | <p>Company URL:</p><p><a href="http://aws.amazon.com/redshift/"><http://aws.amazon.com/redshift/></a></p> |
| <p>Driver URL:</p><p><a href="https://s3.amazonaws.com/redshift-downloads/drivers/RedshiftJDBC4.jar"><https://s3.amazonaws.com/redshift-downloads/drivers/RedshiftJDBC4.jar></a></p> |                                                                                                           |
| <p>JDBC URL Syntax by Type:</p><p><code>jdbc:redshift://\<endpoint>:\<port>/\<database>?tcpKeepAlive=true</code></p>                                                                 | <p>Default Port:</p><p>5439</p>                                                                           |
| <p>JDBC Class:</p><p><code>com.amazon.redshift.jdbc4.Driver</code></p>                                                                                                               | <p>JDBC JAR File Name:</p><p><code>RedshiftJDBC4.jar</code></p>                                           |
| <p>Comments:</p><p>Download and use only the <code>RedshiftJDBC4.jar</code>.</p>                                                                                                     |                                                                                                           |

### AWS Athena

| Vendor Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Details                                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                         |
| Amazon Web Services                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | <p>Company URL:</p><p><a href="https://aws.amazon.com/athena/"><https://aws.amazon.com/athena/></a></p> |
| <p>Driver URL:</p><p><a href="https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver.html"><https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver.html></a></p>                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                         |
| <p>JDBC URL Syntax by Type:</p><p><code>jdbc:athena://WorkGroup=\<workgroup>;Region=\<region>;Catalog=\<catalog>;Database=\<database>;OutputLocation=\<outputlocation>;CredentialsProvider=\<credentialsprovider></code></p>                                                                                                                                                                                                                                                                                                                                                                   | <p>Default Port:</p><p>N/A</p>                                                                          |
| <p>JDBC Class:</p><p><code>com.amazon.athena.jdbc.AthenaDriver</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | <p>JDBC JAR File Name:</p><p><code>athena-jdbc-3.2.0-with-dependencies.jar</code></p>                   |
| <p>Comments:</p><p>Download the <code>athena-jdbc-3.2.0-with-dependencies.jar</code> file from <a href="https://downloads.athena.us-east-1.amazonaws.com/drivers/JDBC/3.2.0/athena-jdbc-3.2.0-with-dependencies.jar"><https://downloads.athena.us-east-1.amazonaws.com/drivers/JDBC/3.2.0/athena-jdbc-3.2.0-with-dependencies.jar></a>.</p><p>See <a href="https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html#credentials-default"><https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html#credentials-default></a> regarding credentials.</p> |                                                                                                         |

### Cache (Caché)

{% hint style="info" %}
**Note:** Deprecated beginning in version 11.0.
{% endhint %}

| Vendor Name                                                                                                                                                                              | Details                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Recommended Native Driver                                                                                                                                                                |                                                                                                  |
| InterSystems                                                                                                                                                                             | <p>Company URL:</p><p><a href="http://www.cachemonitor.de/"><http://www.cachemonitor.de></a></p> |
| <p>Driver URL:</p><p><a href="http://www.cachemonitor.de/intersystems-documentation/cache-jdbc-driver"><http://www.cachemonitor.de/intersystems-documentation/cache-jdbc-driver></a></p> |                                                                                                  |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:Cache://\<server>\[:\<port>]/\<namespace></code></p>                                               | <p>Default Port:</p><p>1972</p>                                                                  |
| <p>JDBC Class:</p><p><code>com.intersys.jdbc.CacheDriver</code></p>                                                                                                                      | <p>JDBC JAR File Name:</p><p><code>cachedb.jar</code></p>                                        |

### CUBRID

| Vendor Name                                                                                                                                                                                                                         | Details                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                                                           |                                                                                       |
| CUBRID                                                                                                                                                                                                                              | <p>Company URL:</p><p><a href="http://www.cubrid.org"><http://www.cubrid.org></a></p> |
| <p>Driver URL:</p><p><a href="http://www.cubrid.org/?mid=downloads&#x26;item=jdbc_driver"><http://www.cubrid.org/?mid=downloads&#x26;item=jdbc_driver></a></p>                                                                      |                                                                                       |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:cubrid:\<server>:\<port>: \<databaseName>:\<username>: \<password> :\[?\<URL attribute>=\<value> \[&\<URL attribute>=\<value>] … ]</code></p> | <p>Default Port:</p><p>33000</p>                                                      |
| <p>JDBC Class:</p><p><code>cubrid.jdbc.driver.CUBRIDDriver</code></p>                                                                                                                                                               | <p>JDBC JAR File Name:</p><p><code>N/A</code></p>                                     |
| <p>Comments:</p><p>Open source database highly optimized for Web applications.</p>                                                                                                                                                  |                                                                                       |

### Daffodil DB

| Vendor Name                                                                                                                                                                                                                                                | Details                                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                                                                                  |                                                                                                                                                             |
| Daffodil Software                                                                                                                                                                                                                                          | <p>Company URL:</p><p><a href="http://db.daffodilsw.com/"><http://db.daffodilsw.com></a></p>                                                                |
| <p>Driver URL:</p><p><a href="http://sourceforge.net/projects/daffodildb/"><http://sourceforge.net/projects/daffodildb/></a></p>                                                                                                                           |                                                                                                                                                             |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:daffodilDB://\<server>\[:\<port>]/\<databaseName></code></p><ul><li><strong>Embedded</strong></li></ul><p><code>jdbc:daffodilDB\_embedded:\<databaseName></code></p> | <p>Default Port:</p><p>3456</p><p>N/A</p>                                                                                                                   |
| <p>JDBC Class:</p><p><code>in.co.daffodil.db.rmi.RmiDaffodilDBDriver</code></p><p><code>in.co.daffodil.db.jdbc.DaffodilDBDriver</code></p>                                                                                                                 | <p>JDBC JAR File Name:</p><p><code>DaffodilDB\_client.jar</code></p><p><code>DaffodilDB\_Embedded.jar</code>,</p><p><code>DaffodilDB\_Common.jar</code></p> |
| <p>Comments:</p><p>Open source database.</p>                                                                                                                                                                                                               |                                                                                                                                                             |

### DB2 AS/400

| Vendor Name                                                                                                                                                                                                                                                                                                                    | Details                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                                                                                                                                                      |                                                                                  |
| IBM                                                                                                                                                                                                                                                                                                                            | <p>Company URL:</p><p><a href="http://www.ibm.com/"><http://www.ibm.com></a></p> |
| <p>Driver URL:</p><p><a href="http://www-01.ibm.com/support/docview.wss?uid=swg21363866"><http://www-01.ibm.com/support/docview.wss?uid=swg21363866></a></p><p><a href="http://www-03.ibm.com/systems/power/software/i/toolbox/downloads.html"><http://www-03.ibm.com/systems/power/software/i/toolbox/downloads.html></a></p> |                                                                                  |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:as400://\<server>naming=sql;errors=full</code></p>                                                                                                                                                                                       | <p>Default Port:</p><p>N/A</p>                                                   |
| <p>JDBC Class:</p><p><code>com.ibm.as400.access.AS400JDBCDriver</code></p>                                                                                                                                                                                                                                                     | <p>JDBC JAR File Name:</p><p><code>jt400.jar</code></p>                          |

### DB2 Universal Database

| Vendor Name                                                                                                                                                                                        | Details                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                          |                                                                                  |
| IBM                                                                                                                                                                                                | <p>Company URL:</p><p><a href="http://www.ibm.com/"><http://www.ibm.com></a></p> |
| <p>Driver URL:</p><p><a href="http://www-01.ibm.com/support/docview.wss?uid=swg21363866"><http://www-01.ibm.com/support/docview.wss?uid=swg21363866></a></p>                                       |                                                                                  |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:db2://\<server>\[:\<port>]/\<databaseName>\[:\<URL attribute>=\<value>;\<URL attribute>=\<value>]</code></p> | <p>Default Port:</p><p>50000</p>                                                 |
| <p>JDBC Class:</p><p><code>com.ibm.db2.jcc.DB2Driver</code></p>                                                                                                                                    | <p>JDBC JAR File Name:</p><p><code>db2jcc4.jar</code></p>                        |

### Firebird

| Vendor Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Details                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Recommended Native Driver                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                  |
| Firebird Foundation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | <p>Company URL:</p><p><a href="http://www.firebirdsql.org/"><http://www.firebirdsql.org></a></p> |
| <p>Driver URL:</p><p><a href="http://www.firebirdsql.org/en/jdbc-driver/"><http://www.firebirdsql.org/en/jdbc-driver/></a></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                  |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:firebirdsql:\<server>\[/\<port>]:/\<database-file></code></p><p>(JDBC Type 4, official format)</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:firebirdsql://\<server>\[:\<port>]/\<database-file></code></p><p>(JDBC Type 4, compatibility format)</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:firebirdsql:native//\<server>\[/\<port>]:/\<database-file></code></p><p>(JDBC Type 2, compatibility format)</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:firebirdsql:native://\<server>\[:\<port>]/\<database-file></code></p><p>JDBC Type 2, compatibility format. Requires libraries)</p><ul><li><strong>Embedded</strong></li></ul><p><code>jdbc:firebirdsql:embedded:/\<local-database-file></code></p><p>(JDBC Type 2, compatibility format. Requires libraries)</p> | <p>Default Port:</p><p>3050</p><p>3050</p><p>3050</p><p>3050</p><p>N/A</p>                       |
| <p>JDBC Class:</p><p><code>org.firebirdsql.jdbc.FBDriver</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | <p>JDBC JAR File Name:</p><p><code>jaybird-full-xxx.jar</code></p>                               |
| <p>Shipped with Pentaho products:</p><p>Pentaho Data Integration</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                  |

### FrontBase

| Vendor Name                                                                                                                                          | Details                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                            |                                                                                              |
| FrontBase                                                                                                                                            | <p>Company URL:</p><p><a href="http://www.frontbase.com/"><http://www.frontbase.com></a></p> |
| <p>Driver URL:</p><p><a href="http://www.frontbase.com/cgi-bin/WebObjects/FBWebSite"><http://www.frontbase.com/cgi-bin/WebObjects/FBWebSite></a></p> |                                                                                              |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:FrontBase://\<host>\[:\<port>]/\<databaseName></code></p>      | <p>Default Port:</p><p>N/A</p>                                                               |
| <p>JDBC Class:</p><p><code>com.frontbase.jdbc.FBJDriver</code></p>                                                                                   | <p>JDBC JAR File Name:</p><p><code>frontbasejdbc.jar</code></p>                              |

### Google BigQuery

| Vendor Name                                                                                                                                                                                                                                                         | Details                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                                                                                           |                                                                                                                                                                                         |
| Google BigQuery                                                                                                                                                                                                                                                     | For installation instructions, see [Google BigQuery](https://github.com/pentaho/documentation/blob/main/PDIA/11.0/Get%20Started/JDBC%20drivers%20reference/broken-reference/README.md). |
| <p>Company URL:</p><p><a href="https://cloud.google.com/bigquery"><https://cloud.google.com/bigquery></a></p>                                                                                                                                                       |                                                                                                                                                                                         |
| <p>Driver URL:</p><p><a href="https://cloud.google.com/bigquery/partners/simba-drivers/"><https://cloud.google.com/bigquery/partners/simba-drivers/></a></p>                                                                                                        |                                                                                                                                                                                         |
| <p>Host URL:</p><p><a href="https://bigquery.googleapis.com/discovery/v1/apis/bigquery/v2/rest"><https://bigquery.googleapis.com/discovery/v1/apis/bigquery/v2/rest></a></p>                                                                                        |                                                                                                                                                                                         |
| <p>Default Port:</p><p>443</p>                                                                                                                                                                                                                                      |                                                                                                                                                                                         |
| <p>Simba JDBC Driver URL:</p><p><a href="https://storage.googleapis.com/simba-bq-release/jdbc/SimbaJDBCDriverforGoogleBigQuery42_1.2.25.1029.zip"><https://storage.googleapis.com/simba-bq-release/jdbc/SimbaJDBCDriverforGoogleBigQuery42_1.2.25.1029.zip></a></p> |                                                                                                                                                                                         |

### Greenplum

| Vendor Name                                                                                                                                        | Details                                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                          |                                                                                       |
| Greenplum                                                                                                                                          | <p>Company URL:</p><p><a href="http://greenplum.org/"><http://greenplum.org/></a></p> |
| <p>Driver URL:</p><p><a href="http://jdbc.postgresql.org/download.html"><http://jdbc.postgresql.org/download.html></a></p>                         |                                                                                       |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:postgresql://\<server>\[:\<port>]/\<databaseName></code></p> | <p>Default Port:</p><p>5342</p>                                                       |
| <p>JDBC Class:</p><p><code>org.postgresql.Driver</code></p>                                                                                        | <p>JDBC JAR File Name:</p><p><code>postgresql-8.x-xxx.jdbc4.jar</code></p>            |
| <p>Comments:</p><p>Greenplum uses the Postgresql JDBC driver.</p>                                                                                  |                                                                                       |

### H2 Database

| Vendor Name                                                                                                                                                                                                         | Details                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                                           |                                                                                                |
| H2                                                                                                                                                                                                                  | <p>Company URL:</p><p><a href="http://www.h2database.com/"><http://www.h2database.com></a></p> |
| <p>Driver URL:</p><p><a href="http://www.h2database.com/"><http://www.h2database.com></a></p>                                                                                                                       |                                                                                                |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:h2:tcp\://server\[:port]/file-path</code></p><ul><li><strong>Embedded</strong></li></ul><p><code>jdbc:h2:file-name</code></p> | <p>Default Port:</p><p>9092</p><p>N/A</p>                                                      |
| <p>JDBC Class:</p><p><code>jdbc:h2:tcp\://server\[:port]/file-path</code></p><p><code>org.h2.Driver</code></p>                                                                                                      | <p>JDBC JAR File Name:</p><p><code>h2-x.x.xxx.jar</code></p>                                   |
| <p>Shipped with Pentaho products:</p><ul><li>Pentaho Server</li><li>Pentaho Data Integration</li><li>Pentaho Metadata Editor</li><li>Pentaho Report Designer</li></ul>                                              |                                                                                                |
| <p>Comments:</p><p>Open source Java SQL database.</p>                                                                                                                                                               |                                                                                                |

### Hive

{% hint style="info" %}
**Note:** Deprecated beginning in version 11.0.
{% endhint %}

| Vendor Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Details                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                 |
| Apache                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | <p>Company URL:</p><p><a href="http://hive.apache.org/"><http://hive.apache.org/></a></p>       |
| <p>Driver URL:</p><p><a href="https://www.cloudera.com/downloads/connectors/hive/jdbc/2-6-21.html"><https://www.cloudera.com/downloads/connectors/hive/jdbc/2-6-21.html></a></p><p>or</p><p><a href="https://mvnrepository.com/artifact/org.apache.hive/hive-jdbc"><https://mvnrepository.com/artifact/org.apache.hive/hive-jdbc></a></p>                                                                                                                                                         |                                                                                                 |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:hive://\<server>\[:\<port>]/default</code></p>                                                                                                                                                                                                                                                                                                                                                              | <p>Default Port:</p><p>10000</p>                                                                |
| <p>JDBC Class:</p><p><code>org.apache.hadoop.hive.jdbc. HiveDriver</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                     | <p>JDBC JAR File Name:</p><p><code>pentaho-hadoop-shims-common-fragment-Vx-x.x.x.jar</code></p> |
| <p>Shipped with Pentaho products:</p><ul><li>Pentaho Server</li><li>Pentaho Data Integration</li><li>Pentaho Metadata Editor</li><li>Pentaho Report Designer</li></ul>                                                                                                                                                                                                                                                                                                                            |                                                                                                 |
| <p>Comments:</p><p>The <code>pentaho-hadoop-shims-common-fragment-Vx-x.x.x.jar</code> library includes a proxy driver. The actual Hive JDBC implementation for the specific distribution and version of Hadoop is located in the Pentaho driver for that distro. See the <strong>Install Pentaho Data Integration and Analytics</strong> document for more information.</p><p>Hive does not support the full SQL capabilities. It uses a subset and is more accurately referred to as HiveQL.</p> |                                                                                                 |

### Hive2

| Vendor Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Details                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                 |
| Apache                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | <p>Company URL:</p><p><a href="http://hive.apache.org/"><http://hive.apache.org/></a></p>       |
| <p>Driver URL:</p><p><a href="https://www.cloudera.com/downloads/connectors/hive/jdbc/2-6-21.html"><https://www.cloudera.com/downloads/connectors/hive/jdbc/2-6-21.html></a></p><p>or</p><p><a href="https://mvnrepository.com/artifact/org.apache.hive/hive-jdbc"><https://mvnrepository.com/artifact/org.apache.hive/hive-jdbc></a></p>                                                                                                                                                          |                                                                                                 |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:hive2://\<server>\[:\<port>]/\<db></code></p>                                                                                                                                                                                                                                                                                                                                                                | <p>Default Port:</p><p>10000</p>                                                                |
| <p>JDBC Class:</p><p><code>org.apache.hive.jdbc. HiveDriver</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                             | <p>JDBC JAR File Name:</p><p><code>pentaho-hadoop-shims-common-fragment-Vx-x.x.x.jar</code></p> |
| <p>Shipped with Pentaho products:</p><ul><li>Pentaho Server</li><li>Pentaho Data Integration</li><li>Pentaho Metadata Editor</li><li>Pentaho Report Designer</li></ul>                                                                                                                                                                                                                                                                                                                             |                                                                                                 |
| <p>Comments:</p><p>The <code>pentaho-hadoop-shims-common-fragment-Vx-x.x.x.jar</code> library includes a proxy driver. The actual Hive JDBC implementation for the specific distribution and version of Hadoop is located in the Pentaho driver for that distro. See the <strong>Install Pentaho Data Integration and Analytics</strong> document for more information.</p><p>Hive2 does not support the full SQL capabilities. It uses a subset and is more accurately referred to as HiveQL.</p> |                                                                                                 |

### HSQLDB

| Vendor Name                                                                                                                                                                                                                                                                                                                                                   | Details                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                                                                                                                                                                                     |                                                                                        |
| HyperSQL                                                                                                                                                                                                                                                                                                                                                      | <p>Company URL:</p><p><a href="http://www.hsqldb.org/"><http://www.hsqldb.org></a></p> |
| <p>Driver URL:</p><p><a href="http://sourceforge.net/projects/hsqldb/"><http://sourceforge.net/projects/hsqldb/></a></p>                                                                                                                                                                                                                                      |                                                                                        |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:hsqldb:hsql://\<server>\[:\<port>]/\<databaseName></code></p><ul><li><strong>Embedded Memory</strong></li></ul><p><code>jdbc:hsqldb:mem:\<databaseName></code></p><ul><li><strong>Embedded File</strong></li></ul><p><code>jdbc:hsqldb:file:\<database-file></code></p> | <p>Default Port:</p><p>9001</p><p>N/A</p><p>N/A</p>                                    |
| <p>JDBC Class:</p><p><code>org.hsqldb.jdbcDriver</code></p>                                                                                                                                                                                                                                                                                                   | <p>JDBC JAR File Name:</p><p><code>hsqldb.jar</code></p>                               |
| <p>Shipped with Pentaho products:</p><ul><li>Pentaho User Console</li><li>Pentaho Server</li><li>Pentaho Aggregation Designer</li><li>Pentaho Data Integration</li><li>Pentaho Metadata Editor</li><li>Pentaho Report Designer</li></ul>                                                                                                                      |                                                                                        |

### Impala

| Vendor Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Details                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                 |
| Cloudera                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | <p>Company URL:</p><p><a href="http://cloudera.com/"><http://cloudera.com></a></p>              |
| <p>Driver URL:</p><p>Built in</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                 |
| <p>JDBC URL Syntax by Type:</p><p><code>jdbc:hive2://\<server>\[\<port>]/;auth=noSasl</code></p>                                                                                                                                                                                                                                                                                                                                                                                                  | <p>Default Port:</p><p>21050</p>                                                                |
| <p>JDBC Class:</p><p><code>org.apache.hadoop.hive.jdbc. HiveDriver</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                     | <p>JDBC JAR File Name:</p><p><code>pentaho-hadoop-shims-common-fragment-Vx-x.x.x.jar</code></p> |
| <p>Shipped with Pentaho products:</p><ul><li>Pentaho Server</li><li>Pentaho Data Integration</li><li>Pentaho Metadata Editor</li><li>Pentaho Report Designer</li></ul>                                                                                                                                                                                                                                                                                                                            |                                                                                                 |
| <p>Comments:</p><p>The <code>pentaho-hadoop-shims-common-fragment-Vx-x.x.x.jar</code> library isncludesa proxy driver. The actual Hive JDBC implementation for the specific distribution and version of Hadoop is located in the Pentaho driver for that distro. See the <strong>Install Pentaho Data Integration and Analytics</strong> document for more information.</p><p>Hive does not support the full SQL capabilities. It uses a subset and is more accurately referred to as HiveQL.</p> |                                                                                                 |

### Informix

| Vendor Name                                                                                                                                                                                          | Details                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                            |                                                                                  |
| IBM                                                                                                                                                                                                  | <p>Company URL:</p><p><a href="http://www.ibm.com/"><http://www.ibm.com></a></p> |
| <p>Driver URL:</p><p><a href="http://www14.software.ibm.com/webapp/download/search.jsp?go=y&#x26;rs=ifxjdbc"><http://www14.software.ibm.com/webapp/download/search.jsp?go=y&#x26;rs=ifxjdbc></a></p> |                                                                                  |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:informix-sqli://\<server>\[:\<port>]/\<databaseName>:informixserver= \<dbservername></code></p>                | Default Port:1533                                                                |
| <p>JDBC Class:</p><p><code>com.informix.jdbc.IfxDriver</code></p>                                                                                                                                    | <p>JDBC JAR File Name:</p><p><code>ifxjdbc.jar</code></p>                        |

### Ingres

{% hint style="info" %}
**Note:** Deprecated beginning in version 11.0.
{% endhint %}

| Vendor Name                                                                                                                                     | Details                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                       |                                                                                         |
| Actian                                                                                                                                          | <p>Company URL:</p><p><a href="http://www.actian.com/"><http://www.actian.com/></a></p> |
| <p>Driver URL:</p><p><a href="http://esd.actian.com/product/drivers/JDBC/java"><http://esd.actian.com/product/drivers/JDBC/java></a></p>        |                                                                                         |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:ingres\://\<server>\[:\<port>]/\<databaseName></code></p> | <p>Default Port:</p><p>21071</p>                                                        |
| <p>JDBC Class:</p><p><code>com.ingres.jdbc.IngresDriver</code></p>                                                                              | <p>JDBC JAR File Name:</p><p><code>iijdbc.jar</code></p>                                |
| <p>Comments:</p><p>Open source relational database management system.</p>                                                                       |                                                                                         |

### InterBase

{% hint style="info" %}
**Note:** Deprecated beginning in version 11.0.
{% endhint %}

| Vendor Name                                                                                                                              | Details                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Recommended Native Driver                                                                                                                |                                                                                                  |
| Embarcadero                                                                                                                              | <p>Company URL:</p><p><a href="http://edn.embarcadero.com/"><http://edn.embarcadero.com></a></p> |
| <p>Driver URL:</p><p>N/A</p>                                                                                                             |                                                                                                  |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:interbase://\<server>/\<full\_db\_path></code></p> | <p>Default Port:</p><p>N/A</p>                                                                   |
| <p>JDBC Class</p><p><code>interbase.interclient.Driver</code></p>                                                                        | <p>JDBC JAR File Name:</p><p><code>interclient.jar</code></p>                                    |

### jTDS Free MS SQL Sybase

{% hint style="info" %}
**Note:** Deprecated beginning in version 11.0.
{% endhint %}

| Vendor Name                                                                                                                                                                                                                                                                                                                | Details                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                                                                                                                                                  |                                                                                                     |
| jTDS                                                                                                                                                                                                                                                                                                                       | <p>Company URL:</p><p><a href="http://jtds.sourceforge.net/"><http://jtds.sourceforge.net/></a></p> |
| <p>Driver URL:</p><p>N/A</p>                                                                                                                                                                                                                                                                                               |                                                                                                     |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>SQL Server</strong></li></ul><p><code>jdbc:jtds:\<server\_type>//\<server>\[:\<port>]\[/\<database>]\[;\<property>=\<value>\[;...]]]</code></p><ul><li><strong>Sybase</strong></li></ul><p><code>jdbc:jtds:\<server\_type>://\<server>\[:\<port>]\[/\<database>]</code></p> | <p>Default Port:</p><p>1433</p><p>7100</p>                                                          |
| <p>JDBC Class:</p><p><code>interbase.interclient.Driver</code></p>                                                                                                                                                                                                                                                         | <p>JDBC JAR File Name:</p><p><code>jtds-x.x.x.jar</code></p>                                        |
| <p>Shipped with Pentaho products:</p><ul><li>Pentaho User Console</li><li>Pentaho Server</li><li>Pentaho Aggregation Designer</li><li>Pentaho Data Integration</li><li>Pentaho Metadata Editor</li><li>Pentaho Report Designer</li></ul>                                                                                   |                                                                                                     |

### MariaDB

| Vendor Name                                                                                                                                                                                                                    | Details                                                                          |                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                                                      |                                                                                  |                                                                             |
| MariaDB                                                                                                                                                                                                                        | <p>Company URL:</p><p><a href="http://mariadb.org/"><http://mariadb.org></a></p> |                                                                             |
| <p>Driver URL:</p><p><a href="https://downloads.mariadb.org/connector-java/"><https://downloads.mariadb.org/connector-java/></a></p>                                                                                           |                                                                                  |                                                                             |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:mariadb://\<hostname>\[,\<failoverhost>]\[:\<port>] /\<dbname>\[?\<URL attribute>=\<value>\[&\<URL attribute>=\<value>] ... ]</code></p> | <p>Default Port:</p><p>3306</p>                                                  |                                                                             |
|                                                                                                                                                                                                                                | <p>JDBC Class:</p><p><code>org.mariadb.jdbc.Driver</code></p>                    | <p>JDBC JAR File Name:</p><p><code>mariadb-java-client-2.1.2.jar</code></p> |

### MaxDB

| Vendor Name                                                                                                                                   | Details                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                     |                                                                                  |
| SAP                                                                                                                                           | <p>Company URL:</p><p><a href="http://www.sap.com/"><http://www.sap.com></a></p> |
| <p>Driver URL:</p><p><a href="http://maxdb.sap.com/"><http://maxdb.sap.com></a></p>                                                           |                                                                                  |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:sapdb://\<server>\[:\<port>]/\<databaseName></code></p> | <p>Default Port:</p><p>7210</p>                                                  |
| <p>JDBC Class:</p><p><code>com.sap.dbtech.jdbc.DriverSapDB</code></p>                                                                         | <p>JDBC JAR File Name:</p><p><code>sapdbc.jar</code></p>                         |
| <p>Comments:</p><p>Database management system developed and supported by SAP AG.</p>                                                          |                                                                                  |

### Mckoi SQL Database

| Vendor Name                                                                                                                                 | Details                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Recommended Native Driver                                                                                                                   |                                                                                      |
| Mckoi                                                                                                                                       | <p>Company URL:</p><p><a href="http://www.mckoi.com/"><http://www.mckoi.com></a></p> |
| <p>Driver URL:</p><p><a href="http://www.mckoi.com/originalmckoisql/index.html"><http://www.mckoi.com/originalmckoisql/index.html></a></p>  |                                                                                      |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:mckoi://\<server>\[:\<port>]\[/\<schema>]/</code></p> | <p>Default Port:</p><p>9157</p>                                                      |
| <p>JDBC Class:</p><p><code>com.mckoi.JDBCDriver</code></p>                                                                                  | <p>DBC JAR File Name:</p><p><code>mckoidb.jar</code></p>                             |
| <p>Comments:</p><p>Open source SQL database written in Java.</p>                                                                            |                                                                                      |

### Mimer

| Vendor Name                                                                                                                                           | Details                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Recommended Native Driver                                                                                                                             |                                                                                      |
| Mimer Information Technology                                                                                                                          | <p>Company URL:</p><p><a href="http://www.mimer.com/"><http://www.mimer.com></a></p> |
| <p>Driver URL:</p><p>N/A</p>                                                                                                                          |                                                                                      |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:mimer:\<protocol>://\<server>\[:\<port>]/\<database></code></p> | <p>Default Port:</p><p>1360</p>                                                      |
| <p>JDBC Class:</p><p><code>com.mimer.jdbc.Driver</code></p>                                                                                           | <p>JDBC JAR File Name:</p><p><code>mimer.jar</code></p>                              |

### MySQL

| Vendor Name                                                                                                                                                                                                                  | Details                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                                                    |                                                                                                                                                                               |
| Oracle                                                                                                                                                                                                                       | <p>Company URL:</p><p><a href="http://www.mysql.com/"><http://www.mysql.com></a></p>                                                                                          |
| <p>Driver URL:</p><p><a href="https://dev.mysql.com/downloads/connector/j/"><https://dev.mysql.com/downloads/connector/j/></a></p>                                                                                           |                                                                                                                                                                               |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:mysql://\<hostname>\[,\<failoverhost>]\[:\<port>] /\<dbname>\[?\<URL attribute>=\<value>\[&\<URL attribute>=\<value>] ... ]</code></p> | <p>Default Port:</p><p>3306</p>                                                                                                                                               |
| <p>JDBC Class:</p><p><code>com.mysql.jdbc.Driver</code> (official class name)</p><p><code>org.gjt.mm.mysql.Driver</code> (older class name)</p>                                                                              | <p>JDBC JAR File Name:</p><p><code>mysql-connector-java-8.0.26</code> (official JAR filename)</p><p><code>mysql-connector-java-5.x.xx-bin.jar</code> (older JAR filename)</p> |
| Comments: Version 8.026 is certified, version 5.7 is supported.                                                                                                                                                              |                                                                                                                                                                               |

### Neoview

{% hint style="info" %}
**Note:** Deprecated beginning in version 11.0.
{% endhint %}

| Vendor Name                                                                                                                                                                                     | Details                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Recommended Native Driver                                                                                                                                                                       |                                                                                |
| HP                                                                                                                                                                                              | <p>Company URL:</p><p><a href="http://www.hp.com/"><http://www.hp.com></a></p> |
| <p>Driver URL:</p><p><a href="http://storiedigitali.live/hp-neoview-jdbc-63.html"><http://storiedigitali.live/hp-neoview-jdbc-63.html></a></p>                                                  |                                                                                |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:hpt4jdbc://\<system>\[:\<port>]/\[:]\[\<URL attribute>=\<value>\[;\<URL attribute>=\<value> …]</code></p> | <p>Default Port:</p><p>18650</p>                                               |
| <p>JDBC Class:</p><p><code>com.hp.t4jdbc.HPT4Driver</code></p>                                                                                                                                  | <p>JDBC JAR File Name:</p><p><code>N/A</code></p>                              |

### Netezza

| Vendor Name                                                                                        | Details                                                                                  |
| -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                          |                                                                                          |
| IBM                                                                                                | <p>Company URL:</p><p><a href="http://www.netezza.com/"><http://www.netezza.com></a></p> |
| <p>Driver URL:</p><p>N/A</p>                                                                       |                                                                                          |
| <p>JDBC URL Syntax by Type:</p><p><code>jdbc:netezza://\<server>\[:\<port>]/\<database></code></p> | <p>Default Port:</p><p>5480</p>                                                          |
| <p>JDBC Class:</p><p><code>org.netezza.Driver</code></p>                                           | <p>JDBC JAR File Name:</p><p><code>N/A</code></p>                                        |

### OpenBase SQL

| Vendor Name                                                                                                                                        | Details                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Recommended Native Driver                                                                                                                          |                                                                                            |
| OpenBase International                                                                                                                             | <p>Company URL:</p><p><a href="http://www.openbase.com/"><http://www.openbase.com></a></p> |
| <p>Driver URL:</p><p><a href="http://www.openbase.com/index.php/products/downloads"><http://www.openbase.com/index.php/products/downloads></a></p> |                                                                                            |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:openbase://\<server>/\<databaseName></code></p>              | <p>Default Port:</p><p>N/A</p>                                                             |
| <p>JDBC Class:</p><p><code>com.openbase.jdbc.ObDriver</code></p>                                                                                   | <p>JDBC JAR File Name:</p><p><code>OpenBaseJDBC.jar</code></p>                             |

### Oracle

| Vendor Name                                                                                                                                                                                                                                                   | Details                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                                                                                     |                                                                                         |
| Oracle                                                                                                                                                                                                                                                        | <p>Company URL:</p><p><a href="http://www.oracle.com/"><http://www.oracle.com></a></p>  |
| <p>Driver URL:</p><p><a href="http://www.oracle.com/technetwork/database/features/jdbc/index.html"><http://www.oracle.com/technetwork/database/features/jdbc/index.html></a></p>                                                                              |                                                                                         |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Thin Server</strong></li></ul><p><code>jdbc:oracle:thin:@\<server>\[:\<port>]: \<sid></code></p><ul><li><strong>OCI Server</strong></li></ul><p><code>jdbc:oracle:oci:@\<server>\[:\<port>]: \<sid></code></p> | <p>Default Port:</p><p>1521</p>                                                         |
| <p>JDBC Class:</p><p><code>oracle.jdbc.driver.OracleDriver</code></p><p><code>oracle.jdbc.OracleDriver</code></p>                                                                                                                                             | <p>JDBC JAR File Name:</p><p><code>ojdbcx.jar</code></p><p><code>orai18n.jar</code></p> |
| <p>Comments:</p><p>The OCI server requires OCI libraries.</p>                                                                                                                                                                                                 |                                                                                         |

### Pervasive

| Vendor Name                                                                                                                                                      | Details                                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                        |                                                                                                                                       |
| Pervasive                                                                                                                                                        | <p>Company URL:</p><p><a href="http://www.pervasivedb.com/Pages/default.aspx"><http://www.pervasivedb.com/Pages/default.aspx></a></p> |
| <p>Driver URL:</p><p><a href="http://www.pervasivedb.com/download/Pages/PDBDownloads.aspx"><http://www.pervasivedb.com/download/Pages/PDBDownloads.aspx></a></p> |                                                                                                                                       |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:pervasive://\<server>\[:\<port>]/\<datasource></code></p>                  | <p>Default Port:</p><p>1583</p>                                                                                                       |
| <p>JDBC Class:</p><p><code>com.pervasive.jdbc.v2.Driver</code></p>                                                                                               | <p>JDBC JAR File Name:</p><p><code>N/A</code></p>                                                                                     |
| <p>Shipped with Pentaho products:</p><ul><li>Pentaho Data Integration</li><li>Pentaho Report Designer</li></ul>                                                  |                                                                                                                                       |
| <p>Comments:</p><p>The data source is the ODBC DSN.</p>                                                                                                          |                                                                                                                                       |

### PostgreSQL

| Vendor Name                                                                                                                                        | Details                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                          |                                                                                                 |
| PostgreSQL Global Development Group                                                                                                                | <p>Company URL:</p><p><a href="http://www.postgresql.org/"><http://www.postgresql.org/></a></p> |
| <p>Driver URL:</p><p><a href="http://jdbc.postgresql.org/"><http://jdbc.postgresql.org/></a></p>                                                   |                                                                                                 |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:postgresql://\<server>\[:\<port>]/\<databaseName></code></p> | <p>Default Port:</p><p>5342</p>                                                                 |
| <p>JDBC Class:</p><p><code>org.postgresql.Driver</code></p>                                                                                        | <p>JDBC JAR File Name:</p><p><code>postgresql-9.x-xxx.jdbc4.2.jar</code></p>                    |
| <p>Shipped with Pentaho products:</p><ul><li>Pentaho Data Integration</li><li>Pentaho Report Designer</li></ul>                                    |                                                                                                 |

### SAP ASE (formerly Sybase ASE)

{% hint style="info" %}
**Note:** Deprecated beginning in version 11.0.
{% endhint %}

| Vendor Name                                                                                                                                                                                                                                                                                        | Details                                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                                                                                                                          |                                                                                                                                     |
| SAP                                                                                                                                                                                                                                                                                                | <p>Company URL:</p><p><a href="https://www.sap.com/products/sybase-ase.html"><https://www.sap.com/products/sybase-ase.html></a></p> |
| <p>Driver URL:</p><p>The jConnect JDBC driver can only be installed from the SAP Adaptive Server Enterprise Installer. See the SAP website for more information.</p>                                                                                                                               |                                                                                                                                     |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:sybase:Tds:\<server>\[:\<port>]/\<databaseName></code></p>                                                                                                                                                   | <p>Default Port:</p><p>5000</p>                                                                                                     |
| <p>JDBC Class:</p><p><code>com.sybase.jdbc4.jdbc.SybDriver</code></p>                                                                                                                                                                                                                              | <p>JDBC JAR File Name:</p><p>N/A</p>                                                                                                |
| <p>Comments:</p><p>The open source jTDS driver works with SAP ASE (formerly Sybase) as well. Note that although you can use jTDS open source JDBC driver, we recommend that you use the SAP-supplied JDBC driver instead. Connections might not work reliably if you use the jTDS JDBC driver.</p> |                                                                                                                                     |

### SAP DB

| Vendor Name                                                                                                                          | Details                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| Recommended Native Driver                                                                                                            |                                                                |
| SAP DB                                                                                                                               | <p>Company URL:</p><p>N/A</p>                                  |
| <p>Driver URL:</p><p><a href="http://www.sapdb.org/sap_db_jdbc.htm"><http://www.sapdb.org/sap_db_jdbc.htm></a></p>                   |                                                                |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:sapdb://\<server>/\<database\_name></code></p> | <p>Default Port:</p><p>N/A</p>                                 |
| <p>JDBC Class:</p><p><code>com.sap.dbtech.jdbc.DriverSapDB</code></p>                                                                | <p>JDBC JAR File Name:</p><p><code>sapdbc-x.x.x.jar</code></p> |
| <p>Shipped with Pentaho products:</p><p>Pentaho Data Integration</p>                                                                 |                                                                |
| <p>Comments:</p><p>FREE Enterprise Open Source Database.</p>                                                                         |                                                                |

### SAP HANA

| Vendor Name                                                                                                                                                                                                                                                                                | Details                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                                                                                                                  |                                                                                    |
| SAP HANA                                                                                                                                                                                                                                                                                   | <p>Company URL:</p><p><a href="http://hana.sap.com/"><http://hana.sap.com></a></p> |
| <p>Driver URL:</p><p>For SAP customers, the driver is part of your client tools. Contact your SAP representative for more information.</p>                                                                                                                                                 |                                                                                    |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:sap\://\<server>:\<port>/?autocommit=false</code></p>                                                                                                                                                | <p>Default Port:</p><p>30015</p>                                                   |
| <p>JDBC Class:</p><p><code>com.sap.db.jdbc.Driver</code></p>                                                                                                                                                                                                                               | <p>JDBC JAR File Name:</p><p><code>ngdbc.jar</code></p>                            |
| <p>Comments:</p><p>Note that the default port number is '<code>30015</code>' where '<code>00</code>' is the instance of the machine you are connecting to. For example, you can connect to the same machine using '<code>30015</code>', '<code>30115</code>', or '<code>31015</code>'.</p> |                                                                                    |

### SAP SQL Anywhere

| Vendor Name                                                                                                                                                                                                                                                                                         | Details                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                                                                                                                           |                                                                                                                                         |
| SAP                                                                                                                                                                                                                                                                                                 | <p>Company URL:</p><p><a href="https://www.sap.com/products/sql-anywhere.html"><https://www.sap.com/products/sql-anywhere.html></a></p> |
| <p>Driver URL:</p><p>The jConnect JDBC driver can only be installed from the SAP Adaptive Server Enterprise Installer. Visit the SAP website for more information.</p>                                                                                                                              |                                                                                                                                         |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:sybase:Tds:\<server>\[:\<port>]/\<databaseName></code></p>                                                                                                                                                    | <p>Default Port:</p><p>2638</p>                                                                                                         |
| <p>JDBC Class:</p><p><code>com.sybase.jdbc4.jdbc.SybDriver</code></p>                                                                                                                                                                                                                               | <p>JDBC JAR File Name:</p><p><code>N/A</code></p>                                                                                       |
| <p>Comments:</p><p>This open source jTDS driver works with SAP ASE (formerly Sybase) as well. Note that although you can use jTDS open source JDBC driver, we recommend that you use the SAP-supplied JDBC driver instead. Connections might not work reliably if you use the jTDS JDBC driver.</p> |                                                                                                                                         |

### SmallSQL

| Vendor Name                                                                                                                                                           | Details                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                             |                                                                                           |
| SmallSQL                                                                                                                                                              | <p>Company URL:</p><p><a href="http://www.smallsql.de/"><http://www.smallsql.de/></a></p> |
| <p>Driver URL:</p><p><a href="http://www.smallsql.de/download.html"><http://www.smallsql.de/download.html></a></p>                                                    |                                                                                           |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Embedded</strong></li></ul><p><code>jdbc:smallsql:databaseName\[?URL attribute=value\[URLattribute=value]…]</code></p> | <p>Default Port:</p><p>N/A</p>                                                            |
| <p>JDBC Class:</p><p><code>smallsql.database.SSDriver</code></p>                                                                                                      | <p>JDBC JAR File Name:</p><p><code>smallsql.jar</code></p>                                |
| <p>Comments</p><p>Java desktop SQL database engine.</p>                                                                                                               |                                                                                           |

### Snowflake

| Vendor Name                                                                                                                                                                                                                                            | Details                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                                                                                                              |                                                                                           |
| Snowflake                                                                                                                                                                                                                                              | <p>Company URL:</p><p><a href="https://www.snowflake.com/"><http://snowflake.com></a></p> |
| <p>Driver URL:</p><p><a href="https://repo1.maven.org/maven2/net/snowflake/snowflake-jdbc"><https://repo1.maven.org/maven2/net/snowflake/snowflake-jdbc></a></p>                                                                                       |                                                                                           |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Embedded</strong></li></ul><p><code>jdbc</code><span data-gb-custom-inline data-tag="emoji" data-code="2744">❄️</span><code>//\<account\_name>.snowflakecomputing.com/?\<connection\_params></code></p> | <p>Default Port:</p><p>443</p>                                                            |
| <p>JDBC Class:</p><p><code>net.snowflake.client.jdbc.SnowflakeDriver</code></p>                                                                                                                                                                        | <p>JDBC JAR File Name:</p><p><code>snowflake-jdbc-3.6.28.jar</code></p>                   |
| Comments: Version 3.13.10 is the minimum version supported. Version 3.13.30 is certified. If timeout errors occur, see **Pentaho Data Integration** to troubleshoot.                                                                                   |                                                                                           |

### SQLite

| Vendor Name                                                                                                                                  | Details                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                    |                                                                     |
| Xerial                                                                                                                                       | <p>Company URL:</p><p>N/A</p>                                       |
| <p>Driver URL:</p><p><a href="http://www.xerial.org/trac/Xerial/wiki/SQLiteJDBC"><http://www.xerial.org/trac/Xerial/wiki/SQLiteJDBC></a></p> |                                                                     |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:sqlite:\<filename.db></code></p>                       | <p>Default Port:</p><p>N/A</p>                                      |
| <p>JDBC Class:</p><p><code>org.sqlite.JDBC</code></p>                                                                                        | <p>JDBC JAR File Name:</p><p><code>sqlite-jdbc-x.x.x.jar</code></p> |
| <p>Shipped with Pentaho products:</p><p>Pentaho Data Integration</p>                                                                         |                                                                     |

### SQL Server

| Vendor Name                                                                                                                                                     | Details                                                                                      |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                                       |                                                                                              |
| Microsoft                                                                                                                                                       | <p>Company URL:</p><p><a href="http://www.microsoft.com/"><http://www.microsoft.com></a></p> |
| <p>Driver URL:</p><p><a href="http://msdn.microsoft.com/en-us/sqlserver/aa937724.aspx"><http://msdn.microsoft.com/en-us/sqlserver/aa937724.aspx></a></p>        |                                                                                              |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:sqlserver://\<server>\[:\<port>];DatabaseName= \<databaseName></code></p> | <p>Default Port:</p><p>1433</p>                                                              |
| <p>JDBC Class:</p><p><code>com.microsoft.sqlserver.jdbc. SQLServerDriver</code></p>                                                                             | <p>JDBC JAR File Name:</p><p><code>sqljdbc4.jar</code></p>                                   |
| <p>Comments:</p><p>The open source jtds driver also works with MSSQL.</p>                                                                                       |                                                                                              |

### Teradata

| Vendor Name                                                                                                                                                              | Details                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| Please see the [Teradata JDBC Driver Reference](http://developer.teradata.com/connectivity/reference/jdbc-driver) for information about required drivers.                |                                                                                                |
| Teradata                                                                                                                                                                 | <p>Company URL:</p><p><a href="http://www.teradata.com/"><http://www.teradata.com></a></p>     |
| <p>Driver URL:</p><p><a href="http://downloads.teradata.com/download/connectivity/jdbc-driver"><http://downloads.teradata.com/download/connectivity/jdbc-driver></a></p> |                                                                                                |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:teradata://\<dbshost>\[/\<URL attribute>\[;\<URL attribute>]…]</code></p>          | <p>Default Port:</p><p>N/A</p>                                                                 |
| <p>JDBC Class:</p><p><code>com.teradata.jdbc.TeraDriver</code></p>                                                                                                       | <p>JDBC JAR File Name:</p><p><code>terajdbc4.jar</code></p><p><code>tdgssconfig.jar</code></p> |

### Vertica

{% hint style="info" %}
**Note:** Deprecated beginning in version 11.0.
{% endhint %}

| Vendor Name                                                                                                                                     | Details                                                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Recommended Native Driver                                                                                                                       |                                                                                          |
| HP                                                                                                                                              | <p>Company URL:</p><p><a href="http://www.vertica.com/"><http://www.vertica.com></a></p> |
| <p>Driver URL:</p><p><a href="http://www.vertica.com/support/myvertica/"><http://www.vertica.com/support/myvertica/></a></p>                    |                                                                                          |
| <p>JDBC URL Syntax by Type:</p><ul><li><strong>Server</strong></li></ul><p><code>jdbc:vertica://\<server>\[:\<port>]/\<databaseName></code></p> | <p>Default Port:</p><p>5433</p>                                                          |
| <p>JDBC Class:</p><p><code>com.vertica.Driver</code></p>                                                                                        | <p>JDBC JAR File Name:</p><p><code>N/A</code></p>                                        |

## Install drivers with the JDBC distribution tool

To connect to a database, including the Pentaho Repository database, download and install the JDBC driver:

* In the appropriate Pentaho component directories.
* In the web application server that hosts Pentaho Server.

{% hint style="info" %}
Due to licensing restrictions, Pentaho cannot redistribute some third-party database drivers.\
You must download and install those drivers yourself.
{% endhint %}

1. Download the JDBC driver JAR from your database vendor or a third-party driver developer.
2. Copy the JDBC driver JAR to `pentaho/jdbc-distribution`.
3. Open a command prompt or shell, then run one of these commands:
   * Windows: `distribute-files.bat <jdbc-driver-jar>`
   * Linux: `./distribute-files.sh <jdbc-driver-jar>`
4. If you ran this utility during installation, continue with your install steps.
5. If you ran this utility to connect to a new repository:
   * Restart Pentaho Server and the design tools.
   * Try the connection again.
   * If the connection still fails, verify driver locations below.

| Product                            | JDBC driver location                                |
| ---------------------------------- | --------------------------------------------------- |
| Pentaho Server                     | `pentaho/server/pentaho-server/tomcat/lib`          |
| Pentaho Data Integration (Spoon)   | `pentaho/design-tools/data-integration/lib`         |
| Pentaho Report Designer (PRD)      | `pentaho/design-tools/report-designer/lib/jdbc`     |
| Pentaho Aggregation Designer (PAD) | `pentaho/design-tools/aggregation-designer/drivers` |
| Pentaho Schema Workbench (PSW)     | `pentaho/design-tools/schema-workbench/drivers`     |
| Pentaho Metadata Editor (PME)      | `pentaho/design-tools/metadata-editor/libext/JDBC`  |


# Pentaho Data Integration 10.2

Pentaho Data Integration (PDI) provides the Extract, Transform, and Load (ETL) capabilities that facilitate the process of capturing, cleansing, and storing data using a uniform and consistent format that is accessible and relevant to end users and IoT technologies. If you or your administrator have not already installed PDI on your system, see the **Install Pentaho Data Integration and Analytics** document for details.


# Get started with the PDI client

PDI client (also known as Spoon) is a desktop application that enables you to build transformations and schedule and run jobs.

Common uses of PDI client include:

* Data migration between different databases and applications
* Loading huge data sets into databases taking full advantage of cloud, clustered and massively parallel processing environments
* Data cleansing with steps ranging from very simple to very complex transformations
* Data integration including the ability to leverage real-time ETL as a data source for Pentaho Reporting
* Data warehouse population with built-in support for slowly changing dimensions and surrogate key creation (as described above)

To get started with Pentaho Data Integration, see the following topics:&#x20;

* [Starting the PDI client](https://docs.pentaho.com/pdia-data-integration/get-started-with-the-pdi-client-1/start-the-pdi-client)
* [Use the PDI client perspectives](https://docs.pentaho.com/pdia-data-integration/get-started-with-the-pdi-client-1/use-the-pdi-client-perspectives)
* [Customize the PDI client](https://docs.pentaho.com/pdia-data-integration/get-started-with-the-pdi-client-1/customize-the-pdi-client)


# Starting the PDI client

After you have installed Pentaho Data Integration (PDI), you can use the PDI client (also known as Spoon) desktop application to start building transformations of your data.

Perform the following steps to launch the PDI client from the `Pentaho` directory.

1. Start the Pentaho Server.
2. Navigate to the folder where you have installed PDI. For example `..\pentaho\design-tools\data-integration`.
3. Launch the PDI client in the best way for your operating system.
   * For Windows: Double-click `Spoon.bat`
   * For Linux: Double-click `spoon.sh`
   * For Macintosh: Go to `../pdi-ee/data-integration` and double-click the **Data Integration** icon.
4. If you do not have a license installed, complete the following substeps to install a license:
   1. When the License Manager dialog box appears, click the plus sign (**+**) to open the Add License window.
   2. Select **License Server**, enter either the cloud license server URL or the local license server URL, and then click **OK**.

      The URL for requesting a license from the local license server looks like the following example:

      ![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-becb44ddad1d00511b4d64a4c0481bd0a4bb15b3%2FAdd_License_dialog.png?alt=media)

      **Note:** The **Activation Code** option is only for activating a trial license.
   3. Review the license summary to see which components you are now entitled to use, and then click **Close**.

      ![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-c59eacbf1f16b3bbbeacd9fe7499e7e11330f145%2FPentaho_License_Manager_available_licenses.png?alt=media)

The PDI client application opens on your desktop.


# Use the PDI client perspectives

Pentaho Data Integration (PDI) empowers you with tools that include ETL and scheduling in one unified environment — the PDI client interface. This integrated environment enables you to work in close cooperation with business users to build business intelligence solutions more quickly and efficiently.

When you are working in the PDI client, you can change perspectives to easily switch back and forth from:

* Designing ETL jobs and transformations, and
* Scheduling jobs and transformations.

As users provide you with feedback about how the data is presented to them, you can also quickly make iterative changes to your data directly using our data inspection tools in the PDI client.

From within the PDI client, you can change perspectives using the **Perspective** icon in the toolbar.

![Perspective selection](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-6e92de17c3a0828c3fb9787d554c541bef782ff6%2FPDI%20perspectives%20selection.png?alt=media)

Perspectives in PDI help you focus how you work with different tasks.

## Data Integration perspective

You can use the **Data Integration** perspective to develop ETL programs known as transformations and jobs.

Consider the following example and table as a guide to the major sections of the **Data Integration** perspective.

![Data Integration perspective](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-4cfa1018038682385e44ee0fb889b2b5478176f0%2FPDI_DataIntegrationPerscpective_810.png?alt=media)

In the table below, match the numbered items in the example illustration above to reference the toolbars, buttons, and areas on the PDI client.

| Item | Feature            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Toolbar            | <p>Use this toolbar to access commonly performed actions: - <strong>New file</strong> button ( <img src="https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-48f4e76df70277734bb70c0c1850e436c9aeaf2e%2Fnew.png?alt=media" alt="New file"> ) to create a new job, transformation, database connection, or slave server.</p><ul><li><strong>Open file</strong> button ( <img src="https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-cf6f1dff77b61014c414e4358784c9a467d1e47d%2Fopen.png?alt=media" alt="Open file"> ) to open a transformation or job from a file.</li><li><strong>Explore Repository</strong> button ( <img src="https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-3792b492e0a01dafb452e1fce2d8800cf5137812%2FexploreRepo.png?alt=media" alt="Explore repository"> ) to explore the repositories.</li><li><strong>Save</strong> button ( <img src="https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-ff2686aef2860b058a0ad61d027edba834ab9303%2Fsave.png?alt=media" alt="Save"> ) to save the current transformation or job to a file or repository.</li><li><strong>Save As</strong> button ( <img src="https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-d17950df32cf6e9abf7c1fa3f1c134346dba37b5%2Fsaveas.png?alt=media" alt="Save as"> ) to save the transformation or job under a different file name or type.</li><li><p><strong>Perspectives</strong> button ( <img src="https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-79c8ac0d0c554378d00406237f8b015ba1ba0aff%2FssPDI_PerspectivesMenu.png?alt=media" alt="Perspectives"> ) to switch between the different perspectives:</p><ul><li><a href="../data-integration-perspective-in-the-pdi-client">Data Integration Perspective</a>: Create ETL transformations and jobs.</li><li><a href="../schedule-perspective-in-the-pdi-client">Schedule Perspective</a>: Manage scheduled ETL activities on the Pentaho Server.</li></ul></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 2    | **Connect** button | Use this button to access the menu to create and connect to [repositories](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi) for central storage of your ETL jobs and transformations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 3    | Sub-toolbar        | <p>Use this toolbar to perform transformation or job actions:- <strong>Run</strong> button ( <img src="https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Get%20started%20with%20the%20PDI%20client/Get%20Started%20with%20the%20PDI%20Client/Use%20the%20PDI%20client%20perspectives/run=GUID-F89218F0-85FF-4F8B-A549-621FFE08FBC5=1=en=Low.png" alt=""><img src="https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-d09177e8c070afa1bd717685fc58ed7c42e1932e%2F9x9_arrow_down.png?alt=media" alt="Run"> ) to run a transformation or job:<br>- <strong>Run</strong>: Runs the current transformation or job from an XML file or a repository.<br>- <strong>Run Options</strong>: Sets the <strong>Run Options</strong> and then runs the current transformation or job from an XML file or a repository.</p><ul><li><strong>Pause</strong> button ( <img src="https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-25241ef690e0ad8f1c86418bd7d31cd1a6805dc7%2Fpause.png?alt=media" alt="Pause"> ) to pause a running transformation or job.</li><li><p><strong>Stop</strong> button ( <img src="https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Get%20started%20with%20the%20PDI%20client/Get%20Started%20with%20the%20PDI%20Client/Use%20the%20PDI%20client%20perspectives/stop=GUID-7D68E089-E5A2-4B8F-ACDA-789F249F7659=1=en=Low.png" alt=""><img src="https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-d09177e8c070afa1bd717685fc58ed7c42e1932e%2F9x9_arrow_down.png?alt=media" alt="Stop"> ) to stop a running transformation or job:</p><ul><li><strong>Stop</strong>: Stops the transformation or job immediately.</li><li><strong>Stop input processing</strong>: Stops the input steps to the transformation or job, while allowing any records already retrieved or initiated to be processed and then stopped.</li></ul></li><li><strong>Preview</strong> button ( <img src="https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-da70646f8f586d95a3bbb6aec085ce30fb7c0fe9%2Fpreview.png?alt=media" alt="Preview"> ) to run the transformation in preview mode to examine the rows produced by the selected steps.</li><li><strong>Debug</strong> button ( <img src="https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-26ef1e6b5c9e2578abfe87321856dc63c0feab80%2Fdebug.png?alt=media" alt="Debug"> ) to run the transformation in debug mode to troubleshoot execution errors.</li><li><strong>Replay</strong> button ( <img src="https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-89d999d6283447f10f61b384070b10f5f263737e%2Freplay.png?alt=media" alt="Replay"> ) to replay the processing of a transformation.</li><li><strong>Verify</strong> button ( <img src="https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-bd836520b9a02d9934c30e6d4efb70740a775458%2Fcheck.png?alt=media" alt="Verify"> ) to verify the transformation.</li><li><strong>Analyze</strong> button ( <img src="https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-3467f492ff37c1532afab9e6cc40b8679d6e8f50%2Fimpact.png?alt=media" alt="Analyze"> ) to run an impact analysis on the database.</li><li><strong>SQL</strong> button ( <img src="https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-577893d443a7afa70b65ba68816c3a2147dbfa43%2FSQLbutton.png?alt=media" alt="SQL"> ) to generate the SQL that is needed to run the loaded transformation.</li><li><strong>Explore DB</strong> button ( <img src="https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Get%20started%20with%20the%20PDI%20client/Get%20Started%20with%20the%20PDI%20Client/Use%20the%20PDI%20client%20perspectives/exploredb=GUID-DD4D4C73-05D1-4638-AA44-44A4B1E9E403=1=en=Low.png" alt=""> ) to launch the <a href="../data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/use-the-database-explorer">Database Explorer</a> to perform actions such as preview data, run SQL queries, and generate DDL.</li><li><strong>Results</strong> button ( <img src="https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-7ccadc86e81fd402f1a662c2bfa71c4efc1350df%2Fshow-results.png?alt=media" alt=""> ) to show the <strong>Execution Results</strong> pane.</li><li><strong>Lock</strong> button ( <img src="https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-3812762a1a360fd76ceef66eed127f93f7cc6b14%2Flock.png?alt=media" alt=""> ) to lock the transformation.</li></ul> |
| 4    | Explore pane       | <p>Use this pane to access the <strong>Design</strong> and <strong>View</strong> tabs:- The <strong>Design</strong> tab provides a list of steps or entries that are used to build transformations or jobs.</p><ul><li>The <strong>View</strong> tab provides information about available database connections and the steps and hops used for the transformation or job.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 5    | Canvas             | Use this canvas for designing and building transformations and jobs for the ETL activities you want to perform.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

See [Data Integration perspective in the PDI client](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client) for more details and instructions.

## Scheduler perspective

You can plan when to run transformations and jobs and set timed intervals to automatically send the output to your preferred destinations. See [Schedule a transformation or job](https://docs.pentaho.com/pdia-data-integration/schedule-perspective-in-the-pdi-client/schedule-a-transformation-or-job) for more details.

![Scheduler perspective](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-d15742b8d92df473ae1c549cb29d4b6ddc12428c%2FPDI%20scheduler%20perspective.png?alt=media)

The table below outlines the features in the Scheduler perspective. See [Scheduler perspective in the PDI client](https://docs.pentaho.com/pdia-data-integration/schedule-perspective-in-the-pdi-client) for details.

| Item | Feature               | Description                                                                                       |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------- |
| 1    | **Perspectives** icon | Allows you to switch between perspectives in PDI.                                                 |
| 2    | Scheduler toolbar     | Provides single-click access to common actions such as edit, refresh, enable, disable, or delete. |
| 3    | Schedules table       | Contains a list of schedules.                                                                     |

<br>


# Customize the PDI client

The PDI client allows you to customize certain aspects of its behavior, along with the look and feel of the interface. The following table describes each of these options, which can be accessed from the menu bar: Go to **Tools** > **Options**, then in the Kettle Options dialog box, select the **Look & Feel** tab.

| **Option**                               | **Description**                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Fixed width font**                     | This option customizes the font that is used in the dialog boxes, trees, input fields, and more; click **Edit** to edit the font or **Delete** to return the font to its default value.                                                                                                                                                                                                        |
| **Font on workspace**                    | This option customizes font that is used in the PDI client interface; click **Edit** to edit the font or **Delete** to return the font to its default value.                                                                                                                                                                                                                                   |
| **Font for notes**                       | This option customizes the font used in notes that are displayed in the PDI client; click **Edit** to edit the font or **Delete** to return the font to its default value.                                                                                                                                                                                                                     |
| **Background color**                     | This option sets the background color in the PDI client and affects all dialog boxes; click **Edit** to edit the color or **Delete** to return the background color to its default value.                                                                                                                                                                                                      |
| **Workspace background color**           | This option sets the background color in the graphical view of the PDI client; click **Edit** to edit the background color or **Delete** to return the background color to its default value.                                                                                                                                                                                                  |
| **Tab color**                            | This option customizes the color that is being used to indicate tabs that are active/selected; click **Edit** to edit the tab color or **Delete** to return the color to its default value.                                                                                                                                                                                                    |
| **Icon size in workspace**               | Affects the size of the icons in the graph window. The original size of an icon is 32x32 pixels. The best results (graphically) are probably at sizes 16,24,32,48,64 and other multiples of 32.                                                                                                                                                                                                |
| **Line width on workspace**              | Affects the line width of the hops in the PDI client graphical view and the border around the step.                                                                                                                                                                                                                                                                                            |
| **Shadow size on workspace**             | If this size is larger than 0, a shadow of the steps, hops, and notes is drawn on the canvas, making it look like the transformation floats above the canvas.                                                                                                                                                                                                                                  |
| **Dialog middle percentage**             | By default, a parameter is drawn at 35% of the width of the dialog box, counted from the left. You can change using this option in instances where you use unusually large fonts.                                                                                                                                                                                                              |
| **Canvas Grid Size**                     | Indicates the size of the grid on the PDI client canvas.                                                                                                                                                                                                                                                                                                                                       |
| **Show Canvas Grid**                     | Enabling this option will show a dotted grid on the PDI client canvas.                                                                                                                                                                                                                                                                                                                         |
| **Canvas anti-aliasing**                 | Some platforms like Windows, OSX and Linux support anti-aliasing through GDI, Carbon or Cairo. Enable this option for smoother lines and icons in your graph view. If you enable the option and your environment does not work, change the value for option **EnableAntiAliasing** to `N` in file `*$HOME*/.kettle/.spoonrc` (`C:\Documents and Settings\<user>\.kettle\.spoonrc` on Windows). |
| **Show bottleneck transformation steps** | If a step in the transformation is processing slowly, a graphic displays around that step to make the bottleneck visible.                                                                                                                                                                                                                                                                      |
| **Use look of OS**                       | Enabling this option on Windows allows you to use the default system settings for fonts and colors in the PDI client. On other platforms, the default is always enabled.                                                                                                                                                                                                                       |
| **Show branding graphics**               | Enabling this option will draw Pentaho Data Integration branding graphics on the canvas and in the left-hand side "expand bar."                                                                                                                                                                                                                                                                |
| **Preferred Language**                   | Specifies the preferred language setting.                                                                                                                                                                                                                                                                                                                                                      |
| **Alternative Language**                 | Specifies the alternative language setting. Because the original language in which Pentaho Data Integration was written is English, it is best to set this locale to English.                                                                                                                                                                                                                  |


# Use a Pentaho Repository in PDI

The PDI client (also known as Spoon) offers several different types of file storage. A Pentaho Repository stores transformations, jobs, and schedules in a central environment through the Pentaho Server. It is recommended for enterprise deployments and fully supported features.

If your team needs a collaborative ETL (Extract, Transform, and Load) environment, we recommend using one or more than one Pentaho Repository. In addition to storing and managing your jobs and transformations, A Pentaho Repository provides full revision history for you to track changes, compare revisions, and revert to previous versions when necessary. These features, along with enterprise security and content locking, make using a Pentaho Repository an ideal platform for collaboration.

You can use the following information in the **Administer Pentaho Data Integration and Analytics** document to help to extend your knowledge of a Pentaho Repository beyond basic setup and use:

* [Create a connection in the PDI client](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/create-a-connection-in-the-pdi-client)
* [Connect to a Pentaho Repository](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/connect-to-a-pentaho-repository)
* [Manage repositories in the PDI client](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/manage-repositories-in-the-pdi-client)
* [Unsupported repositories](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/unsupported-repositories)
* [Use the Repository Explorer](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer)

## Advanced topics

To extend your knowledge of a Pentaho Repository beyond basic setup and use, see the following topics in the [Administer Pentaho Data Integration and Analytics](https://app.gitbook.com/s/TSPdUdWBWVGi0uurnXBG/) guide:&#x20;

* [**Import and export PDI content**](https://app.gitbook.com/s/TSPdUdWBWVGi0uurnXBG/manage-the-pentaho-system/manage-the-pentaho-repository/import-and-export-pdi-content)

  Repository content can also be imported and exported through either the PDI client or a command line interface.
* [**Purge transformations, jobs, and shared objects from the Pentaho Repository**](https://app.gitbook.com/s/TSPdUdWBWVGi0uurnXBG/manage-the-pentaho-system/manage-the-pentaho-repository/purge-transformations-jobs-and-shared-objects-from-the-pentaho-repository)

  If the Pentaho Repository becomes too large for effective system performance, consider purging some of the data.
* [**Backup and restore a Pentaho Repository**](https://app.gitbook.com/s/TSPdUdWBWVGi0uurnXBG/manage-the-pentaho-system/manage-the-pentaho-repository/backup-and-restore-pentaho-repositories)

  Perform routine backups to minimize potential data loss through machine failure, theft, disaster, or accidental change.


# Create a connection in the PDI client

To access the repository items through the PDI client, perform the following steps to create a connection to a Pentaho Repository:

1. Verify the Pentaho Server is running, and then start the PDI client.
2. Click **Connect** in the upper right corner of the PDI client toolbar.

   The **Repository Manager** dialog box opens.

   **Note:** If **Connect** is replaced by a different link name, you are already connected to a repository.
3. Click **Add**.
4. Select from the following options:
   * **Pentaho Repository** - Uses a central environment through the Pentaho Server to store transformations, jobs, and schedules. This is the recommended repository to be used.
   * **File Repository** - Uses your local file system to store the metadata.
   * **Database Repository** - Uses a central relational database to store your ETL metadata.**Note:** Database and file repositories are not supported or recommended for production use.
5. Enter or update the **Display Name** property.
6. Modify the URL associated with your repository, if necessary.
7. (Optional) Provide description in the **Description** field.
8. Click **Save** to create repository.

   The repository is created and is listed in the Repository Manager dialog box.

You can either click **Connect**, to connect to the repository, or click **Close** to close the dialog box. If you chose to connect, see [Connect to a Pentaho Repository](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/connect-to-a-pentaho-repository) and follow the procedure from step 2.

If you choose to close, you can connect to the repository later through the menu next to the **Connect** link in the upper right corner of the PDI client toolbar.


# Connect to a Pentaho Repository

After a repository is created, a menu appears next to the Connect link. You can use this menu to connect to the repository.

1. Select a repository in the **Connect** menu.

   **Note:** If you are in the process of creating your first repository, select the repository after creating it, and then click Connect in the Repository Manager dialog box.
2. Log on to the repository by entering your **User Name** and **Password** credentials. For example, **User Name** = `admin`, **Password** = `password`.
3. Click **Login**.

   **Note:** If the connection fails, ensure that the port number and URL are correct.

   Your username and repository display name appears in the top right corner of the PDI client toolbar.

   **Note:** To make the Repository Connection window appear automatically when the PDI client starts, go to **Tools** > **Options** and click **Show repository dialog at startup**.


# Manage repositories in the PDI client

After a repository is created, a menu appears next to the **Connect** link. You can use the menu to connect to any repository you created. If you connect to a repository, the **Connect** link in the PDI client toolbar is replaced by your user name and the display name of the repository.

This menu can also be used to access the Repository Manager or disconnect from your current repository.

## Repository Manager

You can **Add**, **Edit**, or **Delete** your repositories through the Repository Manager dialog box.

![Repository Manager dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-0e11da904b1a05a687555fd9d40bacff3565e7ec%2FssPDIRepository_Manager_9.4.png?alt=media)

If you set a repository as the default on startup, you can clear this behavior by checking **Launch connection on startup** again.

You can also click on an item in the list to select it. Once selected, you can either **Edit** or **Delete** that repository. If you choose **Edit**, the Connection Details dialog box will appear.

## Connection details

Use the Connection Details dialog box to specify the settings of your repository.

| Setting                          | Description                                                                                                                                                                                        |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Display Name**                 | Identifies the repository within the PDI client.                                                                                                                                                   |
| **URL**                          | Defines the web address of the repository. The default value is `http://localhost:8080/pentaho`. You can change this setting to any web address pertaining to your specific collaboration project. |
| **Description**                  | Describes the repository, such as its type and any other useful information.                                                                                                                       |
| **Launch connection on startup** | Indicates the repository should open by default when starting the PDI client.                                                                                                                      |


# Unsupported repositories

You can also create either a database repository (which uses a central relational database to store your ETL metadata) or a file repository (which uses your local file system to store the metadata). You can create these types of repositories through the **Other Repositories** link in the Pentaho Repository welcome dialog box.

From the Other Repositories dialog box, you can **Get Started** by selecting either the **Database Repository** or the **File Repository** from the list.

**Note:** Database and file repositories are not supported or recommended for production use.

## Database repository

Similar to the Pentaho Repository, you connect to the database repository by entering a **Display Name** into the Connection Details dialog box. After specifying a name, you need to select **Database Connection**, which leads to a list in the Select a database connection dialog box. From this dialog box, you can either create a new database, or **Edit** and **Delete** an existing connection. When you create a new connection or **Edit**, the Database Connection dialog box appears. Use this dialog box to specify your database connection, then select **Test** and click **OK**. In the Select a database connection dialog box, click on what database connection you want to use and then go **Back** to the Connection Details dialog box. After **Display Name** and the **Database Connection** are specified, click **Finish** to test the connection to repository.

## File Repository

Besides entering in a **Display Name**, you will need to specify the **Location** of the local file system that you want to use as a file repository. You can **Browse** to this location from the Connection Details dialog box. After you specify a repository name and file system location, you can click **Finish** to test the connection. Unlike with other repositories, when you connect to a file repository, the link in the upper right corner will only show the display name of file repository.


# Use the Repository Explorer

You can manage your [repository](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi) content in the **Browse** tab of the Repository Explorer window.

* [Access the Repository Explorer window](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/access-the-repository-explorer-window)
* [Create a new folder in the repository](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/create-a-new-folder-in-the-repository)
* [Open a folder, job, or transformation](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/open-a-folder-job-or-transformation)
* [Rename a folder, job, or transformation](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/rename-a-folder-job-or-transformation)
* [Delete a folder, job, or transformation](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/delete-a-folder-job-or-transformation)
* [Move objects](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/move-objects)
* [Restore objects](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/restore-objects)
* [Use Pentaho Repository access control](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/use-pentaho-repository-access-control)
* [Use version history](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/use-version-history-cp)


# Access the Repository Explorer window

To access the Repository Explorer window, perform the following steps:

1. Connect to a repository. To learn how to do this, see [Use a Pentaho Repository in PDI](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi).
2. Select **Tools** > **Repository** > **Explore**.
3. The Repository Explorer window appears.

   **Note:** Permissions set by your administrator determine what you are able to view and tasks you are able to perform in the repository.

   ![Repository Explorer window](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-f2cd0270b2d8c01b140f8f6cdddc4a167f3c8461%2FRepositoryExplorerWindow.png?alt=media)

   **Note:** If you are trying to use LDAP authentication security and the Repository Explorer is empty when it opens, your [security settings need to be updated to the LDAP authentication](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/broken-reference).

### With LDAP authentication, the PDI Repository Explorer is empty

If you log on to a solution repository from the PDI client before you switch authentication to LDAP, then the repository IDs and security structures will be broken. You will not see an error message, but the solution repository explorer will be empty and you will not be able to create new folders or save PDI content.

To fix the problem, you will have to delete the security settings established with the previously used authentication method, which will force the Pentaho Server to regenerate them for LDAP.

**Note:** Following this procedure will destroy any previously definedPentaho Repository users, roles, and access controls. You should back up the files that you delete in these instructions.

1. Stop the Pentaho Server.
2. Delete the security and default directories from the following directory: `/pentaho-solutions/system/jackrabbit/repository/workspaces/`
3. Start the Pentaho Server.

You should now have a proper LDAP-based Pentaho Repository that can store content and create new directories.


# Create a new folder in the repository

To create a new folder in the repository, perform the following steps:

1. In the **Browse** tab in the Repository Explorer window, right-click on the folder that you want to create the new folder under.

   For example, if you want to create a new folder under `public`, right-click the `public` folder.
2. Select **New Folder**.
3. Enter the name for the new folder in the Name New Folder window.
4. Click **OK**.


# Open a folder, job, or transformation

Perform the following steps to open a folder, job, or transformation:

1. Right-click on the folder, job, or transformation.
2. Select **Open**.

   **Note:** To select more than one file, hold down the CTRL or the SHIFT key as you select the folders, jobs, or transformations, then right-click and select **Open**.


# Rename a folder, job, or transformation

Perform the following steps to rename a folder, job, or transformation in the Repository Explorer window:

1. In the **Browse** tab in the Repository Explorer window, right-click the folder, job, or transformation and select **Rename**.
2. Enter the new name in the Name window that appears.
3. Click **OK**.
4. Enter a comment when prompted.
5. Click the **OK** button.

In the **Version History** tab, a comment appears that indicates that the file has been renamed.


# Delete a folder, job, or transformation

Perform the following steps to delete a folder, job, or transformation in the Repository Explorer window:

1. In the **Browse** tab in the Repository Explorer window, right-click the folder, job, or transformation and select **Delete**.
2. Click **Yes** when the warning message appears.
3. Click **OK**.

   **Note:** To select more than one file, hold down the CTRL or the SHIFT key as you select the folders, jobs, or transformations, then right-click and select **Delete**.


# Move objects

Perform the following steps to move objects, such as folders, jobs, or transformations:

1. In the repository, select the object.
2. Click-and-drag the object to the desired location in the navigation pane on the left.

   You can move an object in your folder to the folder of another repository user.

   **Note:** To select more than one file, hold down the CTRL or the SHIFT key as you select the folders, jobs, or transformations, then right-click and select **Move**.


# Restore objects

Perform the following steps to restore an object you deleted:

1. Double-click the **Trash** icon.

   The object(s) you deleted appear in the right pane.
2. Right-click on the object you want restored, and select **Restore** from the menu.


# Use Pentaho Repository access control

You can control access to your [repository](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi) by locking files, establishing connection security, and restricting folder permissions.&#x20;

## Lock and unlock jobs and transformations

You can lock or unlock jobs and transformations. Locking and unlocking jobs and transformations protect them from being edited by other users.

### Lock a job or transformation

To lock a job or transformation, complete these steps:

1. In the **Browse** tab in the Repository Explorer window, right-click the job, or transformation and select **Lock**.
2. Enter the notes in the Lock Notes window that appears.
3. Click **OK**.

   The job or transformation icon changes to show a padlock.

   **Note:** The lock status icons are updated on each PDI client only when the Repository Explorer is accessed. If you want to refresh lock status in the Repository Explorer, exit and access it again. Also, to select more than one file, hold down the CTRL or the SHIFT key as you select the folders, jobs, or transformations.

   ![Locked status icon](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-9d90e42782e4c5108f6c6bdc37d0e89d181841f9%2Flockicon.png?alt=media)

### View lock notes

To view notes that were entered when the job or transformation was locked, do these things:

1. In the **Browse** tab in the Repository Explorer window, right-click the job, or transformation and select **Lock Notes**.

   The lock note appears in a pop-up window.
2. Click **OK** to dismiss the note.

### Unlock a job or transformation

To unlock a job or transformation, complete these steps:

1. In the **Browse** tab in the Repository Explorer window, right-click the job, or transformation,
2. Select **Lock**.

   The icon for the job or transformation returns to normal; the padlock icon disappears.

   **Note:** To select more than one file, hold down the CTRL or the SHIFT key as you select the folders, jobs, or transformations.

## Access connection, security, and cluster information

In addition to managing content such as jobs and transformations, click the **Connections** tab to manage (create, edit, and delete) your database connections in the Pentaho Repository. See [Manage repositories in the PDI client](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/manage-repositories-in-the-pdi-client) for more information about connecting to a database.

Click the **Security** tab to manage users and roles. Pentaho Data Integration comes with a default security provider. If you do not have an existing security such as LDAP or MSAD, you can use Pentaho Security to define users and roles. You must have administrative privileges to manage security. For more information, see the **Administer Pentaho Data Integration and Analytics** document.

![Security tab, Repository explorer](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-3265d56448dd5ef7fea2d41fe2d81d691a7bd263%2Fpermissions.png?alt=media)

You can manage your slave servers (Pentaho and Carte instances) by clicking the **Slaves** tab. See [Initialize Slave Servers](https://docs.pentaho.com/pdia-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/initialize-slave-servers) for instructions.

Click the **Partitions** and **Cluster** tabs to manage partitions and clusters. See [Create a cluster schema](https://docs.pentaho.com/pdia-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/create-a-cluster-schema) for more information.

## Set folder-level permissions

The following table explains the permissions settings for Pentaho Repository content and folders:

| Type                      | Value                                                                                              |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Read**                  | If set, the content of the file or contents of the directory will be accessible. Allows execution. |
| **Manage Access Control** | If set, access controls can be changed for this object.                                            |
| **Write**                 | If set, enables read and write access to the selected content.                                     |
| **Delete**                | If set, the content of the file or directory can be deleted.                                       |

**Note:** You must assign both **Write** and **Manage Access Control** to a directory in order to enable the selected user to create subfolders and save files within the folder.

You can assign any of these permissions to files and folders stored in a Pentaho Repository. Setting permissions manually overrides inherited permissions if the access control flags allow.

Perform the following steps to set folder-level permissions:

1. Open the Repository Explorer (**Tools** > **Repository** > **Explore**).
2. Navigate to the folder to which you want permissions set and click to select it.

   The folder must appear in the right pane before you can set permissions.
3. In the lower pane, under the **Permissions** tab, disable **Inherit security settings from parent**.
4. Click **Add** to open the Select User or Role dialog box.
5. Select a user or role to add to the permission list.
   1. Use the yellow arrows to move the user or role in or out of the permissions list.
   2. Click **OK** when you are done.
6. In the lower pane, under the **Access Control** tab, enable the appropriate **Permissions** granted to your selected user or role.

   If you change your mind, use **Delete** to remove users or roles from the list.
7. Click **Apply** to apply permissions.


# Use version history

Retaining a [repository](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi) version history enables you to show what is different from one version to another, or to restore a previous version if you want to revert back to a specific point in time. By default, each time you save in PDI, a version of your file is committed to the repository.

## Use version history

Versions of a file can be tracked through the Repository Explorer in the PDI client (Spoon). These versions are listed in a tab of the explorer.

To access this version history tab:

1. In the PDI client menubar, go to **Tools** > **Repository** > **Explore**.

   The Repository Explorer window opens to the **Browse** tab.
2. In the left navigation panel of the **Browse** tab, locate and click on a folder to access the file containing your transformation or job.
3. Select your file when it appears in the upper right panel. The versions of this file are shown under the **Version History** tab in the lower right panel.

   ![Version History tab, Repository explorer window](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-faff923279154658ca2f5dc63d2e80c68a6cd7ce%2FssPDIRepository_ExplorerVersionHistoryTab.png?alt=media)

   You can use this history to:

   * [Open a version of a file](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/broken-reference)
   * [Restore a version of a file](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/broken-reference)\
     While saving a file, you are prompted to provide comments. These comments are also included in the **Version History** tab.

   This tab appears in the explorer when version history tracking is enabled. The tab is hidden with tracking is disabled. You can enable or disable tracking of version history and comments through a properties file. See [Enable or disable tracking of version history and comments](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/broken-reference) for more details.

## Open a version of a file

If you want to show differences between each version or you need to remember the details of previous changes, you can open it through the **Version History** tab.

To open a version of a file:

1. Right-click on a version under the **Version History** tab in the Repository Explorer.
2. Choose **Open** to access that version in the PDI client.

It opens as a separate file with the same name but the version number is added to the title on the PDI client canvas tab. If the current version of the file is already open in the PDI client, the latest version number is appended to its title.

## Restore a version of a file

If you do not like a change you made to your file, you can choose to restore to a previous version based on your descriptive comments. You must have administrator privileges to restore a version of a file.

1. Right-click on a version under the **Version History** tab in the Repository Explorer.
2. Select **Restore**.

   ![Restoring a file](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-cb63625056510388872630fd4d87a1ff713903bc%2FssPDIRestoring_a_Previous_Version.png?alt=media)
3. Follow the remaining prompts and click **OK**.

The restored version becomes the latest version of your file. The next time you open the file, you will see the restored version as the most recent one along with all the previous versions.

![Restoring a file result](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-36c26ec28d09c0cdd73f92284cd73b3daddfe7c0%2FssPDIResults_of_Restoring_a_Previous_Version.png?alt=media)

## Enable or disable tracking of version history and comments

You can enable or disable tracking of version history or comments for all users by modifying the **versioningEnabled** and **versionCommentsEnabled** fields within the `server/pentaho-server/pentaho-solutions/system/repository.spring.properties` text file:

| Action (All Users)           | Status                        | Final Setting                  |
| ---------------------------- | ----------------------------- | ------------------------------ |
| **Version History Tracking** | Off                           | `versioningEnabled=false`      |
| On                           | `versioningEnabled=true`      |                                |
| **Comment Tracking**         | Off                           | `versionCommentsEnabled=false` |
| On                           | `versionCommentsEnabled=true` |                                |

When you disable version history tracking, comments are automatically no longer tracked.

To enable or disable tracking:

1. Exit the PDI client.
2. Stop the Pentaho Server.
3. Open the `server/pentaho-server/pentaho-solutions/system/repository.spring.properties` file in a text editor.
4. Change the fields to enable or disable either version history or comment tracking.
5. Start the Pentaho Server.
6. Start the PDI client.


# Scheduler perspective in the PDI client

When you are finished [designing your PDI jobs and transformations](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client) and have saved them in the PDI Server, you can schedule them to run at specific times.

All your active scheduled jobs and transformations are listed in the schedules table in PDI, which you can get to by clicking the **Perspectives** icon (Item 1 below) and then selecting **Scheduler** in the menu.

The schedules table shows which jobs and transformations are scheduled to run, the recurrence pattern for the schedule, when it was last run, when it is set to run again, and the current state of the schedule.

**Note:** You can also create your own schedule using `cron` on Linux, the `Task Scheduler` on Windows, or the `at` command on Windows. If you do this, you will need to call the schedule using Pan or Kitchen commands.

![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-d15742b8d92df473ae1c549cb29d4b6ddc12428c%2FPDI%20scheduler%20perspective.png?alt=media)

You can use the icons in the PDI scheduler toolbar (Item 2, above) to edit and maintain each of your schedules, as described in the following table.

| Icon                                                                                                                                                                                                                         | Name                     | Function                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| ![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-edacc6afd0cc54500d8de6392aefc2679cd11732%2FRefresh.png?alt=media)                       | **Refresh**              | Refreshes the list of schedules.                                                                                    |
| ![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-02b1c7613e41093018c68f2a9a4ea8e1d28acd2b%2FStart%20Scheduled%20Task.png?alt=media)      | **Start Scheduled Task** | Starts scheduled transformations or jobs.                                                                           |
| ![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-6548ba471f06acf4319b9169184cfd372f715b61%2FStop%20Scheduled%20Task.png?alt=media)       | **Stop Scheduled Task**  | Stops a running schedule or schedules at will.                                                                      |
| ![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-f16c971dea795f15dd710d6354d819b1e05104e7%2FStart%20Scheduler.png?alt=media)             | **Start Scheduler**      | Resumes a previously stopped schedule.                                                                              |
| ![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-6fdf6f7b4b13c00b88d52b93763fc87aa1f717a7%2FPause%20Scheduler.png?alt=media)             | **Stop Scheduler**       | Stops a specified schedule. Use **Start Scheduler** to resume a paused schedule.                                    |
| ![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-a35fdd633d4a6fe74f155b1402d5a734ef1d9c29%2FPDI%20Edit%20Scheduled%20Task.png?alt=media) | **Edit Scheduled Task**  | Edits the details of an existing schedule.                                                                          |
| ![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-45e2ce84488aa9127aca96466a464463d847414c%2FRemove.png?alt=media)                        | **Remove**               | Deletes a specified schedule. If the schedule is currently running, it continues to run, but it will not run again. |

You can use the schedules table (Item 2, above) for information about a scheduled item. The columns in the table are described below. You can click the column name to sort content alphabetically in ascending or descending order.

| Column                                                                                     | Description                                                                           |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| **Schedule Name**                                                                          | Lists your schedules by the name you assign to them.                                  |
| **Repeats\***                                                                              | Describes how often the schedule is set to run.                                       |
| **Type**                                                                                   | Displays the file type associated with the schedule.                                  |
| **Source File**                                                                            | Displays the name of the file associated with the schedule.                           |
| **Parameters and Variables**                                                               | Displays the parameter name(s) and variable(s) assigned in the transformation or job. |
| **Last Run (duration)\***                                                                  | Shows the last time, date, and duration when the schedule was run.                    |
| **Next Run\***                                                                             | Shows the next time and date when the schedule will run again.                        |
| **Owner**                                                                                  | Displays the owner of the file associated with the schedule.                          |
| **Status**                                                                                 | Indicates the current state of the schedule, which can be NORMAL or PAUSED.           |
| \* The time and time zone are specified by the user when creating or editing the schedule. |                                                                                       |


# Schedule a transformation or job

You can schedule transformations and jobs to run at specific times by performing the following steps:

1. Connect to the Pentaho Repository.
2. Open a job or transformation from the Pentaho Repository, then select **Action** > **Schedule**. The Schedule window appears.

   ![Schedule window](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-fc2b9da197136eecda7414246cb84f21ef79396a%2Fscheduler.png?alt=media)
3. In the **Start** section, either select **Now** to schedule a transformation or job to run immediately, or select **Date**, and then enter a date, time, and time zone to run it later.
4. In the **Repeat** section, either select **Run Once** to run the transformation or job once or select **Seconds**, **Minutes**, **Weekly**, **Hourly**, **Monthly**, or **Yearly** to run it at regular intervals.
5. In the **End** section, either select **No end** to indicate that the schedule will never expire, or select **Date** to enter a schedule expiration date.
6. To run the scheduled transformation or job in safe mode, select the **Enable Safe Mode** checkbox.

   Safe mode checks every row that passes through the stream to ensure that all layouts are the same as the first row. If the layout differs, an error is generated and reported.
7. Select the **Log Level**.

   Logging levels are addressed in detail in the [Logging levels](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/logging-levels) article.
8. If you have specified parameters, variables, or arguments in a transformation or job, they appear in the bottom part of the window. Adjust values as needed.
9. When done, click **OK**.

   **Note:** If you want to access a Google Drive via your scheduled transformation, copy the **StoredCredential** token into the `pentaho-server/pentaho-solutions/system/kettle/plugins/pentaho-googledrive-vfs/credentials` directory on your Pentaho Server. See [Access to a Google Drive](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/vfs-browser-connecting-to-virtual-file-systems/access-to-a-google-drive) for information on how to obtain a **StoredCredential** token.


# Edit a scheduled run of a transformation or job

To edit a scheduled run of a transformation or job, perform the following steps:

1. Select the **Scheduler** perspective from the **Perspectives** menu in the **Spoon** toolbar.
2. Select the schedule, then click the **Edit Scheduled Task** icon.


# Stop a schedule from running

To stop a scheduled run of a transformation or job, perform the following steps:

1. Select the **Scheduler** perspective from the **Perspectives** menu in the **Spoon** toolbar.
2. Select the schedule that you want to stop, then click the **Stop Scheduled Task** icon.


# Enable or disable a schedule from running

To enable or disable a scheduled run of a transformation or job, perform the following steps:

1. Select the **Scheduler** perspective from the **Perspectives** menu in the **Spoon** toolbar.
2. Select the schedule you want to enable, then click the **Start Scheduler** icon.
3. If you want to disable the schedule, click the **Stop Scheduler** icon.


# Delete a scheduled run of a transformation or job

To delete a scheduled run of a transformation or job, perform the following steps:

1. Select the **Scheduler** perspective from the **Perspectives** menu in the **Spoon** toolbar.
2. Select the schedule you want to delete, then click the **Remove** icon.


# Refresh the schedule list

To refresh the scheduled transformation and jobs list, perform the following steps:

1. Select the **Scheduler** perspective from the **Perspectives** menu in the Spoon toolbar.
2. Click the **Refresh** icon to update the list.


# Streaming analytics

With streaming analytics, you can constantly perform statistical analysis while moving within a data stream.

You can use streaming analytics to manage, monitor, and record real-time analytics of live streaming data so you can quickly extract the necessary information from big volumes of data to react to changing conditions in real time. Businesses generate continuous data from the following sources:

* Log files generated by customers using mobile or web applications, e-commerce purchases, and in-game player activity.
* Telemetry, such as data from connected devices, sensors, and instrumentation in data centers.
* Data collected from social networks, financial trading systems, and geospatial services.

Once collected, the streaming data values from these sources will be processed sequentially and incrementally on a record-by-record basis or a time-based sliding window. Ingesting a window of values allows for both processing and analysis of the data, such as through correlating, aggregating, filtering, and sampling. The following figure is an example of a time-based sliding window.

![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-df0afcfbc2c4cf82f7322b2979cdc4bbd76fd02c%2FStreaming_Analytics_Flow_-_Revised.png?alt=media)

Companies use this information to gain insights into their business and customer activity, such as service usage for billing rates, server activity, website clicks, and geo-locations of devices, people, or physical goods. For example, businesses can track changes in public sentiment on their brands and products by continuously monitoring and analyzing social media streams, and then quickly respond as needed.

The Internet of Things (IoT) also creates large stores of streaming data. Smart objects, such as cars, appliances, and electronic devices, produce data points throughout their operations, activities, and behaviors. Businesses can analyze these points in the data streams to reduce operating costs, improve product reliability, or optimize usage models. For example, you can monitor equipment performance based on its data output. Continuous pattern detection finds anomalies referred to as data gaps. These gaps help to pinpoint when to buy material, plan modifications, and staff personnel.

IoT devices and communication protocols, including text data and transmissions from both legacy and modern equipment sensors, for example, create streaming data of various formats. These multiple formats must be normalized, cleansed, and standardized to process individual events in-memory. Data must be continually corrected and assessed in windows before analysis.

Before you can use streaming analytics, you must ingest the data into PDI as it is received. Within PDI, you can also send event messages to trigger a process of Extract, Transform, and Load (ETL) alerts.


# Get started with streaming analytics in PDI

Pentaho Data Integration (PDI) products are designed to work as if data flows like running water. You can think of PDI as a series of pipes through which water flows and is joined and mixed with other flows. No matter how big the source, the water keeps flowing, such that all the data will be processed if the data keeps flowing. The size of the “pipe” in PDI is directly linked to the number of data records and to the amount of memory needed to hold all those records. The key to successfully transforming your data with high performance is to understand which PDI steps may increase and speed up the flow.

You can develop a PDI transformation that is always waiting for new data. All the steps continue running, awaiting new data. In this transformation, the input steps ingest data records in PDI from the stream. Once ingested, you can process the data to refine it. After processing, you can push it back into the stream or retain it for analysis.


# Data ingestion

Data is ingested into PDI by pulling messages from a stream into a transformation through a specified window. A consumer step in a parent transformation pulls the data into PDI, then runs a child sub-transformation, which executes according to the window parameters. The window creates a continuous stream of records in near real-time.

In the consumer step itself, you can define the number of messages to accept for processing, as well as the specific data formats to stream data. You can set up this step to collect events, monitor alerts, and track user consumption of data streams. Additionally, you can select a step in the child transformation to stream records back to the parent transformation, which passes records downstream to any other steps included within the same parent transformation.

The following consumer steps ingest streaming data into PDI from the specified sources:

* [**AMQP Consumer**](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/amqp-consumer)

  Advanced Message Queuing Protocol brokers
* [**JMS Consumer**](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/jms-consumer)

  Apache ActiveMQ Java Messaging Service server or IBM MQ middleware
* [**Kafka Consumer**](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer)

  Kafka server
* [**Kinesis Consumer**](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/kinesis-consumer)

  Amazon Kinesis Data Streams service
* [**MQTT Consumer**](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/mqtt-consumer)

  Message Queuing Telemetry Transport broker or clients

In PDI, the data stream window is defined by either duration (in milliseconds) or number of rows. The window of data is created when either the duration or number of rows occur. For example, if the duration is set to `1000` milliseconds and the number of rows is 1000, windows of data are created whenever time intervals of 1000 milliseconds are reached or 1000 rows have been received. If you set either duration or number of rows to `0` (zero), PDI will ignore that parameter. For example, if duration is set to `1000` milliseconds and the number of rows is zero, windows are created only every 1000 milliseconds.

You can specify the maximum number of these batches used to collect records at the same time. However, you should only specify a maximum number of these concurrent batches when your consumer step cannot keep pace with the speed at which the data is streaming. Your computing environment must have adequate CPU and memory for this implementation. An error will occur if your environment cannot handle the maximum number of concurrent batches specified.

Depending on your setup, you can run the transformation within PDI or using Spark within the Adaptive Execution Layer (AEL) as the execution engine, which is set in the [Run Options](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation) dialog box. The Spark engine executes the child transformation by duration only, and not by the number of rows.

**Note:** If you use the Spark engine on streaming data, your transformation will use the native Spark Streaming. PDI will not report the execution results. This information will appear in Spark on your cluster.

Before using a consumer step with big data, you must set up Pentaho to connect to a cluster. See [Connecting to a Hadoop cluster with the PDI client](https://docs.pentaho.com/pdia-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article) for instructions.


# Data processing

Once the data stream is ingested through windowing, you can process these windows in your child transformation. Use the child transformation to adjust the data and handle event alerts as needed. After processing, you can either load the windowed data into various outputs or publish it back into the data message stream. You can publish data back into the message stream by using the following producer steps for your specified target:

* [AMQP Producer](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/amqp-producer): Advanced Message Queuing Protocol brokers
* [JMS Producer](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/jms-producer): Apache ActiveMQ Java Messaging Service server or the IBM MQ middleware
* [Kafka Producer](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/kafka-producer): Kafka server
* [Kinesis Producer](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/kinesis-producer): Support for pushing data to a specific region and stream located within the Amazon Kinesis Data Streams service
* [MQTT Producer](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/mqtt-producer): Message Queuing Telemetry Transport broker or clients

You can also use the data streaming window to capture data for analysis. Streaming Pentaho data services can be created from output steps in the child transformation. You can use CTools to create dashboards using these services as data sources. See **Pentaho CTools** for more information.

Once started, streaming data transformations run continuously. You can stop these transformations using the following tools:

* The stop option in the PDI client.
* The [Abort](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/abort) step in either the parent or child transformation.
* Restarting the Pentaho or Spark execution engine.

**CAUTION:**

Stopping or aborting a continuous transformation may cause data loss. Changing the flow of a data stream affects the data that is ingested and processed. Please plan accordingly. If you are working with a Kafka server, you have the option to control when an offset is committed to your window. Use this option to retain the data if the message flow is interrupted.


# Data Integration perspective in the PDI client

The [Pentaho Data Integration](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Pentaho%20Data%20Integration/Pentaho%20Data%20Integration%20cp=GUID-F0F712E0-EF85-4DE2-A8E3-A4948349ACA4=7=en=.md) perspective of the [PDI client (Spoon)](https://docs.pentaho.com/pdia-data-integration/get-started-with-the-pdi-client) enables you to create two basic file types:

* Transformations are used to perform ETL tasks.
* Jobs are used to orchestrate ETL activities, such as defining the flow and dependencies for what order transformations should be run, or preparing for execution by checking conditions.

The following sections describe how to use these transformations and jobs within the Data Integration perspective of Spoon.

* [Basic concepts of PDI](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/basic-concepts-of-pdi)
* [Work with transformations](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp)
* [Work with jobs](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs)
* [Add notes to transformations and jobs](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/add-notes-to-transformations-and-jobs)
* [Connecting to Virtual File Systems](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser)
* [Logging and performance monitoring](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring)
* [Advanced topics](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective)


# Basic concepts of PDI

PDI uses a workflow metaphor as building blocks for transforming your data and other tasks. Workflows are built using steps or entries as you create transformations and jobs. Each step or entry is joined by a hop which passes the flow of data from one item to the next.

To learn about these basical building blocks, review the following sections:

* [Transformations](#transformations)
* [Jobs](#jobs)
* [Hops](#hops)
* [PDI client options](#pdi-client-options)

## Transformations

A transformation is a network of logical tasks called steps. Transformations are essentially data flows. In the example below, the database developer has created a transformation that reads a flat file, filters it, sorts it, and loads it to a relational database table. Suppose the database developer detects an error condition and instead of sending the data to a Dummy step (which does nothing), the data is logged back to a table. The transformation is, in essence, a directed graph of a logical set of data transformation configurations. Transformation file names have a `.ktr` extension.

![Transformation Steps and Hops Example](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-30781fcd166e7e529353735b807b3f657cf029c0%2Fstepandhop.png?alt=media)

The two main components associated with transformations are steps and hops:

* Steps are the building blocks of a transformation, for example a text file input or a table output. There are many steps available in Pentaho Data Integration and they are grouped according to function; for example, input, output, scripting, and so on. Each step in a transformation is designed to perform a specific task, such as reading data from a flat file, filtering rows, and logging to a database as shown in the example above. You can add a step by dragging it from the [Design tab](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Get%20started%20with%20the%20PDI%20client/Get%20Started%20with%20the%20PDI%20Client/Use%20the%20PDI%20client%20perspectives/Data%20Integration%20perspective=GUID-A0FE3FB3-EB3B-40C6-8CBF-945E4F0BC7FF=4=en=.md) onto the canvas, or by double-clicking the step. Steps can be configured to perform the tasks you require. See [PDI transformation steps](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview) for details about the features and ETL functions of the various transformation steps available in PDI.
* Hops are data pathways that connect steps together and allow schema metadata to pass from one step to another. In the image above, it seems like there is a sequential execution occurring; however, that is not true. Hops determine the flow of data through the steps not necessarily the sequence in which they run. When you run a transformation, each step starts up in its own thread and pushes and passes data.

**Note:** All steps in a transformation are started and run in parallel so the initialization sequence is not predictable. That is why you cannot, for example, set a variable in a first step and attempt to use that variable in a subsequent step.

You can connect steps together, edit steps, and open the step **contextual** menu by clicking to edit a step. For more information about connecting steps with hops, see [Hops](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/broken-reference).

![Step Hover Menu](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-5d5dacb16fd08836b842db9a1df921acd90dce7d%2FContextMenu.png?alt=media)

A step can have many connections. Some steps join other steps together, while some serve as an input or output for another step. The data stream flows through steps to the various steps in a transformation. Hops are represented in Spoon as arrows. Hops allow data to be passed from step to step, and also determine the direction and flow of data through the steps. If a step sends outputs to more than one step, the data can either be copied to each step or distributed among them.

## Jobs

Jobs are workflow-like models for coordinating resources, execution, and dependencies of ETL activities.

Jobs aggregate individual pieces of functionality to implement an entire process. Examples of common tasks performed in a job include getting FTP files, checking conditions such as existence of a necessary target database table, running a transformation that populates that table, and e-mailing an error log if a transformation fails. The final job outcome might be a nightly warehouse update, for example.

![Job entry and hop example](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-08d0b6f633d1eee82ca617be5ccd3c06f02287b7%2FJob_Entry_Hop.png?alt=media)

Job entries are the individual configured pieces as shown in the example above; they are the primary building blocks of a job. In data transformations these individual pieces are called steps. Job entries can provide you with a wide range of functionality ranging from executing transformations to getting files from a Web server. A single job entry can be placed multiple times on the canvas; for example, you can take a single job entry such as a transformation run and place it on the canvas multiple times using different configurations. Job settings are the options that control the behavior of a job and the method of logging a job’s actions. Job file names have a `.kjb` extension. See [PDI job entries](https://docs.pentaho.com/pdia-data-integration/pdi-job-entries-reference-overview) for details about the features and ETL functions of the various job entries available in PDI.

Job hops specify the execution order and the condition on which the next job entry will be executed. You can specify the **Evaluation** mode by right clicking on the job hop. A job hop is just a flow of control. Hops link to job entries and, based on the results of the previous job entry, determine what happens next.

**Note:** Hops behave differently when used in a job than when used in a transformation.

Job hop conditions are specified in the following table:

| Condition                       | Description                                                                                                                                                                                                   |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Unconditional**               | Specifies that the next job entry will be executed regardless of the result of the originating job entry                                                                                                      |
| **Follow when result is true**  | Specifies that the next job entry will be executed only when the result of the originating job entry is true; this means a successful execution such as, file found, table found, without error, and so on    |
| **Follow when result is false** | Specifies that the next job entry will only be executed when the result of the originating job entry was false, meaning unsuccessful execution, file not found, table not found, error(s) occurred, and so on |

## Hops

A hop connects one transformation step or job entry with another. The direction of the data flow is indicated by an arrow. To create the hop, click the source step, then press the SHIFT key and draw a line to the target step. Alternatively, you can draw hops by hovering over a step until the **hover** menu appears. Drag the **hop painter** icon from the source step to your target step.

![Dummy step](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-d983b1955adadda655e8dc6eaf37f9c15cd3e834%2FPDI_Dummy_Step.png?alt=media)

Additional methods for creating hops include:

* Click on the source step, hold down the middle mouse button, and drag the hop to the target step.
* Use CTRL and left-click to select two steps the right-click on the step and choose **New Hop**.

To split a hop, insert a new step into the hop between two steps by dragging the step over a hop. Confirm that you want to split the hop. This feature works with steps that have not yet been connected to another step only.

Loops are not allowed in transformations because Spoon depends heavily on the previous steps to determine the field values that are passed from one step to another. Allowing loops in transformations may result in endless loops and other problems. Loops are allowed in jobs because Spoon executes job entries sequentially; however, make sure you do not create endless loops.

Mixing rows that have a different layout is not allowed in a transformation; for example, if you have two table input steps that use a varying number of fields. Mixing row layouts causes steps to fail because fields cannot be found where expected or the data type changes unexpectedly. The trap detector displays warnings at design time if a step is receiving mixed layouts.

You can specify if data can either be **copied**, **distributed**, or **load balanced** between multiple hops leaving a step. Select the step, right-click and choose **Data Movement**.

![Step Copy and Distribute Examples](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-8970faadb0687282eee2ba9cb875ae1f7345210d%2Fdistributedandcopied.png?alt=media)

A hop can be enabled or disabled (for testing purposes for example). Right-click on the hop to display the **Options** menu.

## PDI client options

The PDI client allows you to customize certain aspects of its behavior. To access the options, choose **Tools** > **Options**. The following table describes the **General** tab options for working with transformations and jobs:

| Option                                         | Description                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Preview data batch size**                    | Sets batch size of the preview data buffer. When you preview data, this option sets the buffer size used for these values.                                                                                                                                                                                                                                           |
| **Max number of lines in the logging windows** | Specifies the maximum limit of rows to display in the logging window.                                                                                                                                                                                                                                                                                                |
| **Central log line store timeout in minutes**  | Indicates the number of minutes before the central log line store times out.                                                                                                                                                                                                                                                                                         |
| **Max number of lines in the log history**     | Specifies the maximum limit of line to display in the log history views.                                                                                                                                                                                                                                                                                             |
| **Show welcome page at startup**               | Controls whether or not to display the Welcome page when launching the PDI client.                                                                                                                                                                                                                                                                                   |
| **Use database cache**                         | The PDI client caches information that is stored on the source and target databases. In some instances, caching causes incorrect results when you are making database changes. To prevent errors you can disable the cache altogether instead of clearing the cache every time.                                                                                      |
| **Open last file at startup**                  | Loads the last transformation you used (opened or saved) from XML or repository automatically.                                                                                                                                                                                                                                                                       |
| **Autosave changed files**                     | Automatically saves a changed transformation before running.                                                                                                                                                                                                                                                                                                         |
| **Only show the active file in the main tree** | Reduces the number of transformation and job items in the main tree on the left by only showing the currently active file.                                                                                                                                                                                                                                           |
| **Only save used connections to XML**          | Limits the XML export of a transformation to the used connections in that transformation. This is helpful while exchanging sample transformations to avoid having all defined connections to be included.                                                                                                                                                            |
| **Replace existing objects on open/import**    | Replaces objects, such as existing database connections, during import. If the **Ask before replacing objects** is also checked, you will be prompted before the import occurs. Requests permission before replacing objects, such as existing database connections during import.                                                                                   |
| **Ask before replacing objects**               | Requests permission before replacing objects, such as existing database connections during import.                                                                                                                                                                                                                                                                   |
| **Show Save dialog**                           | Allows you to turn off the confirmation dialogs you receive when a transformation has been changed.                                                                                                                                                                                                                                                                  |
| **Automatically split hops**                   | Disables the confirmation messages that launch when you want to split a hop.                                                                                                                                                                                                                                                                                         |
| **Show Copy or Distribute dialog**             | <p>Disables the warning message that appears when you link a step to multiple outputs. This warning message describes the two options for handling multiple outputs:- <strong>Distribute rows</strong></p><p>Destination steps receive the rows in turns (round robin).</p><ul><li><strong>Copy rows</strong></li></ul><p>All rows are sent to all destinations.</p> |
| **Show repository dialog at startup**          | Controls whether or not the Repository dialog box appears at startup.                                                                                                                                                                                                                                                                                                |
| **Ask user when exiting**                      | Controls whether or not to display a confirmation dialog when a user chooses to exit the application.                                                                                                                                                                                                                                                                |
| **Clear custom parameters (steps/plugins)**    | Clears all parameters and flags that were set in the plug-in or step dialog boxes.                                                                                                                                                                                                                                                                                   |
| **Auto collapse palette tree**                 | Indicates whether the palette tree should be collapsed automatically.                                                                                                                                                                                                                                                                                                |
| **Display tooltips**                           | Controls whether or not to display tool tips for the buttons on the main tool bar.                                                                                                                                                                                                                                                                                   |
| **Show help tooltips**                         | Displays help tool tips. A tool tip is a short description that appears when you hover the mouse pointer over an object in the PDI client.                                                                                                                                                                                                                           |


# Work with transformations

In the [PDI client (Spoon)](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/basic-concepts-of-pdi), you can develop transformations, which are data workflows representing your ETL activities. The steps used in your transformations define the individual ETL activities. The transformations containing your steps are stored in KTR files. You can access these KTR files through the PDI client.

* [Create a transformation](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/create-a-transformation)
* [Open a transformation](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/open-a-transformation)
* [Rename a folder](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/rename-a-folder-for-transformations-and-jobs)
* [Save a transformation](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/save-a-transformation)
* [Run your transformation](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation)
* [Stop your transformation](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/stop-your-transformation)
* [Configure transformation properties](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/configure-transformation-properties)
* [Use the Transformation menu](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/use-the-transformation-menu)


# Create a transformation

Follow these instructions to create your transformation:

1. Perform one of the following actions:
   * Click **File** > **New** > **Transformation**.
   * Click the **New file** icon in the toolbar and select **Transformation**.
   * Hold down the CTRL N keys.
2. Go to the **Design** tab. Expand the folders or use the **Steps** field to search for a specific step.
3. Either drag or double-click a step to place it on the PDI client canvas.
4. Double-click the step in the PDI client canvas to open its properties window. For help with filling out the window, click the **Help** button that is available with each step.
5. To add another step, either drag or double-click the step in the **Design** tab to place it on the PDI client canvas.
   * If you drag the step to the canvas, you can add a hop by pressing the SHIFT key and drawing a hop from one step to the other.
   * If you double-click it, the step appears on the canvas with a hop already connected to your previous step.

After you have created a transformation, you must save the transformation before you can run it.


# Open a transformation

The method you use to open an existing transformation depends on if you are using PDI locally on your machine or if you are connected to a repository. If you are connected to a repository, then you are remotely accessing your file on the Pentaho Server. Optionally, you can open a transformation on a Virtual File System (VFS).

**Note:** If you get a message indicating that a plugin is missing, see the [Troubleshooting transformation steps and job entries](https://docs.pentaho.com/pdia-data-integration/data-integration-issues/troubleshooting-transformation-steps-and-job-entries) section for more details.

If you recently had a file open, you can also use **File** > **Open Recent**.

## On your local machine

Follow these instructions to open a transformation on your local machine.

1. In the PDI client, perform one of the following actions:
   * Select **File** > **Open**.
   * Click the **Open file** icon in the toolbar.
   * Click the **OPEN Files** tile from the **Welcome** screen.
   * Hold down the CTRLO keys.
2. Select the file from the Open window, then click **Open**.

   **Note:** By default, the folder from where the last file was accessed is opened.

The Open window closes when your transformation appears in the canvas.

## In the Pentaho Repository

Follow these instructions to access a transformation in the Pentaho Repository.

1. Verify that you are [connected to a repository](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi), which establishes remote access to the Pentaho Server.
2. In the PDI client, perform one of the following actions to access the Open repository browser window:
   * Select **File** > **Open**.
   * Click the **Open file** icon in the toolbar.
   * Click the **OPEN Files** tile from the **Welcome** screen.
   * Hold down the CTRLO keys.**Note:** By default, the folder from where the last file was accessed is opened.
3. To use a recently opened file, use the **Recents** option to navigate to your transformation.
4. Use either the search box to find your transformation, or use the left panel to navigate to a repository folder containing your transformation.

   **Note:** If the PDI is already connected to the Pentaho Repository, then only the Recents and Pentaho Repository options appear in the left pane. If the PDI is not connected to a Pentaho Repository, then the following options appear in the left pane:

   * Recents
   * Local
   * VFS Connections
   * Hadoop Clusters
5. If you are not connected to Pentaho Repository, then perform one of the following actions to access the transformation:
   * Double-click on your transformation.
   * Select it and press the Enter key.
   * Select it and click **Open**.
6. If you are connected to the Pentaho Repository, click **Open** to access the transformation.

The Open window closes when your transformation appears in the canvas.

## On Virtual File Systems

From the menu bar in the PDI client, select **File** > **Open** to open a PDI transformation on a Virtual File System (VFS). See [Connecting to Virtual File Systems](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser) for details.


# Rename a folder

You can rename a folder from the **Open**. You can rename a folder or file only if you are not connected to the Pentaho Repository.

1. Select a folder or file in the **Open** window.
2. Right-click on it.
3. Select the **Rename** option from the context menu to rename it.


# Save a transformation

The method you use to save a transformation depends on if you are using PDI locally on your machine or if you are connected to a repository. If you are connected to a repository, you are remotely saving your file on the Pentaho Server. Optionally, you can save a transformation on a Virtual File System (VFS) if you are not connected to the Pentaho Repository.

## On your local machine

Follow these instructions to save a transformation on your local machine.

1. In the PDI client, perform one of the following actions:
   * Select **File** > **Save** or **File** > **Save as**.
   * Click the **Save current file** icon in the toolbar.
   * Hold down the CTRL S keys.\
     The Save As window opens.
2. Specify the transformation's name in the window and select the location.

   By default, the folder from where the last file was accessed is opened.

   **Note:** The file types allowed are .ktr or.kjb.
3. Click **Save**.

   The transformation is saved.

The window closes when your transformation is saved.

## In the Pentaho Repository

Follow these instructions to save a transformation to the Pentaho Repository.

1. Verify that you are [connected to a repository](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi), which establishes remote access to the Pentaho Server.
2. In the PDI client, perform one of the following actions:

   * Select **File** > **Save** or **File** > **Save as**.
   * Click the **Save current file** icon in the toolbar.
   * Hold down the CTRLS keys.\
     The Save As window opens. By default, the folder from where the last file was accessed is opened.

   **Note:** The file types allowed are .ktr or.kjb.
3. Navigate to the repository folder where you want to save your transformation.
4. Specify the transformation's name in the **File name** field.
5. Click **Save**.

The window closes when your transformation is saved. If the transformation already exists, an overwrite warning message appears. Click **OK** to overwrite the existing transformation.

## On Virtual File Systems

From the menu bar in the PDI client, select **File** > **Open** to save a PDI transformation on a Virtual File System (VFS). See [Connecting to Virtual File Systems](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser) for details.


# Run your transformation

After creating a transformation as a network of steps (a data workflow) that performs your ETL tasks, you should run it in the PDI client to test how it performs in various scenarios. With the Run Options window, you can apply and adjust different run configurations, options, parameters, and variables.

When you are ready to run your transformation, you can perform any of the following actions to access the Run Options window:

* Click the **Run** icon on the toolbar.
* Select **Run** from the **Action** menu.
* Press F9.

The Run Options window appears.

![Run Options Window](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-14b808664c8a48a54b73edb431a93ed452e3e8de%2FssPDIRunOptions.png?alt=media)

In the Run Options window, you can specify a **Run configuration**. To set up run configurations, see [Run configurations](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/run-your-job/run-configurations-work-with-jobs).

**Note:** The default Pentaho local configuration runs the transformation using the Pentaho engine on your local machine. You cannot edit this default configuration.

The Run Options window also lets you specify logging and other options, or experiment by passing temporary values for defined parameters and variables during each iterative run.

**Always show dialog on run** is set by default. You can deselect this option if you want to use the same run options every time you execute your transformation. After you have selected to not **Always show dialog on run**, you can access it again through the dropdown menu next to the **Run** icon in the toolbar, through the **Action** main menu, or by pressing F8.

After running your transformation, you can use the [Execution panel](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation/analyze-your-transformation-results) to analyze the results.


# Run configurations

Some ETL activities are lightweight, such as loading in a small text file to write out to a database or filtering a few rows to trim down your results. For these activities, you can run your transformation locally using the default Pentaho engine. Some ETL activities are more demanding, containing many steps calling other steps or a network of transformation modules. For these activities, you can set up a separate Pentaho Server dedicated for running transformations using the Pentaho engine. Other ETL activities involve large amounts of data on network clusters requiring greater scalability and reduced execution times. For these activities, you can run your transformation using the **Spark Submit** job entry.

You can create or edit run configurations through the **Run configurations** folder in the **View** tab as shown below:

![Run Configurations Folder](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-8a2167ce5dee539dc1aeef3cab3202a8c028ffa6%2FPDI_Transformation%20View%20Tab%20in%20Run-Options_Panel.png?alt=media)

To create a new run configuration, right-click on the **Run configurations** folder and select **New**. To edit or delete a run configuration, right-click on an existing configuration.

**Note:** **Pentaho local** is the default run configuration. It runs transformations with the Pentaho engine on your local machine. You cannot edit this default configuration.

Selecting **New** or **Edit** opens the Run configuration dialog box that contains the following fields:

| Field           | Description                                        |
| --------------- | -------------------------------------------------- |
| **Name**        | Specify the name of the run configuration.         |
| **Description** | Optionally, specify details of your configuration. |


# Select an Engine

You can select the **Pentaho Engine** to run transformations in the default Pentaho (Kettle) environment.

You can also use the **Spark Submit** job entry to run big data transformations on your Hadoop cluster to coordinate large amounts of data over multiple nodes. See [Spark Submit](https://docs.pentaho.com/pdia-data-integration/pdi-job-entries-reference-overview/spark-submit) for details.

## Pentaho Engine

The Pentaho engine does not execute sub-transformations or sub-jobs when you select the **Pentaho server** or **Slave server** option. If you want to run a sub-transformation on the same server where your parent job runs, select **Local** for the **Run Configuration** type.

![Run Configuration Dialog Box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-a8331438d2d8d77571fd63ddffbbd9ec7b2b59ab%2FPDI_Transformation%20Run-Configuration%20for%20Pentaho%20Engine_Dialog.png?alt=media)

The **Settings** section of the Run configuration dialog box contains the following options when **Pentaho** is selected as the **Engine** for running a transformation:

| Option                           | Description                                                                                                                                                                                                                                                                                                                      |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Local**                        | Select this option to use the Pentaho engine to run a transformation on your local machine.                                                                                                                                                                                                                                      |
| **Pentaho server**               | Select this option to run your transformation on the Pentaho Server. This option only appears if you are connected to a [Pentaho Repository](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi).                                                                                                    |
| **Slave server**                 | Select this option to send your transformation to a slave (remote) server or Carte cluster.                                                                                                                                                                                                                                      |
| **Location**                     | <p>If you select <strong>Slave server</strong>, specify its location.</p><p>If you have set up a Carte cluster, you can specify <strong>Clustered</strong>. See <a href="../../../../advanced-topics-pentaho-data-integration-overview/use-carte-clusters">Use Carte Clusters</a> for more details.</p>                          |
| **Send resources to the server** | If you specified a remote server for your remote **Location**, select to send your transformation to the specified server before running it. Select this option to run the transformation locally on the server. Any related resources, such as other referenced files, are also included in the information sent to the server. |
| **Log remote execution locally** | If you specified **Clustered** for your remote **Location**, select to show the logs from the cluster nodes.                                                                                                                                                                                                                     |
| **Show transformations**         | If you specified **Clustered** for your remote **Location**, select to show the other transformations that are generated when you run on a cluster.                                                                                                                                                                              |


# Options

Errors, warnings, and other information generated as the transformation runs are stored in logs. You can specify how much information is in a log and whether the log is cleared each time through the **Options** section of this window. You can also enable safe mode and specify whether PDI should gather performance metrics. For more informaiton about the logging methods available in PDI, see [Logging and Performance Monitoring](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring).

| Option                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Clear log before running**   | Indicates whether to clear all your logs before you run your transformation. If your log is large, you might need to clear it before the next execution to conserve space.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Log level**                  | <p>Specifies how much logging is performed and the amount of information captured:- <strong>Nothing</strong>: No logging occurs.</p><ul><li><strong>Error</strong>: Only errors are logged.</li><li><strong>Minimal</strong>: Only use minimal logging.</li><li><strong>Basic</strong>: This is the default level.</li><li><strong>Detailed</strong>: Give detailed logging output.</li><li><strong>Debug</strong>: For debugging purposes, very detailed output.</li><li><strong>Row Level</strong>: Logging at a row level, which generates a lot of log data.</li></ul><p><strong>Debug</strong> and <strong>Row Level</strong> logging levels contain information you may consider too sensitive to be shown. Consider the sensitivity of your data when selecting these logging levels. See the <strong>Administer Pentaho Data Integration and Analytics</strong> document for instructions on how best to use these logging methods.</p> |
| **Enable safe mode**           | Checks every row passed through your transformation and ensure all layouts are identical. If a row does not have the same layout as the first row, an error is generated and reported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Gather performance metrics** | Monitors the performance of your transformation execution through these metrics. [Use performance graphs](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/monitor-performance/use-performance-graphs) shows how to visually analyze these metrics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |


# Parameters and Variables

You can temporarily modify parameters and variables for each execution of your transformation to experimentally determine their best values. The values you enter into these tables are only used when you run the transformation from the Run Options window. The values you originally defined for these parameters and variables are not permanently changed by the values you specify in these tables.

| Value Type                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Parameters](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers)          | Set parameter values pertaining to your transformation during runtime. A parameter is a local variable. The parameters you define while creating your transformation are shown in the table under the **Parameters** tab.- [Arguments](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/arguments): Set argument values passed to your transformation through the Arguments dialog box. |
| [Variables](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables) | Set values for user-defined and environment variables pertaining to your transformation during runtime.                                                                                                                                                                                                                                                                                                                                                                                |


# Analyze your transformation results

You can see how your transformation performed, if errors occurred, and explore the data by viewing the execution results.

After you [Run your transformation](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation), the **Execution Results** panel appears. It contains several different tabs that help you to see how the transformation ran, pinpoint errors, and monitor performance.

## Step metrics

The **Step Metrics** tab shows statistics for each step in your transformation including how many records were read, written, caused an error, processing speed (rows per second) and more. This tab also indicates whether an error occurred in your transformation step. If a mistake had occurred, steps that caused the transformation to fail will be highlighted in red. In the example below, the Lookup Missing Zips step caused an error.

![Step Metrics](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-bb3c944d0428ae51d067cd69ce5c661d8d641322%2FssPDIExecutingTransformation.png?alt=media)

## Logging

The **Logging** tab displays the logging details for the most recent execution of the transformation. You can also drill in deeper to determine where errors occur. Error lines are highlighted in red. In the example below, the Lookup Missing Zips step caused an error because it attempted to lookup values on a field called **POSTALCODE2**, which did not exist in the lookup stream.

![Logging Details](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-97a0ba0a3953598b2e5b734a845aeeb5a791cf16%2FssPDIExecuteTransformationLogging.png?alt=media)

## Execution history

The **Execution History** tab enables access to the Step Metrics and Logging information from previous executions of your transformation. This history only works if you have configured your transformation to log to a database through the **Logging** tab of the Transformation Settings dialog box. For more information on configuring logging, see [Logging and performance monitoring](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring).

## Performance graph

The **Performance Graph** enables you to analyze the performance of steps based on a variety of metrics including how many records were read, written, caused an error, processing speed (rows per second) and more. Like the **Execution History**, this graph requires you to configure your transformation to log to a database through the **Logging** tab of the Transformation Settings dialog box.

## Metrics

The **Metrics** tab shows a Gantt chart after your transformation executes. It contains information such as how long it takes to connect to a database, how much time is spent executing a SQL query, or how long it takes to load a transformation.

![Transformation Metrics](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-66290290e74564ce6613c65f0cf78eb8d884ab19%2FssPDIExecuteTransformationMetrics.png?alt=media)

## Preview data

Use the **Preview Data** tab to display a preview of the data per each step of your PDI transformation.

Click on a step to show the data values for that step, as shown in the following example:

![Preview Data](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-88c92683462fed541ce49b1002047b17403bcf15%2FssPDI_ExecutionPanel_InspectingData.png?alt=media)


# Stop your transformation

There are two different methods you can use to stop transformations running in the PDI client. The method you use depends on the processing requirements of your ETL task. Most transformations can be stopped immediately without concern. However, since some transformations are ingesting records using messaging or streaming data, such incoming data may need to be stopped safely so that the potential for data loss is avoided.

To stop a transformation running in the [Data Integration perspective](https://docs.pentaho.com/pdia-data-integration/get-started-with-the-pdi-client-1/use-the-pdi-client-perspectives#data-integration-perspective) of the PDI client:

* Use **Stop** if your ETL task should stop processing all data immediately.
* Use **Stop input processing** if your ETL task needs to finish any records already initiated or retrieved before stopping.


# Configure transformation properties

Transformation properties are a collection of properties that describe the transformation and configure its behavior. You can use transformation properties to customize the processing of your data to achieve the desired output.

To view the transformation properties, click CTRLT or right-click on the canvas and select **Properties** from the menu that appears.. The following sections provide a detailed description of the available settings:

* [Transformation tab](#transformation-tab)
* [Parameters tab](#parameters-tab)
* [Logging tab](#logging-tab)
* [Dates tab](#dates-tab)
* [Dependencies tab](#dependencies-tab)
* [Miscellaneous tab](#miscellaneous-tab)
* [Monitoring tab](#monitoring-tab)

After you have adjusted your settings, click SQL to generate the SQL code necessary for creating the logging table. The Data Definition Language (DDL) displays in the Simple SQL Editor allowing you to execute this or any other SQL statements against the logging connection. For information on how to use the SQL Editor, see [Use the SQL Editor](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/use-the-sql-editor).

## Transformation tab

Use the **Transformation** tab to specify general properties about the transformation.

![Transformation properties - Transformation tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-86a4a8563f52c325ae236ec945d185ece7f44acc%2FPDI_TransProperties_Transformation_Tab.png?alt=media)

This tab includes the following options:

| Property                | Description                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------------------- |
| Transformation name     | The name of the transformation. This field is required to save the settings to a repository. |
| Transformation filename | The file name (\*.ktr) of the transformation.                                                |
| Description             | Short description of the transformation which displays in the repository explorer.           |
| Extended description    | Long extended description of the transformation.                                             |
| Status                  | Draft or production status                                                                   |
| Version                 | Version description                                                                          |
| Directory               | The directory in the repository where the transformation is stored.                          |
| Created by              | Name of the original creator of the transformation.                                          |
| Created at              | Date and time when the transformation was created.                                           |
| Last modified by        | The username of the last user that modified the transformation.                              |
| Last modified at        | Date and time when the transformation was last modified.                                     |

## Parameters tab

Use the **Parameters** tab to add parameters to customize your transformation.

![Transformation properties - Parameters tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-f224d576d3c7cb7de698e26f0570292511675fef%2FPDI_TransProperties_Parameters_Tab.png?alt=media)

This tab includes the following options:

| Property      | Description                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------- |
| Parameter     | Acts as a local variable that can be shared across all steps in an individual transformation. |
| Default Value | Value that is used if the parameter is not set somewhere else in the transformation.          |
| Description   | Description of the user-defined parameter.                                                    |

## Logging tab

Use the **Logging** tab to configure how and where logging information is captured. For more information about how to configure transformation logging, see [Set up transformation logging](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/set-up-transformation-logging).

![Transformation properties - Logging tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-9758780f23f1ae52bb686b337aeef504b3164c78%2FPDI_TransProperties_Logging_Tab.png?alt=media)

In the left navigation pane, select which type of logging you want to use. This tab includes the following options:

| Property                     | Description                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Log Connection               | Specify the database connection you are using for logging. You can configure a new connection by clicking **New**.                                                                                                                                                                                                                                                                                                   |
| Log table schema             | Specify the schema name, if supported by your database.                                                                                                                                                                                                                                                                                                                                                              |
| Log table name               | Specifies the name of the log table. **Note:** If you are also using job logging, use a different table name for Transformation logging.                                                                                                                                                                                                                                                                             |
| Logging interval (seconds)   | Specify the interval in which logs are written to the table. This property only applies to Transformation and Performance logging types.                                                                                                                                                                                                                                                                             |
| Log record timeout (in days) | <p>Specify the number of days to keep log entries in the table before they are deleted.</p><p>This property only applies to Transformation and Performance logging types.</p><p>If you find that data in the log table is not deleted as expected, see <a href="../../data-integration-issues/log-table-data-is-not-deleted">Log table data is not deleted</a> in Troubleshooting for best practice information.</p> |
| Log size limit (in lines)    | <p>Enter the limit for the number of lines that are stored in the LOG\_FIELD. PDI stores logging for the transformation in a long text field (CLOB).</p><p>This property only applies to the Transformation logging type.</p>                                                                                                                                                                                        |
| Fields to log                | Select the fields you want to log in the **Fields to log** pane.                                                                                                                                                                                                                                                                                                                                                     |

## Dates tab

Use the **Dates** tab to configure date ranges and limits for this connection.

![Transformation properties - Dates tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-c6c4da9717dd4a46d018802738e8d0d1ba6d6664%2FPDI_TransProperties_Dates_Tab.png?alt=media)

This tab includes the following options:

| Property                          | Description                                                                                                                                                                                                                                                                  |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maxdate connection                | Get the upper limit for a date range on this connection.                                                                                                                                                                                                                     |
| Maxdate table                     | Get the upper limit for a date range in this table.                                                                                                                                                                                                                          |
| Maxdate field                     | Get the upper limit for a date range in this field.                                                                                                                                                                                                                          |
| Maxdate offset (seconds)          | Increases the upper date limit with this amount. Use this for example, if you find that the field DATE\_LAST\_UPD has a maximum value of 2004-05-29 23:00:00, but you know that the values for the last minute are not complete. In this case, simply set the offset to -60. |
| Maximum date difference (seconds) | Sets the maximum date difference in the obtained date range. This will allow you to limit job sizes.                                                                                                                                                                         |

## Dependencies tab

Use the **Dependencies** tab to specify all of the dependencies for the transformation.

![Transformation properties - Dependencies tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-282d42f007d185b78563a6c45aadfb98b9be33a2%2FPDI_TransProperties_Dependencies_Tab.png?alt=media)

The **Dependencies** tab allows you to enter all of the dependencies for the transformation. For example, if a dimension depends on three lookup tables, make sure that the lookup tables have not changed. If the values in these lookup tables have changed, extend the date range to force a full refresh of the dimension.

Dependencies allow you to determine if a table has changed when you have a "data last changed" column in the table. Click **Get dependencies** to detect dependencies automatically.

| Property   | Description                                                                                       |
| ---------- | ------------------------------------------------------------------------------------------------- |
| Connection | A dropdown to select a database connection that has already been created for that transformation. |
| Table      | A specific table from the selected database connection.                                           |
| Field      | A specific field within the selected table.                                                       |

## Miscellaneous tab

Use the **Miscellaneous** tab to configure buffer and feedback size and performing various administrative tasks.

![Transformation properties - Miscellaneous tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-9cfadd695082206af01019a8fa243fed422d61ae%2FPDI_TransProperties_Miscellaneous_Tab.png?alt=media)

This tab includes the following options:

| Property                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Number of rows in rowset                       | Allows you to change the size of the buffers between the connected steps in a transformation. Do not change this parameter unless you are running low on memory, for example.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Show a feedback row in transformation steps?   | Controls whether or not to add a feedback entry into the log file while the transformation is being executed. By default, this feature is enabled and configured to display a feedback record every 5000 rows.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| The feedback size                              | Sets the number of rows to process before entering a feedback entry into the log. Set this higher when processing large amounts of data to reduce the amount of information in the log file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Make the transformation database transactional | <p>This allows you to open one unique connection per defined and used database connection in the transformation. Enabling this option is required to allow a failed transformation to be completely rolled back.</p><p>Enabling this option is also necessary when trying to alter connection settings before a query using an "Execute SQL script" step. (See also the <strong>Advanced</strong> section in the Database Connection dialog box "Enter the SQL statements (separated ...) to execute right after connecting")</p><p>Further information can be found in <a href="https://pentaho-public.atlassian.net/wiki/spaces/EAI/pages/386803253/Database+transactions+in+jobs+and+transformations">Database transactions in jobs and transformations</a>.</p><p><strong>Note:</strong> A transformation wide commit for all steps is done when the last step finishes. When the transformation fails, a rollback is done. It is not necessary to set any commit sizes since they are ignored.</p> |
| Shared objects file                            | Specifies the location of the XML file used to store shared objects like database connections, clustering schemas, and more.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Manage thread priorities?                      | Allows you to enable or disable the internal logic for changing the Java thread priorities based on the number of input and output rows in the "rowset" buffers. This can be useful in some situations where the cost of using the logic exceeds the benefit of the thread prioritization.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## Monitoring tab

Use the **Monitoring** tab for enabling and disabling step performance monitoring and setting related performance parameters.

![Transformation properties - Monitoring tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-48dd3607a1f75b6d004f274eeed6966fa4dbaeb8%2FPDI_TransProperties_Monitoring_Tab.png?alt=media)

This tab includes the following options:

| Property                                   | Description                                                                                                                                                                                                                                                                                |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Enable step performance monitoring?        | This activates performance monitoring for transformation steps. It shows how many rows of data are being written, read, inputted, or outputted for each step. These metrics can be viewed on the **Performance Graph** tab that’s part of the**Execution Results** panel below the canvas. |
| Step performance measurement interval (ms) | This is the interval in milliseconds used to take a snapshot. Example: 10 ms                                                                                                                                                                                                               |
| Maximum number of snapshots in memory      | Sets the maximum number of measurement snapshots that can be held in memory during runtime.                                                                                                                                                                                                |


# Use the Transformation menu

Use the **Transformation** menu to access transformation settings, options, and properties.

Right-click any step in the PDI client canvas to view the **Transformation** menu. Each menu item is described in the following table:

| Menu Item                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **New Hop**                          | Creates a new hop.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Edit**                             | Shows the configuration window for the step.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Description**                      | Adds a description to the step.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Open Referenced Object**           | Maps a sub-transformation. Mapping a sub-transformation is covered in detail in [Mapping](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/mapping).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Data Movement**                    | <p>Describes the way data moves through the transformation when there is more than one hop. The following options are available:- <strong>Round Robin</strong>: Partitions the output stream and sends a portion of all output records down each hop.</p><ul><li><strong>Load Balance</strong>: Checks the output row sets to see how much room is left in the buffer. It selects the one that is most empty. If the rows are distributed to steps that take very little processing time per row (or the exact same amount of time for each step to process a row), <strong>Load Balance</strong> is identical to <strong>Round Robin</strong>. If the rows are sent down one path that takes a long time to process, such as Sort or Group By and down another path that processes rows more quickly, the "quick path" will likely have more rows sent to it, as it will empty its buffer before the "slow path" has a chance to empty its buffer. This is typically used for clustered transformations, where the same processing occurs on different nodes. The row buffer is set, by default, to 10000. To change the row buffer size, open the Transformation Settings window, then select <strong>Nr of rows in rowset</strong> on the <strong>Miscellaneous</strong> tab.</li><li><strong>Copy Data to Next Steps</strong>: Copies the data to subsequent steps.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Change Number of Copies to Start** | Starts several instances of a step in parallel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Copy**                             | Copies selected items to the clipboard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Duplicate**                        | Makes a copy of the selected items, then pastes them to the canvas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Delete**                           | Deletes selected items from the canvas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Hide**                             | <p>Hides the step from the PDI client canvas.</p><p><strong>CAUTION:</strong></p><p>If you hide the step, you will need to open the transformation or job XML file and hand edit it to view it again. For more details, see the <a href="../../data-integration-issues/troubleshooting-transformation-steps-and-job-entries/step-is-already-on-canvas-error">troubleshooting</a> section.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Detach**                           | Detaches the step or entry from the transformation or job.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Input Fields**                     | Shows metadata, like the field name and type, for fields that come into the step.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Output Fields**                    | Shows metadata, like the field name and type, for fields that go out of the step.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Sniff Test During Execution**      | <p>The sniff test displays data as it travels from one step to another in the stream. To use this, right-click a step in the transformation as it runs and select <strong>Sniff Test During Execution</strong>. The following options are available:- <strong>Sniff test input rows</strong>: Shows the data inputted into the step.</p><ul><li><strong>Sniff test output rows</strong>: Shows the data outputted from the step.</li><li><strong>Sniff test error handling</strong>: Shows error handling data.</li></ul><p>For more information on how to use this tool, see the <a href="../logging-and-performance-monitoring/monitor-performance/sniff-test-tool">Sniff Test tool</a> article.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Check Selected Step(s)**           | Checks transformation steps for problems that could interfere with successfully running the transformation. Right-click the transformation step that you want to check and click **Check Selected Step(s)**. Warnings and errors appear in the Results of transformation checks window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Error Handling**                   | Indicates how to apply error handling for a step. When this is selected, the Step error handling settings window appears.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Preview**                          | Previews the results of the transformation. Launches the Transformation Debug Dialog.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Align/Distribute**                 | <p>Arranges steps on the canvas so that they are aligned properly or distributed evenly. This helps create a visually pleasing transformation that is easier to read and digest.Align refers to where the steps are permitted along the x (horizontal) or y (vertical) axis. Distribute makes the horizontal and vertical spacing between steps consistent. Typically, you turn on the grid, then move the different steps or entries on the canvas so that they form some sort of pattern, like a straight or branching line.</p><p>You select steps and apply the following options, as needed:</p><ul><li><strong>Align Left</strong>: Positions all steps so their left sides start on the same "x" (horizontal) coordinate as the left-most step. After applied, steps are arranged in a straight vertical line. No changes are made to the spaces between steps.</li><li><strong>Align Right</strong>: Positions all steps so their right sides start on the same "x" (horizontal) coordinate as the right-most step. After applied, steps are arranged in a straight vertical line. No changes are made to the spaces between steps.</li><li><strong>Align Top</strong>: Positions all steps so their top sides start on the same "y" (vertical) coordinate as the step positioned closest to the top of the canvas. After applied, steps are arranged in a straight horizontal line. No changes are made to the spaces between steps.</li><li><strong>Align Bottom</strong>: Positions all steps so their bottom sides start on the same "y" (vertical) coordinate as the step positioned closest to the bottom of the canvas. After applied, steps are arranged in a straight horizontal line. No changes are made to the spaces between steps.</li><li><strong>Distribute Horizontally</strong>: Positions all steps so that they are evenly spaced horizontally. After applied, steps are arranged evenly. No changes are made to the alignment.</li><li><strong>Distribute Vertically</strong>: Positions all steps so that they are evenly spaced vertically. After applied, steps are arranged evenly. No changes are made to the alignment.</li><li><strong>Snap to Grid</strong>: Aligns steps on the canvas to the grid. If grid markers do not appear on the canvas, select <strong>Tools</strong> > <strong>Options</strong> > <strong>Look & Feel</strong> > <strong>Show Canvas Grid</strong>. See <a href="broken-reference">PDI client options</a> for more information on how to customize the PDI client.</li></ul> |
| **Data Services**                    | Create, edit, delete, or test a Pentaho Data Service. The Pentaho Data Service allows others to obtain the results of a transformation, even if the person does not have the PDI client or Pentaho Server installed. The Pentaho Data Service is discussed in great detail in [Pentaho Data Services](https://docs.pentaho.com/pdia-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Mapping**                          | <p>Provides a way for you to map target fields from the step to source columns in a database. When selected, the Mappingwindow appears containing the following fields:- <strong>Source Fields</strong>: Lists the field names from the incoming stream.</p><ul><li><strong>Target Fields</strong>: Lists the column names in a target table.</li><li><strong>Auto Target Selection</strong>: Automatically selects a matching table column if the target field is selected.</li><li><strong>Auto Source Select</strong>: Automatically selects a matching target field if the table column is selected.</li><li><strong>Add</strong>: Allows you to move the mapped target and source information to the mappings grid.</li><li><strong>Guess</strong>: Makes mappings based on a computer algorithm.</li><li><strong>Hide assigned source fields</strong> and <strong>Hide assigned target fields</strong>: Removes mappings from the <strong>Source Fields</strong> and <strong>Target Fields</strong> lists those fields are added to the mapping grid.</li><li><strong>Delete</strong>: Removes mappings from the mapping grid so that they reappear in the <strong>Target Fields</strong> and <strong>Source Fields</strong> lists again.</li></ul><p>When you click <strong>OK</strong>, the Mapping window closes and a Select / Rename Values step appears on the canvas. It is usually named after the step that right-clicked. The Select / Rename Values window contains the mappings. If you are not able to make mappings, the step still appears, but the properties are blank.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Partitions**                       | Splits data into subsets according to a rule that is applied on a row of data. **Partitions** are discussed in detail in the [Partitioning data](https://docs.pentaho.com/pdia-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data) article.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Clusters**                         | Creates Carte clusters. For more information, see [Use Carte Clusters](https://docs.pentaho.com/pdia-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |


# Work with jobs

In the [PDI client (Spoon)](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/basic-concepts-of-pdi), you can develop jobs to orchestrate your ETL activities. The entries used in your jobs define the individual ETL elements, such as transformations, applied to your data. The jobs containing your entries are stored in `.kjb` files. You can access these `.kjb` files through the PDI client.

* [Create a job](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/create-a-job)
* [Open a job](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/open-a-job)
* [Rename a folder](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/rename-a-folder-for-transformations-and-jobs)
* [Save a job](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/save-a-job)
* [Run your job](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/run-your-job)
* [Stop your job](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/stop-your-job)
* [Configure job properties](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/configure-job-properties)
* [Use the Job menu](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/use-the-job-menu-cp)


# Create a job

Follow these instructions to create your job:

1. Perform one of the following actions:
   * Click **File** > **New** > **Job**.
   * Click the **New file** icon in the toolbar and select **Job**.
   * Hold down the CTRL ALT N keys.
2. Go to the **Design** tab. Expand the folders or use the **Entries** field to search for specific entries.
3. Either drag or double-click an entry to place it on the PDI client canvas.
4. Double-click the entry to open its properties window. For help on filling out the window, click the **Help** button that is available in each entry.
5. To add another entry, either drag or double-click the entry to place it on the PDI client canvas.
   * If you dragged the entry to the canvas, you can add a hop by pressing the SHIFT key and drawing a hop from one entry to the other.
   * If you double-click it, the entry appears on the canvas with a hop already connected to your previous entry.

When finished, save the job.


# Open a job

The method you use to open an existing job depends on if you are using PDI locally on your machine or if you are [connected to a repository](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi). If you are connected to a repository, you are remotely accessing your file on the Pentaho Server. Optionally, you can open a job on a Virtual File System (VFS).

**Note:** If you get a message indicating that a plugin is missing, see [Troubleshooting Transformation Steps and Job Entries](https://docs.pentaho.com/pdia-data-integration/data-integration-issues/troubleshooting-transformation-steps-and-job-entries) for more details.

If you recently had a file open, you can also use **File** > **Open Recent**.

## On your local machine

Follow these instructions to open a job on your local machine.

1. In the PDI client, perform one of the following actions:
   * Select **File** > **Open**.
   * Click the **Open file** icon in the toolbar.
   * Click the **OPEN Files** tile from the Welcome screen.
   * Hold down the CTRL O keys.
2. Select the file from the Open window, then click **Open**.

   **Note:** By default, the folder from where the last file was accessed is opened.

The Open window closes when your job appears in the canvas.

## In the Pentaho Repository

Follow these instructions to access a job in the Pentaho Repository.

1. Verify that you are [connected to a repository](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi), which establishes remote access to the Pentaho Server.
2. In the PDI client, perform one of the following actions to access the Open repository browser window:
   * Select **File** > **Open**
   * Click the **Open file** icon in the toolbar.
   * Hold down the CTRLO keys.

     **Note:** By default, the folder from where the last file was accessed is opened.
3. To use a recently opened files, use the **Recents** option to navigate to your job.
4. Use either the search box to find your job, or use the left panel to navigate to a repository folder containing your job.

   **Note:** If the PDI is already connected to the Pentaho Repository, then only the **Recents** and **Pentaho Repository** options appear in the left pane. If the PDI is not connected to a Pentaho Repository, then the following options appear in the left pane:

   * Recents
   * Local
   * VFS Connections
   * Hadoop Clusters
5. If you are not connected to Pentaho Repository, then perform one of the following actions to access the job:
   * Double-click on your job.
   * Select it and press the **Enter** key.
   * Select it and click **Open**.
6. If you are connected to the Pentaho Repository, click **Open** to access the job.

The Open window closes when your job appears in the canvas.

## On Virtual File Systems

From the menu bar in the PDI client, select **File** > **Open** to open a PDI job on a Virtual File System (VFS). See [Connecting to Virtual File Systems](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser) for details.

<br>


# Rename a folder

You can rename a folder from the **Open**. You can rename a folder or file only if you are not connected to the Pentaho Repository.

1. Select a folder or file in the **Open** window.
2. Right-click on it.
3. Select the **Rename** option from the context menu to rename it.


# Save a job

The method you use to save a job depends on if you are using PDI locally on your machine or if you are [connected to a repository](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi). If you are connected to a repository, you are remotely saving your file on the Pentaho Server. Optionally, you can save a job on a Virtual File System (VFS).

## On your local machine

Follow these instructions to save a job on your local machine.

1. In the PDI client, perform one of the following actions:
   * Select **File** > **Save** or **File** > **Save as**.
   * Click the **Save current file** icon in the toolbar.
   * Hold down the CTRL S keys.\
     The Save As window appears.
2. Specify the job's name in the window and select the location.

   By default, the folder from where the last file is accessed is opened.

   **Note:** The file types allowed are .ktr or.kjb.
3. Click **Save**.

The window closes when your job is saved.

## In the Pentaho Repository

Follow these instructions to save a job to the Pentaho Repository.

1. Verify that you are [connected to a repository](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi), which establishes remote access to the Pentaho Server.
2. In the PDI client, perform one of the following actions:
   * Select **File** > **Save** or **File** > **Save as**.
   * Click the **Save current file** icon in the toolbar.
   * Hold down the CTRL S keys.\
     The Save As window opens.
3. Navigate to the repository folder where you want to save your job.

   By default, the folder from where the last file was accessed is opened.
4. Specify the job's name in the **File name** field.

   **Note:** The file types allowed are .ktr or.kjb.
5. Click **Save**.

The window closes when your job is saved.

## On Virtual File Systems

From the menu bar in the PDI client, select **File** > **Open** to save a PDI job on a Virtual File System (VFS). See [Connecting to Virtual File Systems](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser) for details.


# Run your job

After [creating a job](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/create-a-job) to orchestrate your ETL activities (such as your transformations), you should run it in the PDI client to test how it performs in various scenarios. With the Run Options window, you can apply and adjust different run configurations, options, parameters, and variables. By defining multiple run configurations, you have a choice of running your job locally or on a server using the Pentaho engine.

When you are ready to run your job, you can perform any of the following actions to access the Run Options window:

* Click the **Run** icon on the toolbar.
* Select **Run** from the **Action** menu.
* Press F9.

The Run Options window appears.

![Run Configuration Window](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-2312d7c5b5427d7e4052fa195dd5b6da72d9bdfc%2FPDI_Run-Options_for_Jobs_Window.png?alt=media)

In the Run Options window, you can specify a **Run configuration** to define whether the job runs locally, on the Pentaho Server, or on a slave (remote) server. To set up run configurations, see [Run Configurations](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs/run-your-job/run-configurations-work-with-jobs).

**Note:** The default Pentaho local configuration runs the job using the Pentaho engine on your local machine. You cannot edit this default configuration.

The Run Options window also lets you specify logging and other options, or experiment by passing temporary values for defined parameters and variables during each iterative run.

**Always show dialog on run** is set by default. You can deselect this option if you want to use the same run options every time you execute your job. After you have selected to not **Always show dialog on run**, you can access it again through the dropdown menu next to the **Run** icon in the toolbar, through the **Action** main menu, or by pressing F8.


# Run configurations

Some ETL activities are lightweight, such as loading in a small text file to write out to a database or filtering a few rows to trim down your results. For these activities, you can run your job locally using the default Pentaho engine. Some ETL activities are more demanding, containing many entries and steps calling other entries and steps or a network of modules. For these activities, you can set up a separate Pentaho Server dedicated for running jobs and transformations using the Pentaho engine.

You can create or edit these configurations through **Run configurations** in the **View** tab as shown below:

![Run Configuration Selection](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-b4173a84f56146108cd442d9078492ed2ccfcde2%2FPDI_View_Tab_in_Run-Options_Panel.png?alt=media)

To create a new run configuration, right-click on **Run configurations** and select **New**. To edit or delete a run configuration, right-click on an existing configuration.

**Note:** Pentaho local is the default run configuration. It runs jobs with the Pentaho engine on your local machine. You cannot edit this default configuration.

Selecting **New** or **Edit** opens the Run configuration dialog box that contains the following fields:

| Field           | Description                                        |
| --------------- | -------------------------------------------------- |
| **Name**        | Specify the name of the run configuration.         |
| **Description** | Optionally, specify details of your configuration. |


# Pentaho engine

The Pentaho engine does not execute sub-transformations or sub-jobs when you select the **Pentaho server** or **Slave server** option. If you want to run a sub-transformation on the same server where your parent job runs, select **Local** for the **Run Configuration** type.

![Run Configuration Dialog Box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-a8331438d2d8d77571fd63ddffbbd9ec7b2b59ab%2FPDI_Job_Run-Configuration_for_Pentaho_Engine_Dialog.png?alt=media)

The Settings section of the Run configuration dialog box contains the following options when **Pentaho** is selected as the **Engine** for running a job:

| Option                           | Description                                                                                                                                                                                                                                                                               |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Local**                        | Select this option to use the Pentaho engine to run a job on your local machine.                                                                                                                                                                                                          |
| **Pentaho Server**               | Select this option to run your job on the Pentaho Server. This option only appears if you are connected to a [Pentaho Repository](https://docs.pentaho.com/pdia-data-integration/use-a-pentaho-repository-in-pdi).                                                                        |
| **Slave server**                 | Select this option to send your job to a slave or remote server.                                                                                                                                                                                                                          |
| **Location**                     | If you select **Slave server**, specify the location of your remote server.                                                                                                                                                                                                               |
| **Send resources to the server** | If you specified a **Location** for a server, select to send your job to the specified server before running it. Select this option to run the job locally on the server. Any related resources, such as other referenced files, are also included in the information sent to the server. |


# Options

Errors, warnings, and other information generated as the job runs are stored in logs. You can specify how much information is in a log and whether the log is cleared each time through the **Options** section of this window. You can also enable safe mode and specify whether PDI should gather performance metrics. [Logging and Performance Monitoring](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring) describes the logging methods available in PDI.

| Option                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Clear log before running**   | Indicates whether to clear all your logs before you run your job. If your log is large, you might need to clear it before the next execution to conserve space.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Log level**                  | <p>Specifies how much logging is performed and the amount of information captured: - <strong>Nothing</strong>: No logging occurs</p><ul><li><strong>Error</strong>: Only errors are logged</li><li><strong>Minimal</strong>: Only use minimal logging</li><li><strong>Basic</strong>: This is the default level</li><li><strong>Detailed</strong>: Give detailed logging output</li><li><strong>Debug</strong>: For debugging purposes, very detailed output</li><li><strong>Row Level</strong>: Logging at a row level, which generates a lot of log data</li></ul><p><strong>Debug</strong> and <strong>Row Level</strong> logging levels contain information you may consider too sensitive to be shown. Consider the sensitivity of your data when selecting these logging levels. See the <strong>Administer Pentaho Data Integration and Analytics</strong> document for instructions on how best to use these logging methods.</p> |
| **Enable safe mode**           | Checks every row passed through your job and ensure all layouts are identical. If a row does not have the same layout as the first row, an error is generated and reported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Start job at**               | Specifies an alternative starting entry for your job. All the current entries in your job are listed as options in the dropdown menu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Gather performance metrics** | Monitors the performance of your job execution through these metrics. [Using Performance Graphs](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring) shows how to visually analyze these metrics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |


# Parameters and variables

You can temporarily modify parameters and variables for each execution of your job to experimentally determine their best values. The values you enter into these tables are only used when you run the job from the Run Options window. The values you originally defined for these parameters and variables are not permanently changed by the values you specify in these tables.

| Value Type                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Parameters](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/parameters) | Set parameter values related to your job during runtime. A parameter is a local variable. The parameters you define while creating your job are shown in the table under the **Parameters** tab. - [Arguments](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/arguments) - Set argument values passed to your job through Arguments dialog box. |
| [Variables](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables)   | Set values for user-defined and environment variables related to your job during runtime.                                                                                                                                                                                                                                                                                                                                                        |


# Stop your job

There are two different methods you can use to stop jobs running in the PDI client. The method you use depends on the processing requirements of your ETL activity. Most jobs can be stopped immediately without concern. However, since some jobs are ingesting records using messaging or streaming data, such incoming data may need to be stopped safely so that the potential for data loss is avoided.

To stop a job running in the [Data Integration perspective](https://docs.pentaho.com/pdia-data-integration/get-started-with-the-pdi-client-1/use-the-pdi-client-perspectives#data-integration-perspective) of the PDI client:

* Use **Stop** if your ETL activity should stop processing all data immediately.
* Use **Stop input processing** if your ETL activity needs to finish any records already initiated or retrieved before stopping.


# Configure job properties

Job properties are options that control how a job behaves and how it is logging what it is doing. To view the job properties, click `CTRL+T` or right-click the canvas and select **Properties** from the menu that appears. For transformation properties, See [Configure transformation properties](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/configure-transformation-properties).

* [Job tab](#job-tab)
* [Parameters tab](#parameters-tab)
* [Settings tab](#settings-tab)
* [Log tab](#log-tab)
* [Transactions tab](#transactions-tab)

## Job tab

General properties for jobs are found on the **Job** tab.

![Job settings job tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-f9dcc32a19ec40ad728b1eb01b2b301abbb55596%2FPDI_Job%20settings%20job%20tab.png?alt=media)

This table describes all of the general job properties found on the **Job** tab:

| Option                   | Description                                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| **Job Name**             | <p>The name of the job.</p><p><strong>Note:</strong> This information is required if you want to save to a repository.</p> |
| **Job filename**         | The file name of the job if it is not stored in the repository.                                                            |
| **Description**          | A user-defined short description of the job which is shown in the repository explorer.                                     |
| **Extended description** | A user-defined longer description of the job.                                                                              |
| **Status**               | The status of the job. The values are **draft** and **production**.                                                        |
| **Version**              | A description of the version.                                                                                              |
| **Directory**            | The directory in the repository where the job is kept.                                                                     |
| **Created by**           | The original creator of the job.                                                                                           |
| **Created at**           | The date and time when the job was created.                                                                                |
| **Last modified by**     | The name of the last user who modified the job.                                                                            |
| **Last modified at**     | The date and time when the job was last modified.                                                                          |

## Parameters tab

You can use the **Parameters** tab to define parameters for your jobs.

![Job settings Parameters tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-39a7a03416bd8071f57bcf198ab2f0ab32ba43b9%2FPDI_Job%20settings%20Parameters%20tab.png?alt=media)

This table describes all of the general job properties found on the **Parameters** tab:

| Option            | Description                                      |
| ----------------- | ------------------------------------------------ |
| **Parameter**     | A user-defined parameter.                        |
| **Default value** | The default value of the user-defined parameter. |
| **Description**   | A description of the parameter.                  |

## Settings tab

The following options are available on the **Settings** tab:

![Job settings Setttings tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-323dd28d4b49bb66c2f8325477f3daf0221a6a7d%2FPDI_Job%20settings%20Settings%20tab.png?alt=media)

| Option                  | Description                                                                                                                                                                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pass batch ID?**      | Select to pass the identification number of the batch to the transformation.                                                                                                                                                          |
| **Shared objects file** | PDI uses a single shared objects file for each user. The default filename is `shared.xml` and is located in the `.kettle` directory in the user’s home directory. You can define a different shared objects file, location, and name. |

## Log tab

Use the **Log** tab to specify logging settings.

![Job settings Log tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-50cb3c4a2d0d97739ff9da962c4cb50137d2949a%2FPDI_Job%20settings%20Log%20tab.png?alt=media)

This table describes all of the general job properties found on the **Log** tab:

| Option                         | Description                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Log connection**             | Specify the database connection you are using for logging. You can configure a new connection by clicking **New**.                                                                                                                                                                                                                                                                          |
| **Log Schema**                 | Specify the schema name, if supported by your database.                                                                                                                                                                                                                                                                                                                                     |
| **Log table**                  | Specify the name of the log table. f you are also using transformation logging, you must use a different table name for job logging.                                                                                                                                                                                                                                                        |
| **Logging interval (seconds)** | Specify the interval in which logs are written to the table. This property only applies to Transformation and Performance logging types.                                                                                                                                                                                                                                                    |
| **Log line timeout (days)**    | <p>Specify the number of days to keep log entries in the table before they are deleted. This property only applies to Transformation and Performance logging types.</p><p>If you find that data in the log table is not deleted as expected, see <a href="../../data-integration-issues/log-table-data-is-not-deleted">Log table data is not deleted</a> for best practice information.</p> |
| **Log size limit in lines**    | Enter the limit for the number of lines that are stored in the `LOG_FIELD`. PDI stores logging for the transformation in a long text field (CLOB). This property only applies to Transformation and Performance logging types.                                                                                                                                                              |
| **SQL button**                 | Generates the SQL needed to create the logging table and allows you to execute this SQL statement.                                                                                                                                                                                                                                                                                          |

## Transactions tab

The **Transaction** tab has one option:

![Job settings Transactions tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-a32cd9acbd584d53d8f7618fc0620de2635c17af%2FPDI_Job%20settings%20Transactions%20tab.png?alt=media)

| Option                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Make the job database transactional** | <p>You can use this property to open one unique connection per defined and used database connection in the job. Enabling this option is required to allow a failed job to be completely rolled back. See also the option within <a href="../work-with-transformations-cp">Work with transformations</a>.</p><p>Further information can be found in <a href="https://pentaho-public.atlassian.net/wiki/spaces/EAI/pages/386803253/Database+transactions+in+jobs+and+transformations">Database transactions in jobs and transformations</a>.</p> |


# Use the Job menu

Right-click any entry in the [job](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs) canvas to view the **Job** menu. Each item is described in the following table:

| Menu Item                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **New Hop**                      | Creates a new hop.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Edit**                         | Shows the configuration window for the entry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Description**                  | Allows you to add a description to the entry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Open Referenced Object**       | Opens referenced transformations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Copy**                         | Copies selected items to the clipboard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Duplicate**                    | Makes a copy of the selected items, then pastes them to the canvas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Delete**                       | Deletes selected items from the canvas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Hide**                         | <p>Hides the entry from the PDI client canvas.</p><p><strong>CAUTION:</strong></p><p>If you hide the entry, you will need to open the job XML file and hand edit it to view it again. For more details, see the troubleshooting section.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Detach**                       | Detaches the entry from the job.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Align/Distribute**             | <p>Arranges entries on the canvas so that they are aligned properly or distributed evenly. This helps create a visually pleasing job that is easier to read and digest. Align refers to where the entries are permitted along the x (horizontal) or y (vertical) axis. Distribute makes the horizontal and vertical spacing between entries consistent. Typically, you turn on the grid, then move the different entries on the canvas so that they form some sort of pattern, like a straight or branching line.</p><p>You select entries and apply the following options, as needed:</p><ul><li><strong>Align Left</strong>: Positions all entries so their left sides start on the same "x" (horizontal) coordinate as the left-most entry. After applied, entries are arranged in a straight vertical line. No changes are made to the spaces between entries.</li><li><strong>Align Right</strong>: Positions all entries so their right sides start on the same "x" (horizontal) coordinate as the right-most entry. After applied, entries are arranged in a straight vertical line. No changes are made to the spaces between entries.</li><li><strong>Align Top</strong>: Positions all entries so their top sides start on the same "y" (vertical) coordinate as the entry positioned closest to the top of the canvas. After applied, entries are arranged in a straight horizontal line. No changes are made to the spaces between entries.</li><li><strong>Align Bottom</strong>: Positions all entries so their bottom sides start on the same "y" (vertical) coordinate as the entry positioned closest to the bottom of the canvas. After applied, entries are arranged in a straight horizontal line. No changes are made to the spaces between entries.</li><li><strong>Distribute Horizontally</strong>: Positions all entries so that they are evenly spaced horizontally. After applied, entries are arranged evenly. No changes are made to the alignment.</li><li><strong>Distribute Vertically</strong>: Positions all entries so that they are evenly spaced vertically. After applied, entries are arranged evenly. No changes are made to the alignment.</li><li><strong>Snap to Grid</strong>: Aligns entries on the canvas to the grid. If grid markers do not appear on the canvas, select <strong>Tools</strong> > <strong>Options</strong> > <strong>Look & Feel</strong> > <strong>Show Canvas Grid</strong>. See the <a href="../../get-started-with-the-pdi-client-1/customize-the-pdi-client">Customize PDI Client Options</a> for more information on how to customize the PDI client.</li></ul> |
| **Restartable Checkpoint**       | Restarts a failed job at specific checkpoints, instead of rerunning the entire job from the beginning. You add checkpoints at hops that connect one job entry to another. Checkpoints are addressed in detail in the [Use Checkpoints to Restart Jobs](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/use-checkpoints-to-restart-jobs) topic.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Run Next Entries in Parallel** | Allows you to launch job entries in parallel (on the same machine or remotely).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |


# Add notes to transformations and jobs

Notes can help you and others understand the structure, design decisions, business rules, dependencies, and other aspects of your transformations and jobs.

You can add and edit notes to your transformations and jobs in the [PDI client](https://docs.pentaho.com/pdia-data-integration/get-started-with-the-pdi-client) canvas.

* [Create a note](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/add-notes-to-transformations-and-jobs/create-a-note)
* [Edit a note](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/add-notes-to-transformations-and-jobs/edit-a-note)
* [Reposition a note](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/add-notes-to-transformations-and-jobs/reposition-a-note)
* [Delete a note](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/add-notes-to-transformations-and-jobs/delete-a-note)


# Create a note

Perform the following steps to create a note:

1. Right-click the canvas and select **New Note**.

   The Notes window appears.
2. Click the **Font Style** tab to customize the font and color.
3. Click the **Note** tab, then in the **Note** field and begin typing the note.
4. Click **OK** to save the note.

The note appears on the canvas.


# Edit a note

Perform the following steps to edit a note:

1. Double-click the note on the canvas.

   The Notes window appears.
2. Click the **Font Style** tab to customize the font and color.
3. Click the **Note** tab, then in the **Note** field to edit the note.
4. Click **OK** to save the note.

The note appears on the canvas.


# Reposition a note

Perform the following steps to move the note to a different area of the canvas:

1. Drag the note to the desired position on the canvas:
2. Right-click on the note and then perform one of the following actions:
   * **Raise Note** then drag the note upwards on the canvas.
   * **Lower Note** then drag the note downwards on the canvas.


# Delete a note

Perform the following steps to delete a note:

1. Hover over the note.
2. Right-click and then select **Delete Note** from the menu that appears.


# Connecting to Virtual File Systems

You can connect to most Virtual File Systems (VFS) through VFS connections in PDI. A VFS connection is a stored set of VFS properties that you can use to connect to a specific file system. In PDI, you can add a VFS connection and then reference that connection whenever you want to [access files or folders on your Virtual File System](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/open-a-transformation-task). For example, you can use the VFS connection for Hitachi Content Platform (HCP) in any of the HCP transformation steps without the need to repeatedly enter your credentials for data access.

With a VFS connection, you can set your VFS properties with a single instance that can be used multiple times. The VFS connection supports the following file systems:

* **Amazon S3/Minio/HCP**
  * Simple Storage Service (S3) accesses the resources on Amazon Web Services. See [Working with AWS Credentials](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html) for Amazon S3 setup instructions.

    **Note:** If a connectivity issue occurs with AWS / S3, perform either of the following actions:

    * Set the Environment Variables for `AWS_REGION` or `AWS_DEFAULT_REGION` to the applicable Default Region.
    * Set the correct Default Region in the shared configuration file (`~/.aws/config`) or the credentials file (`~/.aws/credentials`). For example:

      ![AWS sample config file](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-10cb315a3e908644f3a4f14965a8e78ddc67c2b0%2FAWS_S3_sample_code.png?alt=media)

    See <https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/region-selection.html> and <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html> for more information.
  * Minio accesses data objects on an Amazon compatible storage server. See the [Minio Quickstart Guide](https://docs.min.io/docs/) for Minio setup instructions.
  * HCP uses the S3 protocol to access HCP. See [Access to HCP REST](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-hcp-rest) for more information.
* **Azure Data Lake Gen 1**

  Accesses data objects on Microsoft Azure Gen 1 storage services. You must create an Azure account and configure Azure Data Lake Storage Gen 1. See [Access to Microsoft Azure](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-microsoft-azure) for more information.

  **Note:** Support for Azure Data Lake Gen 1 is discontinued and limited to users with existing Gen 1 accounts. As a best practice, use Azure Data Lake Storage Gen 2. See [Azure](https://azure.microsoft.com/en-us/updates/action-required-switch-to-azure-data-lake-storage-gen2-by-29-february-2024/) for details.
* **Azure Data Lake Gen 2/Blob**

  Accesses data objects on Microsoft Azure Gen 2 or Blob storage services. . You must create an Azure account and configure Azure Data Lake Storage Gen 2 and Blob Storage. See [Access to Microsoft Azure](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-microsoft-azure) for more information.
* **Google Cloud Storage**

  Accesses data in the Google Cloud Storage file system. See [Google Cloud Storage](https://cloud.google.com/storage/docs) for more information on this protocol.
* **HCP REST**

  Accesses data in the Hitachi Content Platform. You must configure HCP and PDI before accessing the platform. See [Access to HCP REST](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-hcp-rest) for more information.
* **Local**

  Accesses data in your local physical file system.
* **SMB/UNC Provider**

  Accesses data in a Windows platform that uses the Server Message Block (SMB) protocol and Universal Naming Convention (UNC) string to specify the resource location path.
* **Snowflake Staging**

  Accesses a staging area used by Snowflake to load files. See [Snowflake staging area](https://docs.snowflake.net/) for more information on this protocol.

After you create a VFS connection, you can use it with PDI steps and entries that support the use of VFS connections. If you are connected to a repository, the VFS connection is saved in the repository. If you are not connected to a repository, the connection is saved locally on the machine where it was created.

If a VFS connection in PDI is not available for your Virtual File System, you may be able to access it with the VFS browser. See [VFS browser](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/vfs-browser-connecting-to-virtual-file-systems) for further details.


# Before you begin

You must first perform a few setup tasks if you need to access the Google Cloud or the Hitachi Content Platform (HCP).

* [Access to Google Cloud](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-google-cloud)
* [Access to HCP REST](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-hcp-rest)
* [Access to Microsoft Azure](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-microsoft-azure)


# Access to Google Cloud

To access Google cloud from PDI, you must have a Google account and service account credentials in the form of a JSON format key file. Additionally, you must set permissions for your Google Cloud accounts. To create service account credentials, see <https://cloud.google.com/storage/docs/authentication>.

Perform the following steps to set up your system to use Google Cloud storage:

1. Download the service account credentials file that you have created using the Google API Console to your local machine.
2. Create a new system environmental variable on your operating system named **GOOGLE\_APPLICATION\_CREDENTIALS**.
3. Set the path to the downloaded JSON service account credentials file as the value of the **GOOGLE\_APPLICATION\_CREDENTIALS** variable.

You are now ready to access files from the Google Cloud Storage file system in PDI.


# Access to HCP REST

Hitachi Content Platform (HCP) is a distributed storage system that can be used through a VFS connection in the PDI client.

Within HCP, access control lists (ACLs) grant privileges to the user to perform a variety of file operations. [Namespaces](https://knowledge.hitachivantara.com/Documents/Storage/Content_Platform/8.1.2/System_administration/Introduction_to_Hitachi_Content_Platform/01_About_Hitachi_Content_Platform/), owned and managed by tenants, are used for logical groupings, access and permissions, and object metadata such as versioning, retention and shred settings. For more information about HCP, see the [Introduction to Hitachi Content Platform](https://knowledge.hitachivantara.com/Documents/Storage/Content_Platform/8.1.2/Tenants_and_Namespaces/Introduction_to_Hitachi_Content_Platform).

Perform the following steps to setup access to HCP:

**Note:** The following process assumes that you have HCP tenant permissions and that namespaces have been created. For more information, see [Tenant Management Console](https://knowledge.hitachivantara.com/Documents/Storage/Content_Platform/8.1.2/Tenants_and_Namespaces/General_administrative_information/03_Tenant_Management_Console).

**Note:** To create a successful VFS connection to HCP, object versioning must be configured in HCP [Namespaces](https://knowledge.hitachivantara.com/Documents/Storage/Content_Platform/8.1.2/Tenants_and_Namespaces/Managing_namespaces).

1. Log on to the HCP Tenant Management Console.
2. Click **Namespaces** and then select the **Name** you want to configure.

   ![HCP Tenant Management Console](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-04ccfa45ac66944d2da343e424e608e7cbf97db3%2FPDI_HCP-DM_Dialog.png?alt=media)
3. In the **Protocols** tab, click **HTTP(S)**, and verify **Enable HTTPS** and **Enable REST API** with **Authenticated access only** are selected.
4. In the **Settings** tab, select **ACLs**.
5. Select the **Enable ACLs** check box and, when prompted, click **Enable ACLs** to confirm.

This completes the setup of HCP for accessing files in the PDI client.


# Access to Microsoft Azure

To access Azure services from PDI, you must first create and configure your Azure Data Lake Gen 1, or Azure Data Lake Storage Gen2 and Blob Storage services. you should also enable the hierarchical namespace to maximize file system performance.

* Access to the Azure services requires an Azure account with an active subscription. See [Create an account for free](https://azure.microsoft.com/en-us/free/?ref=microsoft.com\&utm_source=microsoft.com\&utm_medium=docs\&utm_campaign=visualstudio).
* Access to Azure Storage requires an Azure Storage account. See [Create a storage account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal).


# Create a VFS connection

Perform the following steps to create a VFS connection in PDI:

1. Start the PDI client (Spoon) and create a new [transformation](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Data%20Integration%20Perspective/Data%20Integration%20perspective%20in%20the%20PDI%20client/Work%20with%20transformations%20cp=GUID-1B9C8573-4C71-47FD-AF03-E9A0A43EDCD4=4=en=.md) or [job](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/work-with-jobs).
2. In the **View** tab of the Explorer pane, right-click on the **VFS Connections** folder, and then click **New**.

   The New VFS connection dialog box opens.

   ![New VFS Connection dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-823b3330ed8ea8889f29e9706a8a855c3b2f4127%2FPDI%20VFS%20connection%20dialog.png?alt=media)
3. In the **Connection Name** field, enter a name that uniquely describes this connection. Optionally, add a **Description**.

   The name can contain spaces, but cannot include special characters, such as `#`, `$`, `/`, `\`, `%`, and `%`.
4. In the **Connection Type** field, select from one of the following types:
   * **Amazon S3/Minio/HCP**
   * **Azure Data Lake Gen 1**
   * **Azure Data Lake Gen 2 / Blob**
   * **Google Cloud Storage**
   * **HCP REST**
   * **Local**
   * **SMB/UNC Provider**
   * **Snowflake Staging**
5. In the connection details panel of New VFS Connection dialog box, select the connection type details and options. Choose from the following connection types and options:

   **Note:** You can add a predefined variable file to the fields that have the ![Insert Variable Icon](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Data%20Integration%20Perspective/Data%20Integration%20perspective%20in%20the%20PDI%20client/Connecting%20to%20Virtual%20File%20Systems%20cp/VFS_Variable%20Insert_Icon=GUID-FF2B54CF-F37F-4C16-9544-36743357AE6D=1=en=Low.png)icon. Place the cursor in the required field and enter `Ctrl+Space`. Select the required file from the list of files available. The variable must be a predefined variable and not a runtime variable. The variables are defined in the Kettle.properties. For more information on variables, see [Kettle Variables](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables/kettle-variables).

| Connection type                  | Options                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Amazon**                       | <p>Click <strong>S3 Connection Type</strong> and select <strong>Amazon</strong> from the list to use an Amazon S3 connection.</p><p>Simple Storage Service (S3) accesses the resources on Amazon Web Services. See <a href="https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html">Working with AWS Credentials</a> for Amazon S3 setup instructions.</p><ul><li>Select the <strong>Authentication Type</strong>:<br>- <strong>Access Key/Secret Key</strong><br>- <strong>Credentials File</strong></li><li>Select the <strong>Region</strong>.</li><li><p>When <strong>Authentication Type</strong> is:</p><ul><li><strong>Access Key/Secret Key</strong>, then enter the <strong>Access Key</strong> and <strong>Secret Key</strong>, and optionally enter the <strong>Session Token</strong>.</li><li><strong>Credentials File</strong>, then enter the <strong>Profile Name</strong> and the <strong>File Location</strong>.</li></ul></li><li>Select the <strong>Default S3 Connection</strong> checkbox to make <strong>Amazon</strong> the default S3 connection.</li></ul>                                                                                                                                                                                                                                                                                                                          |
| **Minio/HCP**                    | <p>Click <strong>S3 Connection Type</strong> and select <strong>Minio/HCP</strong> from the list to use a Minio/HCP S3 connection.</p><p>Minio accesses data objects on an Amazon compatible storage server. See the <a href="https://docs.min.io/docs/">Minio Quickstart Guide</a> for Minio setup instructions.</p><ul><li>Enter the <strong>Access Key</strong>.</li><li>Enter the <strong>Secret Key</strong>.</li><li>Enter the <strong>Endpoint</strong>.</li><li>Enter the <strong>Signature Version</strong>.</li><li>Select the <strong>PathStyle Access</strong> checkbox to use path-style requests. Otherwise, Amazon S3 bucket-style access is used.</li><li>Select the <strong>Default S3 Connection</strong> checkbox to make <strong>Minio/HCP</strong> the default S3 connection.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Azure Data Lake Gen 1**        | <p>Accesses data objects on Microsoft Azure Gen 1 storage services. You must create an Azure account and configure Azure Data Lake Storage Gen 1. See <a href="https://docs.hitachivantara.com/r/W5Oy5NghPggWbWs_8gNJXw/bVcEnW6Cj5aOLgChBPiz5w">Access to Microsoft Azure</a> for more information.</p><ul><li>The <strong>Authentication Type</strong> is <strong>Service-to-service authentication</strong>, only.</li><li>Enter the <strong>Account Fully Qualified Domain Name</strong>.</li><li>Enter the <strong>Application (client) ID</strong>.</li><li>Enter the <strong>Client Secret.</strong></li><li>Enter the <strong>OAuth 2.0 token endpoint</strong>.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Azure Data Lake Gen 2 / Blob** | <p>Accesses data objects on Microsoft Azure Gen 2 and Blob storage services. You must create an Azure account and configure Azure Data Lake Storage Gen 2 and Blob Storage. See <a href="https://docs.hitachivantara.com/r/W5Oy5NghPggWbWs_8gNJXw/bVcEnW6Cj5aOLgChBPiz5w">Access to Microsoft Azure</a> for more information.</p><ul><li>Select the <strong>Authentication Type</strong>:<br>- <strong>Account Shared Key</strong><br>- <strong>Azure Active Directory</strong><br>- <strong>Shared Access Signature</strong></li><li>Enter the <strong>Service Account Name</strong>.</li><li>Enter the <strong>Block Size (Min 1 MB to Max 100 MB)</strong>.The default is 50.</li><li>Enter the <strong>Buffer Count (Min 2)</strong>. The default is 5.</li><li>Enter the <strong>Max Block Upload Size (Min 1 MB to 900 MB)</strong>. The default is 100.</li><li>Select the <strong>Access Tier</strong>. The default value is Hot.</li><li><p>When <strong>Authentication Type</strong> is:</p><ul><li><strong>Account Shared Key</strong>, then enter the <strong>Service Account Shared Key</strong>.</li><li><strong>Azure Active Directory</strong>, then enter the <strong>Application (client) ID</strong>, <strong>Client Secret</strong>, and <strong>Directory (tenant) ID</strong>.</li><li><strong>Shared Access Signature</strong>, then enter the <strong>Shared Access Signature</strong>.</li></ul></li></ul> |
| **Google Cloud Storage**         | <p>Accesses data objects on the Google Cloud Storage file system. See <a href="https://cloud.google.com/storage/docs">Google Cloud Storage</a> for more information on this protocol.</p><ul><li>Enter the <strong>Service Account Key Location</strong>.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **HCP REST**                     | <p>Accesses data objects on the Hitachi Content Platform. You must configure HCP and PDI before accessing the platform. You must also configure object versioning in HCP Namespaces. See <a href="https://docs.hitachivantara.com/r/W5Oy5NghPggWbWs_8gNJXw/U4R_swcuWATRSshT9TM1bw">Access to HCP</a> for more information.</p><ul><li>Enter the <strong>Host</strong> and <strong>Port</strong> number.</li><li>Enter the <strong>Tenant</strong>, <strong>Namespace</strong>, <strong>Username</strong>, and <strong>Password</strong>.</li><li>Click <strong>More options</strong> then enter the <strong>Proxy Host</strong> and <strong>Proxy Port</strong> number.</li><li>Select whether to use <strong>Accept self-signed certificate</strong>. The default is No.</li><li>Select whether the <strong>Proxy is secure</strong>. The default is No.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Local**                        | <p>Accesses a file system on your local machine.</p><ul><li>Enter the <strong>Root Folder Path</strong> or click <strong>Browse</strong> to set a folder connection in the local physical file system of the machine. Optionally, use an empty path to allow the selected roles to access the root directory and its folders.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **SMB/UNC Provider**             | <p>Accesses Server Message Block data using a Universal Naming Convention string to specify the file location.</p><ul><li>Enter the <strong>Domain</strong>. The domain name of the target machine hosting the resource. If the machine has no domain name (for example, a home computer), then use the name of the machine.</li><li>Enter the <strong>Port Number</strong>. The default is 445.</li><li>Enter the <strong>Server</strong>, <strong>User Name</strong>, and <strong>Password</strong>.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Snowflake Staging**            | <p>Accesses a staging area used by Snowflake to load files. See <a href="https://docs.snowflake.net/">Snowflake staging area</a> for more information on this protocol.</p><ul><li>Enter the <strong>Host Name</strong>.</li><li>Enter the <strong>Port Number</strong>. The default is 443.</li><li>Enter the <strong>Database</strong>.</li><li>Enter the <strong>Namespace</strong>, <strong>User Name</strong>, and <strong>Password</strong>.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

6\. For all connection types except \*\*Local\*\* which is selected in step 5, enter the \*\*Root Folder Path\*\* for your VFS connection. Enter the full path to set a connection to a specific folder. Optionally, use an empty path to allow access to all folders in the root.

```
The default is to the root and its folders in your local physical file system.
```

7\. (Optional) Click **Test** to verify your connection.

8. Click **OK** to complete the setup.

You can now use your connection to specify VFS information in your transformation steps or job entries, such as the Snowflake entries or HCP steps. See [PDI and Snowflake](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Advanced%20Pentaho%20Data%20Integration%20topics/Advanced%20topics%20\(Pentaho%20Data%20Integration%20overview\)/PDI%20and%20Snowflake%20cp=GUID-75EACA27-8EEE-4543-BD57-99A2697F1839=4=en=.md) and [PDI and Hitachi Content Platform (HCP)](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Advanced%20Pentaho%20Data%20Integration%20topics/Advanced%20topics%20\(Pentaho%20Data%20Integration%20overview\)/PDI%20and%20Hitachi%20Content%20Platform%20\(HCP\)=GUID-F4977458-2FA6-4D2C-8991-1391D0849655=6=en=.md) for more information about these entries and steps, and see [Access files with the VFS browser](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/vfs-browser-connecting-to-virtual-file-systems/use-the-vfs-browser-in-the-pdi-client) for general VFS connection details.


# Edit a VFS connection

Perform the following steps to edit an existing VFS connection:

1. Right-click the **VFS Connections** folder and select **Edit**.
2. When the Edit VFS Connection dialog box opens, select the **Pencil** icon next to the section you want to edit.


# Delete a VFS connection

Perform the following steps to delete a VFS connection:

1. Right-click the **VFS Connections** folder.
2. Select **Delete**, then **Yes, Delete**.

The deleted VFS connection no longer appears under the **VFS Connections** folder in the **View** tab of the PDI Explorer pane.


# Access files with a VFS connection

After you have created a VFS connection, you can use the VFS Open and Save dialog box to access files in the PDI client.

Follow these instructions to access files with the VFS Open or Save dialog box in the PDI client.

1. In the PDI client, select **File** > **Open URL** to open a file or **File** > **Save as** to save a file.

   The VFS Open or Save As dialog box opens, as shown in the following example:

   ![Open dialog box in the PDI client](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-e22e88115d14d9ee084ce64f6fba260ff6b1ab86%2FssPDI_OpenDialogBox_9.4.png?alt=media)

   Recently accessed files appear in the right panel.
2. Navigate to your folders and files through the **VFS connection** category in the left panel.

   When you select a folder or file, the **Recents** drop-down list updates to show the navigation path to your file location.
3. (Optional) Click on the navigation path to show and copy the Pentaho file path, even if it is a Virtual File System (VFS) path. See [Pentaho address to a VFS connection](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/pentaho-address-to-a-vfs-connection-open-a-transformation) for details on the Pentaho file path for the Virtual File System.
4. Select the file and click **Open** or **Save** depending on whether you are opening or saving a file.

The Open or Save As dialog box closes when you have access to your folder or file.

**Note:** If you are not connected to the Pentaho Repository, you can select a folder or file in the Open or Save As dialog box, click on it again, and rename it.


# Pentaho address to a VFS connection

The Pentaho address is the Pentaho virtual file system (`pvfs`) location within your VFS connection. When you are locating a file under the VFS connection category in the file access dialog box, the directory path in your Virtual File System appears in the address text box.

![VFS navigation path in the Open dialog box in the PDI client](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-737c2cdaff12fc62694969d198861a1a1d3f6cdd%2FssPDI_OpenDialogBox_VFSAddressBar.png?alt=media)

When you click in the address bar, the Pentaho address to the file appears in the text box.

![PVFS file path in the Open dialog box in the PDI client](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-f45eca9a3b4549e688d42d86915311abff88aa3d%2FssPDI_OpenDialogBox_VFSAddressBar_PVFSPath.png?alt=media)

You can copy and paste a Pentaho address into file path options of PDI steps and entries that support VFS connections.

**Note:** You must use the Pentaho virtual file system for anything related to Amazon S3. In addition, file paths and permissions in your existing transformations and jobs that use Amazon S3 are supported when **Amazon S3** is the **Default S3 Connection**.


# Create a VFS metastore

A PDI metastore is a location for storing resources shared by multiple tranformations. This enables Pentaho hyperscaler deployments to access the metastore in the cloud environment and also let the PDI client and the Pentaho Server reference the same VFS metastore. The VFS connection information is stored in an XML file The metastore can be located in three locations:

* The metastore can be stored on the machine where you're running PDI in either in your user directory or in a repository.
* If your PDI client is connected to the Pentaho Server, you will use a remote metastore located in your Pentaho Server repository.
* The metastore can be located in a cloud location accessible by a VFS connection.

Multiple users can access the metastore when it is stored in a remote location. The remote metastore has priority over a local metastore. For example, if you set up the PDI client with a valid metastore-config file and then connect to a Pentaho Server repository, your transformations will still use resources from the remote metastore, not the repository metastore.

## Enable a VFS metastore

Before you can use a remote metastore, you must enable the VFS connection in the PDI client. To do this you will create a metastore configuration XML file, then edit the VFS connection information in that file.

Perform the following steps to enable a VFS metastore:

1. Open the PDI client and create a VFS connection to the storage location that you want to use as your metastore.

   The VFS connection information will be saved to a file. See [Create a VFS connection](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/create-a-vfs-connection-in-pdi)
2. Close the PDI client.
3. Navigate to the `\Users\<yourusername>\.pentaho\metastore\pentaho\Amazon S3 Connection\` directory and copy the VFS connection file you just created to the `Users\<yourusername>\.kettle` directory.
4. Rename the file to `metastore-config`.
5. Open the `metastore-config` file with any text editor and add `scheme` and `rootPath` elements, along with their values.

   See the appropriate section in [Metastore configuration](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/broken-reference).
6. Save and close the `metastore-config` file.
7. Restart the PDI client.

The remote VFS metastore is now enabled. Note that the previous connections in the PDI client still exist in your local metastore directory, but no longer display in the PDI client. When you create a new VFS connection, the new connection will be in the location specified in your metastore-config file.

## Metastore configuration

The elements listed in the following table are required for all remote environments. When you create a VFS connection using the PDI client, you will not need to manually edit anything in the `<configuration>` section.

### Common elements

These elements are required for all VFS connections:

<table data-header-hidden><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td>Element</td><td>Value</td><td>Description</td></tr><tr><td><code>scheme</code></td><td>&#x3C;string></td><td><p>The type of connection. The values are:</p><p><strong>s3</strong> - Amazon, MinIO, and HCP</p><p><strong>gs</strong> - Google cloud storage</p><p><strong>abfss</strong> - Azure Data Lake Storage Gen2</p></td></tr><tr><td><code>rootPath</code></td><td>&#x3C;bucket-name>[/&#x3C;path>]</td><td><p>The bucket name and optional folder path where you want to create the VFS metastore. The <code>rootPath</code> element must point to the location where you will store the metastore file on the cloud location.</p><p>This is analogous to the <code>.pentaho</code> folder in a local metastore.</p><p>Examples:</p><ul><li><code>miniobucket/dir1</code></li><li><code>gcpbucket/dir1</code></li></ul></td></tr><tr><td><code>children</code></td><td></td><td><p>A container for type-specific configurations. For example:</p><pre><code>&#x3C;children>
    &#x3C;child>
&#x3C;id>description&#x3C;/id>
         &#x3C;value>&#x3C;/value>
    &#x3C;type>String&#x3C;/type>
&#x3C;/child>
…
&#x3C;/children>

</code></pre></td></tr></tbody></table>

### S3 elements

The elements listed in the table below apply to S3 environments. Some elements are conditional, based on your choices for other settings:

| Element               | Value                            | Description                                                                                                                                                                           |
| --------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `accessKey`           | `<s3-access-key>`                | The S3 user’s access key.                                                                                                                                                             |
| `secretKey`           | `<s3-secret-key>`                | The S3 user’s secret key.                                                                                                                                                             |
| `endPoint`            | `<s3-endpoint>`                  | <p>The URL to access the S3 location. Examples:</p><p><code>http\://\<host ip>:port</code></p><p><code><https://my-hcp-namespace.my-hcp-tenant.hcpdemo.hitachivantara.com></code></p> |
| `region`              | `<s3-region>`                    | The user-designated region. For example, `us-east-1`.                                                                                                                                 |
| `connectionType`      | 0 or 1                           | <p>The connection type value. The values are:</p><p><strong>0</strong> - to connect to AWS</p><p><strong>1</strong> - to connect to MinIO or HCP</p>                                  |
| `credentialFile`      |                                  | An encrypted string that is not user editable                                                                                                                                         |
| `profileName`         | `<string>`                       | The AWS user profile connection when the Type is 0 (AWS) and the `authType` is 1 (credentials file)                                                                                   |
| `defaultS3Config`     | true or false                    | The setting that controls whether the default S3 configuration is used. Set to `true` to use the default S3 configuration                                                             |
| `credentialsFilePath` | `<path to AWS credentials file>` | The path to the AWS credentials file when the connectionType is 0 (AWS) and the authType is 1 (credentials file),                                                                     |
| `pathStyleAccess`     | true or false                    | The setting that controls which access style is used. Specify `true` to use a path-style access; `false` to use S3 bucket-style access                                                |
| `signatureVersion`    | `AWSS3V4SignerType`              | The version of signature used for communicating with the AWS S3 location of your metastore.                                                                                           |
| `name`                | `vfsMetastore`                   | The name for the connection.                                                                                                                                                          |
| `description`         | `<string>`                       | A description of the connection.                                                                                                                                                      |
| `sessionToken`        | `<session token string>`         | Optional. A temporary credential that is used if the AWS S3 bucket is configured to require a session token for access                                                                |
| `authType`            | 0 or 1                           | <p>The authentication type to use when the connection type is 0 (AWS):</p><p>0 – Access key/Secret key</p><p>1 – Credentials file</p>                                                 |

### GCP elements

The elements listed in the table below apply to GCP environments:

| Element             | Value      | Description                                                                |
| ------------------- | ---------- | -------------------------------------------------------------------------- |
| `serviceAccountKey` | `<string>` | A key that is generated based on the contents of the service account JSON. |
| `keyPath`           | `<path>`   | The path to the file containing the GCP service account JSON.              |
| `name`              | `<string>` | The name of the connection.                                                |
| `description`       | `<string>` | A description of the connection.                                           |

### Azure Data Lake Storage Gen2 elements

The elements listed in the table below apply to Azure Data Lake Storage Gen2 environments. See [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/) documentation for more information.

| Element               | Value                | Description                                                                                                                                    |
| --------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `sharedKey`           | `<encrypted string>` | The shared key for accessing the service.                                                                                                      |
| `accountName`         | `<encrypted string>` | The name of the account.                                                                                                                       |
| `accessTier`          | `<string>`           | The access tier value. The default is `Hot.`                                                                                                   |
| `blockSize`           | `<Integer>`          | The default is 50.                                                                                                                             |
| `maxSingleUploadSize` | `<Integer>`          | The default is 100.                                                                                                                            |
| `bufferCount`         | `<Integer>`          | The default is 5.\[MB1]                                                                                                                        |
| `name`                | `<string>`           | The name of the connection.                                                                                                                    |
| `authType`            | `0`, `1`, or `2`     | <p>The authorization type. The values are:</p><p>0 - Account Shared Key</p><p>1 - Azure Active Directory</p><p>2 - Shared Access Signature</p> |


# Steps and entries supporting VFS connections

You may have a transformation or a job containing a step or entry that accesses a file on a Virtual File System.

The following steps and entries support VFS connections:

* [Avro Input](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/avro-input)
* [Avro Output](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/avro-output)
* [Bulk load from MySQL into file](http://wiki.pentaho.com/display/EAI/BulkLoad+from+Mysql+to+file)
* [Bulk load into MSSQL](http://wiki.pentaho.com/display/EAI/BulkLoad+into+MSSQL)
* [Bulk load into MySQL](http://wiki.pentaho.com/display/EAI/Bulkload+into+MySQL)
* [Copybook Input](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/copybook-input-pdi-step)
* [CSV File Input](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/csv-file-input)
* [De-serialize from file](http://wiki.pentaho.com/display/EAI/De-serialize+from+file)
* [Fixed file input](http://wiki.pentaho.com/display/EAI/Fixed+File+Input)
* [Get data from XML](http://wiki.pentaho.com/display/EAI/Get+Data+From+XML)
* [Get File Names](http://wiki.pentaho.com/display/EAI/Get+File+Names)
* [Get Files Rows Count](http://wiki.pentaho.com/display/EAI/Get+Files+Rows+Count)
* [Get SubFolder names](http://wiki.pentaho.com/display/EAI/Get+SubFolder+names)
* [Google Analytics](http://wiki.pentaho.com/display/EAI/Google+Analytics)
* [GZIP CSV Input](http://wiki.pentaho.com/display/EAI/GZIP+CSV+Input)
* [Job (job entry)](https://docs.pentaho.com/pdia-data-integration/pdi-job-entries-reference-overview/job-job-entry)
* [JSON Input](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/json-input)
* [JSON output](http://wiki.pentaho.com/display/EAI/JSON+output)
* [ORC Input](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/orc-input)
* [ORC Output](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/orc-output)
* [Parquet Input](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/parquet-input)
* [Parquet Output](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/parquet-output)
* [Query HCP](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/query-hcp)
* [Read metadata from Copybook](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/read-metadata-from-copybook)
* [Read metadata from HCP](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/read-metadata-from-hcp)
* [Text File Output](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/text-file-output-cp)
* [Transformation (job entry)](https://docs.pentaho.com/pdia-data-integration/pdi-job-entries-reference-overview/transformation-job-entry-cp)
* [Write metadata to HCP](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/write-metadata-to-hcp)


# VFS browser

In some transformation steps and job entries, a Virtual File System (VFS) browser is used in place of VFS connections and the Open dialog box. When you use the VFS browser, specify a VFS URL instead of the VFS connection. The files are accessed using HTTP and the URLs contain schema data that identify a protocol to use. Your files can be local or remote, and can reside in compressed formats such as TAR and ZIP. For more information, see the [Apache Commons VFS documentation](http://commons.apache.org/proper/commons-vfs/).

## Before you begin

If you need to access a Google Drive, see [Access to a Google Drive](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-google-cloud).


# Access to a Google Drive

Perform the following setup steps to initially access your Google Drive.

1. Follow the "Step 1" procedure in the article ["Build your first Drive app (Java)"](https://developers.google.com/drive/api/v3/quickstart/java) in the [Google Drive APIs documentation](https://developers.google.com/drive/).

   This procedure turns on the Google Drive API and creates a `credentials.json` file.
2. Rename the `credentials.json` file to `client_secret.json`. Copy and paste the renamed file into the `data-integration/plugins/pentaho-googledrive-vfs/credentials` directory.
3. Restart PDI.

   The **Google Drive** option does not appear when creating a VFS connection until you copy and paste the `client_secret.json` file into the `credentials` directory and restart PDI.
4. Log in to your Google account.
5. Enter you Google account credentials and log in. The Google Drive permission window displays.
6. Click **Allow** to access your Google Drive Resources.

After this initialization, Pentaho stores a security token called **StoredCredential** in the `data-integration/plugins/pentaho-googledrive-vfs/credentials` directory. With this token, you can access your Google Drive resources whenever you log in to your Google account. If this security token is deleted, you are prompted to log in to your Google account after restarting PDI. If you change your Google account permissions, you must delete the token and repeat the previous steps to generate a new token.

**Note:** If you want to access your Google Drive via a transformation running directly on your Pentaho Server, copy then paste the **StoredCredential** and the `client_secret.json` files into the `pentaho-server/pentaho-solutions/system/kettle/plugins/pentaho-googledrive-vfs/credentials` directory on your Pentaho Server.


# Access files with the VFS browser

Perform the following steps to access your files with the VFS browser.

1. Select **File** > **Open** in the PDI client to open the VFS browser.

   The Open dialog box appears.

   ![Open dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-e0db2371f2c71a4ffa02b6e8278820440e1b56b1%2FPDI%20Open%20file%20dialog%20box.png?alt=media)
2. In the left pane, select the type of file system. The following file systems are supported:
   * **Local**: Opens files on your local machine. Use the folders in the **Name** panel of the Open dialog box to select a resource.
   * **Hadoop Cluster**: Opens files on any Hadoop cluster except S3. Click the **Hadoop Cluster** drop-down box to select your cluster, then the resource you want to access.
   * **HDFS**: Opens files on Hadoop distributed file systems. Select the cluster you want for the **Hadoop Cluster** option, then select the resource you want to access.
   * **Google Drive**: Opens files on the Google file system. You must configure PDI to access the Google file system. See [Access to a Google Drive](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/vfs-browser-connecting-to-virtual-file-systems/access-to-a-google-drive) for more information.
   * **VFS Connections**: Opens files using a stored set of VFS properties to connect to a specific file system.
     * **Amazon S3/Minio/HCP**
     * **Azure Data Lake Gen 1**
     * **Azure Data Lake Gen 2 / Blob**
     * **Google Cloud Storage**
     * **HCP REST**
     * **Local**
     * **SMB/UNC Provider**
     * **Snowflake Staging**
3. Alternatively, in the **Address** bar, enter the VFS URI.

   The following examples are VFS URI addresses:

   * **Local**: `ftp://userID:password@ftp.myhost.com/path_to/file.txt`
   * **HDFS**: `hdfs://myusername:mypassword@mynamenode:port/path`
   * **SMB/UNC Provider**: `smb://<domain>;<username>:<password>@<server>:<port>/<path>`**Note:** The SMB “domain” is the Windows host name, for example, and “domain” and “server” can be the same in the case of an IP address.
4. (Optional) Select another value in the **File type** menu to filter on file types other than transformations and jobs, which is the default value.
5. (Optional) Select a file or folder and click the **X** icon in the upper-right corner of the browser to delete it.
6. (Optional) click the **+** icon to create a new folder.

**Note:** VFS dialog boxes are configured through specific transformation parameters. See [Configure VFS options](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/vfs-browser-connecting-to-virtual-file-systems/configure-vfs-options) for more information.


# Supported steps and entries

The following steps and entries support the VFS browser:

* [Amazon EMR Job Executor](https://docs.pentaho.com/pdia-data-integration/pdi-job-entries-reference-overview/amazon-emr-job-executor) (introduced in v.9.0)
* [Amazon Hive Job Executor](https://docs.pentaho.com/pdia-data-integration/pdi-job-entries-reference-overview/amazon-hive-job-executor) (introduced in v.9.0)
* [AMQP Consumer](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/amqp-consumer) (introduced in v.9.0)
* [Avro Input](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/avro-input) (introduced in v.8.3)
* [Avro Output](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/avro-output) (introduced in v.8.3)
* [ETL metadata injection](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection)
* [File Exists (Job Entry)](https://docs.pentaho.com/pdia-data-integration/pdi-job-entries-reference-overview/file-exists-job-entry)
* [Hadoop Copy Files](https://docs.pentaho.com/pdia-data-integration/pdi-job-entries-reference-overview/hadoop-copy-files)
* [Hadoop File Input](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/hadoop-file-input-cp-main-page)
* [Hadoop File Output](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/hadoop-file-output-cp-main-page)
* [JMS Consumer](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/jms-consumer) (introduced in v.9.0)
* [Job Executor](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/job-executor) (introduced in v.9.0)
* [Kafka consumer](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer) (introduced in v.9.0)
* [Kinesis consumer](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/kinesis-consumer) (introduced in v.9.0)
* [Mapping](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/mapping) (sub-transformation)
* [MQTT Consumer](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/mqtt-consumer) (introduced in v.9.0)
* [ORC Input](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/orc-input) (introduced in v.8.3)
* [ORC Output](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/orc-output) (introduced in v.8.3)
* [Parquet Input](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/parquet-input) (introduced in v.8.3)
* [Parquet Output](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/parquet-output) (introduced in v.8.3)
* [Oozie Job Executor](http://wiki.pentaho.com/display/EAI/Oozie+Job+Executor) (introduced in v.9.0)
* [Simple Mapping](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/simple-mapping-sub-transformation) (introduced in v.9.0)
* [Single Threader](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/single-threader) (introduced in v.9.0)
* [Sqoop Export](http://wiki.pentaho.com/display/EAI/Sqoop+Export) (introduced in v.9.0)
* [Sqoop Import](http://wiki.pentaho.com/display/EAI/Sqoop+Import) (introduced in v.9.0)
* [Transformation Executor](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/transformation-executor) (introduced in v.9.0)
* [Weka Scoring](https://wiki.pentaho.com/display/EAI/Weka+Scoring) (introduced in v.9.0)

**Note:** If you have a Pentaho address to an established VFS connection, you can copy and paste your PVFS location into the file or folder option of any of the steps and entries listed here. You do not need to click **Browse** to access the VFS browser.

The VFS dialog boxes are configured through specific transformation parameters. See [Configure SFTP VFS](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/vfs-browser-connecting-to-virtual-file-systems/broken-reference) for more information on configuring options for SFTP.


# Configure VFS options

The VFS browser can be configured to set variables as parameters for use at runtime. A `VFS Configuration Sample.ktr` sample transformation containing some examples of the parameters you can set is located in the `data-integration/samples/transformations` directory. For more information on setting variables, see [Specifying VFS properties as parameters](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Data%20Integration%20Perspective/Data%20Integration%20perspective%20in%20the%20PDI%20client/Advanced%20topics%20\(PDI%20perspective\)/PDI%20run%20modifiers/Parameters/VFS%20properties/Specifying%20VFS%20properties%20as%20parameters=GUID-1AFFCB92-45CC-43DB-BFB5-9F50E8451FB7=3=en=.md). For an example of configuring an SFTP VFS connection, see [Configure SFTP VFS](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/vfs-browser-connecting-to-virtual-file-systems/broken-reference).


# Logging and performance monitoring

**Pentaho Data Integration** provides you with several methods in which to monitor the performance of jobs and transformations. Logging offers you summarized information regarding a job or transformation such as the number of records inserted and the total elapsed time spent in a transformation. In addition, logging provides detailed information about exceptions, errors, and debugging details.

You may want to enable logging and step performance monitoring to determine if a job completed with errors or to review errors that were encountered during processing. In headless environments, most ETL in production is not run from the graphical user interface and you need a place to watch initiated job results. Performance monitoring can provide you with useful information for both current performance problems and capacity planning.

To see what effect your transformation will have on the data sources it includes, go to the **Action** menu and click on **Impact**. PDI will perform an impact analysis to determine how your data sources will be affected by the transformation if it is completed successfully.

If you are an administrative user and want to monitor jobs and transformations, you must first set up logging and performance monitoring in the PDI client (Spoon). For more information about monitoring jobs and transformations, see the **Administer Pentaho Data Integration and Analytics** document.


# Set up transformation logging

Follow the instructions below to create a log table that keeps a history of information associated with your field information.

1. Ask your system administrator to create a database or table space called `PdiLog`.
2. Right-click in the workspace (canvas) where you have an open transformation and select **Properties**, or press CTRL T.

   The Transformation properties dialog box appears.

   ![Transformation properties dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-7ebaea9efbe698b707752080accbf6a884544fcb%2FPDI_TransformationProperties_Dialog.png?alt=media)
3. In the Transformation properties dialog box, click the **Logging** tab. In the left-side navigation pane, select which type of logging you want to use.

   ![Logging tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-927a40271d52442bf30caac47dc60e6842375796%2FPDI_TransformationProperties_Dialog_Log.png?alt=media)
4. In the **Logging** tab, enter the following information.

| Option                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Log Connection**               | Specify the database connection you are using for logging. You can configure a new connection by clicking **New**.                                                                                                                                                                                                                                                                                                                                     |
| **Log table schema**             | Specify the schema name, if supported by your database.                                                                                                                                                                                                                                                                                                                                                                                                |
| **Log table name**               | <p>Specify the name of the log table.</p><p><strong>Note:</strong> If you are also using job logging, use a different table name for transformation logging.</p>                                                                                                                                                                                                                                                                                       |
| **Logging interval (seconds)**   | <p>Specify the interval in which logs are written to the table.</p><p>This property only applies to <strong>Transformation</strong> and <strong>Performance</strong> logging types.</p>                                                                                                                                                                                                                                                                |
| **Log record timeout (in days)** | <p>Specify the number of days to keep log entries in the table before they are deleted.</p><p>This property only applies to <strong>Transformation</strong> and <strong>Performance</strong> logging types.</p><p>If you find that data in the log table is not deleted as expected, see <a href="../../data-integration-issues/log-table-data-is-not-deleted">Log table data is not deleted</a> in Troubleshooting for best practice information.</p> |
| **Log size limit in lines**      | <p>Enter the limit for the number of lines that are stored in the <strong>LOG\_FIELD</strong>. PDI stores logging for the transformation in a long text field (CLOB).</p><p>This property only applies to the <strong>Transformation</strong> logging type.</p>                                                                                                                                                                                        |

5\. Select the fields you want to log in the \*\*Fields to log\*\* pane, or keep the default selections.

```
**Note:** For effective deletion of expired logs, the **LOGDATE** and **TRANSNAME** fields in the **Fields to log** pane are enabled by default.
```

6\. Click the **SQL** button.

```
PDI checks the log table.
```

7\. If the Simple SQL editor opens, go to step 8. Otherwise, proceed to step 10.

8. Verify your table name, field selections and indices in the Simple SQL editor, and then click **Execute** to create your log table.

   PDI creates or revises the table and displays the results in the Results dialog box.
9. Click **OK** to exit the Results dialog box. Click **Close** to exit the Simple SQL editor.
10. Click **OK** to exit the Transformation properties dialog box.

The next time you run your transformation, logging information will appear under the **Execution History** tab.

**Note:** Monitoring the **LOG\_FIELD** field can negatively impact Pentaho Server performance. However, if you do not select all fields, including **LOG\_FIELD**, when configuring transformation logging, you will not see information about this transformation in the Operations Mart logging.


# Set up job logging

Follow the instructions below to create a log table that keeps a history of information associated with your job information.

1. Ask your system administrator to create a database or table space called `PdiLog`.
2. Right-click in the workspace (canvas) where you have an open job and select **Properties**, or press CTRL T.

   The Job properties dialog box appears.

   ![Job properties dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-141e9f62d021f6757307649da8c86eb0e3c48607%2FPDI_JobProperties_Dialog.png?alt=media)
3. In the Job properties dialog box, click the **Log** tab. In the left-side navigation pane, select which type of logging you want to use.

   ![Log tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-a27cc7c32ce622f6433b73268153ef2e36fbe5e1%2FPDI_JobProperties_Dialog_Log.png?alt=media)
4. In the **Log** tab, enter the following information.

| Option                         | Description                                                                                                                                                                                                                                                                                                                        |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Log Connection**             | Specify the database connection you are using for logging. You can configure a new connection by clicking **New**.                                                                                                                                                                                                                 |
| **Log schema**                 | Specify the schema name, if supported by your database.                                                                                                                                                                                                                                                                            |
| **Log table**                  | <p>Specify the name of the log table.</p><p><strong>Note:</strong> If you are also using transformation logging, use a different table name for jobs.</p>                                                                                                                                                                          |
| **Logging interval (seconds)** | <p>Specify the interval in which logs are written to the table.</p><p>This property only applies to <strong>Job log table</strong> logging type.</p>                                                                                                                                                                               |
| **Log line timeout (days)**    | <p>Specify the number of days to keep log entries in the table before they are deleted.</p><p>If you find that data in the log table is not deleted as expected, see <a href="../../data-integration-issues/log-table-data-is-not-deleted">Log table data is not deleted</a> in Troubleshooting for best practice information.</p> |
| **Log size limit in lines**    | <p>Enter the limit for the number of lines that are stored in the <strong>LOG\_FIELD</strong>. PDI stores logging for the job in a long text field (CLOB).</p><p>This property only applies to <strong>Job log table</strong> logging type.</p>                                                                                    |

5\. Select the fields you want to log in the \*\*Log table fields\*\* pane, or keep the default selections.

```
**Note:** For effective deletion of expired logs, the **LOGDATE**, and **JOBNAME** \(or **TRANSNAME**\) fields in the **Log table fields** pane are enabled by default.
```

6\. Click the **SQL** button.

```
PDI checks the log table.
```

7\. If the Simple SQL editor opens, proceed to the next step. If it does not open, go to step 10.

8. Verify your table name, field selections and indices in the Simple SQL editor, and then click **Execute** to create your log table.

   PDI creates or revises the table and displays the results in the Results dialog box.
9. Click **OK** to exit the Results dialog box. Click **Close** to exit the Simple SQL editor.
10. Click **OK** to exit the Job properties dialog box.

The next time you run your job, logging information will appear under the **History** tab.

**Note:** Monitoring the **LOG\_FIELD** field can negatively impact Pentaho Server performance. However, if you do not select all fields, including **LOG\_FIELD**, when configuring transformation logging, you will not see information about this transformation in the Operations Mart logging.


# Logging levels

When you run a job or transformation that has logging enabled, you have the following log level verbosity options in the Run Options window:

| Log Level     | Description                                                   |
| ------------- | ------------------------------------------------------------- |
| **Nothing**   | Do not record any logging output.                             |
| **Error**     | Only show errors.                                             |
| **Minimal**   | Only use minimal logging.                                     |
| **Basic**     | This is the default level.                                    |
| **Detailed**  | Give detailed logging output.                                 |
| **Debug**     | For debugging purposes, very detailed output.                 |
| **Row Level** | Logging at a row level. This will generate a lot of log data. |

If the **Enable time** option is selected, all lines in the logging will be preceded by the time of day.


# Monitor performance

There are a few ways that you can monitor step performance in PDI. Two tools are particularly helpful: the Sniff Test tool and the **Monitoring** tab. You can also use graphs to view performance.

* [Sniff Test tool](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/monitor-performance/sniff-test-tool)
* [Monitoring tab](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/monitor-performance/monitoring-tab)
* [Use performance graphs](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/monitor-performance/use-performance-graphs)


# Sniff Test tool

The Sniff Test displays data as it travels from one step to another in the stream. The Sniff Test is designed to be used as a supplement to logs so that you can debug complex situations.

**Note:** Applying a Sniff Test slows transformation run speed, so use with care.

To use this, complete these steps:

1. Right-click a step in the transformation as it runs.
2. Select **Sniff Test During Execution**.

   There are three options in this menu:

   * **Sniff test input rows** - Shows the data inputted into the step.
   * **Sniff test output rows** - Shows the data outputted from the step.
   * **Sniff test error handling** - Shows error handling data.

After you have selected an option, values in the data stream appear. You are also able to observe throughput.


# Monitoring tab

Pentaho Data Integration provides you with a tool for tracking the performance of individual steps in a transformation. By helping you identify the slowest step in the transformation, you can fine-tune and enhance the performance of your transformations.

You enable the step performance monitoring in the Transformation Properties dialog box:

1. Right-click in the workspace that is displaying your transformation and select **Transformation Settings**.

   You can also access the Transformation Properties dialog box, by pressing CTRL T.
2. In the dialog box, select **Enable step performance monitoring?**

![Transformation Properties Dialog Box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-d94a33f9c385001195d5823f02a2e556c1cda525%2FTransformationProperties_Monitoring.png?alt=media)

Step performance monitoring may cause memory consumption problems in long-running transformations. By default, a performance snapshot is taken for all the running steps every second. This is not a CPU-intensive operation and, in most instances, does not negatively impact performance unless you have many steps in a transformation or you take a lot of snapshots (several per second, for example). You can control the number of snapshots in memory by changing the **Maximum number of snapshots in memory** value. In addition, if you run in Spoon locally you may consume a fair amount of CPU power when you update the JFreeChart graphics under the **Performance** tab. Running in "headless" mode (Kitchen, Pan, Pentaho Server \[slave server], Carte, Pentaho BI platform, and so on) does not have this drawback and should provide you with accurate performance statistics.


# Use performance graphs

If you configured step performance monitoring with database logging, you can view performance evolution graphs. Performance graphs provide you with a visual interpretation of how your transformation is processing. To view **Performance Graphs**, make sure you enable the Performance logging type.

![Performance Graph Example](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-3162eb7cdb12a390cac14560c3ea0f92b9ed0385%2Fpdi_performance_graph.png?alt=media)


# PDI performance tuning tips

The tips described here may help you to identify and correct performance-related issues associated with PDI transformations.

| Step          | Tip                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| JS            | Turn off compatibility mode                                                   | <p>Rewriting JavaScript to use a format that is not compatible with previous versions is, in most instances, easy to do and makes scripts easier to work with and to read. By default, old JavaScript programs run in compatibility mode. That means that the step will process like it did in a previous version. You may see a small performance drop because of the overload associated with forcing compatibility. If you want to make use of the new architecture, disable compatibility mode and change the code as shown below:</p><ul><li><code>intField.getInteger() > intField</code></li><li><code>numberField.getNumber() > numberField</code></li><li><code>dateField.getDate() > dateField</code></li><li><code>bigNumberField.getBigNumber() > bigNumberField</code></li><li>and so on...</li></ul><p>Instead of Java methods, use the built-in library. Notice that the resulting program code is more intuitive. For example:</p><ul><li>checking for null is now: <code>field.isNull() > field==null</code></li><li>Converting string to date: <code>field.Clone().str2dat() > str2date(field)</code></li><li>and so on...</li></ul><p>If you convert your code as shown above, you may get significant performance benefits.</p><p><strong>Note:</strong> It is no longer possible to modify data in-place using the value methods. This was a design decision to ensure that no data with the wrong type would end up in the output rows of the step. Instead of modifying fields in-place, create new fields using the table at the bottom of the Modified JavaScript transformation.</p> |
| JS            | Combine steps                                                                 | One large JavaScript step runs faster than three consecutive smaller steps. Combining processes in one larger step helps to reduce overhead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| JS            | Avoid the JavaScript step or write a custom plug in                           | Remember that while JavaScript is the fastest scripting language for Java, it is still a scripting language. If you do the same amount of work in a native step or plugin, you avoid the overhead of the JS scripting engine. This has been known to result in significant performance gains. It is also the primary reason why the Calculator step was created — to avoid the use of JavaScript for simple calculations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| JS            | Create a copy of a field                                                      | No JavaScript is required for this, a Select Values step does the trick. You can specify the same field twice. Once without a rename, once (or more) with a rename. Another trick is to use B=NVL(A,A) in a Calculator step where B is forced to be a copy of A.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| JS            | Data conversion                                                               | Consider performing conversions between data types (dates, numeric data, and so on) in a Select Values step. You can do this in the **Metadata** tab of the step.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| JS            | Variable creation                                                             | If you have variables that can be declared once at the beginning of the transformation, make sure you put them in a separate script and mark that script as a startup script (right click on the script name in the tab). JavaScript object creation is time consuming so if you can avoid creating a new object for every row you are transforming, this will translate to a performance boost for the step.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| N/A           | Launch several copies of a step                                               | <p>There are two important reasons why launching multiple copies of a step may result in better performance:1. The step uses a lot of CPU resources and you have multiple processor cores in your computer. Example: a JavaScript step.<br>2. Network latencies and launching multiple copies of a step can reduce average latency. If you have a low network latency of say 5ms and you need to do a round trip to the database, the maximum performance you get is 200 (x5) rows per second, even if the database is running smoothly. You can try to reduce the round trips with caching, but if not, you can try to run multiple copies. Example: a database lookup or table output.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| N/A           | Manage thread priorities                                                      | This feature that is found in the Transformation Settings dialog box under the (**Misc** tab) improves performance by reducing the locking overhead in certain situations. This feature is enabled by default for new transformations that are created in recent versions, but for older transformations this can be different.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Select Values | If possible, don't remove fields in Select Values                             | Don't remove fields in Select Value unless you must. It's a CPU-intensive task as the engine needs to reconstruct the complete row. It is almost always faster to add fields to a row rather than delete fields from a row.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Get Variables | Watch your use of Get Variables                                               | May cause bottlenecks if you use it in a high-volume stream (accepting input). To solve the problem, take the Get Variables step out of the transformation (right click, detach) then insert it in with a Join Rows step. Make sure to specify the main step from which to read in the Join Rows step. Set it to the step that originally provided the Get Variables step with data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| N/A           | Use new text file input                                                       | The CSV File Input or Fixed File Input steps provide optimal performance. If you have a fixed width (field/row) input file, you can even read data in parallel. (multiple copies) These new steps have been rewritten using Non-blocking I/O (NIO) features. Typically, the larger the NIO buffer you specify in the step, the better your read performance will be.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| N/A           | When appropriate, use lazy conversion                                         | In instances in which you are reading data from a text file and you write the data back to a text file, use Lazy conversion to speed up the process. The principle behind lazy conversion that it delays data conversion in hopes that it isn't necessary (reading from a file and writing it back comes to mind). Beyond helping with data conversion, lazy conversion also helps to keep the data in "binary" storage form. This, in turn, helps the internal Kettle engine to perform faster data serialization (sort, clustering, and so on). The **Lazy Conversion** option is available in the CSV File Input and Fixed File Input text file reading steps.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Join Rows     | Use Join Rows                                                                 | You need to specify the main step from which to read. This prevents the step from performing any unnecessary spooling to disk. If you are joining with a set of data that can fit into memory, make sure that the cache size (in rows of data) is large enough. This prevents (slow) spooling to disk.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| N/A           | Review the big picture: database, commit size, row set size and other factors | Consider how the whole environment influences performance. There can be limiting factors in the transformation itself and limiting factors that result from other applications and PDI. Performance depends on your database, your tables, indexes, the JDBC driver, your hardware, speed of the LAN connection to the database, the row size of data and your transformation itself. Test performance using different commit sizes and changing the number of rows in row sets in your transformation settings. Change buffer sizes in your JDBC drivers or database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| N/A           | Step Performance Monitoring                                                   | Step Performance Monitoring is an important tool that allows you identify the slowest step in your transformation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |


# Logging best practices

You can improve your logging with log rotation and other best practices.

For more information, see the **Administer Pentaho Data Integration and Analytics** document.


# Advanced topics

The following topics help to extend your knowledge of PDI beyond basic setup and use:

* [Understanding PDI data types and field metadata](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata)

  Learn how data is treated in PDI to understand data type and field metadata behaviors in transformations and jobs.
* [PDI Run Modifiers](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers)

  Use arguments, parameters, or variables to modify how you run transformation and jobs.
* [Reuse Transformation Flows with Mapping Steps](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/mapping)

  Learn how to map commonly used steps into their own steps.
* [Use Checkpoints to Restart Jobs](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/use-checkpoints-to-restart-jobs)

  Learn how to restart a job at the last checkpoint before an error occurred.
* [Use the SQL Editor](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/use-the-sql-editor)

  Learn how to generate SQL statements.
* [Use the Database Explorer](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/use-the-database-explorer)

  Explore configured database connections.
* [Transactional Databases and Job Rollback](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/transactional-databases-and-job-rollback)

  Implement job rollback by making the transformation or job databases transactional.
* [Interact with Web Services](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/web-services-steps)

  Determine what must occur if your transformation or job interacts with a web service.


# Understanding PDI data types and field metadata

This section is for users who want to maximize the efficiency of their transformation and job results.

As a best practice for producing consistent, predictable outcomes when working with your data in PDI, you must consider how the Pentaho engine processes different data types and field metadata in transformations and jobs. For example, steps like [Avro Input](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/Avro%20Input=GUID-88F915B8-9584-4C38-9974-36D62478D0E4=3=en=.md) and [Text File Input](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/text-file-input-cp), require additional considerations to best meet your working requirements for specific data types, mathematical operations, number conversions, and formatting.

**Note:** As a rule, data is never modified by metadata inside of PDI. Data is only modified when PDI writes to files or similar objects, but not to databases. Refer to the sections below that apply to your use case.


# Data type mappings

PDI data types map internally to Java data types, so the Java behavior of these data types applies to the associated fields, parameters, and variables used in your transformations and jobs. The following table describes these mappings.

| PDI data type    | Java data type | Description                                                                   |
| ---------------- | -------------- | ----------------------------------------------------------------------------- |
| BigNumber        | BigDecimal     | An arbitrary unlimited precision number.                                      |
| Binary           | Byte\[]        | An array of bytes that contain any type of binary data.                       |
| Boolean          | Boolean        | A boolean value `true` or `false.`                                            |
| Date             | Date           | A date-time value with millisecond precision.                                 |
| Integer          | Long           | A signed long 64-bit integer.                                                 |
| Internet Address | InetAddress    | An Internet Protocol (IP) address.                                            |
| Number           | Double         | A double precision floating point value.                                      |
| String           | String         | A variable unlimited length text encoded in UTF-8 (Unicode).                  |
| Timestamp        | Timestamp      | Allows the specification of fractional seconds to a precision of nanoseconds. |


# Using the correct data type for math operations

Using the correct data type for math operations helps ensure expected results from your transformations and jobs. The Number, BigNumber, and Integer types offer specific solutions for different computing needs. The following table highlights the behaviors and possible uses for each data type. For information about the proper method to round or truncate numbers, see [Applying calculations and rounding](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/using-the-fields-table-properties/applying-calculations-and-rounding).

| PDI data type | Description                                                                                                                                                                                                                                                                                             |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Number        | <p>Use for general math with real numbers:</p><ul><li>Decimal precision is not guaranteed.</li><li>Normally precise within 15 to 16 decimal points.</li><li>15.4 may be represented as 15.400000000000000000001111111</li><li>15.498723528092515678989712397 may be 15.498723528092515701252…</li></ul> |
| BigNumber     | <p>Use to get exact results from math of decimal numbers:</p><ul><li>Guarantees precision to about 2 billion decimal places.</li><li>Requires more memory than Integer or Number.</li><li>15.498723528092515678989712397 will always be 15.498723528092515678989712397</li></ul>                        |
| Integer       | <p>Use for math without a fraction or a decimal component:</p><ul><li>Handles minimum and maximum values ranging from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807</li></ul>                                                                                                                 |


# Using the fields table properties

You define properties for the fields to read or write using the fields table. The properties in the fields table determine the field-level processing options for your row data, including the metadata attributes. Some commonly used steps that include a fields table are [Split Fields](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/Split%20Fields=GUID-36055D0C-1602-4F21-BEA7-BEEDF325CAAD=2=en=.md), [Select Values](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/Select%20Values=GUID-14FD2047-C05A-4E28-A0E9-8C8696823EC4=2=en=.md), [Text File Output](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/text-file-output-cp), and [Concat Fields](http://wiki.pentaho.com/display/EAI/Concat+Fields).

When using the fields table the following definitions and processing rules apply.

**Note:** Depending on the transformation step or job entry, some fields tables may feature only a portion of the columns listed below.

![PDI fields table](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-111aff0b329d7b44e6e9f31ed3d8d8f503dfc7b6%2FPDI_format_table_example.png?alt=media)

* **Name**

  The name of the field.
* **Type**

  The type of the field. For example, String, Date, or Number. See [Data type mappings](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/data-type-mappings) for more information.
* **Format**

  Defines the format mask to use when converting the value to, or reading the value from, a string. The **Format** drop-down menu offers suggestions, but you can enter your own mask. **Format** is only used when converting a non-string data type to a string data type. **Format** overrides **Length** and **Precision**. See [Applying formatting](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/using-the-fields-table-properties/applying-formatting) for formatting details.
* **Length**

  Defines the length to use when converting the value to, or reading the value from, a string. The numbers before the decimal point, or a value that is longer than the maximum length, will not be truncated. **Length**, also called Precision in some databases, is a metadata component. PDI converts to the required metadata type when the data is resulted to a string, not during the transformation (or job) or if resulted to non-string data types. See [Output type examples](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/output-type-examples) for a listing of string and non-string types. **Length** is not used when **Format** is specified.
* **Precision**

  Defines the number of digits after the decimal point to use when converting the value to, or reading the value from, a string. The numbers before the decimal point will not be truncated. **Precision**, also called Scale in some databases, is a metadata component. PDI converts to the required metadata type when the data is resulted to a string, not during the transformation (or job) or if resulted to non-string data types. See [Output type examples](https://docs.pentaho.com/pdia-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/output-type-examples) for a listing of string and non-string types. **Precision** is not used when **Format** is specified.
* **Currency**

  Used in conjunction with **Format** to interpret numbers such as `$10,000.00` or `E5.000,00`. If the format mask contains the Unicode currency symbol ¤ (`\u00A4`), then it replaces the symbol by the value in the currency column. In Pentaho, you must use the copy and paste method to apply this symbol. See [Common Formats](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/common-formats) for information on valid number formats.
* **Decimal**

  Represents the character that replaces the period (.) in the format mask. Only applies when converting the value to, or reading the value from, a string.
* **Group**

  Represents the character that replaces the comma (,) in the format mask. Only applies when converting the value to, or reading the value from, a string.
* **Null if**

  Converts the value to null if the input value matches.

  **Note:** This value is case-sensitive.
* **Default**

  Defaults to this value if the value is null.
* **Trim type**

  Defines the type of trimming to perform on the input or the output string. Trimming removes the white space on either side of a string. Options are both, left, right, or none.
* **Repeat**

  Determines how null rows are handled. If the value in this row is null, then the value from the last row where the column was not null is used.


# Applying formatting

Format masks define how data returned for a field is converted to, or from, a string. For example, a field might return the value "`7000`", but you want to display it as "`$7,000.00`". To do this, you apply a format mask to the field. The original data is not truncated when using a format mask.

As shown in the table below, when **Format** is used with **Decimal**, the period (.) in the format mask is replaced with the indicated character. Alternatively, when **Format** is used with **Group**, the comma (,) in the format mask is replaced with the indicated character. See [Common Formats](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/common-formats) for information on valid number formats.

| Input / Output value | **Format** | **Decimal** | **Group** |
| -------------------- | ---------- | ----------- | --------- |
| 10.0                 | #.#        | .           | ,         |
| 1,546.99             | #,###.##   | .           | ,         |
| 1g546d99             | #,###.##   | d           | g         |
| €1.546,99            | €#,###.00  | ,           | .         |
| $1,546.99            | $#,###.00  | .           | ,         |

The following table shows that when \*\*Format\*\*, \*\*Decimal\*\*, \*\*Group\*\*, \*\*Length\*\*, and \*\*Precision\*\* are used together. \*\*Format\*\* always overrides \*\*Length\*\* and \*\*Precision\*\*.

| Input    | **Format** | **Decimal** | **Group** | **Length** | **Precision** | String output | Number output |
| -------- | ---------- | ----------- | --------- | ---------- | ------------- | ------------- | ------------- |
| 10.0     | #.#        | .           | ,         | 5          | 2             | 10.0          | 10.0          |
| 10.0     |            | .           | ,         | 5          | 2             | 010.00        | 10.0          |
| 10.01    |            | .           | ,         | 2          | 1             | 10.0          | 10.01         |
| 1,546.99 | #,###.##   | .           | ,         | 10         | 3             | 1,546.99      | 1546.99       |
| 1,546.99 | 0#,###.000 | .           | ,         |            |               | 01,546.990    | 1546.99       |


# Applying calculations and rounding

Number and date calculations performed in PDI do not apply the **Format**, **Length**, and **Precision** properties. For example, using the table below, A + B + B = `30.1` If you preview B, it will appear as `10.0`, so you would think `10.02 + 10.0 + 10.0` `= 30.02`. However, because B was never converted to a string for the calculation, `10.02 + 10.04 + 10.04` `= 30.1.`

| Field | Input   | **Format** | **Decimal** | **Group** | **Length** | **Precision** |
| ----- | ------- | ---------- | ----------- | --------- | ---------- | ------------- |
| A     | `10.02` | #.0        | .           | ,         | 5          | 1             |
| B     | `10.04` |            | .           | ,         | 5          | 1             |

If you want to truncate a string, use the [Strings cut](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/strings-cut) step.

If you want to round or truncate a number, use the following [Calculator](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/calculator) step features:

* Round function
* Floor and Ceil functions

Alternatively, you can convert the date or number to a string in the [Select Values](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/select-values) step, which applies the formatting specified in the metadata.


# Output type examples

The following table provides examples of the string and non-string output types in PDI. Note that **Format**, **Length**, **Precision**, **Decimal**, and **Group** apply only when reading from, or outputting to, a string.

| String output type example                                             | Non-string output type example                    |
| ---------------------------------------------------------------------- | ------------------------------------------------- |
| Preview                                                                | Table Output when the target field is a number.   |
| Text File Output                                                       | Avro Output when the target field is a number.    |
| JSON Output                                                            | Parquet Output when the target field is a number. |
| XML Output                                                             | ORC Output when the target field is a number.     |
| Table Output when the target field is a varchar.                       | Any binary output type                            |
| Anything displayed by PDI including logs, error messages, and prompts. |                                                   |




---

[Next Page](/llms-full.txt/1)

