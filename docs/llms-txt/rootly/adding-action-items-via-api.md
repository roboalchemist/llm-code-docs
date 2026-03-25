# Source: https://docs.rootly.com/incidents/action-items/adding-action-items-via-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating Action Items via Automation & API

> Automate action item creation through workflows, incident roles, and direct API integration for scalable incident response processes.

### How Automation Creates Action Items

Action items—tasks and follow-ups—can be generated automatically through **Workflows**, **Incident Roles**, or the **Rootly API**. Automation ensures teams never miss a critical task, follow-up, or improvement opportunity during or after an incident.

Automation is especially powerful for:

* Enforcing consistent response processes
* Creating tasks or follow-ups automatically based on incident conditions
* Routing work to the correct owners
* Producing reliable audit trails
* Integrating with tools such as Jira, GitHub, and Slack

<Info>
  Automation reduces operational overhead and ensures every incident produces actionable, trackable work.
</Info>

***

### Action Items and Workflows

Workflows can both **create** and **react to** action items using a variety of triggers and conditions.

#### Supported Workflow Triggers (Action Item Category)

Rootly supports the following action-item–related triggers:

* `incident_updated`
* `action_item_created`
* `action_item_updated`
* `assigned_user_updated`
* `summary_updated`
* `description_updated`
* `status_updated`
* `priority_updated`
* `due_date_updated`
* `teams_updated`
* `slack_command`

#### Workflow Conditions

Workflows can filter based on:

* Action item type (Task / Follow-up)
* Status
* Priority
* Incident severity
* Visibility
* Incident kind
* Incident roles
* Other incident attributes (teams, services, etc.)

<Info>
  Conditions and triggers map directly to code-backed enums and workflow schemas, ensuring strict validation and predictable automation.
</Info>

***

#### Example: Workflow **creates** a task when the Security team is added

<Info>
  **Trigger**

  * Teams added

  **Conditions**

  * Kind → Incident
  * Team → is one of → Security

  **Action**

  * Create a task to alert the Legal team
</Info>

***

#### Example: Workflow **reacts to** a new action item

<Info>
  **Trigger**

  * Action item created

  **Conditions**

  * Type → Task
  * Priority → High

  **Action**

  * Create an external ticket (e.g., Jira, GitHub, GitLab, Linear)
</Info>

<Info>
  Workflow tasks are grouped by integration. Jira actions, for example, appear under the Jira task group and require the Jira integration to be enabled.
</Info>

***

### Action Items and Incident Roles

Incident Roles can include predefined tasks that are automatically converted into incident action items when an incident is created.

These role-based tasks carry:

* Summary
* Priority
* Role assignment metadata
* Ordering/position

### To configure:

1. Go to **Configuration → Roles**
2. Select a role
3. Open the **Tasks** tab
4. Add or reorder tasks

<Info>
  Role-based action items give each incident a predictable starting checklist and ensure operational discipline.
</Info>

Learn more about [Incident Roles](https://docs.rootly.com/configuration/incident-roles).

***

### Action Items and the API

The Rootly API allows programmatic creation, management, and retrieval of action items.

#### Endpoints

* **List incident action items**\
  [https://docs.rootly.com/api-reference/incidentactionitems/list-incident-action-items](https://docs.rootly.com/api-reference/incidentactionitems/list-incident-action-items)

* **Create an incident action item**\
  [https://docs.rootly.com/api-reference/incidentactionitems/creates-an-incident-action-item](https://docs.rootly.com/api-reference/incidentactionitems/creates-an-incident-action-item)

* **Retrieve an incident action item**\
  [https://docs.rootly.com/api-reference/incidentactionitems/retrieves-an-incident-action-item](https://docs.rootly.com/api-reference/incidentactionitems/retrieves-an-incident-action-item)

* **Update an incident action item**\
  [https://docs.rootly.com/api-reference/incidentactionitems/update-an-incident-action-item](https://docs.rootly.com/api-reference/incidentactionitems/update-an-incident-action-item)

* **Delete an incident action item**\
  [https://docs.rootly.com/api-reference/incidentactionitems/delete-an-incident-action-item](https://docs.rootly.com/api-reference/incidentactionitems/delete-an-incident-action-item)

* **List all action items for an organization**\
  [https://docs.rootly.com/api-reference/incidentactionitems/list-all-action-items-for-an-organization](https://docs.rootly.com/api-reference/incidentactionitems/list-all-action-items-for-an-organization)

### Supported API Fields (Create/Update)

* `kind` (`task` or `follow_up`)
* `summary` (required)
* `description` (Markdown supported)
* `assigned_to_user_id`
* `assigned_to_group_ids`
* `priority` (`high`, `medium`, `low`)
* `status` (`open`, `in_progress`, `done`, `cancelled`)
* `due_date` (ISO 8601)
* **Jira fields:**
  * `jira_issue_id`
  * `jira_issue_key`
  * `jira_issue_url`

### Response Fields Include

* Kind, priority, status
* Due date
* Assigned user & groups
* Integration URLs:
  * `jira_issue_url`
  * `github_issue_url`
  * `gitlab_issue_url`
  * `linear_issue_url`
* `url` and `short_url`
* Timestamps and metadata

<Info>
  The API follows the JSON:API spec and enforces the same validations as the Web UI and Slack.
</Info>

***

### Best Practices

* **Automate common tasks** to reduce manual work
* **Use role-based tasks** for consistent incident startup actions
* **Assign owners early** to prevent drift
* **Use priorities intentionally** to structure follow-up workflows
* **Integrate external systems** (Jira, GitHub, etc.) for centralized tracking
* **Review overdue follow-ups regularly** for reliability improvements

***

### Troubleshooting

<AccordionGroup>
  <Accordion title="A workflow didn’t create an action item">
    Confirm the trigger conditions matched the incident and that the user/action had permission to create action items.
  </Accordion>

  <Accordion title="A role task did not appear during incident creation">
    Ensure the role is enabled and the role tasks themselves are active. Disabled tasks are not copied over.
  </Accordion>

  <Accordion title="The API returned a validation error">
    Make sure <code>summary</code> is present and enum fields (priority, status, kind) match allowed values. Check Jira fields if provided.
  </Accordion>

  <Accordion title="A follow-up could not be created">
    Some organizations disable task/follow-up creation after an incident is resolved, cancelled, or closed.
  </Accordion>

  <Accordion title="API-created items aren’t appearing in Slack">
    Slack notifications fire only when:
    <br />• The team has a Slack integration\
    <br />• The incident has a <code>slack\_summary\_timestamp</code>\
    <br />• Notifications aren’t suppressed

    <br />

    These notifications are not workflow-dependent.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).