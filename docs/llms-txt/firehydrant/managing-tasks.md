# Source: https://docs.firehydrant.com/docs/managing-tasks.md

# Managing Tasks

FireHydrant comes with incident task management so responders can track what they need to do during an incident.

**Tasks** are intended to be mid-incident action items while **[Follow-Ups](https://docs.firehydrant.com/docs/managing-follow-ups)** are items uncovered during the incident to be prioritized later.

In addition to creating and managing tasks, you can define **Task Lists** with preset tasks to help ensure consistency in your incident response and reduce cognitive load.

> 🚧 Note:
>
> Slack commands and emojis for Tasks will only work within the context of an incident channel.

## Create and Manage Tasks

Tasks can be created and assigned ad-hoc both via an incident's Command Center as well as in the incident channel in your respective chat application.

<Image alt="via Command Center Tasks tab" align="center" width="650px" src="https://files.readme.io/e7db57a-Screenshot_2023-12-01_at_12.39.18_PM.png">
  via Command Center Tasks tab
</Image>

<Image alt="via `/fh add task` in Slack" align="center" width="400px" src="https://files.readme.io/c4c36c9-slack-create-task.png">
  via `/fh add task` in Slack
</Image>

To view and manage outstanding Tasks, the same tab in the Command Center can be used, and in Slack, the command `/fh tasks [@user | all]` can be used.

### Due Dates and Reminders

When creating tasks, you have the option to set a due time. This can be set in terms of relative time (e.g., *15 minutes from now*) or in absolute time (e.g., due on August 23rd @ 3pm).

<Image alt="Setting a due date/time for a task when creating it" align="center" width="400px" src="https://files.readme.io/a9fee1d-CleanShot_2024-08-09_at_15.07.01.png">
  Setting a due date/time for a task when creating it
</Image>

When users are assigned tasks and with due dates/times, they will receive a Slack DM from the FireHydrant bot as well as an email at the following times:

* When assigned
* 30 minutes before due
* 10 minutes before due
* When due

<Image alt="Example Slack DM from FireHydrant about a due Task" align="center" width="650px" src="https://files.readme.io/24a38a6-CleanShot_2024-08-09_at_16.59.23.png">
  Example Slack DM from FireHydrant about a due Task
</Image>

You can also set a default Task SLA which will automatically set an initial due date/time for all tasks created in the Incident settings page.

<Image alt="Incident task SLA setting" align="center" width="650px" src="https://files.readme.io/0f4ce6655ac3b0e44d705d55087837051b7b8a368c7cd061cc216673fedbce9d-CleanShot_2025-02-10_at_14.39.392x.png">
  Incident task SLA setting
</Image>

### Using Emojis from Slack

<Image alt="Creating Tasks from emoji reaction to a message" align="center" width="400px" src="https://files.readme.io/9d50143-Screenshot_2023-12-01_at_12.51.29_PM.png">
  Creating Tasks from emoji reaction to a message
</Image>

From within the incident channel in Slack, you are able to react to specific messages with emojis to automatically create Tasks or Follow-Ups.

The default configured emoji is `:ballot_box_with_check:` but this can be modified in your **Settings** > **Integrations list** > **Slack settings**.

## Task Lists

<Image alt="Example predefined Task Lists" align="center" src="https://files.readme.io/37207e1-Screenshot_2023-12-01_at_12.54.33_PM.png">
  Example predefined Task Lists
</Image>

Task lists are predefined lists of multiple tasks that you can assign all at once in incidents.

Like with normal tasks, you can assign a Task List ad-hoc during an incident, but there's an additional capability to automate assignment via **Runbooks**.

### Creating a Task List

1. Navigate to **Settings** > **Incidents** > **Task Lists** in the Web UI.
2. Click “+ Add task list.”
3. On this screen, provide a **Name** and **Description** for the Task List.
   * Each Task list requires a unique name. Adding a description will also help provide context for the purpose of this task list. 
4. To add a task to your list, click “+ Add a task”.
   * Enter the task summary and description. Select **Save task** to add this task to the list. A task list must have at least one task before it can be saved.
5. When you are done, you can save the task list to view all the tasks.

Note that tasks can be re-ordered to your preferences.

### Assigning a Task List

Like with individual **Tasks**, you can add a Task List both via the Incident Command Center as well as in Slack.

<Image alt="Adding a Task List via Command Center" align="center" src="https://files.readme.io/e1b63b9-Screenshot_2023-12-01_at_12.57.05_PM.png">
  Adding a Task List via Command Center
</Image>

In Slack, the command is `/fh add task-list`.

<Image alt="Assigning a Task List via Slack" align="center" width="400px" src="https://files.readme.io/950a521-slack-add-task-list.png">
  Assigning a Task List via Slack
</Image>

### Automating via Runbooks

Task Lists have the additional capability of being automatically assigned as part of Runbook automation.

This allows immediately assigning a list of tasks based on various incident parameters. To read more about this, visit [Add Task List Runbook Step](https://docs.firehydrant.com/docs/runbook-step-add-task-list)

## Next Steps

* See how you can manage your incidents [completely from Slack](https://docs.firehydrant.com/docs/slack-responder-guide)
* Learn how to create [Follow-Ups](https://docs.firehydrant.com/docs/managing-follow-ups) to track items to be prioritized post-incident
* Read [Introduction to Runbooks](https://docs.firehydrant.com/docs/introduction-to-runbooks) and how they can be used to automate steps of your process