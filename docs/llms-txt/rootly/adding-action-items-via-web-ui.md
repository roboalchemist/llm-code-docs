# Source: https://docs.rootly.com/incidents/action-items/adding-action-items-via-web-ui.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating Action Items in Web Interface

> Add tasks and follow-ups to incidents through the web interface, with options for exporting to external tools and manual tracking.

### How Web-Based Action Items Work

From the incident page in the Rootly web app, you can create and manage **tasks** (work done during the incident) and **follow-ups** (work done after the incident to prevent recurrence).

Tasks and follow-ups live in dedicated tabs on the incident and are also reflected in retrospectives, exports, and integrations with external tools.

<Info>
  Use the web interface when you want a complete view of all action items for an incident, need richer editing controls, or want to export items to ticketing/project management tools.
</Info>

<img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/incidents/incident-tasks-followups-tabs.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=a18203bfaee0a8ba2c752042a2298ad4" alt="Under the incident title there are tabs for Tasks and Follow-ups" title="Screenshot of an incident title" style={{ width:"48%" }} width="409" height="265" data-path="images/incidents/incident-tasks-followups-tabs.webp" />

***

### Creating Tasks and Follow-Ups from an Incident

Add a task or follow-up directly from the incident page.

<Steps>
  <Step title="Open the incident">
    Open the incident in the Rootly web app from your incidents list or a direct link.
  </Step>

  <Step title="Choose Tasks or Follow-ups">
    Under the incident title, click either the <strong>Tasks</strong> tab (for work done during the incident) or the <strong>Follow-ups</strong> tab (for post-incident work).
  </Step>

  <Step title="Create a new item">
    Click <strong>+ New Task</strong> or <strong>+ New Followup</strong>.

    A form will appear where you can enter details such as:

    * <strong>Title</strong> (required)
    * Description
    * Assignee (person and/or team)
    * Priority
    * Status
    * Due date (especially for follow-ups)
    * Optional links to external systems (e.g., Jira issue URL)
  </Step>

  <Step title="Save the action item">
    Click <strong>Save</strong> to create the item.

    The task or follow-up will appear in the list on the tab and be associated with the incident timeline for future reference and retrospectives.
  </Step>
</Steps>

<Info>
  Depending on your workspace configuration, you may see slightly different fields (for example, required teams, custom fields, or external ticket links). Your admin controls these under <strong>Configuration</strong>.
</Info>

***

### Using Markdown in Action Item Descriptions

Action item descriptions support [Markdown](https://www.markdownguide.org/ "Markdown") so you can structure notes and instructions clearly.

You can use Markdown to:

* Add **bold** or *italic* emphasis
* Create bullet lists or numbered steps
* Insert links to dashboards, runbooks, or logs
* Highlight command snippets

<Info>
  Markdown makes it easier for assignees to understand exactly what needs to be done—especially for complex or multi-step work.
</Info>

***

### Exporting Action Items Automatically (Smart Defaults)

With **Smart Defaults**, you can configure Rootly to automatically export tasks to external tools for tracking—so responders don’t need to create tickets manually.

These settings live under integration pages such as Jira, Asana, Motion, or Linear.

Examples:

* Automatically create a Jira issue whenever a new follow-up is created
* Push all high-priority follow-ups to Linear as issues
* Create Asana tasks for follow-ups tied to specific services

<img src="https://mintcdn.com/rootly/EZBU89ISF00990Wy/images/integrations/jiraactionitesm.webp?fit=max&auto=format&n=EZBU89ISF00990Wy&q=85&s=dc70f475b35e2b3ded38b1ec9967af90" alt="The settings for the Jira integration for automating tasks based on action items." width="971" height="387" data-path="images/integrations/jiraactionitesm.webp" />

<Info>
  Use Smart Defaults when you want **every** action item (or a filtered subset) to end up in your external tracker without manual effort.
</Info>

***

### Exporting Action Items Manually from an Incident

If you prefer more control, you can export action items manually from the **Tasks** and **Follow-ups** tabs.

1. Open the incident in the web app.
2. Go to the **Tasks** or **Follow-ups** tab.
3. Click the **Export to ticketing** button to send selected items to your configured tool (Jira, Linear, Asana, Trello, Zendesk, etc.).

<img src="https://mintcdn.com/rootly/n-fKYpx5M7fU1qc2/images/misc/exporttoticketing.webp?fit=max&auto=format&n=n-fKYpx5M7fU1qc2&q=85&s=a7963c83f2453d87a6e4fa2e65f6e390" alt="This button can be found under the tasks tab in an incident" title="Export to ticketing button" style={{ width:"60%" }} width="400" height="186" data-path="images/misc/exporttoticketing.webp" />

During export, you may need to select:

* Which integration to use
* Project, board, team, or workspace
* Issue type or workflow state
* Whether to create a **subtask/sub-issue** when an incident already has a linked parent ticket

<Info>
  Manual export is perfect when only some action items should be tracked externally.
</Info>

***

### Best Practices

* **Create tasks early** — capture investigation steps while context is fresh.
* **Use follow-ups for long-term improvements** — reliability work, runbook updates, etc.
* **Assign owners immediately** — unassigned items go stale.
* **Set due dates** — especially for follow-ups tied to retrospectives.
* **Use Markdown for clarity** — links and structured notes help assignees move faster.
* **Export to ticketing systems when appropriate** — keep work aligned with your team’s backlog.
* **Review open follow-ups regularly** — ensures continuous improvement.

***

### Troubleshooting

<AccordionGroup>
  <Accordion title="I don’t see the Tasks or Follow-ups tabs">
    Your workspace or role may have restricted access, or you may not have permission to manage action items for this incident.
    Check with your Rootly admin.
  </Accordion>

  <Accordion title="I can’t create a new task or follow-up">
    Some organizations disable new action items after certain incident lifecycle stages (e.g., after resolution or close).
    If the creation buttons are missing, your configuration may enforce these rules.
  </Accordion>

  <Accordion title="The Export button is missing">
    Exporting requires at least one ticketing integration (Jira, Linear, Asana, etc.) to be configured.
    Check <strong>Configuration → Integrations</strong>.
  </Accordion>

  <Accordion title="Export succeeded in Rootly but I don’t see the ticket">
    The external tool may have missing required fields or permission restrictions.
    Verify:

    * Project/workspace is valid
    * Issue type and fields are allowed
    * The integration user has permission to create tickets
  </Accordion>

  <Accordion title="Some fields look different from screenshots">
    Your admin may have enabled custom fields, required teams, or experimental improvements.
    These settings change which form fields appear.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).