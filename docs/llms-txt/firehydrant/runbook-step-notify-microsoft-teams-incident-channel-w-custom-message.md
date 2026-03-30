# Source: https://docs.firehydrant.com/docs/runbook-step-notify-microsoft-teams-incident-channel-w-custom-message.md

# Notify Microsoft Teams Incident Channel w/ Custom Message

FireHydrant offers a variety of channel notification steps. This step is similar to [Notify Microsoft Teams Channel w/ Custom Message](https://docs.firehydrant.com/docs/runbook-step-notify-microsoft-teams-channel-w-custom-message) but is specifically for posting into the incident channel.

Every incident channel will already have a pinned message that is the equivalent of a [Notify Microsoft Teams Channel](https://docs.firehydrant.com/docs/runbook-step-notify-microsoft-teams-channel) templated message, so there is no need to use this step if you want a high-level card with details and action buttons.

## Prerequisites

* You must have [a Microsoft Teams Incident Channel](https://docs.firehydrant.com/docs/runbook-step-create-microsoft-teams-incident-channel) to post into.

## Configuration

<Image alt="Notify Microsoft Teams incident channel w/ a custom message step" align="center" width="650px" src="https://files.readme.io/9a6c16a-CleanShot_2024-05-22_at_17.17.29.png">
  Notify Microsoft Teams incident channel w/ a custom message step
</Image>

This step comes with the following configurable fields:

* **Name** - A configurable name for the step. This shows up in the Runbook details tab for each incident and has no impact on actual execution
* **Your message** - The message you'd like to post. This field has both [Markdown Support](https://docs.firehydrant.com/docs/markdown-support) and [Template Variables](https://docs.firehydrant.com/docs/template-variables) support. MS Teams supports standard Markdown and has an [approximate limit of 28 KB per message](https://learn.microsoft.com/en-us/microsoftteams/limits-specifications-teams#chat).