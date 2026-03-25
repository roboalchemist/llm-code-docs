# Source: https://docs.axonius.com/docs/enrich-azure-ad-users-with-microsoft-defender-attack.md

# Microsoft Entra ID (formerly Azure AD) - Enrich User with Microsoft Defender Attack data

**Microsoft Entra ID (formerly Azure AD) - Enrich User with Microsoft Defender Attack data** enriches Entra ID users with Microsoft Defender Attack report data for:

* Assets returned by the selected query or assets selected on the relevant asset page.

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

These fields must be configured to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Microsoft Entra ID (formerly Azure Active Directory) and Microsoft Intune adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Microsoft Entra ID (formerly Azure Active Directory) and Microsoft Intune](/docs/microsoft-azure-active-directory-ad) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Domain** - The full URL of the YYY server.

  * **Azure Client ID** - The Application ID of the Axonius application, as detailed in the [Required Permissions](#required-permissions) section.

  * **Azure Client Secret** - A user created key for the Axonius application, as detailed in the [Required Permissions](#required-permissions) section.

  * **Azure Tenant ID** - Microsoft Entra ID, as detailed in the [Required Permissions](#required-permissions) section.

  * **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
    ::: info (Note)
    The following parameters are only relevant for customers who have Axonius SaaS Management enabled.
</Callout>

* **Account Sub Domain** - The Microsoft account's sub domain (.onmicrosoft.com).
* **User Name** and **Password** - The credentials for a user account that has the permissions needed to fetch SaaS data.
* **2FA Secret Key** - The secret generated in Microsoft Entra ID for setting up 2-factor authentication for the Microsoft user. For more information, see Enable or Exclude Multi-Factor Authentication.
* **SSO Provide**r - If your organization uses Microsoft Entra ID for SSO, you can select this check box. For more information, see Connecting your SSO Solution Provider Adapter .

:::

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Microsoft Graph Rest API v1.0](https://learn.microsoft.com/en-us/graph/api/securityreportsroot-getattacksimulationsimulationusercoverage?view=graph-rest-1.0\&tabs=http).

## Required Permissions

Choose one of these snippets:
The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* AttackSimulation.Read.All permission on Graph environment

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).