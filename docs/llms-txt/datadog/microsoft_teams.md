# Source: https://docs.datadoghq.com/incident_response/incident_management/integrations/microsoft_teams.md

---
title: Integrate Microsoft Teams with Datadog Incident Management
description: >-
  Integrate Microsoft Teams with Datadog Incident Management to automate
  incident channel creation, synchronize messages, and collaborate with your
  team directly within Microsoft Teams.
breadcrumbs: >-
  Docs > Incident Response > Incident Management > Incident Integrations >
  Integrate Microsoft Teams with Datadog Incident Management
---

# Integrate Microsoft Teams with Datadog Incident Management

## Overview{% #overview %}

The Microsoft Teams integration for Datadog Incident Management enables you to declare and manage incidents, automatically create incident channels, sync messages to timelines, and keep your team informed, all from within Microsoft Teams.

## Prerequisites{% #prerequisites %}

To use Incident Management's Microsoft Teams features, you must first [install the Microsoft Teams integration for Datadog](https://docs.datadoghq.com/integrations/microsoft-teams/?tab=datadogapprecommended) and connect your Microsoft Teams account to your Datadog account.

After installation, go to **[Incident Response > Incident Management > Settings > Integrations](https://app.datadoghq.com/incidents/settings#Integrations)** to configure the Microsoft Teams features for Incident Management.

## Incident channels{% #incident-channels %}

### Automatic channel creation{% #automatic-channel-creation %}

You can configure Incident Management to automatically create an incident Microsoft Teams channel for each incident or for incidents meeting criteria you define. To set up automatic incident channel creation:

1. Navigate to [Incident Settings](https://app.datadoghq.com/incidents/settings#Integrations) and select **Microsoft Teams**.
1. From the **Tenant** dropdown, select your connected Microsoft Teams tenant.
1. Toggle on **Automatically create a Microsoft Teams channel for every incident**.
1. Select the Team in which you want to automatically create new channels.
1. Save your settings.

After you enable this automation, you can define a **channel name template** for Datadog to follow when creating the channel. The following variables are available in channel name templates:

- `{{public_id}}`: Incident's numeric ID
- `{{title}}`: Incident's title
- `{{created}}`: Incident's creation date in format MM_DD_YYYY
- `{{yyyy}}`: Incident's four-digit creation year
- `{{mm}}`: Incident's two-digit creation month
- `{{dd}}`: Incident's two-digit creation day of month
- `{{random_adjective}}`: Random adjective
- `{{random_noun}}`: Random noun

### Channel message syncing{% #channel-message-syncing %}

You can configure Incident Management to push all incident Microsoft Teams channel messages to the incident timeline.

The author of a synced message does not need an Incident Management or Incident Response seat for the message to be recorded. In organizations with usage-based billing for Incident Management, the author is not counted as a monthly active user.

### Automatic channel archiving{% #automatic-channel-archiving %}

You can configure Incident Management to automatically archive an incident channel after the incident is resolved.

## Global channel for incident updates{% #global-channel-for-incident-updates %}

Use an incident updates channel to provide your stakeholders with organization-wide visibility into the status of all incidents directly from Microsoft Teams.

1. In Datadog, navigate to **[Incident Response > Incident Management > Settings > Integrations](https://app.datadoghq.com/incidents/settings#Integrations)**.
1. Select the Microsoft Teams integration and enable **Send all incident updates to a global channel**.
1. Select the Team and channel where you want the incident updates to be posted.

Datadog automatically notifies the selected channel about any newly declared incidents, as well as changes to incident states, severities, and incident commanders.

To customize this behavior, deactivate this setting and [define a notification rule](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/notification_rules) instead.

## Microsoft Teams meetings{% #microsoft-teams-meetings %}

### One-click meeting creation{% #one-click-meeting-creation %}

Delegated permissions are required for one-click Microsoft Teams meetings. To enable one-click Microsoft Teams meetings for incidents:

1. Navigate to [Incident Settings](https://app.datadoghq.com/incidents/settings#Integrations).
1. In Microsoft Teams, select your connected Microsoft Teams tenant.
1. Toggle on **Enable meeting creation**.
1. Save your settings.

After enabling one-click Microsoft Teams meetings, start a meeting by clicking **Start Teams Meeting** from the incident header. You are redirected to instantly join the meeting through the browser.

### Automatic meeting creation{% #automatic-meeting-creation %}

Delegated permissions are required for automatic, criteria-based Microsoft Teams meetings. To enable automatic, criteria-based Microsoft Teams meetings for incidents:

1. Navigate to [Incident Settings](https://app.datadoghq.com/incidents/settings#Integrations).
1. In Microsoft Teams, select your connected Microsoft Teams tenant.
1. Toggle on **Enable meeting creation**.
   1. Toggle on **Automatically create Microsoft Teams meetings**.
   1. (Optional) Specify the incident criteria that creates a Microsoft Teams meeting. If left blank, any changes to an incident without an existing Microsoft Teams meeting will create a Microsoft Teams meeting.
1. Save your settings.

## Using the Datadog tab in Microsoft Teams{% #using-the-datadog-tab-in-microsoft-teams %}

In an incident channel (a channel created specifically for an incident) the Datadog tab displays that specific incident's information and allows you to manage it. In non-incident channels, you can only declare new incidents.

### Declaring and managing incidents{% #declaring-and-managing-incidents %}

To declare an incident from a specific team:

1. [Add the Datadog application](https://docs.datadoghq.com/integrations/microsoft-teams/?tab=datadogapprecommended#datadog-incident-management-in-microsoft-teams) to the team.
1. In any **non-incident** channel, click on the **Datadog** tab.
1. Fill out the incident details and click **Declare Incident**.

To manage an incident from a specific team:

1. In an **incident channel**, click on the **Datadog** tab.
1. Edit the incident details and attributes.

### Sending messages to the timeline{% #sending-messages-to-the-timeline %}

Use the "More actions" menu on any message inside an incident team on the far right to send that message to the incident timeline.

## Microsoft Teams commands{% #microsoft-teams-commands %}

You can view the full list of available commands at any time by typing `@Datadog help` in Microsoft Teams.

| Category                       | Command                            | Description             |
| ------------------------------ | ---------------------------------- | ----------------------- |
| Global commands (run anywhere) | `@Datadog incident`                | Declare a new incident. |
| `@Datadog list incidents`      | Show a list of all open incidents. |
| `@Datadog help`                | Show all supported commands.       |

## Further reading{% #further-reading %}

- [Incident Integrations Settings](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/integrations)
- [Microsoft Teams Integration](https://docs.datadoghq.com/integrations/microsoft-teams)
