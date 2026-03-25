# Source: https://docs.axonius.com/docs/whats-new-in-axonius-701.md

# What's New in Axonius Asset Cloud 7.0.1

#### Release Date: July 20th 2025

These Release Notes contain new features and enhancements added in version 7.0.1.

* Read [**What's New in Axonius 7.0**](/docs/whats-new-in-axonius-700) to see all Axonius 7.0 features.

## Exposures New Features and Enhancements

The following new features and enhancements were added to Exposures:

### Vulnerability Instances Page Enhanced with Multi-Asset Counts and Full Contextual Navigation

The Vulnerability Instances page now displays a full breakdown of all asset types affected by a VI query - not only Devices. 'Unique Devices Count' was renamed to 'Unique Assets Count', and it represents the sum of all unique assets (Devices, Compute Images, Databases, Containers, etc.) detected in the current VI query. Hovering over this displays a breakdown of all the asset counts by their specific type, and each row in the breakdown functions as a navigation link to the relevant Assets page.

![VI Asset Count](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-SHCY8CLD.png)

![AssetNavigation](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-129VGNWU.png)

## Axonius Platform New Features and Enhancements

## General Updates

### Assign Permissions and Access by User - User-Based Access Control

The ability has been added to assign access and permissions to supported resources by user as well as by role. Both roles and users can be selected when assigning who gets access to these resources and what type of permission they get. In addition, we simplified the flow with a new and improved "Who has access" section. Select the access level: Public, Shared, or Private. Then select the users and/or roles and the type of access they receive.

![WhoHasAccess.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WhoHasAccess.png)

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**SmartHub INFER**](/docs/smarthub-infer)
  * SmartHub INFER is a unified endpoint lifecycle management solution for edge devices that provides visibility, monitoring, asset management, and security. (Fetches: Devices, Users)

### Adapter Updates

The following adapters were updated:

* [**Slack**](/docs/slack),[**Salesforce**](/docs/salesforce) and [**Zendesk**](/docs/zendesk-adapter)

  * A dropdown in Advanced Settings (Advanced Configuration section) was added that allows the user to select one or more asset types. After the asset types are selected, the relevant advanced configurations are displayed. Advanced Configuration is divided into subcategories to make finding relevant settings easier. In addition, advanced configurations now have a description in a tooltip that provides information such as asset types, permissions, description, and more.

* [**Abnormal Security**](/docs/abnormal-security) - Add the option to enrich threats with information from the threats\_export/api endpoint.

* [**Check Point CloudGuard**](/docs/dome9) - This adapter now fetches compute services as assets.

* [**FireMon Security Manager**](/docs/firemon-security-manager) - This adapter now fetches firewall rules as assets.

* [**Fortify Software Security Center**](/docs/fortify-software-security-center) - Added the option to fetch attributes from another endpoint.

* [**HPE Switches**](/docs/hpe-switches) - Added support for SNMP V2.

* [**Mist**](/docs/mist) - Added the option to add the Access Point name to the Wireless Client device type assets.

* [**OneLogin**](/docs/onelogin)
  * Added the option to not fetch user applications and user events.
  * Added the option to enrich roles with privileges.

* [**Qualys Cloud Platform**](/docs/qualys-cloud-platform) - The THIRD\_PARTY option was added to the "Ignore devices by tracking methods" menu in the Advanced Settings section.

* [**ServiceNow**](/docs/servicenow)
  * Added a **Table Schema Mapping** option - an array in which each row contains an asset type, a table name, an optional query (list of strings), and an optional list of fields to fetch.
  * Added more asset types to the **Custom Parsing** section (including **Load Balancer**).

* [**Snyk**](/docs/snyk)
  * Added the capability to specify the number of issues per page.
  * Added the capability to select whether to filter open or resolved issues.

* [**VMware NSX Advanced Load Balancer**](/docs/avi-networks) - Added the option to fetch assets from all available tenants instead of the default tenant alone.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Tenable Vulnerability Management - Create User**](/docs/tenable-io-create-user) - Creates a new Tenable user and assigns role permissions to the new user.
* [**Tenable Vulnerability Management - Change User Role**](/docs/tenable-io-change-user-role) - Changes the role of an existing Tenable user.
* [**WMI - WinRM Scan**](/docs/winrm-scan) - Scans devices using WinRM, enriches them, and fetches local users.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**AWS - Send JSON to S3**](/docs/send-json-to-amazon-s3) - Added an "Amazon S3 object location (key)" optional field that allows uploading JSON to an internal bucket.
* [**ServiceNow - Create Incident**](/docs/create-servicenow-incident) - Added the **Wrap request in incident\_object** option to wrap the outgoing request payload within an "incident\_object" for APIGEE integration.
* [**ServiceNow - Create Incident per Asset**](/docs/create-servicenow-incident-per-entity) - Added the **Wrap request in incident\_object** option to wrap the outgoing request payload within an "incident\_object" for APIGEE integration.
* [**SharePoint - Update Item In List**](/docs/sharepoint-update-list-item) and [**SharePoint - Delete Item In List**](/docs/sharepoint-delete-list-item) - Added an option to ignore the query results in these Enforcement Actions and run instead on assets specified under the **Manual Item input** section.