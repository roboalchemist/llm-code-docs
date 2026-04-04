# Source: https://docs.datadoghq.com/events/correlation/triage_and_notify.md

---
title: Triage and Notify
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Event Management > Correlation > Triage and Notify
---

# Triage and Notify

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/events/correlation/triage/triage.8b26a42dd1f53fe5b24bdf022eea9e98.png?auto=format"
   alt="Case detail page with an event side panel. Investigate correlated events from a case and analyze related metrics" /%}

Event Management correlates related events and automatically consolidates them into a single case. Bring in all the context of related logs, related metrics, and alerting monitors to triage and troubleshoot issues in one place.

From the [Correlation](https://app.datadoghq.com/event/correlation) page, find the pattern you want to analyze and click **Triage Cases** at the end of the same row. You can also click **Case Management** at the top of the page to view all cases with correlated events in [Case Management](https://app.datadoghq.com/cases?query=status%3AOPEN%20creation_source%3AEVENT_MANAGEMENT&page=1&page-size=25&sort=created_at). Datadog pulls in related metrics and logs so you can troubleshoot issues with all the related data in one place.

## Event Management Case{% #event-management-case %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/events/correlation/triage/event_management_case_detail.a9247d5e241c8a545fbb27b43cea76dd.png?auto=format"
   alt="Case detail page - Overview" /%}

| Feature         | Description                                                                                                                                                                                                                               |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Priority        | highest priority of correlated alerts                                                                                                                                                                                                     |
| Attribute       | tags from correlated events. user updates won't get overriden by the engine                                                                                                                                                               |
| Status          | automatically managed by system, user updates will get overriden by system. Cases will auto resolve when all of the underline alerts recover and automatically reopen when any alert is re-triggered during the maximum alive time window |
| Deletion        | select the checkbox on the alert to delete any irrelevant alerts, deleted alerts won't get correlated again                                                                                                                               |
| Enriched Alerts | some cases will get automatically enriched with intelligent alerts that Datadog thinks are related based on your infrastructure. Enriched alert do not impact case attribute, priority, and status                                        |

For more information on Case Management operations, see the [Case Management documentation](https://docs.datadoghq.com/incident_response/case_management/view_and_manage).

### Investigation{% #investigation %}

1. From the case Overview, click **Investigation**
1. Under the *Correlations* section, you can see a list of alerts and events
1. Click into any of the alerts or events to view all related metrics and logs in context of the alert
1. (Optional) Select any alerts or events you want to remove that are not related to the case
1. Under the *Related Metrics* section, compare all related metrics or group by tags

## Create a notification or ticket{% #create-a-notification-or-ticket %}

With correlated events, you can configure one notification for a group. So, instead of having 20 notifications and 20 potential issues to investigate, you have one single case and one notification. Combine all your alerts in the Case Management Projects page. There are a few ways to group notifications in Case Management:

### Ticketing{% #ticketing %}

On the Project Settings page, configure the Integrations you want your projects to send notifications to. Datadog supports the following integrations with manual and automatic ticket creation, and bi-directional syncing:

- ServiceNow
- Jira

For setup instructions, see the [Case Management Settings](https://docs.datadoghq.com/incident_response/case_management/settings#set-up-integrations) documentation.

## Notifications{% #notifications %}

In case management, *views* group cases based on a configured query. You can set up a notification when a case matching this query is created. Datadog supports, **Pagerduty**, **Email**, **Webhook**, **Microsoft Teams**, and **Slack**. To learn how to create a view, see the [Case Management Views](https://docs.datadoghq.com/incident_response/case_management/view_and_manage#create-a-view) documentation.

**Note**: You need to reconfigure underlying monitors to remove multiple notifications. Grouping monitor events does not mute individual notifications.
