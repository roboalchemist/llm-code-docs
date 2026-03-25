# Source: https://docs.axonius.com/docs/terminating-a-workflow-run.md

# Terminating a Workflow Run

Workflow runs with a status of either *Running* or *Pending* can be terminated.

A Workflow can include multiple Enforcement Actions. When a Workflow containing more than one Enforcement Action is terminated, the following outcomes are possible  for each Action within that Workflow:

* Completed - The Action finished running before termination. All changes made by this Action are permanent and irreversible.
* Running (interrupted) - The Action was in progress at the time of termination and was immediately stopped. Any changes made before termination are retained and irreversible.
* Not started - The Action has not started to run. No changes are made to any assets and the Action does not run.

**To terminate a Workflow run**

1. In the [Workflows page](/docs/using-the-workflows-page#opening-the-workflows-page), click **Run History**.
2. On the **Run History** page, select the specific Workflow run that you want to terminate.
3. From the **Actions** menu, select **Terminate Task**. This option is enabled only if at least one of the selected Workflows has a status of *In progress* or *Pending*.