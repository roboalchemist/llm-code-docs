# Source: https://docs.axonius.com/docs/whats-new-in-axonius-704.md

# What's New in Axonius Asset Cloud 7.0.4

#### Release Date: August 10th 2025

These release notes detail the new features and enhancements in version 7.0.4.

* Read [**What's New in Axonius 7.0**](/docs/whats-new-in-axonius-700) to see all Axonius 7.0 features.

## SaaS Applications New Features and Enhancements

The following new features and enhancements were added to SaaS Applications:

**Updates to 'Generated From' Field**
The 'Generated From' field on the SaaS Applications page has been updated.

## Exposures New Features and Enhancements

The following new features and enhancements were added to Exposures:

### Risk Score Page - Fallback Configuration for Numeric and Non-Numeric Fields

When setting fallback values for fields used in [Risk Score](/docs/risk-score-settings) calculation, users can now set up to 3 fallback values for each condition - two field values and one numeric value. If the primary field is missing, the system sequentially checks the other two fields until it finds a value to use. If none of the fields can be used, a numeric fallback value is assigned.

**Example:** Users can set the Risk Score to check the value of a vulnerability's **CVSS V4 Score** field, and if the field doesn't exist or has no value or doesn't meet the condition, the system will move on to check the value of the **CVSS V3 Score** field; if this field can't be used either, the system will move on to check the value of the **CVSS V2 Score** field; and if this field can't be used either, the system will use a specified fallback value.

## Software Assets   New Features and Enhancements

The following new features and enhancements were added to Software Assets:

### Software Registry

The Software Registry is a dedicated space to manage and enrich your software data, from Approval status (like the previous Software Approval List) to EOL data, license information, and more.

![SoftwareRegistrypage.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SoftwareRegistrypage\(1\).png)

It provides:

* **Enhanced Enrichment Capabilities**:
  * **Simplified Workflow**: Enables enrichment within the Software Registry without requiring users to navigate to other sections like the Enforcement Center.
  * **Streamlined Data Management**: Provides tools and features for users to easily manage, organize, and update their software data within Axonius Software Assets.
    * Each software is expanded by its versions by default.
* **Comprehensive Software Inventory**: A unified view of managed software assets to manage all software settings in one dedicated place, including:
  * Installed and non-installed software (Detection Status)

  * Approval status (per SW and per version)

  * EOL and EOS

  * Tags

  * Software categories

  * Software owner

  * License quantity

  * License start/end date

## Identity Management New Features and Enhancements

The following new features and enhancements were added to Identity Management:

### New Tools Hub Centralizes Access to Identities Tools and Simulators

The new [Tools Hub](/docs/tools-hub) centralizes access to all Axonius Identities tools and simulators. This dedicated space consolidates essential tools, including Role Mining, Entitlement Consolidation, and Rule Simulator.

Tools Hub is designed to help you investigate complex access scenarios, identify birthright access, pinpoint outlier entitlements and excessive access, and gain deep insights into your identity landscape. Leveraging our AI/ML engine for powerful recommendations, the Tools Hub streamlines administrative access and significantly enhances operational efficiency.

### RBAC and Permissions for Rule Management

The out-of-the-box permissions for [rule management](/docs/managing-rules) have been enhanced to provide more granular control over who can manage rules. In addition to the existing ability to view and create draft rules, new options have been added to control and manage the following actions:

* Creation/Editing of rules
* Deletion of rules
* Activation/Deactivation of rules

These enhancements allow administrators to precisely define roles and permissions, aligning rule management capabilities with specific security and operational responsibilities.

### Access Review: New Actions in Teams and Administrator Enhancements

Several enhancements have been introduced to the Access Review module to improve the user experience.

* For approvers, new decision actions are now available directly within Microsoft Teams, and the [External Approval Form](/docs/responding-to-a-campaign#the-external-approval-form) has been redesigned for better visibility.
* For administrators, the user experience has been made more intuitive for [changing approvers or queries](/docs/creating-a-new-campaign). Administrators can now select a specific adapter connection for notifications and will see a new warning that prevents the loss of unsaved entitlement changes.

These updates are designed to create a smoother and more efficient access review process for all users.

## Axonius Platform New Features and Enhancements

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

* **to\_table** function - The **to\_table** function can be used in a Dynamic Value statement to convert a list (array) of structured objects into an HTML table. Its syntax is **to\_table**(list, columns).

### Cases New Features and Enhancements

#### Unified Case Creation

When a new Case is created, a corresponding Case Set is now automatically generated with a default name. This new capability allows users to define and manage scheduling directly from the Case creation screen.

![UnifiedCaseCreation.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/UnifiedCaseCreation.png)

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Salesbuzz**](/docs/salesbuzz)
  * Salesbuzz is a mobile sales force automation platform that provides trip planning, contact management, order processing, inventory control, reporting, and ERP integration. (Fetches: Users, Roles, Permissions)
* [**VulnDB Enrichment**](/docs/vulndb-enrichment)
  * VulnDB is a vulnerability intelligence platform that offers detailed information on software, hardware, and third-party library vulnerabilities to support risk assessment and remediation efforts. (Fetches: Devices)

### Adapter Updates

The following adapters were updated:

* [**Amazon Web Services (AWS)**](/docs/amazon-web-services-aws)
  * This adapter now fetches WAF devices as Firewall / Network Rules.
  * Added the option to exclude accounts with specific OU accounts.

* [**Backstage**](/docs/backstage) - This adapter now fetches users, groups, and business applications (and no longer fetches devices).

* [**BeyondTrust Privilege Management Cloud**](/docs/beyondtrust-pam-cloud) - This adapter now supports API v3.

* [**Check Point Harmony Endpoint**](/docs/checkpoint-harmony-endpoint) - Added the option to fetch vulnerabilities for devices.

* [**Datadog**](/docs/datadog) - Added the option to fetch Containers and Container Images.

* [**DNSFilter**](/docs/dnsfilter) - This adapter now supports 2-Factor Authentication.

* [**Imperva WAF Cloud**](/docs/imperva-waf-cloud) - Added the following advanced settings to fetch NAT and ACCESS rules:
  * Enrich Sites with Data Centers
  * Enrich Sites with Asset Policies
  * Enrich Sites with APIs
  * Fetch Firewall from Policies (fetches Network / Firewall Rules assets)

* [**Jira Service Management (Service Desk)**](/docs/atlassian-jira-service-desk) - This adapter now fetches application services as assets.

* [**LogicMonitor**](/docs/logicmonitor) - Added the option to parse the value for 'Host Name' from the field `systemProperties -> system.azure.resourcename`.

* [**Microsoft Cloud App Security**](/docs/ms-cloud-app-security) - Added the option to configure the Cloud Environment in the connection parameters. The options are Global, China, Azure US Gov Cloud, and Azure US Gov DoD Cloud.

* [**Netdisco**](/docs/netdisco) - Added the option to convert entities by filter. This capability employs the existing ingestion rules schema to create rules for specific devices. For each device matching the rule, the device will be converted to a network device instead of a regular device.

* [**Omnissa Horizon** ](/docs/vmware-horizon) - The name of the **VMware Horizon** adapter was changed to **Omnissa Horizon**.

* [**Tenable Identity Exposure (formerly Tenable.ad)**](/docs/tenable-ad) - This adapter now fetches Devices.

* [**UpGuard CyberRisk**](/docs/upguard-cyberrisk) - Added the option to fetch all vendor domains (including vendor data).

* [**VMWare ESXi and vSphere**](/docs/vmware-esxi) - Added an option to provide a list of regexes to match with hostname and replace them with the asset name.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**BitSight - Create User**](/docs/bitsight-create-user) - Creates a new user in BitSight.
* [**BitSight - Assign Role to User**](/docs/bitsight-assign-role-to-user) -  Assigns a rule to a BitSight user.
* [**BitSight - Assign Group to User**](/docs/bitsight-assign-group-to-user) -  Assigns a group to a BitSight user.
* [**Microsoft Intune - Update Device**](/docs/intune-update-device) - Updates selected attributes in Microsoft Intune devices with new values.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**AWS - Send CSV to S3**](/docs/send-csv-to-amazon-s3) - Added an option to "**Always export aggregated fields as arrays**". When this is enabled, the aggregated fields in sent Parquet files are represented as proper lists instead of CSV-style strings.