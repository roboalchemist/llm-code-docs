# Source: https://docs.axonius.com/docs/azure-ad-asset-set-enabled.md

# Microsoft Entra ID (formerly Azure AD) - Enable or Disable Assets

**Microsoft Entra ID (formerly Azure AD) - Enable or Disable Assets** enables or disables each of the assets that are the results of the query, which are Microsoft Entra ID blocked/disabled managed devices or users or assets selected on the relevant asset page.

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

* **Use stored credentials from Microsoft Entra ID (formerly Azure AD) adapter** - Select this option to use credentials from the adapter connection.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Microsoft Entra ID](/docs/microsoft-azure-active-directory-ad) adapter connection.
</Callout>

* **Enable Status** - The action you want to perform, select either *Enable* or *Disable*.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Azure Client ID**  -  The Application ID of the Axonius application.

  * **Azure Client Secret**  - Specify a non-expired key generated from the new client secret.

  * **Azure Tenant ID**  - The ID for Microsoft Entra ID.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  <Callout icon="📘" theme="info">
    Note

    The following parameters are only relevant for customers who have SaaS Management enabled.
  </Callout>

  * **Account Sub Domain**  - The Microsoft account's sub domain (.onmicrosoft.com).
  * **User Name** and **Password** - The credentials for a user account that has the permissions needed to fetch SaaS data.
  * **2FA Secret Key** - The secret generated in Microsoft Entra ID for setting up 2-factor authentication for the Microsoft user. For more information, see [Enable or Exclude Multi-Factor Authentication](/docs/microsoft-azure-active-directory-ad#enable-or-exclude-multifactor-authentication).
  * **SSO Provider** - If your organization uses Microsoft Entra ID for SSO, you can select this check box. For more information, see [Connecting your SSO Solution Provider Adapter](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider-adapter).
</Callout>

## APIs

Axonius uses the following APIs:

* [Microsoft Graph REST API v1.0 Update User](https://learn.microsoft.com/en-us/graph/api/user-update?view=graph-rest-1.0\&tabs=http#example-2-update-properties-of-the-specified-user).
* [Microsoft Graph REST API v1.0 Update Device](https://learn.microsoft.com/en-us/graph/api/device-update?view=graph-rest-1.0\&tabs=http#example-1-update-the-accountenabled-property-of-a-device)

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).