# luigi.task_history

Abstract class for task history.
Currently the only subclass is `DbTaskHistory`.

Classes

`NopHistory`()

`StoredTask`(task, status[, host])

Interface for methods on TaskHistory

`TaskHistory`()

Abstract Base Class for updating the run history of a task

class luigi.task_history.StoredTask(*task*, *status*, *host=None*)

Interface for methods on TaskHistory

property task_family

property parameters

class luigi.task_history.TaskHistory

Abstract Base Class for updating the run history of a task

abstractmethod task_scheduled(*task*)

abstractmethod task_finished(*task*, *successful*)

abstractmethod task_started(*task*, *worker_host*)

class luigi.task_history.NopHistory

task_scheduled(*task*)

task_finished(*task*, *successful*)

task_started(*task*, *worker_host*)