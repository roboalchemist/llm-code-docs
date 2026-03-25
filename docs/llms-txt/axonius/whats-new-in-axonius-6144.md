# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6144.md

# What's New in Axonius 6.1.44

#### Release Date: December 8th 2024

These Release Notes detail new features and enhancements introduced in version 6.1.44.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Chart Enhancements

#### New Cards Visualization Format for Asset Data Chart (Previously Asset Table Chart)

Users can now choose to display the Asset Data Chart in the [new ‘Cards’ format](/docs/asset-table-chart#card-view), in addition to the ‘Table’ format. This format presents a data card for each individual asset, offering a more intuitive view and simplifying the investigation of single assets. This is particularly useful in the Asset Profile’s Dashboard tab or when investigating a limited number of assets in a security incident response dashboard.

![AssetDataCards](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetDataCards.png)

#### Updates to Asset Data Chart

The Asset Table chart now includes the following updates:

* The chart was renamed to 'Asset Data' chart.
* The chart now displays up to 20 assets instead of all assets. Users can drill down from the chart to the specific Asset page to explore more assets.

#### Click-through on Matrix Data Chart to Populate Query Wizard with Relevant Expression

Users can now click on data in the Matrix Data table on dashboards to view the relevant query expression in the Query Wizard.

## Assets Pages

The following features were added to all assets pages:

## Software Management Module New Features and Enhancements

The following new features and enhancements were added to the Software Management Module:

#### Vendor Software ID Field

A new 'Vendor Software ID' field was added to the Software Management Module. It shows the software IDs provided by various vendors.

## SaaS Management New Features and Enhancements

#### Renamed 'Is Admin' field to 'Is Super Admin'

The 'Is Admin'[User field](/docs/users-page#user-fields) has been renamed 'Is Super Admin' to reflect it's updated behavior for user data fetched from certain adapters. The 'Has Administrative Permissions' field continues to display a 'Yes' value for users with any admin permissions in that application.

## Licenses New Features and Enhancements

### Manually Enter an End Date for a License

Users can now manually select a date for the End Date field in the [Licenses](/docs/licenses#license-fields) module, when an end date is not included in the data fetched for a license.

## Query Management New Features and Enhancements

The following new features and enhancements were added to the Queries:

### Asset Scope Queries Marked as "Used In"

Asset Scope queries are now marked as "Used In" when used in a Data Scope. The "Used In" tag appears in the **Used In** column on the [Queries](/docs/managing-queries) page.
![AssetScopeQueryUsedIn.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetScopeQueryUsedIn.png)

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Importing and Exporting Enforcement Actions

Users can now [import and export Enforcement Sets ](/docs/importing-and-exporting-enforcement-sets) and their folder format to and from Axonius. This makes it easy to share Enforcement Sets between data scopes. The file format available for both import and export is JSON.

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

#### Dynamic Value Statement Wizard Enhancements

#### Syntax Helper Enhancements

When the [Syntax Helper ](/docs/using-the-syntax-helper) is used to retrieve the Axonius database name for an Asset Field or Relationship Field, it now encloses the name in \[] (square brackets) so that the user can copy it directly into the Dynamic Value Statement without having to add \[] (square brackets) manually.
![AssetFieldRN](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetFieldRN.png)

The Axonius field name is copied directly into the statement, enclosed in \[] (square brackets).

![StatementRN](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/StatementRN.png)

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**NXLog**](/docs/nxlog)
  * NXLog is a log management tool that provides centralized log collection and analysis capabilities. (Fetches: Devices)
* [**Sonatype**](/docs/sonatype)
  * Sonatype provides software supply chain management with a focus on speed and security in open source development. (Fetches: Users, Vulnerabilities, SaaS Applications)

### Adapter Updates

The following adapters were enhanced:

* [**Abnormal Security**](/docs/abnormal-security)
  * Added the option to fetch users of the subtype recipient from the Recipient Employees endpoint.
  * Added the option fetch incidents of the subtype summary from the Summaries endpoint.
  * Added the option to fetch incidents of the subtype trend from the Trends endpoint.
* [**Cherwell IT Service Management**](/docs/cherwell) - Added the capability to enter a comma-separated list of fields from the raw data that can represent the last seen.
* [**Cloudflare DNS**](/docs/cloudflare-dns) - This adapter now fetches domains and URLs.
* [**CrowdStrike Falcon**](/docs/crowdstrike-falcon) - Added support for users due to the fact that the Threat Graph API User and Threat Graph API Key parameters are being deprecated.
* [**FortiCloud**](/docs/forticloud) - Added the option to fetch firewall assets from v3 endpoints.
* **[Google Workspace](/docs/g-suite-by-google#general1)** - Added the option to select the user events to be fetched for the 'Last Access' field.
* [**Infoblox DDI**](/docs/infoblox) - This adapter now fetches domains and URLs.
* [**Microsoft Azure**](/docs/microsoft-azure) - In the **Azure services to fetch as assets** advanced configuration, the Application Gateway HTTP Listener service is now fetched as a Load Balancer generic asset.
* **[Microsoft Entra ID (Azure AD) and Microsoft Intune](/docs/microsoft-azure-active-directory-ad#general1)**
  * Added the option to fetch only users (if no other advanced setting that fetch assets are enabled).
  * Added the option to specify the number of days to fetch mailbox usage information per user.
* [**Pharos Cloud**](/docs/pharos-cloud) - The name of the 'Pharos Beacon' adapter was changed to **Pharos Cloud**.
* [**Silverfort**](/docs/silverfort)
  * Added the option to enrich users with service accounts.
  * Added the option to enrich users with MFA policies.
* [**Symantec Endpoint Management Suite (Altiris)**](/docs/symantec-endpoint-management-suite-altiris) - Added the capability to enter a list of collection names. If the device is a member of those collections, the collection names will be added to a field called "Collections Memberships" in the device.
* [**Tenable.sc**](/docs/tenablesc-formerly-securitycenter) - Added the option to limit the the adding of open port based on the mitigated state.
* [**Vectra AI**](/docs/vectra-ai) - Added the capability to specify the number of devices fetched per page.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**CyberArk Alero - Create User Invitation**](/docs/cyberark-alero-create-user-invitation) - Creates a user invitation in CyberArk Alero.
* [**CyberArk Alero - Update User Role**](/docs/cyberark-alero-update-user-role) - Updates user roles in CyberArk Alero.
* [**CyberArk Alero - Update User Status**](/docs/cyberark-alero-update-user-status) - Updates the status of users in CyberArk Alero.
* [**Thycotic - Enable User**](/docs/thycotic-enable-user) - Enables users in Delinea Secret Server (formerly Thycotic).

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Axonius - Export Assets to Instance**](/docs/export-assets-to-external-axonius)
  * Added the option to not export preferred fields  to the target Axonius instance.
  * Added the option to upload data from the Vulnerability module to the central core.
  * Added the option to upload data from the Software Management module to the central core.
* [**BMC Helix Remedy - Create Ticket**](/docs/create-remedy-ticket) - The Priority field was removed.