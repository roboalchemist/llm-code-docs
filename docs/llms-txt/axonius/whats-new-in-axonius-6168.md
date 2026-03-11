# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6168.md

# What's New in Axonius Asset Cloud 6.1.68

#### Release Date: May 25th 2025

These Release Notes contain new features and enhancements added in version 6.1.68.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Software Assets New Features and Enhancements

The following new features and enhancements were added to Software Assets:

The "Is EOL" field (which can be found on the Software page and the Software Versions tab of the Software Profile page) now accurately reflects the end-of-life status of software, including those without a defined EOL date. Now, if software is known to not have an EOL date, "Is EOL" will be 'No', ensuring accurate reporting and management of your software assets.

## Axonius Platform New Features and Enhancements

### Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Dashboard Management Enhancements

#### New Icon for Favorite Dashboards

The star that indicates that a dashboard is a favorite is now displayed in the icon to the left of the dashboard name. You can add and remove dashboards from the Favorites from the 3-dot menu.
![NewDashboardFavoritesIcon.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NewDashboardFavoritesIcon.png)

### Chart Enhancements

The following enhancements  were made to charts.

#### Add a Hyperlink to a Text Chart

The ability to add a hyperlink to a text chart has been added.

<Image alt="ChartWHyperlinks.png" width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChartWHyperlinks.png" />

### System Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### CyberArk Privilege Cloud Vault External Password Manager

It is now possible to add multiple domains (tenants) of the [CyberArk Privilege Cloud Vault](/docs/managing-external-passwords#cyberark-privilege-cloud-vault) to the external password manager (accessed from **System Settings> Access Management> External Password Managers> CyberArk Privilege Cloud Vault**). When setting up an Adapter or an Enforcement Action, you can [choose from which CyberArk Privilege Cloud Vault domain](/docs/cyberark-privilege-cloud-vault) you want to fetch the secret.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Meegle**](/docs/meegle)
  * Meegle is a platform that offers digital marketing and reputation management services. (Fetches: Users, Tickets)
* [**Nokia**](/docs/nokia)
  * Nokia is a networking and telecommunications company that offers solutions for network infrastructure and services. (Fetches: Devices)
* [**Rapid7 InsightConnect**](/docs/rapid7-insight-connect)
  * Rapid7 InsightConnect is a security orchestration, automation, and response tool that offers streamlined incident response workflows. (Fetches: Tickets)
* [**Synology**](/docs/synology)
  * Synology is a network-attached storage provider that offers data management and backup solutions. (Fetches: Devices, Users)

### Adapter Updates

The following adapters were updated:

* [**Adobe Workfront**](/docs/adobe-workfront)
  * Added parameters **Client ID** and **Client Secret** to be filled in when using the oAuth authentication method.
  * Added the option to select the **API Version**: **v14.0** (default) or **v15.0** (new).

* [**BlackBerry Unified Endpoint Management (UEM)**](/docs/blackberry-unified-endpoint-management-uem)
  * This adapter now fetches users as assets.
  * Added the option to fetch users.

* [**Cisco Identity Services Engine (ISE)**](/docs/cisco-identity-services-engine-ise) - The "Add Authentication Status to Endpoints" advanced setting was renamed as "Enrich Endpoints with Authentication Status and Session Parameters". Now, besides fetching the authentication status, this adapter can also fetch and enrich endpoint devices with session parameters. This allows to populate the Last Seen field, for example.

* [**Dynamics CMDB**](/docs/helpdesk),[**CSV**](/docs/csv),[**JSON**](/docs/json), and [**SQL Server**](/docs/sql-server) - In the Custom Parsing module, the Field Type parameter was renamed to Field Structure.

* [**Elasticsearch**](/docs/elasticsearch) - Added an option to define the name of the object containing extra data for a device. Users can now parse Installed Software, Vulnerabilities, BIOS data and Hardware Serial as custom objects.

* [**Freshservice Fetch Tickets**](/docs/freshservice-fetch-tickets) - Added the option to map each ticket Status to a Status Description, enabling users to easily understand the meaning of each status.

* [**Imperva WAF**](/docs/imperva-waf) - This adapter now fetches network/firewall rules as assets.

* [**IONIX (formerly Cyberpion)**](/docs/ionix) - This adapter now fetches vulnerabilities and SaaS applications as assets.

* [**Microsoft Entra ID (formerly Azure Active Directory) and Microsoft Intune**](/docs/microsoft-azure-active-directory-ad)
  * Added an option to download an exported report from Entra ID and save this data to the database instead of calling the Managed Devices API.
  * Added an option to fetch cloud PCs as Intune devices.

* [**Nozomi Guardian and CMC**](/docs/nozomi-networks-guardian) - Added the option to ignore assets where the name matches the appliance host value.

* [**Nucleus Security**](/docs/nucleussec) - Added the option to fetch the project risk score.

* [**OpenLdap**](/docs/openldap) - Added the option to enter fallback values for host and port to be connected if the first ones fail.

* [**Paycom**](/docs/paycom)
  * Added the option to not fetch employee data from non-sensitive endpoints.
  * Added the option to fetch employee data from sensitive endpoints.
  * Added the capability to enter a list of raw keys that should be removed from ingested data.

* [**PingFederate**](/docs/pingfederate) - Added an option to fetch certificates.

* [**Quest KACE Endpoint Systems Management Appliances**](/docs/quest-kace-endpoint-systems-management-appliances) - Added the capability to parse specific device fields from the raw data fetched by the adapter. Additionally, it is possible to now base this adapter on either the new API version 14.0 or the existing version 12.0.

* [**Rubrik Polaris**](/docs/rubrik-polaris) - Added the option to parse the cluster nodes from the cluster raw as devices.

* [**Sonatype**](/docs/sonatype)
  * This adapter now fetches roles and organizational units as assets.
  * Added the option to enrich Users with Role Membership.
  * Added the option to fetch OrganizationalUnits from Organizations.
  * Added the option to fetch SecurityRoles from Roles.

* [**Trellix Endpoint Security (HX)**](/docs/fireeye-endpoint-security-formerly-hx) - Added the option to enrich devices with sysinfo data.

* [**Trend Micro Vision One**](/docs/trendmicro-vision-one) - Added the capability to specify the number of entities returned per page request.

* [**VMware ESXi and vSphere**](/docs/vmware-esxi) - Added the option to not fetch users and local accounts.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**GitHub - Update Issue**](/docs/github-update-issue) - Updates an issue on GitHub. Users can update the issue's state, title, body, and state reason.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Jira Service Management - Create Ticket**](/docs/create-jira-service-desk-ticket) -
  The new **Append CSV data to request description** option enables automatically adding data from the CSV file to the end of text entered in the **Request description** field.

* [**Nessus - Add Agent to Agent Group**](/docs/nessus-add-agent-to-agent-group) - The name of this action was changed to **Nessus - Add/remove Agent to/from Agent Group**, as now users can also remove agents and not just add them.

* [**ServiceNow - Request Catalog Item**](https://docs.axonius.com/enforcements/docs/request-service-now-catalog-item) - When the **Send CSV data option** is enabled, it is now possible to enable the new advanced **Attach CSV on requested item (RITM) instead of on request** option, to attach the CSV on the requested item (RITM) instead of on the request itself (REQ).

* [**Wrike - Create or Update Task**](/docs/wrike-create-update-task) - Added new options to assign responsibilities, due date, and work on weekends.