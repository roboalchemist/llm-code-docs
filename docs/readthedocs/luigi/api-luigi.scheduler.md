# luigi.scheduler

The system for scheduling tasks and executing them in order.
Deals with dependencies, priorities, resources, etc.
The `Worker` pulls tasks from the scheduler (usually over the REST interface) and executes them.
See Using the Central Scheduler for more info.

Functions

`rpc_method`(**request_args)

Classes

`OrderedSet`([iterable])

Standard Python OrderedSet recipe found at http://code.activestate.com/recipes/576694/

`RetryPolicy`(retry_count, ...)

Create new instance of RetryPolicy(retry_count, disable_hard_timeout, disable_window)

`Scheduler`([config, resources, task_history_impl])

Async scheduler that can handle multiple workers, etc.

`SimpleTaskState`(state_path)

Keep track of the current state and handle persistence.

`Task`(task_id, status, deps[, resources, ...])

`Worker`(worker_id[, last_active])

Structure for tracking worker activity and keeping their references.

`scheduler`(*args, **kwargs)

luigi.scheduler.UPSTREAM_SEVERITY_KEY(*value*, *start=0*, *stop=9223372036854775807*, */*)

Return first index of value.

Raises ValueError if the value is not present.

class luigi.scheduler.RetryPolicy(*retry_count*, *disable_hard_timeout*, *disable_window*)

Create new instance of RetryPolicy(retry_count, disable_hard_timeout, disable_window)

disable_hard_timeout

Alias for field number 1

disable_window

Alias for field number 2

retry_count

Alias for field number 0

luigi.scheduler.rpc_method(***request_args*)

class luigi.scheduler.scheduler(**args*, ***kwargs*)

retry_delay

Parameter whose value is a `float`.

remove_delay

Parameter whose value is a `float`.

worker_disconnect_delay

Parameter whose value is a `float`.

state_path

Parameter whose value is a `str`, and a base class for other parameter types.

Parameters are objects set on the Task class level to make it possible to parameterize tasks.
For instance:

```
class MyTask(luigi.Task):
    foo = luigi.Parameter()

class RequiringTask(luigi.Task):
    def requires(self):
        return MyTask(foo="hello")

    def run(self):
        print(self.requires().foo)  # prints "hello"

```