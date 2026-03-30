# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6172.md

# What's New in Axonius Asset Cloud 6.1.72

#### Release Date: June 23rd 2025

These Release Notes contain new features and enhancements added in version 6.1.72.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Exposures New Features and Enhancements

The following new features and enhancements were added to Exposures:

### Vulnerability Instances Expanded to Additional Asset Types

Axonius now generates Vulnerability Instances from various asset types, including non-device assets - such as Databases, Containers, Compute Images, etc. In the Vulnerability Instances page, a new “Asset Type” field was added, displaying the specific type of asset associated with each vulnerability. Users can filter and sort vulnerabilities by asset type. Clicking on a row from the Vulnerability Instances table leads to the relevant Asset Profile page on which the vulnerability was detected.

![VINewPage](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-6OH1Q1L8.png)

### New Preview Functionality in the Risk Score Page

Users can now test their custom risk score calculations in a dedicated Preview modal. The preview is generated on a randomly selected instance and displays a breakdown of the factors contributing to the calculation, including normalized data. This capability ensures transparency and accuracy, as it allows users to make changes to the calculation parameters before applying them in their environment.

<Image alt="PreviewRiskScore" width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-ZHB2P0DM.png" />

### New Enrichment Source - Qualys Cloud Platform

The Qualys Cloud Platform adapter now enriches CVEs with Qualys Detection Score data.

## Software Assets  New Features and Enhancements

The following new features and enhancements were added to Software Assets:

* In the [Software](/docs/software) page, the **Version Count** field was renamed **Unique Version Count**.

## Identities New Features and Enhancements

The following new features and enhancements were added to Identities:

### Assign Entitlements Manually

Entitlements can now be assigned manually to individual managed identities. This is useful when an assignment needs to be granted ad hoc and on-demand to a specific user and use case. This is useful when using automated actions with Rules, Workflows, or Enforcement Actions is too complex, sensitive, and time-consuming to be used as an alternative.

### Entitlement Consolidation

Entitlement Consolidation analyzes existing entitlements (groups and roles) to identify similarities and redundancies and presents them as a graph in the Role Simulator. Consolidating overlapping entitlements simplifies access management, reduces complexity, and improves overall security posture.
Consolidation reduces the number of entitlements to manage, streamlines access control processes, and minimizes the risk of excessive access by eliminating redundant or unnecessary permissions.

Key capabilities:

* Identify entitlements with overlapping permissions or membership.
* Suggest consolidation opportunities based on identified similarities.
* Streamline the process of merging redundant entitlements.
* Assess the potential impact of consolidation on users, applications, rules, ARM settings, and more.

### Automatic Revocation

When creating rules, you can have Axonius automatically revoke entitlements when identities no longer meet the criteria of the rule. For example, if an employee moves to a different department or leaves the organization, the system will automatically revoke the entitlements that were previously granted based on their former role or team membership. The rule that grants permissions related to the new role or team will grant the employee the new permissions needed for their new position.

### Automatic Revocation Guardrails

Use guardrails to ensure automatic revocation does not remove critical access from system administrators or other roles. Guardrails help to protect organizations from misuse or other issues in the automatic revocation of entitlements. For example, guardrails can prevent revoking permission from all admins or other principal members of the organization.

### AI Generated Names for Suggested Profiles

Axonius AI/ML analyzes the access patterns with Role Mining and overlapping of entitlements with Entitlement Consolidation in your environment and suggests profiles that may help streamline the access management and reduce entitlement complexity. Now, Axonius leverages GenAI to generate useful and descriptive names for the profiles to help users determine what entitlements are included in the profile and which identities it should be serving.

## Axonius Platform New Features and Enhancements

### Chart Updates and Enhancements

The following updates and enhancements have been made to charts:

* The capability was added to the Pivot chart to view stacked bar charts with two dimensions: one dimension defines the y-axis, for example "Last Status Update" grouped by month. The second dimension, for example "Status", determines the stacking within each bar. The x-axis will represent the count of vulnerability instances.
  ![Stacked2DimFull.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Stacked2DimFull.png)

* In the Pivot chart, fields with no value can now be displayed. A custom label can also be configured for empty fields.
  ![ChartNoValue.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChartNoValue.png)

* The ability has been added to set how many segments to display in these charts:
  * Field Segmentation chart
  * Pivot chart
  * Adapter segmentation chart
  The default is 10 segments and the maximum is 20. A label for segments beyond the limit can be configured.

