# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6151.md

# What's New in Axonius 6.1.51

#### Release Date: January 26th 2025

These Release Notes contain new features and enhancements added in version 6.1.51.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Dashboard Name Appears when Hovering Over a Browser Tab

When a dashboard is loaded in a browser tab, the name of the dashboard appears when hovering over the tab.

### Dashboard Navigation Enhancements

#### View Dashboard Queries Directly in the Query Wizard

When a user clicks on chart segments and links in Axonius dashboards, they can now [view the relevant query expression](/docs/chart-actions#view-results) directly in the Query Wizard. This makes it easier to explore and refine the data behind dashboard visualizations and provides greater flexibility and efficiency in asset data exploration.

### Chart Enhancements

#### 'Summary' Visualization Displays Metrics in Pivot Charts

Users can now select the ['Summary' visualization option](/docs/adv-pivot-chart#2-visualization) for Pivot charts to show a metric without selecting a dimension. This allows  users to create Dashboard charts that display one data point.

<Image alt="Summary_RN.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Summary_RN.png" />

## Assets Pages

### Rich Text Formatting for Notes on Asset Pages

Users can now [format notes in Asset pages](/docs/asset-profile-page#notes-tab) with bold, italics, underlines, custom font sizes, colors, and alignments. Users can also add links to notes. This allows for clearer, better-structured, and visually appealing Asset notes.

## Devices and Users Pages New Features and Enhancements

**Normalization Reasons**
Documentation for all possible Normalization Reasons that can populate the [Normalization Reasons Complex Field ](/docs/normalization-reasons-complex-field) was added to the documentation. Normalization Reasons are now listed on a separate page for your convenience.

## Adapter Pages and Adapter Interface New Features and Enhancements

### Create New SQL Adapters

[Create New Adapter](/docs/create-new-adapter) now supports creating adapters of the type SQL. Up to ten custom SQL adapters can be created.

### Clean Phase Improvements

Significant performance improvements were made to the Clean phase, it is now 90% faster.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### All Relationships are Created as Two-Way Relationships

When [creating a relationship](/docs/managing-custom-relationships) between asset types, users now define a relationship for both directions. For example, when creating a relationship between the asset types Devices and Users, two relationships are created and listed in the Relationships table. One for the relationship from Devices to Users and one for the relationship in the other "direction" from Users to Devices.

## Adapter and Enforcement Action Updates

### Adapter Updates

The following adapters were enhanced:

* [**Automox**](/docs/automox) - Added the option to enrich devices with server data from this endpoint: [https://developer.automox.com/openapi/axconsole/operation/getServerGroup/](https://developer.automox.com/openapi/axconsole/operation/getServerGroup/)

* [**Cisco Prime**](/docs/cisco-prime) - Added the option to fetch configuration files for each device.

* **[Cisco Umbrella](/docs/cisco-umbrella#advanced-settings)**- Added the option to skip the SaaS apps repository validation and parse all apps coming from the API.

* [**Cohesity**](/docs/cohesity) - Added the capability to authenticate using an API Key.

* [**Claroty CTD**](/docs/claroty) - Added the option to enrich device data with insight names.

* [**Dragos Platform**](/docs/dragos-platform) - Added support for Dragos Platform 2.4.x (by selecting API v4).

* [**FlexNet Manager Suite Cloud**](/docs/flexnet-manager-suite-cloud) - Added the option to enrich Flexnet software with data from ServiceNow.

* [**ImmuniWeb**](/docs/immuniweb)
  * Added the option to force parse the domains tab as Domains and URLs and as devices.
  * Added the option to parse the domains tab as a Domains and URLs entity only.

* [**Microsoft Active Directory (AD)**](/docs/microsoft-active-directory-ad) - Added the option to fetch Permissions.

* [**Ninja One (RMM)**](/docs/ninja-one-rmm) - Added a new authentication option - Authorization Code Authentication. When enabled, the adapter uses this option instead of the default Client Credentials Authentication.

* [**Palo Alto Networks Cortex XDR**](/docs/palo-alto-networks-cortex-xdr) - Added the option to use Cortex XDR in the Agent Versions Name.

* [**SailPoint IdentityNow**](/docs/sailpoint-identity-now) - Added the option to parse all the attributes and ignore the **List of private account attributes to include** configuration list.

* **[SailPoint Identity Manager](/docs/sailpoint#advanced-settings)** - Added the capability to fetch users from public identities.

* [**ServiceNow**](/docs/servicenow)
  * Added the option to filter out sub-tables of devices from the fetch.
  * Added the option to fetch `cmdb_software_product_model` table for adapters that support device software enrichment.

* [**VMware SD-WAN**](/docs/vmware-sd-wan) - Added the option to enrich edge devices with profile settings data.

* **[Zoom](/docs/zoom#permissions)** - The adapter can now fetch more License data without requiring a Zoom user name and password.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**AssetSonar - Update Asset**](/docs/update-sonar-asset) - Added support for sending complex object fields data, selected from the Field Mapping Wizard.
* [**HTTP Server - Send to Webhook per Asset**](/docs/send-to-webhook-per-asset) - Added an optional "API key for authorization" field.
* [**Splunk - Create and Update Assets**](/docs/splunk-create-and-update-assets) - Added the option to map Axonius fields to Splunk IDs.