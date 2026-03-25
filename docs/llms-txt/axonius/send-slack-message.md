# Source: https://docs.axonius.com/docs/send-slack-message.md

# Slack - Send Message via Webhook

**Slack - Send Message via Webhook** posts a message on Slack using the webhook for Assets returned by the selected query or assets selected on the relevant asset page.

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

* **Incoming webhook URL** - Specify the incoming webhook URL. For details, see [Slack Incoming Webhooks](https://api.slack.com/incoming-webhooks).

* **Incident Description** - Specify an incident description to be included in the Slack message. You can include markup to format your message. For more information see [Format your messages](https://slack.com/help/articles/202288908-Format-your-messages#markup).

## Additional Fields

These fields are optional.

* **Incident Title** - Enter a title for the message.
* **Include Results in Message** - Select this option to include the results of the incident in the Slack message sent by this action.
* **Add Custom Blocks** - Select this option to send custom blocks in the slack messages sent by this EC Action.
  * **Block Title** - The title of the block sent in by this action.
  * **Block Text** - The text of the block sent in by this action.
* **Results display format** *(default: JSON)* - Select the display format of the results in the Slack message: JSON or table.
  * JSON format includes the details of the top 5 assets.
  * Table format includes the details of the top number of assets as defined in **Top Results Count**. Table format is supported only for devices.
* **Top Results Count (max 100**) *(default: 20)* - Set the top number of results to be displayed in a table.
* **Message Color** *(optional)* - Enter the hex code for the color you want the message to appear in.
* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

## API

Axonius uses the [Slack Channels](https://api.slack.com/methods/chat.postMessage#channels) API.

## Required Permissions

The stored credentials, or those provided in Connection and Credentials, must have have the  following permissions: <br />
**Bot tokens**: chat:write <br />
**User token**s: chat:write, chat: write:user, chat:write:bot

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).