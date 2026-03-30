# Source: https://docs.firehydrant.com/docs/runbook-step-notify-microsoft-teams-channel-w-custom-message.md

# Notify Microsoft Teams Channel w/ Custom Message

FireHydrant offers a variety of channel notification steps. You can use a standard, templated notification or customize the message. This page covers **customized notifications**. For Standard Template notifications, see [Notify Microsoft Teams Channel](https://docs.firehydrant.com/docs/runbook-step-notify-microsoft-teams-channel).

## Configuration

<Image alt="Notify Microsoft Teams Channel with a custom message" align="center" width="650px" src="https://files.readme.io/d94588a-CleanShot_2024-05-22_at_17.12.25.png">
  Notify Microsoft Teams Channel with a custom message
</Image>

The custom notification step has three fields:

* **Name** - Any name for the step. This will show up on the Runbook details tab for an incident.
* **Team** - Select which Team you'd like to post to
* **Channel** - Select a channel you'd like to post to within the Team. To post multiple messages to different channels/Teams, clone the step and change the values.
* **Your message** - Allows you to configure exactly what message is sent. This field has both [Markdown Support](https://docs.firehydrant.com/docs/markdown-support) and [Template Variables](https://docs.firehydrant.com/docs/template-variables) support. MS Teams supports standard Markdown and has an [approximate limit of 28 KB per message](https://learn.microsoft.com/en-us/microsoftteams/limits-specifications-teams#chat).

You can optionally specify triggers for when notification should occur. The default is automatically when the incident starts.