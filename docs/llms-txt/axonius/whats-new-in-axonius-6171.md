# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6171.md

# What's New in Axonius Asset Cloud 6.1.71

#### Release Date: June 15th 2025

These Release Notes contain new features and enhancements added in version 6.1.71.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Exposures New Features and Enhancements

The following new features and enhancements were added to Exposures:

### New Enrichment Source - EUVD

European Union Vulnerability Database (EUVD) is a platform that offers information on security vulnerabilities. The EUVD API was integrated into the Axonius platform to automatically enrich CVE data. This enrichment occurs automatically during the system's discovery cycles, without manual intervention. Users can enable or disable enrichment from this source from  **Enrichment** under **System Settings**.

## Software Assets New Features and Enhancements

The following new features and enhancements were added to Software Assets:

The  **Software Sub Category**  field was added to the Software page.

## Axonius Platform New Features and Enhancements

### Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Pivot Chart Enhancements

#### Compare Results to a Previous Date in Pivot Bar Chart and Pivot Single Row Tables

The option to compare current query results to a [specific date or relative date](/docs/comp-query-previous-date) is now available in the Pivot chart for bar charts and single row tables.

<Image alt="CompareHistorical.png" width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CompareHistorical.png" />

#### Min/Max Limits for Y-Axis on the Pivot Timeline Chart

The ability has been added to set minimum and maximum values for the y-axis in a Pivot line chart.
![TimelineYaxisMinMax.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TimelineYaxisMinMax.png)

## Assets Pages

The following features were added to all assets pages:

### Query Wizard Enhancements

Common Enrichment fields were added to Field Comparison.

## Activity Log New Features and Enhancements

Activity logs now show more information about actions taken when remote support is enabled.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Better Stack Uptime**](/docs/betterstack-uptime)
  * Better Stack Uptime is a monitoring solution that provides real-time alerts and incident management for website and service availability. (Fetches: Domains & URLs, Application Services)
* [**KnowBe4 PasswordIQ**](/docs/knowbe4-password-iq)
  * KnowBe4 PasswordIQ is a solution that offers secure password management and access control. (Fetches: Users)
* [**ngrok**](/docs/ngrok)
  * ngrok is a secure tunnel service that provides remote access to local servers. (Fetches: Users, Network/Firewall Rules)
* [**Productiv**](/docs/productiv)
  * Productiv is a SaaS management platform that provides real-time visibility into application usage, spend, and compliance to optimize software investments and governance. (Fetches: Licenses, Expenses, SaaS Applications)
* [**XCP-ng**](/docs/xcp-ng)
  * XCP-ng is an open-source virtualization platform that offers enterprise-grade features for managing virtual machines. (Fetches: Devices)
* [**Yokogawa BKHRevInf**](/docs/yokogawa-bk-rev-info)
  * Yokogawa BKHRevInf is a cybersecurity risk assessment solution that provides a comprehensive evaluation of technical, operational, and business risks within industrial control systems. (Fetches: Devices)
* [**Zscaler SSPM**](/docs/zscaler-sspm)
  * Zscaler SSPM is a solution that provides continuous monitoring and remediation of SaaS application security configurations to enhance data protection and compliance. (Fetches: Vulnerabilities, Users, Business Applications, SaaS Applications, Network Services, Network/Firewall Rules)

### Adapter Updates

The following adapters were updated:

* [**Cisco Prime**](/docs/cisco-prime) - Verify SSL was added to connection parameters.
* [**Cohesity**](/docs/cohesity) - Added the option to fetch protected/unprotected objects from the Cohesity report export.
* [**IBM Guardium Data Protection**](/docs/ibm-guardium-vulnerability-assessment) - Added the option to create ad hoc online reports in JSON format.
* [**Infoblox BloxOne** ](/docs/bloxone) - Added the option to not fetch roaming devices.
* [**Jira Service Management (Service Desk) Fetch Tickets**](/docs/jira-fetch-tickets) - Added the option to fetch Child work items for each Epic ticket.
* [**MarkMonitor**](/docs/markmonitor) - API Key was added to connection parameters.
* [**Microsoft Active Directory (AD)**](/docs/microsoft-active-directory-ad)
  * Added the option to select the port to connect to WinRM.
  * Added a configuration 'WinRM Use SSL' that must be enabled when using port 9586.
  * The name of the advanced setting 'Enrich group members for each group' was changed to 'Enrich group members with SID for each group', which will fetch SID data of the group members.
  * Added an option to enrich group members with the distinguished name for each group member.
* [**Microsoft Azure**](/docs/microsoft-azure) - This adapter now fetches the PurviewAccount entity as Accounts/Tenants.
* [**Microsoft Entra ID (formerly Azure Active Directory) and Microsoft Intune**](/docs/microsoft-azure-active-directory-ad)
  * Added the option to fetch active user details from Office 365 from a specified number of days.
  * Added an option to fetch 'managed app registrations from MAM' from a different API.
* [**Oracle NetSuite**](/docs/netsuite) - Added the option to fetch expenses of sub type `vendor_bill` from the List Vendor Bills endpoint, and expenses of sub type `vendorPayment` from the List Vendor Bill Details endpoint.
* [**Palo Alto Networks Cortex Xpanse** ](/docs/palo-alto-networks-cortex-xpanse) - Added the capability to parse Domains and Certificates as their own asset types, instead of Devices. This is done by enabling the **Categorize devices** advanced setting.
* [**Rubrik Polaris**](/docs/rubrik-polaris) - Added the capability to enter a list of object types to parse asset name and hostname from the device location. This setting only works for devices that have the asset type field with the value 'edge'.
* [**Tanium Client Status**](/docs/tanium-status) - Added the capability to set the number of days prior to token expiration to begin generating fetch event warnings about this.
* [**Tenable.sc**](/docs/tenablesc-formerly-securitycenter) - Added the option to fetch data from acceptRiskRule endpoint and recastRiskRule endpoint.
* [**ThreatLocker**](/docs/threatlocker) - Added the capability to choose the API version in connection parameters.
* [**Trend Micro Deep Security**](/docs/trend-micro-deep-security) - Added the option to fetch Prevention Intrusion Rules, which enrich the fetched devices with CVE information.
* [**Zabbix**](/docs/zabbix) - Added the option to enrich devices with corresponding problems.
* [**Zscaler Client Connector**](/docs/zscaler-zcc) - Added the option to fetch registered devices' details.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**GitHub - Add issues to projects**](/docs/github-add-issues-to-projects) - Adds issues to GitHub Projects.

* [**Splunk - Delete Assets**](/docs/splunk-delete-assets) - Deletes Splunk assets that are no longer valid or active in Axonius.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Microsoft Defender ATP - Add or Remove Tag to/from Assets**](/docs/defender-atp-tag-assets) - Added the option to include only assets from the adapter's last fetch.
* [**Create ServiceNow Incident**](/docs/create-servicenow-incident) and [**ServiceNow - Create Incident per Asset**](/docs/create-servicenow-incident-per-entity) - Returns the unique Incident Sys ID of the newly created ticket as an artifact.
* [**GitHub - Create issue**](/docs/github-create-issue) - Added the option to associate an issue with multiple projects.
* [**Okta - Assign Role to Users**](/docs/assign-okta-role-to-user) - Added the option to select Resource Set IDs to assign/unassign custom roles.