# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6143.md

# What's New in Axonius 6.1.43

#### Release Date: December 1st 2024

These Release Notes contain new features and enhancements added in version 6.1.43.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Reports  New Features and Enhancements

The following enhancements were added to reports.

### System Queries Included in Reports

Added the ability to add [Asset Investigation](/docs/advanced-asset-investigation),[Activity Logs](/docs/activity-logs-page),[Findings](/docs/findings-center-page), and [Adapter Fetch History](/docs/adapters-fetch-history) system queries to [Reports](/docs/report-configuration-page).
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Reports-SystemQueries.png)

## Assets Pages

### New Device Field: Associated Azure Configuration

The new '[Associated Azure Configuration](/docs/asset-profile-page-complex-fields#associated-azure-configuration)' complex field displays configuration information in Azure devices and contains the following fields:

* Policy Name
* Compliance State (for compliant devices)
* Non Compliance State (for non-compliant devices)
* Account Name

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Adapter Interface

'Tiles' was changed to 'Cards' on the **Adapters** page.

<Image alt="Cards button Adapters page.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cards%20button%20Adapters%20page(3).png" />

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:
**[Data Aggregation](/docs/configuring-data-aggregation-settings)**

* Added a setting to remove loopback IP addresses from Preferred IPs.

* Added a setting to remove link-local IP addresses from Preferred IPs.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Palo Alto Networks Cortex XSOAR**](/docs/paloalto-xsoar)
  * Cortex XSOAR is a security orchestration, automation, and response platform that integrates and automates threat detection and incident response. (Fetches: Alerts/Incidents)

### Adapter Updates

The following adapters were enhanced:

* **[AWS](/docs/aws-parameters)** -  The Entry Role and Entry Role External ID are now part of the adapter connection configuration and can be used by Axonius-hosted customers.
* [**CSCDomainManager**](/docs/cscdomainmanager) - This adapter now fetches domains and URLs.
* **[CSV Applications](/docs/applications-csv#advanced-settings)** - Added the option to ignore new applications that are not in the SaaS Applications Repository.
* [**Delinea Secret Server (Thycotic)**](/docs/thycotic-secret-server)
  * This adapter now fetches roles, groups, and application resources.
  * Added the option to fetch the users roles and permissions the user has.
  * Added the option to fetch groups.
  * Added required role permissions information.
* **[Google Workspace](/docs/g-suite-by-google#enable-or-exclude-2step-verification)** - You can now use Axonius's new built-in authenticator to set up Multi-Factor Authenticator when creating a connection to the Google Workspace Adapter.
* [**Guardicore**](/docs/guardicore) - Added the option to create devices on agents.
* [**FleetDM**](/docs/fleetdm) - Added the option to enable Legacy Mode.
* [**Have I Been Pwned**](/docs/have-i-been-pwned) - Added the option to fetch users in an asynchronous way.
* [**Jira Service Management**](/docs/atlassian-jira-service-desk) - This adapter now fetches certificates.
* [**Landscape**](/docs/landscape) - Added the option to fetch the software deny list.
* **[Microsoft Entra ID](/docs/microsoft-azure-active-directory-ad#general1)** - Added the option to select the **Fetch Mailbox Delegation Info** option in the 'Fetch mailbox settings for users' advanced configuration, for accounts that have SaaS Management capabilities.
* [**Qualys Cloud Platform**](/docs/qualys-cloud-platform) - Added the option to fetch certificates as assets.
* [**Randori**](/docs/randori) - Added support for new API Access Token authentication.
* [**Trend Micro Vision One**](/docs/trendmicro-vision-one) - Added the option to fetch extended endpoint details (including MAC addresses).
* [**UpGuard CyberRisk**](/docs/upguard-cyberrisk) - This adapter now fetches domains and URLs.
* [**VMware ESXi and vSphere**](/docs/vmware-esxi) - Added the option to force parsing the serial number from the 'SerialNumberTag' field.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**ManageEngine Endpoint (Desktop) Central and Patch Manager Plus - Create Software Action**](/docs/desktop-central-create-software-action) - Performs an install or uninstall of a software.

* [**Microsoft Teams - Send Direct Message to a User**](/docs/teams-send-dm-to-user) - Sends a direct message to Teams users.

* [**Microsoft Teams - Send Direct Message to a Channel**](/docs/teams-send-dm-to-channel) - Sends a direct message to Teams channels.

* [**Palo Alto Cortex XSOAR Create Incident**](/docs/paloalto-xsoar-create-incident) - Creates incident for assets.

* [**Okta - Reset User Factors**](/docs/okta-reset-user-factors) - Resets all authentication factors of Okta users.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* **[Axonius - Calculate Risk Score](/docs/risk-score#assigning-numeric-values-to-nonnumeric-fields)** - The option to assign numeric values to non-numeric fields incorporated in the calculation process was added. Users can now select non-numeric fields such as text, boolean or enum fields and assign them numeric values using standard Axonius query operators. This way, users can more accurately calculate the risk scores of vulnerabilities that include qualitative attributes.
* **[CSV - Send to Share](/docs/send-csv-to-share)** - Added the capability to export CSV files as Excel Worksheets.
* [**Qualys - Add IP Addresses to Asset Group**](/docs/add-ips-to-qualys-asset-group) - Added the  new 'Fail when no IP is added' field to this Enforcement Action to enable the action to present a failure status when it doesn't find an  IP address to add.
* [**Trace3 Lamp - Update Device**](/docs/trace3-lamp-update-device) - The ability to select Trace3 fields from the list in the Field Mapping was added.