# Source: https://docs.snowflake.com/en/user-guide/tasks-monitor.md

# Monitor task runs

## Monitor task errors

You can configure Snowflake to push notifications when errors occur in task runs. You can also query the event table to
determine if tasks failed to run. For more information, see the following sections:

* [Set up error notifications for tasks](tasks-errors.md)
* [Monitor events for task executions](tasks-events.md)

## See task owners

To see who ran a task that is currently being run, see [SHOW TASKS](../sql-reference/sql/show-tasks.md) or [DESCRIBE TASK](../sql-reference/sql/desc-task.md).

* Check the OWNER column to see the role of the task owner.
* To see if the task has been run on behalf of the task owner, check the EXECUTE_AS_USER column. By default, this shows as NULL, but when the task is run using impersonated privileges, the user name of the user who modified the task is displayed.

To see who ran a task, use the [QUERY_HISTORY](../sql-reference/account-usage/query_history.md) view.

* If the task is not run as an actual user, the QUERY EXECUTED BY TASK column displays the user name as “SYSTEM”.
* If the task is running on behalf of another user, the QUERY EXECUTED BY TASK column displays the user name that the task is running on behalf of.
