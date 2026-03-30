# Source: https://docs.port.io/actions-and-automations/setup-backend/send-slack-message.md

# Send Slack message

The `Send Slack message` backend type allows you to send a message to a Slack channel, using a webhook URL.<br /><!-- -->This can be useful when you want to notify certain users/teams about a specific event that occurred in your software catalog.

## Define the backend[â](#define-the-backend "Direct link to Define the backend")

This backend type requires a Slack webhook URL.<br /><!-- -->To create a webhook in Slack, see the [Slack documentation](https://api.slack.com/messaging/webhooks).

Once you have the webhook URL, simply paste it into the `Webhook URL` field in the backend definition:

![](/img/self-service-actions/setup-backend/slack-message/slackUiExample.png)

### Message[â](#message "Direct link to Message")

The message to be sent is defined under the `Message` section (see image above).

The message uses Slack's `mrkdwn` formatting, information and examples can be found in the [Slack documentation](https://api.slack.com/reference/surfaces/formatting).

### Using trigger data in the message[â](#using-trigger-data-in-the-message "Direct link to Using trigger data in the message")

Just like other backend types, you can access available trigger data using `jq`, by wrapping the expression with `{{ . }}`.

Trigger data structure reminder

See the data available to you when writing your message:

* [Trigger data structure for Self-service actions](/actions-and-automations/create-self-service-experiences/setup-the-backend/.md#trigger-data).
* [Trigger data structure for Automations](/actions-and-automations/define-automations/setup-action.md#trigger-data).

For example, to include the run id of the action that sent the message, you can add the following text to your message:

```
This message was sent via an action run with the following id: {{ .run.id }}.
```
