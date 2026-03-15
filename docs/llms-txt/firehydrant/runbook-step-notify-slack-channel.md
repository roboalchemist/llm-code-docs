# Source: https://docs.firehydrant.com/docs/runbook-step-notify-slack-channel.md

# Notify Slack Channel

FireHydrant offers a variety of channel notification steps. You can use a standard, templated notification or customize the message. This page covers the standard notification template. For customizing notifications, see [Notify Channel w/ Custom Message](https://docs.firehydrant.com/docs/runbook-step-notify-channel-w-custom-message).

## Prerequisites

To notify channels in Slack, **you must invite the FireHydrant bot to the channels you want to notify**. You should only have to do this once for each new channel you want to post notifications to. The FireHydrant bot is included automatically in the incident channels it creates via Runbooks.

## Configuration

<Image alt="Notify Channel step. The step looks identical for both Slack and Microsoft Teams" align="center" width="650px" src="https://files.readme.io/56e6a45-image.png">
  Notify Slack Channel step
</Image>

The standard notification step comes in a preconfigured format and requires no additional setup besides specifying which channels to post in and when.

When filling in the list of comma-separated channels, Slack requires the channel names with the `#` prefix while MS Teams does not.

You can optionally specify conditions for when notification should occur. The default is automatically when the incident starts.

## Runbook Execution

When the notification step executes, it will send a message containing relevant details and links about the incident, including:

* **Severity** and **Title**
* **Started** and **Resolved** times
* **Opened By** and **Resolved By** whom
* **Assigned Roles and People**
* Any links, such as channel, meeting bridge, ticket, etc.
* Buttons to the Command Center and Internal Status Page

The message will also automatically update in place when these details update:

<Image alt="Standard notification template in Slack" align="center" width="650px" src="https://files.readme.io/b58e948-image.png">
  Standard notification template in Slack
</Image>