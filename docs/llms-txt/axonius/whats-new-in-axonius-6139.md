# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6139.md

# What's New in Axonius 6.1.39

#### Release Date: November 3rd 2024

These Release Notes contain new features and enhancements added in version 6.1.39.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

## Devices Page  New Features and Enhancements

The following new features and enhancements were added to the **Devices**  page.

### Support for Additional Operating Systems

It is now possible to query by the following additional Operating Systems on the Devices page:

* IBM AIX

* HP HP-UX

* Adva/Adtran

* Juniper

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Data Aggregation Settings

From the **Convert preferred device manufacturer to** option in [Data Aggregation Settings](/docs/configuring-data-aggregation-settings)(**Settings> Data> Data Aggregation**), it is now possible to convert the case of the preferred manufacturer to one of the following: lowercase, uppercase, title.

### Enrichment Settings

It is now possible to enable the new **Get location information only from the smallest subnet of each device** option in [Enrichment Settings](/docs/configuring-enrichment-settings)(**Settings> Enrichment**) to determine the location information based only on the smallest subnet of each device.

### Association Settings

#### Flexible Filtering of 'Last Used Users'

You can now use the 'Last Used Users' setting to [filter the list of Last Used Users](/docs/configuring-enrichment-settings#association) based on values that start with, end with, or contain the entered filter criteria.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Black Kite V2**](/docs/black-kite-v2)
  * Black Kite is a risk management tool that provides cyber risk intelligence and third-party risk assessment solutions. *(Devices)*
* [**exacqVision**](/docs/exacqvision)
  * exacqVision is a video management system for surveillance, offering video recording, monitoring, and playback. *(Devices)*
* [**Forcepoint NGFW**](/docs/forcepoint-one-ngfw)
  * Forcepoint NGFW is a next-generation firewall that provides advanced security features, including intrusion prevention, VPN, and centralized management to protect network environments. *(Devices, Firewall Rules)*
* [**Microsoft Endpoint Configuration Manager (MECM) for Data Warehouse**](/docs/sccm-warehouse)
  * Microsoft Endpoint Configuration Manager (MECM) (formerly SCCM) is a comprehensive management solution for Microsoft Windows operating systems along with some capabilities for Linux, Mac OS, and mobile devices. *(Devices)*
* **[Morpheus](/docs/morpheus)**
  * Morpheus is a unified cloud management platform that provides automation, self-service, and governance for hybrid cloud infrastructure. *(Devices)*
* [**Rockwell FactoryTalk AssetCentre**](/docs/rockwell-factorytalk)
  * Rockwell FactoryTalk AssetCentre is a software solution that offers asset management, backup, and disaster recovery for automation environments. *(Devices)*
* [**VulnCheck**](/docs/vulncheck)
  * VulnCheck is a cybersecurity platform that identifies and assesses vulnerabilities within IT infrastructure for threat management.
* **[Yokogawa CIM](/docs/yokogawa-cim)**
  * Yokogawa CIM (Consolidated Instrumentation Management) is an industrial automation tool that provides centralized monitoring, management, and optimization of instrumentation and control systems. (Devices)

### Adapter Updates

The following adapters were enhanced:

* [**Absolute**](/docs/absolute) - This adapter now works with v3 of the adapter API.
* [**Aruba Central**](/docs/aruba-central) - Due to changes that were made to the vendor’s API, it’s paramount that you change the value in [Advanced Settings → Adapter Configuration](/docs/advanced-settings#wait-for-a-connection-to-the-source-for-up-to-x-seconds)→ 'Wait for a connection to the sources for up to X seconds' to *3000*.
* [**Axonius Users**](/docs/axonius-users) - Added the option to get the user's query history actions for a configured time range.
* **[Censys](/docs/censys)** - Added the option to enrich each device with its full details.
* [**Cisco Umbrella**](/docs/cisco-umbrella) - Added support for API V2.
* **[IBM QRadar](/docs/ibm-qradar)** - Added the option to fetch all assets from the asset model as devices.
* [**ImmuniWeb**](/docs/immuniweb) - Tab Types field was added to connection parameters.
* **Lansweeper Cloud** - Added the option to control the limit in the vulnerability fetch request.
* **[Microsoft Azure](/docs/microsoft-azure)** -  \* Under **Azure services to fetch as assets**, the App Services option was changed to Function Apps.
* **[Microsoft Defender for Endpoint (Microsoft Defender ATP)](/docs/microsoft-defender-atp)** -  \* Added the option to fetch only applicable and non-compliant recommendations.
* **[Microsoft Entra ID (Azure AD) and Microsoft Intune](/docs/microsoft-azure-active-directory-ad)**  - Added capability to enrich users with the Mailbox Usage data
* [**Netskope**](/docs/netskope) -   This adapter now supports fetching devices from API V2
* [**Netwrix Auditor**](/docs/netwrix-auditor) - Added the option to configure the port to use.
* **[Snyk](/docs/snyk)** - Added the option to select whether to fetch projects with their vulnerabilities or not. If you selected group ID on the main configuration screen, it will fetch all devices from all organizations in the group.
* [**Symantec Endpoint Management Suite (Altiris)**](/docs/symantec-endpoint-management-suite-altiris) - added the option to fetch encryptions.
* **Workday** - Added the capability to add custom fields for users.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Dynatrace - Add Custom Tag**](/docs/dynatrace-add-custom-tag) - adds custom tags to selected assets.
* [**Halo Create or Update Device**](/docs/halo-create-update-device) - Creates or updates devices
* [**Halo Create or Update User**](/docs/halo-create-update-user) - Create or updates users
* [**NinjaOne - Run Scripts on Device**](/docs/ninja-rmm-run-scripts) - Runs scripts on selected assets.
* [**ServiceNow - Manage Assets with Scripted REST API**](/docs/manage-service-now-asset-with-api) - Executes a custom REST API endpoint.
* [**VMware CB Cloud - Delete Assets**](/docs/vmware-cb-cloud-delete-assets) - Deletes asset details from VMware CB Cloud.
* [**WMI - Enrich Devices with DNS Records**](/docs/enrich-device-data-with-dns-records) - Enriches assets with DNS records from Windows Management Instrumentation.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

**SharePoint - Send CSV** - When running this action, if the file generated is greater than 240MB, the file will be split into multiple files (with suffix *1,* 2, etc.) to not exceed Microsoft's limit of 250MB.