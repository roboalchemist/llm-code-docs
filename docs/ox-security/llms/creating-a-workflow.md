# Source: https://docs.ox.security/automate-with-ox-workflows/creating-a-workflow.md

# Regular Workflows

Before configuring an automatic workflow in OX, make sure the system reflects your actual environment. Workflows only make sense once your visibility, application mapping, and prioritization are aligned with the way your teams work.

When everything is set and you trust what the system shows, you’re ready to start building workflows.

### Workflow Best Practices

These practices help you design effective workflows once your environment is ready.

| Tip                                                                                | Benefit                                                                 |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Start simple: create one or two basic workflows before scaling up.                 | Build confidence and validate behavior without overwhelming the system. |
| Use demo organizations to test workflow behavior before production.                | Validate logic safely without triggering unwanted alerts or tickets.    |
| Test webhook endpoints when using webhooks instead of native ticketing connectors. | Confirm external systems handle inputs correctly before scaling up.     |
| Combine multiple conditions (e.g., CVE type, new developer, time window).          | Automate business-specific scenarios with precision.                    |
| Distinguish between production and sandbox/test repos in workflow conditions.      | Ensure alerts and tickets reflect real risk, not noise from test code.  |
| Chain multiple actions (e.g., Slack + Jira + Email).                               | Improve visibility and guarantee follow-up across teams.                |

## Creating a workflow

**To set up a workflow:**

1. Go to **Workflows** in the OX platform.
2. Click **Create New Workflow**.
3. Add a **name** and **description**.
4. Select the [**trigger**](https://docs.ox.security/automate-with-ox-workflows/creating-a-workflow/workflow-triggers).
5. Add optional [**conditions**](https://docs.ox.security/automate-with-ox-workflows/creating-a-workflow/workflow-conditions)(e.g., application, severity, business priority).
6. Define the [**action**](https://docs.ox.security/automate-with-ox-workflows/creating-a-workflow/workflow-actions)(e.g., send Slack notification, create Jira ticket).

You can preview how many issues match your configuration on the right.

### Workflow Builder Tips

The workflow builder UI supports flexible configuration, but some options are easy to miss. Keep these points in mind while creating workflows.

| Tip                                                                        | Benefit                                                               |
| -------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Use hover text to understand how each filter works.                        | Avoid misconfigurations by seeing exact definitions of filter logic.  |
| Review advanced operators like NOT IN, CONTAINS, or HIGHER THAN carefully. | Ensure complex filters behave as expected without unintended results. |
| Group workflows logically by purpose (e.g., ticketing, notifications).     |                                                                       |
