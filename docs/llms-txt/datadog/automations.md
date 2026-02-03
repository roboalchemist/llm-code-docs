# Source: https://docs.datadoghq.com/incident_response/on-call/automations.md

# Source: https://docs.datadoghq.com/incident_response/incident_management/incident_settings/automations.md

---
title: Automations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Incident Response > Incident Management > Incident Settings >
  Automations
---

# Automations

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

{% image
   source="https://datadog-docs.imgix.net/images/incident_response/incident_automations_workflow.3a4f10c0cc11ab0a7375342e9cd9da26.png?auto=format"
   alt="Incident automations workflow diagram showing automation actions." /%}

Automations enable you to customize and extend incident management to fit your organization's specific processes. Automatically trigger actions based on incident events such as severity changes, or state transitions.

Automations are powered by [Datadog Workflow Automation](https://docs.datadoghq.com/actions/workflows/) and are included in your Incident Management billing at no additional cost.

## Prerequisites{% #prerequisites %}

To create and manage automations, you must have the following permissions:

- `Workflows Write` permission
- `Incident Settings Write` **OR** `Incident Notification Settings Write` permission

To run automations on **private incidents**, use a user or service account with the `Private Incidents Global Access` permission. Without this permission, the automation cannot access incident data.

For more information on permissions, see [Datadog Role Permissions](https://docs.datadoghq.com/account_management/rbac/permissions/#case-and-incident-management).

## Accessing automations{% #accessing-automations %}

Automations are configured per [incident type](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/#incident-types). To manage automations:

1. Navigate to [**Incidents > Settings**](https://app.datadoghq.com/incidents/settings).
1. Select an incident type from the list.
1. Click the **Automations** tab.

From this page, you can view, create, enable, disable, and manage your automations.

{% alert level="info" %}
Any user with `Incident Settings Write` or `Incident Notification Settings Write` permissions can toggle automations on or off. This is true even if they don't have edit access to the automation itself. Administrators can quickly disable problematic automations if needed.
{% /alert %}

## Creating an automation{% #creating-an-automation %}

You can build automations entirely from the Incident Management settings UI. For more advanced workflows, open the automation in the [Workflow Automation](https://docs.datadoghq.com/actions/workflows/) editor to access additional actions and logic capabilities.

When you click **New Automation**, you have two options for building your workflow:

### Start with a blueprint{% #start-with-a-blueprint %}

Blueprints provide pre-configured automation templates for common use cases, such as sending a Slack message to the incident channel. Using a blueprint is the fastest way to get started.

### Choose an action{% #choose-an-action %}

For custom processes, you can build an automation from scratch by starting with an individual action. You can choose from incident-specific actions or explore the full Datadog [Action Catalog](https://app.datadoghq.com/actions/action-catalog), which contains thousands of integrations.

## Configuring triggers and conditions{% #configuring-triggers-and-conditions %}

### Trigger types{% #trigger-types %}

Select when your automation should run:

| Trigger Type                                 | Description                                                                                                                                                                  |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **When the incident is declared**            | Runs once when an incident is first declared and meets the defined conditions.                                                                                               |
| **When the incident is declared or updated** | Runs when an incident is declared or when any field changes that cause the incident to meet the conditions.                                                                  |
| **On a schedule**                            | Runs repeatedly on a per-incident basis (for example, every 10 minutes for each active incident that meets the conditions). Useful for periodic reminders and status checks. |

### Conditions{% #conditions %}

Define conditions to specify which incidents trigger the automation. Conditions are based on incident attributes such as Severity, State, Teams, or other custom property fields.

- **Logic within a row**: Selecting multiple values for a single property (like `SEV-1` and `SEV-2`) uses `OR` logic.
- **Logic across rows**: Adding multiple property filters uses `AND` logic.

**Example**: Set conditions for `severity:SEV-1`, `severity:SEV-2`, and `summary:is empty`. The automation runs when the incident is (SEV-1 **OR** SEV-2) **AND** the summary is empty.

{% image
   source="https://datadog-docs.imgix.net/images/incident_response/incident_automations_conditions.13b0cc61f8e51a8803897869881584fd.png?auto=format"
   alt="Screenshot showing incident automation conditions configuration in Datadog. Displays UI for setting trigger, severity, and summary conditions." /%}

## Building automation workflows{% #building-automation-workflows %}

Automations use the Datadog Workflow Automation engine. Each automation is a workflow that can include multiple actions and logic steps.

### Using incident data{% #using-incident-data %}

Automations have access to all incident data through the `incident` context variable, which includes:

- `incident.id`: The incident's unique identifier
- `incident.attributes`: All incident attributes (severity, state, title, custom fields, and more)
- `incident.fieldDiffs`: A list of fields that changed (for update triggers)

Use these variables in your automation actions by referencing them with curly braces, such as `{{ incident.id }}`.

### Configuring actions{% #configuring-actions %}

Each action in your automation requires configuration. For example, to send a message to an incident's Slack channel:

1. Add the **Get incident Slack channel** action.
1. Set the input parameter to `{{ incident.id }}`.
1. Add the **Send Slack message** action.
1. Configure the message content using incident variables.

The workflow editor provides autocomplete for available variables and validates your configuration.

## Testing automations{% #testing-automations %}

There are two ways to test your automations:

### Option 1: Declare a test incident{% #option-1-declare-a-test-incident %}

1. Enable [test incidents](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/information#test-incidents) in your incident settings.
1. Declare a test incident that matches your automation's conditions.
1. View the automation execution in the incident timeline.

### Option 2: Test from an existing incident{% #option-2-test-from-an-existing-incident %}

1. Open the automation in the workflow editor.
1. Click the **Run** button.
1. Select **Test from incident**.
1. Choose an existing incident to simulate the trigger.

This populates the `incident` context variable with data from the selected incident without actually triggering the automation for that incident.

## Viewing automation executions{% #viewing-automation-executions %}

### From the incident timeline{% #from-the-incident-timeline %}

Every automation execution appears in the [incident timeline](https://docs.datadoghq.com/incident_response/incident_management/investigate/timeline). Timeline entries include:

- The automation name
- Execution timestamp
- Link to the detailed execution view
- Execution status (success or failure)

You can filter the timeline to show only automation executions or exclude them entirely.

### From execution history{% #from-execution-history %}

To view all executions of an automation:

1. Open the automation.
1. Click **Execution** in the workflow editor.

The execution history shows:

- All input parameters and their values
- The `incident` context data
- The `fieldDiffs` showing what changed
- Step-by-step execution results
- Any errors or failures

## Permissions and access control{% #permissions-and-access-control %}

### Edit access{% #edit-access %}

By default, only the automation creator can edit an automation. To grant edit access to others:

1. Open the automation.
1. Click **Edit Access**.
1. Add users or service accounts.
Granting edit access allows others to use the Datadog API as you or as the service account. Use service accounts for shared automations to avoid issues when users leave the organization.
### Service accounts{% #service-accounts %}

Using a service account to run automations provides several benefits:

- Automations continue running if the creator leaves the organization
- Better separation of duties and access control
- Clearer audit trails

To use a service account:

1. Open the automation.
1. Click **Run as Service Account**.
1. Create a new service account with appropriate roles or select an existing one.

You must have the `Service Account Write` permission to configure service accounts for automations.

## Private incidents{% #private-incidents %}

Automations can run on private incidents with the following considerations:

### Required permissions{% #required-permissions %}

To run automations on private incidents, use a user or service account with the `Private Incidents Global Access` permission. Without this permission, the automation cannot access incident data.

### Security considerations{% #security-considerations %}

By default, execution history (including private incident data) is visible to anyone in your organization. To run automations on private incidents securely:

1. Use a service account with `Private Incidents Global Access` permission.
1. Restrict viewer access to only users who should see private incident data.

## Differences from notification rules{% #differences-from-notification-rules %}

Both automations and [notification rules](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/notification_rules) can respond to incident events, but they serve different purposes:

| Feature        | Automations                                | Notification Rules                 |
| -------------- | ------------------------------------------ | ---------------------------------- |
| **Purpose**    | Execute complex workflows and integrations | Send notifications to stakeholders |
| **Triggers**   | Declared, updated, or scheduled            | Declared or updated                |
| **Actions**    | Access to full Datadog Action Catalog      | Limited to notification channels   |
| **Complexity** | Multi-step workflows with logic            | Single notification per rule       |
| **Cost**       | Included in Incident Management            | Included in Incident Management    |

Use notification rules for straightforward notifications and automations for complex, multi-step processes.

## Use cases and examples{% #use-cases-and-examples %}

Use the following examples to help you build your own incident automations.

{% collapsible-section %}
#### Add teams to the incident channel

**Trigger**: When declared or updated**Condition**: Severity is `SEV-1` or `SEV-2`**Actions**:

1. Detect when teams field changes
1. Add new teams to the incident teams list
1. For all users in the team, invite them to the incident slack channel

Access the [blueprint in Datadog](https://app.datadoghq.com/workflow/blueprints/add-datadog-team-to-incident-channel).
{% /collapsible-section %}

{% collapsible-section %}
#### Periodic status reminders

**Trigger**: On a schedule (every 30 minutes)**Condition**: Severity is `SEV-1` or `SEV-2`, State is `Active` or `Stable`**Actions**:

1. Check time since last update
1. Send Slack reminder if > 30 minutes
1. Prompt commander to update incident status

Access the [blueprint in Datadog](https://app.datadoghq.com/workflow/blueprints/nudge-incident-commander-old-incident).
{% /collapsible-section %}

## Further reading{% #further-reading %}

- [Workflow Automation](https://docs.datadoghq.com/actions/workflows/)
- [Notification Rules](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/notification_rules)
