# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6148.md

# What's New in Axonius 6.1.48

#### Release Date: January  5th 2025

These Release Notes contain new features and enhancements added in version 6.1.48.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Dashboard New Features and Enhancements

### Chart Enhancements

#### Refine the Data Displayed in the Asset Data Chart

The Data Refinement functionality is now accessible for fields in the [Asset Data Chart](/docs/asset-table-chart#refine-data), providing increased precision in defining the field values displayed. When users click the link to the relevant Asset table, it opens with the configured refinement applied, ensuring consistency with the chart’s configuration.

## Assets Pages

## Devices Page New Features and Enhancements

The following new features and enhancements were added to the **Devices**  page.

#### New Preferred Fields

* The following new Preferred fields were added to the  **Devices** page:
  * **Preferred OS: Code Name**.
  * **Preferred Latest Last Seen Adapter** - The full name of the adapter that provided the latest date for the last seen value.
  * **Preferred Earliest First Seen Adapter** - The full name of the adapter that provided the earliest date for the first seen value.

## Software Management Module New Features and Enhancements

The following new features and enhancements were added to the Software Management Module:

* **Preferred Software Name** and **Preferred Software Vendor** were added to the Installed Software table for users who have the Software Management module.
* **Preferred Software Name** and **Preferred Software Vendor** can be used as part of the Software Versions view on the Devices page.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### New Schedule Plan for Enforcement Sets

The new **Every scheduled adapter fetch** schedule plan option (in the **Select Schedule** tab of the **Create Enforcement Set** drawer) triggers the Enforcement Set run each time the selected adapter connection successfully completes a fetch.

![ScheduleadapterFetch](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ScheduleadapterFetch.png)

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**OX Security**](/docs/ox-security)
  * OX Security is a cybersecurity platform that offers comprehensive threat detection and response solutions. (Fetches: Business Applications, Alerts/Incidents)

### Adapter Updates

The following adapters were enhanced:

* [**1Password**](/docs/one-password) - Added support for service account authentication.
* [**AlgoSec Firewall Analyzer**](/docs/algosec-firewall-analyzer) - Added the option to fetch devices with Firewall Rules.
* [**Amazon Web Services**](/docs/aws-advanced-settings) - Added the option to populate the Cloud Provider Account Name field's value with the account name.
* [**BeyondTrust Password Safe**](/docs/beyondtrust-password-safe)
  * This adapter now fetches groups, activities, and application resources as assets.
  * Added the option to fetch user audits from the last 90 days as Activities.
  * Added the option to fetch secrets as resources.
* [**BigFix**](/docs/ibm-bigfix) - Added the option to disable dynamic parsing of the adapter.
* [**BMC Atrium ADDM**](/docs/bmc-atrium-addm) - Added the option to fetch installed software data in the background.
* [**Citrix Application Delivery Management (ADM)**](/docs/citrix-adm-nitro)
  * This adapter now fetches load balancers as assets.
  * Added the option to fetch Load Balancer data with `ns_lbvserver`.
* [**CyberArk Privilege Cloud**](/docs/cyberark-privilege-cloud)
  * Tenant ID was added to connection parameters.
  * Added the option to use ISPSS authentication.
* [**Cyberhaven**](/docs/cyberhaven) - Added support for API Version 2.
* [**Qualys Cloud Platform** ](/docs/qualys-cloud-platform) - Added the option to configure Posture Info fetch settings.
* [**SailPoint IdentityIQ**](/docs/sailpoint-iq)
  * Port was added to connection parameters.
  * This adapter now fetches roles and accounts/tenants.
* [**SharePoint**](/docs/sharepoint) - Added the option to select the API environment to login to - Public or Gov.
* [**Slack**](/docs/slack#advanced-settings) - Added the option to fetch roles.
* [**Trend Micro Vision One**](/docs/trendmicro-vision-one) - Added the option to disable the risky devices endpoint.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Microsoft MECM - Add or Remove Assets to/from Collection (PS-based)**](/docs/add-or-remove-device-in-sccm) - Adds devices to, or removes them from a collection using direct membership rules.

* [**Microsoft Entra ID (formerly Azure AD) - Update Mailbox Auto Reply Settings**](/docs/azure-ad-update-mailbox-auto-reply-settings) - Updates the Auto Reply settings of users in Entra ID.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Jira Service Management - Create Ticket**](/docs/create-jira-service-desk-ticket) - Added the capability to add a related parent ticket key.
* [**OpenCTI - Enrich Asset Data**](/docs/enrich-device-data-with-opencti) - Added the **Creator Names** and **Label** fields.