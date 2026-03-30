# Source: https://docs.axonius.com/docs/microsoft-azure-active-directory-ad.md

# Microsoft Entra ID (Azure AD) and Microsoft Intune

## Overview

**Microsoft Entra ID (Azure AD) and Microsoft Intune** are cloud-based Identity and Access Management (IAM) services providing secure authentication, Single Sign-On (SSO), Multi-Factor Authentication (MFA), and access control to Microsoft 365, Azure services, and enterprise applications. Entra ID helps organizations manage users, groups, devices, and application access while enabling security features like conditional access and identity protection.

### Use cases the adapter solves

Connecting Microsoft Entra ID and Intune to Axonius allows you to gain full visibility into users, devices, groups, and applications in your environment. Using this adapter, you can:

* Identify devices missing required security or monitoring agents.
* Detect devices excluded from vulnerability assessments.
* Evaluate user and group permissions.
* Analyze application permissions and configuration data.
* Monitor identity, device, and application activity for compliance and security purposes.

## Types of Assets Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Software.svg) Software | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_extensions.svg) Application Extensions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Admin_Managed_Extensions.svg) Admin Managed Extensions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/User_initiated_extensions.svg) User Initiated Extensions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_Add-ons.svg) Application Add-On | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Roles.svg) Roles | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Groups.svg) Groups | Licenses | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_settings.svg) Application Settings | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_Extension_Instances.svg) Application Extension Instances | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Admin_Managed_Extension_Instances.svg) Admin Managed Extension Instances | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/User_initiated_extensions_instances.svg) User Initiated Extension Instances | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_Add-on_instances.svg) Application Add-On Instances | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_keys.svg) Application Keys | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Activities.svg) Activities | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/organizational_units.svg) Organizational Units | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Accounts_Tenants.svg) Accounts/Tenants | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Secrets.svg) Secrets | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Certificates.svg) Certificates | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Permissions.svg) Permissions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Configurations.svg) Configurations

## Data Retrieved from Microsoft Entra ID (Azure AD) and Microsoft Intune

* **Devices**: Device name, ID, join type (hybrid/Azure), compliance status, OS details, last sign-in, BitLocker config (Windows), owner attributes, mobile device management data.
* **Users**: UPN, display name, email, group/role memberships, licenses, sign-in activity, authentication methods, manager info, photo (optional), custom attributes, mailbox usage.
* **Groups**: Group metadata, memberships, types (security/dynamic), assigned licenses.
* **Software and Extensions**: Installed applications, browser extensions, custom security attributes.
* **Configurations and Permissions**: Conditional Access policies, roles/assignments, audit logs, application settings, service principal details.
* **General Fields**: Last sign-in timestamp, activity logs, real-time updates (if enabled).

<Callout icon="📘" theme="info">
  **Note**:

  * **Last Seen** based on sign-in or status change timestamps.
  * Custom attributes fetched via beta APIs (if enabled).
  * SaaS data includes user extensions and audit logs for compliance tracking.
</Callout>

## Before You Begin

### Authentication Methods

The adapter can be connected using one of the following authentication methods:

* **Enterprise Application (Client ID / Client Secret)** – Recommended for standard connections.
* **Enterprise Application (Certificate)** – Recommended for certificate-based authentication.
* **OAuth** – Supports delegated access and user approval flows.
* **Username / Password** – Only for fetching SaaS application data.

### Required Permissions

<Tabs>
  <Tab title="Cyber & Software Assets">
    <Columns layout="auto">
      <Column>
        <strong>Roles:</strong>

        <ul>
          <li>Cyber Administrator</li>
          <li>Device Manager</li>
        </ul>
      </Column>

      <Column>
        <strong>Permissions for Entra ID:</strong>

        <ul>
          <li>`Device.Read.All`</li>
          <li>`User.Read.All`</li>
          <li>`Directory.Read.All`</li>
          <li>`Application.Read.All`</li>
          <li>`AuditLog.Read.All`</li>
          <strong>Permissions for Entra ID Intune:</strong>
          <li>`DeviceManagementApps.Read.All`</li>
          <li>`DeviceManagementConfiguration.Read.All`</li>
          <li>`DeviceManagementManagedDevices.Read.All`</li>
          <li>`DeviceManagementServiceConfig.Read.All`</li>
          <li>`Directory.Read.All`</li>
        </ul>
      </Column>
    </Columns>
  </Tab>

  <Tab title="SaaS Applications">
    <Columns layout="auto">
      <Column>
        <strong>Roles:</strong>

        <ul>
          <li>Global Reader</li>
          <li>Identity Governance Administrator</li>
        </ul>
      </Column>

      <Column>
        <strong>Permissions:</strong>

        <ul>
          <li>`Reports.Read.All`</li>
          <li>`Global.Read`</li>
          <li>`AuditLog.Read.All`</li>
          <li>`MailboxSettings.Read`</li>
          <li>`Policy.Read.All`</li>
        </ul>
      </Column>
    </Columns>
  </Tab>
</Tabs>

## More Information About This Adapter

* [Deploying the Microsoft Entra ID (Azure AD) and Microsoft Intune Adapter](https://docs.axonius.com/axonius-help-docs/docs/entra-id-deploying-the-adapter)
* [Entra-ID Advanced Permissions](https://docs.axonius.com/axonius-help-docs/docs/entra-id-advanced-permissions)
* [Entra-ID Advanced Settings](https://docs.axonius.com/axonius-help-docs/docs/entra-id-advanced-settings)
* [Entra-ID Related Enforcement Actions](https://docs.axonius.com/axonius-help-docs/docs/entra-id-enforcement-actions)