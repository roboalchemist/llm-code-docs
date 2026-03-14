# Source: https://plivo.com/docs/aiagent/human/agentstatus.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Agent Status

> Manage agent availability states to control routing behavior 

Agent statuses help determine whether an agent is eligible to receive new conversations. They can be system-defined (default) or custom-defined by admins and are used in routing decisions throughout the platform.

## Creating and Managing Custom Statuses

<Frame>
    <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/aiagent/images/status1.png?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=ff6fa3fad9ea220a904b15ae6e567d37" alt="" width="2378" height="1030" data-path="aiagent/images/status1.png" />
</Frame>

Admins can add new statuses by specifying:

* **Name**
* **Status Color**
* **Availability Type** (Available / Unavailable)

> Note: Custom statuses can be edited and rearranged, but not deleted once created.

## Default Statuses

The following statuses are automatically created when a new account is set up:

| Status                 | Color     | Availability |
| :--------------------- | :-------- | :----------- |
| **Available**          | 🟢 Green  | Available    |
| **Idle**               | 🟠 Yellow | Unavailable  |
| **Busy**               | 🔴 Red    | Unavailable  |
| **After Contact Work** | 🔴 Red    | Unavailable  |
| **Away**               | 🟠 Yellow | Unavailable  |
| **Offline**            | ⚪ Gray    | Unavailable  |

* These statuses **can be edited (renamed) and reordered**, but **cannot be deleted**.
* The **order of statuses** impacts display priority in some interfaces.

## Configurations

<Frame>
  <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/aiagent/images/status2.png?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=ea58bb289c744198a58c4c571bb4bba1" width="1868" height="1320" data-path="aiagent/images/status2.png" />
</Frame>

Navigate to the **Configurations** tab to set automation rules:

### Default State on Login Events

* **Sign-in Status**: Set the default status when agents log in.
* **Sign-out Status**: Set the default status on logout.

### Idle Timeout Automation

Admins can configure auto-switching for agents who are idle:

* **Enable idle tracking**
* Define **inactivity duration** (in minutes)
* Select the fallback **status to switch to**

Example: After 30 minutes of inactivity, status auto-switches from Available to Idle.

## Agent Options

Agents can manually update their current status from their **profile menu** (bottom-right of the screen). This allows them to reflect real-time availability like:

* Switching to *Busy* during ongoing tasks
* Returning to *Available* after breaks
* Logging out with *Offline*
