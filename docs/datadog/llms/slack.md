# Source: https://docs.datadoghq.com/incident_response/incident_management/integrations/slack.md

---
title: Integrate Slack with Datadog Incident Management
description: Manage Datadog incidents directly from Slack.
breadcrumbs: >-
  Docs > Incident Response > Incident Management > Incident Integrations >
  Integrate Slack with Datadog Incident Management
---

# Integrate Slack with Datadog Incident Management

## Overview{% #overview %}

Slack is a messaging and collaboration platform widely used by teams to communicate in real time. The Datadog Slack integration connects your incident response workflows directly to Slack, so teams can declare, manage, and resolve incidents without leaving their chat environment.

With the integration, you can:

- Respond faster by declaring Datadog incidents directly from Slack.
- Automatically create Slack channels for collaboration when Datadog incidents are declared.
- Execute your incident response in Slack. For example, page on-call teams, assign responder roles, or update severity.

The Slack integration documentation is organized around the typical lifecycle of using Slack with Incident Management:

1. **Install and connect Slack**: Set up the integration between your Slack workspace and Datadog.
1. **Declare incidents**: Learn how to start incidents using Slack commands or message actions.
1. **Manage incidents from incident channels**: Use dedicated Slack channels with commands, syncing, and automations.
1. **Configure global notifications**: Keep your organization informed with automatic updates.
1. **Reference Slack configuration options and Slack commands**: Explore detailed configuration options and see the full list of available Slack commands to tailor and streamline your incident response workflows.

## Prerequisites{% #prerequisites %}

