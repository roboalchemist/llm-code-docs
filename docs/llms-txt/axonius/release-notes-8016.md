# Source: https://docs.axonius.com/changelog/release-notes-8016.md

# Axonius Release Notes 8.0.16

#### Release Date: February 22nd 2026

These Release Notes contain new features and enhancements added in version 8.0.16.

## Exposures New Features and Enhancements

The following new features and enhancements were added to Exposures:

### New Enrichment Source

The following Out-of-the-Box enrichment source was added to enrich Security Finding data:

* **OSV (Open Source Vulnerabilities)** - a database identifying affected open-source packages, ecosystems, severities (when available), and references.

# Axonius Platform New Features and Enhancements

## Dashboard

The following new features and enhancements were added to the Dashboards:

### Chart Enhancements

#### Sorting the Pivot Chart Table Visualization

The capability has been added to sort the [Pivot Chart Table](/docs/configuring-the-pivot-chart-table-visualization) visualization in the chart wizard, allowing users to order pivot table results by dimension or metric values. This improves data readability and speeds chart interpretation.

## Query Management

The following new features and enhancements were added to the Queries:

### Query Versioning

Users can now view and restore prior versions of a saved query. This helps users understand what changed in the query, when, and by whom - particularly useful for accidentally modified or broken queries. The restored version automatically propagates to all instances where the query is used - Dashboards, Reports, Enforcement Actions, and more. Users can also preserve version history of archived queries.

## &#x20;Enforcements

The following new features and enhancements were added to the Enforcements:

### Enforcement Action Run History Shows List of Assets

When an enforcement action fails, either in an enforcement set or as part of a workflow, a list of assets on which it failed is provided in the error message in the [run history](/docs/view-ec-set-history). Click **View Assets** to display the list in a new browser tab or the Copy icon to copy the error message for further investigation.

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/action_center/ECWF-FailedAssetsListViewAssets.png)

***

<br />

## New Adapters

