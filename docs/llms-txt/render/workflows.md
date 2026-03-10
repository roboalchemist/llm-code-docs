# Source: https://render.com/docs/workflows.md

# Render Workflows — Rapidly spin up chains of long-running tasks on distributed compute.


> *Render Workflows is in public beta.*
>
> During the beta, bugs or changes in API/SDK behavior are possible as we continue refining the product. We welcome any and all feedback at *workflows-feedback@render.com*.

Use *Render Workflows* to rapidly distribute computational work across multiple independent instances:

<img src="../assets/images/docs/workflow-diagram.svg" width="95%" alt="Workflows overview" />

Workflows are perfect for use cases that benefit from high-performance, distributed execution, such as AI agents, ETL pipelines, and data processing.

## How it works

1. Using the Render SDK, you can mark functions in your code as *tasks*.

    **TypeScript**

    Here's minimal TypeScript for defining a task named `calculateSquare`. First import `task` from the SDK, then call it with an options object and your task function:

    ```typescript:index.ts
    import { task } from '@renderinc/sdk/workflows'

    const calculateSquare = task(
      { name: 'calculateSquare' },
      function calculateSquare(a: number): number {
        return a * a
      }
    )
    ```

    **Python**

    Here's minimal Python for defining a task named `calculate_square`. First initialize a `Workflows` app, then apply the `@app.task` decorator:

    ```python:main.py
    from render_sdk import Workflows

    app = Workflows()

    @app.task
    def calculate_square(a: int) -> int:
      return a * a

    if __name__ == "__main__":
      app.start()
    ```

2. In the Render Dashboard, you create a workflow service and link the repo containing your task definitions. Render automatically *registers* your defined tasks:

    [image: Viewing registered tasks in the Render Dashboard]

3. You can now trigger *runs* of your registered tasks from anywhere (web apps, agents, etc.) using the Render SDK or API.

    **TypeScript**

    Here's minimal TypeScript for triggering a run of `calculateSquare` and passing the argument `2`:

    ```typescript:client_app.ts
    import { Render } from '@renderinc/sdk'

    const render = new Render()
    const startedRun = await render.workflows.startTask(
      'my-workflow/calculateSquare',
      [2],
    )
    const finishedRun = await startedRun.get()
    console.log(finishedRun.results)
    ```

    **Python (async)**

    Here's minimal async Python for triggering a run of `calculate_square` and passing the argument `2`:

    ```python:client_app.py
    from render_sdk import RenderAsync

    render = RenderAsync()
    started_run = await render.workflows.start_task(
      "my-workflow/calculate_square",
      [2],
    )
    finished_run = await started_run
    print(finished_run.results)
    ```

    **Python (sync)**

    Here's minimal synchronous Python for triggering a run of `calculate_square` and passing the argument `2`:

    ```python:client_app.py
    from render_sdk import Render

    render = Render()
    finished_run = render.workflows.run_task(
      "my-workflow/calculate_square",
      [2],
    )
    print(finished_run.results)
    ```

4. Render spins up each triggered run in its own instance.
    - This usually takes less than a second.
