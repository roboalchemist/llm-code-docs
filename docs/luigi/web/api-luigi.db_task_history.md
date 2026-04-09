# luigi.db_task_history

Provides a database backend to the central scheduler. This lets you see historical runs.
See Enabling Task History for information about how to turn out the task history feature.

Classes

`DbTaskHistory`()

Task History that writes to a database using sqlalchemy.

`TaskEvent`(**kwargs)

Table to track when a task is scheduled, starts, finishes, and fails.

`TaskParameter`(**kwargs)

Table to track luigi.Parameter()s of a Task.

`TaskRecord`(**kwargs)

Base table to track information about a luigi.Task.

class luigi.db_task_history.DbTaskHistory

Task History that writes to a database using sqlalchemy.
Also has methods for useful db queries.

CURRENT_SOURCE_VERSION = 1

task_scheduled(*task*)

task_finished(*task*, *successful*)

task_started(*task*, *worker_host*)

find_all_by_parameters(*task_name*, *session=None*, ***task_params*)

Find tasks with the given task_name and the same parameters as the kwargs.

find_all_by_name(*task_name*, *session=None*)

Find all tasks with the given task_name.

find_latest_runs(*session=None*)

Return tasks that have been updated in the past 24 hours.

find_all_runs(*session=None*)

Return all tasks that have been updated.

find_all_events(*session=None*)

Return all running/failed/done events.

find_task_by_id(*id*, *session=None*)

Find task with the given record ID.

find_task_by_task_id(*task_id*, *session=None*)

Find task with the given task ID.

class luigi.db_task_history.TaskParameter(***kwargs*)

Table to track luigi.Parameter()s of a Task.

A simple constructor that allows initialization from kwargs.

Sets attributes on the constructed instance using the names and
values in `kwargs`.

Only keys that are present as
attributes of the instance’s class are allowed. These could be,
for example, any mapped columns or relationships.

task_id

name

value

class luigi.db_task_history.TaskEvent(***kwargs*)

Table to track when a task is scheduled, starts, finishes, and fails.

A simple constructor that allows initialization from kwargs.

Sets attributes on the constructed instance using the names and
values in `kwargs`.

Only keys that are present as
attributes of the instance’s class are allowed. These could be,
for example, any mapped columns or relationships.

id

task_id

event_name

ts

class luigi.db_task_history.TaskRecord(***kwargs*)

Base table to track information about a luigi.Task.

References to other tables are available through task.events, task.parameters, etc.

A simple constructor that allows initialization from kwargs.

Sets attributes on the constructed instance using the names and
values in `kwargs`.

Only keys that are present as
attributes of the instance’s class are allowed. These could be,
for example, any mapped columns or relationships.

id

task_id

name

host

parameters

events