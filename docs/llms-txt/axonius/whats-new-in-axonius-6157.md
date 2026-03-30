# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6157.md

# What's New in Axonius 6.1.57

#### Release Date: March 9th 2025

These Release Notes contain new features and enhancements added in version 6.1.57.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Assets Pages

## Devices  Page  New Features and Enhancements

The following new features and enhancements were added to the **Devices** page.

### EOL/EOS and Latest Version Support for FortiOS

[Devices in Axonius](/docs/devices-page#os-end-of-life-end-of-support-and-latest-os-version) now support End of Life, End of Support, Latest Version, and Is Latest Version for FortiOS.

## Asset Graph New Features and Enhancements

The following new features and enhancements were added to the Asset Graph:

### Customize the Labels for Graph Nodes

Users can now [customize the labels of nodes](/docs/customizing-node-labels) in an asset graph. By selecting an adapter and a field, the field value that applies to that node will be used as the label. This is useful, for example, when viewing a graph of devices by owner and using the device owner's name or email address as the label. Another use case is when creating [reports](/docs/reports-page). The labels of the graph could be customized to match the report's contents. Custom label settings can be set as the system default so that all assets of this type will be labeled with the appropriate field value.

<Image align="center" alt="CustomizeAssetGraphLabels.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomizeAssetGraphLabels.png" />

The email addresses are used as labels for the devices:

<Image align="center" alt="CustomizeAssetGraphLabelsExample.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomizeAssetGraphLabelsExample.png" />

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### [Adapters Fetch History](/docs/adapters-fetch-history) Page Enhancements

* The 'Total Assets Fetched' column was added to the default view.

* All the other 'Total  Fetched' columns were removed from the default view, however, they can now be added manually.

* The 'Total Assets' filter was added to the list of filters.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Introducing the New Data Scope

The User Interface for [creating data scopes](/docs/data-scope-management) has been redesigned with a brand new data scope drawer with these important new enhancements:

* **User-friendly User Interface** - An intuitive user interface that is easy to use, navigate, and understand. It includes search options and tabs for defining data scopes in two ways:
  * **Selected assets approach** - In the new Data Scope drawer, administrators have more control over the assets included. The data scope only shows the pre-approved assets. Assets not selected to be included in the data scope will not be part of it.
    ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DataScopeByAssets-2.png)

    * Example use case - A user wants to create a data scope for the Human Resources department dealing only with the **Users** asset type.

  * **Define a data scope by adapters** - A new option to use an adapter as a source for the entire data scope was added. The data scope shows only assets fetched using the selected adapter and includes all asset data that is fetched from all other adapters. Assets not coming from the selected adapter will not be shown.

<Image align="center" alt="Data scope by adapter" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DataScopeByAdapter.png" />

* Example use case - The Human Resources data scope from above can be configured to only show **Users** coming from human resources-related adapters.
* When using adapter connections to restrict access to adapter connections configuration information, when **Select adapter connections** is selected but no *connections* are selected, adapter connections are NOT restricted. This is unlike previous versions where, in this configuration, all adapter connections were restricted.
* The new design allows to manage which cloud accounts are available in the [**Cloud Compliance Center**](/docs/cloud-asset-compliance-page). When cloud accounts are selected, only those accounts appear in the Cloud Compliance Center. When no accounts are selected, all cloud accounts are appear.  Previously, the selected accounts were *excluded* from the data scope.

<Image align="center" alt="Data scope restrictions" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DataScopeRestrictions.png" />

### Improved Experience for Adding Single Select Custom Data Fields

When adding custom fields of Single Select type from the **Custom Data Management** page, users can add multiple potential values as a bulk instead of adding them one-by-one. Users can also copy all values to use them elsewhere.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

It is now possible to [rerun Enforcement Sets](/docs/rerunning-enforcement-sets-from-run-history) directly from the [Run History page](/docs/view-ec-set-history). This is particularly useful for rerunning failed Enforcement Sets, without needing to navigate to the Enforcement Set itself.

## System Settings New Features and Enhancements

#### Configuring User Interface Settings

Added the option to mark new events as Info events rather than Warning events.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Cyera**](/docs/cyera)
  * Cyera is a data security platform that provides comprehensive data protection and governance solutions. (Fetches: Devices, Databases, Object Storage)
