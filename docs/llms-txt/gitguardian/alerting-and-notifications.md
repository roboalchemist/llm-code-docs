# Source: https://docs.gitguardian.com/platform/configure-alerting/alerting-and-notifications.md

# Configure real-time alerting and notifications for your perimeter

> Overview of GitGuardian's alerting system, including notification types, delivery channels, and integration options for incident management.

GitGuardian's real-time monitoring allows alerts to be sent immediately when an incident is detected or updated.

<iframe width="560" height="315" src="https://www.youtube.com/embed/2HLPZwebei4?controls=0&modestbranding=1" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>

Configuring a notifier from your GitGuardian workspace allows you to push incident alerts to the channel of your choice (e.g Slack, PagerDuty...). These alerts will contain details about the incident such as the triggered detector and location (org and repository) without revealing the secrets detected or any other sensitive data, avoiding any further contribution to sprawling of secrets.

## Incident types and integration scope

Most GitGuardian's alerting integrations are designed to handle **internal secret incidents** detected within your integrated sources. This includes all the notification channels and issue tracking integrations listed below.

**Custom webhooks** and **Slack** are the exceptions: if your workspace and team have access to **[Public Monitoring](../../public-monitoring/home)**, these integrations can also be configured to receive events related to **public secret incidents** detected on public repositories.

## Available integrations

By default, GitGuardian will notify dashboard users via email for every incident. You can [read more about email alerting here](./notifiers-integrations/email-alerting.md). You can also choose to integrate with other notification channels, GitGuardian currently supports:

- [Custom webhooks](./notifiers-integrations/custom-webhook)
  Custom services can be written to listen in on GitGuardian's detection engine and programmatically treat detected incidents. Can handle internal and/or public secret incidents.

- [Slack](./notifiers-integrations/slack)
  The Slack integration provides comprehensive notification coverage for  internal and/or public secret incident lifecycle events. Configure which events to receive in your team's workspace channels.

- [Microsoft Teams](./notifiers-integrations/microsoft-teams)
  The Microsoft Teams integration allows you to be notified on your team's workspace in a channel of your choice.

- [Discord](./notifiers-integrations/discord)
  The Discord integration allows you to be notified on your team's discord server of your choice.

- [PagerDuty](./notifiers-integrations/pagerduty)
  Send incidents as PagerDuty event notifications with the PagerDuty Integration.

- [Splunk](./notifiers-integrations/splunk)
  Treat incidents as data with the Splunk Integration.
