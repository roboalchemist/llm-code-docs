# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6174.md

# What's New in Axonius Asset Cloud 6.1.74

#### Release Date: July 6th 2025

These Release Notes contain new features and enhancements added in version 6.1.74.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Exposures New Features and Enhancements

The following new features and enhancements were added to Exposures:

### 'Per Vulnerability per Asset' Risk Score Supported for all Asset Types

The **Risk Score** page now enables users to select for all asset types, and not only Devices, whether to calculate the Risk Score *per Asset* or *per Vulnerability per Asset*. When using the *per Vulnerability per Asset* method, the Risk Score is calculated for a specific vulnerability in the context of a specific asset. As part of the calculation, users can use all asset fields in addition to Vulnerabilities and Vulnerability Instances fields.
When calculating a *per Vulnerability per Asset* Risk Score, the result is written into the **Vulnerable Software: Axonius Risk Score** field on the relevant Assets page.

![RiskScoreNew](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-HWIBFV9O.png)

## Axonius Platform New Features and Enhancements

### System Settings New Features and Enhancements

The following updates were made to various System settings:

#### Use SAML Metadata File to Configure SSO Providers

The option has been added to download a metadata file from Axonius to then upload to an SSO provider such as Okta or Microsoft Entra ID. The metadata file includes configuration details making it much easier to [configure SAML integrations](/docs/saml-based-login-settings). When multiple SAML configurations are being used, each configuration has its own metafile for download.

![SAMLMetaDataFileDownload.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAMLMetaDataFileDownload.png)

#### Changes to API Access Methods

The following changes have been made to the method of accessing the Axonius REST API.
These changes were designed to increase platform security.

**For current customers:**

* The API Secret no longer appears on the **Account Settings -> API Key** tab in the user avatar. The API Secret is only displayed once in the message box when resetting the API key, as it is for service accounts.
* Additionally, there is a new option in **Settings -> User and Role Management -> Special Permissions** named **Disable API Key Usage for Users** which, when enabled, will revoke API access for all existing user accounts. Their API Keys and API Secrets will be removed and API access by user accounts will be unavailable. After being enabled and confirmed, this option itself will be disabled. This action is permanent and irreversible.
* Customers who do need API access are required to use the service account option.

**For new customers:**

* API access will only be available using Service Accounts.

## Data Scope New Features and Enhancements

The following new features and enhancements were added to data scopes:

### Hide an Adapter in a Data Scope

You can now hide an adapter and all data fetched from that adapter within a data scope. When an adapter is hidden, all related adapter connections are also hidden. The adapter name, connection labels, and connection IDs are fully hidden. Queries that access a hidden adapter will not run, and data in charts and reports based on these queries is not used. Data from all other adapters is shown as usual. Note that some data may be fetched by other adapters. See [Managing Data Scopes](/docs/data-scope-management).

![HideAdapterConfig.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HideAdapterConfig.png)

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Enhancements to Axonius Actions

* [**Manage Custom Enrichment - Enrich Assets with CSV File**](/docs/add-enrichment) - The Custom Enrichment statement is now automatically validated after you type it. The system checks for correct statement syntax and compatibility between the statement and the uploaded CSV file. It is only possible to save and run the enforcement action once the statement is successfully validated and the CSV file is error-free.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Endor Labs**](/docs/endor-labs)
  * Endor Labs is a platform that provides software supply chain security and management solutions. (Fetches: Vulnerabilities, SaaS Applications, Application Resources)

### Adapter Updates

The following adapters were updated:

* [**CyberArk Privilege Cloud**](/docs/cyberark-privilege-cloud)
  * This adapter now fetches roles and application resources as assets.
  * 'Use Subdomain for tenant URL' was added to connection parameters.
  * Added the option to enrich the Groups endpoint with Safe Membership.
  * Added the option to fetch application resources of the subtype 'safe' from the Safes endpoint.
  * Added the option to add safe members data to Safes.
  * Added the option to fetch application resources of the subtype 'account' from the Accounts endpoint.

* [**Delinea Secret Server**](/docs/thycotic-secret-server) - When fetching Users, includes details on Folder permissions per user, i.e., the folders a user can access, along with their names and IDs.

* [**Forcepoint DLP**](/docs/forcepoint-dlp) - User Name and Password were added to connection parameters.

* [**HPE Switches**](/docs/hpe-switches) - This adapter now fetches Networks (enabled with an advanced setting).

* [**Microsoft Active Directory (AD)**](/docs/microsoft-active-directory-ad) - Added the option to fetch Bitlocker Recovery Password.

* [**Microsoft Azure**](/docs/microsoft-azure) - This adapter now fetches the SqlDBAzureArc and SqlDBAzureArc services as Databases.

* [**Microsoft Defender for Endpoint (Microsoft Defender ATP)**](/docs/microsoft-defender-atp) - Added the option to fetch Vulnerabilities as Vulnerability Instances.

* [**Rapid7 InsightCloudSec**](/docs/divvycloud) - Added the option to categorize assets by asset type.

* [**SailPoint IdentityNow**](/docs/sailpoint-identity-now) - Added the option to populate the Username and Email fields with values from the Attributes section.

* [**Sysdig - Secure**](/docs/sysdig-secure) - Added new endpoints to fetch assets from Workflows and made all the fetch options configurable.

* [**UpGuard CyberRisk**](/docs/upguard-cyberrisk) - Added an option to enable or disable fetching SaaS Applications from the `/vendors` endpoint.

* [**VMware Carbon Black Cloud (Carbon Black CB Defense)**](/docs/carbon-black-cb-defense) - Added the option to filter duplicates based on device's hostname

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Sailpoint Identity Manager - Add/Remove User from Group**](/docs/sailpoint-add-remove-user-from-group) -  Adds or removes users to or from groups in Sailpoint.
* [**Akamai Client List - Append, Delete, and Update entries in a list**](/docs/manage-akamai-client-list-entries) - Appends, deletes, and updates Akamai client list entries.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**phpIPAM - Create or Update Assets**](/docs/create-or-update-php-ipam-asset) - Capability added to select the phpIPAM module used to create/update assets.

* [**ServiceNow - Create Assets**](/docs/create-servicenow-computer) - It is now possible to specify in the new **IRE relation type** field, the relationship between assets that ServiceNow discovers or identifies (such as servers, applications, and databases), specifically for the IRE process. If left empty, ServiceNow uses preconfigured default relationships.