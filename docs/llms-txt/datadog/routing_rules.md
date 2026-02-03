# Source: https://docs.datadoghq.com/incident_response/on-call/routing_rules.md

---
title: Routing Rules
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Incident Response > On-Call > Routing Rules
---

# Routing Rules

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

With routing rules, you can define granular logic to control how alerts reach your team. Instead of sending alerts through a single escalation policy, you can create flexible, condition-based rules to route them based on priority, time of day, tags, and more.

## Routing rules examples{% #routing-rules-examples %}

- Route alerts by priority:

  - Send **priority 1** alerts to your primary escalation policy.
  - Send **priority 2â4** alerts to Slack or Microsoft Teams.

- Route alerts by time of day:

  - During business hours, route alerts to an escalation policy.
  - After hours, route critical alerts to paging, and non-critical alerts to chat.

- Use Dynamic Urgency to automatically detect urgency from the monitor alert:

  - `warn` status â low urgency
  - `alert` status â high urgency

The urgency of a page determines how end users are notified, based on their preferences.

- Trigger workflows (coming soon): Use routing rules to trigger automated workflows in response to matching alerts.

## Send Pages to Slack or Microsoft Teams{% #send-pages-to-slack-or-microsoft-teams %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/page_in_slack_or_ms_teams.379b23b87dff64445fd7a404651bbc8a.png?auto=format"
   alt="A sample routing rule, which routes all incoming Pages to Slack and Microsoft Teams." /%}

When you route Pages to Slack or Microsoft Teams, Datadog sends a notification to the configured channel and creates a corresponding Page object in the On-Call platform. From Slack, team members can use interactive buttons to acknowledge, resolve, escalate, or declare an incident. This streamlines incident response without leaving the chat environment.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/page_representation_in_slack.327c70eab79bca0ee49ea30260a1a2f0.png?auto=format"
   alt="A sample Page rendered in Slack." /%}

When a Page is acknowledged or resolved in Slack, Datadog updates the original notification in place, without sending additional messages. This keeps responders focused by reducing noise and showing the current Page status directly in the original thread.

## Routing rule syntax{% #routing-rule-syntax %}

Routing rules use [Datadog query syntax](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/) and support multiple `if/else` conditions. Rules are evaluated from top to bottom, and the final rule must act as a fallback that routes all unmatched alerts to an escalation policy.

{% alert level="danger" %}
Routing rule syntax is case-sensitive. For example, `tags.env:Prod` will not match `tags.env:prod`.
{% /alert %}

**Supported attributes:**

| Attribute      | Description                                 | Example                           |
| -------------- | ------------------------------------------- | --------------------------------- |
| `tags`         | Tags on the incoming alert                  | `tags.env:prod`                   |
| `groups`       | Monitor group names                         | `groups.service:checkout-service` |
| `priority`     | Monitor priority (1â5)                      | `priority:(1 OR 2)`               |
| `alert_status` | Monitor status (`error`, `warn`, `success`) | `alert_status:(error OR warn)`    |

## Best practices{% #best-practices %}

- Balance visibility with urgency:
  - Use paging and escalation policies for critical alerts that require immediate action.
  - Use Slack or Teams for lower-severity issues that need awareness but don't warrant an on-call response.

## Further reading{% #further-reading %}

- [Datadog On-Call](https://docs.datadoghq.com/incident_response/on-call/)