Install the integration through the [Slack Integration tile](https://app.datadoghq.com/integrations/slack/) with the proper [OAuth scopes](https://docs.datadoghq.com/integrations/slack/?tab=datadogforslack#permissions). For more information, see the [Slack integration](https://docs.datadoghq.com/integrations/slack/?tab=datadogforslack) documentation.

After the integration is installed, navigate to [**Incidents** > **Settings** > **Integrations**](https://app.datadoghq.com/incidents/settings#Integrations) to enable Slack capabilities for Incident Management.

## Declaring incidents from Slack{% #declaring-incidents-from-slack %}

When you connect a Slack workspace to a Datadog organization, users in the workspace can use Slack shortcuts related to Incident Management.

You can declare an incident with the following slash command:

```
/datadog incident
```

To declare an incident from a Slack message, hover over the message, click **More actions** (the three vertical dots), and select **Declare incident**. Datadog posts a message to the message's thread confirming the incident's creation.

By default, only Slack users connected to a Datadog organization can declare incidents. Slack users can connect to a Datadog organization by running `/datadog connect`.

To allow any Slack user in the workspace to declare incidents, enable **Allow Slack users to declare incidents without a connected Datadog account** in Incident Management settings.

## Incident channels{% #incident-channels %}

You can configure Incident Management to automatically create a dedicated Slack channel for each incident that meets criteria you define. Your responders can then manage the incident directly in Slack from the incident channel.

To use incident channels, go to **[Incident Response > Incident Management > Settings > Integrations](https://app.datadoghq.com/incidents/settings#Integrations)** and enable **Create Slack channels for incidents**.

The **channel name template** you define determines how Datadog names the incident channels it creates. The following variables are available in channel name templates:

- `{{public_id}}`: Incident's numeric ID
- `{{title}}`: Incident's title
- `{{created}}`: Incident's creation date in format MM_DD_YYYY
- `{{yyyy}}`: Incident's four-digit creation year
- `{{mm}}`: Incident's two-digit creation month
- `{{dd}}`: Incident's two-digit creation day of month
- `{{random_adjective}}`: Random adjective
- `{{random_noun}}`: Random noun

### Message syncing (Slack mirroring){% #message-syncing-slack-mirroring %}

After enabling automatic channel creation, you can configure Incident Management to sync messages between an incident Slack channel and the incident's timeline in Datadog.

To enable syncing, enable **Push Slack channel messages to the incident timeline** in Incident Management settings, and then select one of the following options:

- **Mirror all messages in real-time**: Datadog syncs all messages posted by Slack users to the incident channel.
- **Push message when ð is added as a reaction**: Datadog syncs messages only when Slack users react to them with pushpins (ð).

For both options, a message's author does not need to be connected to the Datadog organization for Datadog to sync the message. For message pinning, the pinner **does** need to be connected to the Datadog organization for the message pinned to sync.

In organizations with usage-based Incident Management billing:

- Authoring a message that is synced to Datadog does **not** make you a billable user for the current month.
- Pinning a message that is then synced **does** make you a billable user.

In organizations with seat-based Incident Management billing:

- You do **not** need a seat for Datadog to sync your messages to Incident Management.
- When you pin a message, you **must** have a seat for Datadog to sync the message you pinned.

### Slack commands in the incident channel{% #slack-commands-in-the-incident-channel %}

In an incident Slack channel, you can run Slack commands to modify the incident's states and severity, assign responder roles, page on-call teams, and more.

For a full list of Slack commands, see Slack commands.

### Other incident channel configuration options{% #other-incident-channel-configuration-options %}

Access all configuration options for Slack in Incident Management through the [**Incidents** > **Settings** > **Integrations**](https://app.datadoghq.com/incidents/settings#Integrations) page.

| Feature                                                   | Description & Notes                                                                                                                     |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Push incident timeline messages to Slack**              | Automatically send incident timeline updates from Datadog to the Slack channel.Keeps channel participants in-sync with Datadog updates. |
| **Add important links to channel bookmarks**              | Post incident-related links in the Slack channel bookmarks.Provides convenient access to resources.                                     |
| **Add team members automatically**                        | When a Datadog team is added to the incident, its members are added to the Slack channel.                                               |
| **Send incident updates to the Slack channel**            | Update the channel topic with incident state, severity, and incident commander.                                                         |
| **Send a Slack notification when a meeting starts**       | Notify the Slack channel when a meeting is started, with participants and a join link.Provides convenient access to incident calls.     |
| **Activate Bits AI in incident Slack channels**           | Enable AI features that use incident context from Datadog.Applies to all incident types in the selected Slack workspace.                |
| **Automatically archive Slack channels after resolution** | Archive incident Slack channels once the incident is resolved.Helps reduce channel clutter.                                             |

## Global channel for incident updates{% #global-channel-for-incident-updates %}

You can configure Incident Management to automatically post updates about incidents to a selected Slack channel. To enable this:

1. In Datadog, navigate to **[Incident Response > Incident Management > Settings > Integrations](https://app.datadoghq.com/incidents/settings#Integrations)**.
1. In the Slack section, enable **Send all incident updates to a global channel**.
1. Select the Slack workspace and Slack channel where you want the incident updates to be posted.

Datadog automatically notifies the selected channel about any newly declared incidents, as well as changes to incident states, severities, and incident commanders.

Under the hood, this feature is a built-in, hidden [incident notification rule](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/notification_rules/). If you would like to customize the message or its triggers, disable it and define your own notification rule.

## Slack commands{% #slack-commands %}

You can view the full list of available Slack commands at any time by typing `/dd help` or `/datadog help` in Slack. This will open the command reference directly in your Slack workspace. To open the action tray for common incident management actions, type `/datadog`.

### Global commands (run anywhere){% #global-commands-run-anywhere %}

| Command                  | Description                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------- |
| `/datadog incident`      | Declare a new incident.                                                            |
| `/datadog incident test` | Declare a new test incident (if test incidents are enabled for the incident type). |
| `/datadog incident list` | List all open (active and stable) incidents.                                       |

### Incident channel commands{% #incident-channel-commands %}



{% callout %}
# Important note for users on the following Datadog sites: app.datadoghq.com, us3.datadoghq.com, us5.datadoghq.com, app.datadoghq.eu, ap1.datadoghq.com, ap2.datadoghq.com



| Command                        | Description                                                                     |
| ------------------------------ | ------------------------------------------------------------------------------- |
| `/datadog`                     | Open the incident action tray to perform common actions.                        |
| `/datadog incident update`     | Update the incident state, severity, or other attribute of the incident.        |
| `/datadog incident notify`     | Notify `@`-handles about the incident.                                          |
| `/datadog incident private`    | Make the incident private (if private incidents are enabled).                   |
| `/datadog incident public`     | Make the incident public.                                                       |
| `/datadog incident responders` | Manage the incident's response team (add responders and assign response roles). |
| `/datadog task`                | Create an incident task.                                                        |
| `/datadog task list`           | List existing incident tasks.                                                   |
| `/datadog followup`            | Create a follow-up for the incident.                                            |
| `/datadog followup list`       | View and manage existing follow-ups for the incident.                           |
| `/datadog incident summary`    | Get an AI-generated summary of the incident that is visible only to you.        |


{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



| Command                        | Description                                                                     |
| ------------------------------ | ------------------------------------------------------------------------------- |
| `/datadog`                     | Open the incident action tray to perform common actions.                        |
| `/datadog incident update`     | Update the incident state, severity, or other attribute of the incident.        |
| `/datadog incident notify`     | Notify `@`-handles about the incident.                                          |
| `/datadog incident private`    | Make the incident private (if private incidents are enabled).                   |
| `/datadog incident public`     | Make the incident public.                                                       |
| `/datadog incident responders` | Manage the incident's response team (add responders and assign response roles). |
| `/datadog task`                | Create an incident task.                                                        |
| `/datadog task list`           | List existing incident tasks.                                                   |
| `/datadog followup`            | Create a follow-up for the incident.                                            |
| `/datadog followup list`       | View and manage existing follow-ups for the incident.                           |


{% /callout %}



## Further reading{% #further-reading %}

- [Install the Slack Integration](https://docs.datadoghq.com/integrations/slack/)
- [In-app Slack integration tile](https://app.datadoghq.com/integrations/slack)
- [Manage incidents seamlessly with the Datadog integration for Slack](https://www.datadoghq.com/blog/slack-incident-management/)
