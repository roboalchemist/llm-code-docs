# Source: https://docs.axonius.com/docs/whats-new-in-axonius-7010.md

# What's New in Axonius Asset Cloud 7.0.10

#### Release Date: September 21st 2025

These Release Notes contain new features and enhancements added in version 7.0.10.

* Read [**What's New in Axonius 7.0**](/docs/whats-new-in-axonius-700) to see all Axonius 7.0 features.

## Axonius Platform New Features and Enhancements

### Assets Pages

The following features were added to all assets pages:

### Expanding Complex Fields Table View by Adapter Connection

The **Tables** section of an Asset Profile Page displays [complex field tables](/docs/asset-profile-page-complex-fields) such as Network Interfaces, Open Ports, Agent Versions, etc. Users can now expand each row in the table. This enables users to see the specific adapter connection from which each value was fetched.

## Enforcements New Features and Enhancements

The following new features and enhancements were added to the Enforcements:

### Enhancements to Axonius Actions

[Manage Custom Enrichment - Enrich Assets with CSV File](/docs/add-enrichment) - When the system automatically validates an enrichment statement, it also validates the uploaded CSV file. If the CSV file fails validation, an error message appears below the statement, identifying the error and its exact location in the file.

### Cases New Features and Enhancements

In the [Case Management table](/docs/case-management-page#managing-cases-in-table-view), users can now switch between two views: **Case Progress by asset** (the default view) and **Case Progress by ticket** (the new view).
The **Case progress by ticket** view calculates progress based on the number of Case assets linked to tickets that have been updated to one of the following statuses: Done, Solved, Resolved, Closed, Canceled, Rejected, or Finished. When a ticket moves to one of these statuses, all assets associated with that ticket are counted as resolved.
For example, if a Case has 10 assets with two tickets, and the first ticket (linked to four assets) is   'In-progress`while the second ticket (linked to six assets) is`Closed', the Case progress by ticket is 60%.

This new view is available after enabling the new [**Show Case progress by tickets status** UI setting](/docs/configuring-user-interface-settings)(*Settings> GUI> UI*).

![ViewProgressTabs.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ViewProgressTabs.png)

### Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

The [Adapter Connections](/docs/adapter-connections) table can now be sorted by the **Connection Label** column.

### System Settings New Features and Enhancements

The following updates were made to various System settings:

### Concurrent User Sessions

It is now possible to set a [maximum number of active user sessions](/docs/managing-timeout#concurrent-session-settings)(**Settings> Privacy and Security> Session**). When this limit is reached, the user's oldest session is automatically terminated.

![ConcurrentSessionSettings.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ConcurrentSessionSettings.png)

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Denodo**](/docs/denodo)
  * Denodo is a data virtualization platform that offers real-time data integration and management. (Fetches: Devices, Users)
* [**Elastic Fleet**](/docs/elastic-fleet)
  * Elastic Fleet is a management component that offers centralized control over Elastic Agents, policies, and integrations for data collection and protection. (Fetches: Devices)
* [**Keeper Enterprise Password Vault**](/docs/keeper-enterprise-password-vault)
  * Keeper Enterprise Password Vault is a security tool that offers password management and protection solutions. (Fetches: Users, Application Resources)
* [**SAP Ariba SCIM**](/docs/sap-ariba-scim)
  * SAP Ariba SCIM is a REST API that provides standardized identity and group master data provisioning for SAP Ariba environments based on the SCIM protocol. (Fetches: Users, Groups)
* [**Workvivo**](/docs/workvivo)
  * Workvivo is an employee experience platform that provides internal communication, engagement analytics, recognition, and API-based integrations. (Fetches: Users, Groups)
* [**ZeroLock**](/docs/zerolock)
  * ZeroLock is a runtime security platform that provides hypervisor protection and virtual patching for Linux-based environments. (Fetches: Devices)

### Adapter Updates

The following adapters were updated:

* [**Arista CloudVision**](/docs/arista-cloudvision) - Added the option to fetch location data.

* [**BeyondTrust Password Safe**](/docs/beyondtrust-password-safe) - 'Additional assets to fetch' and 'Assets to fetch from Managed Systems' replaced 'Fetch User Audits' and 'Fetch Secrets' in Advanced Settings.

* [**Claroty xDome**](/docs/claroty-cloud) - Added the option to parse the OS information for each device.

* [**CrowdStrike Falcon**](/docs/crowdstrike-falcon)
  * When fetching Users, this adapter now also fetches their associated security roles by default.
  * The following API endpoints used by this adapter were deprecated and replaced:
    * `detects/entities/summaries/GET/v1` - deprecated, replaced by: `alerts/aggregates/alerts/v2`
    * `detects/queries/detects/v1` - deprecated, replaced by: `alerts/queries/alerts/v2`
    * **Note:** The change in the API endpoints only affects customers who have the **Get Detections Information for devices** advanced setting enabled.

* [**Hibob**](/docs/hibob)
  * Added the option to fetch employee lifecycle history.
  * Added the option to fetch inactive users.

* [**Jira Service Management (Service Desk) Fetch Tickets**](/docs/jira-fetch-tickets) - Added the option to fetch ticket updates from the ticketing system for tickets that were created by Axonius EC actions.

* [**Keeper Secrets Manager**](/docs/keeper) - The name of the 'Keeper' adapter was changed to **Keeper Secrets Manager**.

* [**ManageEngine Endpoint (Desktop) Central and Patch Manager Plus**](/docs/manageengine-desktop-central) - Added an option to fetch only vulnerabilities that exist in the threats/vulnerabilities endpoint.

* [**Microsoft Intune**](/docs/microsoftintune)
  * Added an option to enrich Intune devices with discovered apps.
  * Added an option to fetch all of Intune's registered applications and save them in Axonius as Software assets. Their Approval Status will be set to Approved.

* [**Salesforce** ](/docs/salesforce) - This adapter now fetches External Client Apps as User Extensions.

* [**ServiceNow**](/docs/servicenow)
  * Added the option to enrich devices with open Vulnerability Instances data.
  * This adapter now supports [custom parsing](/docs/adapter-custom-parsing) for Application Services.

* **Zscaler Web Security** - This adapter now supports OAuth 2.0 authentication.

### New Enforcement Actions

The following new Enforcement Actions were added:

* [**SentinelOne - Enable or Disable Agent**](/docs/sentinelone-enable-disable-agent) - Enables or disables agents in SentinelOne.

### Updated Enforcement Actions

The following new Enforcement Actions were updated:

* [**Jira Service Management - Create Ticket**](/docs/create-jira-service-desk-ticket) and [**Jira Service Management - Create Ticket per Asset**](/docs/create-jira-service-desk-incident-per-entity) - Added the option to fetch ticket updates from the Jira Service Management Fetch Tickets adapter if you don't have a Jira Service Desk license.