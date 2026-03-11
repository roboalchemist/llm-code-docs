# Source: https://docs.axonius.com/docs/assign-azure-ad-group-to-user.md

# Microsoft Entra ID (formerly Azure AD) - Assign Group to Users

**Microsoft Entra ID (formerly Azure AD) - Assign Group to Users** adds or removes an Entra ID group to or from the users returned by the selected query or assets selected on the relevant asset page.

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

* **Use stored credentials from the Microsoft Entra ID (Azure AD) and Microsoft Intune adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure an [Microsoft Entra ID (Azure AD) and Microsoft Intune](/docs/microsoft-azure-active-directory-ad) adapter connection.
</Callout>

* **Group IDs** -  Select the groups to assign from the list or enter the group IDs in UUID format, separated by comma.

* **Add/Remove assignment** - Select the action to perform: Add or Remove.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

* **Enforce assets only from the selected connection** - When enabled, the enforcement action only runs on assets fetched via the adapter connection configured in **Use stored credentials from the Microsoft Entra ID (Azure AD) and Microsoft Intune adapter**.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Azure Client ID** - The Application ID of the Axonius application.

  * **Azure Client Secret** - Specify a non-expired key generated from the new client secret.

  * **Azure Tenant ID** - The ID for Microsoft Entra ID.

  * **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

  * **Account Sub Domain** - The Microsoft account's sub domain (.onmicrosoft.com).

  * **Username** and **Password** - The credentials for a user account that has the permissions needed to perform this action.

  * **2FA Secret Key** - The secret generated in Microsoft Entra ID for setting up 2-factor authentication for the Microsoft user.

    <Callout icon="📘" theme="info">
      If you have a [**Group ID**](/docs/assign-azure-ad-group-to-user#required-fields) representing a mail-enabled security group, the **Username**, **Password**, and **2FA Secret Key** (if required by your Entra ID authentication policy) are mandatory. These credentials should belong to a service account with the Exchange Recipient Administrator role, which is required to add or remove members from the group. Learn how to [Create a User Account](/docs/microsoft-azure-active-directory-ad#create-a-user-account).
    </Callout>

  * **SSO Provider** - If your organization uses Microsoft Entra ID for SSO, you can select this check box.

  * **Cloud Environment** - Select your Microsoft Azure or Microsoft Entra ID cloud environment type.

  * **Azure OAuth - Authorization Code** - The authorization code to connect to Microsoft Intune. This is a legacy option to allow OAuth delegated authentication.

  * **Azure OAuth  - Redirect URI/Reply URL** - The location where the authorization server sends the user once the Azure has been successfully authorized and granted an authorization code or an access token. For more information, see [Redirect URI (reply URL) restrictions and limitations](https://learn.microsoft.com/en-us/azure/active-directory/develop/reply-url).

  * **Is Azure AD B2C** - Select this option to cause Axonius to consider that this Microsoft Entra ID adapter connection is configured as B2C.

  * **Account Tag** - Specify a tag for Axonius to tag all devices fetched from this adapter for the Azure Cloud instance ("nickname").

  * **Device groups blocklist** - Enter a group or groups whose devices will be ignored and not fetched. If you want to enter more than one group, separate with commas.

  * **HTTPS Proxy** - A proxy to use when connecting to the selected Microsoft Azure/Entra ID cloud environment.

  * **HTTPS Proxy User Name and Password** - The user name and password to use when connecting to the selected Microsoft Azure / Azure AD cloud environment via the value supplied in HTTPS Proxy.

  * **Gateway Name** - Select the Gateway for this action. for more information, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).
    For more information, see [Connecting your SSO Solution Provider Adapter](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider-adapter).
</Callout>

* **Justification reason** - Enter reason for adding or removing the listed groups to/from the users.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Required Permissions

The associated application must be granted the `GroupMember.ReadWrite.All`

For full and up-to-date information about permissions required for working with Microsoft Entra ID refer to [permissions in Microsoft Graph API Documentation](https://learn.microsoft.com/en-us/graph/api/group-post-members?view=graph-rest-1.0\&tabs=http#permissions).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).