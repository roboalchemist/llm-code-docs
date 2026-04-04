# Source: https://checklyhq.com/docs/communicate/alerts/channels.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Alert Channels

> Configure notification channels to receive alerts when checks fail, degrade, or recover. Choose from email, Slack, webhooks, PagerDuty, SMS, and custom integrations.

Alert channels determine **how** alert notifications reach your team when checks fail, degrade, or recover. Checkly supports a wide range of notification methods to fit your team's communication preferences and operational workflows.

## Available Alert Channels

### Communication Platforms

* [Email](/integrations/alerts/email)
* [Slack](/integrations/alerts/slack)
* [Discord](/integrations/alerts/discord)
* [Telegram](/integrations/alerts/telegram)
* [SMS](/integrations/alerts/sms)
* [Phone Call](/integrations/alerts/phone-calls)
* [Microsoft Teams](/integrations/alerts/msteams)
* [GitLab Alerts](/integrations/alerts/gitlab_alerts)

### Incident Management

* [PagerDuty](/integrations/incident-management/pagerduty)
* [Opsgenie](/integrations/incident-management/opsgenie)
* [FireHydrant](/integrations/incident-management/firehydrant)
* [Incident.io](/integrations/incident-management/incidentio)
* [Rootly](/integrations/incident-management/rootly)
* [ilert](/integrations/incident-management/ilert)
* [Splunk On-Call](/integrations/incident-management/splunk-on-call)
* [Spike.sh](/integrations/incident-management/spike)
* [StatusPage](/integrations/incident-management/statuspage)

### Custom Integrations

* [Webhooks](/integrations/alerts/webhooks)

## Managing Alert Channels

### Channel Configuration Overview

Configure channels with flexible subscription and filtering options:

<img src="https://mintcdn.com/checkly-422f444a/riTtJrRZAx73iREC/images/docs/images/alerting/alert-channels.png?fit=max&auto=format&n=riTtJrRZAx73iREC&q=85&s=8b6873d17053e84ec60412b9f4fb9318" alt="Alert channels management interface" width="1291" height="309" data-path="images/docs/images/alerting/alert-channels.png" />

<Steps>
  <Step title="Create Alert Channel">
    Choose your notification method and provide connection details
  </Step>

  <Step title="Configure Alert Types">
    Select which types of events should trigger notifications
  </Step>

  <Step title="Subscribe Checks">
    Choose which checks and check groups use this channel
  </Step>

  <Step title="Test Integration">
    Verify the channel works correctly with test notifications
  </Step>
</Steps>

<Tip>
  Use Checkly's alert notification log to track delivery success rates and identify any channels that frequently fail to deliver notifications.
</Tip>


Built with [Mintlify](https://mintlify.com).