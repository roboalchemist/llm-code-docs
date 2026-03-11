# Source: https://docs.axonius.com/docs/okta.md

# Okta

## Overview

**Okta** is a cloud-based identity and access management (IAM) platform that provides single sign-on (SSO), multi-factor authentication (MFA), user lifecycle management, and application access control. The Axonius Okta adapter enables visibility into Okta users, groups, roles, applications, and related identity configurations to support security posture management, access audits, and identity governance.

### Use cases the adapter solves

The Okta adapter can fetch information regarding enrolled users and their registered applications and permissions. This can be used for access auditing or other related controls.

## Types of Assets Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_extensions.svg) Application Extensions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Admin_Managed_Extensions.svg) Admin Managed Extensions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/User_initiated_extensions.svg) User Initiated Extensions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_Add-ons.svg) Application Add-On | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Roles.svg) Roles | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Groups.svg) Groups | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_settings.svg) Application Settings | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_Extension_Instances.svg) Application Extension Instances | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Admin_Managed_Extension_Instances.svg) Admin Managed Extension Instances | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/User_initiated_extensions_instances.svg) User Initiated Extension Instances | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_Add-on_instances.svg) Application Add-On Instances | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_keys.svg) Application Keys | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Activities.svg) Activities | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Accounts_Tenants.svg) Accounts/Tenants | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Alerts_Incidents.svg) Alerts/Incidents | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_resources.svg)Application Resources | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Permissions.svg) Permissions

## Data Retrieved from Okta

* **Devices**: Device ID, device type, OS details, compliance status, last sign-in, associated user information.
* **Users**: Username, display name, email, status (active/inactive/deprovisioned), group memberships, role assignments, authentication factors, MFA enrollment, last login, custom attributes, profile information.
* **Groups**: Group metadata, memberships, group type (Okta-managed, imported, dynamic), assigned applications, rules and policies.
* **Applications and Extensions**: Assigned applications, application settings, extensions, add-ons, application resources, permissions, keys, OAuth grants, SSO configurations.
* **Roles and Permissions**: Role definitions, role assignments, administrative roles, permissions per role, access scopes.
* **Audit and Activity Logs**: User activity, authentication events, session events, administrative changes, security events, API access logs, system logs.
* **Configurations and Policies**: Authentication policies, sign-on policies, MFA settings, organization-wide settings, notification settings, security rules.
* **General Fields**: Last login timestamp, activity logs, deprovisioned status, enriched identity metadata, real-time updates (if enabled).

## Before You Begin

### Authentication Methods

The Okta adapter can be connected using one of the following authentication methods:

* **API Key** – Recommended for standard read-only connections.
* **OAuth2** – Recommended for secure delegated access, supporting public/private key authentication.

### Required Permissions

<Tabs>
  <Tab title="Cyber Assets">
    <Columns layout="auto">
      <Column>
        <strong>Roles:</strong>

        <ul>
          <li>Read-Only Administrator</li>
        </ul>
      </Column>

      <Column>
        <strong>Permissions:</strong>

        <ul>
          <li><code>okta.users.read</code></li>
          <li><code>okta.groups.read</code></li>
          <li><code>okta.apps.read</code></li>
          <li><code>okta.roles.read</code></li>
          <li><code>okta.logs.read</code></li>
          <li><code>okta.devices.read</code></li>
        </ul>
      </Column>
    </Columns>
  </Tab>

  <Tab title="SaaS Applications">
    <Columns layout="auto">
      <Column>
        <strong>Roles:</strong>

        <ul>
          <li>API Access Management Administrator</li>
          <li>Report Administrator</li>
          <li>Read-Only Administrator</li>
        </ul>
      </Column>
    </Columns>

    <p>
      SaaS Application permissions are required depending on the asset type you want to fetch, as follows:
    </p>

    <table>
      <thead>
        <tr>
          <th>SaaS Asset Type</th>
          <th>Required Okta Permissions</th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>Users</td>
          <td>`okta.users.read`</td>
        </tr>

        <tr>
          <td>Groups</td>
          <td><code>okta.groups.read</code></td>
        </tr>

        <tr>
          <td>Applications</td>

          <td>
            <code>okta.apps.read</code>
            <code>okta.appGrants.read</code>
          </td>
        </tr>

        <tr>
          <td>Application Extensions</td>
          <td><code>okta.apps.read</code></td>
        </tr>

        <tr>
          <td>User Extensions</td>
          <td><code>okta.apps.read</code></td>
        </tr>

        <tr>
          <td>SaaS Applications</td>
          <td><code>okta.apps.read</code></td>
        </tr>

        <tr>
          <td>Roles & Permissions</td>
          <td><code>okta.roles.read</code></td>
        </tr>

        <tr>
          <td>Application Settings</td>

          <td>
            <code>okta.roles.read</code>
            <code>okta.policies.read</code>
            <code>okta.orgs.read</code>
          </td>
        </tr>

        <tr>
          <td>Policies (MFA, Sign-In)</td>
          <td><code>okta.policies.read</code></td>
        </tr>

        <tr>
          <td>Activities</td>
          <td><code>okta.logs.read</code></td>
        </tr>

        <tr>
          <td>Organization Settings</td>
          <td><code>okta.orgs.read</code></td>
        </tr>

        <tr>
          <td>Accounts</td>
          <td>None</td>
        </tr>
      </tbody>
    </table>
  </Tab>
</Tabs>

## More Information About This Adapter

[Deploying the Okta Adapter](/docs/okta-deploying-the-adapter)

[Advanced Settings](/docs/okta-advanced-settings)

[Related Enforcement Actions](/docs/okta-related-enforcement-actions)