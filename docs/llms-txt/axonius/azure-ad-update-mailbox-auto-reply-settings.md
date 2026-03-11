# Source: https://docs.axonius.com/docs/azure-ad-update-mailbox-auto-reply-settings.md

# Microsoft Entra ID (formerly Azure AD) - Update Mailbox Auto Reply Settings

**Microsoft Entra ID (formerly Azure AD) - Update Mailbox Auto Reply Settings** updates the auto reply message status in the user's email settings for:

* Assets returned by the selected query or assets selected on the relevant asset page.

The auto-reply can be set to Disabled, Always Enabled, or Scheduled and a message configured for external and internal audiences.

To use this Enforcement Action, configure a query to find users in a specific Entra ID group. When a user is added to the group, the EC is run on that user.

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

<Callout icon="📘" theme="info">
  Note

  This enforcement action runs on Users only.
</Callout>

* **Use stored credentials from the Microsoft Entra ID (formerly Azure AD) Adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Microsoft Entra ID (Azure AD)](/docs/microsoft-azure-active-directory-ad) adapter connection.
</Callout>

* **Status** - Select the auto-reply status:
  * **Disabled** - No message is sent.
  * **Always Enabled** - These fields are optional:
    * **External Audience** - Send the message to these external contacts:
      * **None** *(default)* - Don't send the message to any external contacts.
      * **Contacts Only** - Send the message to the specified external contacts.
      * **All** - Send the message to all external contacts.
    * **External Reply Message** - Send this message to email addresses that are NOT company email addresses.
    * **Internal Reply Message** - Send this message to email addresses that *are* company email addresses.
  * **Scheduled**
    * For **External Audience**, **External Reply Message**, and  **Internal Reply Message** see above.
    * **Scheduled Start Datetime** - Enter the date and time to start using the new auto reply message.
    * **Scheduled End Datetime** - Enter the date and time to stop using the new auto reply message.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Azure Client ID** *(required)* - The Application ID of the Axonius application. Copy this from the app registrations.

  * **Azure Client Secret** *(required)* -  Specify a non-expired key generated from the new client secret. Copy this from the app registrations.

  * **Azure Tenant ID** *(required)* - The ID for Microsoft Entra ID. Copy this from the app registrations.

  * **Cloud Environment** *(required)* - Select your Microsoft Azure or Microsoft Entra ID cloud environment type.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.

  To view detailed information about how to configure these fields and the adapter, refer to the [Entra ID](/docs/microsoft-azure-active-directory-ad) adapter configuration. To access the values of these fields, refer to the adapter's connection form.
</Callout>

## APIs

Axonius uses the [Update user mailbox settings - Microsoft Graph v1.0 ](https://learn.microsoft.com/en-us/graph/api/user-update-mailboxsettings?view=graph-rest-1.0\&tabs=http).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* `MailboxSettings.ReadWrite`

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).