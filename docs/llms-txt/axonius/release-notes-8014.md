# Source: https://docs.axonius.com/changelog/release-notes-8014.md

# Axonius Release Notes 8.0.14

#### Release Date: February 8th 2026

These Release Notes contain new features and enhancements added in version 8.0.14.

## Exposures New Features and Enhancements

## Exposures Assets Renamed

To support future advanced functions in the Exposures product, and to accurately describe threats that are not reflected in CVEs or plugins but are produced by Axonius or by users, our key Exposures asset types were renamed. The new names are reflected from now on across the entire Axonius system as well as in the documentation.\
The new names and their effect on different customers are as follows:

* **Vulnerability Instances** are now called **Security Findings**
* **Vulnerabilities** are now called **Aggregated Security Findings**
* The **Vulnerable Software** table on the **Devices** page is now called **Security Findings**
* The **Vulnerability Instances** table on the **Devices** now called   **Security Finding Instances**

The new asset names resonate with security audiences at all levels, and support handling solutions of security findings of different natures across different assets.

The following new features and enhancements were added to Exposures:

### Exception Management Enhancements

The following capabilities were added to the Exception Management module:

* Users can now duplicate an Exception and edit the settings of the duplicated instance according to their needs. This makes creating new Exceptions with similar or identical settings (for example, in the case of an expired Exception renewal) easier and quicker.

* Email notifications for Exception requests are enabled by default (configurable by admin) for easy management and tracking of Exceptions. When enabled, whenever a user makes an Exception request:

* An Email notification is automatically sent to the first assigned approver, plus a reminder if the approver did not take action after 48 hours.

* Identical Email notifications are sent to every approver assigned to this request when it's their turn to review.

* Requesters receive Email notifications for every decision made on their request throughout the process, including when their request was approved or denied, when the Exception approaches its expiration date, and when it expires.

# Axonius Platform New Features and Enhancements

## Workflows

**New Location for Save, Workflow Activation, and Changing Workflow Name**

The Save buttons, access to workflow activation, and changing the name of a workflow have been moved to the top of the workflow. This makes it easier to work with workflows and know workflow status. More information about why you cannot save a workflow is available.

**Capability to Configure a Workflow to Fail if a Node Fails**

Users can now configure a workflow node to fail the complete workflow if the node fails. Configure this using Action settings for the node. This is also reflected in Workflow run statuses.

## Cases

**Case Sets**\
Update tickets CSV Attachment - When a case set is updated, the CSV file attachment in the ticketing provider  (Jira etc), containing the original list of affected assets is automatically updated.

***

<br />

## New Adapters

* **Anvilogic**

  * Anvilogic is a security operations platform that provides detection-as-code and AI-driven triage across SIEMs and data lakes. (Assets Fetched: Incidents)

* **Cisco Secure Cloud Analytics**

  * Cisco Secure Cloud Analytics provides network visibility and threat detection for cloud and on-premises environments. (Assets Fetched:Devices)

