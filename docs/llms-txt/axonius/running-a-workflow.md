# Source: https://docs.axonius.com/docs/running-a-workflow.md

# Running Workflows

The way a Workflow is run depends on its configured trigger:

* **Event-triggered Workflows**: Workflows triggered by an **Event** run automatically when the selected triggering event occurs. For this to happen, the Workflow must be saved and activated by clicking **Save and Activate** in the Workflow configuration pane.

* **Manually-triggered Workflows**: Workflows configured with a **Manual** Action trigger can only be started manually. After configuring the Workflow,  click **Save and Run** to run it on demand.

* **Scheduled Workflows**: Workflows configured with a **Scheduled** Action trigger run automatically according to the defined schedule.

Important considerations:

* Workflows operate on a single asset at a time. If a triggering event identifies multiple assets (for example, ten assets), the Workflow runs separately for each asset (ten times in this example).
* You can monitor the results of all Workflow runs, or those of a specific Workflow, on the [**Run History** page](/docs/viewing-workflows-run-history).