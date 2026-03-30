# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6153.md

# What's New in Axonius 6.1.53

#### Release Date: February 9th 2025

These Release Notes contain new features and enhancements added in version 6.1.53.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Clearer Destination Selection for Charts and Reports

When [moving or copying a chart](/docs/chart-actions#move-or-copy), or [adding a chart/dashboard to a report](/docs/report-configuration-page), the selection menu now includes the full folder path. This helps users select the correct dashboard, especially if there are dashboards that have the same name.

## Assets Pages

### SaaS Management New Features and Enhancements

**Define Time Frame for Determining Users' Status as Active or Inactive**
Control when SaaS Application users are marked as 'Inactive`in SaaS Management with the new ['Set SaaS Management active user definition'](https://docs.axonius.com/docs/configuring-data-aggregation-settings) setting (**Data`>` Data Aggregation**). This allows administrators to define the number of days after a user`s last access to a SaaS application before their status changes to 'Inactive' as reflected in all relevant fields across the SaaS Management module.

**New Application and User Extension 'Association Scope' Field**
The new 'Association Scope' field shows if an [Application Extension](/docs/application-extensions#static-fields) or a [User Extension](/docs/user-extensions#user-extension-fields) is for a specific user, a group, or all users.

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Fetch Connection

* A separate **Fetch connection** permission was added in **Adapter Settings**.
* A **Fetch** button was added to the **Adapter Profile** page.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Updating Roles Keeps Users Logged In

When updating permissions for [roles](/docs/role-based-access-control-rbac-management), users now remain logged in unless the new permission now excludes the current action being taken.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Acunetix Premium**](/docs/acunetix-premium)
  * Acunetix Premium is an automated web application security tool that identifies and analyzes vulnerabilities in web applications and APIs. (Fetches: Business Applications)
* [**BIND**](/docs/bind-dns-adapter)
  * BIND is a DNS server software that provides domain name resolution and management services. (Fetches: Devices)
* **Custom Files**
  * The Custom File adapter imports .csv/.json files with inventory information, including device  and user data. (Fetches: Devices, Users, Vulnerabilities, Software, SaaS Applications)
* [**Outreach**](/docs/outreach)
  * Outreach is a sales engagement platform that provides automation and analytics for sales teams. (Fetches: Users)

### Adapter Updates

The following adapters were updated:

* [**Amazon Web Services (AWS)**](/docs/amazon-web-services-aws) - Added the option to fetch EFS assets as File Systems.

* [**Cisco Identity Services Engine (ISE)**](/docs/cisco-identity-services-engine-ise)
  * This adapter now fetches users.
  * Added the option to fetch internal users.
  * Added the option to fetch guest users.

* [**Cisco Meraki**](/docs/cisco-meraki) - Added the option to fetch alerts/incidents (if **Fetch Air Marshal data** is selected in Advanced Settings).

* **[Github](/docs/github#advanced-settings)** - Added the option to set the number of organizations concurrently fetched by the adapter.

* [**Have I Been Pwned**](/docs/have-i-been-pwned) - Added the option to enrich users with stealer logs.

* [**Imperva Data Activity Monitoring (DAM)**](/docs/imperva-data-activity-monitoring-dam) - Added the option to fetch DAS Assessment Run DBS.

* [**Intel 471**](/docs/intel-471) - This adapter's name was changed to **Intel 471 Enrichment**. It now fetches only Vulnerabilities and runs a CVE Enrichment process on them.

* [**Ivanti Unified Endpoint Manager (Landesk)**](/docs/ivanti-unified-endpoint-manager) - Added the option to use short name instead of full name for service complex field.

* **[Jamf Pro](/docs/jamf-pro#advanced-settings)** - Updated the 'Fetch Users' option to fetch users for both Classic and Pro API connections.

* [**ManageEngine Mobile Device Management**](/docs/manageengine-mdm) - Port was added to connection parameters.

* [**Monday**](/docs/monday) - Added support for API version 2024-10.

* [**Qualys Cloud Platform**](/docs/qualys-cloud-platform)
  * Added the option to fetch ignored and disabled Detections.
  * Added the option to fetch Agent platform’s latest version.

* [**ServiceNow**](/docs/servicenow) - Added the capability to filter out sub-tables of assets from the fetch.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**CyberArk Alero - Delete User**](/docs/delete-cyberark-alero-user) - deletes CyberArk Alero users.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Axonius - Enrich DNS Custom Data**](/docs/add-dns-custom-data) - This Enforcement Action can now be used to enrich Domains and URLs, in addition to Devices.
* [**Axonius Network Discovery - Scan**](/docs/network-scanner-scan) -  The certificate data fetch in this Enforcement Action now supports only Background Fetch.
* **[Slack - Send Message via Webhook](/docs/send-slack-message#additional-fields)** - Added the option to set the color for the text of the message.
* **[Slack - Send Message to Channel](/docs/slack-send-message-to-channel)** - Added the option to set the color for the text of the message.