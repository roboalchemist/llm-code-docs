# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6169.md

# What's New in Axonius Asset Cloud 6.1.69

#### Release Date: June 8th 2025

These Release Notes contain new features and enhancements added in version 6.1.69.

<Callout icon="📘" theme="info">
  Note

  The content of this version will be deployed as part of version 6.1.70.
</Callout>

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Axonius Platform New Features and Enhancements

### Query Management New Features and Enhancements

The following new features and enhancements were added to the Queries:

### Managing Data Refinement from the Query Drawer

Users can now manage data refinement for assets not only from the Assets page, but also from the Saved Query drawer. A **Field Refinement** section was added to the Saved Query drawer, where users can see the refinement criteria. In addition, when the drawer is in editing mode, users can navigate directly to the **Refine Data** dialog to edit the refinement.

<Image alt="RefineQuery" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-EHEUD99P.png" />

## General Updates

### Improved Browser Printing for Axonius Screens

When using a browser's Print function to print an Axonius screen, it now prints the complete screen, including areas that require vertical scrolling, such as drawers and long configuration pages.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

The following update was made to the Dynamic Value statement functionality:

#### New Functions and Operators

The following function can now be used in a Dynamic Value statement:

* **title\_case**
  * The new *title-case* function transforms a string in a designated field into title case. For example, 'john doe' becomes 'John Doe'.
    Syntax: **title\_case**(\[adapter.field])

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Palo Alto Networks Prisma Access Insights**](/docs/paloalto-prisma-access-insights)
  * Prisma Access Insights is a monitoring tool that provides visibility into network traffic and security events. (Fetches: Devices, Users, Applications, Alerts/Incidents)

### Adapter Updates

The following adapters were updated:

* [**Bastazo**](/docs/bastazo) - This adapter now enriches CVE information.

* [**BigFix Compliance Analytics (formerly SCA)**](/docs/bigfix-sca) - Added the option to add custom property numbers to fetch.

* [**Bind**](/docs/bind-dns-adapter) - Added a mechanism to allow customers to specify a pattern to replace in their Amazon S3 bucket URL.

* [**Cisco Identity Services Engine (ISE)**](/docs/cisco-identity-services-engine-ise) - Added the option to enrich endpoint devices with the policy name.

* [**Eracent**](/docs/eracent) - Added the option to fetch installed software for devices.

* [**F5 BIG-IQ Centralized Management**](/docs/f5-big-iq-centralized-management) - This adapter now fetches Pool Members as Devices.

* [**Lacework**](/docs/lacework)
  * This adapter now fetches compute images as assets.
  * Added the option to fetch compute images from the Images endpoint (`api/v2/Entities/Images/search`).

* [**Palo Alto Networks IoT Security (Zingbox)**](/docs/paloaltonetworks-iot) - Added the option to fetch device details.

* [**Rapid7 Nexpose and InsightVM**](/docs/rapid7-nexpose) - The "Do not parse Host Name for IP values" advanced setting now also applies to the Secondary Host name field.

* [**Rapid7 Nexpose Warehouse**](/docs/rapid7-nexpose-warehouse) - Added the option to send an email report containing a CSV file of dropped assets.

* **[ServiceNow](/docs/servicenow)** - A dropdown in Advanced Settings (Advanced Configuration section) was added that allows the user to select one or more asset types. After the asset types are selected, the relevant advanced configurations are displayed. Advanced Configuration is divided into subcategories to make finding relevant settings easier. In addition, advanced configurations now have a description in a tooltip that provides information such as asset types, permissions, description, and more.

* [**Site24x7**](/docs/site24x7) - Added the option to fetch and fill monitor tags.

* [**Splunk**](/docs/splunk) - Added the capability to enter a query to parse browsed applications from web activity logs.

* [**Tenable.Vulnerability Management**](/docs/tenableio) - The name of the **Tenable.io** adapter was changed to **Tenable Vulnerability Management**. The names of all related Enforcement Actions were also changed.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Axonius - Run Linux SSH Scan**](/docs/run-linux-ssh-scan) - Added the option to set up connectivity timeout.
* [**Rapid7 - Add IP Addresses to Site**](/docs/add-ips-to-rapid7-insightvm-site) - Added the option to include CIDRs.