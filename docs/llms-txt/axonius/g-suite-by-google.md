# Source: https://docs.axonius.com/docs/g-suite-by-google.md

# Google Workspace (G Suite)  

## Overview

The **Google Workspace (formerly G Suite)** Adapter integrates Axonius with Google Workspace to collect visibility for users, devices, applications, configurations, and activities across the organization. By leveraging Google Workspace APIs and delegated administrative access, Axonius can inventory identity and SaaS assets, enrich security context, and support enforcement actions—while adhering to least-privilege access principles where applicable.

### Use Cases the Adapter Solves

The Google Workspace adapter helps organizations:

* Gain full visibility into users, devices, applications, and licenses in Google Workspace
* Track user access, roles, permissions, and group memberships
* Monitor OAuth applications, browser extensions, and SaaS integrations
* Audit security-relevant activities using Google Workspace audit logs
* Identify misconfigurations, over-privileged users, and unused licenses
* Enrich identity and SaaS posture data for risk analysis and compliance
* Enable enforcement actions such as suspending users, changing OUs, managing roles, or removing extensions

## Types of Assets Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Groups.svg) Groups | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Roles.svg) Roles | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Accounts_Tenants.svg) Accounts & Tenants | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Permissions.svg) Permissions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Rules.svg) Rules | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Software.svg) Software | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_settings.svg) Application Settings | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Licenses.svg) Licenses | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_extensions.svg) Application Extensions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Admin_Managed_Extensions.svg) Admin Managed Extensions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/User_initiated_extensions.svg) User Initiated Extensions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_keys.svg) Application Keys | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Activities.svg) Activities | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_resources.svg) Application Resources

## Before You Begin

### Authentication Methods

The **Google Workspace (G Suite)** adapter supports the following authentication method:

* **Service Account and Enable Domain-Wide Delegation**

### Required Permissions

<Tabs>
  <Tab title="Cyber Assets">
    These **read** privileges and scopes are required to fetch **Cyber Assets** into Axonius.

    <Columns layout="auto">
      <Column>
        **Required Privileges**

        * Users
        * Organizational Units
        * Devices
      </Column>

      <Column>
        **Required Scopes**

        * `admin.directory.user.readonly`
        * `admin.directory.orgunit.readonly`
        * `admin.directory.device.mobile.readonly`
        * `admin.directory.device.chromeos.readonly`
      </Column>
    </Columns>

    ***

    <Columns layout="auto">
      <Column>
        **Optional Privileges**

        * Chrome Management
        * Groups
        * Reports
      </Column>

      <Column>
        **Optional Scopes**

        * `admin.directory.device.chromebrowsers.readonly`
        * `admin.directory.group.readonly`
        * `cloud-identity.devices.readonly`
        * `admin.reports.usage.readonly`
        * `apps.groups.settings`
      </Column>
    </Columns>
  </Tab>

  <Tab title="SaaS Applications & Identities">
    To fetch **Axonius SaaS Applications** and **identity-related data**, authorize the following scopes with additional **read** privileges.

    <Columns layout="auto">
      <Column>
        **Additional Privileges**

        * Admin Roles
      </Column>

      <Column>
        **Required Scopes**

        * `admin.directory.customer.readonly`
        * `admin.directory.domain.readonly`
        * `admin.directory.rolemanagement.readonly`
        * `admin.directory.user.security`
        * `admin.reports.audit.readonly`
        * `calendar`
        * `cloud-identity.groups`
        * `chrome.management.reports.readonly`
        * `chrome.management.policy.readonly`
        * `chat.admin.spaces`
      </Column>
    </Columns>
  </Tab>
</Tabs>

## More Information About This Adapter

[Deploying the Google Workspace (G Suite) Adapter](/docs/google-workspace-deploying-the-adapter)

[Google Workspace Advanced Permissions](/docs/google-workspace-advanced-permissions)

[Google Workspace Advanced Settings](/docs/google-workspace-advanced-settings)

[Google Workspace Related Enforcement Actions](/docs/google-workspace-related-enforcement-actions)