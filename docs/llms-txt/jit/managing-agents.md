# Source: https://docs.jit.io/docs/managing-agents.md

# Managing Agents

Once an agent has been created, it can be viewed, monitored, edited, or deleted from the **My Agents** page. This page provides a centralized location for managing all automated workflows in your workspace.

***

## 3.1 My Agents Page

The **My Agents** page displays every agent in your organization, including custom agents, templates, and Super Agents. Each agent appears as a card showing:

* **Agent name and description**
* **Last run time**
* **Run result** (Completed, Failed, etc.)
* **Schedule** (Daily, Weekly, Manual Only)
* **Notification setting** (Always / Never)
* **Enable / Disable toggle**
* **Configuration button**
* **Delete option**

You can sort, scan, and review the operational status of all automations from this view.

***

### Viewing Agent Results

When an agent runs, its results appear in the agent card and can be opened for full detail.\
Agent output uses the same widget system as Agentic Chat, including:

* Tables
* Dashboards
* Breakdown cards
* Metric summaries

For more information on how to interpret these widgets, see **Section 4.3 — AI Widgets**.

***

### Enabling or Disabling an Agent

Each agent includes a toggle that controls whether it runs according to its schedule:

* **Enabled** — The agent will run automatically based on the defined schedule.
* **Disabled** — The agent will not run unless triggered manually.

Disabling an agent does not delete it; it simply pauses automation.

***

### Deleting an Agent

To remove an agent permanently:

1. Open **My Agents**
2. Select the trash icon on the agent card
3. Confirm deletion

This action cannot be undone.\
Deleting an agent removes its configuration and stops all future runs.

***

## 3.2 Editing Agents

You can edit an existing agent by selecting **Configure** on its card.\
This opens the **same configuration modal** used when creating an agent.

For details on configuration options—including task, schedule, notifications, Slack channel, and advanced instructions—see **Section 2.2 — Agent Configuration**.

**Tasks that use Tools:**\
If the agent’s task includes tool usage (e.g., Jira ticket creation, AWS resource queries, Slack messages), the behavior of those tools will run every time the agent executes.\
Tools cannot be configured separately — they are defined inside the task itself.

For details on available tools and examples of tool-enabled agents, see **[Tools](https://docs.jit.io/docs/agentic-tools)**.

After editing settings, click **Save** to apply changes.\
To run the agent immediately after editing, select **Save & Run** (if available).

***

### Rerunning an Agent Manually

From the agent’s configuration modal (or in some cases from the card dropdown), you may have the option to manually rerun an agent. This is useful for:

* Validating configuration updates
* Generating an on-demand report
* Triggering analysis outside of the scheduled cadence

The output will again appear using standard widgets.\
For help interpreting results, refer to **Section 4.3 — AI Widgets**.

***

## 3.3 Troubleshooting Failed Runs

If an agent shows a **Failed** status, consider checking the following:

* **Slack integration** — Required for notifications
* **Slack channel validity** — Must include the `#` prefix
* **Task instructions** — Invalid or overly complex instructions may cause failures
* **Access permissions** — Missing integrations or expired credentials
* **Advanced instructions** — Overly strict or conflicting settings may affect output
* **Schedule timing** — Conflicts with workspace throttling or limits

If the issue persists after review, temporarily run the agent manually to verify whether the failure is reproducible.

***

## Summary

The **My Agents** page is the operational center for automated workflows. From here, you can:

* Monitor agent performance
* Review results
* Modify configuration
* Adjust schedules and notifications
* Enable or disable automation
* Delete agents when no longer needed

Agent management ensures your automations remain accurate, timely, and aligned with your security workflows.