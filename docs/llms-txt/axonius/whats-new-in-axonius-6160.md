# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6160.md

# What's New in Axonius Asset Cloud 6.1.60

#### Release Date: March 30th 2025

These Release Notes contain new features and enhancements added in version 6.1.60.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## SaaS Applications New Features and Enhancements

The following new features and enhancements were added to SaaS Applications:

### Updated Behavior for the 'Generated From' SaaS Applications Field

For SaaS Applications generated from IDP, Admin consent, and Bookmark extensions, the 'Generated from' field value will be 'Admin Extensions'. For applications generated from Application extensions, the value will be 'Non-Admin Extensions'.

**Asset Name Updates**

* The Application Extension page was renamed 'All Application Extensions'
* The User Extensions page was renamed 'All Application Extension Instances'

## Axonius Platform New Features and Enhancements

### Assets Pages

The following features were added to all assets pages:

### Query Wizard Enhancements

### Access Saved Query Details From Query Wizard

When a user selects a saved query in the Query Wizard, they can open a drawer with details about that query.

![ViewQueryDetails.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ViewQueryDetails.png)

### Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Adapter Interface

#### New Adapter Ingestion Rule Post Action Options

It is now possible to use **key\_exists** and **key\_not\_exists** operators in the [post action](/docs/setting-adapter-ingestion-rules#performing-post-action-only-if-field-value-exists-not-exists) of an ingestion rule. This causes the post action to be performed on the asset only if a value exists or does not exist in the specified field (key).

## System Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Precise User-Device Matching

A new setting lets users control how Axonius associates users with devices. When enabled, Axonius matches user names to email address identifiers (for example, 'john.doe' to '[john.doe@domain.com](mailto:john.doe@domain.com)'). When disabled, Axonius only associates users with devices that have matching full user names, and will not extract the email identifier as a new identifier.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Run Priority

The maximum number of run priorities that can be assigned to Enforcement Sets, scheduled for every global discovery cycle, has increased from 20 to 200, allowing for finer control over the run order.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**CimTrak**](/docs/cimtrak)
  * CimTrak is a file integrity monitoring tool that provides real-time detection of unauthorized changes to critical files. (Fetches: Devices)

### Adapter Updates

The following adapters were updated:

* [**Abnormal Security**](/docs/abnormal-security) - This adapter now fetches alerts/incidents as assets.
* [**AssetSonar**](/docs/asset-sonar) - Added the option to limit the number of API requests per minutes.
* [**CrowdStrike Falcon**](/docs/crowdstrike-falcon) - Added the option to skip the parsing of containers.
* [**CrowdStrike Falcon Identity Protection (Preempt)**](/docs/preempt) - Added the option to exclude devices that have IPs as Hostname.
* [**ExtraHop Reveal(x) 360**](/docs/extra-hop-360) - Added the option to parse dhcp\_name as an alternate source for hostname.
* [**Google Sheets**](/docs/google-sheets) - Added the option to fetch URLs and domains from a spreadsheet.
* [**Huawei eSight 21.x**](/docs/huawei-esight-21) - Added support for Version 10 authentication.
* [**Lansweeper Cloud**](/docs/lansweeper-cloud) - Added the option to disable OS data parsing.
* [**Microsoft Azure**](/docs/microsoft-azure#parameters) - Added the option to authenticate the adapter connection with a certificate to Microsoft Azure.
* [**NetBox**](/docs/netbox) - Added the option to fetch IPAM Prefixes as Network assets.
* [**Nextcloud**](/docs/nextcloud) - User Name was added to connection parameters.
* [**Oracle NetSuite**](/docs/netsuite) - Updated supported algorithms in Private Key Algorithm parameter.
* [**Qualys Cloud Platform**](/docs/qualys-cloud-platform) - Added the option to parse only admins as Last Logged Users.
* [**Rapid7 Nexpose and InsightVM**](/docs/rapid7-nexpose) - Added the option to parse Proof and Key rich text fields for Vulnerabilities.
* [**SentinelOne**](/docs/sentinelone) - Added the option to parse the device model field without the manufacturer information in the model name.
* **[Snowflake Data Warehouse](/docs/snowflake#advanced-settings)**
  * Added the option to fetch warehouses
  * Added the option to fetch database assets as application assets and to select which database assets to fetch.
  * Added the option to select fetch Identity assets
* [**Zscaler Web Security**](/docs/zscaler-web-security#advanced-settings) - Added the option to filter the SaaS Apps report by time period.