5. A run can trigger _additional_ runs simply by calling the corresponding task function. This is called *run chaining*.

    **TypeScript**

    Below, the `sumSquares` task chains two parallel runs of `calculateSquare`:

    ```typescript:index.ts
    import { task } from '@renderinc/sdk/workflows'

    const calculateSquare = task(
      { name: 'calculateSquare' },
      function calculateSquare(a: number): number {
        return a * a
      }
    )

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

    **Python**

    Below, the `sum_squares` task chains two parallel runs of `calculate_square`:

    ```python:main.py
    from render_sdk import Workflows
    import asyncio

    app = Workflows()

    @app.task
    def calculate_square(a: int) -> int:
      return a * a

    @app.task
    async def sum_squares(a: int, b: int) -> int:
      result1, result2 = await asyncio.gather(
        calculate_square(a),
        calculate_square(b)
      )
      return result1 + result2
    ```

Runs execute alongside other Render service types, enabling fast and safe communication over your private network.

## Core features

| Feature | Description |
| --- | --- |
| *Automatic queuing and orchestration* | Render coordinates the entire task run lifecycle for you, from queuing to spin-up to deprovisioning. |
| *Long-running execution* | Each task run can execute for up to 24 hours. |
| *Configurable retry logic* | Define [retry behavior](/workflows-defining#retry-logic) for each task in the event of a failed run, with exponential backoff. |
| *Configurable timeout* | Specify a [timeout](/workflows-defining#timeout) for runs of each task, from 30 seconds to 24 hours. |
| *Configurable compute specs* | Specify which [instance type](/workflows-defining#instance-type-compute-specs) to use for runs of each task. |
| *Workflow-wide defaults* | Set the default retry logic, timeout, and instance type for all tasks in your workflow (and optionally override per task). |
| *Execution observability* | Track the progress and status of active and completed runs in the Render Dashboard. |
| *Outbound networking* | Runs can initiate network connections over both the public internet and your private network. Runs cannot receive _incoming_ network connections. |
| *Unified SDK* | Install a single lightweight SDK both to register tasks and to trigger runs from your code. 
> *The Render SDK is currently available for [TypeScript](/workflows-sdk-typescript) and [Python](/workflows-sdk-python).* SDKs for additional languages are planned for future releases.
 |

### Beta limitations

We'll address these limitations in future releases following beta:

- Workflows currently only support TypeScript and Python for defining tasks.
  - SDKs for other languages are planned for future releases.
- Workflows do not provide built-in support for automatically triggering runs on a schedule.
  - To schedule runs, you can create a [cron job](cronjobs) that runs your tasks on the desired schedule.
- If a workflow belongs to a [network-isolated environment](projects#blocking-cross-environment-traffic), its runs _cannot_ communicate with other services in that environment over its private network.
- Workflows do not yet support running tasks on [HIPAA-compliant](hipaa-compliance) hosts.
  - To prevent accidental PHI exposure, it is not currently possible to create new workflows in a HIPAA-enabled workspace.
  - If you enable HIPAA compliance for a workspace that already has workflows, *do not process PHI in your workflows.*

## Get started

Now that you know the basics, you're ready to [create your first workflow!](/workflows-tutorial)

## Billing

See [Limits and Pricing for Render Workflows](/workflows-limits).

## FAQ

###### How do I get started with Render Workflows?

Get started with [Your First Workflow](/workflows-tutorial).

###### Which languages can I use to define workflow tasks?

The Render SDK is available for [TypeScript](/workflows-sdk-typescript) and [Python](/workflows-sdk-python).

SDKs for additional languages are planned for future releases.

###### Can I trigger task runs without using the Render SDK?

*Yes.* For languages without Render SDK support, you can trigger runs by calling the Render API directly.

For details, see [Triggering Task Runs](/workflows-running).

###### Can my task runs receive incoming network connections?

*No.* Similar to background workers, task runs must initiate any required network connections.


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

###### instance

A virtual machine that runs your service's code on Render.

You can select from a range of *instance types* with different compute specs.

###### run chaining

Triggering a new *task run* by calling its function from an in-progress run.

All runs in a chain belong to the same *workflow*.

Related article: https://render.com/docs/workflows-defining.md

###### service type

When you deploy code on Render, you select a *service type* based on the capabilities you need.

For example, you create a *web service* to host a dynamic web app at a public URL.

Related article: https://render.com/docs/service-types.md

###### private network

Your Render services in the same *region* can reach each other without traversing the public internet, enabling faster and safer communication.

Related article: https://render.com/docs/private-network.md

###### background worker

Deploy this *service type* to continuously run code that does not receive incoming requests.

Ideal for processing jobs from a queue.

Related article: https://render.com/docs/background-workers.md