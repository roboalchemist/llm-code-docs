# Source: https://docs.axonius.com/docs/assign-slack-resource-to-user.md

# Slack - Assign Resource to Users

**Slack - Assign Resource to Users** assigns a resource to users in Slack for:

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

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Slack adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Slack](/docs/slack) adapter connection.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Action.

* **Resource ID** - The ID for the resource you want to assign/remove assignment for.
* **Resource Type** - The list of entity IDs (Org IDs, Team IDs, or Channel IDs) to which the resource can be assigned.
* **Add/Remove Assignment** - Select whether to **Add** or **Remove** the resource assignment.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** *(default: `https://slack.com`)* - The full URL of the Slack server.

  * **Authentication Token** *(required)* - An Authentication Token associated with a user account that has the [Required Permissions](/docs/slack#required-permissions) to fetch assets. For instructions on generating the Authentication Token, see [admin.users.list](https://api.slack.com/methods/admin.users.list).

  * **Authentication Sub Domain** - The Slack account's sub domain (.slack.com).

  * **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](/docs/slack#required-permissions) to perform this Enforcement Action.

  * **MFA Secret** - The MFA Secret Key configured for the [Slack](/docs/slack) adapter.

  * **Enterprise Grid Organization** - Select if you are using the Slack Enterprise Grid Organization solution. This allows Axonius to fetch data from all workspaces associated with the authentication token.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Justification reason** *(optional)* - Enter the reason for assigning the resource.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Slack - Invite Conversation](https://api.slack.com/methods/conversations.invite),[Slack - Remove Conversation](https://api.slack.com/methods/conversations.kick),[Slack - Add an Enterprise User](https://api.slack.com/methods/admin.users.assign), and [Slack - Remove a User](https://api.slack.com/methods/admin.users.remove) APIs.

## Required Permissions

The stored credentials, or those provided in Connection and Credentials, must have the following permissions:

* write
* edit
* admin

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).