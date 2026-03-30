# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6156.md

# What's New in Axonius 6.1.56

#### Release Date: March 2nd 2025

These Release Notes contain new features and enhancements added in version 6.1.56.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Chart Enhancements

#### View Historical Data in Pivot Charts and Asset Data Charts

Users can now select the 'Use historical data' option to display data from previous dates when creating [Pivot Charts](/docs/adv-pivot-chart#7-presentation) and [ Asset Data Charts](/docs/asset-table-chart#create-or-edit-the-asset-data-chart).

## Assets Pages

## SaaS Management New Features and Enhancements

### New 'Approval Status' field for SaaS Applications

The ['Approval Status' field](/docs/saas-applications#static-fields) indicates whether a SaaS Application is approved or not.

<Image alt="ApprovalStatus.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ApprovalStatus.png" />

### New Complex SaaS Application Field: Recommendations

The new ['Recommendations' complex field](/docs/saas-applications#static-fields) displays insights about a SaaS application that can help a user resolve potential issues related to that application. The complex field contains the following sub fields:

* **Name** - Category to describe the insight (for example: Unmanaged Extension Users of an unmanaged app).
* **Type** - The type of entity affected by this application issue.
* **Severity** - Indication if the issue represents a high, medium, or low level security threat.
* **Description** - A description of the insight about the application.
* **Quantity** - Number of application entities affected by this issue.
* **Remediation** - Steps to be taken to resolve this issue.

### Tickets Page  New Features and Enhancements

#### New Associated Ticket Devices Complex Field

The **Associated Ticket Devices** complex field displays in a table the devices associated with a selected ticket. Each row shows information about one associated device including: **Host Name**, **Source Application**, **Device IPs**, **Internal Device ID**, and **Adapter Connections**.

![AssociatedTicketDevices.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssociatedTicketDevices.png)

## System Settings New Features and Enhancements

#### New Enterprise Password Manager

Bitwarden Vault was added to the [External Password Managers](/docs/managing-external-passwords) page. Bitwarden is an open-source password management service used to store sensitive information, such as website credentials, in an encrypted vault.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Assetnote**](/docs/asset-note)
  * Assetnote is an attack surface management platform to help continuously map and monitor the external attack surface. (Fetches: Devices)
* [**SumTotal**](/docs/sumtotal)
  * SumTotal is a learning management system that offers tools for employee training, development, and performance management. (Fetches: Users)
* [**Zscaler Private Access (ZPA)**](/docs/zscaler-private-access)
  * Zscaler Private Access (ZPA) is a zero trust network access solution that provides secure remote access to applications. (Fetches: Devices, SaaS Applications)

### Adapter Updates

The following adapters were updated:

* [**Action1**](/docs/action1) - Add the option to enrich devices with installed software and missing patches.
* [**Commvault**](/docs/commvault) - Added the option to not populate the LastSeen field for VMs.
* **[CrowdStrike Falcon](/docs/crowdstrike-falcon#vulnerability-fetch-settings)** - Added the option to to enrich devices with their online state (for example: 'online', 'offline', or 'unknown').
* [**CrowdStrike Falcon Discover**](/docs/crowd-strike-falcon-discover) - Added the option to separate the parsing of browser extensions from other installed software into a new table called "Browser Extensions".
* [**Microsoft Active Directory (AD)**](/docs/microsoft-active-directory-ad) - Added the option to fetch a "Protect from accidental deletion information" field for Users.
* [**Microsoft Defender for Endpoint (Microsoft Defender ATP)**](/docs/microsoft-defender-atp) - Added the option to ignore loopback IPs in the fetch.
* **[Microsoft Entra ID](/docs/microsoft-azure-active-directory-ad#parameters)** -
  * Added the option to authenticate the adapter connection with a certificate to Entra ID.
  * Added the option to define which users are included in the fetch by [specifying groups that they belong to](/docs/microsoft-azure-active-directory-ad#general1).
* [**Nozomi Vantage**](/docs/nozomi-vantage) - Added the option to configure enrichment with Vulnerabilities, Software, and Sites endpoint.
* [**Palo Alto Networks Prisma Cloud**](/docs/prisma-cloud) - Added support for API V2.
* [**Qualys Container Security**](/docs/qualys-container-security) - Added the option to only fetch devices that have been updated in the last specified number of days.
* [**Secureworks Taegis VDR**](/docs/secureworks-taegis-vdr) - Client Key and Client Secret were added to connection parameters.
* [**Sumo Logic**](/docs/sumo-logic) - Added the option to fetch users and their roles.
* [**Web Server Information** ](/docs/web-server-information) - The advanced configuration **Fetch data from SSL scanner** no longer uses Qualys SSL Labs; instead, the logic is implemented in the adapter. In addition, the advanced configuration **Qualys SSL Labs API v4 registered email** was removed.
* [**Wiz**](/docs/wiz) - Added the option to parse compute images as not only Compute Images but also as Devices.
* [**Zoom**](/docs/zoom) - Added the option to fetch the asset type "Zoom SIP phone".
* [**Zscaler Web Security**](/docs/zscaler-web-security)
  * This adapter now fetches firewall rules as assets.

  * Added the option to fetch firewall policies data.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**AWS - Create Snapshot from EBS Volume**](/docs/aws-create-snapshot-for-ebs-volume) - Creates snapshots from the EBS volumes provided in the query or selected from the relevant Assets page.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Microsoft Azure - Send CSV to Azure Storage** ](/docs/send-csv-to-azure-storage) and [**Microsoft Azure - Send JSON to Azure Storage**](/docs/send-json-to-azure-storage) - The following Additional Fields were added to these actions: HTTPS Proxy, Verify SSL, HTTPS Proxy User Name, and HTTPS Proxy Password.