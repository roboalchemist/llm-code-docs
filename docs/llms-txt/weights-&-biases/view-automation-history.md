# Source: https://docs.wandb.ai/models/automations/view-automation-history.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# View an automation's history

> View the execution history of your W&B Automations to check status, triggering events, and action results.

<Note>
  This feature requires an Enterprise license. It is available only for:

  * W\&B Multi-tenant Cloud
  * W\&B Dedicated Cloud
  * W\&B Self-Managed v0.75.0+
</Note>

This page describes how to view and understand the execution history of your W\&B [automations](/models/automations), including what triggered an automation, what actions were taken, and whether they succeeded or failed.

Each executed automation generates a record that includes:

* **Execution timestamp**: When the automation was triggered.
* **Triggering event**: The specific event triggered the automation.
* **Status**: The execution's status. See [Execution status](#execution-status).
* **Action details**: Information about what action was performed, such as notifying a Slack channel or running a webhook.
* **Result details**: Additional information, if any, about the final outcome of executing the automation, including the error for a failed execution.

Based on your use case, select the **Registry** or **Project** tab for detailed instructions for viewing automation history.

<Tabs>
  <Tab title="Registry">
    1. Navigate to your registry by clicking on **Registry** in the project sidebar.
    2. Select your registry from the list.
    3. View the registry's automations in the **Automations** tab. Click the **Last execution** timestamp to view the execution history details. You can use the search bar to filter by automation name, and you can sort by the last triggered date to find recently executed automations.
    4. View the registry's automation executions in reverse chronological order in the **Automations history** tab, including the event, action, and status. Click an execution timestamp to view details about a particular execution.

    <Tip>If a collection has associated automation executions, the icon <img src="https://mintcdn.com/wb-21fd5541/37SaigLE2GKujbUi/images/automations/collection-automation-execution-icon.png?fit=max&auto=format&n=37SaigLE2GKujbUi&q=85&s=0c3fe797e039b4ed244668cf9d25b996" alt="Collection automation execution symbol, a circle with a right-pointing arrow" width="24" height="24" data-path="images/automations/collection-automation-execution-icon.png" /> displays, along with the number of associated executions.</Tip>
  </Tab>

  <Tab title="Project">
    1. Click the **Automations** tab in the project sidebar. The project's automations display. Click the **Last execution** timestamp to view the execution history details. You can use the search bar to filter by automation name, and you can sort by the last triggered date to find recently executed automations.
    2. In the **History** tab, view all executions of the project's automations in reverse chronological order, starting with the most recent execution. Each execution's metadata displays, including the event, action, and status. Click an execution timestamp to view details about a particular execution.
  </Tab>
</Tabs>

## Understanding execution details

Each automation execution has one of the following statuses:

* **Finished**: The automation completed all actions successfully.
* **Failed**: The automation encountered an error and terminated unsuccessfully.
* **Pending**: The automation is queued for execution.

Click on any execution in the history to view details:

* **Event details**: The specific event that triggered the automation, including:
  * Event type (e.g., "New artifact version", "Run completed")
  * Entity information (run ID, artifact name, etc.)
  * User who triggered the event (if applicable)

* **Action details**: Information about what the automation attempted to do:
  * Action type (Slack notification or webhook)
  * Target (Slack channel or webhook URL)
  * Payload sent (for webhooks)

* **Result information**:
  * Response status (for webhooks)
  * Any error messages or stack traces (for failed executions)

## Next steps

* [Create an automation](/models/automations/create-automations)
* Learn about [Automation events and scopes](/models/automations/automation-events)
* [Create a secret](/platform/secrets)
