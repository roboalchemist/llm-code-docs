# Source: https://docs.datadoghq.com/incident_response/incident_management/declare.md

---
title: Declare an Incident
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Incident Response > Incident Management > Declare an Incident
---

# Declare an Incident

## Overview{% #overview %}

In the Datadog paradigm, any of the following are appropriate situations for declaring an incident:

- An issue is or may be impacting customers.
- You believe an issue (including an internal one) needs to be addressed as an emergency.
- You don't know if you should call an incident - notify other people and increase severity appropriately.

You can declare an incident from multiple places within the Datadog platform, such as a graph widget on a dashboard, the Incidents UI, or any alert reporting into Datadog.

## Declaration modal{% #declaration-modal %}

When you declare an incident, a declaration modal appears. This modal has several core elements:

| Incident elements  | Description                                                                                                                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Title              | (Required) A descriptive title for the incident.                                                                                                                                            |
| Severity Level     | (Required) By default, severity ranges from SEV-1 (most severe) to SEV-5 (least severe). You can customize the number of severities and their descriptions in Incident Management settings. |
| Incident Commander | The person assigned to lead the incident response.                                                                                                                                          |

You can configure [Incident Management Settings](https://docs.datadoghq.com/incident_response/incident_management/incident_settings#information) to include more fields in the incident declaration modal or require certain fields.

## From the Incident page{% #from-the-incident-page %}

In the [Datadog UI](https://app.datadoghq.com/incidents), click **Declare Incident** to create an incident.

The *Declare Incident* modal displays a collapsible side panel that contains helper text and descriptions for the severities and statuses used by your organization. The helper text and descriptions are customizable in [Incident Settings](https://docs.datadoghq.com/incident_response/incident_management/incident_settings#information).

## From a monitor{% #from-a-monitor %}

You can declare an incident directly from a monitor from the Actions dropdown. Select **Declare incident** to open an incident creation modal, and the monitor is added into the incident as a signal. You can also add a monitor to an existing incident.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/declare/declare_monitor.a941e923557bef5003f98a617c6915f0.png?auto=format"
   alt="Actions dropdown menu on monitors where you can select the Declare incident option" /%}

Alternatively, you can have a monitor automatically create an incident when it transitions to a `warn`, `alert`, or `no data` status. To enable this, click **Add Incident** in the **Configure notifications and automations** section of a monitor and select an `@incident-` option. Admins can create `@incident-` options in [Incident Settings](https://app.datadoghq.com/incidents/settings?section=global-settings).

Incidents created from a monitor will inherit [field values](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/property_fields) from the monitor's tags. To send automated notifications from incidents, add tags to a monitor so that created incidents match the criteria of [notification rules](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/notification_rules).

## From a Security Signal{% #from-a-security-signal %}

Declare an incident directly from a Cloud SIEM or Workload Protection signal side panel, by clicking **Declare incident** or **Escalate Investigation**. For more information, see [Investigate Security Signals](https://docs.datadoghq.com/security/workload_protection/security_signals/#declare-an-incident).

Declare an incident from an App and API Protection signal through the actions listed in the signal side panel. Click **Show all actions** and click **Declare Incident**. For more information, see [Investigate Security Signals](https://docs.datadoghq.com/security/workload_protection/security_signals/#declare-an-incident) for App and API Protection.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/declare/declare_asm.bd188c0709428c09399416b1d955586f.png?auto=format"
   alt="Your image description" /%}

## From a case{% #from-a-case %}

Declare an incident from [Case Management](https://docs.datadoghq.com/incident_response/case_management/view_and_manage). From the individual case detail page, click **Declare incident** to escalate a case to an incident.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/declare/declare_case_management.68ff08f07218e99ecd6a3ce6426673c1.png?auto=format"
   alt="An example case page highlighting the Declare Incident button at the top of the page" /%}

## From a graph{% #from-a-graph %}

You can declare an incident directly from a graph by clicking the export button on the graph and then clicking **Declare incident**. The incident creation modal appears, and the graph is added to the incident as a signal.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/from-a-graph.f572c2897c41bf62a6cbfce104018e9c.png?auto=format"
   alt="Create in incident from a graph" /%}

## From a Synthetic test{% #from-a-synthetic-test %}

Create incidents directly from a [Synthetic test](https://app.datadoghq.com/synthetics/tests) through the Actions dropdown. Select **Declare incident** to open an incident creation modal, where a summary of the test is added to your incident timeline, allowing you to pursue the investigation from there.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/declare/synthetics_declare_incident.c57c6dd7fdf36b513645957cf780dd36.png?auto=format"
   alt="Declare an incident from a Synthetic test." /%}

## From the Datadog Clipboard{% #from-the-datadog-clipboard %}

Use the [Datadog Clipboard](https://docs.datadoghq.com/dashboards/guide/datadog_clipboard) to gather multiple monitors and graphs and to generate an incident. To declare an incident from the Clipboard, copy a graph you want to investigate and open the Clipboard with the command `Cmd/Ctrl + Shift + K`. Click **Declare Incident** or the export icon to add to the incident as a signal.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/declare/declare_clipboard.0af876b348e4fdd2d253b35e22e85c13.png?auto=format"
   alt="Declare an incident from the Datadog Clipboard" /%}

## From a Datadog On-Call page{% #from-a-datadog-on-call-page %}

You can declare an incident directly from a [Datadog On-Call page](https://docs.datadoghq.com/incident_response/on-call/). From the [On-Call pages list](https://app.datadoghq.com/on-call/pages), select a page and click **Declare Incident** to create an incident and automatically associate it with the relevant on-call team.

## From Slack{% #from-slack %}

If you have the [Datadog integration enabled on Slack](https://docs.datadoghq.com/integrations/slack/?tab=slackapplicationbeta#using-the-slack-app), you can declare a new incident with the slash command `/datadog incident` from any Slack channel.

If the user declaring the incident connected their Slack to their Datadog account, by default, that user is listed as the Incident Commander. The Incident Commander (IC) can be changed later in-app if necessary. If the user declaring an incident is not a member of a Datadog account, then the IC is assigned to a generic `Slack app user` and can be assigned to another IC in-app.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/from-slack.2f36ce3b79e54e49c1e58a35b2aedd75.png?auto=format"
   alt="Create in incident from Slack" /%}

After you declare an incident from Slack, it generates an incident channel.

## From Handoff Notifications{% #from-handoff-notifications %}

The Handoff Notification displays callout cards when you are paged or added to active incidents. These cards allow you to:

- View and acknowledge On-Call pages
- Navigate to relevant incident resources
- Preview Slack messages from incident channels
- Take direct actions on incidents

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/declare/handoff_notification_card.38fc6da2304f0f0d8730d70e3862d6cf.png?auto=format"
   alt="Handoff notification card showing incident details with options to view, acknowledge, and take actions" /%}

Handoff Notificiation cards remain visible until dismissed or until the incident status changes. You can expand, collapse, or dismiss the entire handoff container rather than individual cards.

You can declare an incident from individual Handoff Notification cards.

## What's next{% #whats-next %}

- [Describe the Incident: Add context and details](https://docs.datadoghq.com/incident_response/incident_management/describe)
