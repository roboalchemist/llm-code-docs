# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6146.md

# What's New in Axonius 6.1.46

#### Release Date: December 22nd 2024

These Release Notes contain new features and enhancements added in version 6.1.46.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Assets Pages

The following features were added to all assets pages:

### Searchable 'Notes' Content on Asset Pages

The Notes content in the Asset Profile page now appears in the new ['Notes' complex field](/docs/asset-profile-page-complex-fields#notes).
Users can add this field to the assets table, use it in the Query Wizard, and search it for the content of the notes, user name, and last updated date.

## SaaS Management New Features and Enhancements

### SaaS Applications/SaaS Applications Repository

#### Enter an Owner for a SaaS Application Directly in the Asset Table

Administrator users can now fill in the value for the [Owner field](/docs/saas-applications#static-fields) directly in the table on the SaaS Applications page, instead of adding it in Custom Data.

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Adapters Fetch History

The following fetch status was added to [Adapters Fetch History](/docs/adapters-fetch-history):

* **Fetch ended with warnings** - The fetch ended successfully with one or more warnings, but no errors.

## Activity Log New Features and Enhancements

The following updates were made to Activity Logs:

### New Activity Log Messages

The following activities are now added to the [Activity Log](/docs/activity-logs-page):

* When a user is required to change their expired password when logging in.

* Permission and name changes to roles are clearly specified. The message includes the old name or role as well as the new one.

* The  **Adapters:**  **'Edit Advanced Settings'** message summary now includes details about configuration changes.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Custom Fields are Supported in Data Scopes

[Custom fields](/docs/managing-custom-fields) are now supported in [Data Scopes](/docs/data-scope-management).

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Check Point Management**](/docs/check-point-management)
  * Check Point Management is a centralized solution for configuring, managing, and monitoring Check Point security policies and devices. (Fetches: Devices, Users, Networks)

### Adapter Updates

The following adapters were enhanced:

* [**Amazon Web Services (AWS)**](/docs/amazon-web-services-aws) - A table detailing all the AWS services fetched by this adapter and the asset types they fetch was added to the documentation.

* [**Aruba ClearPass**](/docs/aruba-clearpass) - Added the option to not fetch endpoint devices.

* [**AttackForge**](/docs/attack-forge) - This adapter now fetches Business Applications.

* [**Auth0**](/docs/auth0) - Added the option to fetch organization members as Axonius users.

* [**Bitdefender GravityZone Business Security**](/docs/bitdefender-gravityzone-business-security)
  * This adapter now fetches software and SaaS applications.
  * Added the option to fetch installed patches.
  * Added the option to fetch missing patches.

* [**CSV**](/docs/csv) - Added the option to set the required date format - MM/DD/YYYY, DD/MM/YYYY, or 'Automatically Identify'.

* [**Forcepoint ONE**](/docs/forcepoint-one) - Added the option to fetch log types as devices.

* [**GLPI**](/docs/glpi) - Added the option to enrich Computers with additional plugin fields.

* **[Microsoft Entra ID (formerly Azure Active Directory) and Microsoft Intune](/docs/microsoft-azure-active-directory-ad#cybersecurity-asset-management)** - Added the option to enrich devices with Windows updates.

* [**Nozomi Vantage**](/docs/nozomi-vantage) - Added the option to select a field to populate Axonius's 'Device Last Seen field'.

* [**OpsRamp**](/docs/opsramp)
  * Added the option to parse tags as fields in addition to parsing them as tags.
  * Added the option to fetch assets only as devices instead of parsing them as different kinds of devices (for example compute services, databases, etc.).

* [**Palo Alto Networks Panorama**](/docs/palo-alto-networks-panorama) - Added the capability to enter a list of zones that are exposed to the Internet.

* [**Rapid7 Insight AppSec**](/docs/rapid7-insight-appsec) - This adapter now fetches Apps as Business Applications instead of Devices.

* [**ThousandEyes**](/docs/thousandeyes) - Added support for API Token.

* [**VirtualMetric**](/docs/virtualmetric) - Added the option to select a field to populate the Host Name field.

* [**VMWare Horizon**](/docs/vmware-horizon) - Added the option to fetch Farms as Compute Service assets.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**LimaCharlie - Tag Sensors**](/docs/limacharlie-tag-sensors) - Tags sensors in LimaCharlie.
* [**Rapid7 - Remove Assets**](/docs/rapid7-remove-assets) - Removes assets from Rapid7 InsightVM.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Update User SAP Concur 4**](/docs/update-sap-concur-4-user) -  Added the option to disable all users (set them as non active).
* [**HTTPS Log Server - Send Log Message**](/docs/send-to-https-log-server) - Added several optional fields to the Action's configuration to enable users to send their assets to a custom destination.