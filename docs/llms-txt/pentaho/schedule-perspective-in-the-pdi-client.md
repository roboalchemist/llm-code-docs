# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/schedule-perspective-in-the-pdi-client.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/schedule-perspective-in-the-pdi-client.md

# Scheduler perspective in the PDI client

When you are finished [designing your PDI jobs and transformations](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client) and have saved them in the PDI Server, you can schedule them to run at specific times.

All your active scheduled jobs and transformations are listed in the schedules table in PDI, which you can get to by clicking the **Perspectives** icon (Item 1 below) and then selecting **Scheduler** in the menu.

The schedules table shows which jobs and transformations are scheduled to run, the recurrence pattern for the schedule, when it was last run, when it is set to run again, and the current state of the schedule.

**Note:** You can also create your own schedule using `cron` on Linux, the `Task Scheduler` on Windows, or the `at` command on Windows. If you do this, you will need to call the schedule using Pan or Kitchen commands.

![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-d15742b8d92df473ae1c549cb29d4b6ddc12428c%2FPDI%20scheduler%20perspective.png?alt=media)

You can use the icons in the PDI scheduler toolbar (Item 2, above) to edit and maintain each of your schedules, as described in the following table.

| Icon                                                                                                                                                                                                                         | Name                     | Function                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| ![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-edacc6afd0cc54500d8de6392aefc2679cd11732%2FRefresh.png?alt=media)                       | **Refresh**              | Refreshes the list of schedules.                                                                                    |
| ![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-02b1c7613e41093018c68f2a9a4ea8e1d28acd2b%2FStart%20Scheduled%20Task.png?alt=media)      | **Start Scheduled Task** | Starts scheduled transformations or jobs.                                                                           |
| ![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-6548ba471f06acf4319b9169184cfd372f715b61%2FStop%20Scheduled%20Task.png?alt=media)       | **Stop Scheduled Task**  | Stops a running schedule or schedules at will.                                                                      |
| ![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-f16c971dea795f15dd710d6354d819b1e05104e7%2FStart%20Scheduler.png?alt=media)             | **Start Scheduler**      | Resumes a previously stopped schedule.                                                                              |
| ![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-6fdf6f7b4b13c00b88d52b93763fc87aa1f717a7%2FPause%20Scheduler.png?alt=media)             | **Stop Scheduler**       | Stops a specified schedule. Use **Start Scheduler** to resume a paused schedule.                                    |
| ![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-a35fdd633d4a6fe74f155b1402d5a734ef1d9c29%2FPDI%20Edit%20Scheduled%20Task.png?alt=media) | **Edit Scheduled Task**  | Edits the details of an existing schedule.                                                                          |
| ![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-45e2ce84488aa9127aca96466a464463d847414c%2FRemove.png?alt=media)                        | **Remove**               | Deletes a specified schedule. If the schedule is currently running, it continues to run, but it will not run again. |

You can use the schedules table (Item 2, above) for information about a scheduled item. The columns in the table are described below. You can click the column name to sort content alphabetically in ascending or descending order.

| Column                                                                                     | Description                                                                           |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| **Schedule Name**                                                                          | Lists your schedules by the name you assign to them.                                  |
| **Repeats\***                                                                              | Describes how often the schedule is set to run.                                       |
| **Type**                                                                                   | Displays the file type associated with the schedule.                                  |
| **Source File**                                                                            | Displays the name of the file associated with the schedule.                           |
| **Parameters and Variables**                                                               | Displays the parameter name(s) and variable(s) assigned in the transformation or job. |
| **Last Run (duration)\***                                                                  | Shows the last time, date, and duration when the schedule was run.                    |
| **Next Run\***                                                                             | Shows the next time and date when the schedule will run again.                        |
| **Owner**                                                                                  | Displays the owner of the file associated with the schedule.                          |
| **Status**                                                                                 | Indicates the current state of the schedule, which can be NORMAL or PAUSED.           |
| \* The time and time zone are specified by the user when creating or editing the schedule. |                                                                                       |
