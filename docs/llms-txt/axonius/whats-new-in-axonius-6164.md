# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6164.md

# What's New in Axonius Asset Cloud 6.1.64

#### Release Date: April 27th 2025

These Release Notes contain new features and enhancements added in version 6.1.64.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Cyber Assets New Features and Enhancements

The following new features and enhancements were added to Axonius Cyber Assets:

### Devices Page New Features and Enhancements

The following new features and enhancements were added to the **Devices**  page.

* **Enrich Windows with End of Life Information**
  * A new setting was added to [enrich Windows with End of Life information](/docs/configuring-enrichment-settings) even if a specific edition for Windows OS is *not* provided. This setting is relevant for Windows 10 and 11.

* **Support for Linux IGEL OS**
  * Linux IGEL OS is now supported.

## Axonius Platform New Features and Enhancements

### Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Chart Enhancements

#### Enhanced Visibility for Complex Tables in Asset Data Chart Table View

Users can now split rows in the [Asset Data table](/docs/asset-table-chart#create-or-edit-the-asset-data-chart) for multiple values within complex tables (for example, Network Interfaces, Vulnerable Software, Users, Agent Versions, Firewall Rules, etc.), to display an individual row for each value.
This enables a clearer and more structured display of complex tables in Asset Profile Dashboards, facilitating faster and easier asset-level analysis.

### Cases New Features and Enhancements

Case Management view-only users can now open a case drawer to review case information (without the ability to modify the configuration). Previously, only users with edit permissions could access this drawer.

### Adapter Pages and Adapter Interface New Features and Enhancements

### Adapter Interface

#### Enhanced Adapter Ingestion Rule Post Action Operator

It is now possible to use the **remove\_values** operator within a [post action](/docs/setting-adapter-ingestion-rules#performing-post-action-only-if-field-value-exists-not-exists) of an ingestion rule to remove specific values from fields within list objects. This expands on the already existing functionality to remove values from list fields.

### System Settings New Features and Enhancements

The following updates were made to various System settings:

### Save Data Scope Configurations as Data Scope Profiles

Data scope restricted fields can now be managed separately as [data scope profiles](/docs/data-scope-profiles). Select asset types and specific fields to include or exclude. Apply profiles on multiple data scopes easily. When creating a data scope, just select a profile to apply. This is useful to see all restricted fields in a centralized manner, and to apply updates easily and faster.

To use profiles, they must be enabled in Data scope settings and then for each specific data scope.

<Image align="center" alt="Datascopedemoprofile.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Datascopedemoprofile.png" />

When profiles are enabled, the "Data scope profile" section appears in the "New Data Scope" drawer.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DataScopeProfileSelection.png)

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Microsoft Intune**](/docs/microsoftintune)
  * Microsoft Intune is a management tool that offers mobile device and application management capabilities. The new adapter does not remove any capabilities from [Microsoft Entra ID (Azure AD) and Microsoft Intune](/docs/microsoft-azure-active-directory-ad), however, it is recommended to use Microsoft Intune when you need to fetch Intune data separately from Entra.
* [**OneTrust**](/docs/one-trust)
  * OneTrust is a privacy, security, and data governance platform that helps organizations manage compliance, risk, and data privacy. (Fetches: Devices)
* [**PROmanage NT**](/docs/indu-sol)
  * PROmanage NT is a network management and monitoring tool that helps IT teams manage and monitor their network infrastructure, including devices, connectivity, and performance. (Fetches: Devices)
* [**Prometheus**](/docs/prometheus)
  * Prometheus is a monitoring system that offers time-series data collection and alerting. (Fetches: Devices)
* [**Twilio SendGrid**](/docs/twilio-sendgrid)
  * Twilio SendGrid is a cloud-based email marketing tool that assists marketers and developers with campaign management and audience engagement. (Fetches: Users)
* [**XenServer**](/docs/xenserver)
  * XenServer is a virtualization platform that enables the creation and management of virtualized server infrastructures. (Fetches: Devices)

### Adapter Updates

The following adapters were updated:

* [**Amazon Web Services (AWS)**](/docs/amazon-web-services-aws) - Added support for opt-in Regions, which are AWS Regions that require manual selection for activation.