* **[Darwinbox](https://docs.axonius.com/axonius-help-docs/docs/Darwinbox)**

  * Darwinbox is a human capital management platform that provides end-to-end HR technology solutions for managing the entire employee lifecycle from recruitment to retirement. (Assets Fetched: Users)

* **FortiRecon**

  * FortiRecon is a digital risk protection service (DRPS) that provides threat intelligence and attack surface management. (Assets Fetched: URLs, Network Services, Network Routes)

**[Rapid7 Bulk Export](https://docs.axonius.com/axonius-help-docs/docs/Rapid7-Bulk-Export)**

* Rapid7 Bulk Export provides visibility and risk prioritization for vulnerabilities found in local, remote, cloud, containerized, and virtual infrastructure.(Assets Fetched: Devices, Aggregated Security Findings, SaaS Applications)

* **[SD Elements](https://docs.axonius.com/axonius-help-docs/docs/SD-Elements)**

  * SD Elements is a threat modeling and security requirements management platform that automates the identification of security controls and compliance requirements throughout the software development lifecycle. (Assets Fetched: Application Resources, Organizational Units, Tickets)

* **[Titan](https://docs.axonius.com/axonius-help-docs/docs/Titan)**

  * Titan is a security platform that offers comprehensive protection and management for digital assets. (Assets Fetched: Users)

## Adapter Enhancements

* **[Axonius Network Discovery](https://docs.axonius.com/axonius-help-docs/docs/network-scanner)** - This adapter now excludes port 9100 - printer port from network scans by default.

* **[Beeline Professional Edition Connect](https://docs.axonius.com/axonius-help-docs/docs/Beeline-Connect)** - Added the option to fetch workers.

* **[Check Point Infinity](https://docs.axonius.com/axonius-help-docs/docs/checkpoint-infinity)** -  Added an option to fetch Threat Protection data.

* **[Cisco AppDynamics](https://docs.axonius.com/axonius-help-docs/docs/App-Dynamics)** - Added an option to fetch Machine Agent data.

* **[CrowdStrike Falcon](https://docs.axonius.com/axonius-help-docs/docs/crowdstrike-falcon)** - Added an option to add device types to enrich with vulnerability data, so you can parse vulnerabilities from external devices.

* **[Databricks](https://docs.axonius.com/axonius-help-docs/docs/Databricks)**
  * Added support for account-level API to fetch  data across all workspaces using Databricks Account API.

* **[Jira Service Management (Service Desk) Fetch Tickets](https://docs.axonius.com/axonius-help-docs/docs/jira-fetch-tickets)** - This adapter now supports [Custom Parsing](https://docs.axonius.com/axonius-help-docs/docs/adapter-custom-parsing).

* **[Oracle NetSuite](https://docs.axonius.com/axonius-help-docs/docs/Netsuite)**
  * Added endpoints for permissions and roles.
  * Added the option to fetch employee permissions and roles data.

* **[Qualys Cloud Platform](https://docs.axonius.com/axonius-help-docs/docs/qualys-cloud-platform)** -  Due to the deprecation of API v2.0 by Qualys (End-of-Life by Jun 2026), some API endpoints from which the adapter fetches data were migrated to newer API versions.

* **[Rapid7 Nexpose and InsightVM](https://docs.axonius.com/axonius-help-docs/docs/rapid7-nexpose)** - Added the option to not parse agent version from services. Enabling this will have the adapter keep only the agent version from the installed software.

* **[Red Hat Satellite](https://docs.axonius.com/axonius-help-docs/docs/red-hat-satellite)** - Added an  option to parse the docker IPs into a specific field rather than the regular NICs.

* **[Salesforce](https://docs.axonius.com/axonius-help-docs/docs/salesforce)** - Application Settings fetched from Salesforce were refined in order to present the most relevant settings. As a result, some users might see less Application Settings in their fetched data

* **[Shadowserver](https://docs.axonius.com/axonius-help-docs/docs/Shadowserver)** - New connection configuration was added 'Download Base URL'.

* **[SQL Server](https://docs.axonius.com/axonius-help-docs/docs/sql-server)** -  Added the option to set the time zone of date/time field values fetched with this adapter. Default is UTC.

* **[Snowflake Data Warehouse](https://docs.axonius.com/axonius-help-docs/docs/snowflake)** - Added configurable timeout for async operations.

* **[Symantec Endpoint Protection 14.x](https://docs.axonius.com/axonius-help-docs/docs/symantec-endpoint-protection)** - Added a default User Name Domain.

* **[Tenable Identity Exposure](https://docs.axonius.com/axonius-help-docs/docs/tenable-ad)** -  Added new endpoints for enhanced parsing for both Users and Devices. The new endpoints allow you to enrich those assets with security checks with recommendations and vulnerability details, AD misconfigurations with adObjectId, reasonId, and attributes, and more.

* **[Trend Micro Vision One](https://docs.axonius.com/axonius-help-docs/docs/Trendmicro-Vision-One)**
  * Added the option to enrich devices with scheduled tasks data.
  * Added the option to enrich devices with recently loaded modules.
  <br />

***

## New Enforcement Actions

The following Enforcement Actions were added:

* **Docebo - Create User**:  Creates new user accounts with username, password, and optional fields
* **Docebo - Update User**:  Updates existing user account information
* **Docebo - Assign User to Group**:  Assigns users to groups/audiences
* **Docebo - Suspend User**:  Suspends or unsuspends user accounts