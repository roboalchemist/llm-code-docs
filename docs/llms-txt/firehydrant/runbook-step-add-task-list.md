# Source: https://docs.firehydrant.com/docs/runbook-step-add-task-list.md

# Add Task List

<Image alt="Add Task List step" align="center" src="https://files.readme.io/9a6922c-image.png">
  Add Task List step
</Image>

The added capability for Task Lists is that you can automatically assign them based on various conditions in a Runbook.

This allows you to assign certain tasks flexibly and powerfully based on various situations. For example, "Assign **Security Response Tasks** if the Severity is **SEC0**," "Always assign **Commander Tasks** to the **Incident Commander**," etc.

## Prerequisite

Ensure you've [created or customized at least one Task List](https://docs.firehydrant.com/docs/managing-tasks).

## Adding the Runbook step

1. Go into a Runbook, click "Edit Runbook," then click '+ Add step.'
2. Search for "task list" and click **Add Task List**. Then select the Task List you'd like added to the incident.
3. **(Optional)** If you want to assign the Task List to a specific role, you can select that in the next dropdown.

### Assigning to a specific role

If assigning to a role, add a conditional execution rule that ensures the assigned role exists. Because Runbook steps execute concurrently, there may be a race condition if this step attempts to assign to a particular role before that role exists. See the image below.

<Image alt="Example conditions on the Add Task List step" align="center" src="https://files.readme.io/5405836-image.png">
  Example conditions on the Add Task List step
</Image>

In addition, if you want to have the timeline message about assigning a task list post into the incident channel, you should add another condition, "if Incident Slack Channel exists."