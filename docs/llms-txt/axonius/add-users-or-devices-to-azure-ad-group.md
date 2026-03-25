# Source: https://docs.axonius.com/docs/add-users-or-devices-to-azure-ad-group.md

# Microsoft Entra ID (formerly Azure AD) - Add or Remove Assets in Group

**Microsoft Entra ID (formerly Azure AD) - Add or Remove Assets in Group** adds or removes a user or device to or from an Entra ID group for:

* Assets returned by the selected query or assets selected on the relevant asset page.
  This action can be used to deploy patches.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Microsoft Entra ID (formerly Azure AD)  adapter** - Select this option to use the first connected Entra ID adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  * To use this option, you must successfully configure an [Azure Active Directory](/docs/microsoft-azure-active-directory-ad) adapter connection.
</Callout>

* **Group Member Operation** - Select the operation you want to perform: 'Add assets to group' or 'Remove assets from group'.
* **AD Group ID** - The ID of the group to which to add the users.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Azure Client ID** - The Application ID of the Axonius application, as detailed in the [Required Permissions](#required-permissions) section.

  * **Azure Client Secret** - A user created key for the Axonius application, as detailed in the [Required Permissions](#required-permissions) section.

  * **Azure Tenant ID** - Microsoft Entra ID, as detailed in the [Required Permissions](#required-permissions) section.

  * **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

  <Callout icon="📘" theme="info">
    Note

    The following parameters are only relevant for customers who have Axonius SaaS Management enabled.
  </Callout>

  * **Account Sub Domain** - The Microsoft account's sub domain (.onmicrosoft.com).
  * **User Name** and **Password** - The credentials for a user account that has the permissions needed to fetch SaaS data.
  * **2FA Secret Key** - The secret generated in Microsoft Entra ID for setting up 2-factor authentication for the Microsoft user. For more information, see Enable or Exclude Multi-Factor Authentication.

  <Callout icon="📘" theme="info">
    Note

    If you have a [**Group ID**](/docs/add-users-or-devices-to-azure-ad-group#required-fields) representing a mail-enabled security group, the **Username**, **Password**, and **2FA Secret Key** (if required by your Entra ID authentication policy) are mandatory. These credentials should belong to a service account with the Exchange Recipient Administrator role, which is required to add or remove members from the group. Learn how to [Create a User Account](/docs/microsoft-azure-active-directory-ad#create-a-user-account).
  </Callout>

  * **SSO Provide**r - If your organization uses Microsoft Entra ID for SSO, you can select this check box. For more information, see Connecting your SSO Solution Provider Adapter .
</Callout>

### Using this Action to Add an Application in InTune

Intune is a Microsoft cloud-based unified endpoint management service that can perform app deployment, updates, and removal.
**Prerequisites**:

* An Entra ID device group
* The App must be added to your Intune environment.[Read about this.](https://learn.microsoft.com/en-us/mem/intune/apps/apps-add)
* The Entra ID device group must be assigned to the App Assignments as required.[Read about this](https://learn.microsoft.com/en-us/mem/intune/apps/apps-deploy)

**To Create the appropriate Group in Microsoft Endpoint Manager admin center**

* Create a group.
  Create the appropriate Group in Microsoft Endpoint Manager admin center.

**To add the application to  InTune:**

1. From  the Microsoft Endpoint Manager admin center click 'Apps'.
2. Choose **All apps**.
3. Click **Add**.
4. Select **app type**.
5. Choose the appropriate Store app.
6. Select the application and click **Select**.
7. Fill in all required information.
8. Create the application.
9. In properties add the group to the app as required.

Use Microsoft Intune documentation for further information

Anyone in this group is now required to install this application. These groups (from InTune) are now available in Entra ID as groups.
Copy the ID of the groups to use above in the configuration.

In order to use this action to install applications, create a query to find Devices on the relevant platform that is missing the application.
For example, azureID exists AND NOT crowdstrike ID exists.
Then, use this Enforcement Action to add the devices to the groups that require these applications. Once the device is added to the group, the user is notified by Entra ID that they have to install the required application.

## Required Permissions

The value supplied in [User name](#connections-settings) must have permission to modify the group listed, meaning, it must have the Add Users or Devices to Microsoft Entra ID Group permissions to add assets.
Delegated permissions are needed to work with this Action.

For full ands up-to-date information about permissions required for working with Microsoft Entra ID refer to [permissions in Microsoft Graph API Documentation](https://learn.microsoft.com/en-us/graph/api/group-post-members?view=graph-rest-1.0\&tabs=http#permissions).

| Supported Resource | Delegated                                               | Application                                             |
| ------------------ | ------------------------------------------------------- | ------------------------------------------------------- |
| device             | GroupMember.ReadWrite.All and Device.ReadWrite.All      | GroupMember.ReadWrite.All and Device.ReadWrite.All      |
| group              | GroupMember.ReadWrite.All and Group.ReadWrite.All       | GroupMember.ReadWrite.All and Group.ReadWrite.All       |
| orgContact         | GroupMember.ReadWrite.All and OrgContact.Read.All       | GroupMember.ReadWrite.All and Group.ReadWrite.All       |
| group              | GroupMember.ReadWrite.All and Group.ReadWrite.All       | GroupMember.ReadWrite.All and OrgContact.Read.All       |
| servicePrincipal   | GroupMember.ReadWrite.All and Application.ReadWrite.All | GroupMember.ReadWrite.All and Application.ReadWrite.All |
| user               | GroupMember.ReadWrite.All and User.ReadWrite.All        | UGroupMember.ReadWrite.All and User.ReadWrite.All       |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).