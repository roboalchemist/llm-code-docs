# Source: https://docs.wandb.ai/models/runs/manage-runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Move a run to a different project or team

> Move runs between projects or teams using the W&B App.

<Note>
  Before you begin, ensure you have the necessary permissions to move runs between projects or teams. You must have access to the run at its current and new locations.
</Note>

To move runs from one project to another or between teams:

1. Navigate to the project that contains the runs you want to move.
2. Select the **Runs** tab from the project sidebar.
3. Select the checkbox next to the runs you want to move.
4. Click the **Move to project** button above the table.
5. Select the destination team and project from the dropdown.

<Note>
  When you move a run, historical artifacts associated with it are not moved. To move an artifact manually, you can use the [`wandb artifact get`](/models/ref/cli/wandb-artifact/wandb-artifact-get/) SDK command or the [`Api.artifact` API](/models/ref/python/public-api/api/#artifact) to download the artifact, then use [`wandb artifact put`](/models/ref/cli/wandb-artifact/wandb-artifact-put/) or the `Api.artifact` API to upload it to the run's new location.
</Note>

{/* #### Manage runs in bulk
  This section shows how to manage multiple runs at once, across one or more run groups.

  1. If necessary, [toggle grouping by columns](#toggle-grouping-by-column-in-the-ui), grouping by the **Group** column.
  1. Expand a group to view its runs. In a single bulk operation, you can move runs from different groups to the same target group. Expand all relevant groups.
  1. To select all runs in a group, click the checkbox next to the group name.
  1. To select individual runs, click their checkboxes.
  1. To select all runs in all groups, click the checkbox next to the **Name** column heading.
  1. Above the table, choose a bulk operation: **Tag**, **Move to group**, **Move to project**, or **New sweep**. */}
