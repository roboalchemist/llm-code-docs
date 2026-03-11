# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6150.md

# What's New in Axonius 6.1.50

#### Release Date: January  19th 2025

These Release Notes contain new features and enhancements added in version 6.1.50.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Assets Pages

The following features were added to all assets pages:

### Query Wizard Enhancements

### Share an Asset Page using "Copy Link with Query"

Users can now [copy a query link](/docs/saved-queries-devices#sharing-a-query-wizard-expression-url) in order to share an asset page. The generated link opens the Query Wizard with all the query details populated - assets, fields, and data refinement. The link acts as a temporary saved query and is available for 30 days.

### Run a Query Directly From the Assets Page URL

Users can now enter an Axonius Query Language (AQL) expression into the URL of an Assets Page and instantly [run a query with that expression](/docs/query-wizard-and-query-filter#running-a-query-directly-from-the-assets-pages-url) to search within the Assets Page.

## Devices  Page New Features and Enhancements

The following new features and enhancements were added to the **Devices**  page.

### EOL/EOS and Latest Version Support for Additional Operating Systems

Devices in Axonius [now support](/docs/devices-page#os-end-of-life-end-of-support-and-latest-os-version) End of Life, End of Support, Latest Version, and Is Latest Version for the following operating systems:

* CentOS Stream

* FreeBSD

* Rocky Linux

* Debian

* Oracle Linux

* IBM AIX

## SaaS Management New Features and Enhancements

#### New SaaS Applications Enrichment Fields: 'Excessive Write Permissions' and 'Excessive Read Permissions'

The following [new enrichment fields](/docs/saas-applications#enrichment-fields) were added to SaaS Applications:

* **Excessive Write Permissions** - The application's user extensions with Write permissions.

* **Excessive Read Permissions** - The application's user extensions with Read permissions.

## Cloud Asset Compliance New Features and Enhancements

[CIS AWS Foundations Benchmark](/docs/cloud-asset-compliance-page) v 3.0.0 is now supported.

## Adapter and Enforcement Action Updates

### Adapter Updates

The following adapters were enhanced:

* [**Dell iDRAC**](/docs/idrac) - Added the option to use SKU as a serial number.
* [**Docusign**](/docs/docusign#parameters) - Added the option to fetch Docusign CLM Licenses to enrich users with permission profiles.
* [**Exabeam Cloud**](/docs/exabeam-cloud)
  * Added the capability to select fields to fetch from the API.
  * Added the capability to select one field to use as the device hostname source.
* [**Google Cloud Platform (GCP)**](/docs/google-cloud-platform-gcp) - Added the option to exclude user data from the fetch.
* [**GoDaddy**](/docs/godaddy)
  * Added the option to include domains without a public IP.
  * Added the capability to specify the DNS server IP to use for translating a hostname to IP.
* [**Hyperview DCIM**](/docs/hyperview-dcim) - Added the capability to enrich the assets endpoint with the following endpoints: IP Properties, Host Properties, Asset Properties, Asset Summaries, Asset Lifecycle.
* [**LogicMonitor**](/docs/logicmonitor) - Added the option to parse OS information from 'system.collectorplatform' if "hp" appears in 'system.sysinfo'.
* [**Microsoft Azure** ](/docs/microsoft-azure)
  * Added the option to enter Azure management group IDs in the connection configuration, so the adapter will only fetch data from subscriptions associated with the specified management groups.
  * The adapter now supports parsing a comma-separated list of tags as asset tags for all asset types.
* **[Ping Federate](/docs/pingfederate)** - Added the option to set this adapter as an SSO provider.
* [**PRTG Network Monitor**](/docs/prtg-network-monitor) - Added the option to parse the hostname from the 'host' field. This setting will only apply if the value in the ‘host’ field is not recognized as an IP address.
* [**Schneider Electric EcoStruxure IT Advisor**](/docs/schneider-electric-ecostruxure) - Added the capability to fetch devices of various subtypes from the following endpoints: Blades, Server, Blade Enclosure, Network, Switch Enclosure.
* [**SecurityScorecard**](/docs/securityscorecard) - Added the option to parse the “Last Seen” value of the device from the latest “Findings: Last Seen Time”.
* [**Silverfort**](/docs/silverfort) - Policy API Key was added to connection parameters.
* [**Splunk**](/docs/splunk) - Added the capability to select a Splunk time zone to adjust the value last seen.
* **[Workday](/docs/workday#advanced-settings)**
  * Added the option to fetch workers filtered by organization.

  * Added the option to specify a list of custom IDs for workers that you want to fetch.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Sumo Logic SIEM - Send Activities to SumoLogic SIEM**](/docs/sumo-logic-siem-send-json-to-http-logs) - Sends Activities data to Sumo Logic via HTTP connection.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Microsoft Entra ID (formerly Azure AD) - Assign Group to Users**](/docs/assign-azure-ad-group-to-user) - Added the option to run the enforcement action only on assets from the query result that are from the selected adapter connection.
* [**Okta - Update User**](/docs/update-okta-user) - Optional input fields were added that the user can use to update user data. Required custom fields defined for user profiles are dynamically added to the Enforcement Set configuration.
* [**Logout User - OneLogin**](/docs/logout-user-onelogin) - Added the capability to enter a comment text to add event data to the user record, append the comment to the existing text or replace it, and add the date and time of the comment. Note that this capability was added to all OneLogin Enforcement Actions.