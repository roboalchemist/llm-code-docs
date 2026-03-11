# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6141.md

# What's New in Axonius 6.1.41

#### Release Date: November 17th 2024

These Release Notes contain new features and enhancements added in version 6.1.41.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Chart Enhancements

#### Updated Chart Type Icons

The new Chart Type icons in the Chart Wizard's Visualization area contribute to a better experience in creating charts for your dashboards.

![TypeIcons](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TypeIcons.png)

## Assets Pages

The following features were added to all assets pages:

### Adapter Connection Column

It is now possible to set the Adapter Connection column as the first (left hand) column on the **Asset Profile** page. Use the [**UI**](/docs/configuring-user-interface-settings) setting under **GUI** on System Settings.

### Query Wizard Enhancements

The Query Wizard was enhanced to show WHERE and WHERE NOT in a clearer way.

![QueryWizardRN](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QueryWizardRN.png)

## Users Page New Features and Enhancements

The following new features and enhancements were added to the  **Users** page.

### 'Is Admin' Field Changes

For the following adapters, the 'Is Admin' field now only displays a 'Yes' value for users with the highest possible admin permissions for the application  fetched by the adapter:

* Tenable IO
* Salesforce
* CrowdStrike Falcon Identity Protection
* MongoDB Atlas Administration
* Atlassian (formerly Atlassian Jira Software)

The 'Has Administrative Permissions' field continues to display a 'Yes' value for users with any admin permissions in an application.

### Normalization Reasons Added for Users

The Users table now supports the [Normalization Reasons complex table](/docs/en/asset-profile-page-complex-fields#normalization-reasons).

## General Updates

### Performance Improvements

As part of ongoing efforts Axonius has made a range of improvements in our infrastructure that lead to multiple performance improvements across the board, in this version.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Enhancements to Axonius Actions

**Axonius - Send Email to Assets**

[Axonius - Send Email to Assets](/docs/send-email-to-entities) - Added the option to only add the custom message content to the email.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Pinpoint**](/docs/pinpoint)
  * PinPoint is an applicant tracking software that offers recruitment management, applicant tracking, and talent acquisition functionalities. (Fetches: Users)
* [**Sprinklr**](/docs/sprinklr)
  * Sprinklr is a customer experience management platform that offers social media monitoring, engagement, and marketing solutions for enterprises. (Fetches: Users, Activities)
* [**VirtualMetric**](/docs/virtualmetric)
  * VirtualMetric is a monitoring solution that offers real-time insights into IT infrastructure performance. (Fetches: Devices)

### Adapter Updates

The following adapters were enhanced:

* [**Akamai CDN Cloud**](/docs/akamai-cdn-cloud) - This adapter now fetches devices.
* [**CrowdStrike Falcon**](/docs/crowdstrike-falcon)
  * Added the option to fetch external DNS domain devices.
  * Added the option to fetch external IP devices.
* **[Google Workspace](/docs/g-suite-by-google#saas-management1)** - Added the capability to fetch extensions based on how recently the extensions were accessed.
* [**IBM MaaS360 with Watson**](/docs/ibm-maas360-with-watson) - Added the option to fetch location data.
* [**IBM QRadar**](/docs/ibm-qradar)
  * Added the option to fetch networks.
  * Added the option to parse network interface related fields.
* [**JFrog Xray**](/docs/jfrog-xray) - Added the capability to filter severities of vulnerabilities fetched.
* **[Microsoft Defender External Attack Surface Management (Defender EASM)](/docs/microsoft-defender-external-attack-surface-management#advanced-settings)** - Added the option to fetch additional asset types: Hosts, Domains and URLs, SSL Certificates and IP Addresses.
* **[Microsoft Endpoint Configuration Manager (MECM)](/docs/microsoft-sccm)** - Added the option to use the "Resource\_Domain\_OR\_Workgr0" field as the device domain, instead of the default option of the "Full\_Domain\_Name0" field.
* **[Microsoft Entra ID (formerly Azure Active Directory) and Microsoft Intune](/docs/microsoft-azure-active-directory-ad#cybersecurity-asset-management)** - The 'Fetch mailbox setting for users' advanced setting now allows users to enter an array of mailbox settings that they want to fetch.
* [**New Relic**](/docs/newrelic) - This adapter now fetches Serverless Functions.
* [**Qualys Cloud Platform**](/docs/qualys-cloud-platform) - Added the option to fetch authentication and compliance reports, and also the option to set a number of retries when fetching devices with a Module Unsupported error.
* [**Pulseway**](/docs/pulseway) - This adapter now supports API v3.
* [**Tenable.sc**](/docs/tenablesc-formerly-securitycenter) - Added the option to set the default page size the adapter will use when making requests.
* [**Tenable.io**](/docs/tenableio) - Added the option to fetch OS serial information to be able to parse the Device Manufacturer Serial.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Datadog - Update Network Device Tags**](/docs/update-datadog-device-tags) - Updates tags for a Datadog network device
* **[Microsoft Defender for Endpoint - Enrich Assets with Client Analyzer Results](/docs/defender-atp-enrichment)** - This action connects to the target device using WinRM/WSMAN connection, and downloads the HTM(L) file using PowerShell. Then, it parses the HTM(L) file and uses it to enrich the device with the extracted data.
* [**Okta - Remove User from Group**](/docs/remove-user-from-groups)
* [**Recorded Future - Add or Remove Assets To/From Watchlist**](/docs/add-or-remove-assets-from-watchlist) - Adds assets to or removes them from a watchlist in Recorded Future.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Okta - Assign Role to Users**](/docs/assign-okta-role-to-user) - Roles can now be selected from a list.
* [**Okta - Assign Group to User**](/docs/assign-okta-group-to-user) - Groups can now be selected from a list.
* [**Okta - Assign Permission to Roles**](/docs/assign-okta-permission-to-role) - Roles can now be selected from a list.
* [**Okta - Assign Role to Groups**](/docs/assign-okta-role-to-group) - The Role can now be selected from a list.
* [**Web Server Information - Enrich Asset Data**](/docs/enrich-device-data-with-web-server-information) - Now fetches certificates as well as devices.