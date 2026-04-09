# luigi.execution_summary

This module provide the function `summary()` that is used for printing
an execution summary [https://github.com/spotify/luigi/blob/master/examples/execution_summary_example.py]
at the end of luigi invocations.

Functions

`summary`(worker)

Given a worker, return a human readable summary of what the worker have done.

Classes

`LuigiRunResult`(worker[, worker_add_run_status])

The result of a call to build/run when passing the detailed_summary=True argument.

`LuigiStatusCode`(*values)

All possible status codes for the attribute `status` in `LuigiRunResult` when the argument `detailed_summary=True` in *luigi.run() / luigi.build*.

`execution_summary`(*args, **kwargs)

class luigi.execution_summary.execution_summary(**args*, ***kwargs*)

summary_length

Parameter whose value is an `int`.

class luigi.execution_summary.LuigiStatusCode(**values*)

All possible status codes for the attribute `status` in `LuigiRunResult` when
the argument `detailed_summary=True` in *luigi.run() / luigi.build*.
Here are the codes and what they mean:

Status Code Name

Meaning

SUCCESS

There were no failed tasks or missing dependencies

SUCCESS_WITH_RETRY

There were failed tasks but they all succeeded in a retry

FAILED

There were failed tasks

FAILED_AND_SCHEDULING_FAILED

There were failed tasks and tasks whose scheduling failed

SCHEDULING_FAILED

There were tasks whose scheduling failed

NOT_RUN

There were tasks that were not granted run permission by the scheduler

MISSING_EXT

There were missing external dependencies

SUCCESS = (':)', 'there were no failed tasks or missing dependencies')

SUCCESS_WITH_RETRY = (':)', 'there were failed tasks but they all succeeded in a retry')

FAILED = (':(', 'there were failed tasks')

FAILED_AND_SCHEDULING_FAILED = (':(', 'there were failed tasks and tasks whose scheduling failed')

SCHEDULING_FAILED = (':(', 'there were tasks whose scheduling failed')

NOT_RUN = (':|', 'there were tasks that were not granted run permission by the scheduler')

MISSING_EXT = (':|', 'there were missing external dependencies')

class luigi.execution_summary.LuigiRunResult(*worker*, *worker_add_run_status=True*)

The result of a call to build/run when passing the detailed_summary=True argument.

Attributes:

- 

one_line_summary (str): One line summary of the progress.

- 

summary_text (str): Detailed summary of the progress.

- 

status (LuigiStatusCode): Luigi Status Code. See `LuigiStatusCode` for what these codes mean.

- 

worker (luigi.worker.worker): Worker object. See `worker`.

- 

scheduling_succeeded (bool): Boolean which is *True* if all the tasks were scheduled without errors.

luigi.execution_summary.summary(*worker*)

Given a worker, return a human readable summary of what the worker have
done.