# Source: https://docs.axonius.com/changelog/release-notes-8015.md

# Axonius Release Notes 8.0.15

#### Release Date: February 16th 2026

These Release Notes contain new features and enhancements added in version 8.0.15.

## Exposures New Features and Enhancements

The following new features and enhancements were added to Exposures:

## Query Wizard

### Adding Notes to Query Expressions

Complex queries are constructed in an iterative process, layering expressions to refine results. As queries grow in complexity, the rationale behind specific parameters or conditions can become difficult to recall or interpret.

To address this issue, users can now add notes to each individual query expression. This capability serves the following key functions:

* **Maintainability:** It allows the original query creator to document their logic for future reference when revisiting the query.
* **Collaboration:** It provides context for team members reviewing or reverse-engineering the query, ensuring the logic is transparent and understandable.
* **Auditing**- When Axonius is used for security audits, notes are required to clearly describe the expressions in the Queries.

## System Settings

The following updates were made to various System settings:

### Network Management - Subnet Fetch

A new Network Management setting **Insert all possible Subnets on Device Network Interface was added**, enabled by default. When enabled, Axonius calculates and inserts all possible common subnets based on the device's IP addresses. To reduce noise in subnet data and fetch only subnets that the device is actually inserted into and receiving traffic from, disable this setting.

### &#x20;Uploading a CA Chain File

In [**Certificate and Encryption Settings**](https://docs.axonius.com/docs/certificate-settings), users can now upload a CA Chain file in DER, PFX or PEM format. Axonius automatically concatenates them and creates a valid certificate file.

## Enforcements

The following new features and enhancements were added to the Enforcements:

### Cancelling a Pending Enforcement Run

It is now possible to cancel an enforcement set run when its status is pending. The new option is available in the node settings. Enforcement sets that have been cancelled are assigned a result of 'Terminated'. The Enforcement set is not run, and no changes are made.

***

<br />

## New Adapters

* **[Menlo Security](https://docs.axonius.com/axonius-help-docs/docs/Menlo-Security)** - Menlo Security is a cybersecurity solution that offers isolation technology to prevent web-based threats. (Fetches: Devices, Users)
* **[Troverlo](https://docs.axonius.com/axonius-help-docs/docs/Troverlo)** - Troverlo is a network intelligence platform that offers asset tracking and monitoring solutions for real-time asset location, current active user tracking, and remote asset action commands. (Fetches: Devices)
* **[Holm Security](https://docs.axonius.com/axonius-help-docs/docs/Holm-Security)** - Holm Security is a cybersecurity platform that provides vulnerability management, attack surface visibility, compliance reporting, and risk assessment across external and internal digital assets. (Fetches: Devices)
* **[Fortinet FortiAnalyzer](https://docs.axonius.com/axonius-help-docs/docs/Forti-Analyzer)** - FortiAnalyzer is a centralized log management and analytics platform that provides log collection, correlation, analysis, and reporting from Fortinet devices and third-party syslog sources for security monitoring and compliance. (Fetches: Devices)

## Updated Adapters

* **[Apache CloudStack](https://docs.axonius.com/axonius-help-docs/docs/apache-cloudstack)** - Added options to fetch domains, users, and networks.

* **[Censys ASM](https://docs.axonius.com/axonius-help-docs/docs/Censys-Asm)**
  * Added the option to parse URL assets.
  * Added the option so that  assets with a valid Top Level Domain are only parsed as URL assets.

* **[Custom Files](https://docs.axonius.com/axonius-help-docs/docs/custom-files)**
  * This adapter now fetches Certificates.
  * Added an option to set the time zone of date fields fetched with this adapter.

* **[CyberArk Privileged Account Security](https://docs.axonius.com/axonius-help-docs/docs/cyberark-privileged-account-security)** - Added the option to enrich account data with platform information (available only when Fetch Accounts is enabled).

* **[Microsoft Defender for Endpoint (Microsoft Defender ATP)](https://docs.axonius.com/axonius-help-docs/docs/microsoft-defender-atp)** - Added a capability to authenticate with Managed Identity.

* **[NTT Application Security](https://docs.axonius.com/axonius-help-docs/docs/ntt-application-security)** - This adapter was renamed to Black Duck Continuous Dynamic.

* **[Rapid7 Insight AppSec](https://docs.axonius.com/axonius-help-docs/docs/Rapid7-Insight-Appsec)** - Added options to enrich apps, devices and URLs with Scans.

* **[SentinelOne Ranger](https://docs.axonius.com/axonius-help-docs/docs/sentinelone-ranger)** - Added device deduplication under advanced configuration.

* **[Slack](https://docs.axonius.com/axonius-help-docs/docs/slack)** - Added the option to fetch Application Settings.

* **[SPEKTRA](https://docs.axonius.com/axonius-help-docs/docs/Spektra)** - Updated network devices categorization.

* **[Tableau](https://docs.axonius.com/axonius-help-docs/docs/Tableau)** - Added the option to fetch Application Settings.

* **[Trend Micro Vision One](https://docs.axonius.com/axonius-help-docs/docs/Trendmicro-Vision-One)** - Added the option to enrich devices with 'Recent Executables'.

* **[Verkada](https://docs.axonius.com/axonius-help-docs/docs/Verkada)** - Adding new endpoints for additional fields.

* **[Zabbix](https://docs.axonius.com/axonius-help-docs/docs/zabbix)** - Added the option to the determine the hostname from the DNS.

## New Enforcement Actions

* [**Netsuite - Create User**](https://docs.axonius.com/axonius-help-docs/docs/netsuite-create-user) - Added new enforcement action to create users.
* [**Netsuite - Delete User**](https://docs.axonius.com/axonius-help-docs/docs/netsuite-delete-user) - Added new enforcement action to delete users.
* [**Netsuite - Suspend User**](https://docs.axonius.com/axonius-help-docs/docs/netsuite-suspend-user) - Added new enforcement action to deactivate users.
* [**Netsuite - Assign User Role**](https://docs.axonius.com/axonius-help-docs/docs/netsuite-assign-user-role) - Added new enforcement action to assign roles to users.
* [**AssetSonar - Delete or Retire Asset**](https://docs.axonius.com/update/docs/manage-sonar-asset) - Added new enforcement action to delete or retire assets.

## Updated Enforcement Actions

* **Have I Been Pwned - Skip Enrichment** - Added new enforcement action configuration to skip enrichment if nothing has changed.
* **[WMI - WinRM Scan](https://docs.axonius.com/axonius-help-docs/docs/winrm-scan)** - Added an option to fetch Share permission.

<br />