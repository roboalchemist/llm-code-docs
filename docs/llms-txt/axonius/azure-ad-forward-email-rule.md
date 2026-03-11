# Source: https://docs.axonius.com/docs/azure-ad-forward-email-rule.md

# Microsoft Entra ID (formerly Azure AD) - Forward Email Rule

**Microsoft Entra ID (formerly Azure AD) - Forward Email Rule** adds a forwarding email address and other related email information to:

* Assets returned by the selected query or assets selected on the relevant asset page.

<Callout icon="📘" theme="info">
  Note

  This enforcement action runs on Users only.
</Callout>

Messages are then forwarded to this new email address. For example, if a user terminates employment and will no longer receive emails to their company email address but to a new email address.

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

* **Use stored credentials from the Microsoft Entra ID (formerly Azure AD) Adapter** - Select this option to use Microsoft Entra ID connected adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Microsoft Entra ID (Azure AD)](/docs/microsoft-azure-active-directory-ad) adapter connection.
</Callout>

* **Display Name** - The display name of the message rule created in Microsoft Entra ID.
* **Recipient Name** - The email recipient's name.
* **Recipient Email Address** - The email recipient's email address.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

* **Remove Existing Rule** - When selected, this removes the email address from the forwarding list. Messages sent to the user's email address will no longer be forwarded.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Azure Client ID** - The Application ID of the Axonius application. Copy this from the app registrations.
  * **Azure Client Secret**-  Specify a non-expired key generated from the new client secret. Copy this from the app registrations.
  * **Azure Tenant ID** - The ID for Microsoft Entra ID. Copy this from the app registrations.
  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  <Callout icon="📘" theme="info">
    Note:

    The following parameters are only relevant for customers who have SaaS Management enabled.
  </Callout>

  * **Account Sub Domain** - The Microsoft account's sub domain (.onmicrosoft.com).
  * **User Name** and **Password** - The credentials for a user account that has the permissions needed to fetch SaaS data.
  * **2FA Secret Key** - The secret generated in Microsoft Entra ID for setting up 2-factor authentication for the Microsoft user.
  * **SSO Provider** - If your organization uses Microsoft Entra ID for SSO, you can select this check box.

  To view detailed information about how to configure these fields and the adapter, refer to the [Entra ID](/docs/microsoft-azure-active-directory-ad) adapter configuration. To access the values of these fields, refer to the adapter's connection form.
</Callout>

## APIs

Axonius uses the [Microsoft Graph REST API v1.0](https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0\&preserve-view=true).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* MailboxSettings.ReadWrite

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).