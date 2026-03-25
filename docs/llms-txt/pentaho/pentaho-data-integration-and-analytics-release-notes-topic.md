# Source: https://docs.pentaho.com/whats-new/pdia-9.3-whats-new/pentaho-data-integration-and-analytics-release-notes-topic.md

# Source: https://docs.pentaho.com/whats-new/10.2-whats-new/pentaho-data-integration-and-analytics-release-notes-topic.md

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