<Image alt="SetMaxSegmentsConfig.png" width="300px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SetMaxSegmentsConfig.png" />

### Cases New Features and Enhancements

When [creating a new case](/docs/creating-a-new-case), it is now possible to set the due date relative to the current date (for example, 'After 2 weeks'), in addition to the existing option of selecting a fixed date.

### System Settings New Features and Enhancements

The following updates were made to various Administrator settings:

#### Enterprise Password Management Settings

The following Enterprise Password Managers were updated:

* [**Delinea Secret Server**](/docs/managing-external-passwords#delinea-secret-server)
  * The new **Use Oauth2** option has been added and is relevant for Delinea Secret Server API V10 only. When enabled, a connection is made using the Delinea Secret Server OAuth 2.0 endpoints instead of authentication with a username and password.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Schneider Electric EcoStruxure Triconex Safety Systems**](/docs/schneider-electric-triconex)
  * Triconex Safety Systems is a suite of safety instrumented systems that provides critical control and shutdown functions for industrial processes using triple modular redundancy technology. (Fetches: Devices)

### Adapter Updates

The following adapters were updated:

* [**CSV - Networks**](/docs/networks-csv) - Added an option to parse entity fields dynamically, which means parsing all the fields in the CSV file and add a custom prefix.
* [**CyberArk Privilege Cloud**](/docs/cyberark-privilege-cloud)
  * Added an option to enrich Users with Safe membership.
  * Added an option to enrich Safes with Safe members.
* [**Delinea Secret Server (Thycotic)**](/docs/thycotic-secret-server) - This adapter now fetches secrets as assets.
* [**Ermetic**](/docs/ermetic)
  * This adapter now fetches vulnerabilities and users.
  * Added the option to fetch AWS users.
  * Added the option to fetch Azure users.
  * Added the option to select device type to fetch: AWS EC2 Instances or Azure Compute Virtual Machines.
* [**ExtraHop Reveal(x) 360**](/docs/extra-hop-360) - Added the option to fetch active devices last seen by the number of days specified.
* [**LogicMonitor**](/docs/logicmonitor) - Added the option to fetch device instances.
* [**ManageEngine Endpoint (Desktop) Central and Patch Manager Plus**](/docs/manageengine-desktop-central) - Two new advanced options have been added:
  * **Device Custom Parsing** - Enables users to define how to parse specific fields from the raw data fetched for device assets.
  * **Enrich Assets Raw Data from query reports** - Scans reports for specific query reports, in order to enrich the asset raw data with data from the first matched query report.
* [**Microsoft Intune**](/docs/microsoftintune) - Added an option to enrich Intune devices with Windows Autopilot Device Identities.
* [**Mosyle**](/docs/mosyle) - Added the option to fetch device groups.
* [**Neustar UltraDNS**](/docs/ultradns) - This adapter now fetches domains and URLs as assets.
* [**Qualys Cloud Platform**](/docs/qualys-cloud-platform)
  * Added an option to store and enrich CVEs with QDS data.
  * Added an option to filter fetched Police Postures by Compliance Status.
* [**Red Canary**](/docs/red-canary) - Add the option to fetch users.
* [**SentinelOne**](/docs/sentinelone) - Added an option to disable Users fetch.
* [**Splunk**](/docs/splunk) - In Splunk Macro fields, if the macro string begins with 'search ', the associated search query is now used exactly as entered. Previously, these inputs were automatically modified into a macro search query. This enhancement enables users to enter Search Processing Language (SPL) queries directly, without needing to add extra logic.
* [**Zafran**](/docs/zafran)
  * Added the option to enrich devices with remediations data.

  * Added the capability to specify the maximum number of minutes to wait for the Remediations export to finish before giving up and continuing to the Devices fetch.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**ServiceNow - Move or Copy Attachment**](/docs/move-or-copy-service-now-attachment) - Moves or copies the attachment from a ServiceNow record to a record in a specified destination table.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Azure DevOps - Create Task**](/docs/create-azure-devops-task) - The **Custom Fields** section was updated so that now, users can also send native Microsoft fields, and not only custom fields. For example: `Microsoft.VSTS.Origin`
* [**Dynatrace Add Tags**](/docs/dynatrace-add-custom-tag) - The ability to delete tags was added.