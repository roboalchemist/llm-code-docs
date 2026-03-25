# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6147.md

# What's New in Axonius 6.1.47

#### Release Date: December 30th 2024

These Release Notes contain new features and enhancements added in version 6.1.47.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Adapter Advanced Settings

The following setting was added to the **Adapter Configuration** section in [**Advanced Settings**](/docs/advanced-settings):

* Added the capability to include assets within defined IPv4 or IPv6 address ranges (in addition to the existing excluding assets capability).

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Zafran**](/docs/zafran)
  * Zafran is a security platform that provides comprehensive attack surface management solutions. (Fetches: Devices, Vulnerabilities, SaaS Applications)

### Adapter Updates

The following adapters were enhanced:

* [**Airlock Digital**](/docs/airlock-digital) - Added support for cloud authentication.

* [**Amazon Web Services (AWS)**](/docs/aws-advanced-settings) - This adapter now fetches orphan EBS volumes as Disks asset type.

* [**Checkmarx SAST**](/docs/checkmarx-sast) - Added the option to parse applications as Devices.

* [**F5 BIG-IP iControl**](/docs/f5-big-ip-icontrol)
  * This adapter now fetches domains and URLs.
  * Added the option to fetch GTM WideIPs, GTM Pools, and GTM Servers.

* [**Microsoft Teams**](/docs/microsoft-teams) - This adapter now fetches Microsoft Teams groups as Groups asset type.

* [**Qualys Cloud Platform**](/docs/qualys-cloud-platform) - Added the option to to enrich Vulnerabilities with Qualys TruRisk score.

* [**Tenable.sc (SecurityCenter)**](/docs/tenablesc-formerly-securitycenter)
  * Added the option to fetch and parse secure boot status from plugins 34096, 34097, 34098.
  * Added the capability to filter software by plugin IDs 22869 and 20811

* [**Veeam**](/docs/veeam) - Added the option to ignore the prefix in the device name.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Google Workspace - Send Direct Message to a User**](/docs/google-mdm-send-dm-to-user) - Sends a message directly to users in Google Workspace.

* [**Jamf Pro - Lock Device**](/docs/lock-device) - Locks the user's device.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Microsoft Teams - Send Direct Message to Assets**](/docs/teams-send-dm-to-assets)
  * Added the option to send a direct message to the last user that used the asset. This option is usually related to device assets.
  * Added the option to send a direct message to the asset owner.  This option is usually related to device assets.
* [**Create Incident - PagerDuty**](/docs/create-incident-pagerduty) - Added the **Allow fields with multiple values in the field mapping** option that parses multiple Axonius values into one vendor field.
* \[**Google Workspace - Send Message**] was renamed to [**Google Workspace - Send Direct Message to a Space**](/docs/gsuite-send-message)