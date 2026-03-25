# Source: https://docs.axonius.com/changelog/release-notes-8018.md

# Axonius Release Notes 8.0.18

#### Release Date: March 8th 2026

These Release Notes contain new features and enhancements added in version 8.0.18.

# Axonius Platform New Features and Enhancements

## Assets Pages

The following features were added to all assets pages:

### Select Specific Relationships for Charts on Asset Profile Dashboards

When building a chart in an Asset Profile dashboard, specific relationships can be selected to further refine the assets represented, improving performance, clarity, and relevance. Relationships are available on all chart types.
For example: Instead of “Devices → Users” with all relationship mappings, users can explicitly select “Device: Owned By → User: Username”
Upon upgrade, existing charts built on “All Relationships” continue to function as before.

<Image align="center" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/asset_profile/QueryCompChartRelationshipSelect.png" />

## Workflows

### &#x20;Workflow Local Variables with Variable Nodes

The capability to use [local variables](https://docs.axonius.com/update/docs/configuring-a-variable-node) in workflows has been added, enabling users to define and use variables scoped to specific blocks, or loops. Local variables allow workflows to process and store data per iteration. They can be referenced in Dynamic Value Statements using `{{var\_name}}` syntax. The system resolves variables from the innermost scope outward, preventing unintended data aggregation across workflow iterations. Local variables support primitive types (string, integer, float, boolean, date) and structured types (array, object) for complex data handling.

## System Settings

The following updates were made to various System settings:

### Importing Internal CIDRs List from API Endpoints

When adding internal CIDRs to Axonius, users can now scale to maintain, add, or delete Internal CIDRs from the system using the following API endpoints:

* **`GET /api/v2/internal_cidrs`** - Retrieve the current list of configured internal CIDRs.
* **`PATCH /api/v2/internal_cidrs`** - Add and/or remove CIDRs in a single request (supports bulk operations).
* **`DELETE /api/v2/internal_cidrs`** - Remove all configured CIDRs at once.

Managing CIDRs via API endpoints allows for bulk operations (uploading 1000+ CIDRs in one import) without manually inserting data into the Axonius User Interface.

## New Adapters

* **[Google Threat Intelligence Vulnerability Intelligence](https://docs.axonius.com/axonius-help-docs/docs/Google-Threat-Intelligence-Vulnerability-Intelligence)** - Google Threat Intelligence Vulnerability Intelligence is a security intelligence service that provides vulnerability data, exploitation context, and threat insights to support risk assessment and remediation workflows.
* **[Raritan CommandCenter Secure Gateway](docs/raritan-commandcenter-secure-gateway-draft)** - Raritan CommandCenter Secure Gateway is a centralized management platform that provides secure access, monitoring, and control of data center infrastructure devices and connected assets. (Fetches: Devices)

## Updated Adapters

* **[Bloodhound](https://docs.axonius.com/axonius-help-docs/docs/bloodhound)** - Added an advanced configuration option to filter only enabled users.

* **[Cisco](https://docs.axonius.com/axonius-help-docs/docs/cisco)** - Added an option to fetch each switch in the switch stack as a separate device.

* **[CrowdStrike Falcon](https://docs.axonius.com/axonius-help-docs/docs/crowdstrike-falcon)**  - Added an option to select which Policy Types to fetch.

* **[Docebo](https://docs.axonius.com/axonius-help-docs/docs/docebo)**
  * This adapter now supports authenticating with username and password.
  * Changed OAuth2 grant type from client credentials to password-based authentication.

* **[Fortinet FortiAnalyzer](https://docs.axonius.com/axonius-help-docs/docs/forti-analyzer)** - This adapter now supports authenticating with FortiCloud Authentication.

* **[Fortinet FortiGate](https://docs.axonius.com/axonius-help-docs/docs/fortinet-fortigate)**
  * Added an "Is Hosted On Cloud" client configuration option in the adapter's connection parameters.
  * New users can no longer use this adapter for FortiManager  and should use the new  [FortiManager](https://docs.axonius.com/axonius-help-docs/docs/forti-manager) adapter.

* **<Anchor label="Lakeside SysTrack" target="_blank" href="doc:systrack">Lakeside SysTrack</Anchor>** - This adapter now supports authenticating with API Key.

* **[Microsoft Azure](https://docs.axonius.com/axonius-help-docs/docs/microsoft-azure)** - The adapter now fetches detailed information about Kubernetes pods running in Azure Kubernetes Service (AKS) clusters. This data is automatically collected during adapter fetch operations and is parsed as Containers.

* **[Microsoft Intune](https://docs.axonius.com/axonius-help-docs/docs/microsoftintune)** - Added an option to select specific extra fields to fetch.

* **<Anchor label="OneTrust" target="_blank" href="doc:one-trust">OneTrust</Anchor>** - Added a custom parsing option for environment-specific custom fields.

* **[Palo Alto Networks Prisma Cloud](https://docs.axonius.com/axonius-help-docs/docs/prisma-cloud)** - Added a new advanced configuration option "Fetch installed software package information" to fetch and parse installed software.

* **[SentinelOne](https://docs.axonius.com/axonius-help-docs/docs/sentinelone)** - Added the option to fetch Application Settings from API v2.1 endpoints.

* **[ServiceNow](https://docs.axonius.com/axonius-help-docs/docs/servicenow)** - Added the ability to use `/` inside the `based_on_field` field when applying `reverse_reference` in a JSON custom schema to support nested list handling.

* **[Snyk](https://docs.axonius.com/axonius-help-docs/docs/snyk)** - The "Enrich organization name" advanced configuration was removed from this adapter

* **[Tenable Nessus](https://docs.axonius.com/axonius-help-docs/docs/tenable-nessus)** - Added an option to classify Attack Surface Discovery assets as Domains & URLs instead of Devices, allowing organizations to better organize and manage their external attack surface.

* **[Tenable Vulnerability Management](https://docs.axonius.com/axonius-help-docs/docs/tenable-security-management)** - This adapter now parses findings from AWS ELBs as Load Balancers instead of Devices, providing better asset classification and visibility for AWS load balancing infrastructure discovered through Tenable scans.

* **[Tenable.sc (SecurityCenter)](https://docs.axonius.com/axonius-help-docs/docs/tenablesc-formerly-securitycenter)** - Added an option to parse SSL certificate information from Tenable Security Center Plugin ID 10863 and create Certificate assets in Axonius.

* **[Wiz](https://docs.axonius.com/axonius-help-docs/docs/wiz)**
  * An asset recategorization was applied to this adapter, and now it parses the following Wiz asset as the following Axonius assets:
    * REGISTERED\_DOMAIN, PRIVATE\_ENDPOINT → URLs
    * SERVICE\_CONFIGURATION → Configuration
    * MESSAGING\_SERVICE → ApplicationServices
    * ENCRYPTION\_KEY → Secret
    * CDN, PRIVATE\_LINK → NetworkServices

## New Enforcement Actions

* [**BeyondTrust Remote Support - Delete Jump Client**](https://docs.axonius.com/update/docs/beyondtrust-remote-support-delete-jump-client) - Deletes an existing Jump Client resource in BeyondTrust Remote Support.
* [**BeyondTrust Remote Support - Update Jump Client**](https://docs.axonius.com/update/docs/beyondtrust-remote-support-update-jump-client) - Updates an existing Jump Client resource in BeyondTrust Remote Support with specified properties.
* [**PANW Cortex XDR - Scan Endpoints**](https://docs.axonius.com/update/docs/paloalto-xdr-scan-endpoints) - Triggers a scan on Palo Alto Networks Cortex XDR endpoints.

## Updated Enforcement Actions

* **[Microsoft Azure - Send JSON to Azure Storage](https://docs.axonius.com/axonius-help-docs/docs/send-json-to-azure-storage)**
  * When selecting Blob containers as the Data Storage type, an option to split the blob storage into multiple small files.

* **[ServiceNow - Manage Assets with Scripted REST API](https://docs.axonius.com/axonius-help-docs/docs/manage-service-now-asset-with-api)**
  * Added the ability to split by field.
  * Added a checkbox to exclude Axonius default mapping.

* **[Tenable Vulnerability Management - Create Assets](https://docs.axonius.com/axonius-help-docs/docs/create-tenableio-asset)**
  * Added an option to wait for the asset creation job to finish before proceeding to the next Enforcement Action in the workflow. This allows the subsequent workflow actions to operate on the newly created asset.