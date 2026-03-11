# Source: https://docs.axonius.com/docs/salesforce.md

# Salesforce

Salesforce is a customer relationship management solution that gives a single, shared view of every customer.

## Use Cases the Adapter Solves

The Salesforce adapter can be used for:

* **User management** - Review users’ statuses, permissions, and activity. identify gaps in offboarding users and in user access levels.
* **Security management** - Find misconfigurations that pose security and compliance risks.
* **Cost optimization** - Identify cost optimization opportunities.

## Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_extensions.svg) Application Extensions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Admin_Managed_Extensions.svg) Admin Managed Extensions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/User_initiated_extensions.svg) User Initiated Extensions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_Add-ons.svg) Application Add-On | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Roles.svg) Roles | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Groups.svg) Groups | Licenses | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_settings.svg) Application Settings | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_Extension_Instances.svg) Application Extension Instances | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Admin_Managed_Extension_Instances.svg) Admin Managed Extension Instances | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/User_initiated_extensions_instances.svg) User Initiated Extension Instances | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_Add-on_instances.svg) Application Add-On Instances | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_keys.svg) Application Keys | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Activities.svg) Activities | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/organizational_units.svg) Organizational Units | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Accounts_Tenants.svg) Accounts/Tenants | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_resources.svg) Application Resources

Some asset types require to enable specific [advanced settings](https://docs.axonius.com/axonius-help-docs/docs/salesforce-advanced-settings) to fetch them.

## APIs

Axonius uses the [Salesforce API](https://developer.salesforce.com/docs/).

## Authentication Methods

To connect to the Salesforce adapter, choose between the following authentication flows. Each flow can be used to fetch all asset types.

* Client Credentials Flow
* Username-Password Flow

## Permissions

<Callout icon="📘" theme="info">
  **Note**

  Only a System Administrator can configure permissions in Salesforce.
</Callout>

<Accordion title="General" icon="fa-info-circle">
  Navigate to **Setup** `>` **Users** `>` **Permission Sets** (or **Profiles**), and assign the following permissions:

  * Every permission listed in the General User section starting with the word "View" **except for View Encrypted Data**
  * Lightning Experience User
  * API Enabled

    <Callout icon="📘" theme="info">
      **Note**

      The API Enable permission is required even if you're using Bulk API. Note that some organizations might require specific Bulk API permissions for large-scale data sets and operations.
    </Callout>
  * Manage IP addresses
  * Manage Login Access Policies
  * Manage Password Policies
  * Manage Profiles and Permissions Sets
  * Manage Roles
  * Manage Sandboxes
  * Manage Sharing
  * View All Profiles
  * View All Users
  * Apex REST Services
  * Manage Users
  * Manage Connected Apps
  * Modify Metadata Through Metadata API Functions
  * Customize Application
  * Is Single Sign-On Enabled
  * Use Any API Client (might be required if you're not using an admin-approved, allow-listed app)
</Accordion>

<Accordion title="Special Permissions" icon="fa-info-circle">
  Some data types require additional, specific permissions. Assign the following permissions if these data types are relevant to you:

  * View Event Log Files: required to fetch event monitoring data.
  * Query All Files: required to search and fetch all files (`Content`) across the organization, regardless of individual sharing.
  * View Setup and Configuration: required to fetch metadata or information about the organization structure.
</Accordion>

<Accordion title="Fetching Application Settings and Licenses" icon="fa-info-circle">
  Additional permissions are required to fetch these asset types.

  * The Salesforce user created for Axonius must have the System Permission Level.
  * In Salesforce, configure the following:

    1. Go to **Administration**, expand the **Users** tab and select **Permissions Sets**.
    2. Disable **Access Salesforce.com only through a Salesforce.com API**.

    <Callout icon="📘" theme="info">
      **Note**

      While to access Application Settings data you need to grant roles and/or permissions that include write capabilities, the adapter only actually reads from the application.
    </Callout>
</Accordion>

## Summary of Adapter Setup

To successfully deploy the adapter in Axonius, follow these steps:

1. **In Salesforce:**
   1. [Enable delegated authentication](https://help.salesforce.com/s/articleView?id=000386846\&type=1)  in your Salesforce environment.
   2. [Set up authorization](https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/CR_quickstart_oauth.htm).
   3. [Manage API Access](https://help.salesforce.com/s/articleView?id=xcloud.security_api_access_control_about.htm\&type=5) and ensure the Salesforce user created for Axonius has the API Access Administrator role.
   4. Create a User Account and a User Profile with the appropriate permissions to fetch assets.
   5. Configure Axonius as an External Client App.
   6. Retrieve the **Consumer Key** and **Consumer Secret**, required for authentication.
2. **In Axonius**:
   1. Connect the adapter using the Client Credentials or Username-Password flow.
   2. Test your credentials to make sure they work for fetching Salesforce data.
   3. *(Optional)* Configure the adapter's Advanced Settings according to the asset types you want to fetch.

See detailed instructions for each step on the next pages:

[Deploying the Salesforce Adapter in Axonius](https://docs.axonius.com/axonius-help-docs/docs/deploying-the-salesforce-adapter-part-1)

[Salesforce Advanced Settings](https://docs.axonius.com/axonius-help-docs/docs/salesforce-advanced-settings)

[Salesforce Enforcement Actions](https://docs.axonius.com/axonius-help-docs/docs/salesforce-enforcement-actions)