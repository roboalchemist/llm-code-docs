# Source: https://render.com/docs/workflows-running.md

# Triggering Task Runs — Kick off runs of registered workflow tasks.


> *Render Workflows is in public beta.*
>
> During the beta, bugs or changes in API/SDK behavior are possible as we continue refining the product. We welcome any and all feedback at *workflows-feedback@render.com*.

After you [create a workflow](/workflows-tutorial) and register tasks, you can start triggering runs of those tasks from your own apps and agents.

You can also [manually trigger runs](#running-manually) in the Render Dashboard and CLI to help with testing and debugging.

## First: Create an API key

*Triggering task runs from code requires a Render API key.*

Create an API key with [these steps](api#1-create-an-api-key), then return here.

## Running with the Render SDK

> *The Render SDK is currently available for TypeScript and Python.*
>
> SDKs for additional languages are planned for future releases. To execute tasks from other languages, [use the Render API](#running-with-the-render-api).

Follow these steps to execute task runs from your code using the Render SDK.

### 1. Install the SDK

**TypeScript**

From your TypeScript project directory:

```shell
npm install @renderinc/sdk
```

(Or `pnpm install`, `bun add`, etc.)

*If you already have the SDK installed,* make sure you're using version `^0.5.0` or later:

```shell
npm install @renderinc/sdk@latest
```

After installing, make sure `@renderinc/sdk` is listed as a dependency in your `package.json` file at version `^0.5.0` or later.

**Python**

From your Python project directory:

```shell
pip install render_sdk
```

*If you already have the SDK installed,* make sure you're using version `0.6.0` or later:

```shell
pip install --upgrade render_sdk
```

After installing, make sure to add `render_sdk>=0.6.0` as a dependency in your application's `requirements.txt`, `pyproject.toml`, or equivalent.

### 2. Set your API key

In your application's environment, set the `RENDER_API_KEY` environment variable to your [API key](#first-create-an-api-key):

```bash
export RENDER_API_KEY=rnd_abc123…
```

The SDK client automatically detects and uses the value of this environment variable.

Alternatively, you can provide your API key explicitly when initializing the client (see the SDK reference for your language).

### 3. Initialize the client and trigger a run

**TypeScript**

The following code demonstrates initializing the SDK client, triggering a task run, and waiting for the run to complete. See below for more details.

```typescript:basic_task_runner.ts
import { Render } from '@renderinc/sdk'

async function triggerTaskRun() {
  // Initialize the client
  const render = new Render()

  // Kick off a task run
  const startedRun = await render.workflows.startTask(
    'my-workflow/calculate_square',
    [2]
  )

  console.log('Task run started:', startedRun.taskRunId)

  // Wait for run to complete
  const finishedRun = await startedRun.get()

  console.log('Task run completed:', finishedRun.id)
  console.log('Final status:', finishedRun.status)
}

triggerTaskRun()
```

You trigger a task run by calling the client's `workflows.startTask` method. This method takes the following arguments:

| Argument | Description |
| --- | --- |
| `taskIdentifier` | The *slug* indicating the task to run, available from your task's page in the [Render Dashboard](https://dashboard.render.com): [image: Task slug in the Render Dashboard] Every task slug has the following format: ```
{workflow-slug}/{task-name}
``` For example: `my-workflow/calculate_square` |
| `inputData` | An array containing the task's input arguments. Elements are positional based on the task's function signature. The `calculate_square` task in the example above takes a single integer argument, provided as the single element of an array. For tasks that take zero arguments, provide an empty array, `[]`. |

The `workflows.startTask` method returns a `TaskRunResult` as soon as the run is created. This object provides the run's `taskRunId` immediately. You can call `await result.get()` to wait for the run to complete and obtain the full task run details (including `status` and `results`).

For full options and details, see the [TypeScript SDK reference](/workflows-sdk-typescript#starttask).

**Python (async)**

> Use this method in *asynchronous* execution contexts (such as FastAPI route handlers).

The following code demonstrates initializing the async SDK client, triggering a task run, and waiting for the run to complete. See below for more details.

```python:basic_task_runner.py
from render_sdk import RenderAsync
import asyncio

async def trigger_task_run():

  # Initialize the async client
  render = RenderAsync()

  # Kick off a task run
  started_run = await render.workflows.start_task(
    "my-workflow/calculate_square",
    [2]
  )

  print(f"Task run started: {started_run.id}")
  print(f"Initial status: {started_run.status}")

  # Wait for run to complete
  finished_run = await started_run

  print(f"Task run completed: {finished_run.id}")
  print(f"Final status: {finished_run.status}")

if __name__ == "__main__":
  asyncio.run(trigger_task_run())
```

You trigger a task run by calling the async client's [`workflows.start_task`](/workflows-sdk-python#async-start-task) method. This method takes the following arguments:

------

###### Argument

`task_identifier`

###### Description

The *slug* indicating the task to run, available from your task's page in the [Render Dashboard](https://dashboard.render.com): [image: Task slug in the Render Dashboard] Every task slug has the following format: ```
{workflow-slug}/{task-name}
``` For example: `my-workflow/calculate_square`

---

###### Argument

`input_data`

###### Description

A list or dictionary containing the task's input arguments:

- *If you provide a list,* elements are positional based on the task's function signature.
- *If you provide a dictionary,* each key maps to a parameter name in the task's function signature.

The `calculate_square` task in the example above takes a single integer argument, provided as the single element of a list. For tasks that take zero arguments, provide an empty list, `[]`.

------

The `workflows.start_task` method returns an [`AwaitableTaskRun`](/workflows-sdk-python#the-awaitabletaskrun-class) object as soon as the run is created. This object provides the run's `id` and initial `status`, which are both available immediately. You can `await` this object to wait for the run to complete, at which point all other properties are available.

For full options and details, see the [Python SDK reference](/workflows-sdk-python#async-start-task).

**Python (sync)**

> Use this method in *synchronous* execution contexts (such as a default Flask or Django app).

The following code demonstrates initializing the synchronous SDK client, triggering a task run, and waiting for the run to complete. See below for more details.

```python:basic_task_runner.py
import time
from render_sdk import Render

def trigger_task_run():

  # Initialize the client
  render = Render()

  # Kick off a task run
  started_run = render.workflows.start_task(
    "my-workflow/calculate_square",
    [2]
  )

  print(f"Task run started: {started_run.id}")
  print(f"Initial status: {started_run.status}")

  # Wait for run to complete (poll until terminal status)
  finished_run = render.workflows.get_task_run(started_run.id)
  while finished_run.status.value not in ("completed", "failed", "canceled"):
    time.sleep(1)
    finished_run = render.workflows.get_task_run(started_run.id)

  print(f"Task run completed: {finished_run.id}")
  print(f"Final status: {finished_run.status}")

if __name__ == "__main__":
  trigger_task_run()
```

You trigger a task run by calling the synchronous client's [`workflows.start_task`](/workflows-sdk-python#start-task) method. This method takes the following arguments:

------

###### Argument

`task_identifier`

###### Description

The *slug* indicating the task to run, available from your task's page in the [Render Dashboard](https://dashboard.render.com): [image: Task slug in the Render Dashboard] Every task slug has the following format: ```
{workflow-slug}/{task-name}
``` For example: `my-workflow/calculate_square`

---

###### Argument

`input_data`

###### Description

A list or dictionary containing the task's input arguments:

- *If you provide a list,* elements are positional based on the task's function signature.
- *If you provide a dictionary,* each key maps to a parameter name in the task's function signature.

The `calculate_square` task in the example above takes a single integer argument, provided as the single element of a list. For tasks that take zero arguments, provide an empty list, `[]`.

------

The `workflows.start_task` method returns a [`TaskRun`](/workflows-sdk-python#the-taskrun-class) object as soon as the run is created. This object provides the run's `id` and initial `status`, which are both available immediately.

To wait for the run to complete, you can poll [`workflows.get_task_run`](/workflows-sdk-python#get-task-run) until the run's status is one of `completed`, `failed`, or `canceled`. You can also use [`workflows.run_task`](/workflows-sdk-python#run-task) instead of `start_task` to start _and_ wait in one blocking call.

For full options and details, see the [Python SDK reference](/workflows-sdk-python#start-task).

## Running with the Render API

The [Render API](api) provides an endpoint for triggering task runs, along with a variety of endpoints for retrieving workflow and task run details. The Render SDK uses the Render API behind the scenes, and you can also use it directly from your own code.

Start a task run by sending a POST request to the [Run task](https://api-docs.render.com/reference/createtask/) endpoint. The JSON body for this request includes two properties:

```json
{
  "task": "my-workflow/calculate_square",
  "input": [2]
}
```

------

###### Property

`task`

###### Description

*Required.* An identifier specifying the task to run. You can provide either of two identifiers, both of which are available from your task's page in the [Render Dashboard](https://dashboard.render.com):  [image: Task slug in the Render Dashboard] 

- The task's *slug*
  - This has the format `{workflow-slug}/{task-name}` (for example, `my-workflow/calculate_square`)
- The task's *ID*
  - This has the format `tsk-abc123...`

---

###### Property

`input`

###### Description

*Required.* An array or object containing values for the task's [input arguments.](/workflows-defining#task-arguments):

- *If you provide an array,* elements are positional based on the task's function signature.
- *If you provide an object,* each key maps to a parameter name in the task's function signature.

For a task that takes zero arguments, provide an empty list, `[]`.

------

## Running manually

You can manually trigger task runs directly from the Render Dashboard and CLI. This is handy for testing and debugging new tasks.

**Dashboard**

#### Running tasks manually in the Render Dashboard

1. From your workflow's *Tasks* page in the [Render Dashboard](https://dashboard.render.com), click a task to open its *Runs* page.

2. Click *Start Task* in the top-right corner of the page:

   [image: Running a task in the Render Dashboard]

   A dialog appears for providing the task's input arguments:

   [image: Providing input arguments for a task run in the Render Dashboard]

3. Provide the task's input arguments as a JSON array. Each array element maps to the task's corresponding positional argument.

   For example, you can provide `[5]` for a task that takes a single integer argument, or `[]` for a task that takes zero arguments.

   You can click *Format* and *Validate* to cleanly structure your input and confirm that it's valid JSON.

4. Click *Start task*.

   Your new task run appears at the top of the *Runs* table.

**CLI**

#### Running manually with the Render CLI

1. Make sure your development machine has version 2.12.0 or later of the Render CLI:

   ```shell{outputLines:2}
   render --version
   render version 2.12.0
   ```

   If it doesn't, [install the latest version](cli#setup).

2. Run the following command:

   ```shell
   render workflows tasks list
   ```

   The CLI opens an interactive menu of all workflow tasks in your workspace:

   [image: Listing tasks in the Render CLI]

3. Select a task and press *Enter*, then select the `run` command.

   The CLI prompts you to provide the task's input arguments as a JSON array:

   [image: Providing input arguments for a task run in the Render CLI]

4. Provide your desired arguments (or `[]` for a task that takes zero arguments) and press *Enter*. The CLI kicks off your task with a request to the Render API and begins tailing its logs.

   You can remain in this view to view live logs from your task run.

5. Press *Esc* to navigate back up to the list of commands for your task. This time select the `runs` command.

   The CLI opens an interactive menu of the task's runs:

   [image: Viewing task runs in the Render CLI]

6. Select a run and press *Enter*, then select the `results` command.

   The CLI opens a view of the run's results:

   [image: Viewing task run details in the Render CLI]



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