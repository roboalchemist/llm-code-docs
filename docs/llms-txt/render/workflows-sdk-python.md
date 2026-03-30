# Source: https://render.com/docs/workflows-sdk-python.md

# Workflows SDK for Python — Usage and symbol reference



> *Render Workflows is in public beta.*
>
> During the beta, bugs or changes in API/SDK behavior are possible as we continue refining the product. We welcome any and all feedback at *workflows-feedback@render.com*.

The Render SDK for Python provides support for:

- Defining workflow tasks
- Triggering runs of those tasks from your other Python code

When triggering runs, you use different classes for [asynchronous](#triggering-runs-async) and [synchronous](#triggering-runs-sync) execution contexts.

## Install

From your Python project directory:

```shell
pip install render_sdk
```

*If you already have the SDK installed,* make sure you're using version `0.6.0` or later:

```shell
pip install --upgrade render_sdk
```

After installing, make sure to add `render_sdk>=0.6.0` as a dependency in your application's `requirements.txt`, `pyproject.toml`, or equivalent.

## Defining tasks

The following symbols pertain to creating and registering tasks in your workflow service. For guidance on how to use them, see [Defining Workflow Tasks](/workflows-defining).

### The `Workflows` class

Handles defining and registering workflow tasks. Initialize this in each file where you define tasks.

#### Initializing

###### `Workflows(default_retry, default_timeout, default_plan)`

Initializes a new `Workflows` object. All arguments are optional.

```python
from render_sdk import Workflows, Retry

# Basic initialization
app = Workflows()

# Initialization with all options set
app = Workflows(
  default_retry=Retry(
    max_retries=3,
    wait_duration_ms=1000,
    backoff_scaling=1.5
  ),
  default_timeout=300,
  default_plan="standard"
)
```

------

###### Argument

`default_retry`

###### Description

A `Retry` object defining default retry behavior for all tasks in this workflow. Individual tasks can [override this](/workflows-defining#retry-logic).

---

###### Argument

`default_timeout`

###### Description

The default timeout (in seconds) for all tasks in this workflow. Individual tasks can [override this](/workflows-defining#timeout).

---

###### Argument

`default_plan`

###### Description

The default instance type to use for all tasks in this workflow. Individual task definitions can [override this](/workflows-defining#instance-type-compute-specs). The following instance types are available for all workspaces:

- `starter` (0.5 CPU / 512 MB RAM)
- `standard` (1 CPU / 2 GB RAM)
- `pro` (2 CPU / 4 GB RAM)

You can request access to the following larger instance types for your workspace:

- `pro_plus` (4 CPU / 8 GB RAM)
- `pro_max` (8 CPU / 16 GB RAM)
- `pro_ultra` (16 CPU / 32 GB RAM)

The default value is `standard`.

------

###### `Workflows.from_workflows(*apps, default_retry, default_timeout, default_plan)`

Initializes a new `Workflows` object that incorporates tasks from one or more _other_ `Workflows` objects.

Use this in your workflow's entry point file if you [import task definitions from other files](/workflows-defining#organizing-tasks):

```python
from render_sdk import Workflows
from math_tasks import app as math_app
from text_tasks import app as text_app

app = Workflows.from_workflows(math_app, text_app)

if __name__ == "__main__":
  app.start()
```

If you set any defaults with this method (such as `default_timeout`), those defaults apply _only_ to tasks registered directly on _this_ object (not to tasks registered on the imported objects).

| Argument | Description |
| --- | --- |
| `*apps` | *Required.* One or more `Workflows` objects to incorporate into this object. If two objects define a task with the same name, this raises a `ValueError`. |
| `default_retry` | Default retry configuration for new tasks registered on the combined object. Same as the [`Workflows` constructor](#workflows) argument. |
| `default_timeout` | Default timeout for new tasks registered on the combined object. Same as the [`Workflows` constructor](#workflows) argument. |
| `default_plan` | Default instance type for new tasks registered on the combined object. Same as the [`Workflows` constructor](#workflows) argument. |

### The `@app.task` decorator

You apply the `@app.task` decorator to a Python function to register it as a workflow task. For details, see [Defining Workflow Tasks](/workflows-defining)

#### Minimal example

```python
from render_sdk import Workflows # highlight-line

app = Workflows() # highlight-line

@app.task # highlight-line
def calculate_square(a: int) -> int:
  return a * a
```

#### Example with all arguments

```python
from render_sdk import Workflows, Retry

app = Workflows()

@app.task(
  name="calc_square", # Give the task a custom name (defaults to function name)
  retry=Retry( # Define default retry logic for the task
    max_retries=3, # Retry up to 3 times (i.e., 4 total attempts)
    wait_duration_ms=1000, # Set a base retry delay of 1 second
    backoff_scaling=1.5 # Increase delay by 50% after each retry (exponential backoff)
  ),
  timeout_seconds=300, # Timeout in seconds
  plan="standard" # Resource plan
)
def calculate_square(a: int) -> int:
  return a * a
```

#### Argument reference

------

###### *Task decorator arguments*

---

###### Option

`name`

###### Description

A custom name for the task. This affects the task's *slug*, which you use to reference the task when [triggering runs](/workflows-running#3-initialize-the-client-and-trigger-a-run). If omitted, defaults to the name of the decorated function.

---

###### Option

`retry`

###### Description

A `Retry` object defining retry behavior for the task. See retry arguments below.

---

###### Option

`timeout_seconds`

###### Description

The timeout for the task's runs, in seconds. Must be between 30 seconds (`30`) and 24 hours (`86400`), inclusive. The default value is 2 hours.

---

###### Option

`plan`

###### Description

The default instance type to use for the task's runs. *Supported values:*

- `starter` (0.5 CPU / 512 MB RAM)
- `standard` (1 CPU / 2 GB RAM)
- `pro` (2 CPU / 4 GB RAM)

You can request access to the following larger instance types for your workspace:

- `pro_plus` (4 CPU / 8 GB RAM)
- `pro_max` (8 CPU / 16 GB RAM)
- `pro_ultra` (16 CPU / 32 GB RAM)

The default value is `standard`.

---

###### *Retry arguments*

---

###### Option

`max_retries`

###### Description

The maximum number of retries to attempt for a given run of the task. The total number of attempts is up to `max_retries + 1` (the initial attempt plus all retries).

---

###### Option

`wait_duration_ms`

###### Description

The base delay before attempting the first retry, in milliseconds.

---

###### Option

`backoff_scaling`

###### Description

The exponential backoff factor. After each retry, the previous delay is multiplied by this factor. For example, a factor of `1.5` increases the delay by 50% after each retry.

- If you provide a `Retry` object but omit this field, the default value is `1.5`.
- If you omit the `Retry` object entirely, the default value is `2`.

------

### The `app.start()` method

The `app.start()` method serves as the entry point for your workflow during both task registration and run execution. Your workflow definition must call this method as part of startup:

```python:main.py
from render_sdk import Workflows

app = Workflows()

@app.task
def calculate_square(a: int) -> int:
  return a * a

if __name__ == "__main__":
  app.start() # highlight-line
```

This method takes no arguments.

## Triggering runs (async)

### The `RenderAsync` class

Use the `RenderAsync` class to trigger and manage task runs from any asynchronous execution context (such as a FastAPI route handler). All methods are async and return `await`able objects.

#### Constructor

###### `RenderAsync(token)`

Initializes a new `RenderAsync` object. All arguments are optional.

```python
from render_sdk import RenderAsync

# Basic initialization
render = RenderAsync()

# Initialization with API key
render = RenderAsync(
  token="rnd_abc123…"
)
```

| Argument | Description |
| --- | --- |
| `token` | The [API key](api#1-create-an-api-key) to use for authentication. If omitted, the client automatically detects and uses the value of the `RENDER_API_KEY` environment variable. |

### Task methods (async)

These methods are available on the `workflows` attribute of the `RenderAsync` class.

###### `async start_task(task_identifier, input_data)`

Kicks off a run of the registered task with the specified identifier, passing the specified arguments.

To instead run a task _and_ wait for it to complete, use [`workflows.run_task`](#async-run-task).

*On success:* Returns an [`AwaitableTaskRun`](#the-awaitabletaskrun-class) object representing the initial state of the task run. You can `await` this object to wait for the run to complete.

*Raises:* [`ClientError`](#clienterror), [`ServerError`](#servererror), [`TimeoutError`](#timeouterror)

```python
# Execute the calculate_square task with an input of 2
started_task_run = await render.workflows.start_task(
  "my-workflow/calculate_square",
  [2]
)

task_run_id = started_task_run.id # ID is available immediately
task_run_status = started_task_run.status # Initial status is available immediately

finished_task_run = await started_task_run # Other properties become available after the task run completes
print(finished_task_run.results) # Prints the task run's result, in this case [4]
```

------

###### Argument

`task_identifier`

###### Description

*Required.* The *slug* indicating the task to run, available from your task's page in the [Render Dashboard](https://dashboard.render.com):  [image: Task slug in the Render Dashboard]  Always has the format `{workflow-slug}/{task-name}` (e.g., `my-workflow/calculate_square`).

---

###### Argument

`input_data`

###### Description

*Required.* A list or dictionary containing the task's [input arguments.](/workflows-defining#task-arguments):

- *If you provide a list,* elements are positional based on the task's function signature.
- *If you provide a dictionary,* each key maps to a parameter name in the task's function signature.

For a task that takes zero arguments, provide an empty list, `[]`.

------

###### `async run_task(task_identifier, input_data)`

Starts the registered task with the specified identifier, waits for it to complete, and returns the result.

To instead kick off a run _without_ waiting for it to complete, use [`workflows.start_task`](#async-start-task).

*On success:* Returns a [`TaskRunDetails`](#the-taskrundetails-class) object for the completed task run.

*Raises:* [`ClientError`](#clienterror), [`ServerError`](#servererror), [`TimeoutError`](#timeouterror), [`TaskRunError`](#taskrunerror)

```python
# Run the calculate_square task and wait for the result
task_run = await render.workflows.run_task(
  "my-workflow/calculate_square",
  [2]
)
print(task_run.results) # [4]
```

------

###### Argument

`task_identifier`

###### Description

*Required.* The *slug* indicating the task to run, available from your task's page in the [Render Dashboard](https://dashboard.render.com):  [image: Task slug in the Render Dashboard]  Always has the format `{workflow-slug}/{task-name}` (e.g., `my-workflow/calculate_square`).

---

###### Argument

`input_data`

###### Description

*Required.* A list or dictionary containing the task's [input arguments.](/workflows-defining#task-arguments):

- *If you provide a list,* elements are positional based on the task's function signature.
- *If you provide a dictionary,* each key maps to a parameter name in the task's function signature.

For a task that takes zero arguments, provide an empty list, `[]`.

------

###### `async list_task_runs(params)`

Lists task runs that match optional filters specified in the provided `ListTaskRunsParams` object.

*On success:* Returns a list of `TaskRun` objects.

*Raises:* [`ClientError`](#clienterror), [`ServerError`](#servererror), [`TimeoutError`](#timeouterror)

```python
from render_sdk.client.types import ListTaskRunsParams

params = ListTaskRunsParams(
  limit=10, # Return up to 10 runs
  cursor="cfQ74cE2sDI=", # Start from this cursor
  owner_id=["tea-d3jm7ai4d50c73fale60"] # Limit to these workspace IDs
)

await render.workflows.list_task_runs(params)
```

Supported fields of the `ListTaskRunsParams` object include:

| Parameter | Description |
| --- | --- |
| `limit` | An integer specifying the maximum number of task runs to return. |
| `cursor` | A cursor string for pagination. Use this to retrieve the next page of results. |
| `owner_id` | A list of workspace IDs to filter results by. Only task runs from these workspaces will be returned. |

###### `async get_task_run(task_run_id)`

Retrieves the details of the task run with the specified ID.

*On success:* Returns a [`TaskRunDetails`](#the-taskrundetails-class) object.

*Raises:* [`ClientError`](#clienterror), [`ServerError`](#servererror), [`TimeoutError`](#timeouterror)

```python
await render.workflows.get_task_run("trn-abc123")
```

| Argument | Description |
| --- | --- |
| `task_run_id` | *Required.* The ID of the task run to retrieve. Has the format `trn-abc123...` |

###### `async cancel_task_run(task_run_id)`

Cancels the task run with the specified ID. This raises a [`ClientError`](#clienterror) if the task run is not found, or if it isn't currently running.

*On success:* Returns `None`.

*Raises:* [`ClientError`](#clienterror), [`ServerError`](#servererror), [`TimeoutError`](#timeouterror)

```python
await render.workflows.cancel_task_run("trn-abc123")
```

| Argument | Description |
| --- | --- |
| `task_run_id` | *Required.* The ID of the task run to cancel. Has the format `trn-abc123...` |

###### `async task_run_events(task_run_ids)`

Streams completion events for one or more task runs via [Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) (SSE). Returns an async iterator that yields a [`TaskRunDetails`](#the-taskrundetails-class) object each time a specified task run completes or fails.

The connection stays open until all events are received or you `break` out of the loop.

*Raises:* [`ClientError`](#clienterror), [`ServerError`](#servererror), [`TimeoutError`](#timeouterror)

```python
# Start multiple tasks
run1 = await render.workflows.start_task("my-workflow/add", [1, 2])
run2 = await render.workflows.start_task("my-workflow/add", [5, 8])

# Stream events until all runs complete
pending = {run1.id, run2.id}
async for event in render.workflows.task_run_events(list(pending)):
  print(f"Run {event.id}: status={event.status}")
  pending.discard(event.id)
  if not pending:
    break
```

| Argument | Description |
| --- | --- |
| `task_run_ids` | *Required.* A list of task run IDs to stream events for. Each ID has the format `trn-abc123...` |

### The `AwaitableTaskRun` class

Represents the initial state of a task run as returned by the async [`workflows.start_task`](#async-start-task) method.

You can `await` this object to wait for the task run to complete. On success, it returns a [`TaskRunDetails`](#the-taskrundetails-class) object:

```python
started_task_run = await render.workflows.start_task(
  "my-workflow/calculate_square",
  [2]
)
finished_task_run = await started_task_run # highlight-line
```

*If the task run fails,* this `await` raises a [`TaskRunError`](#taskrunerror) exception.

#### Properties

| Property | Description |
| --- | --- |
| `id` | The ID of the task run. Has the format `trn-abc123...` |
| `status` | The initial status of the task run. This is usually `pending`. |

## Triggering runs (sync)

### The `Render` class

Use the `Render` class in any synchronous execution context (such as a default Flask or Django app). All methods are blocking.

#### Constructor

###### `Render(token)`

Initializes a new `Render` object. All arguments are optional.

```python
from render_sdk import Render

# Basic initialization
render = Render()

# Initialization with API key
render = Render(
  token="rnd_abc123…"
)
```

| Argument | Description |
| --- | --- |
| `token` | The [API key](api#1-create-an-api-key) to use for authentication. If omitted, the client automatically detects and uses the value of the `RENDER_API_KEY` environment variable. |

### Task methods (sync)

These methods are available on the `workflows` attribute of the `Render` class.

###### `start_task(task_identifier, input_data)`

Runs the registered task with the specified identifier, passing the specified arguments.

To instead run a task _and_ wait for it to complete, use [`workflows.run_task`](#run-task).

*On success:* Returns a `TaskRun` object representing the initial state of the task run (e.g. `id`, `status`). To wait for completion, poll [`workflows.get_task_run`](#get-task-run) or use [`workflows.run_task`](#run-task).

*Raises:* [`ClientError`](#clienterror), [`ServerError`](#servererror), [`TimeoutError`](#timeouterror)

```python
started_task_run = render.workflows.start_task(
  "my-workflow/calculate_square",
  [2]
)
# Poll with get_task_run(started_task_run.id) or use run_task() to block until done
```

| Argument | Description |
| --- | --- |
| `task_identifier` | *Required.* The *slug* indicating the task to run. Format: `{workflow-slug}/{task-name}` (e.g. `my-workflow/calculate_square`). |
| `input_data` | *Required.* A list or dictionary containing the task's [input arguments.](/workflows-defining#task-arguments) For zero arguments, use `[]`. |

###### `run_task(task_identifier, input_data)`

Starts the task, waits for it to complete, and returns the result.

To instead kick off a run _without_ waiting for it to complete, use [`workflows.start_task`](#start-task).

*On success:* Returns a [`TaskRunDetails`](#the-taskrundetails-class) object.

*Raises:* [`ClientError`](#clienterror), [`ServerError`](#servererror), [`TimeoutError`](#timeouterror), [`TaskRunError`](#taskrunerror)

```python
task_run = render.workflows.run_task("my-workflow/calculate_square", [2])
print(task_run.results)
```

| Argument | Description |
| --- | --- |
| `task_identifier` | *Required.* The *slug* indicating the task to run. Format: `{workflow-slug}/{task-name}`. |
| `input_data` | *Required.* A list or dictionary containing the task's [input arguments.](/workflows-defining#task-arguments) For zero arguments, use `[]`. |

###### `list_task_runs(params)`

Lists task runs that match optional filters.

*On success:* Returns a list of `TaskRun` objects.

*Raises:* [`ClientError`](#clienterror), [`ServerError`](#servererror), [`TimeoutError`](#timeouterror)

```python
from render_sdk.client.types import ListTaskRunsParams
params = ListTaskRunsParams(limit=10, cursor="…", owner_id=["tea-…"])
render.workflows.list_task_runs(params)
```

Supported fields: `limit`, `cursor`, `owner_id`. See [`workflows.list_task_runs`](#list-task-runs) for parameter descriptions.

###### `get_task_run(task_run_id)`

Retrieves the details of the task run with the specified ID.

*On success:* Returns a [`TaskRunDetails`](#the-taskrundetails-class) object.

*Raises:* [`ClientError`](#clienterror), [`ServerError`](#servererror), [`TimeoutError`](#timeouterror)

```python
render.workflows.get_task_run("trn-abc123")
```

| Argument | Description |
| --- | --- |
| `task_run_id` | *Required.* The ID of the task run (format `trn-abc123...`). |

###### `cancel_task_run(task_run_id)`

Cancels the task run. Raises [`ClientError`](#clienterror) if not found or not running.

*On success:* Returns `None`.

*Raises:* [`ClientError`](#clienterror), [`ServerError`](#servererror), [`TimeoutError`](#timeouterror)

```python
render.workflows.cancel_task_run("trn-abc123")
```

| Argument | Description |
| --- | --- |
| `task_run_id` | *Required.* The ID of the task run to cancel (format `trn-abc123...`). |

###### `task_run_events(task_run_ids)`

Streams completion events via SSE. Returns a synchronous iterator that yields a [`TaskRunDetails`](#the-taskrundetails-class) object each time a specified task run completes or fails.

*Raises:* [`ClientError`](#clienterror), [`ServerError`](#servererror), [`TimeoutError`](#timeouterror)

```python
for event in render.workflows.task_run_events(["trn-abc123"]):
  print(f"Run {event.id}: status={event.status}")
```

| Argument | Description |
| --- | --- |
| `task_run_ids` | *Required.* List of task run IDs (format `trn-abc123...`). |

## Additional types

### The `TaskRun` class

Summarizes the state of a task run. Obtained in one of the following ways:
- From the sync [`workflows.start_task`](#start-task) method
- Calling the `workflows.list_task_runs` method (sync or async)

To get a run's full details including results, call `workflows.get_task_run` (sync or async) and provide the run's ID to obtain a [`TaskRunDetails`](#the-taskrundetails-class) object.

#### Properties

| Property | Description |
| --- | --- |
| `id` | The ID of the task run. Has the format `trn-abc123...` |
| `task_id` | The ID of the run's associated task. Has the format `tsk-abc123...` |
| `status` | The initial status of the task run. This is usually `pending`. |
| `parent_task_run_id` | The ID of this run's parent run, if this run was chained. For a root-level run, this value is the root run's ID or empty. |
| `root_task_run_id` | The ID of the root task run in this run's execution chain. For a root-level run, this value matches `id`. |
| `retries` | The number of times the task run has retried so far. For a newly started run, this is typically `0`. |
| `attempts` | A list of `TaskAttempt` objects representing each execution attempt so far (including retries). |
| `started_at` | The datetime when the task run started executing. Not present if `status` is `pending`. |
| `completed_at` | The datetime when the task run finished (successfully or otherwise). Present only if status is one of `completed`, `failed`, or `canceled`. |

### The `TaskRunDetails` class

Provides the full details of a task run. Obtained in one of the following ways:

- `await`ing an [`AwaitableTaskRun`](#the-awaitabletaskrun-class) object returned by the async [`workflows.start_task`](#async-start-task) method:

  ```python
  started_task_run = await render.workflows.start_task(
    "my-workflow/calculate_square",
    [2]
  )
  finished_task_run = await started_task_run # highlight-line
  ```

- Calling the `workflows.run_task` method of the `Render` or `RenderAsync` class:

  ```python
  task_run_details = await render.workflows.run_task("my-workflow/calculate_square", [2])
  ```

- Calling the `workflows.get_task_run` method of the `Render` or `RenderAsync` class:

  ```python
  task_run_details = await render.workflows.get_task_run("trn-abc123")
  ```

- Iterating over events from the `workflows.task_run_events` method of the `Render` or `RenderAsync` class:

  ```python
  async for event in render.workflows.task_run_events(["trn-abc123"]):
    task_run_details = event
  ```

#### Properties

*A `TaskRunDetails` object includes all of the same properties as a [`TaskRun`](#the-taskrun-class) object, plus:*

| Property | Description |
| --- | --- |
| `results` | A list containing the task's return value(s). This value is always an empty list if `status` is not `completed`. |
| `input_` | The argument values that were passed to the task run, in the same format they were provided (as a list or a dictionary). Note the trailing underscore (`_`) in this property name. |
| `error` | The error message if the task run failed. Present only if `status` is `failed`. |
| `attempts` | A list of `TaskAttemptDetails` objects (more detailed than the `TaskAttempt` list on [`TaskRun`](#the-taskrun-class)) representing each individual execution attempt for this run, including retries. |

### Exception types

Exceptions raised by the SDK have one of the types listed below. `RenderError` is the parent class for all other exception types.

```python
from render_sdk.client.errors import (
    RenderError, # Parent class for other exceptions
    ClientError,
    RateLimitError,
    ServerError,
    TimeoutError,
    TaskRunError
)
```

------

###### Exception

`RenderError`

###### Description

The base class for all exceptions raised by the SDK.

---

###### Exception

`ClientError`

###### Description

Raised when a request to the Render API returns a 400-level error code. Common causes include:

- Invalid API key
- Invalid task identifier
- Invalid task arguments
- Invalid action (e.g., canceling a task run that is already completed)

---

###### Exception

`RateLimitError`

###### Description

A subclass of `ClientError`. Raised when a request to the Render API returns a 429 (rate limit exceeded) error code.

---

###### Exception

`ServerError`

###### Description

Raised when a request to the Render API returns a 500-level error code.

---

###### Exception

`TimeoutError`

###### Description

Raised when a request to the Render API times out.

---

###### Exception

`TaskRunError`

###### Description

Raised when a task run fails (e.g. when `await`ing an [`AwaitableTaskRun`](#the-awaitabletaskrun-class) or when calling [`workflows.run_task`](#run-task) or sync [`workflows.run_task`](#run-task)).

------


---

##### Appendix: Glossary definitions

###### task

A function you can execute on its own compute as part of a *workflow*.

Each execution of a task is called a *run*.

Related article: https://render.com/docs/workflows-defining.md

###### run

A single execution of a workflow *task*.

A run spins up in its own *instance*, executes, returns a value, and is deprovisioned.

Related article: https://render.com/docs/workflows-running.md

###### instance type

Specifies the RAM and CPU available to your service's *instances*.

Common instance types for a new web service include:

- *Free*: 512 MB RAM / 0.1 CPU
- *Starter*: 512 MB RAM / 0.5 CPU
- *Standard*: 2 GB RAM / 1 CPU

For the full list, see the [pricing page](/pricing#services).

###### run chaining

Triggering a new *task run* by calling its function from an in-progress run.

All runs in a chain belong to the same *workflow*.

Related article: https://render.com/docs/workflows-defining.md