# Source: https://docs.axonius.com/docs/whats-new-in-axonius-708.md

# What's New in Axonius Asset Cloud 7.0.8

#### Release Date: September 7th 2025

These Release Notes contain new features and enhancements added in version 7.0.8.

* Read [**What's New in Axonius 7.0**](/docs/whats-new-in-axonius-700) to see all Axonius 7.0 features.

## SaaS Applications New Features and Enhancements

The following new features and enhancements were added to SaaS Applications:

### New Licenses Field

A new field was added to the [Licenses](/docs/licenses) page: **Currency**, which details the currency in which the license is priced. This field can be either of the following values: USD, EUR, GBP, or AUD.

## Axonius Platform New Features and Enhancements

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Enforcement Center Renamed to Action Center

The **Enforcement Center** was renamed to **Action Center**. Additionally, Its **Enforcements Sets** tab was renamed to **Enforcements**.

### Workflows

#### New Generic Webhook Events

Users can now define new webhook Events, a new feature that allows you to define and manage custom webhook events directly within Axonius. This functionality streamlines integration with custom APIs and third-party tools, simplifying the workflow setup process.

Key features include the ability to:

* Receive data from any external system via a webhook.
* Automatically parse incoming payloads in various formats, including JSON and form data.
* Dynamically extract specific fields for use in subsequent workflow nodes.

Users can create custom webhook events using the **Create Generic Webhook** wizard, accessible from two locations:

* The **Event** node's setup pane.
* **System Settings> External Events> Workflows Events**.

An **Event** node can then be configured with any user-defined **Generic Webhook Event**, in addition to predefined Axonius webhook events.

![GenericWebhookEvents.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GenericWebhookEvents.png)

### Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Adapter Interface

[Adapter Ingestion rules](/docs/setting-adapter-ingestion-rules) now support the **Ticket** and **Account** asset types, in addition to the already supported asset types.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**Amdocs TMF639 Inventory**](/docs/tmf-framework)
  * TMF Framework is a tool that provides a standardized approach to managing telecommunications services and operations. (Fetches: Devices)
* [**Docebo**](/docs/docebo)
  * Docebo is a learning management system that offers e-learning solutions for training and development. (Fetches: Devices, Users, Groups, Organizational Units, Permissions)
* [**MIND**](/docs/mind)
  * MIND is a data security platform that provides autonomous data loss prevention and insider risk management via AI-driven discovery, classification, and automated response. (Fetches: Devices)
* [**Nameshield**](/docs/nameshield)
  * Nameshield is a registrar and domain protection service that provides DNS management, domain monitoring, recovery, SSL certificates and DMARC security. (Fetches: Domains & URLs)
* [**Pipedrive**](/docs/pipedrive)
  * Pipedrive is a sales CRM tool that provides pipeline management and sales automation features. (Fetches: Users)

### Adapter Updates

The following adapters were updated:

* [**Auth0**](/docs/auth0) - Added the option to not fetch users that are not part of an organization.
* [**Cisco Prime**](/docs/cisco-prime) - Added the option to fetch network map images for access points.
* [**Citrix Application Delivery Management (ADM)**](/docs/citrix-adm-nitro) - Added the option to fetch Load Balancer Service Records as Devices.
* [**CrowdStrike Falcon**](/docs/crowdstrike-falcon) - Added the option to not fetch specified deployment types for devices.
* [**JFrog Xray**](/docs/jfrog-xray) - Added the capability to ignore artifacts with names matching the strings entered.
* [**LogicGate**](/docs/logicgate) - API Key was replaced by Client ID and Client Secret in the connection parameters.
* [**Microsoft Active Directory (AD)**](/docs/microsoft-active-directory-ad) - Added the option to fetch group customized attributes with WinRM.
* [**Microsoft Defender for Endpoint (Microsoft Defender ATP)**](/docs/microsoft-defender-atp) - Added the option to aggregate vulnerabilities from same software into one record.
* [**Microsoft Entra ID (formerly Azure Active Directory) and Microsoft Intune**](/docs/microsoft-azure-active-directory-ad) - Added the option to fetch activity usage data for Visio and Project apps.
* [**Ninja One (RMM)**](/docs/ninja-one-rmm) - Added the option to fetch device volume information.
* [**Rapid7 InsightVM**](/docs/rapid7-insightvm) - Added the option to specify a number of days to which device vulnerabilities are compared to determine if they were subsequently patched.
* [**SAP Ariba**](/docs/sap-ariba) - Added the option to fetch groups from the Master Data Retrieval API.
* [**ServiceNow**](/docs/servicenow) - The capability to configure JSON fields to appear in Basic view is now also supported for Tickets.
* [**StackRox**](/docs/stackrox) - Added multiple options to fetch assets from different endpoints.
* [**Ubiquiti Networks UniFi Controller**](/docs/ubiquiti-networks-unifi-controller) - Added the capability to enter a comma-separated list of special characters to remove from each device name that the adapter parses.
* [**VMware Carbon Black Cloud (Carbon Black CB Defense)**](/docs/carbon-black-cb-defense) - This adapter now fetches Users and User Roles (configurable via advanced settings).
* [**Workday**](/docs/workday) - This adapter now fetches user support roles as Roles.
* [**Zscaler Private Access (ZPA)**](/docs/zscaler-private-access)
  * This adapter now fetches Firewalls as assets.

  * Added different enrichment options to the App Connector Endpoint.

### New Enforcement Actions

The following new Enforcement Actions were added:

* [**Microsoft Entra ID (formerly Azure AD) - Update Windows Defender Security Intelligence**](/docs/azure-ad-update-windows-defender-security-intelligence) - Updates the Windows Defender Security Intelligence for selected devices.
* [**Add Pipedrive User**](/docs/add-pipedrive-user) - Adds a new Pipedrive user.
* [**Suspend Pipedrive User**](/docs/update-pipedrive-user) - Deactivates a Pipedrive user.
* [**VMware CB Cloud - Create User**](/docs/carbon-black-cb-defense-create-user) - Creates a user in VMware CB Cloud.
* [**VMware CB Cloud - Delete User**](/docs/carbon-black-cb-defense-delete-user) - Deletes a user in VMware CB Cloud.
* [**VMware CB Cloud - Assign Role to User**](/docs/carbonblack-defense-assign-role-to-user) - Assigns a role or removes a role to/from a VMware CB Cloud user.

### Updated Enforcement Actions

The following new Enforcement Actions were updated:

* [**Axonius Network Discovery - Scan**](/docs/network-scanner-scan) - Added the option to configure scan timeout.