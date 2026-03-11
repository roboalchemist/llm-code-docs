# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6163.md

# What's New in Axonius Asset Cloud 6.1.63

#### Release Date: April 20th 2025

These Release Notes contain new features and enhancements added in version 6.1.63.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Chart Enhancements

#### Sort Query Comparison Chart by Query Order

Users can now [sort the Query Comparison Chart](/docs/query-comparison-chart) based on the order in which they arrange the queries. To change the order, users can simply drag the queries to their preferred position in the Chart wizard.

## SaaS Applications New Features and Enhancements

The following new features and enhancements were added to SaaS Applications:

### SaaS Application Discovery Management

The new [SaaS Application Discovery Management](/docs/managing-saas-applications-discovery) page provides users with increased control over SaaS application discovery to better align with their specific environment and organizational requirements. Currently, Axonius identifies SaaS Applications based on its comprehensive SaaS Applications Repository.

This new feature allows users to:

* **Add Application**: Add an application that came from an adapter, but was not matched by SaaS Applications Repository.

* **Edit Matched Applications**: Change the application name Axonius suggests for a discovery indicator.

* **Remove Matched Applications**: Remove an application that was matched by the SaaS Applications Repository.

* **Bulk Edit Matched Applications**: Simultaneously update matched/unmatched applications for multiple indicators.

* **Filter and Search**: Refine the list of indicators with filter and search capabilities.

![SaaSAppDiscovery.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SaaSAppDiscovery.png)

![EditMatch.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EditMatch.png)

## Axonius Platform New Features and Enhancements

### Assets Pages

The following features were added to all assets pages:

### Asset Actions in Asset Profile Page

In addition to the existing functionality on the asset pages, users can now [perform actions on assets](/docs/asset-profile-page#asset-profile-actions) directly from the Asset Profile page.

The following actions are now available from an asset's profile page:

* Tag
* Add Custom Field
* Create Ticket
* Enforce
* Export Comparison Report
* Unlink Device
* Delete

This provides users with a more streamlined workflow for working with individual assets.

![Profile\_ActionButtons.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Profile_ActionButtons.png)

### Cases New Features and Enhancements

**Auto-Update status**
When creating or editing a case, the new **Auto-Update status** option is enabled by default. When enabled, the system automatically updates the case status based on its progress. Disabling this option reverts to the previous behavior where users manually update the case status.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Egress Defend**](/docs/egress-defend)
  * Egress Defend is an email security solution that provides protection against phishing and data breaches. (Fetches: Users)
* [**Thales BSIDCA**](/docs/thales-mfa)
  * Thales BSIDCA is a security solution that provides identity and access management capabilities. (Fetches: Users)

### Adapter Updates

The following adapters were updated:

* [**BitSight Security Ratings**](/docs/bitsight-security-ratings) This adapter now fetches certificates as assets.
* [**Cloudflare DNS**](/docs/cloudflare-dns) - Added the option to fetch Load Balancers and Spectrum Applications. Spectrum Applications are fetched as Devices.
* [**CrowdStrike Kubernetes Protection**](/docs/crowd-strike-kubernetes-protection) - Added the capability to enter an additional FQL query to filter the containers fetch.
* [**Jira Service Management**](/docs/atlassian-jira-service-desk) -  This adapter now fetches business applications as assets.
* [**Microsoft Azure**](/docs/microsoft-azure) - The ManagedIdentity and B2CTenant services are now fetched by this adapter as Accounts/Tenants asset type.
* [**Microsoft Teams**](/docs/microsoft-teams) - This adapter now fetches Teams users as Users and Teams channels as Application Resources. Fetch of Application Resources is only available for customers who have either the Software Management or Identities modules.
* [**Oracle Fusion HCM Cloud**](/docs/oracle-fusion-hcm-cloud) - This adapter now fetches roles as assets.
* [**Red Hat OpenShift Container**](/docs/openshift) - This adapter now fetches containers as assets.
* [**Sonatype**](/docs/sonatype) - This adapter now fetches business applications as assets.
* [**SQL Server**](/docs/sql-server) - Added the option to ignore the hostname parsing if it contains an IP address from the asset's IP address list.
* [**Symantec Endpoint Protection 12.x**](/docs/symantec-endpoint-protection-12x)
  * Added the option to fetch scans information for each device.
  * Added the option to fetch groups for each device.
* [**Tanium Asset**](/docs/tanium-asset) - Added the option to filter out all software with the source “SIU”.
* [**Tenable.io**](/docs/tenableio) - Added the option to populate rich text fields.
* [**Tenable.sc**](/docs/tenablesc-formerly-securitycenter) - Added the option to fetch Plugin 51187 which fetches Bitlocker data.
* **[Workday](/docs/workday#parameters)** - Added an advanced setting to allow users to enable OAuth2 authentication through the use of a Client ID (Username) / Client Secret (Password).

#### Axonius [CSV](/docs/csv),[JSON](/docs/json) and [SQL Server](/docs/sql-server) Adapters Custom Parsing

A new advanced setting enables users to define how to parse specific fields from the raw data fetched using these adapters. This can be set separately for each type of asset fetched by the adapter.
In addition, a new **Parse entity fields dynamically** advanced configuration was added to these adapters, enabled by default. Users can disable this regardless of the new custom parsing capability.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Freshservice - Update Application**](/docs/update-fresh-service-application) - Changes the status of the software in Freshservice to blacklisted, ignored, or managed.
* [**Sharepoint - Delete Users Sites Permissions**](/docs/sharepoint-delete-users-sites-permissions) - Deletes all permissions from all sites accessed by each user.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* **Tenable.sc (SecurityCenter) - Add IP Addresses to Assets** - The name of this Enforcement Action was changed to [**Tenable.sc (SecurityCenter) - Add or Remove IP Addresses to/from Assets**](/docs/add-ips-to-tenablesc-asset). Users can now remove IP addresses from assets and not only add them.
* [**Rapid7 - Add or Remove Tag to/from Assets**](/docs/tag-rapid7-nexpose-insightvm-assets) - Added the option to add and remove tag types.