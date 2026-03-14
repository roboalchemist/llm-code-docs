# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/task_versions.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/task_versions.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# TASK_VERSIONS view

This Account Usage view enables you to retrieve the history of [task versions](../../user-guide/tasks-intro.md). The returned rows
indicate the tasks that comprised a [task graph](../../user-guide/tasks-graphs.md) and their properties at a given time.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| ROOT_TASK_ID | TEXT | Unique identifier for the root task in a DAG. This ID matches the ID column value in the SHOW TASKS output for the same task. Matches ROOT_TASK_ID in [COMPLETE_TASK_GRAPHS view](complete_task_graphs.md) and [TASK_HISTORY view](task_history.md). |
| GRAPH_VERSION | NUMBER | Integer identifying the version of the task. Matches GRAPH_VERSION in [COMPLETE_TASK_GRAPHS view](complete_task_graphs.md). |
| GRAPH_VERSION_CREATED_ON | TIMESTAMP_LTZ | Date and time when this version of the task graph was saved. |
| NAME | TEXT | Name of the task. |
| ID | TEXT | Unique identifier for each task. Note that recreating a task (using CREATE OR REPLACE TASK) essentially creates a new task, which has a new ID. |
| DATABASE_ID | NUMBER | Internal/system-generated identifier for the database that contained the task. |
| DATABASE_NAME | TEXT | Name of the database in which the task is stored. |
| SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema that contained the task. |
| SCHEMA_NAME | TEXT | Name of the schema in which the task is stored. |
| OWNER | TEXT | Role that owns the task (that is, has the OWNERSHIP privilege on the task). |
| COMMENT | TEXT | Comment for the task. |
| WAREHOUSE_NAME | TEXT | Warehouse that provides the required resources to run the task. |
| SCHEDULE | TEXT | Schedule for running the task. Displays NULL if no schedule is specified. |
| PREDECESSORS | ARRAY | JSON array of any tasks identified in the AFTER parameter for the task (that is, predecessor tasks). When run successfully to completion, these tasks trigger the current task. Individual task names in the array are fully qualified (that is, include the container database and schema names). Displays an empty array if the task has no predecessor. |
| STATE | TEXT | Current state of the task: `started` or `suspended`. `NULL` for root tasks (tasks with no predecessors). |
| DEFINITION | TEXT | SQL statements executed when the task runs. |
| CONDITION_TEXT | TEXT | Condition specified in the WHEN clause for the task. |
| ALLOW_OVERLAPPING_EXECUTION | BOOLEAN | For root tasks in a DAG, displays TRUE if overlapping execution of the DAG is explicitly allowed. For child tasks in a DAG, displays NULL. |
| ERROR_INTEGRATION | TEXT | Name of the notification integration used to access Amazon Simple Notification Service (SNS), Google Pub/Sub, or Microsoft Azure Event Grid to relay error notifications for the task. |
| LAST_COMMITTED_ON | TIMESTAMP_LTZ | Timestamp when a version of the task was last set. If no version has been set (that is, if the task has not been resumed or manually executed after it was created), the value is NULL. |
| LAST_SUSPENDED_ON | TIMESTAMP_LTZ | Timestamp when the task was last suspended. If the task has not been suspended yet, the value is NULL. |
| TARGET_COMPLETION_INTERVAL | TEXT | The window of time when the task should perform. Only used for serverless tasks. Optional for serverless tasks, required for [serverless triggered tasks](../../user-guide/tasks-intro.md). |
| SCHEDULING_MODE | TEXT | Reserved for future functionality. Displays UNKNOWN. |

## Usage notes

Latency for the view may be up to 3 hours.

## Examples

Retrieve the tasks from a specific task graph based on the ROOT_TASK_ID and GRAPH_VERSION:

> ```sqlexample
> SELECT *
> FROM snowflake.account_usage.task_versions
> WHERE ROOT_TASK_ID = 'afb36ccc-. . .-b746f3bf555d' AND GRAPH_VERSION = 3;
> ```

Retrieve the task runs for a particular task graph and its descendant tasks from task_history, with additional task information from task_versions.

> ```sqlexample
> SELECT
> task_history.* rename state AS task_run_state,
> task_versions.state AS task_state,
> task_versions.graph_version_created_on,
> task_versions.warehouse_name,
> task_versions.comment,
> task_versions.schedule,
> task_versions.predecessors,
> task_versions.allow_overlapping_execution,
> task_versions.error_integration
> FROM snowflake.account_usage.task_history
> JOIN snowflake.account_usage.task_versions using (root_task_id, graph_version)
> WHERE task_history.ROOT_TASK_ID = 'afb36ccc-. . .-b746f3bf555d'
> ```
