# Source: https://docs.axonius.com/docs/whats-new-in-axonius-703.md

# What's New in Axonius Asset Cloud 7.0.3

#### Release Date: August 3rd 2025

These Release Notes contain new features and enhancements added in version 7.0.3.

* Read [**What's New in Axonius 7.0**](/docs/whats-new-in-axonius-700) to see all Axonius 7.0 features.

## SaaS Applications New Features and Enhancements

The following new features and enhancements were added to SaaS Applications:

**Dynamic Affiliated Users Field**
Users can now create dynamic fields to create a [filtered Affiliated Users field](/docs/configuring-enrichment-settings#filtered-affiliated-users-settings). From the **Enrichment** page under System Settings, it is possible to create a field in the system that will further filter the results of the Affiliated Users without having to create a new query using the Query Wizard. This field can be used in other modules in Axonius.

<Image alt="FilteredAfiliatedUsers.png" width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FilteredAfiliatedUsers.png" />

**SaaS Applications**
On the **SaaS Applications** page, the 'Source Application' field now populates with the name of the adapter from which the SaaS application's installation was identified. For instance, if CrowdStrike identifies a SaaS application installed on a device, 'CrowdStrike' appears as the Source Application.

## Identities New Features and Enhancements

The following new features and enhancements were added to Identities:

### Exporting Role Mining Profile Data to CSV

The ability has been added to export the data of a role mining profile to CSV. The exported data depends on the selected Identity filters, search terms, entitlement match selections, and the entitlement. This is useful to analyze suggested profiles and what identities they would include.

## Axonius Platform New Features and Enhancements

### Chart Enhancements

The following chart enhancements were added:

#### Export Pivot Chart Data to CSV

The capability has been added to export the data behind a pivot chart to CSV for further analysis outside the platform. This capability is available for the following chart types:

* Bar charts
* Stacked bar charts
* Pie charts (includes percentages)
* Line charts (latest data and data over time)
* Summary charts
* Table charts
* Map charts

<Image alt="PivotExportToCSV.png" width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PivotExportToCSV.png" />

### Assets Pages

The following features were added to all assets pages:

#### Asset Investigation

Axonius [Asset Investigation](/docs/advanced-asset-investigation) now reflects changes in asset values fetched by adapters that support differential fetch (every 15 minutes). This now triggers 'Asset value changed' and 'Asset value not changed' Workflow events every 15 minutes whenever they are received.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**CSV - Software Inventory**](/docs/software-inventory-csv)
  * CSV - Software Inventory imports software inventory information from a CSV file. (Fetches: Software, SaaS Applications)
* [**Entuity**](/docs/entuity)
  * Entuity is a network management tool that offers comprehensive monitoring and analysis capabilities. (Fetches: Devices)

### Adapter Updates

The following adapters were updated:

* [**Axonius Network Discovery**](/docs/network-scanner) - Added an option to set timeout for a single scan.
* [**Citrix Application Delivery Management (ADM)**](/docs/citrix-adm-nitro) - Added support for Token Authentication.
* [**GitLab**](/docs/gitlab) - Added the option to exclude Public Groups and all resources within them.
* [**Jamf Pro**](/docs/jamf-pro) - Added support for the ComputerAdvancedSearch endpoint that fetches Devices.
* [**Juniper Junos Space**](/docs/juniper-junos-space-network-management-platform) - Added the option to fetch addresses and NAT rules.
* [**Microsoft Active Directory (AD)**](/docs/microsoft-active-directory-ad) - Added the option to fetch Contacts as Active Directory Users.
* [**Microsoft Entra ID (formerly Azure Active Directory) and Microsoft Intune**](/docs/azure-ad-user-added-to-group) - Added an option to fetch UCClient from Log Analytics to retrieve information about Intune patches.
* [**NAVEX**](/docs/navex) - This adapter now fetches users and groups as assets.
* **Okta** - this adapter now supports Demonstrating Proof-of-Possession (DPoP) header token for OAuth 2.0 client apps.
* [**Oracle Netsuite**](/docs/netsuite) - When the option to fetch Vendor Bill Details is enabled, it is now possible to specify the look-back period for fetching transactions. Only vendor bills published within this many days of the current date will be retrieved.
* [**Proxmox Virtual Environment (VE)**](/docs/proxmox-virtual-environment-ve) - Added the capability to enter a comma-separated list of tag keys to be parsed as device fields.
* [**Qualys Cloud Platform**](/docs/qualys-cloud-platform) - Added an option to **not** force FQDN as the host name for Mac OS devices.
* [**Rapid7 InsightVM**](/docs/rapid7-insightvm) - Added the option to determine whether to fetch vulnerabilities or not.
* [**runZero**](/docs/rumble-network-discovery) - This adapter now fetches the following asset types (in addition to Devices): Vulnerabilities, SaaS Applications, Domains & URLs, Certificates.
* [**SentinelOne**](/docs/sentinelone) - Added the option to fetch last reboot date of SentinelOne devices.
* [**ServiceNow**](/docs/servicenow) -
  * Added an option to connect the adapter using OAuth Custom Endpoint Path and to enable sending OAuth requests as JSON.
  * Added the advanced configuration **Assets tables to fetch** option to control which main asset tables to fetch.
  * Added an option to use the "asset" raw field of a device as the device's Asset Name.
* [**SOTI MobiControl**](/docs/soti-mobicontrol) - This adapter now fetches users as assets.
* [**Tenable Vulnerability Management**](/docs/tenableio) - Added the option to fetch installed software from plugin 196906.
* [**Workday**](/docs/workday) - Added the option to fetch integration system users as application keys.

### Extension Assets Fetch Update

The following adapters have been updated to retrieve extension-related asset types:

* [GitHub](/docs/github)
* [Netskope](/docs/netskope)
* [JumpCloud](/docs/jumpcloud)
* [Microsoft Entra ID (formerly Azure Active Directory) and Microsoft Intune](/docs/azure-ad-user-added-to-group)
* [Salesforce](/docs/salesforce)
* [OneLogin](/docs/onelogin)
* [Monday](/docs/monday)
* [SailPoint IdentityNow](/docs/sailpoint-identity-now)
* [PingFederate](/docs/pingfederate)
* [Google Workspace (G Suite)](/docs/g-suite-by-google)
* [Active Directory Federation Service (AD FS)](/docs/adfs)
* [Okta](/docs/okta)

**Additional Asset Types Fetched:**

* Admin Managed Extensions

* Application Addons

* User Initiated Extensions

* Admin Managed Extension Instances

* Application Addon Instances

* Application Keys

* User Initiated Extension Instances

### New Enforcement Actions

The following Enforcement Actions were added:

* [**BeyondTrust Password Safe - Manage Assets**](/docs/beyondtrust-password-safe-manage-assets) - Creates and deletes assets in BeyondTrust Password Safe.
* [**Jamf Pro - Update Device**](/docs/update-jamf-device) - Updates the name of a device in Jamf Pro.
* [**Microsoft Entra ID (formerly Azure AD) - Update Entra ID Device**](/docs/azure-ad-update-device) - Modifies Extension Attributes in Entra ID Devices.
* [ **Tenable Vulnerability Management - Unlink Tenable Agents**](/docs/unlink-tenable-agents) - Unlinks decommissioned Tenable Vulnerability Management agents.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Jira Service Management (Service Desk) - Create Ticket**](/docs/create-jira-service-desk-ticket) and [**Jira Service Management (Service Desk) - Create Ticket per Asset**](/docs/create-jira-service-desk-incident-per-entity) - **User Name** is optional when not using the Cloud API.