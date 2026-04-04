# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-task.md

# DROP TASK

Removes a task from the current/specified schema.

See also:
:   [CREATE TASK](create-task.md) , [ALTER TASK](alter-task.md) , [SHOW TASKS](show-tasks.md) , [DESCRIBE TASK](desc-task.md)

## Syntax

```sqlsyntax
DROP TASK [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the task to drop. If the identifier contains spaces, special characters, or mixed-case characters, the
    entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive
    (e.g. `"My Object"`).

    If the task identifier is not fully-qualified (in the form of `db_name.schema_name.task_name` or
    `schema_name.task_name`), the command looks for the task in the current schema for the session.

## Usage notes

* When a task is dropped, any current run of the task (i.e. a run with an EXECUTING state in the
  [TASK_HISTORY](../functions/task_history.md) output) is completed. To abort the run of the specified task, execute the
  [SYSTEM$USER_TASK_CANCEL_ONGOING_EXECUTIONS](../functions/system_user_task_cancel_ongoing_executions.md) function.
* The root task in a [task graph](../../user-guide/tasks-graphs.md) must be suspended before any task in the task graph is dropped.
* A standalone task can be dropped by the task owner (i.e. the role that has the OWNERSHIP privilege on the task) or a higher role
  without first suspending the task.
* If a predecessor task in a task graph is dropped, then all former child tasks that identified this task as the predecessor become either
  standalone tasks or root tasks, depending on whether other tasks identify these former child tasks as their predecessor. These former
  child tasks are suspended by default and must be resumed manually.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

Drop a task:

> ```sqlexample
> SHOW TASKS LIKE 't2%';
>
>
> DROP TASK t2;
>
>
> SHOW TASKS LIKE 't2%';
> ```

Drop the task again, but don’t raise an error if the task does not exist:

> ```sqlexample
> DROP TASK IF EXISTS t2;
> ```
