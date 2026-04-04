# Source: https://docs.datadoghq.com/incident_response/incident_management.md

# Source: https://docs.datadoghq.com/getting_started/incident_management.md

---
title: Getting Started with Incident Management
description: >-
  Track and communicate issues from declaration through resolution with
  collaborative workflows, timelines, and postmortems.
breadcrumbs: Docs > Getting Started > Getting Started with Incident Management
---

# Getting Started with Incident Management

## Overview{% #overview %}

Datadog Incident Management is for tracking and communicating about an issue you've identified with your metrics, traces, or logs.

This guide walks you through using the Datadog site for declaring an incident, updating the incident as investigation and remediation progresses, and generating a postmortem when the incident has been resolved. The example assumes the [Slack integration](https://docs.datadoghq.com/integrations/slack/) is enabled.

## Walking through an incident from issue detection to resolution{% #walking-through-an-incident-from-issue-detection-to-resolution %}

### Declaring an incident{% #declaring-an-incident %}

**Scenario:** A monitor is alerting on a high number of errors which may be slowing down several services. It's unclear whether customers are being impacted.

This guide describes using the [Datadog Clipboard](https://docs.datadoghq.com/dashboards/guide/datadog_clipboard) to declare an incident. Using the Clipboard, you can gather information from different sources, such as graphs, monitors, entire dashboards, or [notebooks](https://docs.datadoghq.com/notebooks/#overview). This helps you provide as much information as possible when declaring an incident.

1. In Datadog, navigate to [**Dashboard List**](https://app.datadoghq.com/dashboard/lists) and select **System - Metrics**.
1. Hover over one of the graphs and copy it to the Clipboard with one of the following commands:
   - **Ctrl**/**Cmd** + **C**
   - Click the **Export** icon on the graph and select **Copy**.
1. In the Datadog menu on the left-hand side, go to [**Monitors** > **Monitors List**](https://app.datadoghq.com/monitors/manage) and select **[Auto] Clock in sync with NTP**.
1. Open the Clipboard: **Ctrl**/**Cmd** + **Shift** + **K**.
1. In the Clipboard, click **Add current page** to add the monitor to the Clipboard.
   {% image
      source="https://datadog-docs.imgix.net/images/getting_started/incident_management/copy_to_clipboard.a1ba0cdba0598063a42cb23d530eabdb.png?auto=format"
      alt="Copy to Clipboard" /%}
1. Click **Select All** and then **Export items toâ¦**
1. Select **Declare Incident**.
1. Describe what's happening:
|  |
|  |
| Title              | Follow any naming conventions your team wants to use for incident titles. Because this is not a real incident, include the word `TEST` to make it clear that this is a test incident. An example title: `[TEST] My incident test` |
| Severity Level     | Set to **Unknown** since it's unclear whether customers are being impacted and how related services are being impacted. See the in-app description of what each severity level means and follow your team's guidelines.           |
| Incident Commander | Leave this assigned to you. In an actual incident this would be assigned to the leader of the incident investigation. You or others can update who the incident commander is as the incident investigation progresses.            |
1. Click **Declare Incident** to create the incident. You can also declare an incident from a [graph](https://docs.datadoghq.com/incident_response/incident_management/#from-a-graph), [monitor](https://docs.datadoghq.com/incident_response/incident_management/#from-a-monitor), or the [incidents API](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident). For APM users, you can click the incidents icon on any APM graph to declare an incident. As part of the Slack integration, you can also use the `/datadog incident` shortcut to declare an incident and set the title, severity, and customer impact.
1. Click **Slack Channel** on the incident's page to go to the incident's Slack channel.

A new Slack channel dedicated to the incident is automatically created for any new incident, so that you can consolidate communication with your team and begin troubleshooting. If your organization's Slack integration is set up to update a global incident channel, then the channel is updated with the new incident.

If you don't have the Slack integration enabled, click **Add Chat** to add the link to the chat service you are using to discuss the incident.

Click **Add Video Call** to add a link to the call where discussions about the incident are happening.

### Troubleshooting and updating the incident{% #troubleshooting-and-updating-the-incident %}

The Incident page has four main sections: *Overview*, *Timeline*, *Remediation*, and *Notifications*. Update these sections as the incident progresses to keep everyone informed of the current status.

#### Overview{% #overview-1 %}

**Scenario:** After some investigation, you discover that the root cause is a host running out of memory. You've also been informed that a small subset of customers are being affected and seeing slow loading of pages. The first customer report came in 15 minutes ago. It is a SEV-3 incident.

In the *Overview* section, you can update incident fields and customer impact as the investigation continues.

To update the severity level and root cause:

1. Click the *Severity* dropdown and select **SEV-3**.
1. Under *What happened*, select **Monitor** in the *Detection Method* dropdown (Unknown is selected), because you were first alerted by a monitor on the issue.
1. Add to the *Why it happened* field: `TEST: Host is running out of memory.`
1. Click **Save** to update the properties. From Slack, you can also update the title, severity, or status of an ongoing issue using the `/datadog incident update` command.

To add the customer impact:

1. Click **+ Add** in the *Impact* section.
1. Change the timestamp to 15 minutes earlier, because that was when the first customer report came in.
1. Add to descriptions field: `TEST: Some customers seeing pages loading slowly.`
1. Click **Save** to update the fields. The *Impact* section updates to show how long the customer impact has been going on. All changes made on the *Overview* page are added to the *Timeline*.

#### Timeline{% #timeline %}

The *Timeline* shows additions and changes to incident fields and information in chronological order.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/incident_management/flag_event.237c6916698429a523a2e39eff38f88e.png?auto=format"
   alt="Flag Event" /%}

1. Click the **Timeline** tab.
1. Find the *Impact added* event and mark as *Important* by clicking the flag icon.
1. Add a note to the timeline: `I found the host causing the issue.`
1. Hover over the note's event and click the pencil icon to change the timestamp of the note because you actually found the host causing the issue 10 minutes ago.
1. Flag the note as **Important**.
1. Click **Slack Channel** to go back to the incident's Slack channel.
1. Post a message in the channel saying `I am working on a fix.`
1. Click the message's actions command icon (three dots on the right after hovering over a message).
1. Select **Add to Incident** to send the message to the timeline.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/incident_management/add_from_slack.cce467f05c722f6a7fc287958b0745e8.png?auto=format"
   alt="Add from Slack" /%}

You can add any Slack comment in the incident channel to the timeline so that you can consolidate important communications related to the investigation and mitigation of the incident.

#### Remediation{% #remediation %}

**Scenario:** There's a notebook on how to handle this kind of issue, which includes tasks that need to be done to fix it.

In the *Remediation* section, you can keep track of documents and tasks for investigating the issue or for post-incident remediation tasks.

1. Click the **Remediation** tab.
1. Click the plus icon `+` in the *Documents* box and add a link to a [Datadog notebook](https://app.datadoghq.com/notebook/list). All updates to the *Documents* section are added to the timeline as an *Incident Update* type.
1. Add a task by adding a description of a task in the *Incident Tasks* box, for example: `Run the steps in the notebook.`
1. Click **Create Task**.
1. Click **Assign To** and assign yourself the task.
1. Click **Set Due Date** and set the date for today. All task additions and changes are recorded in the *Timeline*. You can also add post-incident tasks in the *Remediation* section to keep track of them.

#### Notifications{% #notifications %}

**Scenario:** The issue has been mitigated, and the team is monitoring the situation. The incident status is stable.

In the *Notifications* section, you can send out a notification updating the status of the incident.

1. Navigate back to the *Overview* section.
1. Change the status in the dropdown menu from *ACTIVE* to *STABLE*.
1. Go to the *Notifications* tab.
1. Click **New Notification**. The default message has the incident's title in the subject and information about the current status of the incident in the body. In an actual incident you would send updates to the people involved in the incident. For this example, send a notification to yourself only.
1. Add yourself to the *Recipients* field.
1. Click **Send**. You should receive an email with the message. You can create customized [message templates](https://app.datadoghq.com/incidents/settings#Messages). Group templates together using the *Category* field.

### Resolution and postmortem{% #resolution-and-postmortem %}

**Scenario:** It's been confirmed that the issue no longer impacts customers and that you've resolved the issue. The team wants a postmortem to look back on what went wrong.

1. Go to the *Overview* section.
1. Change the status from *STABLE* to *RESOLVED* so that it's no longer active. You can also change the date and time for when the customer impact ended if it occurred earlier.
1. When an incident's status is set to resolved, a *Generate Postmortem* button appears at the top. Click **Generate Postmortem**.
1. For the timeline section, select **Marked as Important** so that only the *Important* events are added to the postmortem.
1. Click **Generate**.

The postmortem is generated as a Datadog Notebook or Confluence page, and it includes the timeline events and resources referenced during the investigation and remediation. This makes it easier to review and further document what caused the issue and how to prevent it in the future.

If there are follow-up tasks that you and your team need to complete to ensure the issue doesn't happen again, add those and track them in the Remediation's *Incident Tasks* section.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/incident_management/generate_postmortem.4534ce0623bae4e011d057e8a621736d.png?auto=format"
   alt="Generate Postmortem" /%}

## Customizing your incident management workflow{% #customizing-your-incident-management-workflow %}

Datadog Incident Management can be customized with different severity and status levels, based on your organization's needs, and also include additional information such as APM services and teams related to the incident. For more information, see this [section](https://docs.datadoghq.com/incident_response/incident_management/#status-levels) of the Incident Management page.

You can also set up notification rules to automatically notify specific people or services based on an incident's severity level. For more information, see the [Incident Settings](https://docs.datadoghq.com/incident_response/incident_management/incident_settings) documentation.

To customize Incident Management, go to the [incident settings page](https://app.datadoghq.com/incidents/settings). From the Datadog menu on the left-hand side, go to **Monitors** > **Incidents** (if you get an Incident Management welcome screen, click **Get Started**). Then on the top, click **Settings**.

## Create and Manage Incidents on Mobile{% #create-and-manage-incidents-on-mobile %}

The [Datadog Mobile App](https://docs.datadoghq.com/mobile/), available on the [Apple App Store](https://apps.apple.com/app/datadog/id1391380318) and [Google Play Store](https://play.google.com/store/apps/details?id=com.datadog.app), enables users to create, view, search, and filter all incidents you have access to in your Datadog account from the Datadog Mobile App to ensure quick response and resolution without opening your laptop.

You can also declare and edit incidents and quickly communicate to your teams through integrations with Slack, Zoom, and many more.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/iOS_Incident_V2.e869960f9a218c34e15b8b5dbfffbbe0.png?auto=format"
   alt="Two views in the Datadog Mobile App: one showing an incidents list with high-level details about each incident, and one showing a detailed panel for a single incident" /%}

## Further Reading{% #further-reading %}

- [Introduction to Incident Management](https://learn.datadoghq.com/courses/intro-to-incident-management)
- [Datadog on Incident Management](https://www.youtube.com/watch?v=QIambwILy_M)
- [Incident Management](https://docs.datadoghq.com/monitors/incident_management)
- [Join an interactive session to improve your Incident Management](https://dtdg.co/fe)
- [Incident Management with Datadog](https://www.datadoghq.com/blog/incident-response-with-datadog/)
- [Notification Rules](https://docs.datadoghq.com/incident_response/incident_management/incident_settings)
- [Slack integration with incidents](https://docs.datadoghq.com/integrations/slack/?tab=slackapplicationus#using-datadog-incidents)
- [More efficient pair programming with Datadog CoScreen](https://www.datadoghq.com/blog/pair-programming-coscreen-datadog/)
- [Best practices for writing incident postmortems](https://www.datadoghq.com/blog/incident-postmortem-process-best-practices/)
- [How we manage incidents at Datadog](https://www.datadoghq.com/blog/how-datadog-manages-incidents/)
