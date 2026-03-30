# Source: https://docs.rootly.com/workflows/workflow-types.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Workflow Types

> Understand the six workflow types (incident, post-mortem, action item, alert, pulse, and standalone) and the trigger events available for each.

## Overview

Rootly workflows are grouped into **six workflow types**. The workflow type determines two things:

1. **What object the workflow runs against** (incident, alert, action item, etc.)
2. **Which trigger events are available** (because not every object emits the same events)

Most workflow types are tied to a Rootly object and are triggered by changes to that object. For example, an **Incident workflow** can trigger when an incident’s status changes, while an **Action Item workflow** can trigger when a due date changes.

**Standalone workflows** (called **Simple** workflows in Rootly’s internal model) are different: they do not depend on any Rootly object and can only be triggered manually through a Slack command.

<Note>
  You can chain workflow types together. For example, an **Alert workflow** can create an incident, which can then trigger one or more **Incident workflows** configured for **Incident Created** or **Incident Started**.
</Note>

## How Trigger Events Work

Workflows are **not executed in a fixed order**. A workflow runs when:

1. One of its **trigger events** occurs (triggers are evaluated using OR logic), and then
2. Its **run conditions** pass (if configured)

Because workflows are event-driven, two workflows can run “in parallel” if they share the same trigger, and a workflow configured with multiple triggers will run whenever *any* of them occur.

<Warning>
  ### Avoid Overlapping Triggers

  Some triggers are **catch-all** events (for example, **Incident Updated**) that already include more specific triggers (like **Status Updated** or **Severity Updated**). Rootly prevents overlapping configurations to avoid duplicate runs and hard-to-debug behavior.
</Warning>

***

## Workflow Types and Trigger Events

Below are the trigger events grouped by workflow type. These names reflect how Rootly defines triggers internally and how they appear in the workflow builder.

***

## Incident Workflows

Incident workflows trigger from incident lifecycle changes, field updates, timeline events, channel events, and subscriber changes.

| Trigger                             | When it’s triggered                                                                                                             |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Incident In Triage**              | When an incident enters triage (used for triage-first workflows).                                                               |
| **Incident Created**                | When an incident record is created in Rootly.                                                                                   |
| **Incident Started**                | When an incident is started (for teams that distinguish creation vs start).                                                     |
| **Incident Updated**                | Catch-all trigger for incident updates. Use this instead of specific field update triggers when you want “any incident change.” |
| **Status Updated**                  | When incident status changes.                                                                                                   |
| **Severity Updated**                | When incident severity changes.                                                                                                 |
| **Title Updated**                   | When incident title changes.                                                                                                    |
| **Summary Updated**                 | When incident summary changes.                                                                                                  |
| **Visibility Updated**              | When incident visibility changes (for example, public vs private, depending on your configuration).                             |
| **Environments Added**              | When a value is added to environments.                                                                                          |
| **Environments Removed**            | When a value is removed from environments.                                                                                      |
| **Environments Updated**            | When the environments list changes (covers add/remove).                                                                         |
| **Incident Types Added**            | When a value is added to incident types.                                                                                        |
| **Incident Types Removed**          | When a value is removed from incident types.                                                                                    |
| **Incident Types Updated**          | When incident types list changes (covers add/remove).                                                                           |
| **Services Added**                  | When a service is added.                                                                                                        |
| **Services Removed**                | When a service is removed.                                                                                                      |
| **Services Updated**                | When services list changes (covers add/remove).                                                                                 |
| **Functionalities Added**           | When a functionality is added.                                                                                                  |
| **Functionalities Removed**         | When a functionality is removed.                                                                                                |
| **Functionalities Updated**         | When functionalities list changes (covers add/remove).                                                                          |
| **Teams Added**                     | When a team is added.                                                                                                           |
| **Teams Removed**                   | When a team is removed.                                                                                                         |
| **Teams Updated**                   | When teams list changes (covers add/remove).                                                                                    |
| **Causes Added**                    | When a cause is added.                                                                                                          |
| **Causes Removed**                  | When a cause is removed.                                                                                                        |
| **Causes Updated**                  | When causes list changes (covers add/remove).                                                                                   |
| **Role Assignments Added**          | When an incident role assignment is added.                                                                                      |
| **Role Assignments Removed**        | When an incident role assignment is removed.                                                                                    |
| **Role Assignments Updated**        | When a role assignment changes (assign/reassign/unassign).                                                                      |
| **Timeline Updated**                | When a timeline event is added, updated, or removed.                                                                            |
| **Status Page Timeline Updated**    | When a status page timeline event is added, updated, or removed.                                                                |
| **Slack Channel Created**           | When an incident Slack channel is created for the incident.                                                                     |
| **Slack Channel Converted**         | When an existing Slack channel is converted into an incident channel.                                                           |
| **Microsoft Teams Channel Created** | When a Microsoft Teams channel is created for the incident (if enabled).                                                        |
| **User Joined Slack Channel**       | When a user joins the incident Slack channel.                                                                                   |
| **User Left Slack Channel**         | When a user leaves the incident Slack channel.                                                                                  |
| **Subscribers Added**               | When a subscriber is added.                                                                                                     |
| **Subscribers Removed**             | When a subscriber is removed.                                                                                                   |
| **Subscribers Updated**             | When subscriber list changes (covers add/remove).                                                                               |
| **Slack Command**                   | When the workflow is manually triggered via Slack command.                                                                      |

