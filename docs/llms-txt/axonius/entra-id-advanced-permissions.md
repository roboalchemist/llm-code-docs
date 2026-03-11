# Source: https://docs.axonius.com/docs/entra-id-advanced-permissions.md

# Entra-ID Advanced Permissions

## Setting Advanced Permissions

The following table summarizes permissions that Axonius requires to fetch various Entra ID resources.

Use this information to enable required permissions and to only apply necessary permissions.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Azure Service
      </th>

      <th>
        Permissions
      </th>

      <th>
        Advanced Configuration
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Last sign-in audit log information
      </td>

      <td>
        `AuditLog.Read.All` `Device.Read.All`
      </td>

      <td>
        Fetch users Last Sign-In
      </td>
    </tr>

    <tr>
      <td>
        Entra ID Intune
      </td>

      <td>
        `DeviceManagementApps.Read.All` `DeviceManagementConfiguration.Read.All` `DeviceManagementManagedDevices.Read.All` `DeviceManagementServiceConfig.Read.All` `Directory.Read.All` (also for SaaS data)
      </td>

      <td>
        Fetch devices from Intune<br />
        Fetch software information from Intune
      </td>
    </tr>

    <tr>
      <td>
        Allow for enriching Intune devices with their Security Baseline states
      </td>

      <td>
        `DeviceManagementConfiguration.ReadWrite.All`
      </td>

      <td>
        Fetch Security Baseline Device States
      </td>
    </tr>

    <tr>
      <td>
        Fetch Risky Users information
      </td>

      <td>
        `IdentityRiskyUser.Read.All`
      </td>

      <td>
        Fetch risky users information
      </td>
    </tr>

    <tr>
      <td>
        Fetch extra custom user flow attributes to be added dynamically to the User’s assets data
      </td>

      <td>
        `IdentityUserFlow.Read.All`
      </td>

      <td>
        Fetch custom user flow attributes
      </td>
    </tr>

    <tr>
      <td>
        Fetch users
      </td>

      <td>
        `User.Read.All`
      </td>

      <td>
        Default
      </td>
    </tr>

    <tr>
      <td>
        Fetch authentication method (if the Allow use of Beta API endpoints setting is enabled)
      </td>

      <td>
        `UserAuthenticationMethod.Read.All`
      </td>

      <td>
        Fetch user authentication methods<br />
        *If you enable this setting **and** have the additional `Policy.Read.All` permission, not only the adapter will fetch authentication methods, but also extra information regarding each authentication method’s status — whether they are enabled or disabled.*
      </td>
    </tr>

    <tr>
      <td>
        Group app roles
      </td>

      <td>
        `Directory.Read.All` or `AppRoleAssignment.ReadWrite.All`
      </td>

      <td>
        Fetch group app roles
      </td>
    </tr>

    <tr>
      <td>
        Role data
      </td>

      <td>
        `Directory.Read.All`
      </td>

      <td>
        Fetch user app roles
      </td>
    </tr>

    <tr>
      <td>
        User Contacts data
      </td>

      <td>
        `Contacts.Read`
      </td>

      <td>
        Fetch user contacts
      </td>
    </tr>

    <tr>
      <td>
        Fetch password validity data
      </td>

      <td>
        `Domain.Read.All`
      </td>

      <td>
        Default
      </td>
    </tr>

    <tr>
      <td>
        Fetch Device Information Protection - Bitlocker Recovery Key
      </td>

      <td>
        `BitlockerKey.ReadBasic.All`
      </td>

      <td>
        Fetch Device Information Protection - Bitlocker Recovery Key<br />
        Fetch Device Configuration Policy Settings for Bitlocker
      </td>
    </tr>

    <tr>
      <td>
        Fetch mailbox settings for users
      </td>

      <td>
        `MailboxSettings.Read`
      </td>

      <td>
        Fetch mailbox settings for users
      </td>
    </tr>

    <tr>
      <td>
        Fetch claims policy for enterprise applications
      </td>

      <td>
        `Policy.ReadWrite.ApplicationConfiguration`
      </td>

      <td>
        Fetch claims policy for enterprise applications
      </td>
    </tr>

    <tr>
      <td>
        Fetch the conditions created or enforced by the Entra ID configuration
      </td>

      <td>
        `Policy.Read.All`
      </td>

      <td>
        Fetch Conditional Access Policies
      </td>
    </tr>

    <tr>
      <td>
        Fetch information about Microsoft Apps Usage
      </td>

      <td>
        `Reports:Reader`
      </td>

      <td>
        Fetch Microsoft apps reports
      </td>
    </tr>
  </tbody>
</Table>

#### The following permissions are only for Axonius accounts with the Axonius SaaS Applications:

| Azure Service                                                     | Permissions        | Advanced Configuration                                  |
| :---------------------------------------------------------------- | :----------------- | :------------------------------------------------------ |
| Fetch Office365 activity endpoints (and SaaS data)                | `Reports.Read.All` | Fetch date of last activity for M365 product            |
| Allow fetching email activity                                     | `Reports.Read.All` | Fetch email activity from Office 365 in the last X days |
| Allow fetching licenses and application settings                  | `Global.Read`      | Fetch users license detail                              |
| Allow fetching extensions that Entra ID is granted permissions to |                    | Fetch user extensions                                   |

## Enforcement Action Permissions

To use the Entra ID Enforcement Actions, the following permissions are required:

| Supported Resource | Delegated                                               | Application                                             |
| ------------------ | ------------------------------------------------------- | ------------------------------------------------------- |
| device             | `GroupMember.ReadWrite.All` `Device.ReadWrite.All`      | `GroupMember.ReadWrite.All` `Device.ReadWrite.All`      |
| group              | `GroupMember.ReadWrite.All` `Group.ReadWrite.All`       | `GroupMember.ReadWrite.All` `Group.ReadWrite.All`       |
| orgContact         | `GroupMember.ReadWrite.All` `OrgContact.Read.All`       | `GroupMember.ReadWrite.All` `OrgContact.Read.Al`        |
| group              | `GroupMember.ReadWrite.All` `Group.ReadWrite.All`       | `GroupMember.ReadWrite.All` `Group.ReadWrite.All`       |
| servicePrincipal   | `GroupMember.ReadWrite.All` `Application.ReadWrite.All` | `GroupMember.ReadWrite.All` `Application.ReadWrite.All` |
| user               | `GroupMember.ReadWrite.All` `User.ReadWrite.All`        | `GroupMember.ReadWrite.All` `User.ReadWrite.All`        |