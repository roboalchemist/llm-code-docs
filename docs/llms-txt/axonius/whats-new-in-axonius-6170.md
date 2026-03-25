# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6170.md

# What's New in Axonius Asset Cloud 6.1.70

#### Release Date: June 8th 2025

These Release Notes contain new features and enhancements added in version 6.1.70.
This version release also contains the contents of [Version 6.1.69](/docs/whats-new-in-axonius-6169)

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Software Assets New Features and Enhancements

All nested fields will now be included inside the Installed Software complex field in Software, in the same was as they are included in Devices (before this change there was a limited set only). These fields will be available in the Query Wizard and in the Edit Table, even when no value is populated.

## Axonius Platform New Features and Enhancements

### Assets Pages

The following features were added to all assets pages:

### Query Wizard Enhancements

### New Display of Complex Fields in Query Wizard

The display of complex fields in the Query Wizard was changed to a hierarchical display, allowing users to expand each field to see its nested fields. When searching for a nested field within a selected complex field, only the results matching the search will appear in the hierarchy.

![CollapsedDisplay](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-U0KKASU8.png)

### Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Discovery Cycle and System Lifecycle

The following steps were renamed:

* Fetch Devices → Fetch Assets
* Fetch Scanners → Fetch Scanner Assets
* Clean Devices → Clean Assets

This new terminology is also reflected in the Activity Log.

### Activity Log New Features and Enhancements

Log 'Message' field values for the Discovery category now display the word 'Assets' instead of 'Devices' and reflect the terminology changes made.

## Axonius-hosted (SaaS) Deployments New Features and Enhancements

### Use S3 Endpoint URL in Core Node Configuration

The option to use an S3 endpoint URL has been added to the [Amazon S3 Settings](/docs/core-node-and-central-core-node-configuration#amazon-s3-settings) in Core Node configuration.

![DeployS3Buckets-rn](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DeployS3Buckets-rn.png)

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**HashiCorp Vault**](/docs/hashicorpvault)
  * HashiCorp Vault is a tool that provides secure storage and access management for sensitive data and secrets. (Fetches: Users, Application Resources)

* [**Honeywell TDC 3000**](/docs/honeywell-tdc-3000)
  * Honeywell TDC 3000 is a legacy Distributed Control System (DCS) used in industrial automation to manage and monitor complex process operations. It features modular controllers, proprietary networks, and operator stations for real-time control and visualization. (Fetches: Devices)

* [**Palo Alto Networks Prisma Access Insights**](/docs/paloalto-prisma-access-insights)
  * Prisma Access Insights is a monitoring tool that provides visibility into network traffic and security events. (Fetches: Devices, Users, Applications, Alerts/Incidents)

* [**RealVNC**](/docs/real-vnc-gateway-service)
  * RealVNC is a remote access software that provides secure connectivity and control over devices. (Fetches: Users, Groups)

* [**Riverbed AppResponse**](/docs/riverbed-app-response)
  * Riverbed AppResponse is a network performance monitoring tool that offers deep packet inspection and analysis. (Fetches: Devices, Certificates)

* [**STIG Manager**](/docs/stig-manager)
  * STIG Manager is a compliance management tool that offers automated security compliance checks and reporting. (Fetches: Devices)

### Adapter Updates

The following adapters were updated:

* [ **Azure DevOps**](/docs/azure-devops) - Added the option to authenticate using service principals. To use the new type of authentication, users need to provide the following fields: Azure Client ID, Azure Client Secret, Azure Tenant ID, and Cloud Environment.

* [**Claroty xDome**](/docs/claroty-cloud) - This adapter now fetches databases as assets.

* [**CSV**](/docs/csv) and [**Custom Files**](/docs/custom-files) - The option of PGP Decryption was added to connection parameters.

* [**CSV**](/docs/csv),[**Dynamics CMDB Helpdesk**](/docs/helpdesk),[**JSON**](/docs/json),[**SQL Server**](/docs/sql-server), and **ServiceNow** - The Custom Parsing capability in these adapters (under Advanced Settings) now allows to add nested fields of complex fields, for example: “Network Interfaces:Ips“.

* [ **GitHub**](/docs/github) - This adapter now fetches Projects V2 as Application Resources. To enable this, you must check the 'Fetch Projects V2' advanced setting.

* [ **Google Chronicle Security**](/docs/google-chronicle-security)
  * Added the option to define the number of days to fetch from.
  * Added the option to ignore a bad response (such as 400 error) in the Devices fetch and still run through the number of days configured.

* [**Island**](/docs/island) - Added the option to not fetch users.

* **Jamf Pro** - Added the option to fetch the history of policies applied to devices

* [**Microsoft Azure**](/docs/microsoft-azure) - This adapter now fetches IPv4Subnet as Networks.

* [**Okta**](/docs/okta) - This adapter now fetches Resource Sets as Application Resources. To enable this, you must check the 'Fetch roles and permissions' advanced setting.

* [**Oracle Fusion HCM Cloud**](/docs/oracle-fusion-hcm-cloud) - Added the option to parse `PersonNumber` as the Employee ID instead of the Employee Number.

* [**PRTG Network Monitor**](/docs/prtg-network-monitor) - Added the option to fetch Parent Tags data on each device.

* [**ServiceNow**](/docs/servicenow) - Added the option to use the 'ci' raw field as asset name and hostname when they are missing.

* [**SharePoint**](/docs/sharepoint) - Added the option to fetch site groups.

* [**Sophos Central**](/docs/sophos-central) - This adapter now fetches Users and Groups.

* [**Uyuni**](/docs/uyuni) - Added the option to fetch patches according to their status.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Illumio Update Workload**](/docs/illumio-update-workload) - Updates existing workloads.
* [**AWS - Delete Files From S3 Bucket**](/docs/aws-delete-files-from-s3-bucket) - Deletes a file from S3.
* [**Slack - Clear User's session settings**](/docs/clear-slack-session-settings) - Clears Slack sessions for users returned by a query or users selected on the Users page.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Microsoft MECM - Add or Remove Assets to/from Collection (PS-based)**](/docs/add-or-remove-device-in-sccm) - A new optional field was added: **Site Server**, which is the SCCM server hostname.