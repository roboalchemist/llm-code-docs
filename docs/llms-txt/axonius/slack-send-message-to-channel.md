# Source: https://docs.axonius.com/docs/slack-send-message-to-channel.md

# Slack - Send Message to Channel

**Slack - Send Message to Channel** posts a message to a Slack channel for:

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

* **Use stored credentials from Slack Adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Slack](/docs/slack) adapter connection.
</Callout>

* **Channel ID** - The ID of the channel to which to send the messages.

* **Message Description** - Specify a message description to be included in the Slack message. You can include markup to format your message. For more information see [Format your messages](https://slack.com/help/articles/202288908-Format-your-messages#markup).

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

* **Create list of predefined responses** - This field is only available in an action that is added to a Workflow. Enter a list of response buttons to be shown in the Slack message in the order that they are added into this field. Click **Add** to add each possible response to the list. When a response button is clicked in a Slack message that is sent, the workflow continues based on that button.
* **Number of Assets to include in Message Body (max 100)** - Set the top number of results to be displayed. The default value is 20. If this value is 0, the message will consist of just the specified text, and no asset details will be included.
* **Message Color** *(optional)* - Enter the hex code for the color you want the message to appear in.
* **Prettify Entities** -
  * Select this option to present in the Slack message, in an improved format, only the column view set in the Enforcement Action query.
  * Leave this option disabled (the default) to present the Slack message in JSON format.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** - The hostname or IP address of the Slack server.

  * **Authentication Token** -  An Authentication Token associated with a user account that has the [Required Permissions](#required-permissions) to perform this action. For instructions on generating the Authentication Token, see [admin.users.list](https://api.slack.com/methods/admin.users.list).

  * **Account Sub Domain** - The Slack server's sub domain (\<sub\_domain>.slack.com).

  * **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to perform this action.

  * **MFA Secret** - The MFA Secret Key configured for the [Slack](/docs/slack) adapter.

  * **Enterprise Grid Organization** - Select this option if you are using the Slack Enterprise Grid Organization solution.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## API

Axonius uses the [Slack Post Message API](https://api.slack.com/methods/chat.postMessage#channels)

## Required Permissions

The stored credentials, or those provided in Connection and Credentials, must have have the  following permissions:<br />
**Bot tokens**: chat:write <br />
**User tokens**: chat:write, chat: write:user, chat:write:bot, chat.write.public

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).