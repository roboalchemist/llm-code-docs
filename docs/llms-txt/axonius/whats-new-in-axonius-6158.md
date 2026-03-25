# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6158.md

# What's New in Axonius 6.1.58

#### Release Date: March 16th 2025

These Release Notes contain new features and enhancements added in version 6.1.58.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Chart Enhancements

#### Customize the Label for the 'Segment by' Field in the Field Segmentation Chart

When Table view is selected for the [Field Segmentation chart](/docs/field-segmentation-chart), users can edit the label for the 'Segment by' field in the chart configuration. This provides increased flexibility in the way data is presented in the chart's table visualization.

![FIeldSegmentation\_EditFieldName.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FIeldSegmentation_EditFieldName.png)

## Assets Pages

The following features were added to all assets pages:

### Improved Display of Contents for Fields With Long Values from the Asset Table

When a user hovers over a field in the Asset table that contains a long text value, the contents are displayed in a pop-up that includes a button to copy the text.

![LongTextHover.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/LongTextHover.png)

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### New Field for DeepMac Enrichment

While enabling the **MAC address metadata enrichment (DeepMac)** configuration in the **Enrichment Settings** page, a new **Company Name** field is added to the enrichment fields.

### Gateway for HTTPS Logs

A gateway can now be configured for [HTTPS logs](/docs/configuring-https-log-settings).

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Brex**](/docs/brex)
  * Brex is a financial technology platform that offers corporate credit cards and expense management solutions. (Fetches: Expenses, SaaS Applications)
* [**threatER**](/docs/threater)
  * threatER is a platform that provides real-time threat intelligence and response capabilities. (Fetches: Users)

### Adapter Updates

The following adapters were updated:

* [**Bishop Fox**](/docs/bishop-fox-adapter)
  * This adapter now fetches domains and URLs as assets.
  * Added the option to not fetch devices of the subtype 'domains' from the Devices from Domains endpoint.
  * Added the option to not fetch devices of the subtype 'targets' from the Devices from Targets endpoint.
  * Added the option to fetch URLs of the subtype 'domains' from the URLs from Domains endpoint.
  * Added the option to fetch URLs of the subtype 'targets' from the URLs from Targets endpoint.

* [**Cherwell IT Service Management**](/docs/cherwell) - Added the option to fetch business applications as assets.

* [**Cisco Meraki**](/docs/cisco-meraki) - Added the option to select the source data for hostname parsing.

* [**ConnectWise Automate**](/docs/connectwise) - Client\_id was removed from connection parameters.

* [**Kaseya VSA**](/docs/kaseya-vsa)
  * Added the option to not enrich devices with software.
  * Added the option to not enrich devices with group members.

* [**Lansweeper**](/docs/lansweeper) - Added the capability to specify which TDS Driver version to use, either 7.0 or 8.0.

* [**Microsoft Azure**](/docs/microsoft-azure) - Added the option to fetch Policy Set Definitions to the list of Azure services that the user can fetch as assets.

* **Microsoft Entra ID (Azure AD) and Microsoft Intune** - Added the option to fetch device local credentials (LAPS) from BETA Graph API to fetch and parse the Password field.

* [**Palo Alto Networks Panorama**](/docs/palo-alto-networks-panorama)
  * Added the capability to enter a list of CIDRs to be considered internal/private.
  * Added the capability to Panorama addresses to be considered internal/private.

* [**Panorays**](/docs/panorays) - Added the capability to filter which suppliers to fetch by portfolio name.

* [**PingFederate**](/docs/pingfederate) - Added the option to fetch OAuth clients.

* [**Sectigo**](/docs/sectigo) - Added the option to fetch device certificates.

* [**Securonix SNYPR**](/docs/securonix-snypr)
  * This adapter now fetches alerts/incidents as assets.
  * Added the option to not fetch devices.
  * Added the option to not fetch users.
  * Added the option to fetch incidents from events.
  * Added the capability to filter resource group names from the incidents fetch.

* [**SharePoint**](/docs/sharepoint) - Added the option to fetch site user roles when fetching site permissions.

* [**Splunk** ](/docs/splunk)
  * This adapter now fetches Business Applications as assets
  * Added the capability to specify a comma-separated list of Splunk search macro names that provide business application information.

* [**Tenable.io**](/docs/tenableio) - Added the option to fetch assets with Plugin ID 93561 as Containers.

* [**Workday**](/docs/workday) - Added the option to fetch the report for each year in the defined time range.

* [**Zafran**](/docs/zafran) - Added the capability to specify the maximum number of minutes to wait for the Vulnerabilities export to finish before giving up and continuing to the Devices fetch.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Axonius - Enrich Physical Location**](/docs/axonius-enrich-physical-location) - Enriches devices returned by the selected query or selected on the relevant asset page with their full addresses, based on longitude and latitude data.
* [**Qualys - Remove IPs from Asset Group**](/docs/en/qualys-remove-ips-from-asset-group) - Removes all Axonius IP addresses from a Qualys asset group.