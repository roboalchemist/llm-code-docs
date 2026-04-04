# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/complete_task_graphs.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/complete_task_graphs.md

# Source: https://docs.snowflake.com/en/sql-reference/functions/complete_task_graphs.md

Categories:
:   [Information Schema](../info-schema.md) , [Table functions](../functions-table.md)

# COMPLETE_TASK_GRAPHS

Returns the status of a completed *graph* run. The function returns details for runs that executed
successfully, failed, or were cancelled in the past 60 minutes. A graph is currently defined as a single scheduled task or a
[task graph](../../user-guide/tasks-graphs.md) composed of a scheduled root task and one or more dependent tasks (i.e. tasks that have one or more defined predecessor tasks). For the
purposes of this function, *root task* refers to either the single scheduled task or the root task in a [task graph](../../user-guide/tasks-graphs.md).

To retrieve the details for graph runs that are currently executing, or are next scheduled to run within the next 8 days, query the
[CURRENT_TASK_GRAPHS](current_task_graphs.md) table function.

The function returns the graph run details for your entire Snowflake account or a specified root task.

## Syntax

```sqlsyntax
COMPLETE_TASK_GRAPHS(
      [ RESULT_LIMIT => <integer> ]
      [, ROOT_TASK_NAME => '<string>' ]
      [, ERROR_ONLY => { TRUE | FALSE } ] )
```

## Arguments

All the arguments are optional.

`RESULT_LIMIT => integer`
:   A number specifying the maximum number of rows returned by the function. Note that the results are returned in descending COMPLETED_TIME
    order. If the number of matching rows is greater than the result limit, the graph executions with the most recent completed timestamp are
    returned, up to the specified limit.

    Range: `1` to `10000`

    Default: `1000`

`ROOT_TASK_NAME => string`
:   A case-insensitive string specifying the name of the root task. Only non-qualified task names are supported. Only graph runs for the
    specified task are returned. Note that if multiple tasks have the same name, the function returns the graph runs for each of these tasks.

`ERROR_ONLY => TRUE | FALSE`
:   When set to TRUE, this function returns only graph runs that failed or were cancelled.

## Usage notes

* To view a task graph within this function, the invoking role requires at least one of the following privileges:

  * OWNERSHIP privilege on the task (that is, the task owner).
  * MONITOR or OPERATE privileges on the task.
  * The global MONITOR EXECUTION privilege.
  * The ACCOUNTADMIN role.

  The role must also have the USAGE privilege on the database and schema that store the task, otherwise the DATABASE_NAME and SCHEMA_NAME values in the output are NULL.
* This function returns a maximum of 10,000 rows, set in the `RESULT_LIMIT` argument value. The default value is `1000`. To avoid
  this limitation, use the [COMPLETE_TASK_GRAPHS view](../account-usage/complete_task_graphs.md) (Account Usage).
* When the COMPLETE_TASK_GRAPHS function is queried, its task name and result limit arguments are applied first
  followed by the WHERE and LIMIT clause, respectively, if specified. In addition, the function returns records in descending
  COMPLETED_TIME order.

  In practice, if many task graphs completed running in your account in the previous hour, the results returned by the function might not
  include an expected record, especially if the RESULT_LIMIT value is relatively low.
* When calling an Information Schema table function, the session must have an INFORMATION_SCHEMA schema in use or the function
  name must be fully-qualified. For more details, see [Snowflake Information Schema](../info-schema.md).

## Output

The function returns the following columns:

