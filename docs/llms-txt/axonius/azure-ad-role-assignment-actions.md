# Source: https://docs.axonius.com/docs/azure-ad-role-assignment-actions.md

# Microsoft Entra ID (formerly Azure AD) - Role Assignment Actions

**Microsoft Entra ID (formerly Azure AD) - Role Assignments Actions** adds or deletes role assignments in Entra ID.

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

* **Use stored credentials from Microsoft Entra ID (formerly Azure Active Directory) and Microsoft Intune adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Microsoft Entra ID](/docs/microsoft-azure-active-directory-ad) adapter connection.
  </Callout>

* **Directory Role ID** - ID for the role you want to add or remove.
  **To get the Directory Role ID for the role**
  1. In your Microsoft 365 account, navigate to **Roles `>` Role Assignments**.
  2. Open the Role assignment you want.
  3. Copy the Directory Role ID from the URL in your address bar (see screenshot below).
  4. Back in Axonius, paste the copied ID in this Directory Role ID field.
     ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AzureAD_RoleEC_DirectoryRoleID.png)

* **Entity Action** - Select if you want to **Add to Role** or **Remove From Role**.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Azure Client ID** -The Application ID of the Axonius application.

  * **Azure Client Secret** - Specify a non-expired key generated from the new client secret.

  * **Azure Tenant ID** - The ID for Microsoft Entra ID.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **Cloud Environment** - Select your Microsoft Azure or Microsoft Entra ID cloud environment type.

  * **Azure Oauth Authorization Code** - The authorization code to connect to Microsoft Intune. This is a legacy option to allow Oauth delegated authentication.

  * **Azure OAuth - Redirect URI/Reply URL** - The location where the authorization server sends the user once the Azure has been successfully authorized and granted an authorization code or an access token. For more information, see Redirect URI (reply URL) restrictions and limitations.

  * **Is Azure AD B2C** - Select this option to cause Axonius to consider that this Microsoft Entra ID adapter connection is configured as B2C.

  * **Account Tag** - Specify a tag for Axonius to tag all devices fetched from this adapter for the Azure Cloud instance ("nickname").

  * **Device Groups Blocklist** - Enter a group or groups whose devices will be ignored and not fetched. If you want to enter more than one group, separate with commas.

  * **HTTPS Proxy** - A proxy to use when connecting to the selected Microsoft Azure/Entra ID cloud environment.

  * **HTTPS Proxy User Name** and **Password** - The user name and password to use when connecting to the selected Microsoft Azure / Azure AD cloud environment via the value supplied in HTTPS Proxy.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.

  <Callout icon="📘" theme="info">
    Note

    The following parameters are only relevant for customers who have SaaS Management enabled.
  </Callout>

  * **Account Sub Domain** - The Microsoft account's sub domain (.onmicrosoft.com).

  * **User Name** and **Password** - The credentials for a user account that has the permissions needed to perform this action.

  * **2FA Secret Key** - The secret generated in Microsoft Entra ID for setting up 2-factor authentication for the Microsoft user.

  * **SSO Provider** - If your organization uses Microsoft Entra ID for SSO, you can select this check box. For more information, see [Connecting your SSO Solution Provider Adapter](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider-adapter)
</Callout>

* **Is Role ID is for Role Template** - Select if the value you enter in the Directory Role ID field is actually the Role Template ID.

## APIs

Axonius uses the [Add directory role member](https://learn.microsoft.com/en-us/graph/api/directoryrole-post-members?view=graph-rest-1.0\&tabs=http) and the [Remove directory role member](https://learn.microsoft.com/en-us/graph/api/directoryrole-delete-member?view=graph-rest-1.0\&tabs=http) APIs.

## Required Permissions

This action requires the following additional Delegated (for work or school accounts) or Application permission to add or remove a role:

* 'RoleManagement.ReadWrite.Directory'

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).