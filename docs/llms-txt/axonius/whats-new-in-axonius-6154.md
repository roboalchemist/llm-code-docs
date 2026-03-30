# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6154.md

# What's New in Axonius 6.1.54

#### Release Date: February 17th 2025

These Release Notes contain new features and enhancements added in version 6.1.54.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

#### Flexible Asset Page Opening from Dashboards

Users now have more control over [how they open asset pages](/docs/chart-actions#view-results) that are linked from Axonius dashboard charts. The following options are available when clicking on a chart segment or link:

* **Standard Click**: Opens in a new tab and switches focus.

* **CTRL+Click**: Opens in a new tab, focus stays on the dashboard.

* **SHIFT+Click**: Opens in a new window.

## Assets Pages

The following feature was added to all assets pages:

### Share Saved Views

Users can now [share their saved views](/docs/setting-page-columns-display#sharing-a-view) with other users by selecting roles and their access permissions.

<Image align="center" alt="ShareViews.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ShareViews.png" />

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### [Adapter Connections](/docs/adapter-connections) Page  Enhancements

* A new column called "Failed Connection Attempts Before Fetch Failure" was added.
* Renamed the "Gateway Name" column to "Gateway".
* A new filter called "Gateway" was added.

### [Adapter Profile](/docs/adapter-profile-page) Page Enhancements

The Edit Connection drawer, opened from the Adapter Profile page, allows direct access via copiable links.

### Ingestion Rules Support all Axonius Asset Types

[ Ingestion Rules](/docs/setting-adapter-ingestion-rules) now support all Axonius asset types (previously limited to Devices and Users).

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Enhancements

Dynamic Value Statements have been enhanced with a dedicated Settings interface and a new option to control Enforcement Action behavior when a Dynamic Value Statement fails.

#### Dynamic Value Statement Settings

When toggling on **Configure Dynamic Values**, a new Settings icon appears. An orange dot on the icon indicates that at least one setting is enabled.
Clicking the icon displays the following options:

* **Ignore empty values on asset fields** - This existing option (previously outside of Settings) is enabled by default.
* [**Fail the action if dynamic values fail**](#aborting-the-action-when-dynamic-value-statement-fails) - This new option is disabled by default.

<Image alt="DynamicValuesSettings.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DynamicValuesSettings.png" />

#### Aborting an Action when a Dynamic Value Statement Fails

To provide greater control over **Dynamic Value Statements**, a new 'Fail the action if dynamic values fail' setting was added to 'Configure Dynamic Values' in **Enforcement Actions**.  When enabled, this setting halts the Enforcement Action and marks it as 'Failed' if an asset's dynamic value doesn't meet the defined criteria.  By default, if this setting is not enabled, a fallback value is used, and the action is logged as 'Success'.

## System Settings New Features and Enhancements

The following updates were made to various System settings:

#### Change Default CSV Separator Configuration

A new  'Export CSV separator' setting was added to the **[CSV Export](/docs/configuring-csv-export-settings)** settings to allow users to specify the character used to separate items in CSV exports. This allows users to change the default comma (,) to another character, such as a semicolon (;).

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Appknox**](/docs/appknox)
  * Appknox is a tool that provides mobile app security testing and analysis. It allows you to identify and fix security vulnerabilities in your mobile apps, ensuring that they are secure and compliant with industry standards. (Fetches: Users)
* [**Check Point Multi-Domain Security Management (MDSM)**](/docs/checkpoint-mdsm)
  * Check Point Multi-Domain Security Management (MDSM) is a centralized platform that provides comprehensive security management across multiple domains. (Fetches: Devices)
* [**Esper**](/docs/esper-mdm)
  * Esper is a platform that provides comprehensive device management and application deployment solutions. (Fetches: Devices)
* [**GitGuardian**](/docs/git-guardian)
  * GitGuardian is a security platform that offers secret detection and monitoring for code repositories. (Fetches: Alerts/Incidents)
* [**Google Chronicle SOAR**](/docs/google-chronicle-soar)
  * Google Chronicle SOAR is a security orchestration, automation, and response platform that streamlines threat detection, investigation, and remediation. (Fetches: Alerts/Incidents)
* [**MariaDB**](/docs/mariadb)
  * MariaDB is an open-source relational database management system that supports a wide range of database operations and integrations. (Fetches: Users, Application Resources)
* [**Nextcloud**](/docs/nextcloud)
  * Nextcloud is a collaboration platform that provides file sharing and communication tools. (Fetches: Users)

### Adapter Updates

The following adapters were updated:

* [**Action1**](/docs/action1) - Added the option to enrich devices with vulnerabilities.
* [**Alibaba Cloud**](/docs/alibaba-cloud) - Added the option to fetch users.
* **[CSV](/docs/csv)** - Added the option to force non-string fields (dynamically created by the adapter) to be strings.
* [**DNSFilter**](/docs/dnsfilter) - Host Name or IP Address was removed from connection parameters.
* [**Mandiant**](/docs/mandiant) - This adapter now fetches domains and URLs.
* **[Microsoft Azure](/docs/microsoft-azure)** - Added the option to apply the value of Last Seen as a reference timestamp only for connected Arc-Enabled machines. For machines with a status other then 'connected', the reference timestamp is Last Status Change.
* **[Rapid7 InsightVM](/docs/rapid7-insightvm)** - Added the option to parse each CVE ID and plugin ID in the vulnerability as Vulnerable Software.
* **[Rapid7 Nexpose Warehouse](/docs/rapid7-nexpose-warehouse)** - Added the option to parse each CVE ID and plugin ID in the vulnerability as Vulnerable Software.
* [**RSA Archer**](/docs/rsa-archer) - Added the option to fetch applications.
* [**Symantec Endpoint Management Suite (Altiris)**](/docs/symantec-endpoint-management-suite-altiris) - Added the option to fetch only installed software.
* **[Tenable.io](/docs/tenableio)** - Added the option to parse each CVE ID and plugin ID in the vulnerability as Vulnerable Software.
* **Wiz** - Added the capability to not fetch resolved Wiz Vulnerabilities.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Axonius - Change Alert Status**](/docs/change-alert-status) - Changes the status of Finding Alert assets returned by the selected query or selected on the Finding Alerts page.
* [**Zscaler - Delete Users**](/docs/zscaler-delete-user) - Deletes Zscaler users.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Tenable.io - Add IP Addresses to Target Group**](/docs/tenable-io-launch-was-scan) - Added the option to either use the preferred hostname FQDN or use AWS Public DNS as a hostname.