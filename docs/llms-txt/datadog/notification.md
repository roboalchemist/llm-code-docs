# Source: https://docs.datadoghq.com/incident_response/incident_management/notification.md

---
title: Incident Notification
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Incident Response > Incident Management > Incident Notification
---

# Incident Notification

## Overview{% #overview %}

Effective incident response depends on notifying the right people at the right time. Datadog Incident Management provides two key ways to coordinate communication during an incident:

- The **Notifications** tab centralizes stakeholder communications. From here, you can create and send manual updates, save drafts, and view all automated messages triggered by [Notification Rules](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/notification_rules).

- The **Pages** tab helps you manage your on-call Pages. From this tab, you can page [Datadog On-Call](https://docs.datadoghq.com/incident_response/on-call/) teams to prompt them to join the incident response. This tab also shows a history of all Pages sent, whether manually or through [Notification Rules](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/notification_rules), so that you can track which teams have been paged and when.

These tools ensure that both stakeholders and technical responders are promptly and reliably informed throughout the incident lifecycle.

## Add a notification{% #add-a-notification %}

To create a manual notification:

1. Navigate to the **Notifications** tab of an incident.
1. Click the **+ New Notification** button in the top right of the section.
1. Enter your desired recipients. These can be any notification handles supported by Datadog, including emails, Slack channels, PagerDuty handles, and webhooks.
1. Select a Message Template.
1. Edit the title and message of your notification using Markdown and any supported incident template variable by typing `{{`.
   - [Template variables](https://docs.datadoghq.com/monitors/notify/variables/?tab=is_alert) are based on the properties of an incident. Before a message is sent, all template variables are replaced by the corresponding value of the referenced property that is available to the message when it was sent.
1. Use the `{{incident.created}}` variable to customize your message timezone. This template variable will display the option to set your variable time zone.
1. Send your notification or save it as a draft.

## Trigger a Page from an incident{% #trigger-a-page-from-an-incident %}

To page a team or user using [Datadog On-Call](https://docs.datadoghq.com/incident_response/on-call/):

1. Navigate to the **Pages** tab of an incident.
1. Click **Page**.
1. Select the team or user you want to alert.
1. (Optional) Assign an incident role automatically to the person who acknowledges the Page.
1. Click **Page**.

## View all notifications{% #view-all-notifications %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/notification/incident_notifications_sent.a2d95e5ce0bf33554c69d2339cf294a0.png?auto=format"
   alt="Notification tab of an incident showing example list of sent messages" /%}

The Notifications tab of an incident lists notifications as **Drafts** and **Sent**. Both lists display:

- The (intended) recipients of a notification.
- The contents of the notification's message and any renotification messages that were sent.
- When the notification was last updated.
- The original author of the notification.

The **Sent** list also displays if a notification was manually or automatically sent by a notification rule. If the notification was automated, the rule that triggered the notification is displayed.

## Customize notification rules{% #customize-notification-rules %}

Notification Rules allows you to notify stakeholders automatically based on the matching criteria of the incident. Matching criteria include incident severity, affected services, status, root cause category, and a specific resource name. For example, you can set up a rule that automatically notifies your leadership team by email every time there is a SEV-1 incident. With this rule, the individual declaring the incident does not have to know whom to involve in every scenario.

For more information on how to configure a new notification rule, see the [Incident Settings](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/notification_rules) documentation.

## Message templates{% #message-templates %}

Message templates are dynamic, reusable messages that can be used in manual incident notifications, or automated notification rules. Message templates leverage template variables, such as `{{incident.severity}}`, to dynamically inject the corresponding value from the incident that the notification is being sent for. Message templates have Markdown support so that incident notifications can include text formatting, tables, indented lists, and hyperlinks. Template variables are supported in both the message's subject and body.

For more information on how to create a message template, see the [Incident Settings](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/templates) documentation.

## Further reading{% #further-reading %}

- [Customize notifications in Incident Settings](https://docs.datadoghq.com/incident_response/incident_management/incident_settings)
- [Monitor notification variables](https://docs.datadoghq.com/monitors/notify/variables/?tab=is_alert)
