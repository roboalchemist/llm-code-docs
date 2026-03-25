# Source: https://docs.axonius.com/docs/azure-ad-delegate-users-mailbox.md

# Microsoft Entra ID (formerly Azure AD) - Delegate User's Mailbox

**Microsoft Entra ID (formerly Azure AD) - Delegate User's Mailbox** assigns  delegations (permissions) to the mailboxes of Entra ID users, returned by the selected query or assets selected on the relevant asset page.

<Callout icon="📘" theme="info">
  Note

  This EC action runs only on User assets.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from Microsoft Entra ID (formerly Azure Active Directory) and Microsoft Intune Adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Microsoft Entra ID (formerly Azure Active Directory) and Microsoft intune Adapter](/docs/microsoft-azure-active-directory-ad) adapter connection.
</Callout>

* **IDs of Microsoft Entra ID (formerly Azure AD) Users to add permissions** - Specify the IDs of the Microsoft Entra ID users that will be granted the selected permission to the mailboxes of the users matching the query.

* **Permission type** - Select between FullAccess, SendAs, and SendOnBehalf.
  * **Example:** User X was selected in the query. Under **IDs of Microsoft Entra ID (formerly Azure AD) Users to add permissions**, the ID of User Y was specified; Under **Permission type**, FullAccess was selected. That means that User Y has been granted FullAccess permission to User X's mailbox.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Azure Client ID** - The Application ID of the Axonius application.

  * **Azure Client Secret** - Specify a non-expired key generated from the new client secret.

  * **Azure Tenant ID** - The ID for Microsoft Entra ID.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **Enable Certificate-Based Authentication** -  Select to enable Axonius to send requests using the Azure certificates uploaded to allow secure Azure authentication for this adapter.

  * Click **Upload File** next to **Private Key File** to upload an Azure private key file in PEM format.

  * Click **Upload File** next to **Certificate File** to upload an Azure public key file in PEM format.

  <Callout icon="📘" theme="info">
    Note:

    The following parameters are only relevant for customers who have the Axonius SaaS Applications product.
  </Callout>

  * **Account Sub Domain**  - The Microsoft account's sub domain (.onmicrosoft.com).
  * **User Name** and **Password** - The credentials of the user account.
  * **2FA Secret Key** - The secret generated in Microsoft Entra ID for setting up 2-factor authentication for the Microsoft user. For more information, see [Enable or Exclude Multi-Factor Authentication](/docs/microsoft-azure-active-directory-ad#enable-or-exclude-multifactor-authentication).
  * **SSO Provider** - If your organization uses Microsoft Entra ID for SSO, you can select this check box. For more information, see [Connecting your SSO Solution Provider](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider-adapter).
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Microsoft Graph REST API v1.0I](https://learn.microsoft.com/en-us/graph/api/resources/unifiedroledefinition?view=graph-rest-1.0).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* MailboxSettings.ReadWrite

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).