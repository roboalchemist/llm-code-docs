# Source: https://docs.axonius.com/docs/deleting-workflows.md

# Deleting and Deactivating/Activating Workflows

You can remove entire Workflows from the system or temporarily deactivate and reactivate them as needed.

<Callout icon="📘" theme="info">
  Note

  You can also delete individual components (Event, Event Condition, Action, or Action Condition) from a Workflow. Refer to the relevant section in [Viewing and Editing Workflows](/docs/viewing-and-editing-workflows).
</Callout>

## Deleting Workflows

Deleting a Workflow permanently removes it from the system. Once deleted, a Workflow cannot be recovered.
Delete Workflows using one of the following methods:

* From the Workflows page (multiple deletion): Select and delete one or more Workflows directly from the table on the main **Workflows** page. Learn how to [delete one or more Workflows directly from the All Workflows table](/docs/using-the-workflows-page#deleting-workflows-from-the-system).

* From the Workflow configuration page (single deletion):
  **To delete a Workflow from its configuration page**
  1. [Open the Workflow](/docs/viewing-and-editing-workflows#opening-a-workflow) you want to delete.
  2. In the Workflow configuration pane that opens, at the top, click **Delete Workflow**.
  3. In the confirmation prompt, click **Delete** to permanently remove the Workflow. This action cannot be undone.

## Activating and Deactivating a Workflow

A workflow must be activated to run. Deactivating a Workflow prevents it from running, while preserving its configuration for future use. You can deactivate or activate Workflows using two methods:

**To activate or deactivate a workflow from the Workflows page (multiple activation/deactivation):**

* Select one or more workflows directly from the table on the main Workflows page and then selected Activate or Deactivate. Learn how to [deactivate/activate one or more Workflows directly from the All Workflows table](/docs/using-the-workflows-page#changing-the-workflow-status).

**To activate a Workflow from its configuration page:**

1. [Open the desired Workflow](/docs/viewing-and-editing-workflows#opening-a-workflow).

2. Above the configuration pane, enable **Active** to activate the workflow.

   <Image align="center" alt="WorkflowActivateToggle" width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/workflows/WorkflowActivateToggle.png" />

3. Click Save. If all required fields are filled in, you can also click Run to active, save and run the workflow.

**To deactivate a Workflow**

1. Toggle off **Activate**. The workflow will not run.