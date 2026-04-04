# Source: https://render.com/docs/workflows-local-development.md

# Local Dev with Render Workflows — Run tasks locally for faster development and testing.


> *Render Workflows is in public beta.*
>
> During the beta, bugs or changes in API/SDK behavior are possible as we continue refining the product. We welcome any and all feedback at *workflows-feedback@render.com*.

You can run workflow tasks on your local machine to iterate on them quickly. The Render CLI supports spinning up a *local task server* that simulates the entire run execution lifecycle. You can trigger task runs from your application code, or from the CLI itself.

As you iterate on your task definitions, the local task server picks up changes automatically. It also retains in-memory logs and results for each run (these are lost on server shutdown).

## Prerequisites

*Your development machine must have:*

- The Render CLI version 2.12.0 or later
  - [Install the Render CLI](cli#setup)
- A workflow project repo that defines and registers tasks
  - [Create your first workflow](/workflows-tutorial)

## Starting the task server

From your workflow project repo, run the following command:

```shell
render workflows dev -- <WORKFLOW_START_COMMAND>
```

Replace `<WORKFLOW_START_COMMAND>` with the command to start your workflow service, such as:

**TypeScript**

```shell
render workflows dev -- npm start
```

**Python**

```shell
render workflows dev -- python main.py
```

*Command not found?*

- Make sure you've [installed the Render CLI](cli#setup).
- Run `render --version` to confirm you're using version 2.12.0 or later.

Your local task server spins up and starts listening on port `8120`.

You can specify a different port with the `--port` option:

```shell
render workflows dev --port 8121 -- python main.py
```

## Triggering local task runs

### In application code

> *This section assumes you have an existing app that triggers task runs.*
>
> If you don't, first get set up with [Triggering Task Runs](/workflows-running).

You can configure your locally running apps to point to your local task server when triggering task runs. How you do this depends on whether your app uses the Render SDK or the Render API:

**Render SDK**

If your app uses the Render SDK (TypeScript or Python) to trigger task runs, set the following environment variable(s) to run tasks against your local task server:

```bash:.env
# Always set this:
RENDER_USE_LOCAL_DEV=true

# Also set this if you're using a non-default URL/port:
# RENDER_LOCAL_DEV_URL=http://localhost:8121
```

**Render API**

If your app uses the Render API directly to run tasks, swap out the base URL you use for task-related endpoints with your local task server's URL.

Here's a Node.js example:

```js
const TASKS_BASE_URL = process.env.RENDER_TASKS_URL || 'https://api.render.com'
```

In this example, you would set the `RENDER_TASKS_URL` environment variable to your local task server URL (e.g., `http://localhost:8120`) to use it for development.

Note that the local task server _only_ simulates task-related endpoints. Other Render API endpoints are not supported.

### In the Render CLI

**Interactive mode**

1. With your [local task server running](#starting-the-task-server), run the following command:

   ```shell
   render workflows tasks list --local
   ```

   *Don't forget the `--local` flag!* Otherwise, the CLI lists tasks from your deployed workflow services.

   The CLI opens an interactive menu of your locally registered tasks:

   [image: Listing tasks in the Render CLI]

2. Select a task and press *Enter*, then select the `run` command.

   The CLI prompts you to provide the task's input arguments as a JSON array:

   [image: Providing input arguments for a task run in the Render CLI]

   If your task takes zero arguments, provide an empty list, `[]`.

3. Provide your desired arguments and press *Enter*. The CLI kicks off your task with a request to your local task server and begins tailing its logs.

   You can remain in this view to view live logs from your task run.

4. Press *Esc* to navigate back up to the list of commands for your task. This time select the `runs` command.

   The CLI opens an interactive menu of the task's local runs:

   [image: Viewing task runs in the Render CLI]

5. Select a run and press *Enter*, then select the `results` command.

   The CLI opens a view of the run's results:

   [image: Viewing task run details in the Render CLI]

**Non-interactive mode**

In non-interactive environments, provide any of `-o text`, `-o json`, or `-o yaml` to Render CLI commands to disable menu navigation and receive output in the desired format.

The example commands below use `-o text`:

1. With your [local task server running](#starting-the-task-server), run the following command to list your locally registered tasks:

   ```shell{outputLines:2-5}
   render workflows tasks list -o text --local
   NAME               ID                          CREATED                      
   calculateSquare    tsk-d6kba95mo5j36bpg8rs0    2026-03-04T14:41:40-08:00    
   sumSquares         tsk-d6kba95mo5j36bpg8rsg    2026-03-04T14:41:40-08:00    
   flipCoin           tsk-d6kba95mo5j36bpg8rt0    2026-03-04T14:41:40-08:00
   ```

   *Don't forget the `--local` flag for all of these commands!* Otherwise, the CLI runs them against your deployed workflow services.

2. Start a run for that task, passing input as a JSON array:

   ```shell{outputLines:2}
   render workflows tasks start calculateSquare -o text --input='[3]' --local
   Created task run trn-d6kchpdmo5j36bpg8rvg for calculateSquare
   ```

3. List runs for the task:

   ```shell{outputLines:2-3}
   render workflows runs list calculateSquare -o text --local
   ID                          STATUS       STARTED                      COMPLETED                    DURATION     
   trn-d6kchpdmo5j36bpg8rvg    completed    2026-03-04T16:05:57-08:00    2026-03-04T16:05:57-08:00    364.577ms
   ```

4. Fetch details and results for a run by its ID:

   ```shell{outputLines:2-4}
   render workflows runs show calculateSquare -o text --local
   Task run details for trn-d6kchpdmo5j36bpg8rvg: status completed, started at 2026-03-04 16:05:57.371701 -0800 PST, completed at 2026-03-04 16:05:57.736278 -0800 PST,
   input: [3],
   results: [9]
   ```

## Local-only considerations

- Logs and results for local task runs are stored in memory by the local task server.
  - This data is lost when the server shuts down.
  - This data is retained indefinitely as long as the server is running. This can lead to high memory usage over time.
  - If you trigger a high volume of local task runs, we recommend periodically restarting your local task server to free up memory.
- Identifiers for local tasks and runs are randomly generated IDs.
  - The identifier for a given task differs each time you run the local task server.
  - Local identifiers do not correspond to any values in your deployed workflow services.

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