<Note>
  ### Important: “Created” vs “Slack Channel Created”

  If you select **Incident Created**, you generally should not also select **Slack Channel Created** for the same workflow unless you explicitly want separate runs. Rootly guards against trigger overlap patterns that would produce redundant firing.
</Note>

***

## Post-mortem Workflows (Retrospectives)

Post-mortem workflows trigger based on retrospective creation/updates and retrospective status changes.

| Trigger                 | When it’s triggered                                        |
| ----------------------- | ---------------------------------------------------------- |
| **Post Mortem Created** | When a post-mortem (retrospective) is created.             |
| **Post Mortem Updated** | Catch-all trigger for post-mortem updates.                 |
| **Status Updated**      | When post-mortem status changes.                           |
| **Slack Command**       | When the workflow is manually triggered via Slack command. |

<Info>
  Post-mortem workflows do not use a dedicated “Causes Updated” trigger. If your process depends on causes, use **Post Mortem Updated** (with run conditions) or condition on causes directly where supported.
</Info>

***

## Action Item Workflows

Action item workflows trigger based on action item lifecycle changes and field updates. They also support a catch-all update trigger.

| Trigger                   | When it’s triggered                                                              |
| ------------------------- | -------------------------------------------------------------------------------- |
| **Action Item Created**   | When an action item is created.                                                  |
| **Action Item Updated**   | Catch-all trigger for action item updates.                                       |
| **Assigned User Updated** | When the assigned user changes.                                                  |
| **Summary Updated**       | When the summary changes.                                                        |
| **Description Updated**   | When the description changes.                                                    |
| **Status Updated**        | When the status changes.                                                         |
| **Priority Updated**      | When the priority changes.                                                       |
| **Due Date Updated**      | When the due date changes.                                                       |
| **Teams Updated**         | When the assigned team(s) changes.                                               |
| **Incident Updated**      | When the linked incident updates (useful when action items are incident-driven). |
| **Slack Command**         | When the workflow is manually triggered via Slack command.                       |

***

## Alert Workflows

Alert workflows trigger from alert creation and alert lifecycle changes.

| Trigger                  | When it’s triggered                  |
| ------------------------ | ------------------------------------ |
| **Alert Created**        | When an alert is received in Rootly. |
| **Alert Status Updated** | When an alert status changes.        |

***

## Pulse Workflows

Pulse workflows trigger from pulse ingestion events.

| Trigger           | When it’s triggered                 |
| ----------------- | ----------------------------------- |
| **Pulse Created** | When a pulse is received in Rootly. |

***

## Standalone Workflows (Simple)

Standalone workflows do not run against a Rootly object. They are manually triggered and are ideal for “utility” workflows (for example, running a set of Slack actions on demand).

| Trigger           | When it’s triggered                                        |
| ----------------- | ---------------------------------------------------------- |
| **Slack Command** | When the workflow is manually triggered via Slack command. |

***

## Best Practices

* **Prefer specific triggers when possible.** If you only care about severity changes, use **Severity Updated** rather than **Incident Updated**.
* **Use catch-all triggers intentionally.** Catch-all triggers are powerful, but can lead to high execution volume if paired with broad conditions.
* **Avoid redundancy.** If two triggers represent the same functional event for your use case, pick the one you actually want to represent “start.”
* **Design for chaining.** A common pattern is: Alert workflow → create incident → Incident workflow → run structured response actions.
* **Test with narrow scopes first.** Start by scoping run conditions tightly (severity/team/service), confirm behavior, then expand.

***

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Why don’t workflows run in a predictable order?">
    Workflows are event-driven. They execute when their trigger event fires and their conditions pass—not because they are “first” or “second” in a sequence. If multiple workflows listen to the same trigger, they may run around the same time.
  </Accordion>

  <Accordion title="When should I use a catch-all trigger like Incident Updated?">
    Use a catch-all trigger when you truly want to react to *any* update on that object, then refine behavior using run conditions. If you only care about a specific change (like Status Updated), prefer the specific trigger to reduce noise and unintended execution.
  </Accordion>

  <Accordion title="Can I use Slack commands for every workflow type?">
    Slack Command triggers are available on several workflow types (including Incident, Post-mortem, Action Item, and Standalone). Alert and Pulse workflows are designed to run from ingestion and lifecycle events instead of manual command triggers.
  </Accordion>

  <Accordion title="Can one workflow trigger another workflow?">
    Yes. If a workflow action causes another object event (for example, creating an incident from an alert), any workflows listening for that downstream event can run. This is a common way to build multi-stage automation.
  </Accordion>

  <Accordion title="Why does Rootly warn about overlapping triggers?">
    Some triggers are broad and implicitly include other triggers (for example, an object-level “Updated” trigger covering multiple specific field changes). Overlaps can cause duplicate workflow runs and confusing behavior, so Rootly prevents or warns on combinations that represent the same logical event.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).