* **[Fastly](https://docs.axonius.com/axonius-help-docs/docs/Fastly)** - Fastly is an edge cloud platform that provides content delivery, network acceleration, API security, DDoS protection and web application firewall services to process, deliver and secure traffic. (Fetches: Certificates)
* **[Hyland OnBase](https://docs.axonius.com/axonius-help-docs/docs/Hyland-Onbase)** - Hyland OnBase is an enterprise content management platform that provides document management, workflow automation, and case management functions. (Fetches: Users)
* **[LiveNX](https://docs.axonius.com/axonius-help-docs/docs/LiveNX)** - LiveNX is a network and application performance monitoring platform that provides end-to-end visualization, real-time analytics, and actionable insights for enterprise network infrastructure. (Fetches: Devices)
* **[TRIMEDX](https://docs.axonius.com/axonius-help-docs/docs/TRIMEDX)** - TRIMEDX is a healthcare technology management service that offers medical equipment management and maintenance solutions. (Fetches: Devices)

## Updated Adapters

* **[BigFix](https://docs.axonius.com/axonius-help-docs/docs/ibm-bigfix)** - Added the option to configure rate limiting (requests per second) in connection parameters.

* **[Black Duck](https://docs.axonius.com/axonius-help-docs/docs/Blackduck)** - This adapter now fetches Application Services.

* **[Black Kite V2](https://docs.axonius.com/axonius-help-docs/docs/black-kite-v2)** - Added configurable rate limiting.

* **[Custom Files](https://docs.axonius.com/axonius-help-docs/docs/Custom-Files)** - This adapter now fetches SaaS Applications.

* **[JumpCloud](https://docs.axonius.com/axonius-help-docs/docs/jumpcloud)** - Added an option to fetch system policy statuses per device.

* **[Kolide K2](https://docs.axonius.com/axonius-help-docs/docs/kolide-k2)** - The API version for this adapter was updated to [https://api.kolide.com/](https://api.kolide.com/).

* **[LogicMonitor](https://docs.axonius.com/axonius-help-docs/docs/logicmonitor)** - Refactored the advanced configuration options to allow users to select multiple sources for parsing the Host Name field, and prioritize them by order.

* **[ManageEngine ADManager Plus](https://docs.axonius.com/axonius-help-docs/docs/Manage-Engine-Admanager-Plus)**
  * Added the option to configure the product name to the adapters connection parameters.
  * Added the option to configure the asset domain to the adapters connection parameters.

* **[Microsoft Azure](https://docs.axonius.com/axonius-help-docs/docs/microsoft-azure)** - This adapter now supports authenticating with Managed Identity..

* **[Microsoft Defender for Endpoint (Microsoft Defender ATP)](https://docs.axonius.com/axonius-help-docs/docs/microsoft-defender-atp)** - Added the option to fetch Browser Extensions as Installed Software.

* **[Netshot](https://docs.axonius.com/axonius-help-docs/docs/Netshot)**
  * This adapter now fetches groups.
  * Added an option to fetch device groups from the Device Groups endpoint and thus create Group assets.

* **[Palo Alto Networks Cortex Xpanse](https://docs.axonius.com/axonius-help-docs/docs/palo-alto-networks-expanse-expander)** - Added the option to fetch confirmed vulnerabilities from external services.

* **[Palo Alto Networks Strata Cloud Manager](https://docs.axonius.com/axonius-help-docs/docs/Palo-Alto-Networks-Strata-Cloud-Manager)** - Added configuration for  nat rules.

* **[Rapid7 Insight AppSec](https://docs.axonius.com/axonius-help-docs/docs/Rapid7-Insight-Appsec)** - Added options to enrich Business Applications, Devices, and Domains & URLs with tags.

* **[Tenable.sc (SecurityCenter)](https://docs.axonius.com/axonius-help-docs/docs/tenablesc-formerly-securitycenter)** - Added the option to enable granular heavy fields selection.

* **[TruffleHog](https://docs.axonius.com/axonius-help-docs/docs/Trufflehog)**  - Added the option to fetch all locations (disabled by default), which can be enabled in the advanced config labeled "All Locations" (when enabled, disable the "Locations" option).

## New Enforcement Actions

* **[Tenable Vulnerability Management - Restart Agent](https://docs.axonius.com/axonius-help-docs/docs/tenable-io-restart-agent)** - Restarts Tenable unhealthy agents.
* [**WMI - Create or Delete DNS Records**](https://docs.axonius.com/axonius-help-docs/docs/wmi-create-or-delete-dns-records) - Creates or deletes DNS records (A, CNAME, PTR) in a Microsoft DNS Server.
* **[Wiz - Update Issues](https://docs.axonius.com/axonius-help-docs/docs/update-wiz-issues)** - Updates the status, notes, and resolution details of Wiz Issues.

## Updated Enforcement Actions

* **[Axonius - Deploy Files and Run Shell Command on Linux Assets](https://docs.axonius.com/axonius-help-docs/docs/run-linux-shell-command)** - Implemented correlation logic to update existing assets instead of creating new asset records, matching the behavior of the WMI adapter.

* **[Push Security - Add/Remove Group to User](/docs/push-security-alter-group-for-user)** - Added the capability to assign or remove multiple groups to or from a user instead of just one group at a time.

* **Recorded Future - Add or Remove Assets To/From Watchlist**
  * Added an option to set the Recorded Future entity type for watchlist entries.
  * Added the Axonius Field Mapping capability.

* **[WMI - Enrich Devices with DNS Records](https://docs.axonius.com/axonius-help-docs/docs/enrich-device-data-with-dns-records)**
  * Added optional configuration "Query A, CNAME, PTR and check consistency".
  * When enabled the EC will query the A, CNAME, PTR records for the query devices and check if the A-PTR values are consistent.

<br />