* [**Dashlane**](/docs/dashlane)
  * Dashlane is a password management tool that offers secure storage and autofill capabilities for credentials. (Fetches: Users)

### Adapter Updates

The following adapters were updated:

* [**Black Kite V2**](/docs/black-kite-v2)
  * This adapter now fetches users, vulnerabilities, SaaS applications, and domains and URLs as assets.
  * Added the capability to enter a list of company names. The adapter will fetch assets related only to the specified companies.

* [**CIS-CAT Pro**](/docs/cis-cat)
  * This adapter now fetches databases as assets.
  * Added the option to parse devices with database field ("database.name") as Database assets.
  * Added the option to aggregate devices by hostname.

* [**CrowdStrike Falcon**](/docs/crowdstrike-falcon) - Added the option to parse POD devices as containers.

* [**CSCDomainManager**](/docs/cscdomainmanager) - Added the option to use the "qualifiedDomainName" field to fill the Domain field (instead of using the “domain”).

* [**Exabeam Cloud**](/docs/exabeam-cloud) - Added the capability to configure a field to use as the device hostname source.

* [**Microsoft Active Directory (AD)**](/docs/microsoft-active-directory-ad) - Added the option to fetch standalone managed service accounts as Users assets.

* [**Microsoft Cloud App Security**](/docs/ms-cloud-app-security) - Added the option to set the fetch timeframe: 30, 60 or 90 days.

* [**Orca Cloud Visibility Platform**](/docs/orca-cloud-visibility-platform) - Added the capability to enter Orca categories to fetch as Serverless Function assets and not as devices.

* [**Pentera**](/docs/pentera-platform) - Added the capability to specify the number of days since the last scan.

* [**Rapid7 Nexpose and InsightVM**](/docs/rapid7-nexpose) - Added the option to parse users as Users instead of Last Used Users (the default).

* [**SailPoint IdentityNow**](/docs/sailpoint-identity-now)
  * Added the option to enrich the "List Governance Groups" endpoint with the “List Connections for Governance Group“ endpoint.
  * Added the option to enrich the "List Governance Groups" endpoint with the “List Governance Group Members“ endpoint.

* [**SharePoint**](/docs/sharepoint) - The **Fetch Sites as App Resources** was changed to **Fetch Sites as**, where the user can choose which asset type to fetch Sites as:  Devices, App Resources, or Business Applications.

* [**Sophos Central**](/docs/sophos-central) - Added the option to fetch mobile devices.

* [**SteelCloud**](/docs/steel-cloud) - Added an option to download all files from a folder (path) while using **SMB Share** as the File Source. This option is also available on the [CSV](/docs/csv) adapter and the following CSV-style adapters:[Custom Files](/docs/custom-files),[Rockwell FactoryTalk AssetCentre](/docs/rockwell-factorytalk),[Yokogawa CIM](/docs/yokogawa-cim), and [Honeywell Experion](/docs/honeywell-experion).

* [**Tenable.io**](/docs/tenableio) - Added the option to fetch only the latest software versions.

* [**Vulcan Cyber**](/docs/vulcan)
  * Added support for API V2.
  * Added the option to fetch assets and findings from the export endpoints.
  * Added the capability to specify the number of minutes for the adapter to wait for the export process to finish.

* [**watchTowr**](/docs/watchtowr) - This adapter now fetches vulnerabilities and SaaS applications as assets.

* [**Wiz**](/docs/wiz) - Added an option to fetch vulnerabilties with a Low severity only if they have a fix.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Maria DB - Create User**](/docs/maria-db-create-user) - Creates a user in MariaDB.
* [**Maria DB - Delete User**](/docs/maria-db-delete-user) - Deletes a user in MariaDB.
* [**Microsoft AD - Add/Remove Delegate Control Tasks to/from Assets**](/docs/add-remove-delegate-control-tasks) - adds a delegate control task to or removes a delegate control task from assets.

### Updated Enforcement Actions

The following Enforcement Actions were added:

* [**Rapid7 - Add IP Addresses to Site**](/docs/add-ips-to-rapid7-insightvm-site) - Added the option to add a prefix before the hostname.
* [**ServiceNow - Create Assets**](/docs/create-servicenow-computer) - Added the the option to send true/false values in Boolean format.