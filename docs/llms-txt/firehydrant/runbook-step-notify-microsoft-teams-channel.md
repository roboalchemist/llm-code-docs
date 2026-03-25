# Source: https://docs.firehydrant.com/docs/runbook-step-notify-microsoft-teams-channel.md

# Notify Microsoft Teams Channel

FireHydrant offers a variety of channel notification steps. You can use a standard, templated notification or customize the message. This page covers the standard notification template. For customizing notifications, see [Notify Microsoft Teams Channel w/ Custom Message](https://docs.firehydrant.com/docs/runbook-step-notify-microsoft-teams-channel-w-custom-message).

## Configuration

<Image alt="Notify Microsoft Teams channel step" align="center" width="650px" src="https://files.readme.io/baee6d6-CleanShot_2024-05-22_at_17.00.51.png">
  Notify Microsoft Teams channel step
</Image>

The standard notification step comes in a preconfigured format and requires no additional setup besides specifying which Teams and channels to post into and when. To notify multiple channels, clone this step and select different channels.

You can optionally specify conditions for when notification should occur. The default is to trigger when the incident starts automatically.

## Runbook Execution

When the notification step executes, it will send a message containing relevant details and links about the incident, including:

* **Severity** and **Title**
* **Started Date and Time**
* **Opened By**
* **Assigned Roles and People**
* **Current milestone**
* **Any links, such as the incident channel, meeting bridge, Jira ticket, etc.**

The message will also automatically update in place when these details update:

<Image alt="Default templated notification message" align="center" width="650px" src="https://files.readme.io/52ab7fb-CleanShot_2024-05-22_at_17.07.37.png">
  Default templated notification message
</Image>