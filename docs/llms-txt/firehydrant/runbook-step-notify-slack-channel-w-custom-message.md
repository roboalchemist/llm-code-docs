# Source: https://docs.firehydrant.com/docs/runbook-step-notify-slack-channel-w-custom-message.md

# Notify Slack Channel w/ Custom Message

FireHydrant offers a variety of channel notification steps. You can use a standard, templated notification or customize the message. This page covers **customized notifications**. For Standard Template notifications, see [Notify Channel](https://docs.firehydrant.com/docs/runbook-step-notify-channel).

## Prerequisites

* For the notification steps to work in Slack, **you need to invite the FireHydrant bot to the channels you want to notify**. You should only have to do this once for each new channel you want to post notifications to. The FireHydrant bot is included automatically in the incident channels it creates via Runbooks.
* For Microsoft Teams, the FireHydrant bot currently only supports posting into a single Team/Workspace. If the channel you try to notify doesn't exist in a particular Workspace, this step will automatically create it.

## Configuration

<Image alt="Notify channel with a custom message step" align="center" width="650px" src="https://files.readme.io/242b868-image.png">
  Notify channel with a custom message step
</Image>

The custom notification step has two fields:

* **Comma Separated Channels** - This is the same as the Notify Channel step, which allows you to specify a list of channels that should be notified. Slack requires the channel names with the `#` prefix while MS Teams does not.
* **Your message** - Allows you to configure exactly what message is sent. This field has both [Markdown Support](https://docs.firehydrant.com/docs/markdown-support) and [Template Variables](https://docs.firehydrant.com/docs/template-variables) support.

> 📘 Note:
>
> Slack uses a markup language called [mrkdwn](https://api.slack.com/reference/surfaces/formatting#basics), which is similar to Markdown but is not the same. We recommend viewing their documentation (linked above) to see how their conventions are different from standard Markdown. There is a 3,000 character limit for messages posted to Slack.

You can optionally specify conditions for when notification should occur. The default is automatically when the incident starts.