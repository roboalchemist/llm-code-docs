# Source: https://docs.rootly.com/incidents/action-items/action-items.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Action Items Overview

> Understand how action items—including tasks and follow-ups—help teams drive effective incident response and long-term reliability improvements.

### How Action Items Work

Action items are structured pieces of work created during or after an incident. They help teams capture urgent tasks, assign ownership, track accountability, and ensure important follow-up work is completed.

Action items live alongside the incident timeline, Slack workflows, retrospectives, and analytics—providing full visibility into what was done during an incident and what still needs to be done.

This page introduces how action items work, why they matter, and where they fit into the incident lifecycle.

***

### Why Action Items Matter

During fast-moving incidents, it’s easy for important work to be forgotten. Action items help by:

* Capturing tasks needed to investigate or mitigate the issue
* Tracking follow-up work after the incident to prevent recurrence
* Assigning clear ownership so nothing is lost
* Providing structure for retrospectives and improvement planning
* Enabling automation through workflows and integrations
* Improving accountability and long-term system reliability

Common examples include:

* **Task** – “Restart service X on cluster Y.”
* **Task** – “Verify the hotfix on canary pods.”
* **Follow-up** – “Add alerting for cache saturation.”
* **Follow-up** – “Update the API runbook with new mitigation steps.”

<Info>
  Action items are fully customizable and can be created from the Web UI, Slack, API, Workflows, or even tied to specific Incident Roles.
</Info>

***

### Types of Action Items

Action items come in two forms, each serving a different purpose in the response lifecycle.

#### **Tasks — Work During the Incident**

Tasks represent operational or investigative work that helps move the incident toward mitigation or resolution.

Tasks typically include:

* **Title** (required)
* Description (Markdown supported)
* **Assignee** (user or group)
* Priority (High, Medium, Low)
* Status (Open, In Progress, Done, Cancelled)
* Optional reminder (5–180 minutes)

#### **Follow-Ups — Work After the Incident**

Follow-ups help teams improve reliability after the incident is over. They are usually completed post-resolution.

Follow-ups include:

* **Title** (required)
* Description (Markdown supported)
* Priority
* **Assignee** (user or group)
* **Due date**
* Status

<Info>
  Follow-ups are often reviewed and assigned during retrospectives, making them a critical part of continuous improvement.
</Info>

***

### Where Action Items Live in Rootly

#### **On the Incident Timeline (Web UI)**

Every task or follow-up appears directly on the timeline, keeping work tied to the context of the incident. Responders can:

* Create or edit items
* Assign or reassign owners
* Update status or priority
* Open linked JIRA / Linear / GitHub issues (if integrated)

#### **In Slack**

If Slack is integrated, responders can create and manage action items without leaving the incident channel:

* `/rootly task`
* `/rootly followup`
* `/rootly add action item`
* `/rootly action items` (manage existing items)

Slack modals support assignment, priority, reminders, and descriptions.

#### **In the Web Interface**

Each incident has an **Action Items** section where teams can:

* Filter by priority, type, or status
* Bulk-review outstanding work
* Export action items to CSV, JSON, or XML
* Manage all items across all incidents from a global dashboard

#### **In Workflows**

Workflows can create tasks or follow-ups automatically based on:

* Severity
* Impacted services
* Incident type
* Sub-status changes
* Timeline events
* Role assignments
* Custom logic

Automation ensures important tasks are created consistently and early.

#### **Through the API**

Developers can programmatically create or update items:

```
POST /api/v1/teams/:team_id/incidents/:incident_id/action_items
```

The API supports full lifecycle management, including due dates, priority, and linking external issue IDs.

***

### How Action Items Support the Response Process

Action items help orchestrate the human work that happens around incidents:

* Timeline entries show when items were created, updated, or completed
* Slack channel summaries update dynamically as items change
* Workflow triggers can depend on action item status or presence
* Retrospectives include a full list of tasks and follow-ups for review
* Analytics dashboards help track overdue items, recurrence, and team performance
* Permissions determine who can create, edit, or complete action items

<Info>
  When paired with roles and workflows, action items create a structured, predictable response process across teams.
</Info>

***

### Where to Go Next

These pages will help you manage action items across all interfaces:

* **Add via Slack** – Create tasks or follow-ups using Slack commands
* **Add via Web Interface** – Add items directly from the incident page
* **Add via API** – Programmatically create items from external systems
* **Add via Email** – Append email-based action items when responding to incident emails
* **Incident Roles** – Automatically create action items based on role responsibilities
* **Workflows** – Generate tasks and follow-ups automatically based on incident conditions

***

### Best Practices

* **Create tasks early**\
  Capture investigative work as soon as it emerges.

* **Use follow-ups for durable improvements**\
  These often prevent recurrence.

* **Assign owners immediately**\
  Unassigned tasks often go stale.

* **Set due dates for follow-ups**\
  This increases accountability and helps with retrospective follow-through.

* **Use priorities intentionally**\
  High-priority follow-ups should be reviewed in retrospectives or weekly ops meetings.

* **Automate repetitive items**\
  Workflow-generated tasks ensure consistent coverage.

* **Review open follow-ups regularly**\
  Keeps your reliability improvement backlog healthy.

***

### FAQ

<AccordionGroup>
  <Accordion title="Do all incidents need action items?" iconType="thin">
    No. Smaller or operationally simple incidents may not require tasks or follow-ups.
  </Accordion>

  <Accordion title="Can multiple people be assigned to a single action item?">
    One user may own the item, but **multiple groups** can also be assigned for shared accountability.
  </Accordion>

  <Accordion title="Can action items support Markdown formatting?">
    Yes. Descriptions fully support Markdown for links, formatting, and structured notes.
  </Accordion>

  <Accordion title="Can workflows automatically create tasks or follow-ups?">
    Yes. This is one of the most powerful features of Rootly’s workflows for predictable processes.
  </Accordion>

  <Accordion title="Do action items appear in retrospectives?">
    Yes. All tasks and follow-ups associated with an incident appear in the retrospective for review.
  </Accordion>

  <Accordion title="Can I integrate tasks with JIRA, Linear, GitHub, etc.?">
    Yes. Action items support external issue linking for teams who track work in external systems.
  </Accordion>

  <Accordion title="What happens when an incident is resolved?">
    Tasks may be completed, and remaining work typically becomes follow-ups. Some orgs disable new task creation after resolution.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).