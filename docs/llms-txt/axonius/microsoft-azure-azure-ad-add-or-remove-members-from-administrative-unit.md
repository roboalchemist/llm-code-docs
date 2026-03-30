# Source: https://docs.axonius.com/docs/microsoft-azure-azure-ad-add-or-remove-members-from-administrative-unit.md

# Microsoft Entra ID (formerly Azure AD) - Add or Remove Members from Administrative Unit

**Microsoft Entra ID (formerly Azure AD) - Add or Remove Members from Administrative Unit** adds or removes a user to or from an Entra ID Administrative unit for:

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

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the  Microsoft Entra ID (formerly Azure AD)  adapter** - Select this option to use the connected Entra ID adapter credentials. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Microsoft Entra ID](/docs/microsoft-azure-active-directory-ad) adapter connection.
</Callout>

1. **Administrative Unit ID** - The object ID of the Administrative Unit to which to add the users or to remove the users from.
2. **Operation** - Select the operation you want to perform, either **Add members** or **Remove members**.
3. **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Azure Client ID** - The Application ID of the Axonius application.

  * **Azure Client Secret** - Specify a non-expired key generated from the new client secret.

  * **Azure Tenant ID** - The ID for Microsoft Entra ID.

  * **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

  <Callout icon="📘" theme="info">
    Note

    The following parameters are only relevant for customers who have SaaS Management enabled.
  </Callout>

  * **Account Sub Domain** - The Microsoft account's sub domain (.onmicrosoft.com).
  * **Username** and **Password** - The credentials for a user account that has the permissions needed to perform this action.
  * **2FA Secret Key** - The secret generated in Microsoft Entra ID for setting up 2-factor authentication for the Microsoft user.
  * **SSO Provider** - If your organization uses Microsoft Entra ID for SSO, you can select this check box.

  For more information, see [Connecting your SSO Solution Provider Adapter](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider-adapter).
</Callout>

## APIs

Axonius uses the Microsoft Graph REST API v1.0 [Add a Member](https://learn.microsoft.com/en-us/graph/api/administrativeunit-post-members?view=graph-rest-1.0\&tabs=http) and [Remove a Member](https://learn.microsoft.com/en-us/graph/api/administrativeunit-delete-members?view=graph-rest-1.0\&tabs=http) API.

## Required Permissions

The associated application must be granted AdministrativeUnit.ReadWrite.All Application permission and must be assigned the Privileged Role Administrator or Global Administrator role.

For full ands up-to-date information about permissions required for working with Microsoft Entra ID refer to [permissions in Microsoft Graph API Documentation](https://learn.microsoft.com/en-us/graph/api/group-post-members?view=graph-rest-1.0\&tabs=http#permissions).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).