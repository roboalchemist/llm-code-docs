# Source: https://docs.axonius.com/docs/clear-slack-session-settings.md

# Slack - Clear User's session settings

**Slack - Clear User's session settings** clears Slack sessions for:

* Users returned by the selected query or users selected on the Users page.

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

* **Use stored credentials from Slack Adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Slack](/docs/slack) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡">
  sd

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** - The full URL of the Slack server.
  * **Authentication Token** - An Authentication Token associated with a user account that has the [Required Permissions](/docs/slack#required-permissions) to fetch assets. For instructions on generating the Authentication Token, see [admin.users.list](https://api.slack.com/methods/admin.users.list).
  * **Account Sub Domain** - The Slack account's sub domain (.slack.com).
  * **Username** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to perform this Enforcement Action.
  * **MFA Secret** - The MFA Secret Key configured for the [Slack](/docs/slack) adapter.
  * **Enterprise Grid Organization** - Select if you are using the Slack Enterprise Grid Organization solution. This allows Axonius to fetch data from all workspaces associated with the authentication token.
  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
    <br />
</Callout>

## APIs

Axonius uses the [Slack Developers - admin.users.session.clearSettings method](https://docs.slack.dev/reference/methods/admin.users.session.clearSettings/) API.

## Required Permissions

The stored credentials, or those provided in Connection and Credentials, must have the  following permissions:

* admin.users:write

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).