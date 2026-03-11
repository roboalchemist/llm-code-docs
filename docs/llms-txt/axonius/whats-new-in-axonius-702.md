# Source: https://docs.axonius.com/docs/whats-new-in-axonius-702.md

# What's New in Axonius Asset Cloud 7.0.2

#### Release Date: July 27th 2025

These Release Notes contain new features and enhancements added in version 7.0.2.

* Read [**What's New in Axonius 7.0**](/docs/whats-new-in-axonius-700) to see all Axonius 7.0 features.

## SaaS Applications New Features and Enhancements

The following new features and enhancements were added to SaaS Applications:

**Updated Asset Names**

* The names of the following assets were updated:
  * All Application Extensions  to Application Extensions
  * All Application Extension Instances  to  Application Extension Instances

### New License Status Field

A new **License Status** field was added to the SaaS Applications page. Its values can be 'Active', 'Inactive' or 'No Licenses'. When the user selects the value in the 'Active Licenses' or 'Inactive Licenses' columns, they navigate to the licenses page filtered by their selection.

## Axonius Platform New Features and Enhancements

### Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

#### Enhancements to Axonius Actions

The following Enforcement Actions were added:

* [**Axonius - Update case**](/docs/update-case) - Updates existing Cases related to Enforcement Action assets, or directly updates Case assets (if action assets = Cases) with new information, such as Priority, Status, Due Date.

### Cases New Features and Enhancements

#### Case Set Follow-Up Actions Now Run Also on Cases

Case Set follow-up actions can now be configured to run directly on a **Case**. This is in addition to the already existing **Runs on** options of **Asset** and **Ticket**.
This enhancement enables using Case-specific information directly within Enforcement Actions, particularly when using **Dynamic Values**. For example, it is now possible to easily include the **Case ID** within the message of a 'Send email' enforcement action.

### System Settings New Features and Enhancements

The following updates were made to various System settings:

#### Defining Fields in the Basic Query View Based on User Role

Administrators can now define default query fields for each asset type based on user roles. Users with that role will see these fields by default in Basic Query mode. If no role-specific fields are set, the Axonius system defaults apply. Users can override these defaults from the Assets page.

![EditBasicQueryMode](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-GU2RZ18G.png)

#### New System Settings Page - Network

A new **Network** page was added under **System Settings** `>` **Data**. In this page, users can manage their general Network configurations. Currently, they can list all the internal CIDRs in their organization, which affects how Axonius parses the traffic between different nodes - whether it's public to private, private to private, etc.

![NetworkSettings](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-I38VKDVH.png)

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Beeline Professional Edition Connect**](/docs/beeline-connect)
  * Beeline Professional Edition Connect is a workforce management solution that offers vendor management and talent acquisition capabilities. (Fetches: Users)
* [**ProcessUnity**](/docs/process-unity)
  * ProcessUnity is a risk and compliance management platform that provides workflows and automation to assess, monitor and mitigate third-party and enterprise risks. (Fetches: Alerts/Incidents)

### Adapter Updates

The following adapters were updated:

* [**1E**](/docs/1e-tachyon)
  * The name of the '1E Tachyon' adapter was changed to **1E**.
  * Added support for Access Token.
* [**Amazon Web Services (AWS)**](/docs/amazon-web-services-aws) - The [AWS Permissions](/docs/aws-permissions) page was updated to contain JSON versions of each permission group.
* [**Axonius Network Discovery**](/docs/network-scanner) - Added the option to include detailed information in Fetch Event Logs.
* [**Azure Defender for IoT**](/docs/azure-defender-for-iot) - Added a new authentication method in addition to the existing authentication via API Token. Now users can also authenticate using Azure Graph Resource Manager.
* [**Cloudflare DNS**](/docs/cloudflare-dns) - The User Email parameter is now required only if using an API Key (legacy).
* [**Dynatrace**](/docs/dynatrace)
  * This adapter now fetches Load Balancers, Databases, Containers, and Object Storage as assets.
  * Added the capability to select one or more entity types to fetch.
* [**Fortinet FortiNDR Cloud**](/docs/gigamon-threatinsight) - The name of the 'Gigamon ThreatINSIGHT' adapter was changed to **Fortinet FortiNDR Cloud**.
* [**Google Chronicle Security**](/docs/google-chronicle-security)
  * Added the following new connection parameters: Project ID, Project Region, Project Instance
  * Added an option to perform UDM (Unified Data Model) searches. When this is enabled, the user should provide the queries to execute, the time window for fetch, and the fetch size (in records).
* **HP Network Node Manager i (NNMi)** - Added an option to tag devices as network devices according to specific data the adapter parses.
* [**Ivanti Connect Secure**](/docs/pulse-connect-secure) - Added support for API Key.
* [**Ivanti Unified Endpoint Manager (Landesk)**](/docs/ivanti-unified-endpoint-manager) - Added the option to perform Device Custom Parsing.
* [**KnowBe4 PhishER**](/docs/knowb4-phisher) - Added the capability to fetch only incidents seen within the last X days.
* [**Microsoft Endpoint Configuration Manager (MECM) (formerly SCCM)**](/docs/microsoft-sccm) - Added an option to add allowed collections to the fetch.
* [**Oracle Netsuite**](/docs/netsuite)
  * The adapter now yields Expense assets from three different endpoints. You can enable toggles in Advanced Configuration to fetch the desired expense assets.
  * Added an option to filter assets by number of days.
* [**Qualys Cloud Platform**](/docs/qualys-cloud-platform) - Added an option to create local users from last logged users. When this is enabled, local user entries will be generated for users found in the Device’s Last Used Users field.
* [**ServiceNow**](/docs/servicenow) - The **Fetch databases as asset** advanced setting now supports the same filtering mechanism as the **Additional device table names** setting. When this setting is enabled, the adapter will fetch data from all of the additional tables listed, make them into Devices, then proceed with fetching the default hardcoded subset of tables Axonius usually fetches from.
* [**Shodan**](/docs/shodan) - Added the option to enable or disable vulnerability fetch.
* [**Spektra**](/docs/spektra) - Now uses the SPEKTRA Edge API. Additionally, it provides a **Spektra Region** field, enabling configuration for specific customer regions.
* **StackRox** - Added the option to fetch only container deployments with the latest `last_seen` date.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Absolute - Update Custom Device Field**](/docs/absolute-update-custom-device-field) - Updates custom device fields in Absolute assets.
* **Oracle IDCS** - Deactivate/Delete User
* **Oracle IDCS** - Grant/Revoke AppRole to User
* **Oracle IDCS** - Create User
* [Snyk - Add Vulnerability Ignore](/docs/snyk-add-ignore-vuln)*(available only for customers with Exposures)* - Allow users to ignore selected Vulnerability Instances fetched from different adapters.

### Updated Enforcement Actions

The following Enforcement Actions were updated:
**Thycotic - Suspend User** and  **Thycotic - Enable User** were changed to **Delinea Secret Server - Suspend User** and **Delinea Secret Server - Enable User**