# Source: https://docs.axonius.com/docs/whats-new-in-axonius-709.md

# What's New in Axonius Asset Cloud 7.0.9

#### Release Date: September 14th 2025

These Release Notes contain new features and enhancements added in version 7.0.9.

* Read [**What's New in Axonius 7.0**](/docs/whats-new-in-axonius-700) to see all Axonius 7.0 features.

## SaaS Applications New Features and Enhancements

The following new features and enhancements were added to SaaS Applications:

### Licenses Page

**Inline Edit Dynamic Update**
When you edit fields on the licenses asset page using inline edit, the system now updates columns that are dependent on these fields immediately, without waiting for a discovery cycle. If the user uses online edit to change the quantity or price, the annual total cost is updated automatically.

## Axonius Platform New Features and Enhancements

### Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

#### Create Dynamic Dashboards with Saved Filters

You can create dynamic dashboards for specific needs that give you the exact information you want, when you want it. By creating and applying [saved filters](/docs/using-saved-filters) to an entire dashboard, you can focus on specific datasets without having to manually adjust each chart.

For example, if your company operates in multiple regions, you can build one dashboard and apply a saved filter for each geographic region. This way, each regional team can see a personalized view of their data, while you maintain a consistent dashboard design across the entire organization.

<Image align="center" alt="SavedFilterAppliedMenu.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SavedFilterAppliedMenu.png" />

After upgrading to this version of Axonius:

* Dashboards viewed within 30 days of the migration will be automatically refreshed.
* Dashboards not viewed within 30 days of the migration may need to be manually refreshed to see the latest data. A message will appear:

<Image align="center" alt="SavedFilterRefreshMessage.png" border={false} width="700px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SavedFilterRefreshMessage.png" />

* Once 30 days have passed since the upgrade, any dashboard not viewed for 60 days may need to be manually refreshed to see the latest data. The refresh message will appear.
* Dashboards that have been viewed in the last 60 days are still refreshed every 6 hours.

### Reports New Features and Enhancements

The following enhancements were added to reports.

#### Create Custom Reports with Saved Filters

[Saved filters](/docs/using-saved-filters) can be applied to dashboards included in [reports](/docs/report-configuration-page) to create customized version of the report. When selecting the dashboards and charts to include, select a filter to apply to the dashboard. When individual charts are selected from a dashboard, the filter is appied to all charts from the same dashboard. This helps to create custom versions of the dashboards for specific reporting needs.

<Image align="center" alt="SavedFilterReportsMultiple.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SavedFilterReportsMultiple.png" />

### Assets Pages

The following features were added to all assets pages:

### New Option to Exclude Asset Types from Global Search

Administrators can now control which asset types are returned via Global Search. From the **System Settings** page, they can choose to exclude (or include) specific asset types from **Global Search**, so that no results from these asset types are returned in the search.

<Image align="center" alt="SearchSettings" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-TOUB4VVR.png" />

### Query Management New Features and Enhancements

The following new features and enhancements were added to the Queries:

### New Filter: Fields used in Query

A new filter was added to the **Queries** page to find queries by the field names in use in the query expression. You can select fields of multiple asset types and adapters to filter by.

<Image alt="FilterQueriesByFieldName.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FilterQueriesByFieldName.png" />

## System Settings Updates

The following updates were made to various System settings:

### SAML Configuration URLs are Now Validated

When configuring a [SAML integration](https://docs.axonius.com/axonius-help-docs/docs/saml-based-login-settings) without using the metadata file, several URLs are required. These URLs are now validated. Error messages for invalid URLs are displayed at the bottom of the page.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**NetDocuments**](/docs/netdocuments)
  * NetDocuments is a content management platform that provides document and email management, workflow automation, and search capabilities for legal environments. (Fetches: Users, Groups)
* [**NVIDIA Bright Cluster Manager**](/docs/nvidia-bright-cluster-manager)
  * NVIDIA Bright Cluster Manager is a system management tool that provides centralized provisioning, monitoring, and administration of high-performance computing clusters across on-premises and hybrid environments. (Fetches: Devices)
* [**Socket**](/docs/socket)
  * Socket is a developer-first platform that provides real-time monitoring and static analysis to prevent supply chain attacks in open source dependencies. (Fetches: Application Resources)
* [**Synology Surveillance Station**](/docs/synology-surveillance-station)
  * Synology Surveillance Station is a video management software that provides monitoring and recording functionalities for security cameras. (Fetches: Devices)

### Adapter Updates

The following adapters were updated:

* [**BitSight Security Ratings**](/docs/bitsight-security-ratings) - This adapter now fetches Roles.

* [**CrowdStrike Falcon Discover**](/docs/crowd-strike-falcon-discover) - Added the option to fetch only Devices within specific Networks.

* [**Custom Files**](/docs/custom-files) - This adapter now fetches Networks, Application Keys, and Containers. It also supports [Custom Parsing](/docs/adapter-custom-parsing) for these assets.

* [**CyberArk Privilege Cloud**](/docs/cyberark-privilege-cloud)
  * Added the option to enrich the Users endpoint with User Roles.
  * Added the option to fetch users of the subtype 'users from safe members' from the Users From Safe Members endpoint.
  * Added the option to fetch users of the subtype 'users from role members' from the Users From Role Members endpoint.
  * Added the option to fetch security roles from the Built-in Roles endpoint.

* [**eyeInspect**](/docs/eyeinspect) - Added the option to enrich host devices with change log data.

* [**Jira Service Management (Service Desk)**](/docs/atlassian-jira-service-desk) - This adapter now supports [Custom Parsing](/docs/adapter-custom-parsing) for all fetched asset types.

* [**MongoDB**](/docs/mongodb) - Use LDAP Authorization was added to connection parameters.

* [**Okta**](/docs/okta) - Added the option to fetch apps and groups in the background, outside the regular fetch.

* [**OpenLdap**](/docs/openldap) - Added the option to fetch Groups and enrich Users with Groups data.

* [**Palo Alto Networks Strata Cloud Manager**](/docs/palo-alto-networks-strata-cloud-manager) - Added an option to fetch IoT devices.

* [**Rapid7 InsightIDR**](/docs/rapid7-insightidr) - Added an option to fetch security alerts from Rapid7 InsightIDR investigations, in addition to standard device data. When enabled, they are fetched as Alerts/Incidents.

* [**Rapid7 InsightVM**](/docs/rapid7-insightvm) - Added an option to ingest non-CVE Rapid7 Plugin as Vulnerable Software. When enabled, Rapid7 InsightVM vulnerability findings that **don't** have a CVE ID are added to the asset's Vulnerable Software list using the raw Rapid7 plugin ID as the identifier.

* [**Rubrik Security Cloud**](/docs/rubrik-polaris) - The name of the 'Rubrik Polaris' adapter was changed to **Rubrik Security Cloud**.

* [**Sailpoint IdentityIQ**](/docs/sailpoint-iq) - This adapter now supports Layer 7 API gateway connection.

* [**ServiceNow**](/docs/servicenow) - Added an option to display the Upstream and Downstream field values as a flat list rather than a graph. The Relation Depth displayed in this format is greater - up to 10.

* [**Splunk**](/docs/splunk)
  * Added an option to fetch custom agent data.
  * Added an option to provide a Splunk Application Keys Search Macros List and a Splunk Containers Search Macros List while connecting the adapter.

* [**Tenable Vulnerability Management**](/docs/tenableio) - Added an option to fetch plugins explicitly specified in other advanced settings, even when Vulnerability Fetch is disabled.

* [**VMWare ESXi and vSphere**](/docs/vmware-esxi) - Added an option to parse all tags as fields.

### New Enforcement Actions

The following new Enforcement Actions were added:

* [**BambooHR - Create User**](/docs/bamboohr-create-user) - Creates a user in BambooHR.
* [**Tenable Vulnerability Management - Create User**](/docs/tenable-io-create-user) - Creates a user in Tenable Vulnerability Management.
* **Tenable Vulnerability Management - Assign User to Role** - Assigns a specific role to a Tenable Vulnerability Management user.
* **Tenable Vulnerability Management - Assign User to Group** - Adds or remove users from a Tenable Vulnerability Management group.
* [**Tenable Vulnerability Management - Suspend User**](/docs/suspend-tenableio-user) - Suspends a user in Tenable Vulnerability Management.

### Updated Enforcement Actions

The following new Enforcement Actions were updated:

* [**Freshservice - Create Assets**](/docs/create-freshservice-asset) and [**Freshservice - Update Assets**](/docs/update-freshservice-asset) - Added the option to configure the Workspace ID.
* [**Halo - Create or Update Device**](/docs/halo-create-update-device) -  and [**Halo - Create or Update User**](/docs/halo-create-update-user) - New **Site ID** parameter.
* [**Send Assets Data - Kovrr**](/docs/send-asset-data-to-kovrr) - Company ID field added to replace configuration multiple fields.