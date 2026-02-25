# Source: https://docs.datadoghq.com/events/explorer/notifications.md

# Source: https://docs.datadoghq.com/security/notifications.md

---
title: Notifications
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Notifications
---

# Notifications
Available for:
{% icon name="icon-siem" /%}
 Cloud SIEM |
{% icon name="icon-cloud-security-management" /%}
 Cloud Security |
{% icon name="icon-app-sec" /%}
 App and API Protection |
{% icon name="icon-security-code-security" /%}
 Code Security
## Overview{% #overview %}

Notifications help you keep your team informed when a finding or security signal is detected. Findings and security signals are generated when at least one case defined in a [detection rule](https://docs.datadoghq.com/security/detection_rules/#creating-and-managing-detection-rules) is matched over a given period of time. By promptly alerting your team, notifications ensure that immediate action can be taken to address any potential security issues, enhancing your organization's overall security posture.

## Notification types{% #notification-types %}

Notifications can be set up for individual detection rules and also more broadly with notification rules.

### Detection rules{% #detection-rules %}

When you [create or modify a detection rule](https://docs.datadoghq.com/security/detection_rules/#creating-and-managing-detection-rules), you can define the notifications that are sent. For example, you can add rule cases to determine when a detection rule triggers a security signal.

You can also customize the notification message using Markdown and [notification variables](https://docs.datadoghq.com/security/notifications/variables/). This allows you to provide additional details about the signal by referencing its tags and event attributes. You can also add tags to the generated signal, for example, `attack:sql-injection-attempt`.

### Notification rules{% #notification-rules %}

Notification rules allow you to set general alerting preferences that span across multiple detection rules, findings, and signals instead of having to set up notification preferences for individual detection rules. For example, you can set up a notification rule to send a notification if any `CRITICAL` or `HIGH` severity signal is triggered. See [Notification Rules](https://docs.datadoghq.com/security/notifications/rules/) for more information on setup and configuration.

## Notification channels{% #notification-channels %}

Notifications can be sent to individuals and teams through email, Slack, Jira, PagerDuty, webhooks, and more.

### Email{% #email %}

- Notify an active Datadog user by email with `@<DD_USER_EMAIL_ADDRESS>`.

**Note**: An email address associated with a pending Datadog user invitation or a disabled user is considered inactive and does not receive notifications. Blocklists, IP or domain filtering, spam filtering, or email security tools may also cause missing notifications.

- Notify any non-Datadog user by email with `@<EMAIL>`.

**Note**: Email notifications don't support addresses that contain slashes `/`, for example, `@DevOpS/West@example.com`.

### Integrations{% #integrations %}

Notify your team through connected integrations by using the format `@<INTEGRATION_NAME>-<VALUES>`.

This table lists prefixes and example links:

| Integration                                                                 | Prefix        | Examples                                                                                         |
| --------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------ |
| [Jira](https://docs.datadoghq.com/integrations/jira/)                       | `@jira`       | [Examples](https://docs.datadoghq.com/integrations/jira/#usage)                                  |
| [PagerDuty](https://docs.datadoghq.com/integrations/pagerduty/)             | `@pagerduty`  | [Examples](https://docs.datadoghq.com/integrations/pagerduty/#troubleshooting)                   |
| [Slack](https://docs.datadoghq.com/integrations/slack/)                     | `@slack`      | [Examples](https://docs.datadoghq.com/integrations/slack/#-mentions-in-slack-from-monitor-alert) |
| [Webhooks](https://docs.datadoghq.com/integrations/webhooks/)               | `@webhook`    | [Examples](https://docs.datadoghq.com/integrations/webhooks/#usage)                              |
| [Microsoft Teams](https://docs.datadoghq.com/integrations/microsoft_teams/) | `@teams`      | [Examples](https://docs.datadoghq.com/integrations/microsoft_teams/#usage-1)                     |
| [ServiceNow](https://docs.datadoghq.com/integrations/servicenow/)           | `@servicenow` | [Examples](https://docs.datadoghq.com/integrations/servicenow/#knowledge-base)                   |

Handles that include parentheses (`(`, `)`) are not supported. When a handle with parentheses is used, the handle is not parsed and no alert is created.

#### Create a webhook for security automation{% #create-a-webhook-for-security-automation %}

You can use webhooks to send alerts to other platforms, such as SOAR. To set up a webhook:

1. Navigate to the [Webhooks](https://app.datadoghq.com/integrations/webhooks) integration.
1. Click **+ New** in the **Webhooks** section.
1. Enter a name for the webhook.
1. Enter the webhook URL.
1. In the **Payload** section, select **Security Signal**.
   {% image
      source="https://datadog-docs.imgix.net/images/security/security_signal_payload.170df2d8f52f59bfc373874652dd011d.png?auto=format"
      alt="The webhooks signal security payload" /%}
1. See the [Webhooks integration](https://docs.datadoghq.com/integrations/webhooks/) documentation for more information on adding variables, custom variables, custom headers, and encoding as a form.
1. Click **Save**.

To use the webhook, add `@webhook-<WEBHOOK_NAME>` to the rule's notification section.

## Further reading{% #further-reading %}

- [Set up and configure notification rules](https://docs.datadoghq.com/security/notifications/rules/)
- [Learn more about notification variables to customize notifications](https://docs.datadoghq.com/security/notifications/variables/)
- [Explore security detection rules](https://docs.datadoghq.com/security/detection_rules/)