* [**Archer IRM**](/docs/rsa-archer) - The name of the 'RSA Archer' adapter was changed to **Archer IRM**.

* [**AssetPanda**](/docs/assetpanda) - Added the capability to enable custom parsing for devices and users separately.

* [**Atlassian Guard**](/docs/atlassian-access) - The name of the 'Atlassian Access' adapter was changed to **Atlassian Guard**.

* [**CyberArk Privileged Account Security**](/docs/cyberark-privilege-cloud-vault) - This adapter now supports the Layer7 API Gateway for authentication.

* **GitHub** - Added the option to enrich Repositories with a software bill of materials (SBOM).

* [**HPE Aruba Networking ClearPass Policy Manager**](/docs/aruba-clearpass) - The name of the 'Aruba ClearPass' adapter was changed to **HPE Aruba Networking ClearPass Policy Manager**.

* [**Illumio Adaptive Security Platform (ASP)**](/docs/illumio-asp)
  * This adapter now fetches Users, Load Balancers, Containers, Network/Firewall Rules, and Alerts/Incidents as assets.
  * Added the capability to select one or more additional asset types to fetch.

* [**ImmuniWeb**](/docs/immuniweb)
  * The Project ID parameter title was changed to "Discovery ID".
  * Added support for API Version 2.
  * Added the option to select the risk level (for API Version 2 only).

* [**Infoblox DDI**](/docs/infoblox) - Added the option to merge records that have the same MAC address.

* [**IP Fabric**](/docs/ip-fabric) - API Version 7.0 is now supported for this adapter.

* [**Juniper Junos**](/docs/juniper-junos)
  * This adapter now fetches Network/Firewall Rules as assets.
  * Added the option to fetch firewalls.

* [**Microsoft Azure**](/docs/microsoft-azure) - This adapter now fetches the following services as assets:
  * **Services fetched as Containers:** KubernetesAgentPools, ContainerGroup, ContainerApp
  * **Services fetched as Compute Services:** AvailabilitySet, ApacheSparkPool
  * **Services fetched as Application Services:** ApiConnection, LogicApp, ApplicationInsight, FormRecognizer, DataFactory, Workbook, AutomationAccount, AvailabilityTest, CommunicationService, MachineLearningServiceRegistry, SystemTopic, SignalR, MachineLearningServiceWorkspace, AppServicePlan
  * **Services fetched as Networks:** PublicIPAddress
  * **Services fetched as Firewall Rules:** NetworkSecurityRules
  * **Services fetched as Databases:** AnalysisServicesServer, DedicatedSQLPool

* **[Microsoft Entra ID (formerly Azure Active Directory) and Microsoft Intune](/docs/microsoft-azure-active-directory-ad#general1)** - Added the capability to change the number of months for which compliance policies are fetched.

* [**NetApp**](/docs/netapp)
  * Added the option to fetch connected NFS clients.
  * Added the option to create users from CIFS/SMB connected sessions.

* [**Nexthink Query Language (NQL)**](/docs/nexthink-infinity-nql) - Added the capability to enable custom parsing for devices and users separately.

* [**Trend Micro Vision One**](/docs/trendmicro-vision-one) - Added the option to fetch users.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Cloudflare Zero Trust Remove Member**](/docs/cloudflare-zero-trust-remove-member) - Removes account members from the CloudFlare API.
* [**Microsoft Fabric - Send Assets to Lakehouse**](/docs/send-assets-to-lakehouse) - Sends assets from Axonius to OneLake and from OneLake to Lakehouse.
* [**SQL - Update Assets in Table**](/docs/sql-update-asset-in-table) - Updates assets in the MSSQL table supplied.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Box - Send CSV**](/docs/send-csv-to-box) - Added an option to compress the CSV file into a GZIP file and upload the compressed GZIP.
* [**Update Zendesk Tickets**](/docs/update-tickets-zendesk) - Added the capability to add a list of Zendesk tags to ticket assets. These tags overwrite the existing ticket tags.
* [**Freshservice - Create Assets**](https://docs.axonius.com/axonius-help-docs/docs/create-freshservice-asset) - Added fields for querying the API.
* [**Freshservice - Update Assets**](https://docs.axonius.com/axonius-help-docs/docs/update-freshservice-asset) - Added fields for querying the API.