# Source: https://docs.firehydrant.com/docs/notify-slack-incident-channel-w-custom-message.md

# Notify Slack Incident Channel w/ Custom Message

FireHydrant offers a variety of channel notification steps. This step is similar to [a custom notification](https://docs.firehydrant.com/docs/runbook-step-notify-channel-w-custom-message), but since it's posting into the incident channel, you can also add action buttons.

Every incident channel will also have a pinned message that is the equivalent of a [standard, templated notification](https://docs.firehydrant.com/docs/runbook-step-notify-channel).

## Prerequisites

You must [have an incident channel](https://docs.firehydrant.com/docs/runbook-step-create-incident-channel) to post into. The FireHydrant bot is included automatically in the incident channels it creates via Runbooks.

## Configuration

<Image alt="Notify incident channel w/ custom message step" align="center" width="650px" src="https://files.readme.io/5476fee-image.png">
  Notify incident channel w/ custom message step
</Image>

This step comes with a few configurable fields:

* **Your message** - The message you'd like to post. This field has both [Markdown Support](https://docs.firehydrant.com/docs/markdown-support) and [Template Variables](https://docs.firehydrant.com/docs/template-variables) support. Slack uses a markup language called [mrkdwn](https://api.slack.com/reference/surfaces/formatting#basics), which is similar to Markdown but not the same. We recommend that you view their documentation to see how their conventions differ from standard Markdown. Messages posted to Slack have a 3,000-character limit.
* **Action Button(s)** - You can optionally specify available action buttons that will display to users when this notification is posted.
* **Pin Message** - You can optionally pin this message to the channel, making it more easily accessible to others.

<Image alt="Slack custom notification action buttons" align="center" width="650px" src="https://files.readme.io/033a7e4-slack-notify-custom-message-action.png">
  Slack custom notification action buttons
</Image>