| Column Name | Data Type | Description |
| --- | --- | --- |
| ROOT_TASK_NAME | TEXT | Name of the root task. |
| DATABASE_NAME | TEXT | Name of the database that contains the graph. |
| SCHEMA_NAME | TEXT | Name of the schema that contains the graph. |
| STATE | TEXT | State of the graph run:   *`SUCCEEDED`: All tasks in the graph ran successfully to completion, or the root task run succeeded and one or more child task runs were skipped.* `FAILED`: One or more task runs in the graph failed, or the root task run succeeded and one or more child task runs failed. * `CANCELLED`: One or more task runs in the graph were cancelled, or the root task run succeeded and one or more child task runs were cancelled.   Note that if the state of the root task run is SKIPPED, the function does not return a row for the run. |
| SCHEDULED_FROM | TEXT | One of:  *`SCHEDULE`: The task was scheduled to run normally, as described in SCHEDULE or AFTER clauses of [CREATE TASK](../sql/create-task.md).* `EXECUTE_TASK`: The task was scheduled to run with [EXECUTE TASK](../sql/execute-task.md). *`MANUAL RETRY`: The task was scheduled to run with [EXECUTE TASK … RETRY LAST](../sql/execute-task.md).* `AUTOMATIC RETRY`: The task was configured to retry on failure and the previous execution failed. For more information, see [Automatically retry failed task runs](../../user-guide/tasks-intro.md). * `TRIGGER` : The task was run because the stream, in the `WHEN` clause of the task, contained new data.  For runs of child tasks in a task graph, the column returns the same value as the root task run. |
| FIRST_ERROR_TASK_NAME | TEXT | Name of the first task in the graph that returned an error; returns NULL if no task produced an error. |
| FIRST_ERROR_CODE | NUMBER | Error code of the error returned by the task named in FIRST_ERROR_TASK_NAME; returns NULL if no task produced an error. |
| FIRST_ERROR_MESSAGE | TEXT | Error message of the error returned by the task named in FIRST_ERROR_TASK_NAME; returns NULL if no task produced an error. |
| SCHEDULED_TIME | TIMESTAMP_LTZ | Time when the root task was scheduled to start. Tasks start with a brief queueing period before they begin to run. For more information, see [Task graph duration](../../user-guide/tasks-graphs.md). |
| QUERY_START_TIME | TIMESTAMP_LTZ | Time when the query in the root task definition started to run. This timestamp aligns with the start time for the query returned by QUERY_HISTORY. |
| NEXT_SCHEDULED_TIME | TIMESTAMP_LTZ | Time when the standalone or root task (in a [task graph](../../user-guide/tasks-graphs.md)) is next scheduled to start running, assuming the current run of the standalone task or [task graph](../../user-guide/tasks-graphs.md) started at the SCHEDULED_TIME time completes in time. |
| COMPLETED_TIME | TIMESTAMP_LTZ | Time when the last task in the [task graph](../../user-guide/tasks-graphs.md) completed. |
| ROOT_TASK_ID | TEXT | Unique identifier for the root task in a [task graph](../../user-guide/tasks-graphs.md). This ID matches the ID column value in the SHOW TASKS output for the same task. |
| GRAPH_VERSION | NUMBER | Integer identifying the version of the [task graph](../../user-guide/tasks-graphs.md) that was run, or is scheduled to be run. |
| RUN_ID | NUMBER | Time when the standalone or root task in a [task graph](../../user-guide/tasks-graphs.md) is/was originally scheduled to start running. Format is epoch time (in milliseconds). . . *Original* scheduled time refers to rare instances when the system might reschedule the same task to run at a different time to retry it or rebalance the load. If that happens, RUN_ID shows the original scheduled run time and SCHEDULED_TIME shows the rescheduled run time. . . Note that RUN_ID may not be a unique identifier for the current task/graph run before retry. You can use GRAPH_RUN_GROUP_ID column as a replacement for RUN_ID. |
| ATTEMPT_NUMBER | NUMBER | Integer representing the number of attempts to run this task. Initially one. |
| CONFIG | TEXT | Displays the graph level configuration used during the graph run if explicitly set. Otherwise displays NULL. |
| GRAPH_RUN_GROUP_ID | TEXT | Identifier for the graph run. When a graph run has multiple task runs, each task run will show the same GRAPH_RUN_GROUP_ID. The combination of GRAPH_RUN_GROUP_ID, and ATTEMPT_NUMBER can be used to uniquely identify a graph run. |
| BACKFILL_INFO | OBJECT | Reserved for future use. The returned value for all rows is NULL. |

## Examples

Retrieve the 1000 most recent completed graph executions in the account. Note that the maximum number of rows returned by the function is
limited to 1000 by default. To change the number of rows returned, modify the RESULT_LIMIT argument value:

> ```sqlexample
> select *
>   from table(information_schema.complete_task_graphs())
>   order by scheduled_time;
> ```

Retrieve the 10 most recent completed graph runs for a specified task graph within the last hour:

> ```sqlexample
> select *
>   from table(information_schema.complete_task_graphs (
>     result_limit => 10,
>     root_task_name=>'MYTASK'));
> ```
