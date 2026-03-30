# Source: https://render.com/docs/workflows-defining.md

# Defining Workflow Tasks — Specify units of work to run on Render.


> *Render Workflows is in public beta.*
>
> During the beta, bugs or changes in API/SDK behavior are possible as we continue refining the product. We welcome any and all feedback at *workflows-feedback@render.com*.

After you [create your first workflow](/workflows-tutorial), you can start defining your own tasks. This article describes supported syntax and configuration options.

## First: Install the Render SDK

> *The Render SDK is currently available for TypeScript and Python.*
>
> SDKs for additional languages are planned for future releases.

The Render SDK is required to define and register workflow tasks.

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

## Basic example

Let's start with a "minimum viable workflow" that defines a single task:

**TypeScript**

```typescript:index.ts
import { task } from '@renderinc/sdk/workflows'

const calculateSquare = task(
  { name: 'calculateSquare' },
  function calculateSquare(a: number): number {
    return a * a
  }
)
```

This includes everything required to define a workflow:

1. We import the `task` function from the Render SDK.
2. We call `task(...)` to register a function (`calculateSquare`) as a task.
    - You can provide optional arguments to configure timeout, retry logic, and more. For details, see [Task-level config.](#task-level-config)

**Python**

```python:main.py
from render_sdk import Workflows

app = Workflows()

@app.task
def calculate_square(a: int) -> int:
  return a * a

if __name__ == "__main__":
  app.start()
```

This includes everything required to define a workflow:

1. We import the `Workflows` class from the Render SDK and initialize it as `app`.
2. We apply the `@app.task` decorator to a function (`calculate_square`) to mark it as a task.
    - This decorator accepts a number of optional arguments. For details, see [Task-level config.](#task-level-config)
3. We call `app.start()` in our code's entry point.
    - On Render, this is what kicks off the task registration process _and_ the execution of each run.

## Organizing tasks

You can define your workflow's tasks across multiple files in your project repo:

**TypeScript**

```typescript:math-tasks.ts
import { task } from '@renderinc/sdk/workflows'

export const add = task(
  { name: 'add' },
  function add(a: number, b: number): number {
    return a + b
  }
)
```

```typescript:text-tasks.ts
import { task } from '@renderinc/sdk/workflows'

export const capitalize = task(
  { name: 'capitalize' },
  function capitalize(s: string): string {
    return s.toUpperCase()
  }
)
```

```typescript:index.ts
import './math-tasks'
import './text-tasks'
```

In this example, task definitions are distributed across two files: `math-tasks.ts` and `text-tasks.ts`. By setting your workflow's start command to run the JS output of `index.ts`, you ensure that all tasks are imported and registered.

**Python**

```python:math_tasks.py
from render_sdk import Workflows

app = Workflows()

@app.task
def add(a: int, b: int) -> int:
  return a + b
```

```python:text_tasks.py
from render_sdk import Workflows

app = Workflows()

@app.task
def capitalize(s: str) -> str:
  return s.upper()
```

```python:main.py
from render_sdk import Workflows
from math_tasks import app as math_app
from text_tasks import app as text_app

app = Workflows.from_workflows(math_app, text_app) # highlight-line

if __name__ == "__main__":
  app.start() # SDK entry point
```

In this example, task definitions are distributed across two files: `math_tasks.py` and `text_tasks.py`.

To register all of your tasks, your workflow's entry point (commonly `main.py`) imports and incorporates the `Workflows` apps from each other file using the [`Workflows.from_workflows()`](/workflows-sdk-python#workflowsfrom-workflows) method.

## Task arguments

*A task function can define any number of arguments.* This example task takes three arguments of different types:

**TypeScript**

```typescript
const myTask = task(
  { name: 'myTask' },
  function myTask(a: number, b: string, c: boolean): number {
    // ...
  }
)
```

**Python**

```python
@app.task
def my_task(arg1: int, arg2: str, arg3: bool) -> int:
  # ...
```

*Argument and return types must be JSON-serializable.* Your applications provide task arguments in a JSON array or object via the Render API. A task's result is also returned as JSON.

Both the TypeScript and Python SDKs support setting default argument values:

**TypeScript**

```typescript
const myTask = task(
  { name: 'myTask' },
  function myTask(arg1: number = 3): number {
    // ...
  }
)
```

**Python**

```python
@app.task
def my_task(arg1: int = 3) -> int:
  # ...
```

## Task-level config

### Instance type (compute specs)

By default, task runs execute on Render's *Standard* instance type (1 CPU, 2GB RAM). You can override this on a per-task basis.

Set a task's instance type with the following syntax:

**TypeScript**

```typescript
const myTask = task(
  { 
    name: 'myTask',
    plan: 'starter' // highlight-line
  },
  function myTask(a: number): number {
    return a * a
  }
)
```

**Python**

```python
@app.task(
  plan="starter" # highlight-line
)
def my_task(a: int) -> int:
  return a * a
```

The following instance types are supported for all workspaces:

| Instance Type | Specs |
| --- | --- |
| *`starter`* | 0.5 CPU 512 MB RAM |
| *`standard`* (default) | 1 CPU 2 GB RAM |
| *`pro`* | 2 CPU 4 GB RAM |

If you have more resource-intensive workloads, you can request access to the following larger instance types:

| Instance Type | Specs |
| --- | --- |
| *`pro_plus`* | 4 CPU 8 GB RAM |
| *`pro_max`* | 8 CPU 16 GB RAM |
| *`pro_ultra`* | 16 CPU 32 GB RAM |

See [pricing details.](/workflows-limits#instance-types-compute-specs)

### Timeout

By default, task runs time out after 2 hours. You can override this on a per-task basis to any value between *30 seconds* and *24 hours*.

**TypeScript**

Provide your task's timeout to `task(...)` via the `timeoutSeconds` option:

```typescript
const myTask = task(
  {
    name: 'myTask',
    timeoutSeconds: 86400 // 24 hours in seconds
  },
  function myTask(a: number): number {
    return a * a
  }
)
```

**Python**

Provide your task's timeout to the `@app.task` decorator via the `timeout_seconds` argument:

```python
@app.task(
  timeout_seconds=86400 # 24 hours in seconds
)
def my_task(a: int) -> int:
  return a * a
```

### Retry logic

Task runs can automatically *retry* if they fail. A run is considered to have failed if its function raises an exception or throws an error instead of returning a value.

Retries are useful for tasks that might be affected by transient failures, such as network errors or timeouts.

#### Default retry behavior

By default, task runs use the following retry logic:

- Retry up to 3 times (i.e., 4 total attempts)
- Wait 1 second before attempting the first retry
- Double the wait time after each retry (i.e., one second, two seconds, four seconds)

#### Customizing retries

You can customize retry behavior on a per-task basis. Every run of a task uses the same retry settings.

Provide retry settings with the following syntax:

**TypeScript**

```typescript{6-10}
import { task } from '@renderinc/sdk/workflows'

const flipCoin = task(
  {
    name: 'flipCoin',
    retry: {
      maxRetries: 3, // Retry up to 3 times (i.e., 4 total attempts)
      waitDurationMs: 1000, // Set a base retry delay of 1 second
      backoffScaling: 1.5 // Increase delay by 50% after each retry (1s, 1.5s, 2.25s)
    }
  },
  function flipCoin(): string {
    if (Math.random() < 0.5) {
      throw new Error('Flipped tails! Retrying.')
    }
    return 'Flipped heads!'
  }
)
```

**Python**

```python{1,7-11}
from render_sdk import Workflows, Retry
import random

app = Workflows()

@app.task(
  retry=Retry(
    max_retries=3, # Retry up to 3 times (i.e., 4 total attempts)
    wait_duration_ms=1000, # Set a base retry delay of 1 second
    backoff_scaling=1.5 # Increase delay by 50% after each retry (1s, 1.5s, 2.25s)
  )
)
def flip_coin() -> str:
  if random.random() < 0.5:
    raise Exception("Flipped tails! Retrying.")
  return "Flipped heads!"
```

This contrived example defines a task that "flips a coin" and raises an exception/error when it "flips tails", causing the run to fail and retry according to its settings.

## Chaining task runs

A task run can trigger _additional_ task runs. Like other runs, these *chained runs* each execute in their own instance.

<img src="../assets/images/docs/workflow-diagram.svg" width="100%" alt="Workflows overview" />

> *When should I chain runs?*
>
> Chaining is most helpful when different parts of a larger job benefit from long-running, individually provisioned compute.
>
> For simple jobs (such as the very basic example below), it's more efficient to define the entirety of your logic in a single task.

### Example

**TypeScript**

The simple `sumSquares` task below chains two parallel runs of the `calculateSquare` task:

```typescript:math-tasks.ts
import { task } from '@renderinc/sdk/workflows'

const calculateSquare = task(
  { name: 'calculateSquare' },
  function calculateSquare(a: number): number {
    return a * a
  }
)

// A task that chains two parallel runs
const sumSquares = task(
  { name: 'sumSquares' },
  async function sumSquares(a: number, b: number): Promise<number> {
    const [result1, result2] = await Promise.all([
      calculateSquare(a),
      calculateSquare(b)
    ])
    return result1 + result2
  }
)
```

*When chaining runs:*

- In most cases, your chaining task's function should be defined as `async`.
  - Otherwise, it can't `await` the results of its chained runs.
- You chain a run by calling the corresponding task function (e.g., `calculateSquare` above).
  - *However,* this call doesn't return the function's defined return value!
  - *Instead,* this triggers a new run and returns a Promise.
  - As shown, you can `await` this result to obtain the run's _actual_ return value.

**Python**

The simple `sum_squares` task below chains two parallel runs of the `calculate_square` task:

```python:math_tasks.py
from render_sdk import Workflows
import asyncio

app = Workflows()

# A task that chains two parallel runs
@app.task
async def sum_squares(a: int, b: int) -> int: # Must be async to await chained runs
  result1, result2 = await asyncio.gather(
    calculate_square(a),
    calculate_square(b)
  )
  return result1 + result2

@app.task
def calculate_square(a: int) -> int:
  return a * a
```

*When chaining runs:*

- In most cases, your chaining task's function should be defined as `async`.
  - Otherwise, it can't `await` the results of its chained runs.
- You chain a run by calling the corresponding task function (e.g., `calculate_square` above).
  - *However,* this call doesn't return the function's defined return value!
  - *Instead,* this triggers a new run and returns a special `TaskInstance` object.
  - As shown, you can `await` this object to obtain the run's _actual_ return value.

Task functions _can_ call other functions that are _not_ marked as tasks. These functions execute and return as normal (they do not trigger chained runs).

> *Need to run a task defined in a _different_ workflow?*
>
> This requires instead using the Render SDK or Render API, as described in [Running Workflow Tasks](/workflows-running). Note that this is not tracked as a chaining relationship when visualizing task execution in the [Render Dashboard](https://dashboard.render.com).

### Parallel runs

When chaining runs, you'll often want to chain multiple at once to distribute independent work. Common examples include processing batches of images or analyzing different sections of a large data set.

**TypeScript**

To chain parallel runs in TypeScript, use `Promise.all`, `Promise.allSettled`, or a similar concurrency utility.

In this example, the `processPhotoUpload` task chains a separate `processImage` run for each element in its `imageUrls` argument:

```typescript
import { task } from '@renderinc/sdk/workflows'

const processImage = task(
  { name: 'processImage' },
  function processImage(imageUrl: string): {
    url: string
    thumbnailUrl: string
    success: boolean
  } {
    // Image processing logic goes here
    return {
      url: imageUrl,
      thumbnailUrl: `${imageUrl}_thumb.jpg`,
      success: true
    }
  }
)

const processPhotoUpload = task(
  { name: 'processPhotoUpload' },
  async function processPhotoUpload(imageUrls: string[]): Promise<{
    total: number
    processed: number
    failed: number
    results: Array<{ url: string; thumbnailUrl: string; success: boolean }>
  }> {
    // Process all images in parallel by chaining a run for each
    const results = await Promise.all( // highlight-line
      imageUrls.map((url) => processImage(url)) // highlight-line
    ) // highlight-line

    const numSuccessful = results.filter((r) => r.success).length
    const numFailed = results.length - numSuccessful

    return {
      total: imageUrls.length,
      processed: numSuccessful,
      failed: numFailed,
      results
    }
  }
)
```

*If you don't use `Promise.all` or a similar function, chained runs execute serially.*

For example:

```typescript{4-6}
const sumSquaresSlower = task(
  { name: 'sumSquaresSlower' },
  async function sumSquaresSlower(a: number, b: number): Promise<number> {
    // ⚠️ Not parallel!
    const result1 = await calculateSquare(a)
    const result2 = await calculateSquare(b) // Executes after first run completes
    return result1 + result2
  }
)

const calculateSquare = task(
  { name: 'calculateSquare' },
  function calculateSquare(a: number): number {
    return a * a
  }
)
```

**Python**

To chain parallel runs in Python, use `asyncio.gather`, `asyncio.TaskGroup`, or a similar concurrency utility.

In this example, the `process_photo_upload` task chains a separate `process_image` run for each element in its `image_urls` argument:

```python
from render_sdk import Workflows
import asyncio

app = Workflows()

@app.task
async def process_photo_upload(image_urls: list[str]) -> dict:
  # Process all images in parallel by chaining a run for each
  results = await asyncio.gather( # highlight-line
    *[process_image(url) for url in image_urls] # highlight-line
  ) # highlight-line

  num_successful = sum(1 for r in results if r["success"])
  num_failed = len(results) - num_successful

  return {
    "total": len(image_urls),
    "processed": num_successful,
    "failed": num_failed,
    "results": results
  }

@app.task
def process_image(image_url: str) -> dict:

  # Image processing logic goes here

  return {
    "url": image_url,
    "thumbnail_url": f"{image_url}_thumb.jpg",
    "success": True
  }
```

*If you don't use `asyncio.gather` or a similar function, chained runs execute serially.*

For example:

```python{3-5}
@app.task
async def sum_squares_slower(a: int, b: int) -> int:
  # ⚠️ Not parallel!
  result1 = await calculate_square(a)
  result2 = await calculate_square(b) # Executes after first run completes
  return result1 + result2

@app.task
def calculate_square(a: int) -> int:
  return a * a
```

Serial execution _is_ helpful when one run depends on the result of another. However, it can significantly slow execution for runs that are completely independent. *Parallelize wherever your use case allows.*

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

###### instance

A virtual machine that runs your service's code on Render.

You can select from a range of *instance types* with different compute specs.